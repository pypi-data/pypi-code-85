"""
Type annotations for sns service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_sns import SNSClient

    client: SNSClient = boto3.client("sns")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import (
    ListEndpointsByPlatformApplicationPaginator,
    ListPhoneNumbersOptedOutPaginator,
    ListPlatformApplicationsPaginator,
    ListSubscriptionsByTopicPaginator,
    ListSubscriptionsPaginator,
    ListTopicsPaginator,
)
from .type_defs import (
    CheckIfPhoneNumberIsOptedOutResponseTypeDef,
    ConfirmSubscriptionResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreatePlatformApplicationResponseTypeDef,
    CreateTopicResponseTypeDef,
    GetEndpointAttributesResponseTypeDef,
    GetPlatformApplicationAttributesResponseTypeDef,
    GetSMSAttributesResponseTypeDef,
    GetSubscriptionAttributesResponseTypeDef,
    GetTopicAttributesResponseTypeDef,
    ListEndpointsByPlatformApplicationResponseTypeDef,
    ListPhoneNumbersOptedOutResponseTypeDef,
    ListPlatformApplicationsResponseTypeDef,
    ListSubscriptionsByTopicResponseTypeDef,
    ListSubscriptionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTopicsResponseTypeDef,
    MessageAttributeValueTypeDef,
    PublishResponseTypeDef,
    SubscribeResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SNSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AuthorizationErrorException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentAccessException: Type[BotocoreClientError]
    EndpointDisabledException: Type[BotocoreClientError]
    FilterPolicyLimitExceededException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidSecurityException: Type[BotocoreClientError]
    KMSAccessDeniedException: Type[BotocoreClientError]
    KMSDisabledException: Type[BotocoreClientError]
    KMSInvalidStateException: Type[BotocoreClientError]
    KMSNotFoundException: Type[BotocoreClientError]
    KMSOptInRequired: Type[BotocoreClientError]
    KMSThrottlingException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    PlatformApplicationDisabledException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    StaleTagException: Type[BotocoreClientError]
    SubscriptionLimitExceededException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]
    TagPolicyException: Type[BotocoreClientError]
    ThrottledException: Type[BotocoreClientError]
    TopicLimitExceededException: Type[BotocoreClientError]


class SNSClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_permission(
        self, TopicArn: str, Label: str, AWSAccountId: List[str], ActionName: List[str]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.add_permission)
        [Show boto3-stubs documentation](./client.md#add_permission)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def check_if_phone_number_is_opted_out(
        self, phoneNumber: str
    ) -> CheckIfPhoneNumberIsOptedOutResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.check_if_phone_number_is_opted_out)
        [Show boto3-stubs documentation](./client.md#check_if_phone_number_is_opted_out)
        """

    def confirm_subscription(
        self, TopicArn: str, Token: str, AuthenticateOnUnsubscribe: str = None
    ) -> ConfirmSubscriptionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.confirm_subscription)
        [Show boto3-stubs documentation](./client.md#confirm_subscription)
        """

    def create_platform_application(
        self, Name: str, Platform: str, Attributes: Dict[str, str]
    ) -> CreatePlatformApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.create_platform_application)
        [Show boto3-stubs documentation](./client.md#create_platform_application)
        """

    def create_platform_endpoint(
        self,
        PlatformApplicationArn: str,
        Token: str,
        CustomUserData: str = None,
        Attributes: Dict[str, str] = None,
    ) -> CreateEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.create_platform_endpoint)
        [Show boto3-stubs documentation](./client.md#create_platform_endpoint)
        """

    def create_topic(
        self, Name: str, Attributes: Dict[str, str] = None, Tags: List["TagTypeDef"] = None
    ) -> CreateTopicResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.create_topic)
        [Show boto3-stubs documentation](./client.md#create_topic)
        """

    def delete_endpoint(self, EndpointArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.delete_endpoint)
        [Show boto3-stubs documentation](./client.md#delete_endpoint)
        """

    def delete_platform_application(self, PlatformApplicationArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.delete_platform_application)
        [Show boto3-stubs documentation](./client.md#delete_platform_application)
        """

    def delete_topic(self, TopicArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.delete_topic)
        [Show boto3-stubs documentation](./client.md#delete_topic)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_endpoint_attributes(self, EndpointArn: str) -> GetEndpointAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.get_endpoint_attributes)
        [Show boto3-stubs documentation](./client.md#get_endpoint_attributes)
        """

    def get_platform_application_attributes(
        self, PlatformApplicationArn: str
    ) -> GetPlatformApplicationAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.get_platform_application_attributes)
        [Show boto3-stubs documentation](./client.md#get_platform_application_attributes)
        """

    def get_sms_attributes(self, attributes: List[str] = None) -> GetSMSAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.get_sms_attributes)
        [Show boto3-stubs documentation](./client.md#get_sms_attributes)
        """

    def get_subscription_attributes(
        self, SubscriptionArn: str
    ) -> GetSubscriptionAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.get_subscription_attributes)
        [Show boto3-stubs documentation](./client.md#get_subscription_attributes)
        """

    def get_topic_attributes(self, TopicArn: str) -> GetTopicAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.get_topic_attributes)
        [Show boto3-stubs documentation](./client.md#get_topic_attributes)
        """

    def list_endpoints_by_platform_application(
        self, PlatformApplicationArn: str, NextToken: str = None
    ) -> ListEndpointsByPlatformApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.list_endpoints_by_platform_application)
        [Show boto3-stubs documentation](./client.md#list_endpoints_by_platform_application)
        """

    def list_phone_numbers_opted_out(
        self, nextToken: str = None
    ) -> ListPhoneNumbersOptedOutResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.list_phone_numbers_opted_out)
        [Show boto3-stubs documentation](./client.md#list_phone_numbers_opted_out)
        """

    def list_platform_applications(
        self, NextToken: str = None
    ) -> ListPlatformApplicationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.list_platform_applications)
        [Show boto3-stubs documentation](./client.md#list_platform_applications)
        """

    def list_subscriptions(self, NextToken: str = None) -> ListSubscriptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.list_subscriptions)
        [Show boto3-stubs documentation](./client.md#list_subscriptions)
        """

    def list_subscriptions_by_topic(
        self, TopicArn: str, NextToken: str = None
    ) -> ListSubscriptionsByTopicResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.list_subscriptions_by_topic)
        [Show boto3-stubs documentation](./client.md#list_subscriptions_by_topic)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def list_topics(self, NextToken: str = None) -> ListTopicsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.list_topics)
        [Show boto3-stubs documentation](./client.md#list_topics)
        """

    def opt_in_phone_number(self, phoneNumber: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.opt_in_phone_number)
        [Show boto3-stubs documentation](./client.md#opt_in_phone_number)
        """

    def publish(
        self,
        Message: str,
        TopicArn: str = None,
        TargetArn: str = None,
        PhoneNumber: str = None,
        Subject: str = None,
        MessageStructure: str = None,
        MessageAttributes: Dict[str, MessageAttributeValueTypeDef] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> PublishResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.publish)
        [Show boto3-stubs documentation](./client.md#publish)
        """

    def remove_permission(self, TopicArn: str, Label: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.remove_permission)
        [Show boto3-stubs documentation](./client.md#remove_permission)
        """

    def set_endpoint_attributes(self, EndpointArn: str, Attributes: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.set_endpoint_attributes)
        [Show boto3-stubs documentation](./client.md#set_endpoint_attributes)
        """

    def set_platform_application_attributes(
        self, PlatformApplicationArn: str, Attributes: Dict[str, str]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.set_platform_application_attributes)
        [Show boto3-stubs documentation](./client.md#set_platform_application_attributes)
        """

    def set_sms_attributes(self, attributes: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.set_sms_attributes)
        [Show boto3-stubs documentation](./client.md#set_sms_attributes)
        """

    def set_subscription_attributes(
        self, SubscriptionArn: str, AttributeName: str, AttributeValue: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.set_subscription_attributes)
        [Show boto3-stubs documentation](./client.md#set_subscription_attributes)
        """

    def set_topic_attributes(
        self, TopicArn: str, AttributeName: str, AttributeValue: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.set_topic_attributes)
        [Show boto3-stubs documentation](./client.md#set_topic_attributes)
        """

    def subscribe(
        self,
        TopicArn: str,
        Protocol: str,
        Endpoint: str = None,
        Attributes: Dict[str, str] = None,
        ReturnSubscriptionArn: bool = None,
    ) -> SubscribeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.subscribe)
        [Show boto3-stubs documentation](./client.md#subscribe)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def unsubscribe(self, SubscriptionArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.unsubscribe)
        [Show boto3-stubs documentation](./client.md#unsubscribe)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoints_by_platform_application"]
    ) -> ListEndpointsByPlatformApplicationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Paginator.ListEndpointsByPlatformApplication)[Show boto3-stubs documentation](./paginators.md#listendpointsbyplatformapplicationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_phone_numbers_opted_out"]
    ) -> ListPhoneNumbersOptedOutPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Paginator.ListPhoneNumbersOptedOut)[Show boto3-stubs documentation](./paginators.md#listphonenumbersoptedoutpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_platform_applications"]
    ) -> ListPlatformApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Paginator.ListPlatformApplications)[Show boto3-stubs documentation](./paginators.md#listplatformapplicationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscriptions"]
    ) -> ListSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Paginator.ListSubscriptions)[Show boto3-stubs documentation](./paginators.md#listsubscriptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscriptions_by_topic"]
    ) -> ListSubscriptionsByTopicPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Paginator.ListSubscriptionsByTopic)[Show boto3-stubs documentation](./paginators.md#listsubscriptionsbytopicpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_topics"]) -> ListTopicsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/sns.html#SNS.Paginator.ListTopics)[Show boto3-stubs documentation](./paginators.md#listtopicspaginator)
        """
