# bumbal.ActivityApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_activity**](ActivityApi.md#delete_activity) | **DELETE** /activity/{activityId} | Delete an activity
[**lock_activity**](ActivityApi.md#lock_activity) | **POST** /activity/lock | Lock activities which satisfy set filters
[**lock_activity_on_route**](ActivityApi.md#lock_activity_on_route) | **POST** /activity/lock-on-route | Lock activities on route which satisfy set filters
[**lock_activity_on_route_and_time**](ActivityApi.md#lock_activity_on_route_and_time) | **POST** /activity/lock-on-route-and-time | Lock activities on route and time which satisfy set filters
[**retrieve_activity**](ActivityApi.md#retrieve_activity) | **GET** /activity/{activityId} | Find activity by ID
[**retrieve_list_activity**](ActivityApi.md#retrieve_list_activity) | **PUT** /activity | Retrieve List of Activities
[**set_activity**](ActivityApi.md#set_activity) | **POST** /activity/set | Set (create or update) an Activity
[**unlock_activity**](ActivityApi.md#unlock_activity) | **POST** /activity/unlock | Unlock activities which satisfy set filters
[**unsuccessful**](ActivityApi.md#unsuccessful) | **POST** /activity/unsuccessful | Report an unsuccessful activity
[**update_activity**](ActivityApi.md#update_activity) | **PUT** /activity/{activityId} | Update a activity


# **delete_activity**
> ApiResponse delete_activity(activity_id)

Delete an activity

Delete an activity

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
api_instance = bumbal.ActivityApi(bumbal.ApiClient(configuration))
activity_id = 789 # int | ID of the activity to delete

try:
    # Delete an activity
    api_response = api_instance.delete_activity(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->delete_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| ID of the activity to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_activity**
> ApiResponse lock_activity(filters)

Lock activities which satisfy set filters

Lock activities which satisfy set filters

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
api_instance = bumbal.ActivityApi(bumbal.ApiClient(configuration))
filters = bumbal.ActivityFiltersModel() # ActivityFiltersModel | Request Filters

try:
    # Lock activities which satisfy set filters
    api_response = api_instance.lock_activity(filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->lock_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**ActivityFiltersModel**](ActivityFiltersModel.md)| Request Filters | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_activity_on_route**
> ApiResponse lock_activity_on_route(filters)

Lock activities on route which satisfy set filters

Lock activities on route which satisfy set filters

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
api_instance = bumbal.ActivityApi(bumbal.ApiClient(configuration))
filters = bumbal.ActivityFiltersModel() # ActivityFiltersModel | Request Filters

try:
    # Lock activities on route which satisfy set filters
    api_response = api_instance.lock_activity_on_route(filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->lock_activity_on_route: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**ActivityFiltersModel**](ActivityFiltersModel.md)| Request Filters | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_activity_on_route_and_time**
> ApiResponse lock_activity_on_route_and_time(filters)

Lock activities on route and time which satisfy set filters

Lock activities on route and time which satisfy set filters

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
api_instance = bumbal.ActivityApi(bumbal.ApiClient(configuration))
filters = bumbal.ActivityFiltersModel() # ActivityFiltersModel | Request Filters

try:
    # Lock activities on route and time which satisfy set filters
    api_response = api_instance.lock_activity_on_route_and_time(filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->lock_activity_on_route_and_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**ActivityFiltersModel**](ActivityFiltersModel.md)| Request Filters | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_activity**
> ActivityModel retrieve_activity(activity_id, include_activity_status, include_activity_type_name, include_activity_meta_data, include_address_object, include_time_slots, include_route_info, include_route, include_package_lines, include_package_lines_info, include_driver_info, include_communication, include_communication_object, include_activity_links, include_activity_files, include_activity_files_meta_data, include_assignment_nr, include_assignment, include_activity_tags, include_tag_type_name, include_activity_record_info, include_activity_notes, include_activity_note_tags, include_depot_address_object, include_capacity_object, include_zones, include_brand, include_brand_colours, include_brand_files, include_relations)

Find activity by ID

Returns a single activity

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
api_instance = bumbal.ActivityApi(bumbal.ApiClient(configuration))
activity_id = 789 # int | ID of activity to return
include_activity_status = true # bool | Show the text value of the status (default to true)
include_activity_type_name = true # bool | Show the text value of the activity type (default to true)
include_activity_meta_data = true # bool | Include meta data connected to this Activity (default to true)
include_address_object = true # bool | Include address data (default to true)
include_time_slots = true # bool | Include TimeSlots (default to true)
include_route_info = true # bool | Include route data (default to true)
include_route = true # bool | Include Route (default to true)
include_package_lines = true # bool | Include package lines (default to true)
include_package_lines_info = true # bool | Include PackageLines (default to true)
include_driver_info = true # bool | Include driver data (default to true)
include_communication = true # bool | Include Communication Settings (default to true)
include_communication_object = true # bool | Include Communication Object (default to true)
include_activity_links = true # bool | Include Link Data (default to true)
include_activity_files = true # bool | Include files (default to true)
include_activity_files_meta_data = true # bool | Include files meta data (default to true)
include_assignment_nr = true # bool | Include Assignment Nr (default to true)
include_assignment = true # bool | Include Assignment (default to true)
include_activity_tags = true # bool | Include Activity Tags (default to true)
include_tag_type_name = true # bool | Include Activity Tag type names (default to true)
include_activity_record_info = true # bool | Include Activity Info (default to true)
include_activity_notes = true # bool | Include Activity Notes (default to true)
include_activity_note_tags = true # bool | Include Activity Note Tags (default to true)
include_depot_address_object = true # bool | Include Depot Address Object (default to true)
include_capacity_object = true # bool | Include Capacity Object (default to true)
include_zones = true # bool | Include Zones (default to true)
include_brand = true # bool | Include brand (default to true)
include_brand_colours = true # bool | Include brand colours (default to true)
include_brand_files = true # bool | Include brand files (default to true)
include_relations = true # bool | Include activity_before and activity_after (default to true)

try:
    # Find activity by ID
    api_response = api_instance.retrieve_activity(activity_id, include_activity_status, include_activity_type_name, include_activity_meta_data, include_address_object, include_time_slots, include_route_info, include_route, include_package_lines, include_package_lines_info, include_driver_info, include_communication, include_communication_object, include_activity_links, include_activity_files, include_activity_files_meta_data, include_assignment_nr, include_assignment, include_activity_tags, include_tag_type_name, include_activity_record_info, include_activity_notes, include_activity_note_tags, include_depot_address_object, include_capacity_object, include_zones, include_brand, include_brand_colours, include_brand_files, include_relations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->retrieve_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| ID of activity to return | 
 **include_activity_status** | **bool**| Show the text value of the status | [default to true]
 **include_activity_type_name** | **bool**| Show the text value of the activity type | [default to true]
 **include_activity_meta_data** | **bool**| Include meta data connected to this Activity | [default to true]
 **include_address_object** | **bool**| Include address data | [default to true]
 **include_time_slots** | **bool**| Include TimeSlots | [default to true]
 **include_route_info** | **bool**| Include route data | [default to true]
 **include_route** | **bool**| Include Route | [default to true]
 **include_package_lines** | **bool**| Include package lines | [default to true]
 **include_package_lines_info** | **bool**| Include PackageLines | [default to true]
 **include_driver_info** | **bool**| Include driver data | [default to true]
 **include_communication** | **bool**| Include Communication Settings | [default to true]
 **include_communication_object** | **bool**| Include Communication Object | [default to true]
 **include_activity_links** | **bool**| Include Link Data | [default to true]
 **include_activity_files** | **bool**| Include files | [default to true]
 **include_activity_files_meta_data** | **bool**| Include files meta data | [default to true]
 **include_assignment_nr** | **bool**| Include Assignment Nr | [default to true]
 **include_assignment** | **bool**| Include Assignment | [default to true]
 **include_activity_tags** | **bool**| Include Activity Tags | [default to true]
 **include_tag_type_name** | **bool**| Include Activity Tag type names | [default to true]
 **include_activity_record_info** | **bool**| Include Activity Info | [default to true]
 **include_activity_notes** | **bool**| Include Activity Notes | [default to true]
 **include_activity_note_tags** | **bool**| Include Activity Note Tags | [default to true]
 **include_depot_address_object** | **bool**| Include Depot Address Object | [default to true]
 **include_capacity_object** | **bool**| Include Capacity Object | [default to true]
 **include_zones** | **bool**| Include Zones | [default to true]
 **include_brand** | **bool**| Include brand | [default to true]
 **include_brand_colours** | **bool**| Include brand colours | [default to true]
 **include_brand_files** | **bool**| Include brand files | [default to true]
 **include_relations** | **bool**| Include activity_before and activity_after | [default to true]

### Return type

[**ActivityModel**](ActivityModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_activity**
> ActivityListResponse retrieve_list_activity(arguments)

Retrieve List of Activities

Retrieve List of Activities

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
api_instance = bumbal.ActivityApi(bumbal.ApiClient(configuration))
arguments = bumbal.ActivityRetrieveListArguments() # ActivityRetrieveListArguments | Activity RetrieveList Arguments

try:
    # Retrieve List of Activities
    api_response = api_instance.retrieve_list_activity(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->retrieve_list_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**ActivityRetrieveListArguments**](ActivityRetrieveListArguments.md)| Activity RetrieveList Arguments | 

### Return type

[**ActivityListResponse**](ActivityListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_activity**
> ApiResponse set_activity(body=body)

Set (create or update) an Activity

Set (create or update) an Activity. If id or links are set in the data, and a corresponding activity is found in Bumbal, an update will be performed.

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
api_instance = bumbal.ActivityApi(bumbal.ApiClient(configuration))
body = bumbal.ActivityModel() # ActivityModel | Activity object (optional)

try:
    # Set (create or update) an Activity
    api_response = api_instance.set_activity(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->set_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActivityModel**](ActivityModel.md)| Activity object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_activity**
> ApiResponse unlock_activity(filters)

Unlock activities which satisfy set filters

Unlock activities which satisfy set filters

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
api_instance = bumbal.ActivityApi(bumbal.ApiClient(configuration))
filters = bumbal.ActivityFiltersModel() # ActivityFiltersModel | Request Filters

try:
    # Unlock activities which satisfy set filters
    api_response = api_instance.unlock_activity(filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->unlock_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | [**ActivityFiltersModel**](ActivityFiltersModel.md)| Request Filters | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsuccessful**
> UnsuccessfulResponseModel unsuccessful(arguments)

Report an unsuccessful activity

Report an unsuccessful activity

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
api_instance = bumbal.ActivityApi(bumbal.ApiClient(configuration))
arguments = bumbal.UnsuccessfulModel() # UnsuccessfulModel | Request Arguments

try:
    # Report an unsuccessful activity
    api_response = api_instance.unsuccessful(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->unsuccessful: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**UnsuccessfulModel**](UnsuccessfulModel.md)| Request Arguments | 

### Return type

[**UnsuccessfulResponseModel**](UnsuccessfulResponseModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_activity**
> ApiResponse update_activity(activity_id, body=body)

Update a activity

Update a activity

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
api_instance = bumbal.ActivityApi(bumbal.ApiClient(configuration))
activity_id = 789 # int | ID of activity to update
body = bumbal.ActivityModel() # ActivityModel | Activity object that needs to be updated (optional)

try:
    # Update a activity
    api_response = api_instance.update_activity(activity_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->update_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| ID of activity to update | 
 **body** | [**ActivityModel**](ActivityModel.md)| Activity object that needs to be updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

