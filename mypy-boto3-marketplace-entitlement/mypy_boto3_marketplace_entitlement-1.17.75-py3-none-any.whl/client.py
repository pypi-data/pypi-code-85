"""
Type annotations for marketplace-entitlement service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplace_entitlement import MarketplaceEntitlementServiceClient

    client: MarketplaceEntitlementServiceClient = boto3.client("marketplace-entitlement")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import GetEntitlementFilterNameType
from .paginator import GetEntitlementsPaginator
from .type_defs import GetEntitlementsResultTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MarketplaceEntitlementServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class MarketplaceEntitlementServiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.can_paginate)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_entitlements(
        self,
        ProductCode: str,
        Filter: Dict[GetEntitlementFilterNameType, List[str]] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetEntitlementsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Client.get_entitlements)
        [Show boto3-stubs documentation](./client.md#get_entitlements)
        """

    def get_paginator(
        self, operation_name: Literal["get_entitlements"]
    ) -> GetEntitlementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements)[Show boto3-stubs documentation](./paginators.md#getentitlementspaginator)
        """
