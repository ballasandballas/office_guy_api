# swagger_client.CRMDataApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c_rm_data_archive_entity**](CRMDataApi.md#c_rm_data_archive_entity) | **POST** /api/crm/data/archiveentity/ | Archive entity
[**c_rm_data_count_entity_usage**](CRMDataApi.md#c_rm_data_count_entity_usage) | **POST** /api/crm/data/countentityusage/ | Count entity usage
[**c_rm_data_create_entity**](CRMDataApi.md#c_rm_data_create_entity) | **POST** /api/crm/data/createentity/ | Create entity
[**c_rm_data_delete_entity**](CRMDataApi.md#c_rm_data_delete_entity) | **POST** /api/crm/data/deleteentity/ | Delete entity
[**c_rm_data_get_entities_html**](CRMDataApi.md#c_rm_data_get_entities_html) | **POST** /api/crm/data/getentitieshtml/ | Get entities HTML contents for print
[**c_rm_data_get_entity**](CRMDataApi.md#c_rm_data_get_entity) | **POST** /api/crm/data/getentity/ | Get entity
[**c_rm_data_get_entity_print_html**](CRMDataApi.md#c_rm_data_get_entity_print_html) | **POST** /api/crm/data/getentityprinthtml/ | Get entity HTML contents for print
[**c_rm_data_list_entities**](CRMDataApi.md#c_rm_data_list_entities) | **POST** /api/crm/data/listentities/ | List entities
[**c_rm_data_update_entity**](CRMDataApi.md#c_rm_data_update_entity) | **POST** /api/crm/data/updateentity/ | Update entity


# **c_rm_data_archive_entity**
> CoreAPIEmptyResponse c_rm_data_archive_entity(request=request, content_language=content_language)

Archive entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CRMDataApi()
request = swagger_client.CRMDataArchiveEntityRequest() # CRMDataArchiveEntityRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Archive entity
    api_response = api_instance.c_rm_data_archive_entity(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMDataApi->c_rm_data_archive_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMDataArchiveEntityRequest**](CRMDataArchiveEntityRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**CoreAPIEmptyResponse**](CoreAPIEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_rm_data_count_entity_usage**
> ResponseSystemInt64 c_rm_data_count_entity_usage(request=request, content_language=content_language)

Count entity usage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CRMDataApi()
request = swagger_client.CRMDataCountEntityUsageRequest() # CRMDataCountEntityUsageRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Count entity usage
    api_response = api_instance.c_rm_data_count_entity_usage(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMDataApi->c_rm_data_count_entity_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMDataCountEntityUsageRequest**](CRMDataCountEntityUsageRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseSystemInt64**](ResponseSystemInt64.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_rm_data_create_entity**
> ResponseCRMDataCreateEntityResponse c_rm_data_create_entity(request=request, content_language=content_language)

Create entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CRMDataApi()
request = swagger_client.CRMDataCreateEntityRequest() # CRMDataCreateEntityRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Create entity
    api_response = api_instance.c_rm_data_create_entity(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMDataApi->c_rm_data_create_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMDataCreateEntityRequest**](CRMDataCreateEntityRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCRMDataCreateEntityResponse**](ResponseCRMDataCreateEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_rm_data_delete_entity**
> CoreAPIEmptyResponse c_rm_data_delete_entity(request=request, content_language=content_language)

Delete entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CRMDataApi()
request = swagger_client.CRMDataDeleteEntityRequest() # CRMDataDeleteEntityRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Delete entity
    api_response = api_instance.c_rm_data_delete_entity(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMDataApi->c_rm_data_delete_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMDataDeleteEntityRequest**](CRMDataDeleteEntityRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**CoreAPIEmptyResponse**](CoreAPIEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_rm_data_get_entities_html**
> c_rm_data_get_entities_html(request=request, content_language=content_language)

Get entities HTML contents for print

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CRMDataApi()
request = swagger_client.CRMDataGetEntitiesHTMLRequest() # CRMDataGetEntitiesHTMLRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get entities HTML contents for print
    api_instance.c_rm_data_get_entities_html(request=request, content_language=content_language)
except ApiException as e:
    print("Exception when calling CRMDataApi->c_rm_data_get_entities_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMDataGetEntitiesHTMLRequest**](CRMDataGetEntitiesHTMLRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_rm_data_get_entity**
> ResponseCRMDataGetEntityResponse c_rm_data_get_entity(request=request, content_language=content_language)

Get entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CRMDataApi()
request = swagger_client.CRMDataGetEntityRequest() # CRMDataGetEntityRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get entity
    api_response = api_instance.c_rm_data_get_entity(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMDataApi->c_rm_data_get_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMDataGetEntityRequest**](CRMDataGetEntityRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCRMDataGetEntityResponse**](ResponseCRMDataGetEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_rm_data_get_entity_print_html**
> c_rm_data_get_entity_print_html(request=request, content_language=content_language)

Get entity HTML contents for print

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CRMDataApi()
request = swagger_client.CRMDataGetEntityPrintHTMLRequest() # CRMDataGetEntityPrintHTMLRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get entity HTML contents for print
    api_instance.c_rm_data_get_entity_print_html(request=request, content_language=content_language)
except ApiException as e:
    print("Exception when calling CRMDataApi->c_rm_data_get_entity_print_html: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMDataGetEntityPrintHTMLRequest**](CRMDataGetEntityPrintHTMLRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_rm_data_list_entities**
> ResponseCRMDataListEntitiesResponse c_rm_data_list_entities(request=request, content_language=content_language)

List entities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CRMDataApi()
request = swagger_client.CRMDataListEntitiesRequest() # CRMDataListEntitiesRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # List entities
    api_response = api_instance.c_rm_data_list_entities(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMDataApi->c_rm_data_list_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMDataListEntitiesRequest**](CRMDataListEntitiesRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCRMDataListEntitiesResponse**](ResponseCRMDataListEntitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_rm_data_update_entity**
> ResponseCRMDataUpdateEntityResponse c_rm_data_update_entity(request=request, content_language=content_language)

Update entity

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CRMDataApi()
request = swagger_client.CRMDataUpdateEntityRequest() # CRMDataUpdateEntityRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Update entity
    api_response = api_instance.c_rm_data_update_entity(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CRMDataApi->c_rm_data_update_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CRMDataUpdateEntityRequest**](CRMDataUpdateEntityRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCRMDataUpdateEntityResponse**](ResponseCRMDataUpdateEntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

