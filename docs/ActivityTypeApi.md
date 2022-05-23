# bumbal.ActivityTypeApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_activity_type**](ActivityTypeApi.md#retrieve_activity_type) | **GET** /activity-type/{activityTypeId} | Find ActivityType by ID
[**retrieve_list_activity_type**](ActivityTypeApi.md#retrieve_list_activity_type) | **PUT** /activity-type | Retrieve List of ActivityTypes


# **retrieve_activity_type**
> ActivityTypeModel retrieve_activity_type(activity_type_id)

Find ActivityType by ID

Returns a single ActivityType

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
api_instance = bumbal.ActivityTypeApi(bumbal.ApiClient(configuration))
activity_type_id = 789 # int | ID of ActivityType to return

try:
    # Find ActivityType by ID
    api_response = api_instance.retrieve_activity_type(activity_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityTypeApi->retrieve_activity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_type_id** | **int**| ID of ActivityType to return | 

### Return type

[**ActivityTypeModel**](ActivityTypeModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_activity_type**
> ActivityTypeListResponse retrieve_list_activity_type(arguments)

Retrieve List of ActivityTypes

Retrieve List of ActivityTypes

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
api_instance = bumbal.ActivityTypeApi(bumbal.ApiClient(configuration))
arguments = bumbal.ActivityTypeRetrieveListArguments() # ActivityTypeRetrieveListArguments | ActivityType RetrieveList Arguments

try:
    # Retrieve List of ActivityTypes
    api_response = api_instance.retrieve_list_activity_type(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityTypeApi->retrieve_list_activity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**ActivityTypeRetrieveListArguments**](ActivityTypeRetrieveListArguments.md)| ActivityType RetrieveList Arguments | 

### Return type

[**ActivityTypeListResponse**](ActivityTypeListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

