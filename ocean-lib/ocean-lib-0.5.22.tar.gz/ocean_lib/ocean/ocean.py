#
# Copyright 2021 Ocean Protocol Foundation
# SPDX-License-Identifier: Apache-2.0
#

"""Ocean module."""
import logging
import os

from eth_utils import remove_0x_prefix
from ocean_lib.config import Config
from ocean_lib.config_provider import ConfigProvider
from ocean_lib.data_provider.data_service_provider import DataServiceProvider
from ocean_lib.enforce_typing_shim import enforce_types_shim
from ocean_lib.models.data_token import DataToken
from ocean_lib.models.dtfactory import DTFactory
from ocean_lib.models.fixed_rate_exchange import FixedRateExchange
from ocean_lib.models.metadata import MetadataContract
from ocean_lib.models.order import Order
from ocean_lib.ocean.env_constants import ENV_CONFIG_FILE
from ocean_lib.ocean.ocean_assets import OceanAssets
from ocean_lib.ocean.ocean_compute import OceanCompute
from ocean_lib.ocean.ocean_exchange import OceanExchange
from ocean_lib.ocean.ocean_pool import OceanPool
from ocean_lib.ocean.ocean_services import OceanServices
from ocean_lib.ocean.util import (
    from_base_18,
    get_bfactory_address,
    get_contracts_addresses,
    get_ocean_token_address,
    get_web3_connection_provider,
    to_base_18,
)
from ocean_lib.web3_internal.contract_handler import ContractHandler
from ocean_lib.web3_internal.utils import get_network_name
from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.web3_internal.web3_provider import Web3Provider
from web3.datastructures import AttributeDict

logger = logging.getLogger("ocean")


@enforce_types_shim
class Ocean:

    """The Ocean class is the entry point into Ocean Protocol."""

    def __init__(self, config=None, data_provider=None):
        """Initialize Ocean class.

        Usage: Make a new Ocean instance

        `ocean = Ocean({...})`

        This class provides the main top-level functions in ocean protocol:
        1. Publish assets metadata and associated services
            - Each asset is assigned a unique DID and a DID Document (DDO)
            - The DDO contains the asset's services including the metadata
            - The DID is registered on-chain with a URL of the metadata store
              to retrieve the DDO from

            `asset = ocean.assets.create(metadata, publisher_wallet)`

        2. Discover/Search assets via the current configured metadata store (Aquarius)

            - Usage:
            `assets_list = ocean.assets.search('search text')`

        An instance of Ocean is parameterized by a `Config` instance.

        :param config: `Config` instance
        :param data_provider: `DataServiceProvider` instance
        """
        # Configuration information for the market is stored in the Config class
        # config = Config(filename=config_file, options_dict=config_dict)
        if not config:
            try:
                config = ConfigProvider.get_config()
            except AssertionError:
                config = Config(os.getenv(ENV_CONFIG_FILE))
                ConfigProvider.set_config(config)
        if isinstance(config, dict):
            # fallback to metadataStoreUri
            cache_key = (
                "metadataCacheUri"
                if ("metadataCacheUri" in config)
                else "metadataStoreUri"
            )
            metadata_cache_uri = config.get(
                cache_key, config.get("metadata_cache_uri", "http://localhost:5000")
            )
            config_dict = {
                "eth-network": {"network": config.get("network", "")},
                "resources": {
                    "metadata_cache_uri": metadata_cache_uri,
                    "provider.url": config.get("providerUri", "http://localhost:8030"),
                },
            }
            config = Config(options_dict=config_dict)
        ConfigProvider.set_config(config)
        self._config = config
        ContractHandler.set_artifacts_path(self._config.artifacts_path)
        Web3Provider.init_web3(
            provider=get_web3_connection_provider(self._config.network_url)
        )

        self._web3 = Web3Provider.get_web3()

        if not data_provider:
            data_provider = DataServiceProvider

        network = get_network_name()
        addresses = get_contracts_addresses(network, self._config)
        self.assets = OceanAssets(
            self._config, data_provider, addresses.get(MetadataContract.CONTRACT_NAME)
        )
        self.services = OceanServices()
        self.compute = OceanCompute(self._config, data_provider)

        ocean_address = get_ocean_token_address(network)
        self.pool = OceanPool(ocean_address, get_bfactory_address(network))
        self.exchange = OceanExchange(
            ocean_address,
            FixedRateExchange.configured_address(
                network or get_network_name(), ConfigProvider.get_config().address_file
            ),
            self.config,
        )

        logger.debug("Ocean instance initialized: ")

    @property
    def config(self):
        """
        `Config` stores artifact path, urls.
        """
        return self._config

    @property
    def web3(self):
        return self._web3

    @property
    def OCEAN_address(self):
        return get_ocean_token_address(get_network_name())

    def create_data_token(
        self,
        name: str,
        symbol: str,
        from_wallet: Wallet,
        cap: float = DataToken.DEFAULT_CAP,
        blob: str = "",
    ) -> DataToken:
        """
        This method deploys a datatoken contract on the blockchain.

        Usage:
        ```python
            config = Config('config.ini')
            ocean = Ocean(config)
            wallet = Wallet(ocean.web3, private_key=private_key)
            datatoken = ocean.create_data_token("Dataset name", "dtsymbol", from_wallet=wallet)
        ```

        :param name: Datatoken name, str
        :param symbol: Datatoken symbol, str
        :param from_wallet: wallet instance, wallet
        :param cap: float

        :return: `Datatoken` instance
        """

        dtfactory = self.get_dtfactory()
        tx_id = dtfactory.createToken(
            blob, name, symbol, to_base_18(cap), from_wallet=from_wallet
        )
        address = dtfactory.get_token_address(tx_id)
        assert address, "new datatoken has no address"
        dt = DataToken(address)
        return dt

    def get_data_token(self, token_address: str) -> DataToken:
        """
        :param token_address: Token contract address, str
        :return: `Datatoken` instance
        """

        return DataToken(token_address)

    def get_dtfactory(self, dtfactory_address: str = "") -> DTFactory:
        dtf_address = dtfactory_address or DTFactory.configured_address(
            get_network_name(), self._config.address_file
        )
        """
        :param dtfactory_address: contract address, str

        :return: `DTFactory` instance
        """
        return DTFactory(dtf_address)

    def get_user_orders(self, address, datatoken=None, service_id=None):
        """
        :return: List of orders `[Order]`
        """
        dt = DataToken(datatoken)
        _orders = []
        for log in dt.get_start_order_logs(
            self._web3, address, from_all_tokens=not bool(datatoken)
        ):
            a = dict(log.args.items())
            a["amount"] = from_base_18(int(log.args.amount))
            a["marketFee"] = from_base_18(int(log.args.marketFee))
            a = AttributeDict(a.items())

            # 'datatoken', 'amount', 'timestamp', 'transactionId', 'did', 'payer', 'consumer', 'serviceId', 'serviceType'
            order = Order(
                log.address,
                a.amount,
                a.timestamp,
                log.transactionHash,
                f"did:op:{remove_0x_prefix(log.address)}",
                a.payer,
                a.consumer,
                a.serviceId,
                None,
            )
            if service_id is None or order.serviceId == service_id:
                _orders.append(order)

        return _orders
