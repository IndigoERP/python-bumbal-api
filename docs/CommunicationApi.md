# bumbal.CommunicationApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_activity_communication**](CommunicationApi.md#retrieve_activity_communication) | **POST** /communication/retrieve-activity | Retrieve Activity
[**trigger_message_communication**](CommunicationApi.md#trigger_message_communication) | **POST** /communication/trigger-message | Trigger Message to Communication


# **retrieve_activity_communication**
> ApiResponse retrieve_activity_communication(activity_id)

Retrieve Activity

Retrieve Activity from Communication

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
api_instance = bumbal.CommunicationApi(bumbal.ApiClient(configuration))
activity_id = 56 # int | ActivityId

try:
    # Retrieve Activity
    api_response = api_instance.retrieve_activity_communication(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationApi->retrieve_activity_communication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| ActivityId | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_message_communication**
> ApiResponse trigger_message_communication(activity_id, message_type, check_preference)

Trigger Message to Communication

Trigger Message to Communication

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
api_instance = bumbal.CommunicationApi(bumbal.ApiClient(configuration))
activity_id = 56 # int | ActivityId
message_type = 'message_type_example' # str | MessageType
check_preference = true # bool | checkPreference

try:
    # Trigger Message to Communication
    api_response = api_instance.trigger_message_communication(activity_id, message_type, check_preference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationApi->trigger_message_communication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| ActivityId | 
 **message_type** | **str**| MessageType | 
 **check_preference** | **bool**| checkPreference | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

