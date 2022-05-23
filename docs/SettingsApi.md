# bumbal.SettingsApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_constants**](SettingsApi.md#get_constants) | **GET** /settings/get-constants | getConstants, returns in structure &#39;string&#39;:&#39;string&#39;, can contain rounding errors for floating points
[**get_constants_reversed**](SettingsApi.md#get_constants_reversed) | **GET** /settings/get-constants-reversed | getConstantsReversed, returns in structure &#39;string&#39;:int/float
[**retrieve_list_settings**](SettingsApi.md#retrieve_list_settings) | **PUT** /settings | Retrieve List of Settings
[**retrieve_settings**](SettingsApi.md#retrieve_settings) | **GET** /settings/{settingsId} | Retrieve a Settings
[**set_setting**](SettingsApi.md#set_setting) | **POST** /settings/set | Set (update) Setting value
[**update_settings**](SettingsApi.md#update_settings) | **PUT** /settings/{settingsId} | Update a Settings


# **get_constants**
> SettingsGetConstantsResponse get_constants()

getConstants, returns in structure 'string':'string', can contain rounding errors for floating points

getConstants, returns in structure 'string':'string', can contain rounding errors for floating points, use the reversed function for correct floating points

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
api_instance = bumbal.SettingsApi(bumbal.ApiClient(configuration))

try:
    # getConstants, returns in structure 'string':'string', can contain rounding errors for floating points
    api_response = api_instance.get_constants()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_constants: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsGetConstantsResponse**](SettingsGetConstantsResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_constants_reversed**
> SettingsGetConstantsReversedResponse get_constants_reversed()

getConstantsReversed, returns in structure 'string':int/float

getConstantsReversed, returns in structure 'string':int/float

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
api_instance = bumbal.SettingsApi(bumbal.ApiClient(configuration))

try:
    # getConstantsReversed, returns in structure 'string':int/float
    api_response = api_instance.get_constants_reversed()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_constants_reversed: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsGetConstantsReversedResponse**](SettingsGetConstantsReversedResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_settings**
> list[SettingsModel] retrieve_list_settings(arguments)

Retrieve List of Settings

Retrieve List of Settings

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
api_instance = bumbal.SettingsApi(bumbal.ApiClient(configuration))
arguments = bumbal.SettingsRetrieveListArguments() # SettingsRetrieveListArguments | Settings RetrieveList Arguments

try:
    # Retrieve List of Settings
    api_response = api_instance.retrieve_list_settings(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->retrieve_list_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**SettingsRetrieveListArguments**](SettingsRetrieveListArguments.md)| Settings RetrieveList Arguments | 

### Return type

[**list[SettingsModel]**](SettingsModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_settings**
> SettingsModel retrieve_settings(settings_id)

Retrieve a Settings

Retrieve an Settings

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
api_instance = bumbal.SettingsApi(bumbal.ApiClient(configuration))
settings_id = 789 # int | ID of settings to retrieve

try:
    # Retrieve a Settings
    api_response = api_instance.retrieve_settings(settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->retrieve_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_id** | **int**| ID of settings to retrieve | 

### Return type

[**SettingsModel**](SettingsModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_setting**
> ApiResponse set_setting(body=body)

Set (update) Setting value

Set (update) Setting value. If no id or key are set in the data, corresponding to one of teh Bumbal settings, no update can be performed.

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
api_instance = bumbal.SettingsApi(bumbal.ApiClient(configuration))
body = bumbal.SettingsModel() # SettingsModel | Setting object (optional)

try:
    # Set (update) Setting value
    api_response = api_instance.set_setting(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->set_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SettingsModel**](SettingsModel.md)| Setting object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings**
> ApiResponse update_settings(settings_id)

Update a Settings

Update a Setting

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
api_instance = bumbal.SettingsApi(bumbal.ApiClient(configuration))
settings_id = 789 # int | ID of settings to update

try:
    # Update a Settings
    api_response = api_instance.update_settings(settings_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_id** | **int**| ID of settings to update | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

