# bumbal.QuestionnaireTemplateQuestionOptionApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_questionnaire_template_question_option**](QuestionnaireTemplateQuestionOptionApi.md#create_questionnaire_template_question_option) | **POST** /questionnaire-template-question-option | Add a new QuestionnaireTemplateQuestionOption
[**delete_questionnaire_template_question_option**](QuestionnaireTemplateQuestionOptionApi.md#delete_questionnaire_template_question_option) | **DELETE** /questionnaire-template-question-option/{questionnaire-template-question-optionId} | Delete an QuestionnaireTemplateQuestionOption entry
[**find_possible_follow_up_questions**](QuestionnaireTemplateQuestionOptionApi.md#find_possible_follow_up_questions) | **POST** /questionnaire-template-question-option/find-possible-followup-questions | find possible follow up questions
[**get_possible_follow_up_questions**](QuestionnaireTemplateQuestionOptionApi.md#get_possible_follow_up_questions) | **POST** /questionnaire-template-question-option/get-possible-followup-questions | get possible follow up questions
[**retrieve_list_questionnaire_template_question_option**](QuestionnaireTemplateQuestionOptionApi.md#retrieve_list_questionnaire_template_question_option) | **PUT** /questionnaire-template-question-option | Retrieve List of QuestionnaireTemplateQuestionOption
[**retrieve_questionnaire_template_question_option**](QuestionnaireTemplateQuestionOptionApi.md#retrieve_questionnaire_template_question_option) | **GET** /questionnaire-template-question-option/{questionnaire-template-question-optionId} | Retrieve a QuestionnaireTemplateQuestionOption
[**set_questionnaire_template_question_option**](QuestionnaireTemplateQuestionOptionApi.md#set_questionnaire_template_question_option) | **POST** /questionnaire-template-question-option/set | Set (create or update) a QuestionnaireTemplateQuestionOption
[**update_questionnaire_template_question_option**](QuestionnaireTemplateQuestionOptionApi.md#update_questionnaire_template_question_option) | **PUT** /questionnaire-template-question-option/{questionnaire-template-question-optionId} | Update a specific QuestionnaireTemplateQuestionOption object


# **create_questionnaire_template_question_option**
> ApiResponse42 create_questionnaire_template_question_option(body=body)

Add a new QuestionnaireTemplateQuestionOption

Add a new QuestionnaireTemplateQuestionOption

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateQuestionOptionModel() # QuestionnaireTemplateQuestionOptionModel | QuestionnaireTemplateQuestionOption object that needs to be created (optional)

try:
    # Add a new QuestionnaireTemplateQuestionOption
    api_response = api_instance.create_questionnaire_template_question_option(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionApi->create_questionnaire_template_question_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateQuestionOptionModel**](QuestionnaireTemplateQuestionOptionModel.md)| QuestionnaireTemplateQuestionOption object that needs to be created | [optional] 

### Return type

[**ApiResponse42**](ApiResponse42.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_questionnaire_template_question_option**
> ApiResponse40 delete_questionnaire_template_question_option(questionnaire_template_question_option_id)

Delete an QuestionnaireTemplateQuestionOption entry

Delete an QuestionnaireTemplateQuestionOption entry

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionApi(bumbal.ApiClient(configuration))
questionnaire_template_question_option_id = 789 # int | ID of QuestionnaireTemplateQuestionOption to delete

try:
    # Delete an QuestionnaireTemplateQuestionOption entry
    api_response = api_instance.delete_questionnaire_template_question_option(questionnaire_template_question_option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionApi->delete_questionnaire_template_question_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_template_question_option_id** | **int**| ID of QuestionnaireTemplateQuestionOption to delete | 

### Return type

[**ApiResponse40**](ApiResponse40.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_possible_follow_up_questions**
> ApiResponse44 find_possible_follow_up_questions(body=body)

find possible follow up questions

find possible follow up questions

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateQuestionOptionPossibleQuestionsModel() # QuestionnaireTemplateQuestionOptionPossibleQuestionsModel | QuestionnaireTemplate object that needs to be updated (optional)

try:
    # find possible follow up questions
    api_response = api_instance.find_possible_follow_up_questions(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionApi->find_possible_follow_up_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateQuestionOptionPossibleQuestionsModel**](QuestionnaireTemplateQuestionOptionPossibleQuestionsModel.md)| QuestionnaireTemplate object that needs to be updated | [optional] 

### Return type

[**ApiResponse44**](ApiResponse44.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_possible_follow_up_questions**
> ApiResponse40 get_possible_follow_up_questions(questionnaire_template_question_id)

get possible follow up questions

get possible follow up questions

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionApi(bumbal.ApiClient(configuration))
questionnaire_template_question_id = 789 # int | ID of QuestionnaireTemplateQuestion

try:
    # get possible follow up questions
    api_response = api_instance.get_possible_follow_up_questions(questionnaire_template_question_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionApi->get_possible_follow_up_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_template_question_id** | **int**| ID of QuestionnaireTemplateQuestion | 

### Return type

[**ApiResponse40**](ApiResponse40.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_questionnaire_template_question_option**
> QuestionnaireTemplateQuestionOptionListResponse retrieve_list_questionnaire_template_question_option(arguments)

Retrieve List of QuestionnaireTemplateQuestionOption

Retrieve List of QuestionnaireTemplateQuestionOption

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireTemplateQuestionOptionRetrieveListArguments() # QuestionnaireTemplateQuestionOptionRetrieveListArguments | QuestionnaireTemplateQuestionOption RetrieveList Arguments

try:
    # Retrieve List of QuestionnaireTemplateQuestionOption
    api_response = api_instance.retrieve_list_questionnaire_template_question_option(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionApi->retrieve_list_questionnaire_template_question_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireTemplateQuestionOptionRetrieveListArguments**](QuestionnaireTemplateQuestionOptionRetrieveListArguments.md)| QuestionnaireTemplateQuestionOption RetrieveList Arguments | 

### Return type

[**QuestionnaireTemplateQuestionOptionListResponse**](QuestionnaireTemplateQuestionOptionListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_questionnaire_template_question_option**
> QuestionnaireTemplateQuestionOptionModel retrieve_questionnaire_template_question_option(notification_id)

Retrieve a QuestionnaireTemplateQuestionOption

Retrieve an QuestionnaireTemplateQuestionOption

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of QuestionnaireTemplateQuestionOption to retrieve

try:
    # Retrieve a QuestionnaireTemplateQuestionOption
    api_response = api_instance.retrieve_questionnaire_template_question_option(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionApi->retrieve_questionnaire_template_question_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of QuestionnaireTemplateQuestionOption to retrieve | 

### Return type

[**QuestionnaireTemplateQuestionOptionModel**](QuestionnaireTemplateQuestionOptionModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_questionnaire_template_question_option**
> ApiResponse set_questionnaire_template_question_option(body=body)

Set (create or update) a QuestionnaireTemplateQuestionOption

Set (create or update) a d=QuestionnaireTemplateQuestionOption. If id or links are set in the data, and a corresponding QuestionnaireTemplateQuestionOption is found in Bumbal, an update will be performed.

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateQuestionOptionModel() # QuestionnaireTemplateQuestionOptionModel | QuestionnaireTemplateQuestionOption object (optional)

try:
    # Set (create or update) a QuestionnaireTemplateQuestionOption
    api_response = api_instance.set_questionnaire_template_question_option(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionApi->set_questionnaire_template_question_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateQuestionOptionModel**](QuestionnaireTemplateQuestionOptionModel.md)| QuestionnaireTemplateQuestionOption object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_questionnaire_template_question_option**
> ApiResponse39 update_questionnaire_template_question_option(notification_id, body=body)

Update a specific QuestionnaireTemplateQuestionOption object

Update a specific QuestionnaireTemplateQuestionOption object

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of the QuestionnaireTemplateQuestionOption object to update
body = bumbal.QuestionnaireTemplateQuestionOptionModel() # QuestionnaireTemplateQuestionOptionModel | QuestionnaireTemplateQuestionOption object that needs to be updated (optional)

try:
    # Update a specific QuestionnaireTemplateQuestionOption object
    api_response = api_instance.update_questionnaire_template_question_option(notification_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionApi->update_questionnaire_template_question_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of the QuestionnaireTemplateQuestionOption object to update | 
 **body** | [**QuestionnaireTemplateQuestionOptionModel**](QuestionnaireTemplateQuestionOptionModel.md)| QuestionnaireTemplateQuestionOption object that needs to be updated | [optional] 

### Return type

[**ApiResponse39**](ApiResponse39.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

