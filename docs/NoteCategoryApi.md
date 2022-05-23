# bumbal.NoteCategoryApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_note_category**](NoteCategoryApi.md#delete_note_category) | **DELETE** /note-category/{noteCategoryId} | Delete a note-category
[**retrieve_list_note_category**](NoteCategoryApi.md#retrieve_list_note_category) | **PUT** /note-category | Retrieve List of NoteCategories
[**retrieve_note_category**](NoteCategoryApi.md#retrieve_note_category) | **GET** /note-category/{noteCategoryId} | Find note-category by ID
[**set_note_category**](NoteCategoryApi.md#set_note_category) | **POST** /note-category/set | Set (create or update) an NoteCategory


# **delete_note_category**
> ApiResponse delete_note_category(note_category_id)

Delete a note-category

Delete a note-category

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
api_instance = bumbal.NoteCategoryApi(bumbal.ApiClient(configuration))
note_category_id = 789 # int | ID of the note-category to delete

try:
    # Delete a note-category
    api_response = api_instance.delete_note_category(note_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteCategoryApi->delete_note_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_category_id** | **int**| ID of the note-category to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_note_category**
> NoteCategoryListResponse retrieve_list_note_category(arguments)

Retrieve List of NoteCategories

Retrieve List of NoteCategories

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
api_instance = bumbal.NoteCategoryApi(bumbal.ApiClient(configuration))
arguments = bumbal.NoteCategoryRetrieveListArguments() # NoteCategoryRetrieveListArguments | NoteCategory RetrieveList Arguments

try:
    # Retrieve List of NoteCategories
    api_response = api_instance.retrieve_list_note_category(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteCategoryApi->retrieve_list_note_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**NoteCategoryRetrieveListArguments**](NoteCategoryRetrieveListArguments.md)| NoteCategory RetrieveList Arguments | 

### Return type

[**NoteCategoryListResponse**](NoteCategoryListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_note_category**
> NoteCategoryModel retrieve_note_category(note_category_id)

Find note-category by ID

Returns a single note-category

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
api_instance = bumbal.NoteCategoryApi(bumbal.ApiClient(configuration))
note_category_id = 789 # int | ID of note-category to return

try:
    # Find note-category by ID
    api_response = api_instance.retrieve_note_category(note_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteCategoryApi->retrieve_note_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_category_id** | **int**| ID of note-category to return | 

### Return type

[**NoteCategoryModel**](NoteCategoryModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_note_category**
> ApiResponse set_note_category(body=body)

Set (create or update) an NoteCategory

Set (create or update) a NoteCategory. If id is set in the data, and a corresponding note-category is found in Bumbal, an update will be performed.

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
api_instance = bumbal.NoteCategoryApi(bumbal.ApiClient(configuration))
body = bumbal.NoteCategoryModel() # NoteCategoryModel | NoteCategory model (optional)

try:
    # Set (create or update) an NoteCategory
    api_response = api_instance.set_note_category(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteCategoryApi->set_note_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NoteCategoryModel**](NoteCategoryModel.md)| NoteCategory model | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

