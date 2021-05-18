"""
Type annotations for iotdeviceadvisor service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotdeviceadvisor import IoTDeviceAdvisorClient

    client: IoTDeviceAdvisorClient = boto3.client("iotdeviceadvisor")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .type_defs import (
    CreateSuiteDefinitionResponseTypeDef,
    GetSuiteDefinitionResponseTypeDef,
    GetSuiteRunReportResponseTypeDef,
    GetSuiteRunResponseTypeDef,
    ListSuiteDefinitionsResponseTypeDef,
    ListSuiteRunsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartSuiteRunResponseTypeDef,
    SuiteDefinitionConfigurationTypeDef,
    SuiteRunConfigurationTypeDef,
    UpdateSuiteDefinitionResponseTypeDef,
)

__all__ = ("IoTDeviceAdvisorClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class IoTDeviceAdvisorClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_suite_definition(
        self,
        suiteDefinitionConfiguration: "SuiteDefinitionConfigurationTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateSuiteDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.create_suite_definition)
        [Show boto3-stubs documentation](./client.md#create_suite_definition)
        """

    def delete_suite_definition(self, suiteDefinitionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.delete_suite_definition)
        [Show boto3-stubs documentation](./client.md#delete_suite_definition)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_suite_definition(
        self, suiteDefinitionId: str, suiteDefinitionVersion: str = None
    ) -> GetSuiteDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_definition)
        [Show boto3-stubs documentation](./client.md#get_suite_definition)
        """

    def get_suite_run(self, suiteDefinitionId: str, suiteRunId: str) -> GetSuiteRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_run)
        [Show boto3-stubs documentation](./client.md#get_suite_run)
        """

    def get_suite_run_report(
        self, suiteDefinitionId: str, suiteRunId: str
    ) -> GetSuiteRunReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.get_suite_run_report)
        [Show boto3-stubs documentation](./client.md#get_suite_run_report)
        """

    def list_suite_definitions(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListSuiteDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_suite_definitions)
        [Show boto3-stubs documentation](./client.md#list_suite_definitions)
        """

    def list_suite_runs(
        self,
        suiteDefinitionId: str = None,
        suiteDefinitionVersion: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSuiteRunsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_suite_runs)
        [Show boto3-stubs documentation](./client.md#list_suite_runs)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def start_suite_run(
        self,
        suiteDefinitionId: str,
        suiteDefinitionVersion: str = None,
        suiteRunConfiguration: "SuiteRunConfigurationTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> StartSuiteRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.start_suite_run)
        [Show boto3-stubs documentation](./client.md#start_suite_run)
        """

    def stop_suite_run(self, suiteDefinitionId: str, suiteRunId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.stop_suite_run)
        [Show boto3-stubs documentation](./client.md#stop_suite_run)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    def update_suite_definition(
        self,
        suiteDefinitionId: str,
        suiteDefinitionConfiguration: "SuiteDefinitionConfigurationTypeDef" = None,
    ) -> UpdateSuiteDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/iotdeviceadvisor.html#IoTDeviceAdvisor.Client.update_suite_definition)
        [Show boto3-stubs documentation](./client.md#update_suite_definition)
        """
