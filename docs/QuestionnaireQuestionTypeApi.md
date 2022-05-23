# bumbal.QuestionnaireQuestionTypeApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_list_questionnaire_question_type**](QuestionnaireQuestionTypeApi.md#retrieve_list_questionnaire_question_type) | **PUT** /questionnaire-question-type | Retrieve List of QuestionnaireQuestionType
[**retrieve_questionnaire_question_type**](QuestionnaireQuestionTypeApi.md#retrieve_questionnaire_question_type) | **GET** /questionnaire-question-type/{questionnaire-question-typeId} | Retrieve a QuestionnaireQuestionType


# **retrieve_list_questionnaire_question_type**
> QuestionnaireQuestionTypeListResponse retrieve_list_questionnaire_question_type(arguments)

Retrieve List of QuestionnaireQuestionType

Retrieve List of QuestionnaireQuestionType

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
api_instance = bumbal.QuestionnaireQuestionTypeApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireQuestionTypeRetrieveListArguments() # QuestionnaireQuestionTypeRetrieveListArguments | QuestionnaireQuestionType RetrieveList Arguments

try:
    # Retrieve List of QuestionnaireQuestionType
    api_response = api_instance.retrieve_list_questionnaire_question_type(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireQuestionTypeApi->retrieve_list_questionnaire_question_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireQuestionTypeRetrieveListArguments**](QuestionnaireQuestionTypeRetrieveListArguments.md)| QuestionnaireQuestionType RetrieveList Arguments | 

### Return type

[**QuestionnaireQuestionTypeListResponse**](QuestionnaireQuestionTypeListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_questionnaire_question_type**
> QuestionnaireQuestionTypeModel retrieve_questionnaire_question_type(notification_id)

Retrieve a QuestionnaireQuestionType

Retrieve an QuestionnaireQuestionType

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
api_instance = bumbal.QuestionnaireQuestionTypeApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of QuestionnaireQuestionType to retrieve

try:
    # Retrieve a QuestionnaireQuestionType
    api_response = api_instance.retrieve_questionnaire_question_type(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireQuestionTypeApi->retrieve_questionnaire_question_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of QuestionnaireQuestionType to retrieve | 

### Return type

[**QuestionnaireQuestionTypeModel**](QuestionnaireQuestionTypeModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

