# swagger_client.CreditCardTerminalGatewayApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_guy_gateway_begin_redirect**](CreditCardTerminalGatewayApi.md#credit_guy_gateway_begin_redirect) | **POST** /api/creditguy/gateway/beginredirect/ | Begin redirect for transaction
[**credit_guy_gateway_get_reference_numbers**](CreditCardTerminalGatewayApi.md#credit_guy_gateway_get_reference_numbers) | **POST** /api/creditguy/gateway/getreferencenumbers/ | Get reference numbers for existing transactions
[**credit_guy_gateway_get_transaction**](CreditCardTerminalGatewayApi.md#credit_guy_gateway_get_transaction) | **POST** /api/creditguy/gateway/gettransaction/ | Get existing transaction details
[**credit_guy_gateway_transaction**](CreditCardTerminalGatewayApi.md#credit_guy_gateway_transaction) | **POST** /api/creditguy/gateway/transaction/ | Credit card transaction


# **credit_guy_gateway_begin_redirect**
> ResponseCreditGuyGatewayBeginRedirectResponse credit_guy_gateway_begin_redirect(request=request, content_language=content_language)

Begin redirect for transaction

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditCardTerminalGatewayApi()
request = swagger_client.CreditGuyGatewayBeginRedirectRequest() # CreditGuyGatewayBeginRedirectRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Begin redirect for transaction
    api_response = api_instance.credit_guy_gateway_begin_redirect(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalGatewayApi->credit_guy_gateway_begin_redirect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreditGuyGatewayBeginRedirectRequest**](CreditGuyGatewayBeginRedirectRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyGatewayBeginRedirectResponse**](ResponseCreditGuyGatewayBeginRedirectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_guy_gateway_get_reference_numbers**
> ResponseCreditGuyGatewayGetReferenceNumbersResponse credit_guy_gateway_get_reference_numbers(request=request, content_language=content_language)

Get reference numbers for existing transactions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditCardTerminalGatewayApi()
request = swagger_client.CreditGuyGatewayGetReferenceNumbersRequest() # CreditGuyGatewayGetReferenceNumbersRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get reference numbers for existing transactions
    api_response = api_instance.credit_guy_gateway_get_reference_numbers(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalGatewayApi->credit_guy_gateway_get_reference_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreditGuyGatewayGetReferenceNumbersRequest**](CreditGuyGatewayGetReferenceNumbersRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyGatewayGetReferenceNumbersResponse**](ResponseCreditGuyGatewayGetReferenceNumbersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_guy_gateway_get_transaction**
> ResponseCreditGuyGatewayGetTransactionResponse credit_guy_gateway_get_transaction(request=request, content_language=content_language)

Get existing transaction details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditCardTerminalGatewayApi()
request = swagger_client.CreditGuyGatewayGetTransactionRequest() # CreditGuyGatewayGetTransactionRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get existing transaction details
    api_response = api_instance.credit_guy_gateway_get_transaction(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalGatewayApi->credit_guy_gateway_get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreditGuyGatewayGetTransactionRequest**](CreditGuyGatewayGetTransactionRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyGatewayGetTransactionResponse**](ResponseCreditGuyGatewayGetTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_guy_gateway_transaction**
> ResponseCreditGuyGatewayTransactionResponse credit_guy_gateway_transaction(request=request, content_language=content_language)

Credit card transaction

This method should be used in rare occasions.  For common use scenarios, refer to \"Payments -&gt; Charge customer\" method.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreditCardTerminalGatewayApi()
request = swagger_client.CreditGuyGatewayTransactionRequest() # CreditGuyGatewayTransactionRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Credit card transaction
    api_response = api_instance.credit_guy_gateway_transaction(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditCardTerminalGatewayApi->credit_guy_gateway_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreditGuyGatewayTransactionRequest**](CreditGuyGatewayTransactionRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseCreditGuyGatewayTransactionResponse**](ResponseCreditGuyGatewayTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

