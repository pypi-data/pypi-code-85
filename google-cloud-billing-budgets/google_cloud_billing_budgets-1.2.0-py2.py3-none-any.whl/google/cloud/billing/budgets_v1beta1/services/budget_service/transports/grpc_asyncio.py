# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1  # type: ignore
from google.api_core import grpc_helpers_async  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
import packaging.version

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.billing.budgets_v1beta1.types import budget_model
from google.cloud.billing.budgets_v1beta1.types import budget_service
from google.protobuf import empty_pb2  # type: ignore
from .base import BudgetServiceTransport, DEFAULT_CLIENT_INFO
from .grpc import BudgetServiceGrpcTransport


class BudgetServiceGrpcAsyncIOTransport(BudgetServiceTransport):
    """gRPC AsyncIO backend transport for BudgetService.

    BudgetService stores Cloud Billing budgets, which define a
    budget plan and rules to execute as we track spend against that
    plan.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "billingbudgets.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        self_signed_jwt_kwargs = cls._get_self_signed_jwt_kwargs(host, scopes)

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            **self_signed_jwt_kwargs,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "billingbudgets.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id=None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def create_budget(
        self,
    ) -> Callable[[budget_service.CreateBudgetRequest], Awaitable[budget_model.Budget]]:
        r"""Return a callable for the create budget method over gRPC.

        Creates a new budget. See
        <a href="https://cloud.google.com/billing/quotas">Quotas
        and limits</a> for more information on the limits of the
        number of budgets you can create.

        Returns:
            Callable[[~.CreateBudgetRequest],
                    Awaitable[~.Budget]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_budget" not in self._stubs:
            self._stubs["create_budget"] = self.grpc_channel.unary_unary(
                "/google.cloud.billing.budgets.v1beta1.BudgetService/CreateBudget",
                request_serializer=budget_service.CreateBudgetRequest.serialize,
                response_deserializer=budget_model.Budget.deserialize,
            )
        return self._stubs["create_budget"]

    @property
    def update_budget(
        self,
    ) -> Callable[[budget_service.UpdateBudgetRequest], Awaitable[budget_model.Budget]]:
        r"""Return a callable for the update budget method over gRPC.

        Updates a budget and returns the updated budget.
        WARNING: There are some fields exposed on the Google
        Cloud Console that aren't available on this API. Budget
        fields that are not exposed in this API will not be
        changed by this method.

        Returns:
            Callable[[~.UpdateBudgetRequest],
                    Awaitable[~.Budget]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_budget" not in self._stubs:
            self._stubs["update_budget"] = self.grpc_channel.unary_unary(
                "/google.cloud.billing.budgets.v1beta1.BudgetService/UpdateBudget",
                request_serializer=budget_service.UpdateBudgetRequest.serialize,
                response_deserializer=budget_model.Budget.deserialize,
            )
        return self._stubs["update_budget"]

    @property
    def get_budget(
        self,
    ) -> Callable[[budget_service.GetBudgetRequest], Awaitable[budget_model.Budget]]:
        r"""Return a callable for the get budget method over gRPC.

        Returns a budget.
        WARNING: There are some fields exposed on the Google
        Cloud Console that aren't available on this API. When
        reading from the API, you will not see these fields in
        the return value, though they may have been set in the
        Cloud Console.

        Returns:
            Callable[[~.GetBudgetRequest],
                    Awaitable[~.Budget]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_budget" not in self._stubs:
            self._stubs["get_budget"] = self.grpc_channel.unary_unary(
                "/google.cloud.billing.budgets.v1beta1.BudgetService/GetBudget",
                request_serializer=budget_service.GetBudgetRequest.serialize,
                response_deserializer=budget_model.Budget.deserialize,
            )
        return self._stubs["get_budget"]

    @property
    def list_budgets(
        self,
    ) -> Callable[
        [budget_service.ListBudgetsRequest],
        Awaitable[budget_service.ListBudgetsResponse],
    ]:
        r"""Return a callable for the list budgets method over gRPC.

        Returns a list of budgets for a billing account.
        WARNING: There are some fields exposed on the Google
        Cloud Console that aren't available on this API. When
        reading from the API, you will not see these fields in
        the return value, though they may have been set in the
        Cloud Console.

        Returns:
            Callable[[~.ListBudgetsRequest],
                    Awaitable[~.ListBudgetsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_budgets" not in self._stubs:
            self._stubs["list_budgets"] = self.grpc_channel.unary_unary(
                "/google.cloud.billing.budgets.v1beta1.BudgetService/ListBudgets",
                request_serializer=budget_service.ListBudgetsRequest.serialize,
                response_deserializer=budget_service.ListBudgetsResponse.deserialize,
            )
        return self._stubs["list_budgets"]

    @property
    def delete_budget(
        self,
    ) -> Callable[[budget_service.DeleteBudgetRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete budget method over gRPC.

        Deletes a budget. Returns successfully if already
        deleted.

        Returns:
            Callable[[~.DeleteBudgetRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_budget" not in self._stubs:
            self._stubs["delete_budget"] = self.grpc_channel.unary_unary(
                "/google.cloud.billing.budgets.v1beta1.BudgetService/DeleteBudget",
                request_serializer=budget_service.DeleteBudgetRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_budget"]


__all__ = ("BudgetServiceGrpcAsyncIOTransport",)
