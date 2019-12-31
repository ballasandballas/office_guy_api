# swagger_client.CreditCardTerminalVaultApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_guy_vault_tokenize**](CreditCardTerminalVaultApi.md#credit_guy_vault_tokenize) | **POST** /api/creditguy/vault/tokenize/ | Tokenize card (card number-&amp;gt;token)
[**credit_guy_vault_tokenize_single_use**](CreditCardTerminalVaultApi.md#credit_guy_vault_tokenize_single_use) | **POST** /api/creditguy/vault/tokenizesingleuse/ | Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.
[**credit_guy_vault_tokenize_single_use_json**](CreditCardTerminalVaultApi.md#credit_guy_vault_tokenize_single_use_json) | **POST** /api/creditguy/vault/tokenizesingleusejson/ | Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.


# **credit_guy_vault_tokenize**
> ResponseCreditGuyVaultTokenizeResponse credit_guy_vault_tokenize(request=request, content_language=content_language)

Tokenize card (card number-&gt;token)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditCardTerminalVaultApi()
request = swagger_client.CreditGuyVaultTokenizeRequest() # CreditGuyVaultTokenizeRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Tokenize card (card number-&gt;token)
    api_response = api_instance.credit_guy_vault_tokenize(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalVaultApi->credit_guy_vault_tokenize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreditGuyVaultTokenizeRequest**](CreditGuyVaultTokenizeRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyVaultTokenizeResponse**](ResponseCreditGuyVaultTokenizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_guy_vault_tokenize_single_use**
> ResponseCreditGuyVaultTokenizeSingleUseResponse credit_guy_vault_tokenize_single_use(card_number, expiration_month, expiration_year, cvv=cvv, citizen_id=citizen_id, credentials_company_id=credentials_company_id, credentials_api_public_key=credentials_api_public_key, response_language=response_language, content_language=content_language)

Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.

Used primarily by the Payments JavaScript API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditCardTerminalVaultApi()
card_number = 'card_number_example' # str | Full card number to tokenize
expiration_month = 56 # int | Card expiration month (1-12).
expiration_year = 56 # int | Card expiration year (4 digits).
cvv = 'cvv_example' # str | Card CVV/CVV2. (optional)
citizen_id = 'citizen_id_example' # str | Israel Citizen ID / Passport Number. (optional)
credentials_company_id = 789 # int | Company identifier (optional)
credentials_api_public_key = 'credentials_api_public_key_example' # str | API public key (optional)
response_language = 'response_language_example' # str | This property is obsolete. Please refer to the \"Content-Language\" header instead. (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.
    api_response = api_instance.credit_guy_vault_tokenize_single_use(card_number, expiration_month, expiration_year, cvv=cvv, citizen_id=citizen_id, credentials_company_id=credentials_company_id, credentials_api_public_key=credentials_api_public_key, response_language=response_language, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalVaultApi->credit_guy_vault_tokenize_single_use: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_number** | **str**| Full card number to tokenize | 
 **expiration_month** | **int**| Card expiration month (1-12). | 
 **expiration_year** | **int**| Card expiration year (4 digits). | 
 **cvv** | **str**| Card CVV/CVV2. | [optional] 
 **citizen_id** | **str**| Israel Citizen ID / Passport Number. | [optional] 
 **credentials_company_id** | **int**| Company identifier | [optional] 
 **credentials_api_public_key** | **str**| API public key | [optional] 
 **response_language** | **str**| This property is obsolete. Please refer to the \&quot;Content-Language\&quot; header instead. | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyVaultTokenizeSingleUseResponse**](ResponseCreditGuyVaultTokenizeSingleUseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_guy_vault_tokenize_single_use_json**
> ResponseCreditGuyVaultTokenizeSingleUseResponse credit_guy_vault_tokenize_single_use_json(request=request, content_language=content_language)

Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.

Used primarily by the Payments JavaScript API.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditCardTerminalVaultApi()
request = swagger_client.CreditGuyVaultTokenizeSingleUseRequest() # CreditGuyVaultTokenizeSingleUseRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.
    api_response = api_instance.credit_guy_vault_tokenize_single_use_json(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalVaultApi->credit_guy_vault_tokenize_single_use_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreditGuyVaultTokenizeSingleUseRequest**](CreditGuyVaultTokenizeSingleUseRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyVaultTokenizeSingleUseResponse**](ResponseCreditGuyVaultTokenizeSingleUseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

