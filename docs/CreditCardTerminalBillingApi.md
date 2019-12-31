# swagger_client.CreditCardTerminalBillingApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_guy_billing_get_status**](CreditCardTerminalBillingApi.md#credit_guy_billing_get_status) | **POST** /api/creditguy/billing/getstatus/ | Get billing process status
[**credit_guy_billing_load**](CreditCardTerminalBillingApi.md#credit_guy_billing_load) | **POST** /api/creditguy/billing/load/ | Load billing transactions
[**credit_guy_billing_process**](CreditCardTerminalBillingApi.md#credit_guy_billing_process) | **POST** /api/creditguy/billing/process/ | Process loaded billing transactions.


# **credit_guy_billing_get_status**
> ResponseCreditGuyBillingGetStatusResponse credit_guy_billing_get_status(request=request, content_language=content_language)

Get billing process status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditCardTerminalBillingApi()
request = swagger_client.CreditGuyBillingGetStatusRequest() # CreditGuyBillingGetStatusRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get billing process status
    api_response = api_instance.credit_guy_billing_get_status(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalBillingApi->credit_guy_billing_get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreditGuyBillingGetStatusRequest**](CreditGuyBillingGetStatusRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyBillingGetStatusResponse**](ResponseCreditGuyBillingGetStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_guy_billing_load**
> ResponseCreditGuyBillingLoadResponse credit_guy_billing_load(request=request, content_language=content_language)

Load billing transactions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditCardTerminalBillingApi()
request = swagger_client.CreditGuyBillingLoadRequest() # CreditGuyBillingLoadRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Load billing transactions
    api_response = api_instance.credit_guy_billing_load(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalBillingApi->credit_guy_billing_load: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreditGuyBillingLoadRequest**](CreditGuyBillingLoadRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyBillingLoadResponse**](ResponseCreditGuyBillingLoadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_guy_billing_process**
> ResponseCreditGuyBillingProcessResponse credit_guy_billing_process(request=request, content_language=content_language)

Process loaded billing transactions.

Please note, once process has started, it can't be stopped, and no additional transactions can be loaded.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditCardTerminalBillingApi()
request = swagger_client.CreditGuyBillingProcessRequest() # CreditGuyBillingProcessRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Process loaded billing transactions.
    api_response = api_instance.credit_guy_billing_process(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalBillingApi->credit_guy_billing_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreditGuyBillingProcessRequest**](CreditGuyBillingProcessRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyBillingProcessResponse**](ResponseCreditGuyBillingProcessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

