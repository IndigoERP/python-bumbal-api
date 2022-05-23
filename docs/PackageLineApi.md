# bumbal.PackageLineApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_package_line**](PackageLineApi.md#create_package_line) | **POST** /package-line | Create or update an Package Line
[**delete_package_line**](PackageLineApi.md#delete_package_line) | **DELETE** /package-line/{packageLineId} | Delete an package-line
[**retrieve_list_package_line**](PackageLineApi.md#retrieve_list_package_line) | **PUT** /package-line | Retrieve List of PackageLines
[**retrieve_package_line**](PackageLineApi.md#retrieve_package_line) | **GET** /package-line/{packageLineId} | Find package-line by ID
[**set_package_line**](PackageLineApi.md#set_package_line) | **POST** /package-line/set | Set (create or update) an PackageLine
[**update_package_line**](PackageLineApi.md#update_package_line) | **PUT** /package-line/update | Update package-lines in bulk


# **create_package_line**
> ApiResponse create_package_line(body=body)

Create or update an Package Line

Create or update an PackageLine. If id or links are set in the data, and a corresponding package-line    *     is found in Bumbal, an update will be performed.

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
api_instance = bumbal.PackageLineApi(bumbal.ApiClient(configuration))
body = bumbal.PackageLineModel() # PackageLineModel | PackageLine model (optional)

try:
    # Create or update an Package Line
    api_response = api_instance.create_package_line(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageLineApi->create_package_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PackageLineModel**](PackageLineModel.md)| PackageLine model | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_package_line**
> ApiResponse delete_package_line(package_line_id)

Delete an package-line

Delete an package-line

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
api_instance = bumbal.PackageLineApi(bumbal.ApiClient(configuration))
package_line_id = 789 # int | ID of the package-line to delete

try:
    # Delete an package-line
    api_response = api_instance.delete_package_line(package_line_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageLineApi->delete_package_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_line_id** | **int**| ID of the package-line to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_package_line**
> PackageLineListResponse retrieve_list_package_line(arguments)

Retrieve List of PackageLines

Retrieve List of PackageLines

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
api_instance = bumbal.PackageLineApi(bumbal.ApiClient(configuration))
arguments = bumbal.PackageLineRetrieveListArguments() # PackageLineRetrieveListArguments | PackageLine RetrieveList Arguments

try:
    # Retrieve List of PackageLines
    api_response = api_instance.retrieve_list_package_line(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageLineApi->retrieve_list_package_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**PackageLineRetrieveListArguments**](PackageLineRetrieveListArguments.md)| PackageLine RetrieveList Arguments | 

### Return type

[**PackageLineListResponse**](PackageLineListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_package_line**
> PackageLineModel retrieve_package_line(package_line_id, include_package_line_status, include_package_line_type_name, include_package_line_meta_data, include_address_object, include_time_slots, include_time_slot_tags, include_route_info, include_driver_info, include_communication, include_package_line_links, include_package_lines_info, include_package_line_files, include_package_line_files_meta_data)

Find package-line by ID

Returns a single package-line

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
api_instance = bumbal.PackageLineApi(bumbal.ApiClient(configuration))
package_line_id = 789 # int | ID of package-line to return
include_package_line_status = true # bool | Show the text value of the status (default to true)
include_package_line_type_name = true # bool | Show the text value of the package-line type (default to true)
include_package_line_meta_data = true # bool | Include meta data connected to this PackageLine (default to true)
include_address_object = true # bool | Include address data (default to true)
include_time_slots = true # bool | Include TimeSlots (default to true)
include_time_slot_tags = true # bool | Include tags from TimeSlots (default to true)
include_route_info = true # bool | Include route data (default to true)
include_driver_info = true # bool | Include driver data (default to true)
include_communication = true # bool | Include Communication Settings (default to true)
include_package_line_links = true # bool | Include Link Data (default to true)
include_package_lines_info = true # bool | Include PackageLines (default to true)
include_package_line_files = true # bool | Include files (default to true)
include_package_line_files_meta_data = true # bool | Include files meta data (default to true)

try:
    # Find package-line by ID
    api_response = api_instance.retrieve_package_line(package_line_id, include_package_line_status, include_package_line_type_name, include_package_line_meta_data, include_address_object, include_time_slots, include_time_slot_tags, include_route_info, include_driver_info, include_communication, include_package_line_links, include_package_lines_info, include_package_line_files, include_package_line_files_meta_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageLineApi->retrieve_package_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_line_id** | **int**| ID of package-line to return | 
 **include_package_line_status** | **bool**| Show the text value of the status | [default to true]
 **include_package_line_type_name** | **bool**| Show the text value of the package-line type | [default to true]
 **include_package_line_meta_data** | **bool**| Include meta data connected to this PackageLine | [default to true]
 **include_address_object** | **bool**| Include address data | [default to true]
 **include_time_slots** | **bool**| Include TimeSlots | [default to true]
 **include_time_slot_tags** | **bool**| Include tags from TimeSlots | [default to true]
 **include_route_info** | **bool**| Include route data | [default to true]
 **include_driver_info** | **bool**| Include driver data | [default to true]
 **include_communication** | **bool**| Include Communication Settings | [default to true]
 **include_package_line_links** | **bool**| Include Link Data | [default to true]
 **include_package_lines_info** | **bool**| Include PackageLines | [default to true]
 **include_package_line_files** | **bool**| Include files | [default to true]
 **include_package_line_files_meta_data** | **bool**| Include files meta data | [default to true]

### Return type

[**PackageLineModel**](PackageLineModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_package_line**
> ApiResponse set_package_line(body=body)

Set (create or update) an PackageLine

Set (create or update) an PackageLine. If id or links are set in the data, and a corresponding package-line is found in Bumbal, an update will be performed.

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
api_instance = bumbal.PackageLineApi(bumbal.ApiClient(configuration))
body = bumbal.PackageLineModel() # PackageLineModel | PackageLine model (optional)

try:
    # Set (create or update) an PackageLine
    api_response = api_instance.set_package_line(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageLineApi->set_package_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PackageLineModel**](PackageLineModel.md)| PackageLine model | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_package_line**
> ApiResponse update_package_line(body=body)

Update package-lines in bulk

Update package-lines in bulk

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
api_instance = bumbal.PackageLineApi(bumbal.ApiClient(configuration))
body = bumbal.PackageLineUpdateArguments() # PackageLineUpdateArguments | PackageLine Update object that contains all information about this update (optional)

try:
    # Update package-lines in bulk
    api_response = api_instance.update_package_line(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackageLineApi->update_package_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PackageLineUpdateArguments**](PackageLineUpdateArguments.md)| PackageLine Update object that contains all information about this update | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

