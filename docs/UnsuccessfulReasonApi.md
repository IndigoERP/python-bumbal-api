# bumbal.UnsuccessfulReasonApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_unsuccessful_reason**](UnsuccessfulReasonApi.md#create_unsuccessful_reason) | **POST** /unsuccessful-reason | Add a new UnsuccessfulReason
[**delete_unsuccessful_reason**](UnsuccessfulReasonApi.md#delete_unsuccessful_reason) | **DELETE** /unsuccessful-reason/{unsuccessful-reasonId} | Delete a UnsuccessfulReason entry
[**retrieve_list_unsuccessful_reason**](UnsuccessfulReasonApi.md#retrieve_list_unsuccessful_reason) | **PUT** /unsuccessful-reason | Retrieve List of UnsuccessfulReason
[**retrieve_unsuccessful_reason**](UnsuccessfulReasonApi.md#retrieve_unsuccessful_reason) | **GET** /unsuccessful-reason/{unsuccessful-reasonId} | Retrieve a UnsuccessfulReason
[**update_unsuccessful_reason**](UnsuccessfulReasonApi.md#update_unsuccessful_reason) | **PUT** /unsuccessful-reason/{unsuccessful-reasonId} | Update a specific UnsuccessfulReason object


# **create_unsuccessful_reason**
> ApiResponse55 create_unsuccessful_reason(body=body)

Add a new UnsuccessfulReason

Add a new UnsuccessfulReason

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
api_instance = bumbal.UnsuccessfulReasonApi(bumbal.ApiClient(configuration))
body = bumbal.UnsuccessfulReasonModel() # UnsuccessfulReasonModel | UnsuccessfulReason object that needs to be created (optional)

try:
    # Add a new UnsuccessfulReason
    api_response = api_instance.create_unsuccessful_reason(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnsuccessfulReasonApi->create_unsuccessful_reason: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnsuccessfulReasonModel**](UnsuccessfulReasonModel.md)| UnsuccessfulReason object that needs to be created | [optional] 

### Return type

[**ApiResponse55**](ApiResponse55.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_unsuccessful_reason**
> ApiResponse53 delete_unsuccessful_reason(unsuccessful_reason_id)

Delete a UnsuccessfulReason entry

Delete a Metadata entry

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
api_instance = bumbal.UnsuccessfulReasonApi(bumbal.ApiClient(configuration))
unsuccessful_reason_id = 789 # int | ID of UnsuccessfulReason to delete

try:
    # Delete a UnsuccessfulReason entry
    api_response = api_instance.delete_unsuccessful_reason(unsuccessful_reason_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnsuccessfulReasonApi->delete_unsuccessful_reason: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unsuccessful_reason_id** | **int**| ID of UnsuccessfulReason to delete | 

### Return type

[**ApiResponse53**](ApiResponse53.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_unsuccessful_reason**
> UnsuccessfulReasonListResponse retrieve_list_unsuccessful_reason(arguments)

Retrieve List of UnsuccessfulReason

Retrieve List of UnsuccessfulReason

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
api_instance = bumbal.UnsuccessfulReasonApi(bumbal.ApiClient(configuration))
arguments = bumbal.UnsuccessfulReasonRetrieveListArguments() # UnsuccessfulReasonRetrieveListArguments | UnsuccessfulReason RetrieveList Arguments

try:
    # Retrieve List of UnsuccessfulReason
    api_response = api_instance.retrieve_list_unsuccessful_reason(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnsuccessfulReasonApi->retrieve_list_unsuccessful_reason: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**UnsuccessfulReasonRetrieveListArguments**](UnsuccessfulReasonRetrieveListArguments.md)| UnsuccessfulReason RetrieveList Arguments | 

### Return type

[**UnsuccessfulReasonListResponse**](UnsuccessfulReasonListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_unsuccessful_reason**
> UnsuccessfulReasonModel retrieve_unsuccessful_reason(unsuccessful_reason_id, include_object_type_name=include_object_type_name, include_record_info=include_record_info)

Retrieve a UnsuccessfulReason

Retrieve an UnsuccessfulReason

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
api_instance = bumbal.UnsuccessfulReasonApi(bumbal.ApiClient(configuration))
unsuccessful_reason_id = 789 # int | ID of UnsuccessfulReason to retrieve
include_object_type_name = false # bool | Show the name of the object type (optional) (default to false)
include_record_info = false # bool | Show the record info (optional) (default to false)

try:
    # Retrieve a UnsuccessfulReason
    api_response = api_instance.retrieve_unsuccessful_reason(unsuccessful_reason_id, include_object_type_name=include_object_type_name, include_record_info=include_record_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnsuccessfulReasonApi->retrieve_unsuccessful_reason: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unsuccessful_reason_id** | **int**| ID of UnsuccessfulReason to retrieve | 
 **include_object_type_name** | **bool**| Show the name of the object type | [optional] [default to false]
 **include_record_info** | **bool**| Show the record info | [optional] [default to false]

### Return type

[**UnsuccessfulReasonModel**](UnsuccessfulReasonModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_unsuccessful_reason**
> ApiResponse52 update_unsuccessful_reason(unsuccessful_reason_id, body=body)

Update a specific UnsuccessfulReason object

Update a specific UnsuccessfulReason object

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
api_instance = bumbal.UnsuccessfulReasonApi(bumbal.ApiClient(configuration))
unsuccessful_reason_id = 789 # int | ID of the UnsuccessfulReason object to update
body = bumbal.UnsuccessfulReasonModel() # UnsuccessfulReasonModel | UnsuccessfulReason object that needs to be updated (optional)

try:
    # Update a specific UnsuccessfulReason object
    api_response = api_instance.update_unsuccessful_reason(unsuccessful_reason_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnsuccessfulReasonApi->update_unsuccessful_reason: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unsuccessful_reason_id** | **int**| ID of the UnsuccessfulReason object to update | 
 **body** | [**UnsuccessfulReasonModel**](UnsuccessfulReasonModel.md)| UnsuccessfulReason object that needs to be updated | [optional] 

### Return type

[**ApiResponse52**](ApiResponse52.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

