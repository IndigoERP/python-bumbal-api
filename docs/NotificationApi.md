# bumbal.NotificationApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification**](NotificationApi.md#create_notification) | **POST** /notification | Add a new Notification
[**delete_notification**](NotificationApi.md#delete_notification) | **DELETE** /notification/{notificationId} | Delete an Notification entry
[**retrieve_list_notification**](NotificationApi.md#retrieve_list_notification) | **PUT** /notification | Retrieve List of Notification
[**retrieve_notification**](NotificationApi.md#retrieve_notification) | **GET** /notification/{notificationId} | Retrieve a Notification
[**set_notification**](NotificationApi.md#set_notification) | **POST** /notification/set | Set (create or update) a notification
[**update_notification**](NotificationApi.md#update_notification) | **PUT** /notification/{notificationId} | Update a specific Notification object


# **create_notification**
> ApiResponse20 create_notification(body=body)

Add a new Notification

Add a new Notification

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
api_instance = bumbal.NotificationApi(bumbal.ApiClient(configuration))
body = bumbal.NotificationModel() # NotificationModel | Notification object that needs to be created (optional)

try:
    # Add a new Notification
    api_response = api_instance.create_notification(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->create_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationModel**](NotificationModel.md)| Notification object that needs to be created | [optional] 

### Return type

[**ApiResponse20**](ApiResponse20.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification**
> ApiResponse17 delete_notification(notification_id)

Delete an Notification entry

Delete an Notification entry

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
api_instance = bumbal.NotificationApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of Notification to delete

try:
    # Delete an Notification entry
    api_response = api_instance.delete_notification(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->delete_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of Notification to delete | 

### Return type

[**ApiResponse17**](ApiResponse17.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_notification**
> NotificationListResponse retrieve_list_notification(arguments)

Retrieve List of Notification

Retrieve List of Notification

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
api_instance = bumbal.NotificationApi(bumbal.ApiClient(configuration))
arguments = bumbal.NotificationRetrieveListArguments() # NotificationRetrieveListArguments | Notification RetrieveList Arguments

try:
    # Retrieve List of Notification
    api_response = api_instance.retrieve_list_notification(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->retrieve_list_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**NotificationRetrieveListArguments**](NotificationRetrieveListArguments.md)| Notification RetrieveList Arguments | 

### Return type

[**NotificationListResponse**](NotificationListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_notification**
> NotificationModel retrieve_notification(notification_id, include_category_type_name=include_category_type_name, include_record_info=include_record_info)

Retrieve a Notification

Retrieve an Notification

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
api_instance = bumbal.NotificationApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of Notification to retrieve
include_category_type_name = false # bool | Show the name of the category type (optional) (default to false)
include_record_info = false # bool | Show the record info (optional) (default to false)

try:
    # Retrieve a Notification
    api_response = api_instance.retrieve_notification(notification_id, include_category_type_name=include_category_type_name, include_record_info=include_record_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->retrieve_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of Notification to retrieve | 
 **include_category_type_name** | **bool**| Show the name of the category type | [optional] [default to false]
 **include_record_info** | **bool**| Show the record info | [optional] [default to false]

### Return type

[**NotificationModel**](NotificationModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_notification**
> ApiResponse set_notification(body=body)

Set (create or update) a notification

Set (create or update) a notification. If id or links are set in the data, and a corresponding notification is found in Bumbal, an update will be performed.

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
api_instance = bumbal.NotificationApi(bumbal.ApiClient(configuration))
body = bumbal.NotificationModel() # NotificationModel | Notification object (optional)

try:
    # Set (create or update) a notification
    api_response = api_instance.set_notification(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->set_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationModel**](NotificationModel.md)| Notification object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification**
> ApiResponse16 update_notification(notification_id, body=body)

Update a specific Notification object

Update a specific Notification object

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
api_instance = bumbal.NotificationApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of the Notification object to update
body = bumbal.NotificationModel() # NotificationModel | Notification object that needs to be updated (optional)

try:
    # Update a specific Notification object
    api_response = api_instance.update_notification(notification_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationApi->update_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of the Notification object to update | 
 **body** | [**NotificationModel**](NotificationModel.md)| Notification object that needs to be updated | [optional] 

### Return type

[**ApiResponse16**](ApiResponse16.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

