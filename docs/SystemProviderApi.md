# bumbal.SystemProviderApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_list_system_provider**](SystemProviderApi.md#retrieve_list_system_provider) | **PUT** /system-provider | Retrieve List of System Providers
[**retrieve_system_provider**](SystemProviderApi.md#retrieve_system_provider) | **GET** /system-provider/{providerId} | Retrieve a System Provider


# **retrieve_list_system_provider**
> SystemProviderListResponse retrieve_list_system_provider(arguments)

Retrieve List of System Providers

Retrieve List of System Providers

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
api_instance = bumbal.SystemProviderApi(bumbal.ApiClient(configuration))
arguments = bumbal.SystemProviderRetrieveListArguments() # SystemProviderRetrieveListArguments | System Provider RetrieveList Arguments

try:
    # Retrieve List of System Providers
    api_response = api_instance.retrieve_list_system_provider(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemProviderApi->retrieve_list_system_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**SystemProviderRetrieveListArguments**](SystemProviderRetrieveListArguments.md)| System Provider RetrieveList Arguments | 

### Return type

[**SystemProviderListResponse**](SystemProviderListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_system_provider**
> SystemProviderModel retrieve_system_provider(provider_id)

Retrieve a System Provider

Retrieve a System Provider

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
api_instance = bumbal.SystemProviderApi(bumbal.ApiClient(configuration))
provider_id = 789 # int | ID of System Provider to retrieve

try:
    # Retrieve a System Provider
    api_response = api_instance.retrieve_system_provider(provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemProviderApi->retrieve_system_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**| ID of System Provider to retrieve | 

### Return type

[**SystemProviderModel**](SystemProviderModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

