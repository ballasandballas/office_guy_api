# swagger_client.AccountingIncomeItemsApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounting_income_items_create**](AccountingIncomeItemsApi.md#accounting_income_items_create) | **POST** /api/accounting/incomeitems/create/ | Create income item
[**accounting_income_items_list_stock**](AccountingIncomeItemsApi.md#accounting_income_items_list_stock) | **POST** /api/accounting/incomeitems/liststock/ | List stock


# **accounting_income_items_create**
> ResponseAccountingIncomeItemsCreateResponse accounting_income_items_create(request=request, content_language=content_language)

Create income item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingIncomeItemsApi()
request = swagger_client.AccountingIncomeItemsCreateRequest() # AccountingIncomeItemsCreateRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Create income item
    api_response = api_instance.accounting_income_items_create(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingIncomeItemsApi->accounting_income_items_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AccountingIncomeItemsCreateRequest**](AccountingIncomeItemsCreateRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingIncomeItemsCreateResponse**](ResponseAccountingIncomeItemsCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_income_items_list_stock**
> ResponseAccountingIncomeItemsListStockResponse accounting_income_items_list_stock(request=request, content_language=content_language)

List stock

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingIncomeItemsApi()
request = swagger_client.AccountingIncomeItemsListStockRequest() # AccountingIncomeItemsListStockRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # List stock
    api_response = api_instance.accounting_income_items_list_stock(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingIncomeItemsApi->accounting_income_items_list_stock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AccountingIncomeItemsListStockRequest**](AccountingIncomeItemsListStockRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingIncomeItemsListStockResponse**](ResponseAccountingIncomeItemsListStockResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

