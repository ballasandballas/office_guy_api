# swagger_client.EmailSubscriptionsMailingListsApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_subscriptions_mailing_lists_add**](EmailSubscriptionsMailingListsApi.md#email_subscriptions_mailing_lists_add) | **POST** /api/emailsubscriptions/mailinglists/add/ | 
[**email_subscriptions_mailing_lists_list**](EmailSubscriptionsMailingListsApi.md#email_subscriptions_mailing_lists_list) | **POST** /api/emailsubscriptions/mailinglists/list/ | 


# **email_subscriptions_mailing_lists_add**
> ResponseEmailSubscriptionsMailingListsAddResponse email_subscriptions_mailing_lists_add(request=request, content_language=content_language)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailSubscriptionsMailingListsApi()
request = swagger_client.EmailSubscriptionsMailingListsAddRequest() # EmailSubscriptionsMailingListsAddRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    api_response = api_instance.email_subscriptions_mailing_lists_add(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailSubscriptionsMailingListsApi->email_subscriptions_mailing_lists_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailSubscriptionsMailingListsAddRequest**](EmailSubscriptionsMailingListsAddRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseEmailSubscriptionsMailingListsAddResponse**](ResponseEmailSubscriptionsMailingListsAddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_subscriptions_mailing_lists_list**
> ResponseEmailSubscriptionsMailingListsListResponse email_subscriptions_mailing_lists_list(request=request, content_language=content_language)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailSubscriptionsMailingListsApi()
request = swagger_client.EmailSubscriptionsMailingListsListRequest() # EmailSubscriptionsMailingListsListRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    api_response = api_instance.email_subscriptions_mailing_lists_list(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailSubscriptionsMailingListsApi->email_subscriptions_mailing_lists_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**EmailSubscriptionsMailingListsListRequest**](EmailSubscriptionsMailingListsListRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseEmailSubscriptionsMailingListsListResponse**](ResponseEmailSubscriptionsMailingListsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

