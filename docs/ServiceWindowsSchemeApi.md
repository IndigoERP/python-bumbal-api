# bumbal.ServiceWindowsSchemeApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_service_windows_scheme**](ServiceWindowsSchemeApi.md#delete_service_windows_scheme) | **DELETE** /service-windows-scheme/{serviceWindowsSchemeId} | Delete a service windows scheme
[**retrieve_list_service_windows_scheme**](ServiceWindowsSchemeApi.md#retrieve_list_service_windows_scheme) | **PUT** /service-windows-scheme | Retrieve a list of service windows schemes
[**retrieve_service_windows_scheme**](ServiceWindowsSchemeApi.md#retrieve_service_windows_scheme) | **GET** /service-windows-scheme/{serviceWindowsSchemeId} | Retrieve a single service windows scheme
[**set_service_windows_scheme**](ServiceWindowsSchemeApi.md#set_service_windows_scheme) | **POST** /service-windows-scheme/set | Add or update a service windows scheme


# **delete_service_windows_scheme**
> ApiResponse delete_service_windows_scheme(service_windows_scheme_id)

Delete a service windows scheme

Delete a service windows scheme

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
api_instance = bumbal.ServiceWindowsSchemeApi(bumbal.ApiClient(configuration))
service_windows_scheme_id = 789 # int | ID of Service Windows Scheme to delete

try:
    # Delete a service windows scheme
    api_response = api_instance.delete_service_windows_scheme(service_windows_scheme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceWindowsSchemeApi->delete_service_windows_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_windows_scheme_id** | **int**| ID of Service Windows Scheme to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_service_windows_scheme**
> ServiceWindowsSchemeListResponse retrieve_list_service_windows_scheme(arguments)

Retrieve a list of service windows schemes

Retrieve a list of service windows schemes

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
api_instance = bumbal.ServiceWindowsSchemeApi(bumbal.ApiClient(configuration))
arguments = bumbal.ServiceWindowsSchemeRetrieveListArguments() # ServiceWindowsSchemeRetrieveListArguments | Service Windows Scheme RetrieveList Arguments

try:
    # Retrieve a list of service windows schemes
    api_response = api_instance.retrieve_list_service_windows_scheme(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceWindowsSchemeApi->retrieve_list_service_windows_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**ServiceWindowsSchemeRetrieveListArguments**](ServiceWindowsSchemeRetrieveListArguments.md)| Service Windows Scheme RetrieveList Arguments | 

### Return type

[**ServiceWindowsSchemeListResponse**](ServiceWindowsSchemeListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_service_windows_scheme**
> ServiceWindowsSchemeModel retrieve_service_windows_scheme(service_windows_scheme_id)

Retrieve a single service windows scheme

Retrieve a single service windows scheme

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
api_instance = bumbal.ServiceWindowsSchemeApi(bumbal.ApiClient(configuration))
service_windows_scheme_id = 789 # int | ID of Service windows scheme to retrieve

try:
    # Retrieve a single service windows scheme
    api_response = api_instance.retrieve_service_windows_scheme(service_windows_scheme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceWindowsSchemeApi->retrieve_service_windows_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_windows_scheme_id** | **int**| ID of Service windows scheme to retrieve | 

### Return type

[**ServiceWindowsSchemeModel**](ServiceWindowsSchemeModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_service_windows_scheme**
> ApiResponse set_service_windows_scheme(body=body)

Add or update a service windows scheme

Add or update a service windows scheme

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
api_instance = bumbal.ServiceWindowsSchemeApi(bumbal.ApiClient(configuration))
body = bumbal.ServiceWindowsSchemeModel() # ServiceWindowsSchemeModel | Service windows scheme object that needs to be created or updated (optional)

try:
    # Add or update a service windows scheme
    api_response = api_instance.set_service_windows_scheme(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceWindowsSchemeApi->set_service_windows_scheme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceWindowsSchemeModel**](ServiceWindowsSchemeModel.md)| Service windows scheme object that needs to be created or updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

