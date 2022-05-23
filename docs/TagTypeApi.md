# bumbal.TagTypeApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag_type**](TagTypeApi.md#create_tag_type) | **POST** /tag-type | Add a new Tag type
[**delete_tag_type**](TagTypeApi.md#delete_tag_type) | **DELETE** /tag-type/{tagTypeId} | Delete a Tag type
[**retrieve_list_tag_type**](TagTypeApi.md#retrieve_list_tag_type) | **PUT** /tag-type | Retrieve List of Tag types
[**retrieve_tag_type**](TagTypeApi.md#retrieve_tag_type) | **GET** /tag-type/{tagTypeId} | Retrieve a Tag type
[**set_tag_type**](TagTypeApi.md#set_tag_type) | **POST** /tag-type/set | Set (create or update) Tag type
[**update_tag_type**](TagTypeApi.md#update_tag_type) | **PUT** /tag-type/{tagTypeId} | Update a Tag type


# **create_tag_type**
> ApiResponse create_tag_type(body)

Add a new Tag type

Add a new Tag type

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
api_instance = bumbal.TagTypeApi(bumbal.ApiClient(configuration))
body = bumbal.TagTypeModel() # TagTypeModel | Tag type object that needs to be created

try:
    # Add a new Tag type
    api_response = api_instance.create_tag_type(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTypeApi->create_tag_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagTypeModel**](TagTypeModel.md)| Tag type object that needs to be created | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_type**
> ApiResponse delete_tag_type(tag_type_id)

Delete a Tag type

Delete a Tag type

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
api_instance = bumbal.TagTypeApi(bumbal.ApiClient(configuration))
tag_type_id = 789 # int | ID of tag type to delete

try:
    # Delete a Tag type
    api_response = api_instance.delete_tag_type(tag_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTypeApi->delete_tag_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_type_id** | **int**| ID of tag type to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_tag_type**
> TagTypeRetrieveResponse retrieve_list_tag_type(arguments)

Retrieve List of Tag types

Retrieve List of Tags

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
api_instance = bumbal.TagTypeApi(bumbal.ApiClient(configuration))
arguments = bumbal.TagTypeRetrieveListArguments() # TagTypeRetrieveListArguments | Tag types RetrieveList Arguments

try:
    # Retrieve List of Tag types
    api_response = api_instance.retrieve_list_tag_type(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTypeApi->retrieve_list_tag_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**TagTypeRetrieveListArguments**](TagTypeRetrieveListArguments.md)| Tag types RetrieveList Arguments | 

### Return type

[**TagTypeRetrieveResponse**](TagTypeRetrieveResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_tag_type**
> TagTypeModel retrieve_tag_type(tag_type_id, include_object_types=include_object_types)

Retrieve a Tag type

Retrieve an Tag type

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
api_instance = bumbal.TagTypeApi(bumbal.ApiClient(configuration))
tag_type_id = 789 # int | ID of tag type to retrieve
include_object_types = true # bool | Show the text value of the status (optional)

try:
    # Retrieve a Tag type
    api_response = api_instance.retrieve_tag_type(tag_type_id, include_object_types=include_object_types)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTypeApi->retrieve_tag_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_type_id** | **int**| ID of tag type to retrieve | 
 **include_object_types** | **bool**| Show the text value of the status | [optional] 

### Return type

[**TagTypeModel**](TagTypeModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tag_type**
> ApiResponse set_tag_type(body=body)

Set (create or update) Tag type

Set (create or update) Tag type. If a tag type with same name is found in Bumbal, the tag type id is returned.

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
api_instance = bumbal.TagTypeApi(bumbal.ApiClient(configuration))
body = bumbal.TagTypeModel() # TagTypeModel | tag type data (optional)

try:
    # Set (create or update) Tag type
    api_response = api_instance.set_tag_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTypeApi->set_tag_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagTypeModel**](TagTypeModel.md)| tag type data | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag_type**
> ApiResponse update_tag_type(tag_type_id)

Update a Tag type

Update a Tag type

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
api_instance = bumbal.TagTypeApi(bumbal.ApiClient(configuration))
tag_type_id = 789 # int | ID of tag type to update

try:
    # Update a Tag type
    api_response = api_instance.update_tag_type(tag_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagTypeApi->update_tag_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_type_id** | **int**| ID of tag type to update | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

