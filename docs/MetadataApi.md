# bumbal.MetadataApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_meta_data**](MetadataApi.md#create_meta_data) | **POST** /metadata | Add a new MetaData
[**delete_meta_data**](MetadataApi.md#delete_meta_data) | **DELETE** /metadata/{metadataId} | Delete a MetaData entry
[**retrieve_list_meta_data**](MetadataApi.md#retrieve_list_meta_data) | **PUT** /metadata | Retrieve List of MetaData
[**retrieve_meta_data**](MetadataApi.md#retrieve_meta_data) | **GET** /metadata/{metadataId} | Retrieve a MetaData
[**set_meta_data**](MetadataApi.md#set_meta_data) | **POST** /metadata/set | Set (create or update) a MetaData record
[**update_meta_data**](MetadataApi.md#update_meta_data) | **PUT** /metadata/{metadataId} | Update a specific MetaData object


# **create_meta_data**
> ApiResponse create_meta_data(body=body)

Add a new MetaData

Add a new MetaData

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
api_instance = bumbal.MetadataApi(bumbal.ApiClient(configuration))
body = bumbal.MetaDataModel() # MetaDataModel | MetaData object that needs to be created (optional)

try:
    # Add a new MetaData
    api_response = api_instance.create_meta_data(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->create_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetaDataModel**](MetaDataModel.md)| MetaData object that needs to be created | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_meta_data**
> ApiResponse6 delete_meta_data(metadata_id)

Delete a MetaData entry

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
api_instance = bumbal.MetadataApi(bumbal.ApiClient(configuration))
metadata_id = 789 # int | ID of MetaData to delete

try:
    # Delete a MetaData entry
    api_response = api_instance.delete_meta_data(metadata_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->delete_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_id** | **int**| ID of MetaData to delete | 

### Return type

[**ApiResponse6**](ApiResponse6.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_meta_data**
> MetaDataListResponse retrieve_list_meta_data(arguments)

Retrieve List of MetaData

Retrieve List of MetaData

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
api_instance = bumbal.MetadataApi(bumbal.ApiClient(configuration))
arguments = bumbal.MetaDataRetrieveListArguments() # MetaDataRetrieveListArguments | MetaData RetrieveList Arguments

try:
    # Retrieve List of MetaData
    api_response = api_instance.retrieve_list_meta_data(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->retrieve_list_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**MetaDataRetrieveListArguments**](MetaDataRetrieveListArguments.md)| MetaData RetrieveList Arguments | 

### Return type

[**MetaDataListResponse**](MetaDataListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_meta_data**
> MetaDataModel retrieve_meta_data(metadata_id, include_object_type_name=include_object_type_name, include_record_info=include_record_info)

Retrieve a MetaData

Retrieve an MetaData

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
api_instance = bumbal.MetadataApi(bumbal.ApiClient(configuration))
metadata_id = 789 # int | ID of MetaData to retrieve
include_object_type_name = false # bool | Show the name of the object type (optional) (default to false)
include_record_info = false # bool | Show the record info (optional) (default to false)

try:
    # Retrieve a MetaData
    api_response = api_instance.retrieve_meta_data(metadata_id, include_object_type_name=include_object_type_name, include_record_info=include_record_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->retrieve_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_id** | **int**| ID of MetaData to retrieve | 
 **include_object_type_name** | **bool**| Show the name of the object type | [optional] [default to false]
 **include_record_info** | **bool**| Show the record info | [optional] [default to false]

### Return type

[**MetaDataModel**](MetaDataModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_meta_data**
> ApiResponse set_meta_data(body=body)

Set (create or update) a MetaData record

Set (create or update) a meta data record. If id or name is set in the data, and a corresponding meta data record is found in Bumbal, an update will be performed.

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
api_instance = bumbal.MetadataApi(bumbal.ApiClient(configuration))
body = bumbal.MetaDataModel() # MetaDataModel | MetaData object (optional)

try:
    # Set (create or update) a MetaData record
    api_response = api_instance.set_meta_data(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->set_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MetaDataModel**](MetaDataModel.md)| MetaData object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_meta_data**
> ApiResponse5 update_meta_data(metadata_id, body=body)

Update a specific MetaData object

Update a specific MetaData object

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
api_instance = bumbal.MetadataApi(bumbal.ApiClient(configuration))
metadata_id = 789 # int | ID of the MetaData object to update
body = bumbal.MetaDataModel() # MetaDataModel | MetaData object that needs to be updated (optional)

try:
    # Update a specific MetaData object
    api_response = api_instance.update_meta_data(metadata_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->update_meta_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metadata_id** | **int**| ID of the MetaData object to update | 
 **body** | [**MetaDataModel**](MetaDataModel.md)| MetaData object that needs to be updated | [optional] 

### Return type

[**ApiResponse5**](ApiResponse5.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

