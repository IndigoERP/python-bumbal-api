# bumbal.QuestionnaireTemplateQuestionApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_questionnaire_template_question**](QuestionnaireTemplateQuestionApi.md#create_questionnaire_template_question) | **POST** /questionnaire-template-question | Add a new QuestionnaireTemplateQuestion
[**delete_questionnaire_template_question**](QuestionnaireTemplateQuestionApi.md#delete_questionnaire_template_question) | **DELETE** /questionnaire-template-question/{questionnaireTemplateQuestionId} | Delete an QuestionnaireTemplateQuestion entry
[**retrieve_list_questionnaire_template_question**](QuestionnaireTemplateQuestionApi.md#retrieve_list_questionnaire_template_question) | **PUT** /questionnaire-template-question | Retrieve List of QuestionnaireTemplateQuestion
[**retrieve_questionnaire_template_question**](QuestionnaireTemplateQuestionApi.md#retrieve_questionnaire_template_question) | **GET** /questionnaire-template-question/{questionnaireTemplateQuestionId} | Retrieve a QuestionnaireTemplateQuestion
[**set_questionnaire_template_question**](QuestionnaireTemplateQuestionApi.md#set_questionnaire_template_question) | **POST** /questionnaire-template-question/set | Set (create or update) a QuestionnaireTemplateQuestion
[**update_questionnaire_template_question**](QuestionnaireTemplateQuestionApi.md#update_questionnaire_template_question) | **PUT** /questionnaire-template-question/{questionnaireTemplateQuestionId} | Update a specific QuestionnaireTemplateQuestion object


# **create_questionnaire_template_question**
> ApiResponse38 create_questionnaire_template_question(body=body)

Add a new QuestionnaireTemplateQuestion

Add a new QuestionnaireTemplateQuestion

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
api_instance = bumbal.QuestionnaireTemplateQuestionApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateQuestionModel() # QuestionnaireTemplateQuestionModel | QuestionnaireTemplateQuestion object that needs to be created (optional)

try:
    # Add a new QuestionnaireTemplateQuestion
    api_response = api_instance.create_questionnaire_template_question(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionApi->create_questionnaire_template_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateQuestionModel**](QuestionnaireTemplateQuestionModel.md)| QuestionnaireTemplateQuestion object that needs to be created | [optional] 

### Return type

[**ApiResponse38**](ApiResponse38.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_questionnaire_template_question**
> ApiResponse36 delete_questionnaire_template_question(questionnaire_template_question_id)

Delete an QuestionnaireTemplateQuestion entry

Delete an QuestionnaireTemplateQuestion entry

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
api_instance = bumbal.QuestionnaireTemplateQuestionApi(bumbal.ApiClient(configuration))
questionnaire_template_question_id = 789 # int | ID of QuestionnaireTemplateQuestion to delete

try:
    # Delete an QuestionnaireTemplateQuestion entry
    api_response = api_instance.delete_questionnaire_template_question(questionnaire_template_question_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionApi->delete_questionnaire_template_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_template_question_id** | **int**| ID of QuestionnaireTemplateQuestion to delete | 

### Return type

[**ApiResponse36**](ApiResponse36.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_questionnaire_template_question**
> QuestionnaireTemplateQuestionListResponse retrieve_list_questionnaire_template_question(arguments)

Retrieve List of QuestionnaireTemplateQuestion

Retrieve List of QuestionnaireTemplateQuestion

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
api_instance = bumbal.QuestionnaireTemplateQuestionApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireTemplateQuestionRetrieveListArguments() # QuestionnaireTemplateQuestionRetrieveListArguments | QuestionnaireTemplateQuestion RetrieveList Arguments

try:
    # Retrieve List of QuestionnaireTemplateQuestion
    api_response = api_instance.retrieve_list_questionnaire_template_question(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionApi->retrieve_list_questionnaire_template_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireTemplateQuestionRetrieveListArguments**](QuestionnaireTemplateQuestionRetrieveListArguments.md)| QuestionnaireTemplateQuestion RetrieveList Arguments | 

### Return type

[**QuestionnaireTemplateQuestionListResponse**](QuestionnaireTemplateQuestionListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_questionnaire_template_question**
> QuestionnaireTemplateQuestionModel retrieve_questionnaire_template_question(questionnaire_template_question_id)

Retrieve a QuestionnaireTemplateQuestion

Retrieve an QuestionnaireTemplateQuestion

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
api_instance = bumbal.QuestionnaireTemplateQuestionApi(bumbal.ApiClient(configuration))
questionnaire_template_question_id = 789 # int | ID of QuestionnaireTemplateQuestion to retrieve

try:
    # Retrieve a QuestionnaireTemplateQuestion
    api_response = api_instance.retrieve_questionnaire_template_question(questionnaire_template_question_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionApi->retrieve_questionnaire_template_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_template_question_id** | **int**| ID of QuestionnaireTemplateQuestion to retrieve | 

### Return type

[**QuestionnaireTemplateQuestionModel**](QuestionnaireTemplateQuestionModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_questionnaire_template_question**
> ApiResponse set_questionnaire_template_question(body=body)

Set (create or update) a QuestionnaireTemplateQuestion

Set (create or update) a d=QuestionnaireTemplateQuestion. If id or links are set in the data, and a corresponding QuestionnaireTemplateQuestion is found in Bumbal, an update will be performed.

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
api_instance = bumbal.QuestionnaireTemplateQuestionApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateQuestionModel() # QuestionnaireTemplateQuestionModel | QuestionnaireTemplateQuestion object (optional)

try:
    # Set (create or update) a QuestionnaireTemplateQuestion
    api_response = api_instance.set_questionnaire_template_question(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionApi->set_questionnaire_template_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateQuestionModel**](QuestionnaireTemplateQuestionModel.md)| QuestionnaireTemplateQuestion object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_questionnaire_template_question**
> ApiResponse35 update_questionnaire_template_question(questionnaire_template_question_id, body=body)

Update a specific QuestionnaireTemplateQuestion object

Update a specific QuestionnaireTemplateQuestion object

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
api_instance = bumbal.QuestionnaireTemplateQuestionApi(bumbal.ApiClient(configuration))
questionnaire_template_question_id = 789 # int | ID of the QuestionnaireTemplateQuestion object to update
body = bumbal.QuestionnaireTemplateQuestionModel() # QuestionnaireTemplateQuestionModel | QuestionnaireTemplateQuestion object that needs to be updated (optional)

try:
    # Update a specific QuestionnaireTemplateQuestion object
    api_response = api_instance.update_questionnaire_template_question(questionnaire_template_question_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionApi->update_questionnaire_template_question: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_template_question_id** | **int**| ID of the QuestionnaireTemplateQuestion object to update | 
 **body** | [**QuestionnaireTemplateQuestionModel**](QuestionnaireTemplateQuestionModel.md)| QuestionnaireTemplateQuestion object that needs to be updated | [optional] 

### Return type

[**ApiResponse35**](ApiResponse35.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

