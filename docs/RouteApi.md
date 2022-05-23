# bumbal.RouteApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**block_routes**](RouteApi.md#block_routes) | **POST** /route/block-routes | Block routes which satisfy set filters
[**create_route**](RouteApi.md#create_route) | **POST** /route | Add a new Route
[**delete_route**](RouteApi.md#delete_route) | **DELETE** /route/{routeId} | Delete an Route
[**get_executable_activities**](RouteApi.md#get_executable_activities) | **POST** /route/get-executable-activities | Returns all activities in this route which hav enot been executed yet.
[**retrieve_list_route**](RouteApi.md#retrieve_list_route) | **PUT** /route | Retrieve List of Routes
[**retrieve_route**](RouteApi.md#retrieve_route) | **GET** /route/{routeId} | Retrieve a Route
[**route_store_geo_locations**](RouteApi.md#route_store_geo_locations) | **POST** /route/store-geo-locations | Store tracked Geo Locations in bulk
[**set_route**](RouteApi.md#set_route) | **POST** /route/set | Set (create or update) an Route
[**unblock_routes**](RouteApi.md#unblock_routes) | **POST** /route/unblock-routes | Unblock routes which satisfy set filters
[**update_route**](RouteApi.md#update_route) | **PUT** /route/{routeId} | Update a Route


# **block_routes**
> ApiResponse block_routes(filters)

Block routes which satisfy set filters

Block routes which satisfy set filters

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
api_instance = bumbal.RouteApi(bumbal.ApiClient(configuration))
filters = bumbal.RouteFiltersModel() # RouteFiltersModel | Request Filters

try:
    # Block routes which satisfy set filters
    api_response = api_instance.block_routes(filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->block_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**RouteFiltersModel**](RouteFiltersModel.md)| Request Filters | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_route**
> ApiResponse create_route(body=body)

Add a new Route

Add a new Route

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
api_instance = bumbal.RouteApi(bumbal.ApiClient(configuration))
body = bumbal.RouteModel() # RouteModel | Route object that needs to be created (optional)

try:
    # Add a new Route
    api_response = api_instance.create_route(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->create_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RouteModel**](RouteModel.md)| Route object that needs to be created | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_route**
> ApiResponse delete_route(route_id, cancel_activities)

Delete an Route

Delete an Route

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
api_instance = bumbal.RouteApi(bumbal.ApiClient(configuration))
route_id = 789 # int | ID of route to update
cancel_activities = true # bool | Cancel activities on Route

try:
    # Delete an Route
    api_response = api_instance.delete_route(route_id, cancel_activities)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->delete_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| ID of route to update | 
 **cancel_activities** | **bool**| Cancel activities on Route | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_executable_activities**
> ApiResponse get_executable_activities(arguments)

Returns all activities in this route which hav enot been executed yet.

Returns all activities in this route which have not been executed yet. This will be in execution order.

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
api_instance = bumbal.RouteApi(bumbal.ApiClient(configuration))
arguments = bumbal.GetExecutableActivitiesArguments() # GetExecutableActivitiesArguments | Request Arguments

try:
    # Returns all activities in this route which hav enot been executed yet.
    api_response = api_instance.get_executable_activities(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->get_executable_activities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**GetExecutableActivitiesArguments**](GetExecutableActivitiesArguments.md)| Request Arguments | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_route**
> RouteListResponse retrieve_list_route(arguments)

Retrieve List of Routes

Retrieve List of Routes

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
api_instance = bumbal.RouteApi(bumbal.ApiClient(configuration))
arguments = bumbal.RouteRetrieveListArguments() # RouteRetrieveListArguments | Route RetrieveList Arguments

try:
    # Retrieve List of Routes
    api_response = api_instance.retrieve_list_route(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->retrieve_list_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**RouteRetrieveListArguments**](RouteRetrieveListArguments.md)| Route RetrieveList Arguments | 

### Return type

[**RouteListResponse**](RouteListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_route**
> RouteModel retrieve_route(route_id, include_address_object, include_route_status, include_route_tags, include_driver_info, include_equipment_info_car, include_gps_locations, include_activity_ids, include_latest_position)

Retrieve a Route

Retrieve an Route

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
api_instance = bumbal.RouteApi(bumbal.ApiClient(configuration))
route_id = 789 # int | ID of route to retrieve
include_address_object = true # bool | Include Address Objects (default to true)
include_route_status = true # bool | Include Status Name (default to true)
include_route_tags = true # bool | Include Tags (default to true)
include_driver_info = true # bool | Include Driver info (default to true)
include_equipment_info_car = true # bool | Include Equipment info car (default to true)
include_gps_locations = false # bool | Include GPS locations (default to false)
include_activity_ids = false # bool | Include Activity IDs (default to false)
include_latest_position = false # bool | Include Latest Known GPS location (default to false)

try:
    # Retrieve a Route
    api_response = api_instance.retrieve_route(route_id, include_address_object, include_route_status, include_route_tags, include_driver_info, include_equipment_info_car, include_gps_locations, include_activity_ids, include_latest_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->retrieve_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| ID of route to retrieve | 
 **include_address_object** | **bool**| Include Address Objects | [default to true]
 **include_route_status** | **bool**| Include Status Name | [default to true]
 **include_route_tags** | **bool**| Include Tags | [default to true]
 **include_driver_info** | **bool**| Include Driver info | [default to true]
 **include_equipment_info_car** | **bool**| Include Equipment info car | [default to true]
 **include_gps_locations** | **bool**| Include GPS locations | [default to false]
 **include_activity_ids** | **bool**| Include Activity IDs | [default to false]
 **include_latest_position** | **bool**| Include Latest Known GPS location | [default to false]

### Return type

[**RouteModel**](RouteModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route_store_geo_locations**
> ApiResponse route_store_geo_locations(arguments)

Store tracked Geo Locations in bulk

Store tracked Geo Locations in bulk

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
api_instance = bumbal.RouteApi(bumbal.ApiClient(configuration))
arguments = bumbal.RouteStoreGeoLocations() # RouteStoreGeoLocations | Request Arguments

try:
    # Store tracked Geo Locations in bulk
    api_response = api_instance.route_store_geo_locations(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->route_store_geo_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**RouteStoreGeoLocations**](RouteStoreGeoLocations.md)| Request Arguments | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_route**
> ApiResponse set_route(body=body)

Set (create or update) an Route

Set (create or update) an Route. If id or links are set in the data, and a corresponding route is found in Bumbal, an update will be performed.

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
api_instance = bumbal.RouteApi(bumbal.ApiClient(configuration))
body = bumbal.RouteModel() # RouteModel | Route object (optional)

try:
    # Set (create or update) an Route
    api_response = api_instance.set_route(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->set_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RouteModel**](RouteModel.md)| Route object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unblock_routes**
> ApiResponse unblock_routes(filters)

Unblock routes which satisfy set filters

Unblock routes which satisfy set filters

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
api_instance = bumbal.RouteApi(bumbal.ApiClient(configuration))
filters = bumbal.RouteFiltersModel() # RouteFiltersModel | Request Filters

try:
    # Unblock routes which satisfy set filters
    api_response = api_instance.unblock_routes(filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->unblock_routes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**RouteFiltersModel**](RouteFiltersModel.md)| Request Filters | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_route**
> ApiResponse update_route(route_id)

Update a Route

Update an Route

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
api_instance = bumbal.RouteApi(bumbal.ApiClient(configuration))
route_id = 789 # int | ID of route to update

try:
    # Update a Route
    api_response = api_instance.update_route(route_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RouteApi->update_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| ID of route to update | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

