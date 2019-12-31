# coding: utf-8

"""
    OfficeGuy API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TriggersTriggersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def triggers_triggers_subscribe(self, **kwargs):  # noqa: E501
        """Subscribe a trigger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_triggers_subscribe(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TriggersTriggersSubscribeRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseTriggersTriggersSubscribeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.triggers_triggers_subscribe_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.triggers_triggers_subscribe_with_http_info(**kwargs)  # noqa: E501
            return data

    def triggers_triggers_subscribe_with_http_info(self, **kwargs):  # noqa: E501
        """Subscribe a trigger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_triggers_subscribe_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TriggersTriggersSubscribeRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseTriggersTriggersSubscribeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'content_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method triggers_triggers_subscribe" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_language' in params:
            header_params['Content-Language'] = params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/triggers/triggers/subscribe/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseTriggersTriggersSubscribeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def triggers_triggers_unsubscribe(self, **kwargs):  # noqa: E501
        """Unsubscribe a trigger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_triggers_unsubscribe(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TriggersTriggersUnsubscribeRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseTriggersTriggersUnsubscribeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.triggers_triggers_unsubscribe_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.triggers_triggers_unsubscribe_with_http_info(**kwargs)  # noqa: E501
            return data

    def triggers_triggers_unsubscribe_with_http_info(self, **kwargs):  # noqa: E501
        """Unsubscribe a trigger  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.triggers_triggers_unsubscribe_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TriggersTriggersUnsubscribeRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseTriggersTriggersUnsubscribeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'content_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method triggers_triggers_unsubscribe" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'content_language' in params:
            header_params['Content-Language'] = params['content_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/triggers/triggers/unsubscribe/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseTriggersTriggersUnsubscribeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
