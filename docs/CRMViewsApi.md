# swagger_client.CRMViewsApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c_rm_views_list_views**](CRMViewsApi.md#c_rm_views_list_views) | **POST** /api/crm/views/listviews/ | List views


# **c_rm_views_list_views**
> ResponseCRMViewsListViewsResponse c_rm_views_list_views(request=request, content_language=content_language)

List views

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.CRMViewsApi()
request = office_guy_api.CRMViewsListViewsRequest() # CRMViewsListViewsRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # List views
    api_response = api_instance.c_rm_views_list_views(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMViewsApi->c_rm_views_list_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMViewsListViewsRequest**](CRMViewsListViewsRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCRMViewsListViewsResponse**](ResponseCRMViewsListViewsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

