"""
Type annotations for lexv2-runtime service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_lexv2_runtime import LexRuntimeV2Client

    client: LexRuntimeV2Client = boto3.client("lexv2-runtime")
    ```
"""
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import ClientMeta

from .type_defs import (
    DeleteSessionResponseTypeDef,
    GetSessionResponseTypeDef,
    MessageTypeDef,
    PutSessionResponseTypeDef,
    RecognizeTextResponseTypeDef,
    RecognizeUtteranceResponseTypeDef,
    SessionStateTypeDef,
)

__all__ = ("LexRuntimeV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadGatewayException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DependencyFailedException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LexRuntimeV2Client:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/lexv2-runtime.html#LexRuntimeV2.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def delete_session(
        self, botId: str, botAliasId: str, localeId: str, sessionId: str
    ) -> DeleteSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.delete_session)
        [Show boto3-stubs documentation](./client.md#delete_session)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_session(
        self, botId: str, botAliasId: str, localeId: str, sessionId: str
    ) -> GetSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.get_session)
        [Show boto3-stubs documentation](./client.md#get_session)
        """

    def put_session(
        self,
        botId: str,
        botAliasId: str,
        localeId: str,
        sessionId: str,
        sessionState: "SessionStateTypeDef",
        messages: List["MessageTypeDef"] = None,
        requestAttributes: Dict[str, str] = None,
        responseContentType: str = None,
    ) -> PutSessionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.put_session)
        [Show boto3-stubs documentation](./client.md#put_session)
        """

    def recognize_text(
        self,
        botId: str,
        botAliasId: str,
        localeId: str,
        sessionId: str,
        text: str,
        sessionState: "SessionStateTypeDef" = None,
        requestAttributes: Dict[str, str] = None,
    ) -> RecognizeTextResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.recognize_text)
        [Show boto3-stubs documentation](./client.md#recognize_text)
        """

    def recognize_utterance(
        self,
        botId: str,
        botAliasId: str,
        localeId: str,
        sessionId: str,
        requestContentType: str,
        sessionState: str = None,
        requestAttributes: str = None,
        responseContentType: str = None,
        inputStream: Union[bytes, IO[bytes]] = None,
    ) -> RecognizeUtteranceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/lexv2-runtime.html#LexRuntimeV2.Client.recognize_utterance)
        [Show boto3-stubs documentation](./client.md#recognize_utterance)
        """
