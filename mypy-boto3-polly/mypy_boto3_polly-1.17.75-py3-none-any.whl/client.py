"""
Type annotations for polly service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_polly import PollyClient

    client: PollyClient = boto3.client("polly")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from .literals import (
    EngineType,
    LanguageCodeType,
    OutputFormatType,
    SpeechMarkTypeType,
    TaskStatusType,
    TextTypeType,
    VoiceIdType,
)
from .paginator import (
    DescribeVoicesPaginator,
    ListLexiconsPaginator,
    ListSpeechSynthesisTasksPaginator,
)
from .type_defs import (
    DescribeVoicesOutputTypeDef,
    GetLexiconOutputTypeDef,
    GetSpeechSynthesisTaskOutputTypeDef,
    ListLexiconsOutputTypeDef,
    ListSpeechSynthesisTasksOutputTypeDef,
    StartSpeechSynthesisTaskOutputTypeDef,
    SynthesizeSpeechOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PollyClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    EngineNotSupportedException: Type[BotocoreClientError]
    InvalidLexiconException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidS3BucketException: Type[BotocoreClientError]
    InvalidS3KeyException: Type[BotocoreClientError]
    InvalidSampleRateException: Type[BotocoreClientError]
    InvalidSnsTopicArnException: Type[BotocoreClientError]
    InvalidSsmlException: Type[BotocoreClientError]
    InvalidTaskIdException: Type[BotocoreClientError]
    LanguageNotSupportedException: Type[BotocoreClientError]
    LexiconNotFoundException: Type[BotocoreClientError]
    LexiconSizeExceededException: Type[BotocoreClientError]
    MarksNotSupportedForFormatException: Type[BotocoreClientError]
    MaxLexemeLengthExceededException: Type[BotocoreClientError]
    MaxLexiconsNumberExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    SsmlMarksNotSupportedForTextTypeException: Type[BotocoreClientError]
    SynthesisTaskNotFoundException: Type[BotocoreClientError]
    TextLengthExceededException: Type[BotocoreClientError]
    UnsupportedPlsAlphabetException: Type[BotocoreClientError]
    UnsupportedPlsLanguageException: Type[BotocoreClientError]


class PollyClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def delete_lexicon(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.delete_lexicon)
        [Show boto3-stubs documentation](./client.md#delete_lexicon)
        """

    def describe_voices(
        self,
        Engine: EngineType = None,
        LanguageCode: LanguageCodeType = None,
        IncludeAdditionalLanguageCodes: bool = None,
        NextToken: str = None,
    ) -> DescribeVoicesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.describe_voices)
        [Show boto3-stubs documentation](./client.md#describe_voices)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_lexicon(self, Name: str) -> GetLexiconOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.get_lexicon)
        [Show boto3-stubs documentation](./client.md#get_lexicon)
        """

    def get_speech_synthesis_task(self, TaskId: str) -> GetSpeechSynthesisTaskOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.get_speech_synthesis_task)
        [Show boto3-stubs documentation](./client.md#get_speech_synthesis_task)
        """

    def list_lexicons(self, NextToken: str = None) -> ListLexiconsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.list_lexicons)
        [Show boto3-stubs documentation](./client.md#list_lexicons)
        """

    def list_speech_synthesis_tasks(
        self, MaxResults: int = None, NextToken: str = None, Status: TaskStatusType = None
    ) -> ListSpeechSynthesisTasksOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.list_speech_synthesis_tasks)
        [Show boto3-stubs documentation](./client.md#list_speech_synthesis_tasks)
        """

    def put_lexicon(self, Name: str, Content: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.put_lexicon)
        [Show boto3-stubs documentation](./client.md#put_lexicon)
        """

    def start_speech_synthesis_task(
        self,
        OutputFormat: OutputFormatType,
        OutputS3BucketName: str,
        Text: str,
        VoiceId: VoiceIdType,
        Engine: EngineType = None,
        LanguageCode: LanguageCodeType = None,
        LexiconNames: List[str] = None,
        OutputS3KeyPrefix: str = None,
        SampleRate: str = None,
        SnsTopicArn: str = None,
        SpeechMarkTypes: List[SpeechMarkTypeType] = None,
        TextType: TextTypeType = None,
    ) -> StartSpeechSynthesisTaskOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.start_speech_synthesis_task)
        [Show boto3-stubs documentation](./client.md#start_speech_synthesis_task)
        """

    def synthesize_speech(
        self,
        OutputFormat: OutputFormatType,
        Text: str,
        VoiceId: VoiceIdType,
        Engine: EngineType = None,
        LanguageCode: LanguageCodeType = None,
        LexiconNames: List[str] = None,
        SampleRate: str = None,
        SpeechMarkTypes: List[SpeechMarkTypeType] = None,
        TextType: TextTypeType = None,
    ) -> SynthesizeSpeechOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Client.synthesize_speech)
        [Show boto3-stubs documentation](./client.md#synthesize_speech)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_voices"]) -> DescribeVoicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Paginator.DescribeVoices)[Show boto3-stubs documentation](./paginators.md#describevoicespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_lexicons"]) -> ListLexiconsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Paginator.ListLexicons)[Show boto3-stubs documentation](./paginators.md#listlexiconspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_speech_synthesis_tasks"]
    ) -> ListSpeechSynthesisTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks)[Show boto3-stubs documentation](./paginators.md#listspeechsynthesistaskspaginator)
        """
