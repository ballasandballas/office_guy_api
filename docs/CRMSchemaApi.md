# swagger_client.CRMSchemaApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c_rm_schema_get_folder**](CRMSchemaApi.md#c_rm_schema_get_folder) | **POST** /api/crm/schema/getfolder/ | Get folder details
[**c_rm_schema_list_folders**](CRMSchemaApi.md#c_rm_schema_list_folders) | **POST** /api/crm/schema/listfolders/ | List folders


# **c_rm_schema_get_folder**
> ResponseCRMSchemaGetFolderResponse c_rm_schema_get_folder(request=request, content_language=content_language)

Get folder details

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.CRMSchemaApi()
request = office_guy_api.CRMSchemaGetFolderRequest() # CRMSchemaGetFolderRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get folder details
    api_response = api_instance.c_rm_schema_get_folder(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMSchemaApi->c_rm_schema_get_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMSchemaGetFolderRequest**](CRMSchemaGetFolderRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCRMSchemaGetFolderResponse**](ResponseCRMSchemaGetFolderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_rm_schema_list_folders**
> ResponseCRMSchemaListFoldersResponse c_rm_schema_list_folders(request=request, content_language=content_language)

List folders

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.CRMSchemaApi()
request = office_guy_api.CRMSchemaListFoldersRequest() # CRMSchemaListFoldersRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # List folders
    api_response = api_instance.c_rm_schema_list_folders(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMSchemaApi->c_rm_schema_list_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMSchemaListFoldersRequest**](CRMSchemaListFoldersRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCRMSchemaListFoldersResponse**](ResponseCRMSchemaListFoldersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

