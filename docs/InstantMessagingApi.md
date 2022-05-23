# bumbal.InstantMessagingApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instant_messaging_list**](InstantMessagingApi.md#instant_messaging_list) | **POST** /instant-messaging/list | List conversations
[**instant_messaging_post**](InstantMessagingApi.md#instant_messaging_post) | **POST** /instant-messaging/post | Post a message to some one
[**instant_messaging_retrieve_conversation**](InstantMessagingApi.md#instant_messaging_retrieve_conversation) | **POST** /instant-messaging/retrieve-conversation | Retrieve Conversation


# **instant_messaging_list**
> ApiResponse instant_messaging_list()

List conversations

List conversations

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
api_instance = bumbal.InstantMessagingApi(bumbal.ApiClient(configuration))

try:
    # List conversations
    api_response = api_instance.instant_messaging_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMessagingApi->instant_messaging_list: %s\n" % e)
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

# **instant_messaging_post**
> ApiResponse instant_messaging_post()

Post a message to some one

Post a message to some one

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
api_instance = bumbal.InstantMessagingApi(bumbal.ApiClient(configuration))

try:
    # Post a message to some one
    api_response = api_instance.instant_messaging_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMessagingApi->instant_messaging_post: %s\n" % e)
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

# **instant_messaging_retrieve_conversation**
> ApiResponse instant_messaging_retrieve_conversation()

Retrieve Conversation

Retrieve Conversation

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
api_instance = bumbal.InstantMessagingApi(bumbal.ApiClient(configuration))

try:
    # Retrieve Conversation
    api_response = api_instance.instant_messaging_retrieve_conversation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstantMessagingApi->instant_messaging_retrieve_conversation: %s\n" % e)
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

