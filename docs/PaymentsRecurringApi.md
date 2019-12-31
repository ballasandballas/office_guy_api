# swagger_client.PaymentsRecurringApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_recurring_cancel**](PaymentsRecurringApi.md#billing_recurring_cancel) | **POST** /api/billing/recurring/cancel/ | Cancel customer item
[**billing_recurring_charge**](PaymentsRecurringApi.md#billing_recurring_charge) | **POST** /api/billing/recurring/charge/ | Charge customer and create recurring payment
[**billing_recurring_list_for_customer**](PaymentsRecurringApi.md#billing_recurring_list_for_customer) | **POST** /api/billing/recurring/listforcustomer/ | List customer recurring items
[**billing_recurring_update**](PaymentsRecurringApi.md#billing_recurring_update) | **POST** /api/billing/recurring/update/ | Update customer recurring item
[**billing_recurring_update_settings**](PaymentsRecurringApi.md#billing_recurring_update_settings) | **POST** /api/billing/recurring/updatesettings/ | Update recurring billing application settings


# **billing_recurring_cancel**
> ResponseBillingRecurringCancelResponse billing_recurring_cancel(request=request, content_language=content_language)

Cancel customer item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsRecurringApi()
request = swagger_client.BillingRecurringCancelRequest() # BillingRecurringCancelRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Cancel customer item
    api_response = api_instance.billing_recurring_cancel(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsRecurringApi->billing_recurring_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingRecurringCancelRequest**](BillingRecurringCancelRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingRecurringCancelResponse**](ResponseBillingRecurringCancelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_recurring_charge**
> ResponseBillingRecurringChargeResponse billing_recurring_charge(request=request, content_language=content_language)

Charge customer and create recurring payment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsRecurringApi()
request = swagger_client.BillingRecurringChargeRequest() # BillingRecurringChargeRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Charge customer and create recurring payment
    api_response = api_instance.billing_recurring_charge(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsRecurringApi->billing_recurring_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingRecurringChargeRequest**](BillingRecurringChargeRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingRecurringChargeResponse**](ResponseBillingRecurringChargeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_recurring_list_for_customer**
> ResponseBillingRecurringListForCustomerResponse billing_recurring_list_for_customer(request=request, content_language=content_language)

List customer recurring items

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsRecurringApi()
request = swagger_client.BillingRecurringListForCustomerRequest() # BillingRecurringListForCustomerRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # List customer recurring items
    api_response = api_instance.billing_recurring_list_for_customer(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsRecurringApi->billing_recurring_list_for_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingRecurringListForCustomerRequest**](BillingRecurringListForCustomerRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingRecurringListForCustomerResponse**](ResponseBillingRecurringListForCustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_recurring_update**
> ResponseBillingRecurringUpdateResponse billing_recurring_update(request=request, content_language=content_language)

Update customer recurring item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsRecurringApi()
request = swagger_client.BillingRecurringUpdateRequest() # BillingRecurringUpdateRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Update customer recurring item
    api_response = api_instance.billing_recurring_update(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsRecurringApi->billing_recurring_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingRecurringUpdateRequest**](BillingRecurringUpdateRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingRecurringUpdateResponse**](ResponseBillingRecurringUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_recurring_update_settings**
> ResponseBillingRecurringUpdateSettingsResponse billing_recurring_update_settings(request=request, content_language=content_language)

Update recurring billing application settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PaymentsRecurringApi()
request = swagger_client.BillingRecurringUpdateSettingsRequest() # BillingRecurringUpdateSettingsRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Update recurring billing application settings
    api_response = api_instance.billing_recurring_update_settings(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsRecurringApi->billing_recurring_update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**BillingRecurringUpdateSettingsRequest**](BillingRecurringUpdateSettingsRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseBillingRecurringUpdateSettingsResponse**](ResponseBillingRecurringUpdateSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

