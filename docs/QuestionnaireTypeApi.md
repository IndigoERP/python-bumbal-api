# bumbal.QuestionnaireTypeApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_list_questionnaire_type**](QuestionnaireTypeApi.md#retrieve_list_questionnaire_type) | **PUT** /questionnaire-type | Retrieve List of QuestionnaireType
[**retrieve_questionnaire_type**](QuestionnaireTypeApi.md#retrieve_questionnaire_type) | **GET** /questionnaire-type/{questionnaire-typeId} | Retrieve a QuestionnaireType


# **retrieve_list_questionnaire_type**
> QuestionnaireTypeListResponse retrieve_list_questionnaire_type(arguments)

Retrieve List of QuestionnaireType

Retrieve List of QuestionnaireType

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
api_instance = bumbal.QuestionnaireTypeApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireTypeRetrieveListArguments() # QuestionnaireTypeRetrieveListArguments | QuestionnaireType RetrieveList Arguments

try:
    # Retrieve List of QuestionnaireType
    api_response = api_instance.retrieve_list_questionnaire_type(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTypeApi->retrieve_list_questionnaire_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireTypeRetrieveListArguments**](QuestionnaireTypeRetrieveListArguments.md)| QuestionnaireType RetrieveList Arguments | 

### Return type

[**QuestionnaireTypeListResponse**](QuestionnaireTypeListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_questionnaire_type**
> QuestionnaireTypeModel retrieve_questionnaire_type(notification_id)

Retrieve a QuestionnaireType

Retrieve an QuestionnaireType

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
api_instance = bumbal.QuestionnaireTypeApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of QuestionnaireType to retrieve

try:
    # Retrieve a QuestionnaireType
    api_response = api_instance.retrieve_questionnaire_type(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTypeApi->retrieve_questionnaire_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of QuestionnaireType to retrieve | 

### Return type

[**QuestionnaireTypeModel**](QuestionnaireTypeModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

