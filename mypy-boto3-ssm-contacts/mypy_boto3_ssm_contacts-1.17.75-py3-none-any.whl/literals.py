"""
Type annotations for ssm-contacts service literal definitions.

[Open documentation](./literals.md)

Usage::

    ```python
    from mypy_boto3_ssm_contacts.literals import AcceptTypeType

    data: AcceptTypeType = "DELIVERED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AcceptTypeType",
    "ActivationStatusType",
    "ChannelTypeType",
    "ContactTypeType",
    "ListContactChannelsPaginatorName",
    "ListContactsPaginatorName",
    "ListEngagementsPaginatorName",
    "ListPageReceiptsPaginatorName",
    "ListPagesByContactPaginatorName",
    "ListPagesByEngagementPaginatorName",
    "ReceiptTypeType",
)


AcceptTypeType = Literal["DELIVERED", "READ"]
ActivationStatusType = Literal["ACTIVATED", "NOT_ACTIVATED"]
ChannelTypeType = Literal["EMAIL", "SMS", "VOICE"]
ContactTypeType = Literal["ESCALATION", "PERSONAL"]
ListContactChannelsPaginatorName = Literal["list_contact_channels"]
ListContactsPaginatorName = Literal["list_contacts"]
ListEngagementsPaginatorName = Literal["list_engagements"]
ListPageReceiptsPaginatorName = Literal["list_page_receipts"]
ListPagesByContactPaginatorName = Literal["list_pages_by_contact"]
ListPagesByEngagementPaginatorName = Literal["list_pages_by_engagement"]
ReceiptTypeType = Literal["DELIVERED", "ERROR", "READ", "SENT", "STOP"]
