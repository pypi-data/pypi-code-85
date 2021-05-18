"""
Type annotations for translate service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_translate import TranslateClient

    client: TranslateClient = boto3.client("translate")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from .literals import TerminologyDataFormatType
from .paginator import ListTerminologiesPaginator
from .type_defs import (
    CreateParallelDataResponseTypeDef,
    DeleteParallelDataResponseTypeDef,
    DescribeTextTranslationJobResponseTypeDef,
    EncryptionKeyTypeDef,
    GetParallelDataResponseTypeDef,
    GetTerminologyResponseTypeDef,
    ImportTerminologyResponseTypeDef,
    InputDataConfigTypeDef,
    ListParallelDataResponseTypeDef,
    ListTerminologiesResponseTypeDef,
    ListTextTranslationJobsResponseTypeDef,
    OutputDataConfigTypeDef,
    ParallelDataConfigTypeDef,
    StartTextTranslationJobResponseTypeDef,
    StopTextTranslationJobResponseTypeDef,
    TerminologyDataTypeDef,
    TextTranslationJobFilterTypeDef,
    TranslateTextResponseTypeDef,
    UpdateParallelDataResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TranslateClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DetectedLanguageLowConfidenceException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidFilterException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TextSizeLimitExceededException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnsupportedLanguagePairException: Type[BotocoreClientError]


class TranslateClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_parallel_data(
        self,
        Name: str,
        ParallelDataConfig: "ParallelDataConfigTypeDef",
        ClientToken: str,
        Description: str = None,
        EncryptionKey: "EncryptionKeyTypeDef" = None,
    ) -> CreateParallelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.create_parallel_data)
        [Show boto3-stubs documentation](./client.md#create_parallel_data)
        """

    def delete_parallel_data(self, Name: str) -> DeleteParallelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.delete_parallel_data)
        [Show boto3-stubs documentation](./client.md#delete_parallel_data)
        """

    def delete_terminology(self, Name: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.delete_terminology)
        [Show boto3-stubs documentation](./client.md#delete_terminology)
        """

    def describe_text_translation_job(
        self, JobId: str
    ) -> DescribeTextTranslationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.describe_text_translation_job)
        [Show boto3-stubs documentation](./client.md#describe_text_translation_job)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_parallel_data(self, Name: str) -> GetParallelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.get_parallel_data)
        [Show boto3-stubs documentation](./client.md#get_parallel_data)
        """

    def get_terminology(
        self, Name: str, TerminologyDataFormat: TerminologyDataFormatType
    ) -> GetTerminologyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.get_terminology)
        [Show boto3-stubs documentation](./client.md#get_terminology)
        """

    def import_terminology(
        self,
        Name: str,
        MergeStrategy: Literal["OVERWRITE"],
        TerminologyData: TerminologyDataTypeDef,
        Description: str = None,
        EncryptionKey: "EncryptionKeyTypeDef" = None,
    ) -> ImportTerminologyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.import_terminology)
        [Show boto3-stubs documentation](./client.md#import_terminology)
        """

    def list_parallel_data(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListParallelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.list_parallel_data)
        [Show boto3-stubs documentation](./client.md#list_parallel_data)
        """

    def list_terminologies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListTerminologiesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.list_terminologies)
        [Show boto3-stubs documentation](./client.md#list_terminologies)
        """

    def list_text_translation_jobs(
        self,
        Filter: TextTranslationJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTextTranslationJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.list_text_translation_jobs)
        [Show boto3-stubs documentation](./client.md#list_text_translation_jobs)
        """

    def start_text_translation_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        SourceLanguageCode: str,
        TargetLanguageCodes: List[str],
        ClientToken: str,
        JobName: str = None,
        TerminologyNames: List[str] = None,
        ParallelDataNames: List[str] = None,
    ) -> StartTextTranslationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.start_text_translation_job)
        [Show boto3-stubs documentation](./client.md#start_text_translation_job)
        """

    def stop_text_translation_job(self, JobId: str) -> StopTextTranslationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.stop_text_translation_job)
        [Show boto3-stubs documentation](./client.md#stop_text_translation_job)
        """

    def translate_text(
        self,
        Text: str,
        SourceLanguageCode: str,
        TargetLanguageCode: str,
        TerminologyNames: List[str] = None,
    ) -> TranslateTextResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.translate_text)
        [Show boto3-stubs documentation](./client.md#translate_text)
        """

    def update_parallel_data(
        self,
        Name: str,
        ParallelDataConfig: "ParallelDataConfigTypeDef",
        ClientToken: str,
        Description: str = None,
    ) -> UpdateParallelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Client.update_parallel_data)
        [Show boto3-stubs documentation](./client.md#update_parallel_data)
        """

    def get_paginator(
        self, operation_name: Literal["list_terminologies"]
    ) -> ListTerminologiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/translate.html#Translate.Paginator.ListTerminologies)[Show boto3-stubs documentation](./paginators.md#listterminologiespaginator)
        """
