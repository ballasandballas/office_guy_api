# office_guy_api.CreditCardTerminalVaultApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_guy_vault_tokenize**](CreditCardTerminalVaultApi.md#credit_guy_vault_tokenize) | **POST** /api/creditguy/vault/tokenize/ | Tokenize card (card number-&gt;token)
[**credit_guy_vault_tokenize_single_use**](CreditCardTerminalVaultApi.md#credit_guy_vault_tokenize_single_use) | **POST** /api/creditguy/vault/tokenizesingleuse/ | Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.
[**credit_guy_vault_tokenize_single_use_json**](CreditCardTerminalVaultApi.md#credit_guy_vault_tokenize_single_use_json) | **POST** /api/creditguy/vault/tokenizesingleusejson/ | Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.

# **credit_guy_vault_tokenize**
> ResponseCreditGuyVaultTokenizeResponse credit_guy_vault_tokenize(body=body, content_language=content_language)

Tokenize card (card number->token)

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.CreditCardTerminalVaultApi()
body = office_guy_api.Body88() # Body88 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Tokenize card (card number->token)
    api_response = api_instance.credit_guy_vault_tokenize(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalVaultApi->credit_guy_vault_tokenize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body88**](Body88.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyVaultTokenizeResponse**](ResponseCreditGuyVaultTokenizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_guy_vault_tokenize_single_use**
> ResponseCreditGuyVaultTokenizeSingleUseResponse credit_guy_vault_tokenize_single_use(card_number=card_number, expiration_month=expiration_month, expiration_year=expiration_year, cvv=cvv, citizen_id=citizen_id, credentials_company_id=credentials_company_id, credentials_api_public_key=credentials_api_public_key, response_language=response_language, content_language=content_language)

Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.

Used primarily by the Payments JavaScript API.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.CreditCardTerminalVaultApi()
card_number = 'card_number_example' # str |  (optional)
expiration_month = 56 # int |  (optional)
expiration_year = 56 # int |  (optional)
cvv = 'cvv_example' # str |  (optional)
citizen_id = 'citizen_id_example' # str |  (optional)
credentials_company_id = 789 # int |  (optional)
credentials_api_public_key = 'credentials_api_public_key_example' # str |  (optional)
response_language = 'response_language_example' # str |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.
    api_response = api_instance.credit_guy_vault_tokenize_single_use(card_number=card_number, expiration_month=expiration_month, expiration_year=expiration_year, cvv=cvv, citizen_id=citizen_id, credentials_company_id=credentials_company_id, credentials_api_public_key=credentials_api_public_key, response_language=response_language, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalVaultApi->credit_guy_vault_tokenize_single_use: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_number** | **str**|  | [optional] 
 **expiration_month** | **int**|  | [optional] 
 **expiration_year** | **int**|  | [optional] 
 **cvv** | **str**|  | [optional] 
 **citizen_id** | **str**|  | [optional] 
 **credentials_company_id** | **int**|  | [optional] 
 **credentials_api_public_key** | **str**|  | [optional] 
 **response_language** | **str**|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyVaultTokenizeSingleUseResponse**](ResponseCreditGuyVaultTokenizeSingleUseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_guy_vault_tokenize_single_use_json**
> ResponseCreditGuyVaultTokenizeSingleUseResponse credit_guy_vault_tokenize_single_use_json(body=body, content_language=content_language)

Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.

Used primarily by the Payments JavaScript API.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.CreditCardTerminalVaultApi()
body = office_guy_api.Body93() # Body93 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.
    api_response = api_instance.credit_guy_vault_tokenize_single_use_json(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalVaultApi->credit_guy_vault_tokenize_single_use_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body93**](Body93.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyVaultTokenizeSingleUseResponse**](ResponseCreditGuyVaultTokenizeSingleUseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

