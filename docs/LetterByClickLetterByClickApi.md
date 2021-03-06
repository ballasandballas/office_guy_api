# swagger_client.LetterByClickLetterByClickApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**letter_by_click_letter_by_click_get_tracking_code**](LetterByClickLetterByClickApi.md#letter_by_click_letter_by_click_get_tracking_code) | **POST** /api/letterbyclick/letterbyclick/gettrackingcode/ | Get tracking code from Beeri&#39;s Letter by Click service.  Please note tracking codes are available ~30 minutes after sending the document using the API.
[**letter_by_click_letter_by_click_send_document**](LetterByClickLetterByClickApi.md#letter_by_click_letter_by_click_send_document) | **POST** /api/letterbyclick/letterbyclick/senddocument/ | Send mail through Beeri&#39;s Letter by Click service.


# **letter_by_click_letter_by_click_get_tracking_code**
> ResponseLetterByClickLetterByClickGetTrackingCodeResponse letter_by_click_letter_by_click_get_tracking_code(request=request, content_language=content_language)

Get tracking code from Beeri's Letter by Click service.  Please note tracking codes are available ~30 minutes after sending the document using the API.

Contact us before using this API, as it's currently experimental.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.LetterByClickLetterByClickApi()
request = office_guy_api.LetterByClickLetterByClickGetTrackingCodeRequest() # LetterByClickLetterByClickGetTrackingCodeRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get tracking code from Beeri's Letter by Click service.  Please note tracking codes are available ~30 minutes after sending the document using the API.
    api_response = api_instance.letter_by_click_letter_by_click_get_tracking_code(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LetterByClickLetterByClickApi->letter_by_click_letter_by_click_get_tracking_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**LetterByClickLetterByClickGetTrackingCodeRequest**](LetterByClickLetterByClickGetTrackingCodeRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseLetterByClickLetterByClickGetTrackingCodeResponse**](ResponseLetterByClickLetterByClickGetTrackingCodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **letter_by_click_letter_by_click_send_document**
> ResponseLetterByClickLetterByClickSendDocumentResponse letter_by_click_letter_by_click_send_document(request=request, content_language=content_language)

Send mail through Beeri's Letter by Click service.

Contact us before using this API, as it's currently experimental.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.LetterByClickLetterByClickApi()
request = office_guy_api.LetterByClickLetterByClickSendDocumentRequest() # LetterByClickLetterByClickSendDocumentRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Send mail through Beeri's Letter by Click service.
    api_response = api_instance.letter_by_click_letter_by_click_send_document(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LetterByClickLetterByClickApi->letter_by_click_letter_by_click_send_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**LetterByClickLetterByClickSendDocumentRequest**](LetterByClickLetterByClickSendDocumentRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseLetterByClickLetterByClickSendDocumentResponse**](ResponseLetterByClickLetterByClickSendDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

