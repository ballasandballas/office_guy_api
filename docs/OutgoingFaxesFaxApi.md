# office_guy_api.OutgoingFaxesFaxApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fax_fax_send**](OutgoingFaxesFaxApi.md#fax_fax_send) | **POST** /api/fax/fax/send/ | 

# **fax_fax_send**
> ResponseFaxFaxSendResponse fax_fax_send(body=body, content_language=content_language)



### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.OutgoingFaxesFaxApi()
body = office_guy_api.Body169() # Body169 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    api_response = api_instance.fax_fax_send(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutgoingFaxesFaxApi->fax_fax_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body169**](Body169.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseFaxFaxSendResponse**](ResponseFaxFaxSendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

