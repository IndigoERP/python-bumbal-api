# bumbal.UomApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_list_uom**](UomApi.md#retrieve_list_uom) | **PUT** /uom | Retrieve List of Uom&#39;s


# **retrieve_list_uom**
> UomListResponse retrieve_list_uom(arguments)

Retrieve List of Uom's

Retrieve List of Uom's

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
api_instance = bumbal.UomApi(bumbal.ApiClient(configuration))
arguments = bumbal.UomRetrieveListArguments() # UomRetrieveListArguments | Uom RetrieveList Arguments

try:
    # Retrieve List of Uom's
    api_response = api_instance.retrieve_list_uom(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UomApi->retrieve_list_uom: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**UomRetrieveListArguments**](UomRetrieveListArguments.md)| Uom RetrieveList Arguments | 

### Return type

[**UomListResponse**](UomListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

