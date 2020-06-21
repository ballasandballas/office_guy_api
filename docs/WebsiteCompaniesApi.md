# office_guy_api.WebsiteCompaniesApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**website_companies_create**](WebsiteCompaniesApi.md#website_companies_create) | **POST** /api/website/companies/create/ | Create new organization
[**website_companies_get_details**](WebsiteCompaniesApi.md#website_companies_get_details) | **POST** /api/website/companies/getdetails/ | 
[**website_companies_install_additions**](WebsiteCompaniesApi.md#website_companies_install_additions) | **POST** /api/website/companies/installadditions/ | Install additions
[**website_companies_install_applications**](WebsiteCompaniesApi.md#website_companies_install_applications) | **POST** /api/website/companies/installapplications/ | Install applications
[**website_companies_list_quotas**](WebsiteCompaniesApi.md#website_companies_list_quotas) | **POST** /api/website/companies/listquotas/ | 
[**website_companies_remove_additions**](WebsiteCompaniesApi.md#website_companies_remove_additions) | **POST** /api/website/companies/removeadditions/ | Removes additions
[**website_companies_update**](WebsiteCompaniesApi.md#website_companies_update) | **POST** /api/website/companies/update/ | Update organization details

# **website_companies_create**
> ResponseWebsiteCompaniesCreateResponse website_companies_create(body=body, content_language=content_language)

Create new organization

Created organization payment method, will be set to the calling organization payment method.  This method requires an active payment method.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsiteCompaniesApi()
body = office_guy_api.Body261() # Body261 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Create new organization
    api_response = api_instance.website_companies_create(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body261**](Body261.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesCreateResponse**](ResponseWebsiteCompaniesCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_get_details**
> ResponseWebsiteCompaniesGetDetailsResponse website_companies_get_details(body=body, content_language=content_language)



### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsiteCompaniesApi()
body = office_guy_api.Body269() # Body269 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    api_response = api_instance.website_companies_get_details(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body269**](Body269.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesGetDetailsResponse**](ResponseWebsiteCompaniesGetDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_install_additions**
> ResponseWebsiteCompaniesInstallAdditionsResponse website_companies_install_additions(body=body, content_language=content_language)

Install additions

Please note this method requires an active payment method.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsiteCompaniesApi()
body = office_guy_api.Body281() # Body281 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Install additions
    api_response = api_instance.website_companies_install_additions(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_install_additions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body281**](Body281.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesInstallAdditionsResponse**](ResponseWebsiteCompaniesInstallAdditionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_install_applications**
> ResponseWebsiteCompaniesInstallApplicationsResponse website_companies_install_applications(body=body, content_language=content_language)

Install applications

Please note this method requires an active payment method.

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsiteCompaniesApi()
body = office_guy_api.Body277() # Body277 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Install applications
    api_response = api_instance.website_companies_install_applications(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_install_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body277**](Body277.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesInstallApplicationsResponse**](ResponseWebsiteCompaniesInstallApplicationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_list_quotas**
> ResponseWebsiteCompaniesListQuotasResponse website_companies_list_quotas(body=body, content_language=content_language)



### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsiteCompaniesApi()
body = office_guy_api.Body273() # Body273 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    api_response = api_instance.website_companies_list_quotas(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_list_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body273**](Body273.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesListQuotasResponse**](ResponseWebsiteCompaniesListQuotasResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_remove_additions**
> ResponseWebsiteCompaniesRemoveAdditionsResponse website_companies_remove_additions(body=body, content_language=content_language)

Removes additions

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsiteCompaniesApi()
body = office_guy_api.Body285() # Body285 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Removes additions
    api_response = api_instance.website_companies_remove_additions(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_remove_additions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body285**](Body285.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesRemoveAdditionsResponse**](ResponseWebsiteCompaniesRemoveAdditionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_companies_update**
> ResponseWebsiteCompaniesUpdateResponse website_companies_update(body=body, content_language=content_language)

Update organization details

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsiteCompaniesApi()
body = office_guy_api.Body265() # Body265 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Update organization details
    api_response = api_instance.website_companies_update(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteCompaniesApi->website_companies_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body265**](Body265.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteCompaniesUpdateResponse**](ResponseWebsiteCompaniesUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

