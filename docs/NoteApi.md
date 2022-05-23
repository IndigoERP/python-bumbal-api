# bumbal.NoteApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_note**](NoteApi.md#delete_note) | **DELETE** /note/{noteId} | Delete an note
[**retrieve_list_note**](NoteApi.md#retrieve_list_note) | **PUT** /note | Retrieve List of Notes
[**retrieve_note**](NoteApi.md#retrieve_note) | **GET** /note/{noteId} | Find note by ID
[**set_note**](NoteApi.md#set_note) | **POST** /note/set | Set (create or update) a note


# **delete_note**
> ApiResponse delete_note(note_id)

Delete an note

Delete an note

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
api_instance = bumbal.NoteApi(bumbal.ApiClient(configuration))
note_id = 789 # int | ID of the note to delete

try:
    # Delete an note
    api_response = api_instance.delete_note(note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteApi->delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| ID of the note to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_note**
> list[NoteModel] retrieve_list_note(arguments)

Retrieve List of Notes

Retrieve List of Notes

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
api_instance = bumbal.NoteApi(bumbal.ApiClient(configuration))
arguments = bumbal.NoteRetrieveListArguments() # NoteRetrieveListArguments | Note RetrieveList Arguments

try:
    # Retrieve List of Notes
    api_response = api_instance.retrieve_list_note(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteApi->retrieve_list_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**NoteRetrieveListArguments**](NoteRetrieveListArguments.md)| Note RetrieveList Arguments | 

### Return type

[**list[NoteModel]**](NoteModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_note**
> NoteModel retrieve_note(note_id, include_note_tags, include_note_tag_type_link_ids, include_note_object_link_ids, include_updated_by)

Find note by ID

Returns a single note

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
api_instance = bumbal.NoteApi(bumbal.ApiClient(configuration))
note_id = 789 # int | ID of note to return
include_note_tags = true # bool | a list of tags bound to note (default to true)
include_note_tag_type_link_ids = true # bool | link ids of the tag types (default to true)
include_note_object_link_ids = true # bool | Include teh link ids bound to teh object where teh note belongs to (default to true)
include_updated_by = true # bool | include updated_by_name (default to true)

try:
    # Find note by ID
    api_response = api_instance.retrieve_note(note_id, include_note_tags, include_note_tag_type_link_ids, include_note_object_link_ids, include_updated_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteApi->retrieve_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_id** | **int**| ID of note to return | 
 **include_note_tags** | **bool**| a list of tags bound to note | [default to true]
 **include_note_tag_type_link_ids** | **bool**| link ids of the tag types | [default to true]
 **include_note_object_link_ids** | **bool**| Include teh link ids bound to teh object where teh note belongs to | [default to true]
 **include_updated_by** | **bool**| include updated_by_name | [default to true]

### Return type

[**NoteModel**](NoteModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_note**
> ApiResponse set_note(body=body)

Set (create or update) a note

Set (create or update) a note. If id or links are set in the data, and a corresponding note is found in Bumbal, an update will be performed.

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
api_instance = bumbal.NoteApi(bumbal.ApiClient(configuration))
body = bumbal.NoteModel() # NoteModel | Note object (optional)

try:
    # Set (create or update) a note
    api_response = api_instance.set_note(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NoteApi->set_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NoteModel**](NoteModel.md)| Note object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

