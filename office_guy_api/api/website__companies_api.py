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


class WebsiteCompaniesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def website_companies_create(self, **kwargs):  # noqa: E501
        """Create new organization  # noqa: E501

        Created organization payment method, will be set to the calling organization payment method.  This method requires an active payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesCreateRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.website_companies_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.website_companies_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def website_companies_create_with_http_info(self, **kwargs):  # noqa: E501
        """Create new organization  # noqa: E501

        Created organization payment method, will be set to the calling organization payment method.  This method requires an active payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesCreateRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesCreateResponse
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
                    " to method website_companies_create" % key
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
            '/api/website/companies/create/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseWebsiteCompaniesCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def website_companies_get_details(self, **kwargs):  # noqa: E501
        """Get organization details  # noqa: E501

        This method can be used to make sure the correct organization ID is used, when multiple companies are in use.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_get_details(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesGetDetailsRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesGetDetailsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.website_companies_get_details_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.website_companies_get_details_with_http_info(**kwargs)  # noqa: E501
            return data

    def website_companies_get_details_with_http_info(self, **kwargs):  # noqa: E501
        """Get organization details  # noqa: E501

        This method can be used to make sure the correct organization ID is used, when multiple companies are in use.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_get_details_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesGetDetailsRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesGetDetailsResponse
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
                    " to method website_companies_get_details" % key
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
            '/api/website/companies/getdetails/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseWebsiteCompaniesGetDetailsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def website_companies_install_additions(self, **kwargs):  # noqa: E501
        """Install additions  # noqa: E501

        Please note this method requires an active payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_install_additions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesInstallAdditionsRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesInstallAdditionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.website_companies_install_additions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.website_companies_install_additions_with_http_info(**kwargs)  # noqa: E501
            return data

    def website_companies_install_additions_with_http_info(self, **kwargs):  # noqa: E501
        """Install additions  # noqa: E501

        Please note this method requires an active payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_install_additions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesInstallAdditionsRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesInstallAdditionsResponse
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
                    " to method website_companies_install_additions" % key
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
            '/api/website/companies/installadditions/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseWebsiteCompaniesInstallAdditionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def website_companies_install_applications(self, **kwargs):  # noqa: E501
        """Install applications  # noqa: E501

        Please note this method requires an active payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_install_applications(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesInstallApplicationsRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesInstallApplicationsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.website_companies_install_applications_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.website_companies_install_applications_with_http_info(**kwargs)  # noqa: E501
            return data

    def website_companies_install_applications_with_http_info(self, **kwargs):  # noqa: E501
        """Install applications  # noqa: E501

        Please note this method requires an active payment method.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_install_applications_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesInstallApplicationsRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesInstallApplicationsResponse
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
                    " to method website_companies_install_applications" % key
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
            '/api/website/companies/installapplications/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseWebsiteCompaniesInstallApplicationsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def website_companies_remove_additions(self, **kwargs):  # noqa: E501
        """Removes additions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_remove_additions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesRemoveAdditionsRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesRemoveAdditionsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.website_companies_remove_additions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.website_companies_remove_additions_with_http_info(**kwargs)  # noqa: E501
            return data

    def website_companies_remove_additions_with_http_info(self, **kwargs):  # noqa: E501
        """Removes additions  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_remove_additions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesRemoveAdditionsRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesRemoveAdditionsResponse
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
                    " to method website_companies_remove_additions" % key
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
            '/api/website/companies/removeadditions/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseWebsiteCompaniesRemoveAdditionsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def website_companies_update(self, **kwargs):  # noqa: E501
        """Update organization details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_update(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesUpdateRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.website_companies_update_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.website_companies_update_with_http_info(**kwargs)  # noqa: E501
            return data

    def website_companies_update_with_http_info(self, **kwargs):  # noqa: E501
        """Update organization details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.website_companies_update_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebsiteCompaniesUpdateRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseWebsiteCompaniesUpdateResponse
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
                    " to method website_companies_update" % key
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
            '/api/website/companies/update/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseWebsiteCompaniesUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def website_companies_update_quota(self, **kwargs):  # noqa: E501
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
                    " to method website_companies_update" % key
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
            '/api/website/companies/updatequota/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCompanyUpdateQuota',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
