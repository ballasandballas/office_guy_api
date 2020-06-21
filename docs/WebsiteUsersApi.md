# office_guy_api.WebsiteUsersApi

All URIs are relative to *https://www.myofficeguy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**website_users_create**](WebsiteUsersApi.md#website_users_create) | **POST** /api/website/users/create/ | Create user and grant permissions to the current organization
[**website_users_login_redirect**](WebsiteUsersApi.md#website_users_login_redirect) | **POST** /api/website/users/loginredirect/ | Login using redirect, without exposing the user credentials.

# **website_users_create**
> ResponseWebsiteUsersCreateResponse website_users_create(body=body, content_language=content_language)

Create user and grant permissions to the current organization

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsiteUsersApi()
body = office_guy_api.Body297() # Body297 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Create user and grant permissions to the current organization
    api_response = api_instance.website_users_create(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteUsersApi->website_users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body297**](Body297.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteUsersCreateResponse**](ResponseWebsiteUsersCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_users_login_redirect**
> ResponseWebsiteUsersLoginRedirectResponse website_users_login_redirect(body=body, content_language=content_language)

Login using redirect, without exposing the user credentials.

Please note, this doesn't validate the user credentials, and will allow creating tokens for incorrect credentials

### Example
```python
from __future__ import print_function
import time
import office_guy_api
from office_guy_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = office_guy_api.WebsiteUsersApi()
body = office_guy_api.Body301() # Body301 |  (optional)
content_language = office_guy_api.ContentLanguage() # ContentLanguage | Sets the content response language. Defaults to Hebrew (he). (optional)

try:
    # Login using redirect, without exposing the user credentials.
    api_response = api_instance.website_users_login_redirect(body=body, content_language=content_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsiteUsersApi->website_users_login_redirect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body301**](Body301.md)|  | [optional] 
 **content_language** | [**ContentLanguage**](.md)| Sets the content response language. Defaults to Hebrew (he). | [optional] 

### Return type

[**ResponseWebsiteUsersLoginRedirectResponse**](ResponseWebsiteUsersLoginRedirectResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

