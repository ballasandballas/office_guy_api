# office_guy_api.StockManagementStockApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stock_stock_list**](StockManagementStockApi.md#stock_stock_list) | **POST** /api/stock/stock/list/ | List stock levels

# **stock_stock_list**
> ResponseStockStockListResponse stock_stock_list(body=body, content_language=content_language)

List stock levels

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.StockManagementStockApi()
body = office_guy_api.Body249() # Body249 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # List stock levels
    api_response = api_instance.stock_stock_list(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StockManagementStockApi->stock_stock_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body249**](Body249.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseStockStockListResponse**](ResponseStockStockListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

