# bumbal.WebhookApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_web_hook**](WebhookApi.md#trigger_web_hook) | **POST** /web-hook/trigger | Trigger a webhook


# **trigger_web_hook**
> ApiResponse trigger_web_hook(object_id, web_hook_name, extra_payload=extra_payload)

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
api_instance = bumbal.WebhookApi(bumbal.ApiClient(configuration))
object_id = 56 # int | objectId
web_hook_name = ['web_hook_name_example'] # list[str] | Name of this Web Hook
extra_payload = [bumbal.PayloadItem()] # list[PayloadItem] | extra payload to be sent when the webhook is triggered (optional)

try:
    # Trigger a webhook
    api_response = api_instance.trigger_web_hook(object_id, web_hook_name, extra_payload=extra_payload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhookApi->trigger_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_id** | **int**| objectId | 
 **web_hook_name** | [**list[str]**](str.md)| Name of this Web Hook | 
 **extra_payload** | [**list[PayloadItem]**](PayloadItem.md)| extra payload to be sent when the webhook is triggered | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

