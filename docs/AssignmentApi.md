# bumbal.AssignmentApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_assignment**](AssignmentApi.md#delete_assignment) | **DELETE** /assignment/{assignmentId} | Delete an assignment
[**retrieve_assignment**](AssignmentApi.md#retrieve_assignment) | **GET** /assignment/{assignmentId} | Find assignment by ID
[**retrieve_list_assignment**](AssignmentApi.md#retrieve_list_assignment) | **PUT** /assignment | Retrieve List of Assignments
[**set_assignment**](AssignmentApi.md#set_assignment) | **POST** /assignment/set | Set (create or update) an Assignment
[**update_assignment**](AssignmentApi.md#update_assignment) | **PUT** /assignment/{assignmentId} | Update a assignment


# **delete_assignment**
> ApiResponse delete_assignment(assignment_id)

Delete an assignment

Delete an assignment

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
api_instance = bumbal.AssignmentApi(bumbal.ApiClient(configuration))
assignment_id = 789 # int | ID of the assignment to delete

try:
    # Delete an assignment
    api_response = api_instance.delete_assignment(assignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentApi->delete_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**| ID of the assignment to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_assignment**
> AssignmentModel retrieve_assignment(assignment_id, include_activities=include_activities, include_meta_data=include_meta_data, include_links=include_links, include_files=include_files, include_tag_ids=include_tag_ids, include_tag_names=include_tag_names, include_booking_account=include_booking_account, include_record_info=include_record_info, include_record_object=include_record_object)

Find assignment by ID

Returns a single assignment

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
api_instance = bumbal.AssignmentApi(bumbal.ApiClient(configuration))
assignment_id = 789 # int | ID of assignment to return
include_activities = false # bool | Include activities belonging to assignment (optional) (default to false)
include_meta_data = false # bool | Include meta data (optional) (default to false)
include_links = false # bool | Include links (optional) (default to false)
include_files = false # bool | Include files (optional) (default to false)
include_tag_ids = false # bool | Include tag ids (optional) (default to false)
include_tag_names = false # bool | Include tag names (optional) (default to false)
include_booking_account = false # bool | Include booking account (optional) (default to false)
include_record_info = false # bool | Include record info (optional) (default to false)
include_record_object = false # bool | Include record object (optional) (default to false)

try:
    # Find assignment by ID
    api_response = api_instance.retrieve_assignment(assignment_id, include_activities=include_activities, include_meta_data=include_meta_data, include_links=include_links, include_files=include_files, include_tag_ids=include_tag_ids, include_tag_names=include_tag_names, include_booking_account=include_booking_account, include_record_info=include_record_info, include_record_object=include_record_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentApi->retrieve_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**| ID of assignment to return | 
 **include_activities** | **bool**| Include activities belonging to assignment | [optional] [default to false]
 **include_meta_data** | **bool**| Include meta data | [optional] [default to false]
 **include_links** | **bool**| Include links | [optional] [default to false]
 **include_files** | **bool**| Include files | [optional] [default to false]
 **include_tag_ids** | **bool**| Include tag ids | [optional] [default to false]
 **include_tag_names** | **bool**| Include tag names | [optional] [default to false]
 **include_booking_account** | **bool**| Include booking account | [optional] [default to false]
 **include_record_info** | **bool**| Include record info | [optional] [default to false]
 **include_record_object** | **bool**| Include record object | [optional] [default to false]

### Return type

[**AssignmentModel**](AssignmentModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_assignment**
> AssignmentListResponse retrieve_list_assignment(arguments)

Retrieve List of Assignments

Retrieve List of Assignments

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
api_instance = bumbal.AssignmentApi(bumbal.ApiClient(configuration))
arguments = bumbal.AssignmentRetrieveListArguments() # AssignmentRetrieveListArguments | Assignment RetrieveList Arguments

try:
    # Retrieve List of Assignments
    api_response = api_instance.retrieve_list_assignment(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentApi->retrieve_list_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**AssignmentRetrieveListArguments**](AssignmentRetrieveListArguments.md)| Assignment RetrieveList Arguments | 

### Return type

[**AssignmentListResponse**](AssignmentListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_assignment**
> ApiResponse set_assignment(body=body)

Set (create or update) an Assignment

Set (create or update) an Assignment. If id or links are set in the data, and a corresponding assignment is found in Bumbal, an update will be performed.

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
api_instance = bumbal.AssignmentApi(bumbal.ApiClient(configuration))
body = bumbal.AssignmentModel() # AssignmentModel | Assignment object (optional)

try:
    # Set (create or update) an Assignment
    api_response = api_instance.set_assignment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentApi->set_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignmentModel**](AssignmentModel.md)| Assignment object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assignment**
> ApiResponse update_assignment(assignment_id, body=body)

Update a assignment

Update a assignment

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
api_instance = bumbal.AssignmentApi(bumbal.ApiClient(configuration))
assignment_id = 789 # int | ID of assignment to update
body = bumbal.AssignmentModel() # AssignmentModel | Assignment object that needs to be updated (optional)

try:
    # Update a assignment
    api_response = api_instance.update_assignment(assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentApi->update_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**| ID of assignment to update | 
 **body** | [**AssignmentModel**](AssignmentModel.md)| Assignment object that needs to be updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

