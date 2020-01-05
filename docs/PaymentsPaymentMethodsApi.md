# swagger_client.PaymentsPaymentMethodsApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_payment_methods_get_for_customer**](PaymentsPaymentMethodsApi.md#billing_payment_methods_get_for_customer) | **POST** /api/billing/paymentmethods/getforcustomer/ | Get payment details
[**billing_payment_methods_remove**](PaymentsPaymentMethodsApi.md#billing_payment_methods_remove) | **POST** /api/billing/paymentmethods/remove/ | Remove payment details from existing customer
[**billing_payment_methods_set_for_customer**](PaymentsPaymentMethodsApi.md#billing_payment_methods_set_for_customer) | **POST** /api/billing/paymentmethods/setforcustomer/ | Set payment details


# **billing_payment_methods_get_for_customer**
> ResponseBillingPaymentMethodsGetForCustomerResponse billing_payment_methods_get_for_customer(request=request, content_language=content_language)

Get payment details

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.PaymentsPaymentMethodsApi()
request = office_guy_api.BillingPaymentMethodsGetForCustomerRequest() # BillingPaymentMethodsGetForCustomerRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get payment details
    api_response = api_instance.billing_payment_methods_get_for_customer(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsPaymentMethodsApi->billing_payment_methods_get_for_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingPaymentMethodsGetForCustomerRequest**](BillingPaymentMethodsGetForCustomerRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingPaymentMethodsGetForCustomerResponse**](ResponseBillingPaymentMethodsGetForCustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_payment_methods_remove**
> ResponseBillingPaymentMethodsRemoveResponse billing_payment_methods_remove(request=request, content_language=content_language)

Remove payment details from existing customer

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.PaymentsPaymentMethodsApi()
request = office_guy_api.BillingPaymentMethodsRemoveRequest() # BillingPaymentMethodsRemoveRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Remove payment details from existing customer
    api_response = api_instance.billing_payment_methods_remove(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsPaymentMethodsApi->billing_payment_methods_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingPaymentMethodsRemoveRequest**](BillingPaymentMethodsRemoveRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingPaymentMethodsRemoveResponse**](ResponseBillingPaymentMethodsRemoveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_payment_methods_set_for_customer**
> ResponseBillingPaymentMethodsSetForCustomerResponse billing_payment_methods_set_for_customer(request=request, content_language=content_language)

Set payment details

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.PaymentsPaymentMethodsApi()
request = office_guy_api.BillingPaymentMethodsSetForCustomerRequest() # BillingPaymentMethodsSetForCustomerRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Set payment details
    api_response = api_instance.billing_payment_methods_set_for_customer(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsPaymentMethodsApi->billing_payment_methods_set_for_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingPaymentMethodsSetForCustomerRequest**](BillingPaymentMethodsSetForCustomerRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingPaymentMethodsSetForCustomerResponse**](ResponseBillingPaymentMethodsSetForCustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

