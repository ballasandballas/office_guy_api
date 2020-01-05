# swagger_client.AccountingCustomersApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounting_customers_create**](AccountingCustomersApi.md#accounting_customers_create) | **POST** /api/accounting/customers/create/ | Create customer


# **accounting_customers_create**
> ResponseAccountingCustomersCreateResponse accounting_customers_create(request=request, content_language=content_language)

Create customer

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingCustomersApi()
request = office_guy_api.AccountingCustomersCreateRequest() # AccountingCustomersCreateRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Create customer
    api_response = api_instance.accounting_customers_create(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingCustomersApi->accounting_customers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AccountingCustomersCreateRequest**](AccountingCustomersCreateRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingCustomersCreateResponse**](ResponseAccountingCustomersCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

