# bumbal.RoutePointsApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_list_route_points**](RoutePointsApi.md#retrieve_list_route_points) | **PUT** /route-points | Find Route Points for multiple routes by route ID
[**retrieve_route_points**](RoutePointsApi.md#retrieve_route_points) | **GET** /route-points/{routeId} | Find Route Points by route ID


# **retrieve_list_route_points**
> list[RoutePointsModel] retrieve_list_route_points(arguments)

Find Route Points for multiple routes by route ID

Returns array of RoutePointsModels

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
api_instance = bumbal.RoutePointsApi(bumbal.ApiClient(configuration))
arguments = bumbal.RoutePointsRetrieveListArguments() # RoutePointsRetrieveListArguments | Route Points RetrieveList Arguments

try:
    # Find Route Points for multiple routes by route ID
    api_response = api_instance.retrieve_list_route_points(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutePointsApi->retrieve_list_route_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**RoutePointsRetrieveListArguments**](RoutePointsRetrieveListArguments.md)| Route Points RetrieveList Arguments | 

### Return type

[**list[RoutePointsModel]**](RoutePointsModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_route_points**
> RoutePointsModel retrieve_route_points(route_id)

Find Route Points by route ID

Returns route_id with a GeoJSON object

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
api_instance = bumbal.RoutePointsApi(bumbal.ApiClient(configuration))
route_id = 789 # int | ID of Route for which to return the Route Points

try:
    # Find Route Points by route ID
    api_response = api_instance.retrieve_route_points(route_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutePointsApi->retrieve_route_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_id** | **int**| ID of Route for which to return the Route Points | 

### Return type

[**RoutePointsModel**](RoutePointsModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

