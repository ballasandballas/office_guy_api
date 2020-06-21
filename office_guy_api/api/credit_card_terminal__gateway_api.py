# coding: utf-8

"""
    OfficeGuy API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2020-06-20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from office_guy_api.api_client import ApiClient


class CreditCardTerminalGatewayApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def credit_guy_gateway_begin_redirect(self, **kwargs):  # noqa: E501
        """Begin redirect for transaction  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credit_guy_gateway_begin_redirect(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body80 body:
        :param ContentLanguage content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCreditGuyGatewayBeginRedirectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.credit_guy_gateway_begin_redirect_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.credit_guy_gateway_begin_redirect_with_http_info(**kwargs)  # noqa: E501
            return data

    def credit_guy_gateway_begin_redirect_with_http_info(self, **kwargs):  # noqa: E501
        """Begin redirect for transaction  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credit_guy_gateway_begin_redirect_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body80 body:
        :param ContentLanguage content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCreditGuyGatewayBeginRedirectResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'content_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credit_guy_gateway_begin_redirect" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/creditguy/gateway/beginredirect/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCreditGuyGatewayBeginRedirectResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def credit_guy_gateway_get_reference_numbers(self, **kwargs):  # noqa: E501
        """Get reference numbers for existing transactions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credit_guy_gateway_get_reference_numbers(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body84 body:
        :param ContentLanguage content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCreditGuyGatewayGetReferenceNumbersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.credit_guy_gateway_get_reference_numbers_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.credit_guy_gateway_get_reference_numbers_with_http_info(**kwargs)  # noqa: E501
            return data

    def credit_guy_gateway_get_reference_numbers_with_http_info(self, **kwargs):  # noqa: E501
        """Get reference numbers for existing transactions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credit_guy_gateway_get_reference_numbers_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body84 body:
        :param ContentLanguage content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCreditGuyGatewayGetReferenceNumbersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'content_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credit_guy_gateway_get_reference_numbers" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/creditguy/gateway/getreferencenumbers/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCreditGuyGatewayGetReferenceNumbersResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def credit_guy_gateway_get_transaction(self, **kwargs):  # noqa: E501
        """Get existing transaction details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credit_guy_gateway_get_transaction(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body76 body:
        :param ContentLanguage content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCreditGuyGatewayGetTransactionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.credit_guy_gateway_get_transaction_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.credit_guy_gateway_get_transaction_with_http_info(**kwargs)  # noqa: E501
            return data

    def credit_guy_gateway_get_transaction_with_http_info(self, **kwargs):  # noqa: E501
        """Get existing transaction details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credit_guy_gateway_get_transaction_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body76 body:
        :param ContentLanguage content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCreditGuyGatewayGetTransactionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'content_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credit_guy_gateway_get_transaction" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/creditguy/gateway/gettransaction/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCreditGuyGatewayGetTransactionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def credit_guy_gateway_transaction(self, **kwargs):  # noqa: E501
        """Credit card transaction  # noqa: E501

        This method should be used in rare occasions.  For common use scenarios, refer to \"Payments -> Charge customer\" method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credit_guy_gateway_transaction(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body72 body:
        :param ContentLanguage content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCreditGuyGatewayTransactionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.credit_guy_gateway_transaction_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.credit_guy_gateway_transaction_with_http_info(**kwargs)  # noqa: E501
            return data

    def credit_guy_gateway_transaction_with_http_info(self, **kwargs):  # noqa: E501
        """Credit card transaction  # noqa: E501

        This method should be used in rare occasions.  For common use scenarios, refer to \"Payments -> Charge customer\" method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credit_guy_gateway_transaction_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body72 body:
        :param ContentLanguage content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCreditGuyGatewayTransactionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'content_language']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credit_guy_gateway_transaction" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/creditguy/gateway/transaction/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCreditGuyGatewayTransactionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
