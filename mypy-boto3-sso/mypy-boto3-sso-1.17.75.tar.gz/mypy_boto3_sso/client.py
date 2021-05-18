"""
Type annotations for sso service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_sso import SSOClient

    client: SSOClient = boto3.client("sso")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from .paginator import ListAccountRolesPaginator, ListAccountsPaginator
from .type_defs import (
    GetRoleCredentialsResponseTypeDef,
    ListAccountRolesResponseTypeDef,
    ListAccountsResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSOClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class SSOClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sso.html#SSO.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sso.html#SSO.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sso.html#SSO.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_role_credentials(
        self, roleName: str, accountId: str, accessToken: str
    ) -> GetRoleCredentialsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sso.html#SSO.Client.get_role_credentials)
        [Show boto3-stubs documentation](./client.md#get_role_credentials)
        """

    def list_account_roles(
        self, accessToken: str, accountId: str, nextToken: str = None, maxResults: int = None
    ) -> ListAccountRolesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sso.html#SSO.Client.list_account_roles)
        [Show boto3-stubs documentation](./client.md#list_account_roles)
        """

    def list_accounts(
        self, accessToken: str, nextToken: str = None, maxResults: int = None
    ) -> ListAccountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sso.html#SSO.Client.list_accounts)
        [Show boto3-stubs documentation](./client.md#list_accounts)
        """

    def logout(self, accessToken: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sso.html#SSO.Client.logout)
        [Show boto3-stubs documentation](./client.md#logout)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_roles"]
    ) -> ListAccountRolesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sso.html#SSO.Paginator.ListAccountRoles)[Show boto3-stubs documentation](./paginators.md#listaccountrolespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_accounts"]) -> ListAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sso.html#SSO.Paginator.ListAccounts)[Show boto3-stubs documentation](./paginators.md#listaccountspaginator)
        """
