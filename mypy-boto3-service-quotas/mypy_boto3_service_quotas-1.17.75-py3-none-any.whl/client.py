"""
Type annotations for service-quotas service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_service_quotas import ServiceQuotasClient

    client: ServiceQuotasClient = boto3.client("service-quotas")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import RequestStatusType
from .paginator import (
    ListAWSDefaultServiceQuotasPaginator,
    ListRequestedServiceQuotaChangeHistoryByQuotaPaginator,
    ListRequestedServiceQuotaChangeHistoryPaginator,
    ListServiceQuotaIncreaseRequestsInTemplatePaginator,
    ListServiceQuotasPaginator,
    ListServicesPaginator,
)
from .type_defs import (
    GetAssociationForServiceQuotaTemplateResponseTypeDef,
    GetAWSDefaultServiceQuotaResponseTypeDef,
    GetRequestedServiceQuotaChangeResponseTypeDef,
    GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef,
    GetServiceQuotaResponseTypeDef,
    ListAWSDefaultServiceQuotasResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryResponseTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef,
    ListServiceQuotasResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef,
    RequestServiceQuotaIncreaseResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceQuotasClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AWSServiceAccessNotEnabledException: Type[BotocoreClientError]
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DependencyAccessDeniedException: Type[BotocoreClientError]
    IllegalArgumentException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidResourceStateException: Type[BotocoreClientError]
    NoAvailableOrganizationException: Type[BotocoreClientError]
    NoSuchResourceException: Type[BotocoreClientError]
    OrganizationNotInAllFeaturesModeException: Type[BotocoreClientError]
    QuotaExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ServiceQuotaTemplateNotInUseException: Type[BotocoreClientError]
    TagPolicyViolationException: Type[BotocoreClientError]
    TemplatesNotAvailableInRegionException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class ServiceQuotasClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_service_quota_template(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.associate_service_quota_template)
        [Show boto3-stubs documentation](./client.md#associate_service_quota_template)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def delete_service_quota_increase_request_from_template(
        self, ServiceCode: str, QuotaCode: str, AwsRegion: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.delete_service_quota_increase_request_from_template)
        [Show boto3-stubs documentation](./client.md#delete_service_quota_increase_request_from_template)
        """

    def disassociate_service_quota_template(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.disassociate_service_quota_template)
        [Show boto3-stubs documentation](./client.md#disassociate_service_quota_template)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_association_for_service_quota_template(
        self,
    ) -> GetAssociationForServiceQuotaTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.get_association_for_service_quota_template)
        [Show boto3-stubs documentation](./client.md#get_association_for_service_quota_template)
        """

    def get_aws_default_service_quota(
        self, ServiceCode: str, QuotaCode: str
    ) -> GetAWSDefaultServiceQuotaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.get_aws_default_service_quota)
        [Show boto3-stubs documentation](./client.md#get_aws_default_service_quota)
        """

    def get_requested_service_quota_change(
        self, RequestId: str
    ) -> GetRequestedServiceQuotaChangeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.get_requested_service_quota_change)
        [Show boto3-stubs documentation](./client.md#get_requested_service_quota_change)
        """

    def get_service_quota(self, ServiceCode: str, QuotaCode: str) -> GetServiceQuotaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.get_service_quota)
        [Show boto3-stubs documentation](./client.md#get_service_quota)
        """

    def get_service_quota_increase_request_from_template(
        self, ServiceCode: str, QuotaCode: str, AwsRegion: str
    ) -> GetServiceQuotaIncreaseRequestFromTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.get_service_quota_increase_request_from_template)
        [Show boto3-stubs documentation](./client.md#get_service_quota_increase_request_from_template)
        """

    def list_aws_default_service_quotas(
        self, ServiceCode: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAWSDefaultServiceQuotasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.list_aws_default_service_quotas)
        [Show boto3-stubs documentation](./client.md#list_aws_default_service_quotas)
        """

    def list_requested_service_quota_change_history(
        self,
        ServiceCode: str = None,
        Status: RequestStatusType = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListRequestedServiceQuotaChangeHistoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.list_requested_service_quota_change_history)
        [Show boto3-stubs documentation](./client.md#list_requested_service_quota_change_history)
        """

    def list_requested_service_quota_change_history_by_quota(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: RequestStatusType = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.list_requested_service_quota_change_history_by_quota)
        [Show boto3-stubs documentation](./client.md#list_requested_service_quota_change_history_by_quota)
        """

    def list_service_quota_increase_requests_in_template(
        self,
        ServiceCode: str = None,
        AwsRegion: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.list_service_quota_increase_requests_in_template)
        [Show boto3-stubs documentation](./client.md#list_service_quota_increase_requests_in_template)
        """

    def list_service_quotas(
        self, ServiceCode: str, NextToken: str = None, MaxResults: int = None
    ) -> ListServiceQuotasResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.list_service_quotas)
        [Show boto3-stubs documentation](./client.md#list_service_quotas)
        """

    def list_services(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListServicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.list_services)
        [Show boto3-stubs documentation](./client.md#list_services)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def put_service_quota_increase_request_into_template(
        self, QuotaCode: str, ServiceCode: str, AwsRegion: str, DesiredValue: float
    ) -> PutServiceQuotaIncreaseRequestIntoTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.put_service_quota_increase_request_into_template)
        [Show boto3-stubs documentation](./client.md#put_service_quota_increase_request_into_template)
        """

    def request_service_quota_increase(
        self, ServiceCode: str, QuotaCode: str, DesiredValue: float
    ) -> RequestServiceQuotaIncreaseResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.request_service_quota_increase)
        [Show boto3-stubs documentation](./client.md#request_service_quota_increase)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_aws_default_service_quotas"]
    ) -> ListAWSDefaultServiceQuotasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas)[Show boto3-stubs documentation](./paginators.md#listawsdefaultservicequotaspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_requested_service_quota_change_history"]
    ) -> ListRequestedServiceQuotaChangeHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory)[Show boto3-stubs documentation](./paginators.md#listrequestedservicequotachangehistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_requested_service_quota_change_history_by_quota"]
    ) -> ListRequestedServiceQuotaChangeHistoryByQuotaPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota)[Show boto3-stubs documentation](./paginators.md#listrequestedservicequotachangehistorybyquotapaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_quota_increase_requests_in_template"]
    ) -> ListServiceQuotaIncreaseRequestsInTemplatePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate)[Show boto3-stubs documentation](./paginators.md#listservicequotaincreaserequestsintemplatepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_quotas"]
    ) -> ListServiceQuotasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas)[Show boto3-stubs documentation](./paginators.md#listservicequotaspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices)[Show boto3-stubs documentation](./paginators.md#listservicespaginator)
        """
