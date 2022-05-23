# bumbal.VehicleApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vehicle**](VehicleApi.md#create_vehicle) | **POST** /vehicle | Add a new vehicle
[**delete_vehicle**](VehicleApi.md#delete_vehicle) | **DELETE** /vehicle/{vehicleId} | Delete a vehicle entry
[**retrieve_list_vehicle**](VehicleApi.md#retrieve_list_vehicle) | **PUT** /vehicle | Retrieve List of Vehicles
[**retrieve_vehicle**](VehicleApi.md#retrieve_vehicle) | **GET** /vehicle/{vehicleId} | Find vehicle by ID
[**set_vehicle**](VehicleApi.md#set_vehicle) | **POST** /vehicle/set | Set (create or update) a vehicle
[**update_vehicle**](VehicleApi.md#update_vehicle) | **PUT** /vehicle/{vehicleId} | Update a vehicle


# **create_vehicle**
> ApiResponse57 create_vehicle(body=body)

Add a new vehicle

Add a new vehicle

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
api_instance = bumbal.VehicleApi(bumbal.ApiClient(configuration))
body = bumbal.VehicleModel() # VehicleModel | Vehicle object that needs to be created (optional)

try:
    # Add a new vehicle
    api_response = api_instance.create_vehicle(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->create_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VehicleModel**](VehicleModel.md)| Vehicle object that needs to be created | [optional] 

### Return type

[**ApiResponse57**](ApiResponse57.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vehicle**
> ApiResponse58 delete_vehicle(vehicle_id)

Delete a vehicle entry

Delete a vehicle entry

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
api_instance = bumbal.VehicleApi(bumbal.ApiClient(configuration))
vehicle_id = 789 # int | ID of vehicle to delete

try:
    # Delete a vehicle entry
    api_response = api_instance.delete_vehicle(vehicle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->delete_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| ID of vehicle to delete | 

### Return type

[**ApiResponse58**](ApiResponse58.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_vehicle**
> list[VehicleModel] retrieve_list_vehicle(arguments)

Retrieve List of Vehicles

Retrieve List of Vehicles

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
api_instance = bumbal.VehicleApi(bumbal.ApiClient(configuration))
arguments = bumbal.VehicleRetrieveListArguments() # VehicleRetrieveListArguments | Vehicle RetrieveList Arguments

try:
    # Retrieve List of Vehicles
    api_response = api_instance.retrieve_list_vehicle(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->retrieve_list_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**VehicleRetrieveListArguments**](VehicleRetrieveListArguments.md)| Vehicle RetrieveList Arguments | 

### Return type

[**list[VehicleModel]**](VehicleModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_vehicle**
> VehicleModel retrieve_vehicle(vehicle_id, include_vehicle_tags, include_updated_by)

Find vehicle by ID

Returns a single vehicle

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
api_instance = bumbal.VehicleApi(bumbal.ApiClient(configuration))
vehicle_id = 789 # int | ID of vehicle to return
include_vehicle_tags = true # bool | a list of tags bound to vehicle (default to true)
include_updated_by = true # bool | include updated_by_name (default to true)

try:
    # Find vehicle by ID
    api_response = api_instance.retrieve_vehicle(vehicle_id, include_vehicle_tags, include_updated_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->retrieve_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| ID of vehicle to return | 
 **include_vehicle_tags** | **bool**| a list of tags bound to vehicle | [default to true]
 **include_updated_by** | **bool**| include updated_by_name | [default to true]

### Return type

[**VehicleModel**](VehicleModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_vehicle**
> ApiResponse set_vehicle(body=body)

Set (create or update) a vehicle

Set (create or update) a vehicle. If id or links are set in the data, and a corresponding vehicle is found in Bumbal, an update will be performed.

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
api_instance = bumbal.VehicleApi(bumbal.ApiClient(configuration))
body = bumbal.VehicleModel() # VehicleModel | Vehicle object (optional)

try:
    # Set (create or update) a vehicle
    api_response = api_instance.set_vehicle(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->set_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VehicleModel**](VehicleModel.md)| Vehicle object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vehicle**
> ApiResponse update_vehicle(vehicle_id, body=body)

Update a vehicle

Update a vehicle

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
api_instance = bumbal.VehicleApi(bumbal.ApiClient(configuration))
vehicle_id = 789 # int | ID of vehicle to update
body = bumbal.VehicleModel() # VehicleModel | Vehicle object that needs to be updated (optional)

try:
    # Update a vehicle
    api_response = api_instance.update_vehicle(vehicle_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VehicleApi->update_vehicle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vehicle_id** | **int**| ID of vehicle to update | 
 **body** | [**VehicleModel**](VehicleModel.md)| Vehicle object that needs to be updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

