# swagger_client.AccountingGeneralApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounting_general_get_exchange_rate**](AccountingGeneralApi.md#accounting_general_get_exchange_rate) | **POST** /api/accounting/general/getexchangerate/ | Get foreign currency exchange rate
[**accounting_general_get_vat_rate**](AccountingGeneralApi.md#accounting_general_get_vat_rate) | **POST** /api/accounting/general/getvatrate/ | Get VAT rate by date
[**accounting_general_set_next_document_number**](AccountingGeneralApi.md#accounting_general_set_next_document_number) | **POST** /api/accounting/general/setnextdocumentnumber/ | Sets the next document number for a document type.
[**accounting_general_update_settings**](AccountingGeneralApi.md#accounting_general_update_settings) | **POST** /api/accounting/general/updatesettings/ | Update accounting application settings
[**accounting_general_verify_bank_account**](AccountingGeneralApi.md#accounting_general_verify_bank_account) | **POST** /api/accounting/general/verifybankaccount/ | Verify bank account details


# **accounting_general_get_exchange_rate**
> ResponseAccountingGeneralGetExchangeRateResponse accounting_general_get_exchange_rate(request=request, content_language=content_language)

Get foreign currency exchange rate

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingGeneralApi()
request = office_guy_api.AccountingGeneralGetExchangeRateRequest() # AccountingGeneralGetExchangeRateRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get foreign currency exchange rate
    api_response = api_instance.accounting_general_get_exchange_rate(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingGeneralApi->accounting_general_get_exchange_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AccountingGeneralGetExchangeRateRequest**](AccountingGeneralGetExchangeRateRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingGeneralGetExchangeRateResponse**](ResponseAccountingGeneralGetExchangeRateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_general_get_vat_rate**
> ResponseAccountingGeneralGetVATRateResponse accounting_general_get_vat_rate(request=request, content_language=content_language)

Get VAT rate by date

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingGeneralApi()
request = office_guy_api.AccountingGeneralGetVATRateRequest() # AccountingGeneralGetVATRateRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get VAT rate by date
    api_response = api_instance.accounting_general_get_vat_rate(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingGeneralApi->accounting_general_get_vat_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AccountingGeneralGetVATRateRequest**](AccountingGeneralGetVATRateRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingGeneralGetVATRateResponse**](ResponseAccountingGeneralGetVATRateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_general_set_next_document_number**
> ResponseAccountingGeneralSetNextDocumentNumberResponse accounting_general_set_next_document_number(request=request, content_language=content_language)

Sets the next document number for a document type.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingGeneralApi()
request = office_guy_api.AccountingGeneralSetNextDocumentNumberRequest() # AccountingGeneralSetNextDocumentNumberRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Sets the next document number for a document type.
    api_response = api_instance.accounting_general_set_next_document_number(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingGeneralApi->accounting_general_set_next_document_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AccountingGeneralSetNextDocumentNumberRequest**](AccountingGeneralSetNextDocumentNumberRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingGeneralSetNextDocumentNumberResponse**](ResponseAccountingGeneralSetNextDocumentNumberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_general_update_settings**
> ResponseAccountingGeneralUpdateSettingsResponse accounting_general_update_settings(request=request, content_language=content_language)

Update accounting application settings

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingGeneralApi()
request = office_guy_api.AccountingGeneralUpdateSettingsRequest() # AccountingGeneralUpdateSettingsRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Update accounting application settings
    api_response = api_instance.accounting_general_update_settings(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingGeneralApi->accounting_general_update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AccountingGeneralUpdateSettingsRequest**](AccountingGeneralUpdateSettingsRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingGeneralUpdateSettingsResponse**](ResponseAccountingGeneralUpdateSettingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_general_verify_bank_account**
> ResponseAccountingGeneralVerifyBankAccountResponse accounting_general_verify_bank_account(request=request, content_language=content_language)

Verify bank account details

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.AccountingGeneralApi()
request = office_guy_api.AccountingGeneralVerifyBankAccountRequest() # AccountingGeneralVerifyBankAccountRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Verify bank account details
    api_response = api_instance.accounting_general_verify_bank_account(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingGeneralApi->accounting_general_verify_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**AccountingGeneralVerifyBankAccountRequest**](AccountingGeneralVerifyBankAccountRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseAccountingGeneralVerifyBankAccountResponse**](ResponseAccountingGeneralVerifyBankAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

