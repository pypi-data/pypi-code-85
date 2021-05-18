"""
Type annotations for signer service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_signer import SignerClient

    client: SignerClient = boto3.client("signer")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import SigningProfileStatusType, SigningStatusType
from .paginator import (
    ListSigningJobsPaginator,
    ListSigningPlatformsPaginator,
    ListSigningProfilesPaginator,
)
from .type_defs import (
    AddProfilePermissionResponseTypeDef,
    DescribeSigningJobResponseTypeDef,
    DestinationTypeDef,
    GetSigningPlatformResponseTypeDef,
    GetSigningProfileResponseTypeDef,
    ListProfilePermissionsResponseTypeDef,
    ListSigningJobsResponseTypeDef,
    ListSigningPlatformsResponseTypeDef,
    ListSigningProfilesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutSigningProfileResponseTypeDef,
    RemoveProfilePermissionResponseTypeDef,
    SignatureValidityPeriodTypeDef,
    SigningMaterialTypeDef,
    SigningPlatformOverridesTypeDef,
    SourceTypeDef,
    StartSigningJobResponseTypeDef,
)
from .waiter import SuccessfulSigningJobWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SignerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceLimitExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SignerClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_profile_permission(
        self,
        profileName: str,
        action: str,
        principal: str,
        statementId: str,
        profileVersion: str = None,
        revisionId: str = None,
    ) -> AddProfilePermissionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.add_profile_permission)
        [Show boto3-stubs documentation](./client.md#add_profile_permission)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def cancel_signing_profile(self, profileName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.cancel_signing_profile)
        [Show boto3-stubs documentation](./client.md#cancel_signing_profile)
        """

    def describe_signing_job(self, jobId: str) -> DescribeSigningJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.describe_signing_job)
        [Show boto3-stubs documentation](./client.md#describe_signing_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_signing_platform(self, platformId: str) -> GetSigningPlatformResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.get_signing_platform)
        [Show boto3-stubs documentation](./client.md#get_signing_platform)
        """

    def get_signing_profile(
        self, profileName: str, profileOwner: str = None
    ) -> GetSigningProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.get_signing_profile)
        [Show boto3-stubs documentation](./client.md#get_signing_profile)
        """

    def list_profile_permissions(
        self, profileName: str, nextToken: str = None
    ) -> ListProfilePermissionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.list_profile_permissions)
        [Show boto3-stubs documentation](./client.md#list_profile_permissions)
        """

    def list_signing_jobs(
        self,
        status: SigningStatusType = None,
        platformId: str = None,
        requestedBy: str = None,
        maxResults: int = None,
        nextToken: str = None,
        isRevoked: bool = None,
        signatureExpiresBefore: datetime = None,
        signatureExpiresAfter: datetime = None,
        jobInvoker: str = None,
    ) -> ListSigningJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.list_signing_jobs)
        [Show boto3-stubs documentation](./client.md#list_signing_jobs)
        """

    def list_signing_platforms(
        self,
        category: str = None,
        partner: str = None,
        target: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSigningPlatformsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.list_signing_platforms)
        [Show boto3-stubs documentation](./client.md#list_signing_platforms)
        """

    def list_signing_profiles(
        self,
        includeCanceled: bool = None,
        maxResults: int = None,
        nextToken: str = None,
        platformId: str = None,
        statuses: List[SigningProfileStatusType] = None,
    ) -> ListSigningProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.list_signing_profiles)
        [Show boto3-stubs documentation](./client.md#list_signing_profiles)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def put_signing_profile(
        self,
        profileName: str,
        platformId: str,
        signingMaterial: "SigningMaterialTypeDef" = None,
        signatureValidityPeriod: "SignatureValidityPeriodTypeDef" = None,
        overrides: "SigningPlatformOverridesTypeDef" = None,
        signingParameters: Dict[str, str] = None,
        tags: Dict[str, str] = None,
    ) -> PutSigningProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.put_signing_profile)
        [Show boto3-stubs documentation](./client.md#put_signing_profile)
        """

    def remove_profile_permission(
        self, profileName: str, revisionId: str, statementId: str
    ) -> RemoveProfilePermissionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.remove_profile_permission)
        [Show boto3-stubs documentation](./client.md#remove_profile_permission)
        """

    def revoke_signature(self, jobId: str, reason: str, jobOwner: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.revoke_signature)
        [Show boto3-stubs documentation](./client.md#revoke_signature)
        """

    def revoke_signing_profile(
        self, profileName: str, profileVersion: str, reason: str, effectiveTime: datetime
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.revoke_signing_profile)
        [Show boto3-stubs documentation](./client.md#revoke_signing_profile)
        """

    def start_signing_job(
        self,
        source: "SourceTypeDef",
        destination: DestinationTypeDef,
        profileName: str,
        clientRequestToken: str,
        profileOwner: str = None,
    ) -> StartSigningJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.start_signing_job)
        [Show boto3-stubs documentation](./client.md#start_signing_job)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_jobs"]
    ) -> ListSigningJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Paginator.ListSigningJobs)[Show boto3-stubs documentation](./paginators.md#listsigningjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_platforms"]
    ) -> ListSigningPlatformsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Paginator.ListSigningPlatforms)[Show boto3-stubs documentation](./paginators.md#listsigningplatformspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signing_profiles"]
    ) -> ListSigningProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Paginator.ListSigningProfiles)[Show boto3-stubs documentation](./paginators.md#listsigningprofilespaginator)
        """

    def get_waiter(
        self, waiter_name: Literal["successful_signing_job"]
    ) -> SuccessfulSigningJobWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/signer.html#Signer.Waiter.successful_signing_job)[Show boto3-stubs documentation](./waiters.md#successfulsigningjobwaiter)
        """
