# bumbal.DriverApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_driver**](DriverApi.md#create_driver) | **POST** /driver | Add a driver
[**delete_driver**](DriverApi.md#delete_driver) | **DELETE** /driver/{driverId} | Delete an driver
[**retrieve_driver**](DriverApi.md#retrieve_driver) | **GET** /driver/{driverId} | Find driver by ID
[**retrieve_list_driver**](DriverApi.md#retrieve_list_driver) | **PUT** /driver | Retrieve List of Drivers
[**set_driver**](DriverApi.md#set_driver) | **POST** /driver/set | Set (create or update) a driver
[**update_driver**](DriverApi.md#update_driver) | **PUT** /driver/{driverId} | Update a driver


# **create_driver**
> ApiResponse create_driver(body=body)

Add a driver

Add a driver

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
api_instance = bumbal.DriverApi(bumbal.ApiClient(configuration))
body = bumbal.DriverModel() # DriverModel | Driver object that needs to be created (optional)

try:
    # Add a driver
    api_response = api_instance.create_driver(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverApi->create_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DriverModel**](DriverModel.md)| Driver object that needs to be created | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_driver**
> ApiResponse delete_driver(driver_id)

Delete an driver

Delete an driver

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
api_instance = bumbal.DriverApi(bumbal.ApiClient(configuration))
driver_id = 789 # int | ID of the driver to delete

try:
    # Delete an driver
    api_response = api_instance.delete_driver(driver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverApi->delete_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the driver to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_driver**
> DriverModel retrieve_driver(driver_id, include_driver_tags, include_updated_by)

Find driver by ID

Returns a single driver

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
api_instance = bumbal.DriverApi(bumbal.ApiClient(configuration))
driver_id = 789 # int | ID of driver to return
include_driver_tags = true # bool | a list of tags bound to driver (default to true)
include_updated_by = true # bool | include updated_by_name (default to true)

try:
    # Find driver by ID
    api_response = api_instance.retrieve_driver(driver_id, include_driver_tags, include_updated_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverApi->retrieve_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of driver to return | 
 **include_driver_tags** | **bool**| a list of tags bound to driver | [default to true]
 **include_updated_by** | **bool**| include updated_by_name | [default to true]

### Return type

[**DriverModel**](DriverModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_driver**
> DriverListResponse retrieve_list_driver(arguments)

Retrieve List of Drivers

Retrieve List of Drivers

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
api_instance = bumbal.DriverApi(bumbal.ApiClient(configuration))
arguments = bumbal.DriverRetrieveListArguments() # DriverRetrieveListArguments | Driver RetrieveList Arguments

try:
    # Retrieve List of Drivers
    api_response = api_instance.retrieve_list_driver(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverApi->retrieve_list_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**DriverRetrieveListArguments**](DriverRetrieveListArguments.md)| Driver RetrieveList Arguments | 

### Return type

[**DriverListResponse**](DriverListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_driver**
> ApiResponse set_driver(body=body)

Set (create or update) a driver

Set (create or update) a driver. If id or links are set in the data, and a corresponding driver is found in Bumbal, an update will be performed.

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
api_instance = bumbal.DriverApi(bumbal.ApiClient(configuration))
body = bumbal.DriverModel() # DriverModel | Driver object (optional)

try:
    # Set (create or update) a driver
    api_response = api_instance.set_driver(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverApi->set_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DriverModel**](DriverModel.md)| Driver object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_driver**
> ApiResponse update_driver(driver_id, body=body)

Update a driver

Update a driver

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
api_instance = bumbal.DriverApi(bumbal.ApiClient(configuration))
driver_id = 789 # int | ID of driver to update
body = bumbal.DriverModel() # DriverModel | Driver object that needs to be updated (optional)

try:
    # Update a driver
    api_response = api_instance.update_driver(driver_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DriverApi->update_driver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of driver to update | 
 **body** | [**DriverModel**](DriverModel.md)| Driver object that needs to be updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

