from __future__ import annotations

import asyncio
import enum
import os
import sys
import time
import uuid
import warnings
from asyncio import wait_for
from typing import (
    Awaitable,
    Callable,
    Dict,
    Generic,
    Optional,
    TypeVar,
    Union,
    cast,
    overload,
)

import aiobotocore
import boto3
import botocore
import dask
import dask.distributed
import distributed.deploy
from distributed.core import Status
from rich.text import Text
from typing_extensions import Literal

from .compatibility import DISTRIBUTED_VERSION
from .core import Async, Cloud, IsAsynchronous, Sync
from .utils import name_exists_in_dict, parse_identifier, rich_console


@enum.unique
class CredentialsPreferred(enum.Enum):
    LOCAL = "local"
    # USER = 'user'
    ACCOUNT = "account"
    NONE = None


_T = TypeVar("_T")


class Cluster(distributed.deploy.Cluster, Generic[IsAsynchronous]):
    """Create a Dask cluster with Coiled

    Parameters
    ----------
    n_workers
        Number of workers in this cluster. Defaults to 4.
    configuration
        Name of cluster configuration to create cluster from.
        If not specified, defaults to ``coiled/default`` for the
        current Python version.
    name
        Name to use for identifying this cluster. Defaults to ``None``.
    software
        Identifier of the software environment to use, in the format (<account>/)<name>. If the software environment
        is owned by the same account as that passed into "account", the (<account>/) prefix is optional.

        For example, suppose your account is "wondercorp", but your friends at "friendlycorp" have an environment
        named "xgboost" that you want to use; you can specify this with "friendlycorp/xgboost". If you simply
        entered "xgboost", this is shorthand for "wondercorp/xgboost".

        The "name" portion of (<account>/)<name> can only contain ASCII letters, hyphens and underscores.
    worker_cpu
        Number of CPUs allocated for each worker. Defaults to 2.
    worker_gpu
        Number of GPUs allocated for each worker. Defaults to 0 (no GPU support). Note that this will _always_
        allocate GPU-enabled workers, so is expensive.
    worker_memory
        Amount of memory to allocate for each worker. Defaults to 8 GiB.
    worker_class
        Worker class to use. Defaults to "dask.distributed.Nanny".
    worker_options
        Mapping with keyword arguments to pass to ``worker_class``. Defaults to ``{}``.
    scheduler_cpu
        Number of CPUs allocated for the scheduler. Defaults to 1.
    scheduler_memory
        Amount of memory to allocate for the scheduler. Defaults to 4 GiB.
    scheduler_class
        Scheduler class to use. Defaults to "dask.distributed.Scheduler".
    scheduler_options
        Mapping with keyword arguments to pass to ``scheduler_class``. Defaults to ``{}``.
    asynchronous
        Set to True if using this Cloud within ``async``/``await`` functions or
        within Tornado ``gen.coroutines``. Otherwise this should remain
        ``False`` for normal use. Default is ``False``.
    cloud
        Cloud object to use for interacting with Coiled.
    account
        Name of Coiled account to use. If not provided, will
        default to the user account for the ``cloud`` object being used.
    shutdown_on_close
        Whether or not to shut down the cluster when it finishes.
        Defaults to True, unless name points to an existing cluster.
    backend_options
        Dictionary of backend specific options (e.g. ``{'region': 'us-east-2'}``). Any options
        specified with this keyword argument will take precedence over those stored in the
        ``coiled.backend-options`` cofiguration value.
    credentials
        Which credentials to use for Dask operations and forward to Dask clusters --
        options are "account", "local", or "none". The default behavior is to prefer
        credentials associated with the Coiled Account, if available, then try to
        use local credentials, if available.
        NOTE: credential handling currently only works with AWS credentials.
    timeout
        Timeout in seconds to wait for a cluster to start, will use ``default_cluster_timeout``
        set on parent Cloud by default.
    """

    @overload
    def __init__(
        self: Cluster[Sync],
        name: Optional[str] = None,
        *,
        n_workers: int = 4,
        configuration: str = None,
        software: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: str = None,
        worker_class: str = None,
        worker_options: dict = None,
        scheduler_cpu: int = None,
        scheduler_memory: str = None,
        scheduler_class: str = None,
        scheduler_options: dict = None,
        asynchronous: Sync = False,
        cloud: Literal[None] = None,
        account: str = None,
        shutdown_on_close=None,
        backend_options: Optional[Dict] = None,
        credentials: Optional[str] = "account",
        timeout: Optional[int] = None,
    ):
        ...

    @overload
    def __init__(
        self: Cluster[Sync],
        name: Optional[str] = None,
        *,
        n_workers: int = 4,
        configuration: str = None,
        software: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: str = None,
        worker_class: str = None,
        worker_options: dict = None,
        scheduler_cpu: int = None,
        scheduler_memory: str = None,
        scheduler_class: str = None,
        scheduler_options: dict = None,
        asynchronous: bool = False,
        cloud: Cloud[Sync],
        account: str = None,
        shutdown_on_close=None,
        backend_options: Optional[Dict] = None,
        credentials: Optional[str] = "account",
        timeout: Optional[int] = None,
    ):
        ...

    @overload
    def __init__(
        self: Cluster[Async],
        name: Optional[str] = None,
        *,
        n_workers: int = 4,
        configuration: str = None,
        software: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: str = None,
        worker_class: str = None,
        worker_options: dict = None,
        scheduler_cpu: int = None,
        scheduler_memory: str = None,
        scheduler_class: str = None,
        scheduler_options: dict = None,
        asynchronous: Async = True,
        cloud: Literal[None] = None,
        account: str = None,
        shutdown_on_close=None,
        backend_options: Optional[Dict] = None,
        credentials: Optional[str] = "account",
        timeout: Optional[int] = None,
    ):
        ...

    @overload
    def __init__(
        self: Cluster[Async],
        name: Optional[str] = None,
        *,
        n_workers: int = 4,
        configuration: str = None,
        software: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: str = None,
        worker_class: str = None,
        worker_options: dict = None,
        scheduler_cpu: int = None,
        scheduler_memory: str = None,
        scheduler_class: str = None,
        scheduler_options: dict = None,
        asynchronous: bool = False,
        cloud: Cloud[Async],
        account: str = None,
        shutdown_on_close=None,
        backend_options: Optional[Dict] = None,
        credentials: Optional[str] = "account",
        timeout: Optional[int] = None,
    ):
        ...

    def __init__(
        self,
        name: Optional[str] = None,
        *,
        n_workers: int = 4,
        configuration: str = None,
        software: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: str = None,
        worker_class: str = None,
        worker_options: dict = None,
        scheduler_cpu: int = None,
        scheduler_memory: str = None,
        scheduler_class: str = None,
        scheduler_options: dict = None,
        asynchronous: bool = False,
        cloud: Cloud = None,
        account: str = None,
        shutdown_on_close=None,
        backend_options: Optional[Dict] = None,
        credentials: Optional[str] = "account",
        timeout: Optional[int] = None,
    ):
        # Determine consistent sync/async
        if cloud and asynchronous is not None and cloud.asynchronous != asynchronous:
            warnings.warn(
                f"Requested a Cluster with asynchronous={asynchronous}, but "
                f"cloud.asynchronous={cloud.asynchronous}, so the cluster will be"
                f"{cloud.asynchronous}"
            )
            asynchronous = cloud.asynchronous

        # we really need to call this first before any of the below code errors
        # out; otherwise because of the fact that this object inherits from
        # deploy.Cloud __del__ (and perhaps __repr__) will have AttributeErrors
        # because the gc will run and attributes like `.status` and
        # `.scheduler_comm` will not have been assigned to the object's instance
        # yet
        super().__init__(asynchronous)

        self.cloud: Cloud[IsAsynchronous] = cloud or Cloud.current(
            asynchronous=asynchronous
        )
        self.timeout = (
            timeout if timeout is None else self.cloud.default_cluster_timeout
        )
        if configuration is None:
            v = "".join(map(str, sys.version_info[:2]))
            configuration = f"coiled/default-py{v}"
        self.configuration = configuration
        self.software = software
        self.worker_cpu = worker_cpu
        self.worker_gpu = worker_gpu
        self.worker_memory = worker_memory
        self.worker_class = worker_class
        self.worker_options = worker_options
        self.scheduler_cpu = scheduler_cpu
        self.scheduler_memory = scheduler_memory
        self.scheduler_class = scheduler_class
        self.scheduler_options = scheduler_options
        self.name = name
        self.account = account
        self._start_n_workers = n_workers
        self._lock = None
        self._asynchronous = asynchronous
        self.shutdown_on_close = shutdown_on_close
        self.backend_options = {
            **(dask.config.get("coiled.backend-options", None) or {}),
            **(backend_options or {}),
        }
        self.credentials = CredentialsPreferred(credentials)
        self.cluster_id: Optional[int] = None

        self._name = "coiled.Cluster"  # Used in Dask's Cluster._ipython_display_
        if not self.asynchronous:
            self.sync(self._start)

    @property
    def loop(self):
        return self.cloud.loop

    @overload
    def sync(
        self: Cluster[Sync],
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: Union[Sync, Literal[None]] = None,
        callback_timeout=None,
        **kwargs,
    ) -> _T:
        ...

    @overload
    def sync(
        self: Cluster[Async],
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: Union[bool, Literal[None]] = None,
        callback_timeout=None,
        **kwargs,
    ) -> Awaitable[_T]:
        ...

    def sync(
        self,
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: bool = None,
        callback_timeout=None,
        **kwargs,
    ) -> Union[_T, Awaitable[_T]]:
        return super().sync(
            func,
            *args,
            asynchronous=asynchronous,
            callback_timeout=callback_timeout,
            **kwargs,
        )

    async def _start(self):
        console = rich_console()
        with console.status(
            Text(
                "Creating Cluster. This might take a few minutes...", style="bold green"
            )
        ):
            # When invoked using distributed.utils.sync, sub-invocations are all async.
            # As long as we are in a private API that is always called that way,
            # we should be able to safely cast this to async.
            cloud = cast(Cloud[Async], self.cloud)
            self.cloud = await cloud
            should_create = True
            available_configs = None

            if self.name:
                try:
                    self.cluster_id = await cloud._get_cluster_by_name(
                        name=self.name,
                        account=self.account,
                    )
                except Exception:
                    # if there's no such cluster, we'll get an Exception
                    pass
                else:
                    console.print(
                        f"Using existing cluster: '{self.name}'"
                    )  # TODO: add timer
                    should_create = False
                    if self.shutdown_on_close is None:
                        self.shutdown_on_close = False

            self.name = self.name or cloud.user + "-" + str(uuid.uuid4())[:10]

            if should_create:

                # TODO: should this check also be upstream on the server?
                software_env = await self._check_software_environment_exists(cloud)
                available_configs = await self._check_cluster_configuration_exists(
                    cloud,
                    software_env,
                )

                self.cluster_id = await cloud.create_cluster(
                    account=self.account,
                    configuration=self.configuration,
                    name=self.name,
                    workers=self._start_n_workers,
                    backend_options=self.backend_options,
                    software=self.software,
                    worker_cpu=self.worker_cpu,
                    worker_gpu=self.worker_gpu,
                    worker_memory=self.worker_memory,
                    worker_class=self.worker_class,
                    worker_options=self.worker_options,
                    scheduler_cpu=self.scheduler_cpu,
                    scheduler_memory=self.scheduler_memory,
                    scheduler_class=self.scheduler_class,
                    scheduler_options=self.scheduler_options,
                )
                if self._start_n_workers:
                    await self._scale(self._start_n_workers)
            if not self.cluster_id:
                raise RuntimeError(f"Failed to find/create cluster {self.name}")

            self.security, info = await cloud.security(
                cluster_id=self.cluster_id, account=self.account
            )
            self._proxy = bool(self.security.extra_conn_args)
            self._dashboard_address = info["dashboard_address"]

            try:
                self.scheduler_comm = dask.distributed.rpc(
                    info["public_address"],
                    connection_args=self.security.get_connection_args("client"),
                    timeout=5.0,  # if we don't connect quickly, we won't connect
                )
                await self._send_credentials(cloud)
            except IOError as e:
                if "Timed out" in "".join(e.args):
                    raise RuntimeError(
                        "Unable to connect to Dask cluster. This may be due "
                        "to different versions of `dask` and `distributed` "
                        "locally and remotely.\n\n"
                        f"You are using distributed={DISTRIBUTED_VERSION} locally.\n\n"
                        "With pip, you can upgrade to the latest with:\n\n"
                        "\tpip install --upgrade dask distributed"
                    )
                raise

            await super()._start()

            # TODO: Come up with a better long-term solution. Below we raise an informative error message
            # when workers with GPUs take a long time to arrive (due to GPU availability on AWS)
            if (
                should_create
                and self._start_n_workers
                and available_configs
                and (
                    self.worker_gpu
                    or available_configs[self.configuration]["worker"]["gpu"]
                )
            ):
                try:
                    err_msg = (
                        "GPU workers are not being created. This happens when there is limited GPU availability "
                        "in your AWS region. For example, the default region, us-east-2, often runs out of GPUs while "
                        "other regions like us-west-1 still have capacity. You may want to try moving regions:\n\n"
                        "cluster = coiled.Cluster(..., backend_options={'region': 'us-west-1'}"
                    )
                    await self._wait_for_workers(
                        1, timeout="10 minutes", err_msg=err_msg
                    )
                except TimeoutError as e:
                    await self._close()
                    raise e

    async def _wait_for_workers(self, n_workers, timeout=None, err_msg=None) -> None:
        if timeout is None:
            deadline = None
        else:
            timeout = dask.utils.parse_timedelta(timeout, "s")
            deadline = time.time() + timeout
        while n_workers and len(self.scheduler_info["workers"]) < n_workers:
            if deadline and time.time() > deadline:
                err_msg = (
                    err_msg
                    or "Timed out after {timeout} seconds waiting for {n_workers} workers to arrive"
                )
                raise TimeoutError(err_msg)
            await asyncio.sleep(1)

    async def _check_software_environment_exists(
        self, cloud: Cloud[Async]
    ) -> Optional[dict]:
        """Check if software environment exists.

        When we list software environments, we get the user software environments
        and any software environments from the team that the user belongs to. We
        should check if the software environment name that he user is trying to use
        exists. If we can't find the software environment with the given name, we
        will use coiled's default one and tell the user about this. That way we
        don't stop the Cluster creation process if the software env doesn't exist.

        """
        if self.software:
            account, software_name, revision = parse_identifier(
                self.software,
                property_name="software_environment",
                can_have_revision=True,
            )

            software_envs = await cloud.list_software_environments(account=account)

            if name_exists_in_dict(
                user=self.account or cloud.default_account,
                name=self.software,
                dictionary=software_envs,
            ):

                return software_envs

            raise ValueError(
                f" Unable to create Cluster: Software environment with the name '{software_name}' "
                "not found. Have you created this software environment or have you specified your "
                "software environment in the format '<account>/<software environment>'?"
            )

        return None

    async def _check_cluster_configuration_exists(
        self, cloud: Cloud[Async], software_environments: dict = None
    ):
        """Check if the cluster configuration exists.

        We will list cluster configurations and check if the configuration exists within the
        user account or any teams that the user belongs to. We will also check if the user
        attempted to pass a software environment name as the configuration and raise an
        exception indicating that we found a software environment with that name and that
        the user needs to create a configuration with that software name.

        We are getting the software_environments from ``self._check_software_environment_exists``
        so we don't have to do another API call.

        """
        acct, name, _ = parse_identifier(self.configuration, "configuration")
        if not acct:
            # Cluster configs are returned with '<account>/<name>' if no account passed,
            # let's add it ourselves.
            self.configuration = f"{self.account or cloud.default_account}/{name}"
        available_configs = await cloud.list_cluster_configurations(
            account=acct or self.account or cloud.default_account
        )

        if not software_environments:
            software_environments = await cloud.list_software_environments(
                account=acct or self.account or cloud.default_account
            )

        if not name_exists_in_dict(
            user=acct, name=self.configuration, dictionary=available_configs
        ):
            error_msg = f"Cluster configuration '{self.configuration}' not found."
            if not self.software:
                software_environments = await cloud.list_software_environments(
                    account=self.account or cloud.default_account
                )

            if name_exists_in_dict(
                user=cloud.user,
                name=self.configuration,
                dictionary=software_environments,
            ):
                error_msg += (
                    "\n"
                    f"We did find a software environment '{self.configuration}'.\n"
                    "You may need to make a cluster configuration with this \n"
                    "software environment:\n\n"
                    f"  coiled.create_cluster_configuration(name='{self.configuration}', software='{self.configuration}')"  # noqa: E501
                )
            raise ValueError(error_msg)
        return available_configs

    async def _send_credentials(self, cloud: Cloud[Async]):
        """Get credentials and pass them to the scheduler.

        If we are launching a cluster withint a Coiled Job/Notebook
        we don't even try to send credentials along.

        """
        # TODO: Figure out a way to do this in a clean way

        if (
            "DASK_COILED__JOB_ID" not in os.environ
        ) or self.credentials is CredentialsPreferred.NONE:
            aws_creds = {}
            try:
                if self.credentials is CredentialsPreferred.ACCOUNT:
                    aws_creds = await cloud.get_aws_credentials(self.account)
                    # Setup the default session & environment variables so that
                    # account creds are used for other AWS things (e.g. local Dask
                    # client)
                    boto3.setup_default_session(**aws_creds)
                    for k, v in aws_creds.items():
                        os.environ[k.upper()] = v
                # elif self.credentials == CredentialsPreferred.USER:
                #     aws_creds = cloud.get_aws_credentials(self.user)
                creds = {}
                session = aiobotocore.get_session()
                async with session.create_client("sts", **aws_creds) as sts:
                    try:
                        credentials = await sts.get_session_token()
                        credentials = credentials["Credentials"]
                        creds = {
                            k: credentials[k]
                            for k in ["AccessKeyId", "SecretAccessKey", "SessionToken"]
                        }
                    except botocore.errorfactory.ClientError as e:
                        if "session credentials" in str(e):
                            # STS session. Can't request a new session token
                            credentials = await session.get_credentials()
                            credentials = await credentials.get_frozen_credentials()
                            creds = {
                                "AccessKeyId": credentials.access_key,
                                "SecretAccessKey": credentials.secret_key,
                                "SessionToken": credentials.token,
                            }
                    if creds:
                        # TODO: set up TTL, and update these credentials periodically
                        await self.scheduler_comm.aws_update_credentials(
                            credentials={
                                k: creds.get(k)
                                for k in [
                                    "AccessKeyId",
                                    "SecretAccessKey",
                                    "SessionToken",
                                ]
                            }
                        )
            except botocore.exceptions.ProfileNotFound:
                # no AWS credentials (maybe not running against AWS?), fail gracefully
                pass
            except Exception as e:
                # warn, but don't crash
                warnings.warn(str(e))

    def __await__(self: Cluster[Async]):
        async def _():
            if self._lock is None:
                self._lock = asyncio.Lock()
            async with self._lock:
                if self.status == Status.created:
                    await wait_for(self._start(), self.timeout)
                assert self.status == Status.running
            return self

        return _().__await__()

    @overload
    def close(self: Cluster[Sync]) -> None:
        ...

    @overload
    def close(self: Cluster[Async]) -> Awaitable[None]:
        ...

    def close(self) -> Union[None, Awaitable[None]]:
        """
        Close the cluster.
        """
        return self.sync(self._close)

    async def _close(self) -> None:
        if not self.cluster_id:
            raise ValueError("No cluster available to close!")
        cloud = cast(Cloud[Async], self.cloud)
        if self.shutdown_on_close in (True, None):
            await cloud.delete_cluster(
                account=self.account,
                cluster_id=self.cluster_id,
            )
        await super()._close()

    async def _scale(self, n: int) -> None:
        if not self.cluster_id:
            raise ValueError("No cluster available to scale!")
        cloud = cast(Cloud[Async], self.cloud)
        return await cloud._scale(
            account=self.account,
            cluster_id=self.cluster_id,
            n=n,
        )

    @overload
    def scale(self: Cluster[Sync], n: int) -> None:
        ...

    @overload
    def scale(self: Cluster[Async], n: int) -> Awaitable[None]:
        ...

    def scale(self, n: int) -> Optional[Awaitable[None]]:
        """Scale cluster to ``n`` workers

        Parameters
        ----------
        n
            Number of workers to scale cluster size to.
        """
        return self.sync(self._scale, n=n)

    def __enter__(self: Cluster[Sync]) -> Cluster[Sync]:
        return self.sync(self.__aenter__)

    def __exit__(self: Cluster[Sync], *args, **kwargs) -> None:
        return self.sync(self.__aexit__, *args, **kwargs)

    @overload
    def get_logs(self: Cluster[Sync], scheduler: bool, workers: bool = True) -> dict:
        ...

    @overload
    def get_logs(
        self: Cluster[Async], scheduler: bool, workers: bool = True
    ) -> Awaitable[dict]:
        ...

    def get_logs(
        self, scheduler: bool = True, workers: bool = True
    ) -> Union[dict, Awaitable[dict]]:
        """Return logs for the scheduler and workers
        Parameters
        ----------
        scheduler : boolean
            Whether or not to collect logs for the scheduler
        workers : boolean
            Whether or not to collect logs for the workers
        Returns
        -------
        logs: Dict[str]
            A dictionary of logs, with one item for the scheduler and one for
            the workers
        """
        return self.sync(self._get_logs, scheduler=scheduler, workers=workers)

    async def _get_logs(self, scheduler: bool = True, workers: bool = True) -> dict:
        if not self.cluster_id:
            raise ValueError("No cluster available for logs!")
        cloud = cast(Cloud[Async], self.cloud)
        return await cloud.cluster_logs(
            cluster_id=self.cluster_id,
            account=self.account,
            scheduler=scheduler,
            workers=workers,
        )

    @property
    def dashboard_link(self):
        # Only use proxied dashboard address if we're in a hosted notebook
        # Otherwise fall back to the non-proxied address
        if self._proxy or dask.config.get("coiled.dashboard.proxy", False):
            return f"{self.cloud.server}/dashboard/{self.cluster_id}/status"
        else:
            return self._dashboard_address
