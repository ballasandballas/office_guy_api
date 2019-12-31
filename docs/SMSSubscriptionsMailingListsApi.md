# swagger_client.SMSSubscriptionsMailingListsApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s_ms_mailing_lists_add**](SMSSubscriptionsMailingListsApi.md#s_ms_mailing_lists_add) | **POST** /api/sms/mailinglists/add/ | Add recipient to a mailing list
[**s_ms_mailing_lists_list**](SMSSubscriptionsMailingListsApi.md#s_ms_mailing_lists_list) | **POST** /api/sms/mailinglists/list/ | List mailing lists


# **s_ms_mailing_lists_add**
> ResponseSMSMailingListsAddResponse s_ms_mailing_lists_add(request=request, content_language=content_language)

Add recipient to a mailing list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SMSSubscriptionsMailingListsApi()
request = swagger_client.SMSMailingListsAddRequest() # SMSMailingListsAddRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Add recipient to a mailing list
    api_response = api_instance.s_ms_mailing_lists_add(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSSubscriptionsMailingListsApi->s_ms_mailing_lists_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SMSMailingListsAddRequest**](SMSMailingListsAddRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseSMSMailingListsAddResponse**](ResponseSMSMailingListsAddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_ms_mailing_lists_list**
> ResponseSMSMailingListListResponse s_ms_mailing_lists_list(request=request, content_language=content_language)

List mailing lists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SMSSubscriptionsMailingListsApi()
request = swagger_client.SMSMailingListsListRequest() # SMSMailingListsListRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # List mailing lists
    api_response = api_instance.s_ms_mailing_lists_list(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSSubscriptionsMailingListsApi->s_ms_mailing_lists_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SMSMailingListsListRequest**](SMSMailingListsListRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseSMSMailingListListResponse**](ResponseSMSMailingListListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

