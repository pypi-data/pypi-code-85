"""
Type annotations for machinelearning service client waiters.

[Open documentation](./waiters.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_machinelearning import MachineLearningClient
    from mypy_boto3_machinelearning.waiter import (
        BatchPredictionAvailableWaiter,
        DataSourceAvailableWaiter,
        EvaluationAvailableWaiter,
        MLModelAvailableWaiter,
    )

    client: MachineLearningClient = boto3.client("machinelearning")

    batch_prediction_available_waiter: BatchPredictionAvailableWaiter = client.get_waiter("batch_prediction_available")
    data_source_available_waiter: DataSourceAvailableWaiter = client.get_waiter("data_source_available")
    evaluation_available_waiter: EvaluationAvailableWaiter = client.get_waiter("evaluation_available")
    ml_model_available_waiter: MLModelAvailableWaiter = client.get_waiter("ml_model_available")
    ```
"""
from botocore.waiter import Waiter as Boto3Waiter

from .literals import (
    BatchPredictionFilterVariableType,
    DataSourceFilterVariableType,
    EvaluationFilterVariableType,
    MLModelFilterVariableType,
    SortOrderType,
)
from .type_defs import WaiterConfigTypeDef

__all__ = (
    "BatchPredictionAvailableWaiter",
    "DataSourceAvailableWaiter",
    "EvaluationAvailableWaiter",
    "MLModelAvailableWaiter",
)


class BatchPredictionAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/machinelearning.html#MachineLearning.Waiter.batch_prediction_available)[Show boto3-stubs documentation](./waiters.md#batchpredictionavailablewaiter)
    """

    def wait(
        self,
        FilterVariable: BatchPredictionFilterVariableType = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#batchpredictionavailable)
        """


class DataSourceAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/machinelearning.html#MachineLearning.Waiter.data_source_available)[Show boto3-stubs documentation](./waiters.md#datasourceavailablewaiter)
    """

    def wait(
        self,
        FilterVariable: DataSourceFilterVariableType = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#datasourceavailable)
        """


class EvaluationAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/machinelearning.html#MachineLearning.Waiter.evaluation_available)[Show boto3-stubs documentation](./waiters.md#evaluationavailablewaiter)
    """

    def wait(
        self,
        FilterVariable: EvaluationFilterVariableType = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#evaluationavailable)
        """


class MLModelAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/machinelearning.html#MachineLearning.Waiter.ml_model_available)[Show boto3-stubs documentation](./waiters.md#mlmodelavailablewaiter)
    """

    def wait(
        self,
        FilterVariable: MLModelFilterVariableType = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailableWaiter)
        [Show boto3-stubs documentation](./waiters.md#mlmodelavailable)
        """
