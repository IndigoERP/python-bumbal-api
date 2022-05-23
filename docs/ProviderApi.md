# bumbal.ProviderApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_provider**](ProviderApi.md#create_provider) | **POST** /provider | Add a new Provider
[**retrieve_list_provider**](ProviderApi.md#retrieve_list_provider) | **PUT** /provider | Retrieve List of Providers
[**retrieve_provider**](ProviderApi.md#retrieve_provider) | **GET** /provider/{providerId} | Retrieve a Provider
[**update_provider**](ProviderApi.md#update_provider) | **PUT** /provider/{providerId} | Update a specific provider object


# **create_provider**
> ApiResponse22 create_provider(body=body)

Add a new Provider

Add a new Provider

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
api_instance = bumbal.ProviderApi(bumbal.ApiClient(configuration))
body = bumbal.ProviderModel() # ProviderModel | Provider object that needs to be created (optional)

try:
    # Add a new Provider
    api_response = api_instance.create_provider(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->create_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProviderModel**](ProviderModel.md)| Provider object that needs to be created | [optional] 

### Return type

[**ApiResponse22**](ApiResponse22.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_provider**
> ProviderListResponse retrieve_list_provider(arguments)

Retrieve List of Providers

Retrieve List of Providers

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
api_instance = bumbal.ProviderApi(bumbal.ApiClient(configuration))
arguments = bumbal.ProviderRetrieveListArguments() # ProviderRetrieveListArguments | Provider RetrieveList Arguments

try:
    # Retrieve List of Providers
    api_response = api_instance.retrieve_list_provider(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->retrieve_list_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**ProviderRetrieveListArguments**](ProviderRetrieveListArguments.md)| Provider RetrieveList Arguments | 

### Return type

[**ProviderListResponse**](ProviderListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_provider**
> ProviderModel retrieve_provider(provider_id)

Retrieve a Provider

Retrieve an Provider

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
api_instance = bumbal.ProviderApi(bumbal.ApiClient(configuration))
provider_id = 789 # int | ID of provider to retrieve

try:
    # Retrieve a Provider
    api_response = api_instance.retrieve_provider(provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->retrieve_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**| ID of provider to retrieve | 

### Return type

[**ProviderModel**](ProviderModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_provider**
> ApiResponse21 update_provider(provider_id, body=body)

Update a specific provider object

Update a specific provider object

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
api_instance = bumbal.ProviderApi(bumbal.ApiClient(configuration))
provider_id = 789 # int | ID of the provider object to update
body = bumbal.ProviderModel() # ProviderModel | Provider object that needs to be updated (optional)

try:
    # Update a specific provider object
    api_response = api_instance.update_provider(provider_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProviderApi->update_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**| ID of the provider object to update | 
 **body** | [**ProviderModel**](ProviderModel.md)| Provider object that needs to be updated | [optional] 

### Return type

[**ApiResponse21**](ApiResponse21.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

