"""
Type annotations for appintegrations service type definitions.

[Open documentation](./type_defs.md)

Usage::

    ```python
    from mypy_boto3_appintegrations.type_defs import CreateEventIntegrationResponseTypeDef

    data: CreateEventIntegrationResponseTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEventIntegrationResponseTypeDef",
    "EventFilterTypeDef",
    "EventIntegrationAssociationTypeDef",
    "EventIntegrationTypeDef",
    "GetEventIntegrationResponseTypeDef",
    "ListEventIntegrationAssociationsResponseTypeDef",
    "ListEventIntegrationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
)

CreateEventIntegrationResponseTypeDef = TypedDict(
    "CreateEventIntegrationResponseTypeDef",
    {
        "EventIntegrationArn": str,
    },
    total=False,
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Source": str,
    },
)

EventIntegrationAssociationTypeDef = TypedDict(
    "EventIntegrationAssociationTypeDef",
    {
        "EventIntegrationAssociationArn": str,
        "EventIntegrationAssociationId": str,
        "EventIntegrationName": str,
        "ClientId": str,
        "EventBridgeRuleName": str,
        "ClientAssociationMetadata": Dict[str, str],
    },
    total=False,
)

EventIntegrationTypeDef = TypedDict(
    "EventIntegrationTypeDef",
    {
        "EventIntegrationArn": str,
        "Name": str,
        "Description": str,
        "EventFilter": "EventFilterTypeDef",
        "EventBridgeBus": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

GetEventIntegrationResponseTypeDef = TypedDict(
    "GetEventIntegrationResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "EventIntegrationArn": str,
        "EventBridgeBus": str,
        "EventFilter": "EventFilterTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

ListEventIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListEventIntegrationAssociationsResponseTypeDef",
    {
        "EventIntegrationAssociations": List["EventIntegrationAssociationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListEventIntegrationsResponseTypeDef = TypedDict(
    "ListEventIntegrationsResponseTypeDef",
    {
        "EventIntegrations": List["EventIntegrationTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)
