# bumbal.CapacityTypeApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_capacity_type**](CapacityTypeApi.md#delete_capacity_type) | **DELETE** /capacity-type/{capacityTypeId} | Delete a capacity-type
[**retrieve_capacity_type**](CapacityTypeApi.md#retrieve_capacity_type) | **GET** /capacity-type/{capacityTypeId} | Find capacity-type by ID
[**retrieve_list_capacity_type**](CapacityTypeApi.md#retrieve_list_capacity_type) | **PUT** /capacity-type | Retrieve List of CapacityTypes
[**set_capacity_type**](CapacityTypeApi.md#set_capacity_type) | **POST** /capacity-type/set | Set (create or update) an CapacityType


# **delete_capacity_type**
> ApiResponse delete_capacity_type(capacity_type_id)

Delete a capacity-type

Delete a capacity-type

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
api_instance = bumbal.CapacityTypeApi(bumbal.ApiClient(configuration))
capacity_type_id = 789 # int | ID of the capacity-type to delete

try:
    # Delete a capacity-type
    api_response = api_instance.delete_capacity_type(capacity_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CapacityTypeApi->delete_capacity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capacity_type_id** | **int**| ID of the capacity-type to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_capacity_type**
> CapacityTypeModel retrieve_capacity_type(capacity_type_id, include_uom=include_uom, include_uom_group=include_uom_group, include_uom_name=include_uom_name)

Find capacity-type by ID

Returns a single capacity-type

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
api_instance = bumbal.CapacityTypeApi(bumbal.ApiClient(configuration))
capacity_type_id = 789 # int | ID of capacity-type to return
include_uom = false # bool | Include uom object (optional) (default to false)
include_uom_group = false # bool | Include uom group (optional) (default to false)
include_uom_name = false # bool | Include uom name (optional) (default to false)

try:
    # Find capacity-type by ID
    api_response = api_instance.retrieve_capacity_type(capacity_type_id, include_uom=include_uom, include_uom_group=include_uom_group, include_uom_name=include_uom_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CapacityTypeApi->retrieve_capacity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capacity_type_id** | **int**| ID of capacity-type to return | 
 **include_uom** | **bool**| Include uom object | [optional] [default to false]
 **include_uom_group** | **bool**| Include uom group | [optional] [default to false]
 **include_uom_name** | **bool**| Include uom name | [optional] [default to false]

### Return type

[**CapacityTypeModel**](CapacityTypeModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_capacity_type**
> CapacityTypeListResponse retrieve_list_capacity_type(arguments)

Retrieve List of CapacityTypes

Retrieve List of CapacityTypes

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
api_instance = bumbal.CapacityTypeApi(bumbal.ApiClient(configuration))
arguments = bumbal.CapacityTypeRetrieveListArguments() # CapacityTypeRetrieveListArguments | CapacityType RetrieveList Arguments

try:
    # Retrieve List of CapacityTypes
    api_response = api_instance.retrieve_list_capacity_type(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CapacityTypeApi->retrieve_list_capacity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**CapacityTypeRetrieveListArguments**](CapacityTypeRetrieveListArguments.md)| CapacityType RetrieveList Arguments | 

### Return type

[**CapacityTypeListResponse**](CapacityTypeListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_capacity_type**
> ApiResponse set_capacity_type(body=body)

Set (create or update) an CapacityType

Set (create or update) a CapacityType. If id is set in the data, and a corresponding capacity-type is found in Bumbal, an update will be performed.

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
api_instance = bumbal.CapacityTypeApi(bumbal.ApiClient(configuration))
body = bumbal.CapacityTypeModel() # CapacityTypeModel | CapacityType model (optional)

try:
    # Set (create or update) an CapacityType
    api_response = api_instance.set_capacity_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CapacityTypeApi->set_capacity_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CapacityTypeModel**](CapacityTypeModel.md)| CapacityType model | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

