# office_guy_api.AccountingIncomeItemsApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounting_income_items_create**](AccountingIncomeItemsApi.md#accounting_income_items_create) | **POST** /api/accounting/incomeitems/create/ | Create income item

# **accounting_income_items_create**
> ResponseAccountingIncomeItemsCreateResponse accounting_income_items_create(body=body, content_language=content_language)

Create income item

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingIncomeItemsApi()
body = office_guy_api.Body56() # Body56 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Create income item
    api_response = api_instance.accounting_income_items_create(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingIncomeItemsApi->accounting_income_items_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body56**](Body56.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingIncomeItemsCreateResponse**](ResponseAccountingIncomeItemsCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

