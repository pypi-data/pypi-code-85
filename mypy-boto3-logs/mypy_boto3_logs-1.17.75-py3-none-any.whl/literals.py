"""
Type annotations for logs service literal definitions.

[Open documentation](./literals.md)

Usage::

    ```python
    from mypy_boto3_logs.literals import DescribeDestinationsPaginatorName

    data: DescribeDestinationsPaginatorName = "describe_destinations"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeDestinationsPaginatorName",
    "DescribeExportTasksPaginatorName",
    "DescribeLogGroupsPaginatorName",
    "DescribeLogStreamsPaginatorName",
    "DescribeMetricFiltersPaginatorName",
    "DescribeQueriesPaginatorName",
    "DescribeResourcePoliciesPaginatorName",
    "DescribeSubscriptionFiltersPaginatorName",
    "DistributionType",
    "ExportTaskStatusCodeType",
    "FilterLogEventsPaginatorName",
    "OrderByType",
    "QueryStatusType",
)


DescribeDestinationsPaginatorName = Literal["describe_destinations"]
DescribeExportTasksPaginatorName = Literal["describe_export_tasks"]
DescribeLogGroupsPaginatorName = Literal["describe_log_groups"]
DescribeLogStreamsPaginatorName = Literal["describe_log_streams"]
DescribeMetricFiltersPaginatorName = Literal["describe_metric_filters"]
DescribeQueriesPaginatorName = Literal["describe_queries"]
DescribeResourcePoliciesPaginatorName = Literal["describe_resource_policies"]
DescribeSubscriptionFiltersPaginatorName = Literal["describe_subscription_filters"]
DistributionType = Literal["ByLogStream", "Random"]
ExportTaskStatusCodeType = Literal[
    "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
]
FilterLogEventsPaginatorName = Literal["filter_log_events"]
OrderByType = Literal["LastEventTime", "LogStreamName"]
QueryStatusType = Literal["Cancelled", "Complete", "Failed", "Running", "Scheduled"]
