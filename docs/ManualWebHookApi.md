# bumbal.ManualWebHookApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**manual_web_hook_trigger**](ManualWebHookApi.md#manual_web_hook_trigger) | **POST** /manual-web-hook/trigger | Trigger a webhook


# **manual_web_hook_trigger**
> ApiResponse manual_web_hook_trigger(body=body)

Trigger a webhook

Manually trigger a webhook

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
api_instance = bumbal.ManualWebHookApi(bumbal.ApiClient(configuration))
body = bumbal.ManualWebHookModel() # ManualWebHookModel | WebHook that has to be triggered manually (optional)

try:
    # Trigger a webhook
    api_response = api_instance.manual_web_hook_trigger(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManualWebHookApi->manual_web_hook_trigger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ManualWebHookModel**](ManualWebHookModel.md)| WebHook that has to be triggered manually | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

