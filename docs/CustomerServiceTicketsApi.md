# office_guy_api.CustomerServiceTicketsApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_service_tickets_create**](CustomerServiceTicketsApi.md#customer_service_tickets_create) | **POST** /api/customerservice/tickets/create/ | 

# **customer_service_tickets_create**
> ResponseCustomerServiceTicketsCreateResponse customer_service_tickets_create(body=body, content_language=content_language)



### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.CustomerServiceTicketsApi()
body = office_guy_api.Body145() # Body145 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    api_response = api_instance.customer_service_tickets_create(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerServiceTicketsApi->customer_service_tickets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body145**](Body145.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCustomerServiceTicketsCreateResponse**](ResponseCustomerServiceTicketsCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

