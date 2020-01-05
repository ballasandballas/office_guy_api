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

from office_guy_api.api_client import ApiClient


class PaymentsPaymentMethodsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def billing_payment_methods_get_for_customer(self, **kwargs):  # noqa: E501
        """Get payment details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_payment_methods_get_for_customer(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BillingPaymentMethodsGetForCustomerRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseBillingPaymentMethodsGetForCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.billing_payment_methods_get_for_customer_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.billing_payment_methods_get_for_customer_with_http_info(**kwargs)  # noqa: E501
            return data

    def billing_payment_methods_get_for_customer_with_http_info(self, **kwargs):  # noqa: E501
        """Get payment details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_payment_methods_get_for_customer_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BillingPaymentMethodsGetForCustomerRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseBillingPaymentMethodsGetForCustomerResponse
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
                    " to method billing_payment_methods_get_for_customer" % key
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
            '/api/billing/paymentmethods/getforcustomer/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseBillingPaymentMethodsGetForCustomerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def billing_payment_methods_remove(self, **kwargs):  # noqa: E501
        """Remove payment details from existing customer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_payment_methods_remove(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BillingPaymentMethodsRemoveRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseBillingPaymentMethodsRemoveResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.billing_payment_methods_remove_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.billing_payment_methods_remove_with_http_info(**kwargs)  # noqa: E501
            return data

    def billing_payment_methods_remove_with_http_info(self, **kwargs):  # noqa: E501
        """Remove payment details from existing customer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_payment_methods_remove_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BillingPaymentMethodsRemoveRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseBillingPaymentMethodsRemoveResponse
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
                    " to method billing_payment_methods_remove" % key
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
            '/api/billing/paymentmethods/remove/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseBillingPaymentMethodsRemoveResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def billing_payment_methods_set_for_customer(self, **kwargs):  # noqa: E501
        """Set payment details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_payment_methods_set_for_customer(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BillingPaymentMethodsSetForCustomerRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseBillingPaymentMethodsSetForCustomerResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.billing_payment_methods_set_for_customer_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.billing_payment_methods_set_for_customer_with_http_info(**kwargs)  # noqa: E501
            return data

    def billing_payment_methods_set_for_customer_with_http_info(self, **kwargs):  # noqa: E501
        """Set payment details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.billing_payment_methods_set_for_customer_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BillingPaymentMethodsSetForCustomerRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseBillingPaymentMethodsSetForCustomerResponse
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
                    " to method billing_payment_methods_set_for_customer" % key
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
            '/api/billing/paymentmethods/setforcustomer/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseBillingPaymentMethodsSetForCustomerResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)