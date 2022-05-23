# bumbal.PauseApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pause**](PauseApi.md#create_pause) | **POST** /pause | Add a new Pause
[**delete_pause**](PauseApi.md#delete_pause) | **DELETE** /pause/{pauseId} | Delete a Pause
[**retrieve_list_pause**](PauseApi.md#retrieve_list_pause) | **PUT** /pause | Retrieve List of Pauses
[**retrieve_pause**](PauseApi.md#retrieve_pause) | **GET** /pause/{pauseId} | Retrieve a Pause
[**set_pause**](PauseApi.md#set_pause) | **POST** /pause/set | Set (create or update) a Pause
[**update_pause**](PauseApi.md#update_pause) | **PUT** /pause/{pauseId} | Update a Pause


# **create_pause**
> ApiResponse create_pause(body=body)

Add a new Pause

Add a new Pause

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
api_instance = bumbal.PauseApi(bumbal.ApiClient(configuration))
body = bumbal.PauseModel() # PauseModel | Pause object that needs to be created (optional)

try:
    # Add a new Pause
    api_response = api_instance.create_pause(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PauseApi->create_pause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PauseModel**](PauseModel.md)| Pause object that needs to be created | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pause**
> ApiResponse delete_pause(pause_id)

Delete a Pause

Delete a Pause

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
api_instance = bumbal.PauseApi(bumbal.ApiClient(configuration))
pause_id = 789 # int | ID of pause to delete

try:
    # Delete a Pause
    api_response = api_instance.delete_pause(pause_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PauseApi->delete_pause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pause_id** | **int**| ID of pause to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_pause**
> PauseListResponse retrieve_list_pause(arguments)

Retrieve List of Pauses

Retrieve List of Pauses

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
api_instance = bumbal.PauseApi(bumbal.ApiClient(configuration))
arguments = bumbal.PauseRetrieveListArguments() # PauseRetrieveListArguments | Pause RetrieveList Arguments

try:
    # Retrieve List of Pauses
    api_response = api_instance.retrieve_list_pause(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PauseApi->retrieve_list_pause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**PauseRetrieveListArguments**](PauseRetrieveListArguments.md)| Pause RetrieveList Arguments | 

### Return type

[**PauseListResponse**](PauseListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_pause**
> PauseModel retrieve_pause(pause_id)

Retrieve a Pause

Retrieve an Pause

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
api_instance = bumbal.PauseApi(bumbal.ApiClient(configuration))
pause_id = 789 # int | ID of pause to retrieve

try:
    # Retrieve a Pause
    api_response = api_instance.retrieve_pause(pause_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PauseApi->retrieve_pause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pause_id** | **int**| ID of pause to retrieve | 

### Return type

[**PauseModel**](PauseModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pause**
> ApiResponse set_pause(body=body)

Set (create or update) a Pause

Set (create or update) a Pause. If id or links are set in the data, and a corresponding pause is found in Bumbal, an update will be performed.

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
api_instance = bumbal.PauseApi(bumbal.ApiClient(configuration))
body = bumbal.PauseModel() # PauseModel | Pause object (optional)

try:
    # Set (create or update) a Pause
    api_response = api_instance.set_pause(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PauseApi->set_pause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PauseModel**](PauseModel.md)| Pause object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pause**
> ApiResponse update_pause(pause_id)

Update a Pause

Update an Pause

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
api_instance = bumbal.PauseApi(bumbal.ApiClient(configuration))
pause_id = 789 # int | ID of pause to update

try:
    # Update a Pause
    api_response = api_instance.update_pause(pause_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PauseApi->update_pause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pause_id** | **int**| ID of pause to update | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

