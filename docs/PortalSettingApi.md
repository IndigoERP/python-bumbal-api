# bumbal.PortalSettingApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_portal_setting**](PortalSettingApi.md#create_portal_setting) | **POST** /portal-setting | Add a new PortalSetting
[**delete_portal_setting**](PortalSettingApi.md#delete_portal_setting) | **DELETE** /portal-setting/{portal-settingId} | Delete a PortalSetting
[**retrieve_list_portal_setting**](PortalSettingApi.md#retrieve_list_portal_setting) | **PUT** /portal-setting | Retrieve List of Portal Settings
[**retrieve_portal_setting**](PortalSettingApi.md#retrieve_portal_setting) | **GET** /portal-setting/{portal-settingId} | Retrieve a PortalSetting
[**set_portal_setting**](PortalSettingApi.md#set_portal_setting) | **POST** /portal-setting/set | Set (create or update) a PortalSetting
[**update_portal_setting**](PortalSettingApi.md#update_portal_setting) | **PUT** /portal-setting/{portal-settingId} | Update a PortalSetting


# **create_portal_setting**
> ApiResponse create_portal_setting(body=body)

Add a new PortalSetting

Add a new PortalSetting

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
api_instance = bumbal.PortalSettingApi(bumbal.ApiClient(configuration))
body = bumbal.PortalSettingModel() # PortalSettingModel | PortalSetting object that needs to be created (optional)

try:
    # Add a new PortalSetting
    api_response = api_instance.create_portal_setting(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalSettingApi->create_portal_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortalSettingModel**](PortalSettingModel.md)| PortalSetting object that needs to be created | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portal_setting**
> ApiResponse delete_portal_setting(portal_setting_id)

Delete a PortalSetting

Delete a PortalSetting

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
api_instance = bumbal.PortalSettingApi(bumbal.ApiClient(configuration))
portal_setting_id = 789 # int | ID of portal-setting to delete

try:
    # Delete a PortalSetting
    api_response = api_instance.delete_portal_setting(portal_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalSettingApi->delete_portal_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_setting_id** | **int**| ID of portal-setting to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_portal_setting**
> PortalSettingListResponse retrieve_list_portal_setting(arguments)

Retrieve List of Portal Settings

Retrieve List of Portal Settings

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
api_instance = bumbal.PortalSettingApi(bumbal.ApiClient(configuration))
arguments = bumbal.PortalSettingRetrieveListArguments() # PortalSettingRetrieveListArguments | PortalSetting RetrieveList Arguments

try:
    # Retrieve List of Portal Settings
    api_response = api_instance.retrieve_list_portal_setting(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalSettingApi->retrieve_list_portal_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**PortalSettingRetrieveListArguments**](PortalSettingRetrieveListArguments.md)| PortalSetting RetrieveList Arguments | 

### Return type

[**PortalSettingListResponse**](PortalSettingListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_portal_setting**
> PortalSettingModel retrieve_portal_setting(portal_setting_id)

Retrieve a PortalSetting

Retrieve an PortalSetting

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
api_instance = bumbal.PortalSettingApi(bumbal.ApiClient(configuration))
portal_setting_id = 789 # int | ID of portal-setting to retrieve

try:
    # Retrieve a PortalSetting
    api_response = api_instance.retrieve_portal_setting(portal_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalSettingApi->retrieve_portal_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_setting_id** | **int**| ID of portal-setting to retrieve | 

### Return type

[**PortalSettingModel**](PortalSettingModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_portal_setting**
> ApiResponse set_portal_setting(body=body)

Set (create or update) a PortalSetting

Set (create or update) a PortalSetting. If id or links are set in the data, and a corresponding portal-setting is found in Bumbal, an update will be performed.

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
api_instance = bumbal.PortalSettingApi(bumbal.ApiClient(configuration))
body = bumbal.PortalSettingModel() # PortalSettingModel | PortalSetting object (optional)

try:
    # Set (create or update) a PortalSetting
    api_response = api_instance.set_portal_setting(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalSettingApi->set_portal_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PortalSettingModel**](PortalSettingModel.md)| PortalSetting object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portal_setting**
> ApiResponse update_portal_setting(portal_setting_id)

Update a PortalSetting

Update an PortalSetting

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
api_instance = bumbal.PortalSettingApi(bumbal.ApiClient(configuration))
portal_setting_id = 789 # int | ID of portal-setting to update

try:
    # Update a PortalSetting
    api_response = api_instance.update_portal_setting(portal_setting_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortalSettingApi->update_portal_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portal_setting_id** | **int**| ID of portal-setting to update | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

