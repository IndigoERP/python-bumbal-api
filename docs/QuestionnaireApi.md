# bumbal.QuestionnaireApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_language**](QuestionnaireApi.md#change_language) | **POST** /questionnaire/change-language | change language of a Questionnaire
[**delete_questionnaire**](QuestionnaireApi.md#delete_questionnaire) | **DELETE** /questionnaire/{questionnaireId} | Delete an Questionnaire entry
[**get_next_question**](QuestionnaireApi.md#get_next_question) | **POST** /questionnaire/get-next-question | getNextQuestion of an Questionnaire
[**get_previous_question**](QuestionnaireApi.md#get_previous_question) | **POST** /questionnaire/get-previous-question | getPreviousQuestion of an Questionnaire
[**retrieve_list_questionnaire**](QuestionnaireApi.md#retrieve_list_questionnaire) | **PUT** /questionnaire | Retrieve List of Questionnaire
[**retrieve_questionnaire**](QuestionnaireApi.md#retrieve_questionnaire) | **GET** /questionnaire/{questionnaireId} | Retrieve a Questionnaire


# **change_language**
> QuestionnaireChangeLanguageResponse change_language(arguments)

change language of a Questionnaire

change language of a Questionnaire

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
api_instance = bumbal.QuestionnaireApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireChangeLanguageArguments() # QuestionnaireChangeLanguageArguments | Request Arguments

try:
    # change language of a Questionnaire
    api_response = api_instance.change_language(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireApi->change_language: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireChangeLanguageArguments**](QuestionnaireChangeLanguageArguments.md)| Request Arguments | 

### Return type

[**QuestionnaireChangeLanguageResponse**](QuestionnaireChangeLanguageResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_questionnaire**
> ApiResponse27 delete_questionnaire(notification_id)

Delete an Questionnaire entry

Delete an Questionnaire entry

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
api_instance = bumbal.QuestionnaireApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of Questionnaire to delete

try:
    # Delete an Questionnaire entry
    api_response = api_instance.delete_questionnaire(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireApi->delete_questionnaire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of Questionnaire to delete | 

### Return type

[**ApiResponse27**](ApiResponse27.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_next_question**
> QuestionnaireQuestionModel get_next_question(arguments)

getNextQuestion of an Questionnaire

getNextQuestion of an Questionnaire

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
api_instance = bumbal.QuestionnaireApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireGetNextQuestionArguments() # QuestionnaireGetNextQuestionArguments | Request Arguments

try:
    # getNextQuestion of an Questionnaire
    api_response = api_instance.get_next_question(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireApi->get_next_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireGetNextQuestionArguments**](QuestionnaireGetNextQuestionArguments.md)| Request Arguments | 

### Return type

[**QuestionnaireQuestionModel**](QuestionnaireQuestionModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_previous_question**
> QuestionnaireQuestionModel get_previous_question(arguments)

getPreviousQuestion of an Questionnaire

getPreviousQuestion of an Questionnaire

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
api_instance = bumbal.QuestionnaireApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireGetPreviousQuestionArguments() # QuestionnaireGetPreviousQuestionArguments | Request Arguments

try:
    # getPreviousQuestion of an Questionnaire
    api_response = api_instance.get_previous_question(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireApi->get_previous_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireGetPreviousQuestionArguments**](QuestionnaireGetPreviousQuestionArguments.md)| Request Arguments | 

### Return type

[**QuestionnaireQuestionModel**](QuestionnaireQuestionModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_questionnaire**
> QuestionnaireListResponse retrieve_list_questionnaire(arguments)

Retrieve List of Questionnaire

Retrieve List of Questionnaire

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
api_instance = bumbal.QuestionnaireApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireRetrieveListArguments() # QuestionnaireRetrieveListArguments | Questionnaire RetrieveList Arguments

try:
    # Retrieve List of Questionnaire
    api_response = api_instance.retrieve_list_questionnaire(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireApi->retrieve_list_questionnaire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireRetrieveListArguments**](QuestionnaireRetrieveListArguments.md)| Questionnaire RetrieveList Arguments | 

### Return type

[**QuestionnaireListResponse**](QuestionnaireListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_questionnaire**
> QuestionnaireModel retrieve_questionnaire(notification_id, include_answers)

Retrieve a Questionnaire

Retrieve an Questionnaire

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
api_instance = bumbal.QuestionnaireApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of Questionnaire to retrieve
include_answers = true # bool | Include answers

try:
    # Retrieve a Questionnaire
    api_response = api_instance.retrieve_questionnaire(notification_id, include_answers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireApi->retrieve_questionnaire: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of Questionnaire to retrieve | 
 **include_answers** | **bool**| Include answers | 

### Return type

[**QuestionnaireModel**](QuestionnaireModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

