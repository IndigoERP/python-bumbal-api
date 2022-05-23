# bumbal.ServiceWindowApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_list_service_window**](ServiceWindowApi.md#retrieve_list_service_window) | **PUT** /service-window | Retrieve a list of service windows
[**retrieve_service_window**](ServiceWindowApi.md#retrieve_service_window) | **GET** /service-window/{serviceWindowId} | Retrieve a single service window
[**set_service_window**](ServiceWindowApi.md#set_service_window) | **POST** /service-window/set | Add or update a service window


# **retrieve_list_service_window**
> ServiceWindowListResponse retrieve_list_service_window(arguments)

Retrieve a list of service windows

Retrieve a list of service windows

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
api_instance = bumbal.ServiceWindowApi(bumbal.ApiClient(configuration))
arguments = bumbal.ServiceWindowRetrieveListArguments() # ServiceWindowRetrieveListArguments | Service Window RetrieveList Arguments

try:
    # Retrieve a list of service windows
    api_response = api_instance.retrieve_list_service_window(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceWindowApi->retrieve_list_service_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**ServiceWindowRetrieveListArguments**](ServiceWindowRetrieveListArguments.md)| Service Window RetrieveList Arguments | 

### Return type

[**ServiceWindowListResponse**](ServiceWindowListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_service_window**
> ServiceWindowModel retrieve_service_window(service_window_id)

Retrieve a single service window

Retrieve a single service window

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
api_instance = bumbal.ServiceWindowApi(bumbal.ApiClient(configuration))
service_window_id = 789 # int | ID of Service windows scheme to retrieve

try:
    # Retrieve a single service window
    api_response = api_instance.retrieve_service_window(service_window_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceWindowApi->retrieve_service_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_window_id** | **int**| ID of Service windows scheme to retrieve | 

### Return type

[**ServiceWindowModel**](ServiceWindowModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_service_window**
> ApiResponse set_service_window(body=body)

Add or update a service window

Add or update a service window

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
api_instance = bumbal.ServiceWindowApi(bumbal.ApiClient(configuration))
body = bumbal.ServiceWindowModel() # ServiceWindowModel | Service window object that needs to be created or updated (optional)

try:
    # Add or update a service window
    api_response = api_instance.set_service_window(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceWindowApi->set_service_window: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceWindowModel**](ServiceWindowModel.md)| Service window object that needs to be created or updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

