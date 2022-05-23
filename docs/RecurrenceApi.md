# bumbal.RecurrenceApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_activity_recurrence**](RecurrenceApi.md#create_activity_recurrence) | **POST** /recurrence/create-activity-recurrence | create a activity recurrence
[**create_route_recurrence**](RecurrenceApi.md#create_route_recurrence) | **POST** /recurrence/create-route-recurrence | create a route recurrence
[**delete_recurrence**](RecurrenceApi.md#delete_recurrence) | **DELETE** /recurrence/{recurrenceId} | Delete an Recurrence
[**finish**](RecurrenceApi.md#finish) | **POST** /recurrence/finish | Cleans up after the process run
[**get_runs**](RecurrenceApi.md#get_runs) | **POST** /recurrence/get-runs | Returns the given runs for the next recurrences!
[**process_runs**](RecurrenceApi.md#process_runs) | **POST** /recurrence/process-runs | Executes the the processes for the ids retrieved with get-runs
[**retrieve_list_recurrence**](RecurrenceApi.md#retrieve_list_recurrence) | **PUT** /recurrence | Retrieve List of Recurrences
[**retrieve_recurrence**](RecurrenceApi.md#retrieve_recurrence) | **GET** /recurrence/{recurrenceId} | Retrieve a Recurrence
[**update_recurrence**](RecurrenceApi.md#update_recurrence) | **PUT** /recurrence/{recurrenceId} | Update a Recurrence


# **create_activity_recurrence**
> ApiResponse create_activity_recurrence(body)

create a activity recurrence

create a activity recurrence

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
api_instance = bumbal.RecurrenceApi(bumbal.ApiClient(configuration))
body = bumbal.RecurrenceModel() # RecurrenceModel | Recurrence object that needs to be created

try:
    # create a activity recurrence
    api_response = api_instance.create_activity_recurrence(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrenceApi->create_activity_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecurrenceModel**](RecurrenceModel.md)| Recurrence object that needs to be created | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_route_recurrence**
> ApiResponse create_route_recurrence(body)

create a route recurrence

create a route recurrence

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
api_instance = bumbal.RecurrenceApi(bumbal.ApiClient(configuration))
body = bumbal.RecurrenceModel() # RecurrenceModel | Recurrence object that needs to be created

try:
    # create a route recurrence
    api_response = api_instance.create_route_recurrence(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrenceApi->create_route_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecurrenceModel**](RecurrenceModel.md)| Recurrence object that needs to be created | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recurrence**
> ApiResponse delete_recurrence(recurrence_id)

Delete an Recurrence

Delete an Recurrence

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
api_instance = bumbal.RecurrenceApi(bumbal.ApiClient(configuration))
recurrence_id = 789 # int | ID of recurrence to delete

try:
    # Delete an Recurrence
    api_response = api_instance.delete_recurrence(recurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrenceApi->delete_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurrence_id** | **int**| ID of recurrence to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **finish**
> RecurrenceFinishResponse finish()

Cleans up after the process run



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
api_instance = bumbal.RecurrenceApi(bumbal.ApiClient(configuration))

try:
    # Cleans up after the process run
    api_response = api_instance.finish()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrenceApi->finish: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RecurrenceFinishResponse**](RecurrenceFinishResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runs**
> RecurrenceGetRunsResponse get_runs(arguments)

Returns the given runs for the next recurrences!



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
api_instance = bumbal.RecurrenceApi(bumbal.ApiClient(configuration))
arguments = bumbal.RecurrenceGetRunsArguments() # RecurrenceGetRunsArguments | Request Arguments

try:
    # Returns the given runs for the next recurrences!
    api_response = api_instance.get_runs(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrenceApi->get_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**RecurrenceGetRunsArguments**](RecurrenceGetRunsArguments.md)| Request Arguments | 

### Return type

[**RecurrenceGetRunsResponse**](RecurrenceGetRunsResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_runs**
> RecurrenceProcessRunsResponse process_runs(arguments)

Executes the the processes for the ids retrieved with get-runs



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
api_instance = bumbal.RecurrenceApi(bumbal.ApiClient(configuration))
arguments = bumbal.RecurrenceProcessRunsArguments() # RecurrenceProcessRunsArguments | Request Arguments

try:
    # Executes the the processes for the ids retrieved with get-runs
    api_response = api_instance.process_runs(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrenceApi->process_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**RecurrenceProcessRunsArguments**](RecurrenceProcessRunsArguments.md)| Request Arguments | 

### Return type

[**RecurrenceProcessRunsResponse**](RecurrenceProcessRunsResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_recurrence**
> RecurrenceListResponse retrieve_list_recurrence(arguments)

Retrieve List of Recurrences

Retrieve List of Recurrences

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
api_instance = bumbal.RecurrenceApi(bumbal.ApiClient(configuration))
arguments = bumbal.RecurrenceRetrieveListArguments() # RecurrenceRetrieveListArguments | Recurrence RetrieveList Arguments

try:
    # Retrieve List of Recurrences
    api_response = api_instance.retrieve_list_recurrence(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrenceApi->retrieve_list_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**RecurrenceRetrieveListArguments**](RecurrenceRetrieveListArguments.md)| Recurrence RetrieveList Arguments | 

### Return type

[**RecurrenceListResponse**](RecurrenceListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_recurrence**
> RecurrenceModel retrieve_recurrence(recurrence_id)

Retrieve a Recurrence

Retrieve an Recurrence

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
api_instance = bumbal.RecurrenceApi(bumbal.ApiClient(configuration))
recurrence_id = 789 # int | ID of recurrence to retrieve

try:
    # Retrieve a Recurrence
    api_response = api_instance.retrieve_recurrence(recurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrenceApi->retrieve_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurrence_id** | **int**| ID of recurrence to retrieve | 

### Return type

[**RecurrenceModel**](RecurrenceModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recurrence**
> ApiResponse update_recurrence(recurrence_id)

Update a Recurrence

Update an Recurrence

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
api_instance = bumbal.RecurrenceApi(bumbal.ApiClient(configuration))
recurrence_id = 789 # int | ID of recurrence to update

try:
    # Update a Recurrence
    api_response = api_instance.update_recurrence(recurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecurrenceApi->update_recurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recurrence_id** | **int**| ID of recurrence to update | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

