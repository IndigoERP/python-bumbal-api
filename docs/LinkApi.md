# bumbal.LinkApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_link**](LinkApi.md#delete_link) | **DELETE** /link/{linkId} | Delete a link
[**retrieve_list_link**](LinkApi.md#retrieve_list_link) | **PUT** /link | Retrieve List of Links
[**update_link**](LinkApi.md#update_link) | **PUT** /link/{linkId} | Update a specific link object


# **delete_link**
> ApiResponse delete_link(driver_id)

Delete a link

Delete a link

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
api_instance = bumbal.LinkApi(bumbal.ApiClient(configuration))
driver_id = 789 # int | ID of the link to delete

try:
    # Delete a link
    api_response = api_instance.delete_link(driver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkApi->delete_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **driver_id** | **int**| ID of the link to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_link**
> list[LinkListResponse] retrieve_list_link(arguments)

Retrieve List of Links

Retrieve List of Links

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
api_instance = bumbal.LinkApi(bumbal.ApiClient(configuration))
arguments = bumbal.LinkRetrieveListArguments() # LinkRetrieveListArguments | Link RetrieveList Arguments

try:
    # Retrieve List of Links
    api_response = api_instance.retrieve_list_link(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkApi->retrieve_list_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**LinkRetrieveListArguments**](LinkRetrieveListArguments.md)| Link RetrieveList Arguments | 

### Return type

[**list[LinkListResponse]**](LinkListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_link**
> ApiResponse update_link(link_id, body=body)

Update a specific link object

Update a specific link object

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
api_instance = bumbal.LinkApi(bumbal.ApiClient(configuration))
link_id = 789 # int | ID of the link object to update
body = bumbal.LinkModel() # LinkModel | Link object that needs to be updated (optional)

try:
    # Update a specific link object
    api_response = api_instance.update_link(link_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkApi->update_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_id** | **int**| ID of the link object to update | 
 **body** | [**LinkModel**](LinkModel.md)| Link object that needs to be updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

