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


class CRMDataApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def c_rm_data_archive_entity(self, **kwargs):  # noqa: E501
        """Archive entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_archive_entity(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataArchiveEntityRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: CoreAPIEmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.c_rm_data_archive_entity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.c_rm_data_archive_entity_with_http_info(**kwargs)  # noqa: E501
            return data

    def c_rm_data_archive_entity_with_http_info(self, **kwargs):  # noqa: E501
        """Archive entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_archive_entity_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataArchiveEntityRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: CoreAPIEmptyResponse
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
                    " to method c_rm_data_archive_entity" % key
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
            '/api/crm/data/archiveentity/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CoreAPIEmptyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def c_rm_data_count_entity_usage(self, **kwargs):  # noqa: E501
        """Count entity usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_count_entity_usage(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataCountEntityUsageRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseSystemInt64
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.c_rm_data_count_entity_usage_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.c_rm_data_count_entity_usage_with_http_info(**kwargs)  # noqa: E501
            return data

    def c_rm_data_count_entity_usage_with_http_info(self, **kwargs):  # noqa: E501
        """Count entity usage  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_count_entity_usage_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataCountEntityUsageRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseSystemInt64
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
                    " to method c_rm_data_count_entity_usage" % key
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
            '/api/crm/data/countentityusage/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseSystemInt64',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def c_rm_data_create_entity(self, **kwargs):  # noqa: E501
        """Create entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_create_entity(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataCreateEntityRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCRMDataCreateEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.c_rm_data_create_entity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.c_rm_data_create_entity_with_http_info(**kwargs)  # noqa: E501
            return data

    def c_rm_data_create_entity_with_http_info(self, **kwargs):  # noqa: E501
        """Create entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_create_entity_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataCreateEntityRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCRMDataCreateEntityResponse
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
                    " to method c_rm_data_create_entity" % key
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
            '/api/crm/data/createentity/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCRMDataCreateEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def c_rm_data_delete_entity(self, **kwargs):  # noqa: E501
        """Delete entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_delete_entity(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataDeleteEntityRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: CoreAPIEmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.c_rm_data_delete_entity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.c_rm_data_delete_entity_with_http_info(**kwargs)  # noqa: E501
            return data

    def c_rm_data_delete_entity_with_http_info(self, **kwargs):  # noqa: E501
        """Delete entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_delete_entity_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataDeleteEntityRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: CoreAPIEmptyResponse
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
                    " to method c_rm_data_delete_entity" % key
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
            '/api/crm/data/deleteentity/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CoreAPIEmptyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def c_rm_data_get_entities_html(self, **kwargs):  # noqa: E501
        """Get entities HTML contents for print  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_get_entities_html(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataGetEntitiesHTMLRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.c_rm_data_get_entities_html_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.c_rm_data_get_entities_html_with_http_info(**kwargs)  # noqa: E501
            return data

    def c_rm_data_get_entities_html_with_http_info(self, **kwargs):  # noqa: E501
        """Get entities HTML contents for print  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_get_entities_html_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataGetEntitiesHTMLRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: None
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
                    " to method c_rm_data_get_entities_html" % key
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
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/crm/data/getentitieshtml/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def c_rm_data_get_entity(self, **kwargs):  # noqa: E501
        """Get entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_get_entity(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataGetEntityRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCRMDataGetEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.c_rm_data_get_entity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.c_rm_data_get_entity_with_http_info(**kwargs)  # noqa: E501
            return data

    def c_rm_data_get_entity_with_http_info(self, **kwargs):  # noqa: E501
        """Get entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_get_entity_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataGetEntityRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCRMDataGetEntityResponse
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
                    " to method c_rm_data_get_entity" % key
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
            '/api/crm/data/getentity/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCRMDataGetEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def c_rm_data_get_entity_print_html(self, **kwargs):  # noqa: E501
        """Get entity HTML contents for print  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_get_entity_print_html(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataGetEntityPrintHTMLRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.c_rm_data_get_entity_print_html_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.c_rm_data_get_entity_print_html_with_http_info(**kwargs)  # noqa: E501
            return data

    def c_rm_data_get_entity_print_html_with_http_info(self, **kwargs):  # noqa: E501
        """Get entity HTML contents for print  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_get_entity_print_html_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataGetEntityPrintHTMLRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: None
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
                    " to method c_rm_data_get_entity_print_html" % key
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
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/crm/data/getentityprinthtml/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def c_rm_data_list_entities(self, **kwargs):  # noqa: E501
        """List entities  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_list_entities(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataListEntitiesRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCRMDataListEntitiesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.c_rm_data_list_entities_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.c_rm_data_list_entities_with_http_info(**kwargs)  # noqa: E501
            return data

    def c_rm_data_list_entities_with_http_info(self, **kwargs):  # noqa: E501
        """List entities  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_list_entities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataListEntitiesRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCRMDataListEntitiesResponse
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
                    " to method c_rm_data_list_entities" % key
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
            '/api/crm/data/listentities/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCRMDataListEntitiesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def c_rm_data_update_entity(self, **kwargs):  # noqa: E501
        """Update entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_update_entity(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataUpdateEntityRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCRMDataUpdateEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.c_rm_data_update_entity_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.c_rm_data_update_entity_with_http_info(**kwargs)  # noqa: E501
            return data

    def c_rm_data_update_entity_with_http_info(self, **kwargs):  # noqa: E501
        """Update entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.c_rm_data_update_entity_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CRMDataUpdateEntityRequest request:
        :param str content_language: Sets the content response language. Defaults to Hebrew (he).
        :return: ResponseCRMDataUpdateEntityResponse
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
                    " to method c_rm_data_update_entity" % key
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
            '/api/crm/data/updateentity/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCRMDataUpdateEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
