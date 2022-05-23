# bumbal.LogApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_list_log**](LogApi.md#retrieve_list_log) | **PUT** /log | Retrieve List of Log messages
[**set_log**](LogApi.md#set_log) | **POST** /log/set | Post a Log message


# **retrieve_list_log**
> LogListResponse retrieve_list_log(arguments)

Retrieve List of Log messages

Retrieve List of Log messages

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
api_instance = bumbal.LogApi(bumbal.ApiClient(configuration))
arguments = bumbal.LogRetrieveListArguments() # LogRetrieveListArguments | Log RetrieveList Arguments

try:
    # Retrieve List of Log messages
    api_response = api_instance.retrieve_list_log(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogApi->retrieve_list_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**LogRetrieveListArguments**](LogRetrieveListArguments.md)| Log RetrieveList Arguments | 

### Return type

[**LogListResponse**](LogListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_log**
> ApiResponse set_log(body)

Post a Log message

Post a Log message.

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
api_instance = bumbal.LogApi(bumbal.ApiClient(configuration))
body = bumbal.LogModel() # LogModel | Log object

try:
    # Post a Log message
    api_response = api_instance.set_log(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogApi->set_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LogModel**](LogModel.md)| Log object | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

