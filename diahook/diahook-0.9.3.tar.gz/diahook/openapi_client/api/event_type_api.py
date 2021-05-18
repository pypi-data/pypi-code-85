"""
    Diahook

    The Diahook server API documentation  # noqa: E501

    The version of the OpenAPI document: 1.4
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from diahook.openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from diahook.openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from diahook.openapi_client.model.event_type_in_out import EventTypeInOut
from diahook.openapi_client.model.http_validation_error import HTTPValidationError
from diahook.openapi_client.model.http_error_out import HttpErrorOut
from diahook.openapi_client.model.list_response_event_type_in_out import ListResponseEventTypeInOut


class EventTypeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_event_type_api_v1_event_type_post(
            self,
            event_type_in_out,
            **kwargs
        ):
            """Create Event Type  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_event_type_api_v1_event_type_post(event_type_in_out, async_req=True)
            >>> result = thread.get()

            Args:
                event_type_in_out (EventTypeInOut):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                EventTypeInOut
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['event_type_in_out'] = \
                event_type_in_out
            return self.call_with_http_info(**kwargs)

        self.create_event_type_api_v1_event_type_post = _Endpoint(
            settings={
                'response_type': (EventTypeInOut,),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/event-type/',
                'operation_id': 'create_event_type_api_v1_event_type_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'event_type_in_out',
                ],
                'required': [
                    'event_type_in_out',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'event_type_in_out':
                        (EventTypeInOut,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'event_type_in_out': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_event_type_api_v1_event_type_post
        )

        def __delete_event_type_api_v1_event_type_event_type_name_delete(
            self,
            event_type_name,
            **kwargs
        ):
            """Delete Event Type  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_event_type_api_v1_event_type_event_type_name_delete(event_type_name, async_req=True)
            >>> result = thread.get()

            Args:
                event_type_name (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['event_type_name'] = \
                event_type_name
            return self.call_with_http_info(**kwargs)

        self.delete_event_type_api_v1_event_type_event_type_name_delete = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/event-type/{event_type_name}/',
                'operation_id': 'delete_event_type_api_v1_event_type_event_type_name_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'event_type_name',
                ],
                'required': [
                    'event_type_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'event_type_name':
                        (str,),
                },
                'attribute_map': {
                    'event_type_name': 'event_type_name',
                },
                'location_map': {
                    'event_type_name': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_event_type_api_v1_event_type_event_type_name_delete
        )

        def __list_event_types_api_v1_event_type_get(
            self,
            **kwargs
        ):
            """List Event Types  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_event_types_api_v1_event_type_get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                iterator (str): [optional]
                limit (int): [optional] if omitted the server will use the default value of 50
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListResponseEventTypeInOut
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        self.list_event_types_api_v1_event_type_get = _Endpoint(
            settings={
                'response_type': (ListResponseEventTypeInOut,),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/event-type/',
                'operation_id': 'list_event_types_api_v1_event_type_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'iterator',
                    'limit',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'iterator':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'iterator': 'iterator',
                    'limit': 'limit',
                },
                'location_map': {
                    'iterator': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_event_types_api_v1_event_type_get
        )
