# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class DocumentSentimentValue(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Predicted sentiment for document (Negative, Neutral, Positive, or Mixed).
    """

    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"
    MIXED = "mixed"

class ErrorCodeValue(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Error code.
    """

    INVALID_REQUEST = "invalidRequest"
    INVALID_ARGUMENT = "invalidArgument"
    INTERNAL_SERVER_ERROR = "internalServerError"
    SERVICE_UNAVAILABLE = "serviceUnavailable"

class InnerErrorCodeValue(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Error code.
    """

    INVALID_PARAMETER_VALUE = "invalidParameterValue"
    INVALID_REQUEST_BODY_FORMAT = "invalidRequestBodyFormat"
    EMPTY_REQUEST = "emptyRequest"
    MISSING_INPUT_RECORDS = "missingInputRecords"
    INVALID_DOCUMENT = "invalidDocument"
    MODEL_VERSION_INCORRECT = "modelVersionIncorrect"
    INVALID_DOCUMENT_BATCH = "invalidDocumentBatch"
    UNSUPPORTED_LANGUAGE_CODE = "unsupportedLanguageCode"
    INVALID_COUNTRY_HINT = "invalidCountryHint"

class SentenceSentimentValue(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The predicted Sentiment for the sentence.
    """

    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"

class WarningCodeValue(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Error code.
    """

    LONG_WORDS_IN_DOCUMENT = "LongWordsInDocument"
    DOCUMENT_TRUNCATED = "DocumentTruncated"
