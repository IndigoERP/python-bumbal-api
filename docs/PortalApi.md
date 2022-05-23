# bumbal.PortalApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_portal**](PortalApi.md#create_portal) | **POST** /portal | Add a new Portal
[**delete_portal**](PortalApi.md#delete_portal) | **DELETE** /portal/{portalId} | Delete a Portal
[**retrieve_list_portal**](PortalApi.md#retrieve_list_portal) | **PUT** /portal | Retrieve List of Portals
[**retrieve_portal**](PortalApi.md#retrieve_portal) | **GET** /portal/{portalId} | Retrieve a Portal
[**set_portal**](PortalApi.md#set_portal) | **POST** /portal/set | Set (create or update) a Portal
[**update_portal**](PortalApi.md#update_portal) | **PUT** /portal/{portalId} | Update a Portal


# **create_portal**
> ApiResponse create_portal(body=body)

Add a new Portal

Add a new Portal

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
api_instance = bumbal.PortalApi(bumbal.ApiClient(configuration))
body = bumbal.PortalModel() # PortalModel | Portal object that needs to be created (optional)

try:
    # Add a new Portal
    api_response = api_instance.create_portal(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->create_portal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortalModel**](PortalModel.md)| Portal object that needs to be created | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portal**
> ApiResponse delete_portal(portal_id)

Delete a Portal

Delete a Portal

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
api_instance = bumbal.PortalApi(bumbal.ApiClient(configuration))
portal_id = 789 # int | ID of portal to delete

try:
    # Delete a Portal
    api_response = api_instance.delete_portal(portal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->delete_portal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **int**| ID of portal to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_portal**
> PortalListResponse retrieve_list_portal(arguments)

Retrieve List of Portals

Retrieve List of Portals

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
api_instance = bumbal.PortalApi(bumbal.ApiClient(configuration))
arguments = bumbal.PortalRetrieveListArguments() # PortalRetrieveListArguments | Portal RetrieveList Arguments

try:
    # Retrieve List of Portals
    api_response = api_instance.retrieve_list_portal(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->retrieve_list_portal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**PortalRetrieveListArguments**](PortalRetrieveListArguments.md)| Portal RetrieveList Arguments | 

### Return type

[**PortalListResponse**](PortalListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_portal**
> PortalModel retrieve_portal(portal_id)

Retrieve a Portal

Retrieve an Portal

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
api_instance = bumbal.PortalApi(bumbal.ApiClient(configuration))
portal_id = 789 # int | ID of portal to retrieve

try:
    # Retrieve a Portal
    api_response = api_instance.retrieve_portal(portal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->retrieve_portal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **int**| ID of portal to retrieve | 

### Return type

[**PortalModel**](PortalModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_portal**
> ApiResponse set_portal(body=body)

Set (create or update) a Portal

Set (create or update) a Portal. If id or links are set in the data, and a corresponding portal is found in Bumbal, an update will be performed.

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
api_instance = bumbal.PortalApi(bumbal.ApiClient(configuration))
body = bumbal.PortalModel() # PortalModel | Portal object (optional)

try:
    # Set (create or update) a Portal
    api_response = api_instance.set_portal(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->set_portal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortalModel**](PortalModel.md)| Portal object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portal**
> ApiResponse update_portal(portal_id)

Update a Portal

Update an Portal

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
api_instance = bumbal.PortalApi(bumbal.ApiClient(configuration))
portal_id = 789 # int | ID of portal to update

try:
    # Update a Portal
    api_response = api_instance.update_portal(portal_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalApi->update_portal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_id** | **int**| ID of portal to update | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

