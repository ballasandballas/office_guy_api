# office_guy_api.WebsitePermissionsApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**website_permissions_remove**](WebsitePermissionsApi.md#website_permissions_remove) | **POST** /api/website/permissions/remove/ | Remove user permission
[**website_permissions_set**](WebsitePermissionsApi.md#website_permissions_set) | **POST** /api/website/permissions/set/ | Grant user permission

# **website_permissions_remove**
> CoreAPIEmptyResponse website_permissions_remove(body=body, content_language=content_language)

Remove user permission

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsitePermissionsApi()
body = office_guy_api.Body293() # Body293 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Remove user permission
    api_response = api_instance.website_permissions_remove(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitePermissionsApi->website_permissions_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body293**](Body293.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**CoreAPIEmptyResponse**](CoreAPIEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_permissions_set**
> CoreAPIEmptyResponse website_permissions_set(body=body, content_language=content_language)

Grant user permission

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsitePermissionsApi()
body = office_guy_api.Body289() # Body289 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Grant user permission
    api_response = api_instance.website_permissions_set(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitePermissionsApi->website_permissions_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body289**](Body289.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**CoreAPIEmptyResponse**](CoreAPIEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

