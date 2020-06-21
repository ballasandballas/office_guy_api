# office_guy_api.SMSSubscriptionsSMSApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s_mssms_list_senders**](SMSSubscriptionsSMSApi.md#s_mssms_list_senders) | **POST** /api/sms/sms/listsenders/ | List verified sender numbers
[**s_mssms_send**](SMSSubscriptionsSMSApi.md#s_mssms_send) | **POST** /api/sms/sms/send/ | Sends a single SMS message
[**s_mssms_send_multiple**](SMSSubscriptionsSMSApi.md#s_mssms_send_multiple) | **POST** /api/sms/sms/sendmultiple/ | Sends multiple SMS messages

# **s_mssms_list_senders**
> ResponseSMSSMSListSendersResponse s_mssms_list_senders(body=body, content_language=content_language)

List verified sender numbers

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.SMSSubscriptionsSMSApi()
body = office_guy_api.Body245() # Body245 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # List verified sender numbers
    api_response = api_instance.s_mssms_list_senders(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSSubscriptionsSMSApi->s_mssms_list_senders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body245**](Body245.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseSMSSMSListSendersResponse**](ResponseSMSSMSListSendersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_mssms_send**
> ResponseSMSSMSSendResponse s_mssms_send(body=body, content_language=content_language)

Sends a single SMS message

When possible, SendMultiple should be used

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.SMSSubscriptionsSMSApi()
body = office_guy_api.Body237() # Body237 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Sends a single SMS message
    api_response = api_instance.s_mssms_send(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSSubscriptionsSMSApi->s_mssms_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body237**](Body237.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseSMSSMSSendResponse**](ResponseSMSSMSSendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_mssms_send_multiple**
> ResponseSMSSMSSendMultipleResponse s_mssms_send_multiple(body=body, content_language=content_language)

Sends multiple SMS messages

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.SMSSubscriptionsSMSApi()
body = office_guy_api.Body241() # Body241 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Sends multiple SMS messages
    api_response = api_instance.s_mssms_send_multiple(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SMSSubscriptionsSMSApi->s_mssms_send_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body241**](Body241.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseSMSSMSSendMultipleResponse**](ResponseSMSSMSSendMultipleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

