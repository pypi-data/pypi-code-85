"""
Type annotations for elastic-inference service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_elastic_inference import ElasticInferenceClient

    client: ElasticInferenceClient = boto3.client("elastic-inference")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import LocationTypeType
from .paginator import DescribeAcceleratorsPaginator
from .type_defs import (
    DescribeAcceleratorOfferingsResponseTypeDef,
    DescribeAcceleratorsResponseTypeDef,
    DescribeAcceleratorTypesResponseTypeDef,
    FilterTypeDef,
    ListTagsForResourceResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticInferenceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class ElasticInferenceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/elastic-inference.html#ElasticInference.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/elastic-inference.html#ElasticInference.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def describe_accelerator_offerings(
        self, locationType: LocationTypeType, acceleratorTypes: List[str] = None
    ) -> DescribeAcceleratorOfferingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerator_offerings)
        [Show boto3-stubs documentation](./client.md#describe_accelerator_offerings)
        """

    def describe_accelerator_types(self) -> DescribeAcceleratorTypesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerator_types)
        [Show boto3-stubs documentation](./client.md#describe_accelerator_types)
        """

    def describe_accelerators(
        self,
        acceleratorIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeAcceleratorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerators)
        [Show boto3-stubs documentation](./client.md#describe_accelerators)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/elastic-inference.html#ElasticInference.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/elastic-inference.html#ElasticInference.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/elastic-inference.html#ElasticInference.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/elastic-inference.html#ElasticInference.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    def get_paginator(
        self, operation_name: Literal["describe_accelerators"]
    ) -> DescribeAcceleratorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/elastic-inference.html#ElasticInference.Paginator.DescribeAccelerators)[Show boto3-stubs documentation](./paginators.md#describeacceleratorspaginator)
        """
