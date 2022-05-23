# bumbal.SystemApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_get_config**](SystemApi.md#system_get_config) | **GET** /system/get-config | Retrieve System Configuration
[**system_get_say_when_config**](SystemApi.md#system_get_say_when_config) | **GET** /system/get-say-when-config | Retrieve SayWhen System Configuration
[**system_get_variables**](SystemApi.md#system_get_variables) | **GET** /system/get-variables | Retrieve System Variables


# **system_get_config**
> ConfigModel system_get_config()

Retrieve System Configuration

Retrieve System Configuration

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
api_instance = bumbal.SystemApi(bumbal.ApiClient(configuration))

try:
    # Retrieve System Configuration
    api_response = api_instance.system_get_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigModel**](ConfigModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_say_when_config**
> SayWhenConfigModel system_get_say_when_config()

Retrieve SayWhen System Configuration

Retrieve SayWhen System Configuration

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
api_instance = bumbal.SystemApi(bumbal.ApiClient(configuration))

try:
    # Retrieve SayWhen System Configuration
    api_response = api_instance.system_get_say_when_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_say_when_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SayWhenConfigModel**](SayWhenConfigModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_variables**
> VariablesModel system_get_variables()

Retrieve System Variables

Retrieve System Variables

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
api_instance = bumbal.SystemApi(bumbal.ApiClient(configuration))

try:
    # Retrieve System Variables
    api_response = api_instance.system_get_variables()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_get_variables: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VariablesModel**](VariablesModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

