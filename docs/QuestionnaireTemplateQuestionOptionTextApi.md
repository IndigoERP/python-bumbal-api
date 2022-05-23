# bumbal.QuestionnaireTemplateQuestionOptionTextApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_questionnaire_template_question_option_text**](QuestionnaireTemplateQuestionOptionTextApi.md#create_questionnaire_template_question_option_text) | **POST** /questionnaire-template-question-option-text | Add a new QuestionnaireTemplateQuestionOptionText
[**delete_questionnaire_template_question_option_text**](QuestionnaireTemplateQuestionOptionTextApi.md#delete_questionnaire_template_question_option_text) | **DELETE** /questionnaire-template-question-option-text/{questionnaire-template-question-option-textId} | Delete an QuestionnaireTemplateQuestionOptionText entry
[**retrieve_list_questionnaire_template_question_option_text**](QuestionnaireTemplateQuestionOptionTextApi.md#retrieve_list_questionnaire_template_question_option_text) | **PUT** /questionnaire-template-question-option-text | Retrieve List of QuestionnaireTemplateQuestionOptionText
[**retrieve_questionnaire_template_question_option_text**](QuestionnaireTemplateQuestionOptionTextApi.md#retrieve_questionnaire_template_question_option_text) | **GET** /questionnaire-template-question-option-text/{questionnaire-template-question-option-textId} | Retrieve a QuestionnaireTemplateQuestionOptionText
[**set_questionnaire_template_question_option_text**](QuestionnaireTemplateQuestionOptionTextApi.md#set_questionnaire_template_question_option_text) | **POST** /questionnaire-template-question-option-text/set | Set (create or update) a QuestionnaireTemplateQuestionOptionText
[**update_questionnaire_template_question_option_text**](QuestionnaireTemplateQuestionOptionTextApi.md#update_questionnaire_template_question_option_text) | **PUT** /questionnaire-template-question-option-text/{questionnaire-template-question-option-textId} | Update a specific QuestionnaireTemplateQuestionOptionText object


# **create_questionnaire_template_question_option_text**
> ApiResponse47 create_questionnaire_template_question_option_text(body=body)

Add a new QuestionnaireTemplateQuestionOptionText

Add a new QuestionnaireTemplateQuestionOptionText

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionTextApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateQuestionOptionTextModel() # QuestionnaireTemplateQuestionOptionTextModel | QuestionnaireTemplateQuestionOptionText object that needs to be created (optional)

try:
    # Add a new QuestionnaireTemplateQuestionOptionText
    api_response = api_instance.create_questionnaire_template_question_option_text(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionTextApi->create_questionnaire_template_question_option_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateQuestionOptionTextModel**](QuestionnaireTemplateQuestionOptionTextModel.md)| QuestionnaireTemplateQuestionOptionText object that needs to be created | [optional] 

### Return type

[**ApiResponse47**](ApiResponse47.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_questionnaire_template_question_option_text**
> ApiResponse46 delete_questionnaire_template_question_option_text(notification_id)

Delete an QuestionnaireTemplateQuestionOptionText entry

Delete an QuestionnaireTemplateQuestionOptionText entry

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionTextApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of QuestionnaireTemplateQuestionOptionText to delete

try:
    # Delete an QuestionnaireTemplateQuestionOptionText entry
    api_response = api_instance.delete_questionnaire_template_question_option_text(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionTextApi->delete_questionnaire_template_question_option_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of QuestionnaireTemplateQuestionOptionText to delete | 

### Return type

[**ApiResponse46**](ApiResponse46.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_questionnaire_template_question_option_text**
> QuestionnaireTemplateQuestionOptionTextListResponse retrieve_list_questionnaire_template_question_option_text(arguments)

Retrieve List of QuestionnaireTemplateQuestionOptionText

Retrieve List of QuestionnaireTemplateQuestionOptionText

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionTextApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireTemplateQuestionOptionTextRetrieveListArguments() # QuestionnaireTemplateQuestionOptionTextRetrieveListArguments | QuestionnaireTemplateQuestionOptionText RetrieveList Arguments

try:
    # Retrieve List of QuestionnaireTemplateQuestionOptionText
    api_response = api_instance.retrieve_list_questionnaire_template_question_option_text(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionTextApi->retrieve_list_questionnaire_template_question_option_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireTemplateQuestionOptionTextRetrieveListArguments**](QuestionnaireTemplateQuestionOptionTextRetrieveListArguments.md)| QuestionnaireTemplateQuestionOptionText RetrieveList Arguments | 

### Return type

[**QuestionnaireTemplateQuestionOptionTextListResponse**](QuestionnaireTemplateQuestionOptionTextListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_questionnaire_template_question_option_text**
> QuestionnaireTemplateQuestionOptionTextModel retrieve_questionnaire_template_question_option_text(notification_id)

Retrieve a QuestionnaireTemplateQuestionOptionText

Retrieve an QuestionnaireTemplateQuestionOptionText

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionTextApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of QuestionnaireTemplateQuestionOptionText to retrieve

try:
    # Retrieve a QuestionnaireTemplateQuestionOptionText
    api_response = api_instance.retrieve_questionnaire_template_question_option_text(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionTextApi->retrieve_questionnaire_template_question_option_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of QuestionnaireTemplateQuestionOptionText to retrieve | 

### Return type

[**QuestionnaireTemplateQuestionOptionTextModel**](QuestionnaireTemplateQuestionOptionTextModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_questionnaire_template_question_option_text**
> ApiResponse set_questionnaire_template_question_option_text(body=body)

Set (create or update) a QuestionnaireTemplateQuestionOptionText

Set (create or update) a d=QuestionnaireTemplateQuestionOptionText. If id or links are set in the data, and a corresponding QuestionnaireTemplateQuestionOptionText is found in Bumbal, an update will be performed.

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionTextApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateQuestionOptionTextModel() # QuestionnaireTemplateQuestionOptionTextModel | QuestionnaireTemplateQuestionOptionText object (optional)

try:
    # Set (create or update) a QuestionnaireTemplateQuestionOptionText
    api_response = api_instance.set_questionnaire_template_question_option_text(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionTextApi->set_questionnaire_template_question_option_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateQuestionOptionTextModel**](QuestionnaireTemplateQuestionOptionTextModel.md)| QuestionnaireTemplateQuestionOptionText object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_questionnaire_template_question_option_text**
> ApiResponse45 update_questionnaire_template_question_option_text(notification_id, body=body)

Update a specific QuestionnaireTemplateQuestionOptionText object

Update a specific QuestionnaireTemplateQuestionOptionText object

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
api_instance = bumbal.QuestionnaireTemplateQuestionOptionTextApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of the QuestionnaireTemplateQuestionOptionText object to update
body = bumbal.QuestionnaireTemplateQuestionOptionTextModel() # QuestionnaireTemplateQuestionOptionTextModel | QuestionnaireTemplateQuestionOptionText object that needs to be updated (optional)

try:
    # Update a specific QuestionnaireTemplateQuestionOptionText object
    api_response = api_instance.update_questionnaire_template_question_option_text(notification_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionOptionTextApi->update_questionnaire_template_question_option_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of the QuestionnaireTemplateQuestionOptionText object to update | 
 **body** | [**QuestionnaireTemplateQuestionOptionTextModel**](QuestionnaireTemplateQuestionOptionTextModel.md)| QuestionnaireTemplateQuestionOptionText object that needs to be updated | [optional] 

### Return type

[**ApiResponse45**](ApiResponse45.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

