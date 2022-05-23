# bumbal.FileApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](FileApi.md#delete_file) | **DELETE** /file/{fileId} | Delete an File
[**file_copy**](FileApi.md#file_copy) | **POST** /file/copy | Copy File
[**retrieve_file**](FileApi.md#retrieve_file) | **GET** /file/{fileId} | Retrieve a File
[**retrieve_list_file**](FileApi.md#retrieve_list_file) | **PUT** /file | Retrieve List of Files
[**set_file**](FileApi.md#set_file) | **POST** /file/set | Create or Update a File Object


# **delete_file**
> ApiResponse delete_file(file_id)

Delete an File

Delete an File

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
api_instance = bumbal.FileApi(bumbal.ApiClient(configuration))
file_id = 789 # int | ID of file to update

try:
    # Delete an File
    api_response = api_instance.delete_file(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| ID of file to update | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_copy**
> ApiResponse file_copy(arguments)

Copy File

Copy file from one object to another

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
api_instance = bumbal.FileApi(bumbal.ApiClient(configuration))
arguments = bumbal.FileCopyArguments() # FileCopyArguments | Request Arguments

try:
    # Copy File
    api_response = api_instance.file_copy(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->file_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**FileCopyArguments**](FileCopyArguments.md)| Request Arguments | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_file**
> FileModel retrieve_file(file_id)

Retrieve a File

Retrieve an File

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
api_instance = bumbal.FileApi(bumbal.ApiClient(configuration))
file_id = 789 # int | ID of file to retrieve

try:
    # Retrieve a File
    api_response = api_instance.retrieve_file(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->retrieve_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| ID of file to retrieve | 

### Return type

[**FileModel**](FileModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_file**
> list[FileModel] retrieve_list_file(arguments)

Retrieve List of Files

Retrieve List of Files

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
api_instance = bumbal.FileApi(bumbal.ApiClient(configuration))
arguments = bumbal.FileRetrieveListArguments() # FileRetrieveListArguments | File RetrieveList Arguments

try:
    # Retrieve List of Files
    api_response = api_instance.retrieve_list_file(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->retrieve_list_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**FileRetrieveListArguments**](FileRetrieveListArguments.md)| File RetrieveList Arguments | 

### Return type

[**list[FileModel]**](FileModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file**
> ApiResponse set_file(body=body)

Create or Update a File Object

Create or Update a File Object

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
api_instance = bumbal.FileApi(bumbal.ApiClient(configuration))
body = bumbal.FileModel() # FileModel | File object that needs to be set (optional)

try:
    # Create or Update a File Object
    api_response = api_instance.set_file(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->set_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileModel**](FileModel.md)| File object that needs to be set | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

