# office_guy_api.AccountingDocumentsApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounting_documents_add_expense**](AccountingDocumentsApi.md#accounting_documents_add_expense) | **POST** /api/accounting/documents/addexpense/ | Add expense
[**accounting_documents_cancel**](AccountingDocumentsApi.md#accounting_documents_cancel) | **POST** /api/accounting/documents/cancel/ | Cancel document (Also known as storno).
[**accounting_documents_create**](AccountingDocumentsApi.md#accounting_documents_create) | **POST** /api/accounting/documents/create/ | Create document
[**accounting_documents_get_details**](AccountingDocumentsApi.md#accounting_documents_get_details) | **POST** /api/accounting/documents/getdetails/ | Get document details
[**accounting_documents_get_pdf**](AccountingDocumentsApi.md#accounting_documents_get_pdf) | **POST** /api/accounting/documents/getpdf/ | Get document PDF
[**accounting_documents_move_to_books**](AccountingDocumentsApi.md#accounting_documents_move_to_books) | **POST** /api/accounting/documents/movetobooks/ | Move document to books (Finalize a draft document).
[**accounting_documents_send**](AccountingDocumentsApi.md#accounting_documents_send) | **POST** /api/accounting/documents/send/ | Send document by email

# **accounting_documents_add_expense**
> ResponseAccountingDocumentsAddExpenseResponse accounting_documents_add_expense(body=body, content_language=content_language)

Add expense

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingDocumentsApi()
body = office_guy_api.Body24() # Body24 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Add expense
    api_response = api_instance.accounting_documents_add_expense(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingDocumentsApi->accounting_documents_add_expense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body24**](Body24.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingDocumentsAddExpenseResponse**](ResponseAccountingDocumentsAddExpenseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_documents_cancel**
> ResponseAccountingDocumentsCancelResponse accounting_documents_cancel(body=body, content_language=content_language)

Cancel document (Also known as storno).

Please note cancelling documents is allowed within the same calendar day of the document creation date.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingDocumentsApi()
body = office_guy_api.Body28() # Body28 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Cancel document (Also known as storno).
    api_response = api_instance.accounting_documents_cancel(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingDocumentsApi->accounting_documents_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body28**](Body28.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingDocumentsCancelResponse**](ResponseAccountingDocumentsCancelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_documents_create**
> ResponseAccountingDocumentsCreateResponse accounting_documents_create(body=body, content_language=content_language)

Create document

Creates an invoice, receipt, donation receipt, price quotation or any other accounting document.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingDocumentsApi()
body = office_guy_api.Body20() # Body20 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Create document
    api_response = api_instance.accounting_documents_create(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingDocumentsApi->accounting_documents_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body20**](Body20.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingDocumentsCreateResponse**](ResponseAccountingDocumentsCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_documents_get_details**
> ResponseAccountingDocumentsGetDetailsResponse accounting_documents_get_details(body=body, content_language=content_language)

Get document details

Documents can be located either using DocumentID, or a combination of DocumentType and DocumentNumber.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingDocumentsApi()
body = office_guy_api.Body16() # Body16 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get document details
    api_response = api_instance.accounting_documents_get_details(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingDocumentsApi->accounting_documents_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body16**](Body16.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingDocumentsGetDetailsResponse**](ResponseAccountingDocumentsGetDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_documents_get_pdf**
> accounting_documents_get_pdf(body=body, content_language=content_language)

Get document PDF

Documents can be located either using DocumentID, or a combination of DocumentType and DocumentNumber.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingDocumentsApi()
body = office_guy_api.Body12() # Body12 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get document PDF
    api_instance.accounting_documents_get_pdf(body=body, content_language=content_language)
except ApiException as e:
    print("Exception when calling AccountingDocumentsApi->accounting_documents_get_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body12**](Body12.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_documents_move_to_books**
> ResponseAccountingDocumentsMoveToBooksResponse accounting_documents_move_to_books(body=body, content_language=content_language)

Move document to books (Finalize a draft document).

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingDocumentsApi()
body = office_guy_api.Body32() # Body32 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Move document to books (Finalize a draft document).
    api_response = api_instance.accounting_documents_move_to_books(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingDocumentsApi->accounting_documents_move_to_books: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body32**](Body32.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingDocumentsMoveToBooksResponse**](ResponseAccountingDocumentsMoveToBooksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_documents_send**
> CoreAPIEmptyResponse accounting_documents_send(body=body, content_language=content_language)

Send document by email

Documents can be located either using DocumentID (EntityID), or a combination of DocumentType and DocumentNumber.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingDocumentsApi()
body = office_guy_api.Body8() # Body8 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Send document by email
    api_response = api_instance.accounting_documents_send(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingDocumentsApi->accounting_documents_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body8**](Body8.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**CoreAPIEmptyResponse**](CoreAPIEmptyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

