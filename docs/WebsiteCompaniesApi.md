# swagger_client.WebsiteCompaniesApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**website_companies_create**](WebsiteCompaniesApi.md#website_companies_create) | **POST** /api/website/companies/create/ | Create new organization
[**website_companies_get_details**](WebsiteCompaniesApi.md#website_companies_get_details) | **POST** /api/website/companies/getdetails/ | Get organization details
[**website_companies_install_additions**](WebsiteCompaniesApi.md#website_companies_install_additions) | **POST** /api/website/companies/installadditions/ | Install additions
[**website_companies_install_applications**](WebsiteCompaniesApi.md#website_companies_install_applications) | **POST** /api/website/companies/installapplications/ | Install applications
[**website_companies_remove_additions**](WebsiteCompaniesApi.md#website_companies_remove_additions) | **POST** /api/website/companies/removeadditions/ | Removes additions
[**website_companies_update**](WebsiteCompaniesApi.md#website_companies_update) | **POST** /api/website/companies/update/ | Update organization details


# **website_companies_create**
> ResponseWebsiteCompaniesCreateResponse website_companies_create(request=request, content_language=content_language)

Create new organization

Created organization payment method, will be set to the calling organization payment method.  This method requires an active payment method.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsiteCompaniesApi()
request = swagger_client.WebsiteCompaniesCreateRequest() # WebsiteCompaniesCreateRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Create new organization
    api_response = api_instance.website_companies_create(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**WebsiteCompaniesCreateRequest**](WebsiteCompaniesCreateRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesCreateResponse**](ResponseWebsiteCompaniesCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_get_details**
> ResponseWebsiteCompaniesGetDetailsResponse website_companies_get_details(request=request, content_language=content_language)

Get organization details

This method can be used to make sure the correct organization ID is used, when multiple companies are in use.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsiteCompaniesApi()
request = swagger_client.WebsiteCompaniesGetDetailsRequest() # WebsiteCompaniesGetDetailsRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Get organization details
    api_response = api_instance.website_companies_get_details(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**WebsiteCompaniesGetDetailsRequest**](WebsiteCompaniesGetDetailsRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesGetDetailsResponse**](ResponseWebsiteCompaniesGetDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_install_additions**
> ResponseWebsiteCompaniesInstallAdditionsResponse website_companies_install_additions(request=request, content_language=content_language)

Install additions

Please note this method requires an active payment method.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsiteCompaniesApi()
request = swagger_client.WebsiteCompaniesInstallAdditionsRequest() # WebsiteCompaniesInstallAdditionsRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Install additions
    api_response = api_instance.website_companies_install_additions(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_install_additions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**WebsiteCompaniesInstallAdditionsRequest**](WebsiteCompaniesInstallAdditionsRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesInstallAdditionsResponse**](ResponseWebsiteCompaniesInstallAdditionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_install_applications**
> ResponseWebsiteCompaniesInstallApplicationsResponse website_companies_install_applications(request=request, content_language=content_language)

Install applications

Please note this method requires an active payment method.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsiteCompaniesApi()
request = swagger_client.WebsiteCompaniesInstallApplicationsRequest() # WebsiteCompaniesInstallApplicationsRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Install applications
    api_response = api_instance.website_companies_install_applications(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_install_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**WebsiteCompaniesInstallApplicationsRequest**](WebsiteCompaniesInstallApplicationsRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesInstallApplicationsResponse**](ResponseWebsiteCompaniesInstallApplicationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_remove_additions**
> ResponseWebsiteCompaniesRemoveAdditionsResponse website_companies_remove_additions(request=request, content_language=content_language)

Removes additions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsiteCompaniesApi()
request = swagger_client.WebsiteCompaniesRemoveAdditionsRequest() # WebsiteCompaniesRemoveAdditionsRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Removes additions
    api_response = api_instance.website_companies_remove_additions(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_remove_additions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**WebsiteCompaniesRemoveAdditionsRequest**](WebsiteCompaniesRemoveAdditionsRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesRemoveAdditionsResponse**](ResponseWebsiteCompaniesRemoveAdditionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_update**
> ResponseWebsiteCompaniesUpdateResponse website_companies_update(request=request, content_language=content_language)

Update organization details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsiteCompaniesApi()
request = swagger_client.WebsiteCompaniesUpdateRequest() # WebsiteCompaniesUpdateRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Update organization details
    api_response = api_instance.website_companies_update(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**WebsiteCompaniesUpdateRequest**](WebsiteCompaniesUpdateRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesUpdateResponse**](ResponseWebsiteCompaniesUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

