# bumbal.WorkerApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_action_to_worker_stack**](WorkerApi.md#add_action_to_worker_stack) | **POST** /worker/add-action-to-stack | Add Action To Worker Stack


# **add_action_to_worker_stack**
> ApiResponse add_action_to_worker_stack()

Add Action To Worker Stack

Add Action To Worker Stack

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
api_instance = bumbal.WorkerApi(bumbal.ApiClient(configuration))

try:
    # Add Action To Worker Stack
    api_response = api_instance.add_action_to_worker_stack()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkerApi->add_action_to_worker_stack: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

