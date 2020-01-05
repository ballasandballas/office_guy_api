# swagger_client.HashExportExportApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounting_hash_export_export_send**](HashExportExportApi.md#accounting_hash_export_export_send) | **POST** /api/accountinghashexport/export/send/ | Sends hash export by mail


# **accounting_hash_export_export_send**
> ResponseAccountingHashExportExportSendResponse accounting_hash_export_export_send(request=request, content_language=content_language)

Sends hash export by mail

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.HashExportExportApi()
request = office_guy_api.AccountingHashExportExportSendRequest() # AccountingHashExportExportSendRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Sends hash export by mail
    api_response = api_instance.accounting_hash_export_export_send(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HashExportExportApi->accounting_hash_export_export_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AccountingHashExportExportSendRequest**](AccountingHashExportExportSendRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingHashExportExportSendResponse**](ResponseAccountingHashExportExportSendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

