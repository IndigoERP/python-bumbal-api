# bumbal.TrackTraceApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track_trace_calculate_eta**](TrackTraceApi.md#track_trace_calculate_eta) | **GET** /track-and-trace/calculate-eta/{activityId} | Calculate ETA for Activity
[**track_trace_calculate_routes_eta**](TrackTraceApi.md#track_trace_calculate_routes_eta) | **PUT** /track-and-trace/calculate-routes-eta | Calculate ETA for Activities on Routes


# **track_trace_calculate_eta**
> ApiResponse track_trace_calculate_eta(activity_id)

Calculate ETA for Activity

Calculate ETA for Activity

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
api_instance = bumbal.TrackTraceApi(bumbal.ApiClient(configuration))
activity_id = 789 # int | ID of the activity to calculate ETA for

try:
    # Calculate ETA for Activity
    api_response = api_instance.track_trace_calculate_eta(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackTraceApi->track_trace_calculate_eta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| ID of the activity to calculate ETA for | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_trace_calculate_routes_eta**
> RoutesEtaResponse track_trace_calculate_routes_eta(arguments)

Calculate ETA for Activities on Routes

Calculate ETA for Activities on Routes

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
api_instance = bumbal.TrackTraceApi(bumbal.ApiClient(configuration))
arguments = bumbal.RoutesEtaArguments() # RoutesEtaArguments | Routes ETA Arguments

try:
    # Calculate ETA for Activities on Routes
    api_response = api_instance.track_trace_calculate_routes_eta(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackTraceApi->track_trace_calculate_routes_eta: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**RoutesEtaArguments**](RoutesEtaArguments.md)| Routes ETA Arguments | 

### Return type

[**RoutesEtaResponse**](RoutesEtaResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

