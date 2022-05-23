# bumbal.LanguageApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_list_language**](LanguageApi.md#retrieve_list_language) | **PUT** /language | Retrieve List of Language


# **retrieve_list_language**
> LanguageListResponse retrieve_list_language(arguments)

Retrieve List of Language

Retrieve List of Language

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
api_instance = bumbal.LanguageApi(bumbal.ApiClient(configuration))
arguments = bumbal.LanguageRetrieveListArguments() # LanguageRetrieveListArguments | Language RetrieveList Arguments

try:
    # Retrieve List of Language
    api_response = api_instance.retrieve_list_language(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguageApi->retrieve_list_language: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**LanguageRetrieveListArguments**](LanguageRetrieveListArguments.md)| Language RetrieveList Arguments | 

### Return type

[**LanguageListResponse**](LanguageListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

