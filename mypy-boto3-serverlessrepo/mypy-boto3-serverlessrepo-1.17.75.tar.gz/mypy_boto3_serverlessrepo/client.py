"""
Type annotations for serverlessrepo service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_serverlessrepo import ServerlessApplicationRepositoryClient

    client: ServerlessApplicationRepositoryClient = boto3.client("serverlessrepo")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import (
    ListApplicationDependenciesPaginator,
    ListApplicationsPaginator,
    ListApplicationVersionsPaginator,
)
from .type_defs import (
    ApplicationPolicyStatementTypeDef,
    CreateApplicationResponseTypeDef,
    CreateApplicationVersionResponseTypeDef,
    CreateCloudFormationChangeSetResponseTypeDef,
    CreateCloudFormationTemplateResponseTypeDef,
    GetApplicationPolicyResponseTypeDef,
    GetApplicationResponseTypeDef,
    GetCloudFormationTemplateResponseTypeDef,
    ListApplicationDependenciesResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ParameterValueTypeDef,
    PutApplicationPolicyResponseTypeDef,
    RollbackConfigurationTypeDef,
    TagTypeDef,
    UpdateApplicationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServerlessApplicationRepositoryClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class ServerlessApplicationRepositoryClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_application(
        self,
        Author: str,
        Description: str,
        Name: str,
        HomePageUrl: str = None,
        Labels: List[str] = None,
        LicenseBody: str = None,
        LicenseUrl: str = None,
        ReadmeBody: str = None,
        ReadmeUrl: str = None,
        SemanticVersion: str = None,
        SourceCodeArchiveUrl: str = None,
        SourceCodeUrl: str = None,
        SpdxLicenseId: str = None,
        TemplateBody: str = None,
        TemplateUrl: str = None,
    ) -> CreateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_application)
        [Show boto3-stubs documentation](./client.md#create_application)
        """

    def create_application_version(
        self,
        ApplicationId: str,
        SemanticVersion: str,
        SourceCodeArchiveUrl: str = None,
        SourceCodeUrl: str = None,
        TemplateBody: str = None,
        TemplateUrl: str = None,
    ) -> CreateApplicationVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_application_version)
        [Show boto3-stubs documentation](./client.md#create_application_version)
        """

    def create_cloud_formation_change_set(
        self,
        ApplicationId: str,
        StackName: str,
        Capabilities: List[str] = None,
        ChangeSetName: str = None,
        ClientToken: str = None,
        Description: str = None,
        NotificationArns: List[str] = None,
        ParameterOverrides: List[ParameterValueTypeDef] = None,
        ResourceTypes: List[str] = None,
        RollbackConfiguration: RollbackConfigurationTypeDef = None,
        SemanticVersion: str = None,
        Tags: List[TagTypeDef] = None,
        TemplateId: str = None,
    ) -> CreateCloudFormationChangeSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_cloud_formation_change_set)
        [Show boto3-stubs documentation](./client.md#create_cloud_formation_change_set)
        """

    def create_cloud_formation_template(
        self, ApplicationId: str, SemanticVersion: str = None
    ) -> CreateCloudFormationTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.create_cloud_formation_template)
        [Show boto3-stubs documentation](./client.md#create_cloud_formation_template)
        """

    def delete_application(self, ApplicationId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.delete_application)
        [Show boto3-stubs documentation](./client.md#delete_application)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_application(
        self, ApplicationId: str, SemanticVersion: str = None
    ) -> GetApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_application)
        [Show boto3-stubs documentation](./client.md#get_application)
        """

    def get_application_policy(self, ApplicationId: str) -> GetApplicationPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_application_policy)
        [Show boto3-stubs documentation](./client.md#get_application_policy)
        """

    def get_cloud_formation_template(
        self, ApplicationId: str, TemplateId: str
    ) -> GetCloudFormationTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.get_cloud_formation_template)
        [Show boto3-stubs documentation](./client.md#get_cloud_formation_template)
        """

    def list_application_dependencies(
        self,
        ApplicationId: str,
        MaxItems: int = None,
        NextToken: str = None,
        SemanticVersion: str = None,
    ) -> ListApplicationDependenciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_application_dependencies)
        [Show boto3-stubs documentation](./client.md#list_application_dependencies)
        """

    def list_application_versions(
        self, ApplicationId: str, MaxItems: int = None, NextToken: str = None
    ) -> ListApplicationVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_application_versions)
        [Show boto3-stubs documentation](./client.md#list_application_versions)
        """

    def list_applications(
        self, MaxItems: int = None, NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.list_applications)
        [Show boto3-stubs documentation](./client.md#list_applications)
        """

    def put_application_policy(
        self, ApplicationId: str, Statements: List["ApplicationPolicyStatementTypeDef"]
    ) -> PutApplicationPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.put_application_policy)
        [Show boto3-stubs documentation](./client.md#put_application_policy)
        """

    def unshare_application(self, ApplicationId: str, OrganizationId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.unshare_application)
        [Show boto3-stubs documentation](./client.md#unshare_application)
        """

    def update_application(
        self,
        ApplicationId: str,
        Author: str = None,
        Description: str = None,
        HomePageUrl: str = None,
        Labels: List[str] = None,
        ReadmeBody: str = None,
        ReadmeUrl: str = None,
    ) -> UpdateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Client.update_application)
        [Show boto3-stubs documentation](./client.md#update_application)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_dependencies"]
    ) -> ListApplicationDependenciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies)[Show boto3-stubs documentation](./paginators.md#listapplicationdependenciespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_versions"]
    ) -> ListApplicationVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions)[Show boto3-stubs documentation](./paginators.md#listapplicationversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplications)[Show boto3-stubs documentation](./paginators.md#listapplicationspaginator)
        """
