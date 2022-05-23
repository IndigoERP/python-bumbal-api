# bumbal.AddressAppliedApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_address_applied**](AddressAppliedApi.md#retrieve_address_applied) | **GET** /address-applied/{addressId} | Retrieve an Applied Address
[**update_address_applied**](AddressAppliedApi.md#update_address_applied) | **PUT** /address-applied/{addressId} | Update a AddressApplied


# **retrieve_address_applied**
> AddressAppliedModel retrieve_address_applied(address_id)

Retrieve an Applied Address

Retrieve an Applied Address

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
api_instance = bumbal.AddressAppliedApi(bumbal.ApiClient(configuration))
address_id = 789 # int | ID of the applied address to retrieve

try:
    # Retrieve an Applied Address
    api_response = api_instance.retrieve_address_applied(address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressAppliedApi->retrieve_address_applied: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**| ID of the applied address to retrieve | 

### Return type

[**AddressAppliedModel**](AddressAppliedModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address_applied**
> ApiResponse update_address_applied(address_id, body=body)

Update a AddressApplied

Update an AddressApplied

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
api_instance = bumbal.AddressAppliedApi(bumbal.ApiClient(configuration))
address_id = 789 # int | ID of address to update
body = bumbal.AddressAppliedModel() # AddressAppliedModel | AddressApplied object that needs to be updated (optional)

try:
    # Update a AddressApplied
    api_response = api_instance.update_address_applied(address_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressAppliedApi->update_address_applied: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**| ID of address to update | 
 **body** | [**AddressAppliedModel**](AddressAppliedModel.md)| AddressApplied object that needs to be updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

