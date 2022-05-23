# bumbal.EquipmentApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_equipment**](EquipmentApi.md#create_equipment) | **POST** /equipment | Add a new Equipment
[**delete_equipment**](EquipmentApi.md#delete_equipment) | **DELETE** /equipment/{equipmentId} | Delete an Equipment entry
[**retrieve_equipment**](EquipmentApi.md#retrieve_equipment) | **GET** /equipment/{equipmentId} | Retrieve a Equipment
[**retrieve_list_equipment**](EquipmentApi.md#retrieve_list_equipment) | **PUT** /equipment | Retrieve List of Equipment
[**set_equipment**](EquipmentApi.md#set_equipment) | **POST** /equipment/set | Set (create or update) a Equipment
[**update_equipment**](EquipmentApi.md#update_equipment) | **PUT** /equipment/{equipmentId} | Update a specific Equipment object


# **create_equipment**
> EquipmentCreateResponse create_equipment(body=body)

Add a new Equipment

Add a new Equipment

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
api_instance = bumbal.EquipmentApi(bumbal.ApiClient(configuration))
body = bumbal.EquipmentModel() # EquipmentModel | Equipment object that needs to be created (optional)

try:
    # Add a new Equipment
    api_response = api_instance.create_equipment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentApi->create_equipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EquipmentModel**](EquipmentModel.md)| Equipment object that needs to be created | [optional] 

### Return type

[**EquipmentCreateResponse**](EquipmentCreateResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_equipment**
> EquipmentDeleteResponse delete_equipment(equipment_id)

Delete an Equipment entry

Delete an Equipment entry

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
api_instance = bumbal.EquipmentApi(bumbal.ApiClient(configuration))
equipment_id = 789 # int | ID of Equipment to delete

try:
    # Delete an Equipment entry
    api_response = api_instance.delete_equipment(equipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentApi->delete_equipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **equipment_id** | **int**| ID of Equipment to delete | 

### Return type

[**EquipmentDeleteResponse**](EquipmentDeleteResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_equipment**
> EquipmentModel retrieve_equipment(equipment_id)

Retrieve a Equipment

Retrieve an Equipment

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
api_instance = bumbal.EquipmentApi(bumbal.ApiClient(configuration))
equipment_id = 789 # int | ID of Equipment to retrieve

try:
    # Retrieve a Equipment
    api_response = api_instance.retrieve_equipment(equipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentApi->retrieve_equipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **equipment_id** | **int**| ID of Equipment to retrieve | 

### Return type

[**EquipmentModel**](EquipmentModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_equipment**
> EquipmentListResponse retrieve_list_equipment(arguments)

Retrieve List of Equipment

Retrieve List of Equipment

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
api_instance = bumbal.EquipmentApi(bumbal.ApiClient(configuration))
arguments = bumbal.EquipmentRetrieveListArguments() # EquipmentRetrieveListArguments | Equipment RetrieveList Arguments

try:
    # Retrieve List of Equipment
    api_response = api_instance.retrieve_list_equipment(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentApi->retrieve_list_equipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**EquipmentRetrieveListArguments**](EquipmentRetrieveListArguments.md)| Equipment RetrieveList Arguments | 

### Return type

[**EquipmentListResponse**](EquipmentListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_equipment**
> EquipmentSetResponse set_equipment(body=body)

Set (create or update) a Equipment

Set (create or update) a d=Equipment. If id or links are set in the data, and a corresponding Equipment is found in Bumbal, an update will be performed.

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
api_instance = bumbal.EquipmentApi(bumbal.ApiClient(configuration))
body = bumbal.EquipmentModel() # EquipmentModel | Equipment object (optional)

try:
    # Set (create or update) a Equipment
    api_response = api_instance.set_equipment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentApi->set_equipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EquipmentModel**](EquipmentModel.md)| Equipment object | [optional] 

### Return type

[**EquipmentSetResponse**](EquipmentSetResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_equipment**
> EquipmentUpdateResponse update_equipment(equipment_id, body=body)

Update a specific Equipment object

Update a specific Equipment object

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
api_instance = bumbal.EquipmentApi(bumbal.ApiClient(configuration))
equipment_id = 789 # int | ID of the Equipment object to update
body = bumbal.EquipmentModel() # EquipmentModel | Equipment object that needs to be updated (optional)

try:
    # Update a specific Equipment object
    api_response = api_instance.update_equipment(equipment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EquipmentApi->update_equipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **equipment_id** | **int**| ID of the Equipment object to update | 
 **body** | [**EquipmentModel**](EquipmentModel.md)| Equipment object that needs to be updated | [optional] 

### Return type

[**EquipmentUpdateResponse**](EquipmentUpdateResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

