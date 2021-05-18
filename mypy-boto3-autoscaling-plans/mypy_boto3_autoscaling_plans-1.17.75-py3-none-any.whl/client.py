"""
Type annotations for autoscaling-plans service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_autoscaling_plans import AutoScalingPlansClient

    client: AutoScalingPlansClient = boto3.client("autoscaling-plans")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import ForecastDataTypeType, ScalableDimensionType, ServiceNamespaceType
from .paginator import DescribeScalingPlanResourcesPaginator, DescribeScalingPlansPaginator
from .type_defs import (
    ApplicationSourceTypeDef,
    CreateScalingPlanResponseTypeDef,
    DescribeScalingPlanResourcesResponseTypeDef,
    DescribeScalingPlansResponseTypeDef,
    GetScalingPlanResourceForecastDataResponseTypeDef,
    ScalingInstructionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AutoScalingPlansClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentUpdateException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ObjectNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class AutoScalingPlansClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_scaling_plan(
        self,
        ScalingPlanName: str,
        ApplicationSource: "ApplicationSourceTypeDef",
        ScalingInstructions: List["ScalingInstructionTypeDef"],
    ) -> CreateScalingPlanResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.create_scaling_plan)
        [Show boto3-stubs documentation](./client.md#create_scaling_plan)
        """

    def delete_scaling_plan(self, ScalingPlanName: str, ScalingPlanVersion: int) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.delete_scaling_plan)
        [Show boto3-stubs documentation](./client.md#delete_scaling_plan)
        """

    def describe_scaling_plan_resources(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeScalingPlanResourcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.describe_scaling_plan_resources)
        [Show boto3-stubs documentation](./client.md#describe_scaling_plan_resources)
        """

    def describe_scaling_plans(
        self,
        ScalingPlanNames: List[str] = None,
        ScalingPlanVersion: int = None,
        ApplicationSources: List["ApplicationSourceTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeScalingPlansResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.describe_scaling_plans)
        [Show boto3-stubs documentation](./client.md#describe_scaling_plans)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_scaling_plan_resource_forecast_data(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        ServiceNamespace: ServiceNamespaceType,
        ResourceId: str,
        ScalableDimension: ScalableDimensionType,
        ForecastDataType: ForecastDataTypeType,
        StartTime: datetime,
        EndTime: datetime,
    ) -> GetScalingPlanResourceForecastDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.get_scaling_plan_resource_forecast_data)
        [Show boto3-stubs documentation](./client.md#get_scaling_plan_resource_forecast_data)
        """

    def update_scaling_plan(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        ApplicationSource: "ApplicationSourceTypeDef" = None,
        ScalingInstructions: List["ScalingInstructionTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Client.update_scaling_plan)
        [Show boto3-stubs documentation](./client.md#update_scaling_plan)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_plan_resources"]
    ) -> DescribeScalingPlanResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources)[Show boto3-stubs documentation](./paginators.md#describescalingplanresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scaling_plans"]
    ) -> DescribeScalingPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans)[Show boto3-stubs documentation](./paginators.md#describescalingplanspaginator)
        """
