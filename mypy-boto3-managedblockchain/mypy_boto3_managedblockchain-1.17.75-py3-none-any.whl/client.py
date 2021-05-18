"""
Type annotations for managedblockchain service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_managedblockchain import ManagedBlockchainClient

    client: ManagedBlockchainClient = boto3.client("managedblockchain")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import (
    FrameworkType,
    MemberStatusType,
    NetworkStatusType,
    NodeStatusType,
    VoteValueType,
)
from .type_defs import (
    CreateMemberOutputTypeDef,
    CreateNetworkOutputTypeDef,
    CreateNodeOutputTypeDef,
    CreateProposalOutputTypeDef,
    GetMemberOutputTypeDef,
    GetNetworkOutputTypeDef,
    GetNodeOutputTypeDef,
    GetProposalOutputTypeDef,
    ListInvitationsOutputTypeDef,
    ListMembersOutputTypeDef,
    ListNetworksOutputTypeDef,
    ListNodesOutputTypeDef,
    ListProposalsOutputTypeDef,
    ListProposalVotesOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    MemberConfigurationTypeDef,
    MemberLogPublishingConfigurationTypeDef,
    NetworkFrameworkConfigurationTypeDef,
    NodeConfigurationTypeDef,
    NodeLogPublishingConfigurationTypeDef,
    ProposalActionsTypeDef,
    VotingPolicyTypeDef,
)

__all__ = ("ManagedBlockchainClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    IllegalActionException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class ManagedBlockchainClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_member(
        self,
        ClientRequestToken: str,
        InvitationId: str,
        NetworkId: str,
        MemberConfiguration: MemberConfigurationTypeDef,
    ) -> CreateMemberOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_member)
        [Show boto3-stubs documentation](./client.md#create_member)
        """

    def create_network(
        self,
        ClientRequestToken: str,
        Name: str,
        Framework: FrameworkType,
        FrameworkVersion: str,
        VotingPolicy: "VotingPolicyTypeDef",
        MemberConfiguration: MemberConfigurationTypeDef,
        Description: str = None,
        FrameworkConfiguration: NetworkFrameworkConfigurationTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> CreateNetworkOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_network)
        [Show boto3-stubs documentation](./client.md#create_network)
        """

    def create_node(
        self,
        ClientRequestToken: str,
        NetworkId: str,
        NodeConfiguration: NodeConfigurationTypeDef,
        MemberId: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateNodeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_node)
        [Show boto3-stubs documentation](./client.md#create_node)
        """

    def create_proposal(
        self,
        ClientRequestToken: str,
        NetworkId: str,
        MemberId: str,
        Actions: "ProposalActionsTypeDef",
        Description: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateProposalOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.create_proposal)
        [Show boto3-stubs documentation](./client.md#create_proposal)
        """

    def delete_member(self, NetworkId: str, MemberId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_member)
        [Show boto3-stubs documentation](./client.md#delete_member)
        """

    def delete_node(self, NetworkId: str, NodeId: str, MemberId: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.delete_node)
        [Show boto3-stubs documentation](./client.md#delete_node)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_member(self, NetworkId: str, MemberId: str) -> GetMemberOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_member)
        [Show boto3-stubs documentation](./client.md#get_member)
        """

    def get_network(self, NetworkId: str) -> GetNetworkOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_network)
        [Show boto3-stubs documentation](./client.md#get_network)
        """

    def get_node(self, NetworkId: str, NodeId: str, MemberId: str = None) -> GetNodeOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_node)
        [Show boto3-stubs documentation](./client.md#get_node)
        """

    def get_proposal(self, NetworkId: str, ProposalId: str) -> GetProposalOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.get_proposal)
        [Show boto3-stubs documentation](./client.md#get_proposal)
        """

    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_invitations)
        [Show boto3-stubs documentation](./client.md#list_invitations)
        """

    def list_members(
        self,
        NetworkId: str,
        Name: str = None,
        Status: MemberStatusType = None,
        IsOwned: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListMembersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_members)
        [Show boto3-stubs documentation](./client.md#list_members)
        """

    def list_networks(
        self,
        Name: str = None,
        Framework: FrameworkType = None,
        Status: NetworkStatusType = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListNetworksOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_networks)
        [Show boto3-stubs documentation](./client.md#list_networks)
        """

    def list_nodes(
        self,
        NetworkId: str,
        MemberId: str = None,
        Status: NodeStatusType = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListNodesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_nodes)
        [Show boto3-stubs documentation](./client.md#list_nodes)
        """

    def list_proposal_votes(
        self, NetworkId: str, ProposalId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListProposalVotesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposal_votes)
        [Show boto3-stubs documentation](./client.md#list_proposal_votes)
        """

    def list_proposals(
        self, NetworkId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListProposalsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_proposals)
        [Show boto3-stubs documentation](./client.md#list_proposals)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](./client.md#list_tags_for_resource)
        """

    def reject_invitation(self, InvitationId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.reject_invitation)
        [Show boto3-stubs documentation](./client.md#reject_invitation)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.tag_resource)
        [Show boto3-stubs documentation](./client.md#tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.untag_resource)
        [Show boto3-stubs documentation](./client.md#untag_resource)
        """

    def update_member(
        self,
        NetworkId: str,
        MemberId: str,
        LogPublishingConfiguration: "MemberLogPublishingConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.update_member)
        [Show boto3-stubs documentation](./client.md#update_member)
        """

    def update_node(
        self,
        NetworkId: str,
        NodeId: str,
        MemberId: str = None,
        LogPublishingConfiguration: "NodeLogPublishingConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.update_node)
        [Show boto3-stubs documentation](./client.md#update_node)
        """

    def vote_on_proposal(
        self, NetworkId: str, ProposalId: str, VoterMemberId: str, Vote: VoteValueType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/managedblockchain.html#ManagedBlockchain.Client.vote_on_proposal)
        [Show boto3-stubs documentation](./client.md#vote_on_proposal)
        """
