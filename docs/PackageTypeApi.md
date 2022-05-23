# bumbal.PackageTypeApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_package_type**](PackageTypeApi.md#create_package_type) | **POST** /package-type | Create or update a Package Line
[**delete_package_type**](PackageTypeApi.md#delete_package_type) | **DELETE** /package-type/{packageTypeId} | Delete an package-type
[**retrieve_list_package_type**](PackageTypeApi.md#retrieve_list_package_type) | **PUT** /package-type | Retrieve List of PackageTypes
[**retrieve_package_type**](PackageTypeApi.md#retrieve_package_type) | **GET** /package-type/{packageTypeId} | Find package-type by ID
[**set_package_type**](PackageTypeApi.md#set_package_type) | **POST** /package-type/set | Set (create or update) an PackageType
[**update_package_type**](PackageTypeApi.md#update_package_type) | **PUT** /package-type/{packageTypeId} | Update a package-type


# **create_package_type**
> ApiResponse create_package_type(body=body)

Create or update a Package Line

Create or update a PackageType. If id or links are set in the data, and a corresponding package-type    *     is found in Bumbal, an update will be performed.

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
api_instance = bumbal.PackageTypeApi(bumbal.ApiClient(configuration))
body = bumbal.PackageTypeModel() # PackageTypeModel | PackageType model (optional)

try:
    # Create or update a Package Line
    api_response = api_instance.create_package_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageTypeApi->create_package_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PackageTypeModel**](PackageTypeModel.md)| PackageType model | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_package_type**
> ApiResponse delete_package_type(package_type_id)

Delete an package-type

Delete an package-type

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
api_instance = bumbal.PackageTypeApi(bumbal.ApiClient(configuration))
package_type_id = 789 # int | ID of the package-type to delete

try:
    # Delete an package-type
    api_response = api_instance.delete_package_type(package_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageTypeApi->delete_package_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_type_id** | **int**| ID of the package-type to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_package_type**
> PackageTypeListResponse retrieve_list_package_type(arguments)

Retrieve List of PackageTypes

Retrieve List of PackageTypes

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
api_instance = bumbal.PackageTypeApi(bumbal.ApiClient(configuration))
arguments = bumbal.PackageTypeRetrieveListArguments() # PackageTypeRetrieveListArguments | PackageType RetrieveList Arguments

try:
    # Retrieve List of PackageTypes
    api_response = api_instance.retrieve_list_package_type(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageTypeApi->retrieve_list_package_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**PackageTypeRetrieveListArguments**](PackageTypeRetrieveListArguments.md)| PackageType RetrieveList Arguments | 

### Return type

[**PackageTypeListResponse**](PackageTypeListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_package_type**
> PackageTypeModel retrieve_package_type(package_type_id)

Find package-type by ID

Returns a single package-type

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
api_instance = bumbal.PackageTypeApi(bumbal.ApiClient(configuration))
package_type_id = 789 # int | ID of package-type to return

try:
    # Find package-type by ID
    api_response = api_instance.retrieve_package_type(package_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageTypeApi->retrieve_package_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_type_id** | **int**| ID of package-type to return | 

### Return type

[**PackageTypeModel**](PackageTypeModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_package_type**
> ApiResponse set_package_type(body=body)

Set (create or update) an PackageType

Set (create or update) an PackageType. If id or links are set in the data, and a corresponding package-type is found in Bumbal, an update will be performed.

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
api_instance = bumbal.PackageTypeApi(bumbal.ApiClient(configuration))
body = bumbal.PackageTypeModel() # PackageTypeModel | PackageType model (optional)

try:
    # Set (create or update) an PackageType
    api_response = api_instance.set_package_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageTypeApi->set_package_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PackageTypeModel**](PackageTypeModel.md)| PackageType model | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_package_type**
> ApiResponse update_package_type(package_type_id, body=body)

Update a package-type

Update a package-type

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
api_instance = bumbal.PackageTypeApi(bumbal.ApiClient(configuration))
package_type_id = 789 # int | ID of package-type to update
body = bumbal.PackageTypeModel() # PackageTypeModel | PackageType object that needs to be updated (optional)

try:
    # Update a package-type
    api_response = api_instance.update_package_type(package_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageTypeApi->update_package_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_type_id** | **int**| ID of package-type to update | 
 **body** | [**PackageTypeModel**](PackageTypeModel.md)| PackageType object that needs to be updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

