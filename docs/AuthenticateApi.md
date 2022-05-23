# bumbal.AuthenticateApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_check_token**](AuthenticateApi.md#authenticate_check_token) | **GET** /authenticate/check-token | Check a token for validity
[**authenticate_sign_in**](AuthenticateApi.md#authenticate_sign_in) | **POST** /authenticate/sign-in | Sign In with your user credentials
[**authenticate_sign_out**](AuthenticateApi.md#authenticate_sign_out) | **GET** /authenticate/sign-out | Sign out


# **authenticate_check_token**
> ApiResponse authenticate_check_token()

Check a token for validity

Check a token for validity

### Example
```python
from __future__ import print_function
import time
import bumbal
from bumbal.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bumbal.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: jwt
configuration = bumbal.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bumbal.AuthenticateApi(bumbal.ApiClient(configuration))

try:
    # Check a token for validity
    api_response = api_instance.authenticate_check_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticateApi->authenticate_check_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_sign_in**
> AuthenticateModel authenticate_sign_in(body=body)

Sign In with your user credentials

Sign In with your user credentials, you will get a access token if successful

### Example
```python
from __future__ import print_function
import time
import bumbal
from bumbal.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bumbal.AuthenticateApi()
body = bumbal.CredentialsModel() # CredentialsModel | Credentials object (optional)

try:
    # Sign In with your user credentials
    api_response = api_instance.authenticate_sign_in(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticateApi->authenticate_sign_in: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CredentialsModel**](CredentialsModel.md)| Credentials object | [optional] 

### Return type

[**AuthenticateModel**](AuthenticateModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_sign_out**
> ApiResponse authenticate_sign_out(token)

Sign out

Sign out using your access token

### Example
```python
from __future__ import print_function
import time
import bumbal
from bumbal.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bumbal.Configuration()
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'
# Configure API key authorization: jwt
configuration = bumbal.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bumbal.AuthenticateApi(bumbal.ApiClient(configuration))
token = 'token_example' # str | Token

try:
    # Sign out
    api_response = api_instance.authenticate_sign_out(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticateApi->authenticate_sign_out: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Token | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

