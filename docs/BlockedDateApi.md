# bumbal.BlockedDateApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_blocked_date**](BlockedDateApi.md#delete_blocked_date) | **DELETE** /blocked-date/{blockedDateId} | Delete a blocked date
[**retrieve_list_blocked_date**](BlockedDateApi.md#retrieve_list_blocked_date) | **PUT** /blocked-date | Retrieve List of blocked dates
[**set_blocked_date**](BlockedDateApi.md#set_blocked_date) | **POST** /blocked-date/set | Set (create or update) a blocked date


# **delete_blocked_date**
> ApiResponse delete_blocked_date(blocked_date_id)

Delete a blocked date

Delete a blocked date

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
api_instance = bumbal.BlockedDateApi(bumbal.ApiClient(configuration))
blocked_date_id = 789 # int | ID of blocked date to delete

try:
    # Delete a blocked date
    api_response = api_instance.delete_blocked_date(blocked_date_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockedDateApi->delete_blocked_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blocked_date_id** | **int**| ID of blocked date to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_blocked_date**
> BlockedDateListResponse retrieve_list_blocked_date(arguments)

Retrieve List of blocked dates

Retrieve List of blocked dates

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
api_instance = bumbal.BlockedDateApi(bumbal.ApiClient(configuration))
arguments = bumbal.BlockedDateRetrieveListArguments() # BlockedDateRetrieveListArguments | Blocked date RetrieveList Arguments

try:
    # Retrieve List of blocked dates
    api_response = api_instance.retrieve_list_blocked_date(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockedDateApi->retrieve_list_blocked_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**BlockedDateRetrieveListArguments**](BlockedDateRetrieveListArguments.md)| Blocked date RetrieveList Arguments | 

### Return type

[**BlockedDateListResponse**](BlockedDateListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_blocked_date**
> ApiResponse set_blocked_date(body=body)

Set (create or update) a blocked date

Set (create or update) a blocked date.

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
api_instance = bumbal.BlockedDateApi(bumbal.ApiClient(configuration))
body = bumbal.BlockedDateModel() # BlockedDateModel | Blocked date object object (optional)

try:
    # Set (create or update) a blocked date
    api_response = api_instance.set_blocked_date(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlockedDateApi->set_blocked_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BlockedDateModel**](BlockedDateModel.md)| Blocked date object object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

