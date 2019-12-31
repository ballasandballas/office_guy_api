# swagger_client.SMSSubscriptionsSMSApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s_mssms_list_senders**](SMSSubscriptionsSMSApi.md#s_mssms_list_senders) | **POST** /api/sms/sms/listsenders/ | List verified sender numbers
[**s_mssms_send**](SMSSubscriptionsSMSApi.md#s_mssms_send) | **POST** /api/sms/sms/send/ | Sends a single SMS message
[**s_mssms_send_multiple**](SMSSubscriptionsSMSApi.md#s_mssms_send_multiple) | **POST** /api/sms/sms/sendmultiple/ | Sends multiple SMS messages


# **s_mssms_list_senders**
> ResponseSMSSMSListSendersResponse s_mssms_list_senders(request=request, content_language=content_language)

List verified sender numbers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SMSSubscriptionsSMSApi()
request = swagger_client.SMSSMSListSendersRequest() # SMSSMSListSendersRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # List verified sender numbers
    api_response = api_instance.s_mssms_list_senders(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSSubscriptionsSMSApi->s_mssms_list_senders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SMSSMSListSendersRequest**](SMSSMSListSendersRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseSMSSMSListSendersResponse**](ResponseSMSSMSListSendersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_mssms_send**
> ResponseSMSSMSSendResponse s_mssms_send(request=request, content_language=content_language)

Sends a single SMS message

When possible, SendMultiple should be used

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SMSSubscriptionsSMSApi()
request = swagger_client.SMSSMSSendRequest() # SMSSMSSendRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Sends a single SMS message
    api_response = api_instance.s_mssms_send(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSSubscriptionsSMSApi->s_mssms_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SMSSMSSendRequest**](SMSSMSSendRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseSMSSMSSendResponse**](ResponseSMSSMSSendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_mssms_send_multiple**
> ResponseSMSSMSSendMultipleResponse s_mssms_send_multiple(request=request, content_language=content_language)

Sends multiple SMS messages

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SMSSubscriptionsSMSApi()
request = swagger_client.SMSSMSSendMultipleRequest() # SMSSMSSendMultipleRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Sends multiple SMS messages
    api_response = api_instance.s_mssms_send_multiple(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSSubscriptionsSMSApi->s_mssms_send_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**SMSSMSSendMultipleRequest**](SMSSMSSendMultipleRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseSMSSMSSendMultipleResponse**](ResponseSMSSMSSendMultipleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

