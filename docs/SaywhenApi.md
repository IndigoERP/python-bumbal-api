# bumbal.SaywhenApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**saywhen_retrieve_portal_ur_ls**](SaywhenApi.md#saywhen_retrieve_portal_ur_ls) | **PUT** /saywhen/retrieve-portal-urls | Retrieve SayWhen Portal URLs
[**saywhen_retrieve_portal_url**](SaywhenApi.md#saywhen_retrieve_portal_url) | **GET** /saywhen/retrieve-portal-url/{activityId} | Retrieve SayWhen Portal URL
[**saywhen_retrieve_status**](SaywhenApi.md#saywhen_retrieve_status) | **GET** /saywhen/retrieve-status/{activityId} | Retrieve SayWhen Status


# **saywhen_retrieve_portal_ur_ls**
> ApiResponse saywhen_retrieve_portal_ur_ls(arguments)

Retrieve SayWhen Portal URLs

Retrieve SayWhen Portal URLs

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
api_instance = bumbal.SaywhenApi(bumbal.ApiClient(configuration))
arguments = bumbal.SayWhenRetrievePortalURLsArguments() # SayWhenRetrievePortalURLsArguments | portal urls Arguments

try:
    # Retrieve SayWhen Portal URLs
    api_response = api_instance.saywhen_retrieve_portal_ur_ls(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaywhenApi->saywhen_retrieve_portal_ur_ls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**SayWhenRetrievePortalURLsArguments**](SayWhenRetrievePortalURLsArguments.md)| portal urls Arguments | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **saywhen_retrieve_portal_url**
> ApiResponse saywhen_retrieve_portal_url(activity_id)

Retrieve SayWhen Portal URL

Retrieve SayWhen Portal URL

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
api_instance = bumbal.SaywhenApi(bumbal.ApiClient(configuration))
activity_id = 789 # int | ID of the activity to retrieve portal url for

try:
    # Retrieve SayWhen Portal URL
    api_response = api_instance.saywhen_retrieve_portal_url(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaywhenApi->saywhen_retrieve_portal_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| ID of the activity to retrieve portal url for | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **saywhen_retrieve_status**
> SayWhenVisitModel saywhen_retrieve_status(activity_id)

Retrieve SayWhen Status

Retrieve SayWhen Status

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
api_instance = bumbal.SaywhenApi(bumbal.ApiClient(configuration))
activity_id = 789 # int | ID of the activity to retrieve status for

try:
    # Retrieve SayWhen Status
    api_response = api_instance.saywhen_retrieve_status(activity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SaywhenApi->saywhen_retrieve_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_id** | **int**| ID of the activity to retrieve status for | 

### Return type

[**SayWhenVisitModel**](SayWhenVisitModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

