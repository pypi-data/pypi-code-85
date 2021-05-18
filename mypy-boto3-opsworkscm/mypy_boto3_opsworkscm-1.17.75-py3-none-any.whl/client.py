"""
Type annotations for opsworkscm service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_opsworkscm import OpsWorksCMClient

    client: OpsWorksCMClient = boto3.client("opsworkscm")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .paginator import (
    DescribeBackupsPaginator,
    DescribeEventsPaginator,
    DescribeServersPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    AssociateNodeResponseTypeDef,
    CreateBackupResponseTypeDef,
    CreateServerResponseTypeDef,
    DescribeAccountAttributesResponseTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeNodeAssociationStatusResponseTypeDef,
    DescribeServersResponseTypeDef,
    DisassociateNodeResponseTypeDef,
    EngineAttributeTypeDef,
    ExportServerEngineAttributeResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartMaintenanceResponseTypeDef,
    TagTypeDef,
    UpdateServerEngineAttributesResponseTypeDef,
    UpdateServerResponseTypeDef,
)
from .waiter import NodeAssociatedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("OpsWorksCMClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class OpsWorksCMClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_node(
        self, ServerName: str, NodeName: str, EngineAttributes: List["EngineAttributeTypeDef"]
    ) -> AssociateNodeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.associate_node)
        [Show boto3-stubs documentation](./client.md#associate_node)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_backup(
        self, ServerName: str, Description: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateBackupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.create_backup)
        [Show boto3-stubs documentation](./client.md#create_backup)
        """

    def create_server(
        self,
        Engine: str,
        ServerName: str,
        InstanceProfileArn: str,
        InstanceType: str,
        ServiceRoleArn: str,
        AssociatePublicIpAddress: bool = None,
        CustomDomain: str = None,
        CustomCertificate: str = None,
        CustomPrivateKey: str = None,
        DisableAutomatedBackup: bool = None,
        EngineModel: str = None,
        EngineVersion: str = None,
        EngineAttributes: List["EngineAttributeTypeDef"] = None,
        BackupRetentionCount: int = None,
        KeyPair: str = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None,
        SecurityGroupIds: List[str] = None,
        SubnetIds: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        BackupId: str = None,
    ) -> CreateServerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.create_server)
        [Show boto3-stubs documentation](./client.md#create_server)
        """

    def delete_backup(self, BackupId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_backup)
        [Show boto3-stubs documentation](./client.md#delete_backup)
        """

    def delete_server(self, ServerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.delete_server)
        [Show boto3-stubs documentation](./client.md#delete_server)
        """

    def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_account_attributes)
        [Show boto3-stubs documentation](./client.md#describe_account_attributes)
        """

    def describe_backups(
        self,
        BackupId: str = None,
        ServerName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeBackupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_backups)
        [Show boto3-stubs documentation](./client.md#describe_backups)
        """

    def describe_events(
        self, ServerName: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_events)
        [Show boto3-stubs documentation](./client.md#describe_events)
        """

    def describe_node_association_status(
        self, NodeAssociationStatusToken: str, ServerName: str
    ) -> DescribeNodeAssociationStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_node_association_status)
        [Show boto3-stubs documentation](./client.md#describe_node_association_status)
        """

    def describe_servers(
        self, ServerName: str = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeServersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.describe_servers)
        [Show boto3-stubs documentation](./client.md#describe_servers)
        """

    def disassociate_node(
        self,
        ServerName: str,
        NodeName: str,
        EngineAttributes: List["EngineAttributeTypeDef"] = None,
    ) -> DisassociateNodeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.disassociate_node)
        [Show boto3-stubs documentation](./client.md#disassociate_node)
        """

    def export_server_engine_attribute(
        self,
        ExportAttributeName: str,
        ServerName: str,
        InputAttributes: List["EngineAttributeTypeDef"] = None,
    ) -> ExportServerEngineAttributeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.export_server_engine_attribute)
        [Show boto3-stubs documentation](./client.md#export_server_engine_attribute)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def list_tags_for_resource(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def restore_server(
        self, BackupId: str, ServerName: str, InstanceType: str = None, KeyPair: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.restore_server)
        [Show boto3-stubs documentation](./client.md#restore_server)
        """

    def start_maintenance(
        self, ServerName: str, EngineAttributes: List["EngineAttributeTypeDef"] = None
    ) -> StartMaintenanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.start_maintenance)
        [Show boto3-stubs documentation](./client.md#start_maintenance)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    def update_server(
        self,
        ServerName: str,
        DisableAutomatedBackup: bool = None,
        BackupRetentionCount: int = None,
        PreferredMaintenanceWindow: str = None,
        PreferredBackupWindow: str = None,
    ) -> UpdateServerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server)
        [Show boto3-stubs documentation](./client.md#update_server)
        """

    def update_server_engine_attributes(
        self, ServerName: str, AttributeName: str, AttributeValue: str = None
    ) -> UpdateServerEngineAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Client.update_server_engine_attributes)
        [Show boto3-stubs documentation](./client.md#update_server_engine_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_backups"]
    ) -> DescribeBackupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups)[Show boto3-stubs documentation](./paginators.md#describebackupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents)[Show boto3-stubs documentation](./paginators.md#describeeventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_servers"]
    ) -> DescribeServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers)[Show boto3-stubs documentation](./paginators.md#describeserverspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Paginator.ListTagsForResource)[Show boto3-stubs documentation](./paginators.md#listtagsforresourcepaginator)
        """

    def get_waiter(self, waiter_name: Literal["node_associated"]) -> NodeAssociatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/opsworkscm.html#OpsWorksCM.Waiter.node_associated)[Show boto3-stubs documentation](./waiters.md#nodeassociatedwaiter)
        """
