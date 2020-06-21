# office_guy_api.TriggersTriggersApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**triggers_triggers_subscribe**](TriggersTriggersApi.md#triggers_triggers_subscribe) | **POST** /api/triggers/triggers/subscribe/ | Subscribe a trigger
[**triggers_triggers_unsubscribe**](TriggersTriggersApi.md#triggers_triggers_unsubscribe) | **POST** /api/triggers/triggers/unsubscribe/ | Unsubscribe a trigger

# **triggers_triggers_subscribe**
> ResponseTriggersTriggersSubscribeResponse triggers_triggers_subscribe(body=body, content_language=content_language)

Subscribe a trigger

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.TriggersTriggersApi()
body = office_guy_api.Body253() # Body253 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Subscribe a trigger
    api_response = api_instance.triggers_triggers_subscribe(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersTriggersApi->triggers_triggers_subscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body253**](Body253.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseTriggersTriggersSubscribeResponse**](ResponseTriggersTriggersSubscribeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **triggers_triggers_unsubscribe**
> ResponseTriggersTriggersUnsubscribeResponse triggers_triggers_unsubscribe(body=body, content_language=content_language)

Unsubscribe a trigger

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.TriggersTriggersApi()
body = office_guy_api.Body257() # Body257 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Unsubscribe a trigger
    api_response = api_instance.triggers_triggers_unsubscribe(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TriggersTriggersApi->triggers_triggers_unsubscribe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body257**](Body257.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseTriggersTriggersUnsubscribeResponse**](ResponseTriggersTriggersUnsubscribeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

