# bumbal.TrailerApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trailer**](TrailerApi.md#create_trailer) | **POST** /trailer | Add a trailer
[**delete_trailer**](TrailerApi.md#delete_trailer) | **DELETE** /trailer/{trailerId} | Delete an trailer
[**retrieve_list_trailer**](TrailerApi.md#retrieve_list_trailer) | **PUT** /trailer | Retrieve List of Trailers
[**retrieve_trailer**](TrailerApi.md#retrieve_trailer) | **GET** /trailer/{trailerId} | Find trailer by ID
[**set_trailer**](TrailerApi.md#set_trailer) | **POST** /trailer/set | Set (create or update) a trailer
[**update_trailer**](TrailerApi.md#update_trailer) | **PUT** /trailer/{trailerId} | Update a trailer


# **create_trailer**
> ApiResponse create_trailer(body=body)

Add a trailer

Add a trailer

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
api_instance = bumbal.TrailerApi(bumbal.ApiClient(configuration))
body = bumbal.TrailerModel() # TrailerModel | Trailer object that needs to be created (optional)

try:
    # Add a trailer
    api_response = api_instance.create_trailer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrailerApi->create_trailer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrailerModel**](TrailerModel.md)| Trailer object that needs to be created | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_trailer**
> ApiResponse delete_trailer(trailer_id)

Delete an trailer

Delete an trailer

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
api_instance = bumbal.TrailerApi(bumbal.ApiClient(configuration))
trailer_id = 789 # int | ID of the trailer to delete

try:
    # Delete an trailer
    api_response = api_instance.delete_trailer(trailer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrailerApi->delete_trailer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trailer_id** | **int**| ID of the trailer to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_trailer**
> list[TrailerModel] retrieve_list_trailer(arguments)

Retrieve List of Trailers

Retrieve List of Trailers

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
api_instance = bumbal.TrailerApi(bumbal.ApiClient(configuration))
arguments = bumbal.TrailerRetrieveListArguments() # TrailerRetrieveListArguments | Trailer RetrieveList Arguments

try:
    # Retrieve List of Trailers
    api_response = api_instance.retrieve_list_trailer(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrailerApi->retrieve_list_trailer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**TrailerRetrieveListArguments**](TrailerRetrieveListArguments.md)| Trailer RetrieveList Arguments | 

### Return type

[**list[TrailerModel]**](TrailerModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_trailer**
> TrailerModel retrieve_trailer(trailer_id, include_trailer_tags, include_updated_by)

Find trailer by ID

Returns a single trailer

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
api_instance = bumbal.TrailerApi(bumbal.ApiClient(configuration))
trailer_id = 789 # int | ID of trailer to return
include_trailer_tags = true # bool | a list of tags bound to trailer (default to true)
include_updated_by = true # bool | include updated_by_name (default to true)

try:
    # Find trailer by ID
    api_response = api_instance.retrieve_trailer(trailer_id, include_trailer_tags, include_updated_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrailerApi->retrieve_trailer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trailer_id** | **int**| ID of trailer to return | 
 **include_trailer_tags** | **bool**| a list of tags bound to trailer | [default to true]
 **include_updated_by** | **bool**| include updated_by_name | [default to true]

### Return type

[**TrailerModel**](TrailerModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_trailer**
> ApiResponse set_trailer(body=body)

Set (create or update) a trailer

Set (create or update) a trailer. If id or links are set in the data, and a corresponding trailer is found in Bumbal, an update will be performed.

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
api_instance = bumbal.TrailerApi(bumbal.ApiClient(configuration))
body = bumbal.TrailerModel() # TrailerModel | Trailer object (optional)

try:
    # Set (create or update) a trailer
    api_response = api_instance.set_trailer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrailerApi->set_trailer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TrailerModel**](TrailerModel.md)| Trailer object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_trailer**
> ApiResponse update_trailer(trailer_id, body=body)

Update a trailer

Update a trailer

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
api_instance = bumbal.TrailerApi(bumbal.ApiClient(configuration))
trailer_id = 789 # int | ID of trailer to update
body = bumbal.TrailerModel() # TrailerModel | Trailer object that needs to be updated (optional)

try:
    # Update a trailer
    api_response = api_instance.update_trailer(trailer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrailerApi->update_trailer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trailer_id** | **int**| ID of trailer to update | 
 **body** | [**TrailerModel**](TrailerModel.md)| Trailer object that needs to be updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

