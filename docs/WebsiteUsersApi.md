# swagger_client.WebsiteUsersApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**website_users_create**](WebsiteUsersApi.md#website_users_create) | **POST** /api/website/users/create/ | Create user and grant permissions to the current organization
[**website_users_login_redirect**](WebsiteUsersApi.md#website_users_login_redirect) | **POST** /api/website/users/loginredirect/ | Login using redirect, without exposing the user credentials.


# **website_users_create**
> ResponseWebsiteUsersCreateResponse website_users_create(request=request, content_language=content_language)

Create user and grant permissions to the current organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsiteUsersApi()
request = swagger_client.WebsiteUsersCreateRequest() # WebsiteUsersCreateRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Create user and grant permissions to the current organization
    api_response = api_instance.website_users_create(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteUsersApi->website_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**WebsiteUsersCreateRequest**](WebsiteUsersCreateRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteUsersCreateResponse**](ResponseWebsiteUsersCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_users_login_redirect**
> ResponseWebsiteUsersLoginRedirectResponse website_users_login_redirect(request=request, content_language=content_language)

Login using redirect, without exposing the user credentials.

Please note, this doesn't validate the user credentials, and will allow creating tokens for incorrect credentials

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsiteUsersApi()
request = swagger_client.WebsiteUsersLoginRedirectRequest() # WebsiteUsersLoginRedirectRequest |  (optional)
content_language = 'content_language_example' # str | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Login using redirect, without exposing the user credentials.
    api_response = api_instance.website_users_login_redirect(request=request, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteUsersApi->website_users_login_redirect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**WebsiteUsersLoginRedirectRequest**](WebsiteUsersLoginRedirectRequest.md)|  | [optional] 
 **content_language** | **str**| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteUsersLoginRedirectResponse**](ResponseWebsiteUsersLoginRedirectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

