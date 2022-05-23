# bumbal.DriverUnavailabilityApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_driver_unavailability**](DriverUnavailabilityApi.md#create_driver_unavailability) | **POST** /driver-unavailability | Add a new DriverUnavailability
[**delete_driver_unavailability**](DriverUnavailabilityApi.md#delete_driver_unavailability) | **DELETE** /driver-unavailability/{driverunavailabilityId} | Delete a DriverUnavailability entry
[**retrieve_driver_unavailability**](DriverUnavailabilityApi.md#retrieve_driver_unavailability) | **GET** /driver-unavailability/{driverunavailabilityId} | Retrieve a DriverUnavailability
[**retrieve_list_driver_unavailability**](DriverUnavailabilityApi.md#retrieve_list_driver_unavailability) | **PUT** /driver-unavailability | Retrieve List of DriverUnavailability
[**set_driver_unavailability**](DriverUnavailabilityApi.md#set_driver_unavailability) | **POST** /driver-unavailability/set | Set (create or update) a driver unavailability
[**update_driver_unavailability**](DriverUnavailabilityApi.md#update_driver_unavailability) | **PUT** /driver-unavailability/{driverunavailabilityId} | Update a specific DriverUnavailability object


# **create_driver_unavailability**
> ApiResponse4 create_driver_unavailability(body=body)

Add a new DriverUnavailability

Add a new DriverUnavailability

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
api_instance = bumbal.DriverUnavailabilityApi(bumbal.ApiClient(configuration))
body = bumbal.DriverUnavailabilityModel() # DriverUnavailabilityModel | DriverUnavailability object that needs to be created (optional)

try:
    # Add a new DriverUnavailability
    api_response = api_instance.create_driver_unavailability(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverUnavailabilityApi->create_driver_unavailability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DriverUnavailabilityModel**](DriverUnavailabilityModel.md)| DriverUnavailability object that needs to be created | [optional] 

### Return type

[**ApiResponse4**](ApiResponse4.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_driver_unavailability**
> ApiResponse2 delete_driver_unavailability(driverunavailability_id)

Delete a DriverUnavailability entry

Delete a Metadata entry

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
api_instance = bumbal.DriverUnavailabilityApi(bumbal.ApiClient(configuration))
driverunavailability_id = 789 # int | ID of DriverUnavailability to delete

try:
    # Delete a DriverUnavailability entry
    api_response = api_instance.delete_driver_unavailability(driverunavailability_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverUnavailabilityApi->delete_driver_unavailability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driverunavailability_id** | **int**| ID of DriverUnavailability to delete | 

### Return type

[**ApiResponse2**](ApiResponse2.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_driver_unavailability**
> DriverUnavailabilityModel retrieve_driver_unavailability(driverunavailability_id, include_object_type_name=include_object_type_name, include_record_info=include_record_info)

Retrieve a DriverUnavailability

Retrieve an DriverUnavailability

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
api_instance = bumbal.DriverUnavailabilityApi(bumbal.ApiClient(configuration))
driverunavailability_id = 789 # int | ID of DriverUnavailability to retrieve
include_object_type_name = false # bool | Show the name of the object type (optional) (default to false)
include_record_info = false # bool | Show the record info (optional) (default to false)

try:
    # Retrieve a DriverUnavailability
    api_response = api_instance.retrieve_driver_unavailability(driverunavailability_id, include_object_type_name=include_object_type_name, include_record_info=include_record_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverUnavailabilityApi->retrieve_driver_unavailability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driverunavailability_id** | **int**| ID of DriverUnavailability to retrieve | 
 **include_object_type_name** | **bool**| Show the name of the object type | [optional] [default to false]
 **include_record_info** | **bool**| Show the record info | [optional] [default to false]

### Return type

[**DriverUnavailabilityModel**](DriverUnavailabilityModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_driver_unavailability**
> DriverUnavailabilityListResponse retrieve_list_driver_unavailability(arguments)

Retrieve List of DriverUnavailability

Retrieve List of DriverUnavailability

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
api_instance = bumbal.DriverUnavailabilityApi(bumbal.ApiClient(configuration))
arguments = bumbal.DriverUnavailabilityRetrieveListArguments() # DriverUnavailabilityRetrieveListArguments | DriverUnavailability RetrieveList Arguments

try:
    # Retrieve List of DriverUnavailability
    api_response = api_instance.retrieve_list_driver_unavailability(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverUnavailabilityApi->retrieve_list_driver_unavailability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**DriverUnavailabilityRetrieveListArguments**](DriverUnavailabilityRetrieveListArguments.md)| DriverUnavailability RetrieveList Arguments | 

### Return type

[**DriverUnavailabilityListResponse**](DriverUnavailabilityListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_driver_unavailability**
> ApiResponse set_driver_unavailability(body=body)

Set (create or update) a driver unavailability

Set (create or update) a driver unavailability. If id or links are set in the data, and a corresponding driver unavailability is found in Bumbal, an update will be performed.

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
api_instance = bumbal.DriverUnavailabilityApi(bumbal.ApiClient(configuration))
body = bumbal.DriverUnavailabilityModel() # DriverUnavailabilityModel | DriverUnavailability object (optional)

try:
    # Set (create or update) a driver unavailability
    api_response = api_instance.set_driver_unavailability(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverUnavailabilityApi->set_driver_unavailability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DriverUnavailabilityModel**](DriverUnavailabilityModel.md)| DriverUnavailability object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_driver_unavailability**
> ApiResponse1 update_driver_unavailability(driverunavailability_id, body=body)

Update a specific DriverUnavailability object

Update a specific DriverUnavailability object

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
api_instance = bumbal.DriverUnavailabilityApi(bumbal.ApiClient(configuration))
driverunavailability_id = 789 # int | ID of the DriverUnavailability object to update
body = bumbal.DriverUnavailabilityModel() # DriverUnavailabilityModel | DriverUnavailability object that needs to be updated (optional)

try:
    # Update a specific DriverUnavailability object
    api_response = api_instance.update_driver_unavailability(driverunavailability_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverUnavailabilityApi->update_driver_unavailability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driverunavailability_id** | **int**| ID of the DriverUnavailability object to update | 
 **body** | [**DriverUnavailabilityModel**](DriverUnavailabilityModel.md)| DriverUnavailability object that needs to be updated | [optional] 

### Return type

[**ApiResponse1**](ApiResponse1.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

