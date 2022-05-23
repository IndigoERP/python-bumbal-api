# bumbal.NotificationCategoryApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_category**](NotificationCategoryApi.md#create_notification_category) | **POST** /notification-category | Add a new NotificationCategory
[**delete_notification_category**](NotificationCategoryApi.md#delete_notification_category) | **DELETE** /notification-category/{notification-categoryId} | Delete an NotificationCategory entry
[**retrieve_list_notification_category**](NotificationCategoryApi.md#retrieve_list_notification_category) | **PUT** /notification-category | Retrieve List of NotificationCategory
[**retrieve_notification_category**](NotificationCategoryApi.md#retrieve_notification_category) | **GET** /notification-category/{notification-categoryId} | Retrieve a NotificationCategory
[**set_notification_category**](NotificationCategoryApi.md#set_notification_category) | **POST** /notification-category/set | Create a new NotificationCategory or update an existing one
[**update_notification_category**](NotificationCategoryApi.md#update_notification_category) | **PUT** /notification-category/{notification-categoryId} | Update a specific NotificationCategory object


# **create_notification_category**
> ApiResponse11 create_notification_category(body=body)

Add a new NotificationCategory

Add a new NotificationCategory

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
api_instance = bumbal.NotificationCategoryApi(bumbal.ApiClient(configuration))
body = bumbal.NotificationCategoryModel() # NotificationCategoryModel | NotificationCategory object that needs to be created (optional)

try:
    # Add a new NotificationCategory
    api_response = api_instance.create_notification_category(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationCategoryApi->create_notification_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationCategoryModel**](NotificationCategoryModel.md)| NotificationCategory object that needs to be created | [optional] 

### Return type

[**ApiResponse11**](ApiResponse11.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notification_category**
> ApiResponse9 delete_notification_category(notification_category_id)

Delete an NotificationCategory entry

Delete an NotificationCategory entry

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
api_instance = bumbal.NotificationCategoryApi(bumbal.ApiClient(configuration))
notification_category_id = 789 # int | ID of NotificationCategory to delete

try:
    # Delete an NotificationCategory entry
    api_response = api_instance.delete_notification_category(notification_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationCategoryApi->delete_notification_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_category_id** | **int**| ID of NotificationCategory to delete | 

### Return type

[**ApiResponse9**](ApiResponse9.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_notification_category**
> NotificationCategoryListResponse retrieve_list_notification_category(arguments)

Retrieve List of NotificationCategory

Retrieve List of NotificationCategory

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
api_instance = bumbal.NotificationCategoryApi(bumbal.ApiClient(configuration))
arguments = bumbal.NotificationCategoryRetrieveListArguments() # NotificationCategoryRetrieveListArguments | NotificationCategory RetrieveList Arguments

try:
    # Retrieve List of NotificationCategory
    api_response = api_instance.retrieve_list_notification_category(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationCategoryApi->retrieve_list_notification_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**NotificationCategoryRetrieveListArguments**](NotificationCategoryRetrieveListArguments.md)| NotificationCategory RetrieveList Arguments | 

### Return type

[**NotificationCategoryListResponse**](NotificationCategoryListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_notification_category**
> NotificationCategoryModel retrieve_notification_category(notification_category_id, include_object_type_name=include_object_type_name, include_record_info=include_record_info)

Retrieve a NotificationCategory

Retrieve an NotificationCategory

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
api_instance = bumbal.NotificationCategoryApi(bumbal.ApiClient(configuration))
notification_category_id = 789 # int | ID of NotificationCategory to retrieve
include_object_type_name = false # bool | Show the name of the object type (optional) (default to false)
include_record_info = false # bool | Show the record info (optional) (default to false)

try:
    # Retrieve a NotificationCategory
    api_response = api_instance.retrieve_notification_category(notification_category_id, include_object_type_name=include_object_type_name, include_record_info=include_record_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationCategoryApi->retrieve_notification_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_category_id** | **int**| ID of NotificationCategory to retrieve | 
 **include_object_type_name** | **bool**| Show the name of the object type | [optional] [default to false]
 **include_record_info** | **bool**| Show the record info | [optional] [default to false]

### Return type

[**NotificationCategoryModel**](NotificationCategoryModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_notification_category**
> ApiResponse12 set_notification_category(body=body)

Create a new NotificationCategory or update an existing one

Set (create or update) a notification category. If id or links are set in the data, and a corresponding notification category is found in Bumbal, an update will be performed.

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
api_instance = bumbal.NotificationCategoryApi(bumbal.ApiClient(configuration))
body = bumbal.NotificationCategoryModel() # NotificationCategoryModel | NotificationCategory object that needs to be set (optional)

try:
    # Create a new NotificationCategory or update an existing one
    api_response = api_instance.set_notification_category(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationCategoryApi->set_notification_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationCategoryModel**](NotificationCategoryModel.md)| NotificationCategory object that needs to be set | [optional] 

### Return type

[**ApiResponse12**](ApiResponse12.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_category**
> ApiResponse8 update_notification_category(notification_category_id, body=body)

Update a specific NotificationCategory object

Update a specific NotificationCategory object

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
api_instance = bumbal.NotificationCategoryApi(bumbal.ApiClient(configuration))
notification_category_id = 789 # int | ID of the NotificationCategory object to update
body = bumbal.NotificationCategoryModel() # NotificationCategoryModel | NotificationCategory object that needs to be updated (optional)

try:
    # Update a specific NotificationCategory object
    api_response = api_instance.update_notification_category(notification_category_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationCategoryApi->update_notification_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_category_id** | **int**| ID of the NotificationCategory object to update | 
 **body** | [**NotificationCategoryModel**](NotificationCategoryModel.md)| NotificationCategory object that needs to be updated | [optional] 

### Return type

[**ApiResponse8**](ApiResponse8.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

