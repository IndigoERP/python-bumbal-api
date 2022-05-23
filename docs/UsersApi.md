# bumbal.UsersApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_credentials_user**](UsersApi.md#check_credentials_user) | **GET** /users/check-credentials | Checks the credentials of a User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{userId} | Delete a user
[**retrieve_list_user_notification**](UsersApi.md#retrieve_list_user_notification) | **PUT** /users/notification | Retrieve List of UserNotification
[**retrieve_list_users**](UsersApi.md#retrieve_list_users) | **PUT** /users | Retrieve List of Users
[**retrieve_users**](UsersApi.md#retrieve_users) | **GET** /users/{usersId} | Retrieve a Users
[**set_user**](UsersApi.md#set_user) | **POST** /users/set | Set (create or update) a User
[**set_user_notification**](UsersApi.md#set_user_notification) | **POST** /users/notification | Create a new UserNotification or update an existing one
[**update_users**](UsersApi.md#update_users) | **PUT** /users/{usersId} | Update a Users


# **check_credentials_user**
> UsersModel check_credentials_user(email, password)

Checks the credentials of a User

Checks the credentials of a User

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
api_instance = bumbal.UsersApi(bumbal.ApiClient(configuration))
email = 'email_example' # str | User Email
password = 'password_example' # str | User Password

try:
    # Checks the credentials of a User
    api_response = api_instance.check_credentials_user(email, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->check_credentials_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| User Email | 
 **password** | **str**| User Password | 

### Return type

[**UsersModel**](UsersModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> ApiResponse delete_user(user_id)

Delete a user

Delete a user

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
api_instance = bumbal.UsersApi(bumbal.ApiClient(configuration))
user_id = 789 # int | ID of user to delete

try:
    # Delete a user
    api_response = api_instance.delete_user(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of user to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_user_notification**
> UserNotificationListResponse retrieve_list_user_notification(arguments)

Retrieve List of UserNotification

Retrieve List of UserNotification

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
api_instance = bumbal.UsersApi(bumbal.ApiClient(configuration))
arguments = bumbal.UserNotificationRetrieveListArguments() # UserNotificationRetrieveListArguments | UserNotification RetrieveList Arguments

try:
    # Retrieve List of UserNotification
    api_response = api_instance.retrieve_list_user_notification(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->retrieve_list_user_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**UserNotificationRetrieveListArguments**](UserNotificationRetrieveListArguments.md)| UserNotification RetrieveList Arguments | 

### Return type

[**UserNotificationListResponse**](UserNotificationListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_users**
> UsersListResponse retrieve_list_users(arguments)

Retrieve List of Users

Retrieve List of Users

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
api_instance = bumbal.UsersApi(bumbal.ApiClient(configuration))
arguments = bumbal.UsersRetrieveListArguments() # UsersRetrieveListArguments | Users RetrieveList Arguments

try:
    # Retrieve List of Users
    api_response = api_instance.retrieve_list_users(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->retrieve_list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**UsersRetrieveListArguments**](UsersRetrieveListArguments.md)| Users RetrieveList Arguments | 

### Return type

[**UsersListResponse**](UsersListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_users**
> UsersModel retrieve_users(users_id)

Retrieve a Users

Retrieve a Users

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
api_instance = bumbal.UsersApi(bumbal.ApiClient(configuration))
users_id = 789 # int | ID of users to retrieve

try:
    # Retrieve a Users
    api_response = api_instance.retrieve_users(users_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->retrieve_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_id** | **int**| ID of users to retrieve | 

### Return type

[**UsersModel**](UsersModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user**
> ApiResponse set_user(body=body)

Set (create or update) a User

Set (create or update) a User. If id or links are set in the data, and a corresponding users is found in Bumbal, an update will be performed.

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
api_instance = bumbal.UsersApi(bumbal.ApiClient(configuration))
body = bumbal.UsersModel() # UsersModel | User object (optional)

try:
    # Set (create or update) a User
    api_response = api_instance.set_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->set_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersModel**](UsersModel.md)| User object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_notification**
> ApiResponse56 set_user_notification(body=body)

Create a new UserNotification or update an existing one

Set (create or update) a user notification. If id or links are set in the data, and a corresponding user notification is found in Bumbal, an update will be performed.

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
api_instance = bumbal.UsersApi(bumbal.ApiClient(configuration))
body = bumbal.UserNotificationModel() # UserNotificationModel | UserNotification object that needs to be set (optional)

try:
    # Create a new UserNotification or update an existing one
    api_response = api_instance.set_user_notification(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->set_user_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserNotificationModel**](UserNotificationModel.md)| UserNotification object that needs to be set | [optional] 

### Return type

[**ApiResponse56**](ApiResponse56.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_users**
> ApiResponse update_users(users_id)

Update a Users

Update a Setting

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
api_instance = bumbal.UsersApi(bumbal.ApiClient(configuration))
users_id = 789 # int | ID of users to update

try:
    # Update a Users
    api_response = api_instance.update_users(users_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_id** | **int**| ID of users to update | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

