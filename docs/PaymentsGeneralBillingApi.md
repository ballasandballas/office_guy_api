# office_guy_api.PaymentsGeneralBillingApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_general_billing_open_u_pay_terminal**](PaymentsGeneralBillingApi.md#billing_general_billing_open_u_pay_terminal) | **POST** /api/billing/generalbilling/openupayterminal/ | Open an instant credit card terminal using UPay.
[**billing_general_billing_set_u_pay_credentials**](PaymentsGeneralBillingApi.md#billing_general_billing_set_u_pay_credentials) | **POST** /api/billing/generalbilling/setupaycredentials/ | Setup existing UPay account credentials

# **billing_general_billing_open_u_pay_terminal**
> ResponseBillingGeneralOpenUPayTerminalResponse billing_general_billing_open_u_pay_terminal(body=body, content_language=content_language)

Open an instant credit card terminal using UPay.

Please note all parameters set on the request, are automatically requested from UPay, yet should be manually approved by contacting UPay.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.PaymentsGeneralBillingApi()
body = office_guy_api.Body173() # Body173 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Open an instant credit card terminal using UPay.
    api_response = api_instance.billing_general_billing_open_u_pay_terminal(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsGeneralBillingApi->billing_general_billing_open_u_pay_terminal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body173**](Body173.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingGeneralOpenUPayTerminalResponse**](ResponseBillingGeneralOpenUPayTerminalResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_general_billing_set_u_pay_credentials**
> ResponseBillingGeneralSetUPayCredentialsResponse billing_general_billing_set_u_pay_credentials(body=body, content_language=content_language)

Setup existing UPay account credentials

Please note when using existing UPay credentials, customer terms will remain as they were before using OfficeGuy

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.PaymentsGeneralBillingApi()
body = office_guy_api.Body177() # Body177 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Setup existing UPay account credentials
    api_response = api_instance.billing_general_billing_set_u_pay_credentials(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsGeneralBillingApi->billing_general_billing_set_u_pay_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body177**](Body177.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingGeneralSetUPayCredentialsResponse**](ResponseBillingGeneralSetUPayCredentialsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

