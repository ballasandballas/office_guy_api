# swagger_client.PaymentsPaymentsApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_payments_begin_redirect**](PaymentsPaymentsApi.md#billing_payments_begin_redirect) | **POST** /api/billing/payments/beginredirect/ | Begin redirect for transaction
[**billing_payments_charge**](PaymentsPaymentsApi.md#billing_payments_charge) | **POST** /api/billing/payments/charge/ | Charge customer
[**billing_payments_get**](PaymentsPaymentsApi.md#billing_payments_get) | **POST** /api/billing/payments/get/ | Get payment details
[**billing_payments_list**](PaymentsPaymentsApi.md#billing_payments_list) | **POST** /api/billing/payments/list/ | List payments


# **billing_payments_begin_redirect**
> ResponseBillingPaymentsBeginRedirectResponse billing_payments_begin_redirect(request=request, content_language=content_language)

Begin redirect for transaction

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.PaymentsPaymentsApi()
request = office_guy_api.BillingPaymentsBeginRedirectRequest() # BillingPaymentsBeginRedirectRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Begin redirect for transaction
    api_response = api_instance.billing_payments_begin_redirect(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsPaymentsApi->billing_payments_begin_redirect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingPaymentsBeginRedirectRequest**](BillingPaymentsBeginRedirectRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingPaymentsBeginRedirectResponse**](ResponseBillingPaymentsBeginRedirectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_payments_charge**
> ResponseBillingPaymentsChargeResponse billing_payments_charge(request=request, content_language=content_language)

Charge customer

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.PaymentsPaymentsApi()
request = office_guy_api.BillingPaymentsChargeRequest() # BillingPaymentsChargeRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Charge customer
    api_response = api_instance.billing_payments_charge(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsPaymentsApi->billing_payments_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingPaymentsChargeRequest**](BillingPaymentsChargeRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingPaymentsChargeResponse**](ResponseBillingPaymentsChargeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_payments_get**
> ResponseBillingPaymentsGetResponse billing_payments_get(request=request, content_language=content_language)

Get payment details

Remarks goes here

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.PaymentsPaymentsApi()
request = office_guy_api.BillingPaymentsGetRequest() # BillingPaymentsGetRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get payment details
    api_response = api_instance.billing_payments_get(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsPaymentsApi->billing_payments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingPaymentsGetRequest**](BillingPaymentsGetRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingPaymentsGetResponse**](ResponseBillingPaymentsGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_payments_list**
> ResponseBillingPaymentsListResponse billing_payments_list(request=request, content_language=content_language)

List payments

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.PaymentsPaymentsApi()
request = office_guy_api.BillingPaymentsListRequest() # BillingPaymentsListRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # List payments
    api_response = api_instance.billing_payments_list(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsPaymentsApi->billing_payments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingPaymentsListRequest**](BillingPaymentsListRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingPaymentsListResponse**](ResponseBillingPaymentsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

