"""
Type annotations for iotfleethub service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotfleethub import IoTFleetHubClient

    client: IoTFleetHubClient = boto3.client("iotfleethub")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .paginator import ListApplicationsPaginator
from .type_defs import (
    CreateApplicationResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTFleetHubClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class IoTFleetHubClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_application(
        self,
        applicationName: str,
        roleArn: str,
        applicationDescription: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client.create_application)
        [Show boto3-stubs documentation](./client.md#create_application)
        """

    def delete_application(self, applicationId: str, clientToken: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client.delete_application)
        [Show boto3-stubs documentation](./client.md#delete_application)
        """

    def describe_application(self, applicationId: str) -> DescribeApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client.describe_application)
        [Show boto3-stubs documentation](./client.md#describe_application)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def list_applications(self, nextToken: str = None) -> ListApplicationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client.list_applications)
        [Show boto3-stubs documentation](./client.md#list_applications)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    def update_application(
        self,
        applicationId: str,
        applicationName: str = None,
        applicationDescription: str = None,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Client.update_application)
        [Show boto3-stubs documentation](./client.md#update_application)
        """

    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotfleethub.html#IoTFleetHub.Paginator.ListApplications)[Show boto3-stubs documentation](./paginators.md#listapplicationspaginator)
        """
