# bumbal.VehicleTypeApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vehicle_type**](VehicleTypeApi.md#create_vehicle_type) | **POST** /vehicle-type | Add a new VehicleType
[**delete_vehicle_type**](VehicleTypeApi.md#delete_vehicle_type) | **DELETE** /vehicle-type/{vehicleTypeId} | Delete a VehicleType entry
[**retrieve_list_vehicle_type**](VehicleTypeApi.md#retrieve_list_vehicle_type) | **PUT** /vehicle-type | Retrieve List of VehicleTypes
[**retrieve_vehicle_type**](VehicleTypeApi.md#retrieve_vehicle_type) | **GET** /vehicle-type/{vehicleTypeId} | Retrieve a VehicleType
[**update_vehicle_type**](VehicleTypeApi.md#update_vehicle_type) | **PUT** /vehicle-type/{vehicleTypeId} | Update a specific VehicleType object


# **create_vehicle_type**
> VehicleTypeCreateResponse create_vehicle_type(body=body)

Add a new VehicleType

Add a new VehicleType

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
api_instance = bumbal.VehicleTypeApi(bumbal.ApiClient(configuration))
body = bumbal.VehicleTypeModel() # VehicleTypeModel | VehicleType object that needs to be created (optional)

try:
    # Add a new VehicleType
    api_response = api_instance.create_vehicle_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleTypeApi->create_vehicle_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VehicleTypeModel**](VehicleTypeModel.md)| VehicleType object that needs to be created | [optional] 

### Return type

[**VehicleTypeCreateResponse**](VehicleTypeCreateResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vehicle_type**
> VehicleTypeDeleteResponse delete_vehicle_type(vehicle_type_id)

Delete a VehicleType entry

Delete a VehicleType entry

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
api_instance = bumbal.VehicleTypeApi(bumbal.ApiClient(configuration))
vehicle_type_id = 789 # int | ID of VehicleType to delete

try:
    # Delete a VehicleType entry
    api_response = api_instance.delete_vehicle_type(vehicle_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleTypeApi->delete_vehicle_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_type_id** | **int**| ID of VehicleType to delete | 

### Return type

[**VehicleTypeDeleteResponse**](VehicleTypeDeleteResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_vehicle_type**
> VehicleTypeListResponse retrieve_list_vehicle_type(arguments)

Retrieve List of VehicleTypes

Retrieve List of VehicleTypes

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
api_instance = bumbal.VehicleTypeApi(bumbal.ApiClient(configuration))
arguments = bumbal.VehicleTypeRetrieveListArguments() # VehicleTypeRetrieveListArguments | VehicleType RetrieveList Arguments

try:
    # Retrieve List of VehicleTypes
    api_response = api_instance.retrieve_list_vehicle_type(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleTypeApi->retrieve_list_vehicle_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**VehicleTypeRetrieveListArguments**](VehicleTypeRetrieveListArguments.md)| VehicleType RetrieveList Arguments | 

### Return type

[**VehicleTypeListResponse**](VehicleTypeListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vehicle_type**
> VehicleTypeModel retrieve_vehicle_type(provider_id)

Retrieve a VehicleType

Retrieve an VehicleType

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
api_instance = bumbal.VehicleTypeApi(bumbal.ApiClient(configuration))
provider_id = 789 # int | ID of VehicleType to retrieve

try:
    # Retrieve a VehicleType
    api_response = api_instance.retrieve_vehicle_type(provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleTypeApi->retrieve_vehicle_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**| ID of VehicleType to retrieve | 

### Return type

[**VehicleTypeModel**](VehicleTypeModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vehicle_type**
> VehicleTypeUpdateResponse update_vehicle_type(vehicle_type_id, body=body)

Update a specific VehicleType object

Update a specific VehicleType object

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
api_instance = bumbal.VehicleTypeApi(bumbal.ApiClient(configuration))
vehicle_type_id = 789 # int | ID of the VehicleType object to update
body = bumbal.VehicleTypeModel() # VehicleTypeModel | VehicleType object that needs to be updated (optional)

try:
    # Update a specific VehicleType object
    api_response = api_instance.update_vehicle_type(vehicle_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleTypeApi->update_vehicle_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_type_id** | **int**| ID of the VehicleType object to update | 
 **body** | [**VehicleTypeModel**](VehicleTypeModel.md)| VehicleType object that needs to be updated | [optional] 

### Return type

[**VehicleTypeUpdateResponse**](VehicleTypeUpdateResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

