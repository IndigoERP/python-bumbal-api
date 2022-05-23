# bumbal.PortalCommunicationApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_activity_by_id_communication**](PortalCommunicationApi.md#retrieve_activity_by_id_communication) | **GET** /portal-communication/retrieve-activity-by-id/{activityId} | Retrieve an activity by ID
[**trigger_message_communication_by_message_type**](PortalCommunicationApi.md#trigger_message_communication_by_message_type) | **POST** /portal-communication/trigger-message-by-message-type | Trigger Message to Communication by Message Type


# **retrieve_activity_by_id_communication**
> ApiResponse retrieve_activity_by_id_communication(activity_id)

Retrieve an activity by ID

Retrieve an activity by ID

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
api_instance = bumbal.PortalCommunicationApi(bumbal.ApiClient(configuration))
activity_id = 789 # int | ID of activity to retrieve

try:
    # Retrieve an activity by ID
    api_response = api_instance.retrieve_activity_by_id_communication(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalCommunicationApi->retrieve_activity_by_id_communication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| ID of activity to retrieve | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_message_communication_by_message_type**
> ApiResponse trigger_message_communication_by_message_type(body=body)

Trigger Message to Communication by Message Type

Trigger Message to Communication by Message Type

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
api_instance = bumbal.PortalCommunicationApi(bumbal.ApiClient(configuration))
body = bumbal.CommunicationTriggerMessageModel() # CommunicationTriggerMessageModel | communication trigger message object (optional)

try:
    # Trigger Message to Communication by Message Type
    api_response = api_instance.trigger_message_communication_by_message_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalCommunicationApi->trigger_message_communication_by_message_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommunicationTriggerMessageModel**](CommunicationTriggerMessageModel.md)| communication trigger message object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, multipart/form-data
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

