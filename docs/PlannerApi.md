# bumbal.PlannerApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_planning**](PlannerApi.md#apply_planning) | **POST** /planner/apply-planning | Apply a planning schema
[**auto_plan**](PlannerApi.md#auto_plan) | **POST** /planner/auto-plan | Plan a certain activity in any fitting route
[**auto_plan_result**](PlannerApi.md#auto_plan_result) | **POST** /planner/auto-plan-result | Fetch current result for a auto plan Request. This could be done, in progress or cancelled.
[**change_activity_sequence**](PlannerApi.md#change_activity_sequence) | **POST** /planner/change-activity-sequence | Change Activity Sequence
[**check_availability**](PlannerApi.md#check_availability) | **POST** /planner/check-availability | check availability in planning for a certain set of activity properties
[**check_availability_result**](PlannerApi.md#check_availability_result) | **POST** /planner/check-availability-result | Fetch current result for a checkAvailability Request. This could be done, in progress or cancelled.
[**planner_add_activities_to_route**](PlannerApi.md#planner_add_activities_to_route) | **POST** /planner/add-activities-to-route | Add Activities to Route
[**remove_activities_from_route**](PlannerApi.md#remove_activities_from_route) | **POST** /planner/remove-activities-from-route | Remove Activities From Route


# **apply_planning**
> ApiResponse apply_planning(arguments)

Apply a planning schema

Apply a planning schema

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
api_instance = bumbal.PlannerApi(bumbal.ApiClient(configuration))
arguments = bumbal.ApplyPlanningArguments() # ApplyPlanningArguments | Request Arguments

try:
    # Apply a planning schema
    api_response = api_instance.apply_planning(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlannerApi->apply_planning: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**ApplyPlanningArguments**](ApplyPlanningArguments.md)| Request Arguments | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auto_plan**
> ApiResponse auto_plan(arguments)

Plan a certain activity in any fitting route

Plan a certain activity in any fitting route

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
api_instance = bumbal.PlannerApi(bumbal.ApiClient(configuration))
arguments = bumbal.AutoPlanArguments() # AutoPlanArguments | Request Arguments

try:
    # Plan a certain activity in any fitting route
    api_response = api_instance.auto_plan(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlannerApi->auto_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**AutoPlanArguments**](AutoPlanArguments.md)| Request Arguments | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auto_plan_result**
> ApiResponse auto_plan_result(arguments)

Fetch current result for a auto plan Request. This could be done, in progress or cancelled.

Fetch current result for a auto plan Request. This could be done, in progress or cancelled.

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
api_instance = bumbal.PlannerApi(bumbal.ApiClient(configuration))
arguments = bumbal.AutoPlanArguments() # AutoPlanArguments | Request Arguments

try:
    # Fetch current result for a auto plan Request. This could be done, in progress or cancelled.
    api_response = api_instance.auto_plan_result(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlannerApi->auto_plan_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**AutoPlanArguments**](AutoPlanArguments.md)| Request Arguments | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_activity_sequence**
> ApiResponse change_activity_sequence()

Change Activity Sequence

Change Activity Sequence

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
api_instance = bumbal.PlannerApi(bumbal.ApiClient(configuration))

try:
    # Change Activity Sequence
    api_response = api_instance.change_activity_sequence()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlannerApi->change_activity_sequence: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_availability**
> ApiResponse check_availability(arguments)

check availability in planning for a certain set of activity properties

check availability in planning for a certain set of activity properties

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
api_instance = bumbal.PlannerApi(bumbal.ApiClient(configuration))
arguments = bumbal.CheckAvailabilityArguments() # CheckAvailabilityArguments | Request Arguments

try:
    # check availability in planning for a certain set of activity properties
    api_response = api_instance.check_availability(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlannerApi->check_availability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**CheckAvailabilityArguments**](CheckAvailabilityArguments.md)| Request Arguments | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_availability_result**
> ApiResponse check_availability_result(arguments)

Fetch current result for a checkAvailability Request. This could be done, in progress or cancelled.

Fetch current result for a checkAvailability Request. This could be done, in progress or cancelled.

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
api_instance = bumbal.PlannerApi(bumbal.ApiClient(configuration))
arguments = bumbal.CheckAvailabilityArguments() # CheckAvailabilityArguments | Request Arguments

try:
    # Fetch current result for a checkAvailability Request. This could be done, in progress or cancelled.
    api_response = api_instance.check_availability_result(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlannerApi->check_availability_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**CheckAvailabilityArguments**](CheckAvailabilityArguments.md)| Request Arguments | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **planner_add_activities_to_route**
> AddActivitiesToRouteResponse planner_add_activities_to_route(arguments)

Add Activities to Route

Add Activities to Route

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
api_instance = bumbal.PlannerApi(bumbal.ApiClient(configuration))
arguments = bumbal.AddActivitiesToRouteArguments() # AddActivitiesToRouteArguments | Request Arguments

try:
    # Add Activities to Route
    api_response = api_instance.planner_add_activities_to_route(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlannerApi->planner_add_activities_to_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**AddActivitiesToRouteArguments**](AddActivitiesToRouteArguments.md)| Request Arguments | 

### Return type

[**AddActivitiesToRouteResponse**](AddActivitiesToRouteResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_activities_from_route**
> ApiResponse remove_activities_from_route(arguments)

Remove Activities From Route

Remove Activities From Route

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
api_instance = bumbal.PlannerApi(bumbal.ApiClient(configuration))
arguments = bumbal.RemoveActivitiesFromRouteArguments() # RemoveActivitiesFromRouteArguments | Request Arguments

try:
    # Remove Activities From Route
    api_response = api_instance.remove_activities_from_route(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlannerApi->remove_activities_from_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**RemoveActivitiesFromRouteArguments**](RemoveActivitiesFromRouteArguments.md)| Request Arguments | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

