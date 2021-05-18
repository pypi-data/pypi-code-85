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
from diahook.openapi_client.model.http_validation_error import HTTPValidationError
from diahook.openapi_client.model.http_error_out import HttpErrorOut
from diahook.openapi_client.model.list_response_message_out import ListResponseMessageOut
from diahook.openapi_client.model.message_in import MessageIn
from diahook.openapi_client.model.message_out import MessageOut


class MessageApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_message_api_v1_app_app_id_msg_post(
            self,
            app_id,
            message_in,
            **kwargs
        ):
            """Create Message  # noqa: E501

            Creates a new message and schedules it to be sent. If the message includes an `event_id` and a message with this id already exists, a 409 conflict error will be returned.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_message_api_v1_app_app_id_msg_post(app_id, message_in, async_req=True)
            >>> result = thread.get()

            Args:
                app_id (str):
                message_in (MessageIn):

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
                MessageOut
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
            kwargs['app_id'] = \
                app_id
            kwargs['message_in'] = \
                message_in
            return self.call_with_http_info(**kwargs)

        self.create_message_api_v1_app_app_id_msg_post = _Endpoint(
            settings={
                'response_type': (MessageOut,),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/app/{app_id}/msg/',
                'operation_id': 'create_message_api_v1_app_app_id_msg_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_id',
                    'message_in',
                ],
                'required': [
                    'app_id',
                    'message_in',
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
                    'app_id':
                        (str,),
                    'message_in':
                        (MessageIn,),
                },
                'attribute_map': {
                    'app_id': 'app_id',
                },
                'location_map': {
                    'app_id': 'path',
                    'message_in': 'body',
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
            callable=__create_message_api_v1_app_app_id_msg_post
        )

        def __get_message_api_v1_app_app_id_msg_msg_id_get(
            self,
            msg_id,
            app_id,
            **kwargs
        ):
            """Get Message  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_message_api_v1_app_app_id_msg_msg_id_get(msg_id, app_id, async_req=True)
            >>> result = thread.get()

            Args:
                msg_id (str):
                app_id (str):

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
                MessageOut
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
            kwargs['msg_id'] = \
                msg_id
            kwargs['app_id'] = \
                app_id
            return self.call_with_http_info(**kwargs)

        self.get_message_api_v1_app_app_id_msg_msg_id_get = _Endpoint(
            settings={
                'response_type': (MessageOut,),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/app/{app_id}/msg/{msg_id}/',
                'operation_id': 'get_message_api_v1_app_app_id_msg_msg_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'msg_id',
                    'app_id',
                ],
                'required': [
                    'msg_id',
                    'app_id',
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
                    'msg_id':
                        (str,),
                    'app_id':
                        (str,),
                },
                'attribute_map': {
                    'msg_id': 'msg_id',
                    'app_id': 'app_id',
                },
                'location_map': {
                    'msg_id': 'path',
                    'app_id': 'path',
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
            callable=__get_message_api_v1_app_app_id_msg_msg_id_get
        )

        def __list_messages_api_v1_app_app_id_msg_get(
            self,
            app_id,
            **kwargs
        ):
            """List Messages  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_messages_api_v1_app_app_id_msg_get(app_id, async_req=True)
            >>> result = thread.get()

            Args:
                app_id (str):

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
                ListResponseMessageOut
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
            kwargs['app_id'] = \
                app_id
            return self.call_with_http_info(**kwargs)

        self.list_messages_api_v1_app_app_id_msg_get = _Endpoint(
            settings={
                'response_type': (ListResponseMessageOut,),
                'auth': [
                    'HTTPBearer'
                ],
                'endpoint_path': '/api/v1/app/{app_id}/msg/',
                'operation_id': 'list_messages_api_v1_app_app_id_msg_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'app_id',
                    'iterator',
                    'limit',
                ],
                'required': [
                    'app_id',
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
                    'app_id':
                        (str,),
                    'iterator':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'app_id': 'app_id',
                    'iterator': 'iterator',
                    'limit': 'limit',
                },
                'location_map': {
                    'app_id': 'path',
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
            callable=__list_messages_api_v1_app_app_id_msg_get
        )
