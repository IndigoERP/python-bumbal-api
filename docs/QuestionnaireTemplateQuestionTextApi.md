# bumbal.QuestionnaireTemplateQuestionTextApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_questionnaire_template_question_text**](QuestionnaireTemplateQuestionTextApi.md#create_questionnaire_template_question_text) | **POST** /questionnaire-template-question-text | Add a new QuestionnaireTemplateQuestionText
[**delete_questionnaire_template_question_text**](QuestionnaireTemplateQuestionTextApi.md#delete_questionnaire_template_question_text) | **DELETE** /questionnaire-template-question-text/{questionnaire-template-question-textId} | Delete an QuestionnaireTemplateQuestionText entry
[**retrieve_list_questionnaire_template_question_text**](QuestionnaireTemplateQuestionTextApi.md#retrieve_list_questionnaire_template_question_text) | **PUT** /questionnaire-template-question-text | Retrieve List of QuestionnaireTemplateQuestionText
[**retrieve_questionnaire_template_question_text**](QuestionnaireTemplateQuestionTextApi.md#retrieve_questionnaire_template_question_text) | **GET** /questionnaire-template-question-text/{questionnaire-template-question-textId} | Retrieve a QuestionnaireTemplateQuestionText
[**set_questionnaire_template_question_text**](QuestionnaireTemplateQuestionTextApi.md#set_questionnaire_template_question_text) | **POST** /questionnaire-template-question-text/set | Set (create or update) a QuestionnaireTemplateQuestionText
[**update_questionnaire_template_question_text**](QuestionnaireTemplateQuestionTextApi.md#update_questionnaire_template_question_text) | **PUT** /questionnaire-template-question-text/{questionnaire-template-question-textId} | Update a specific QuestionnaireTemplateQuestionText object


# **create_questionnaire_template_question_text**
> ApiResponse50 create_questionnaire_template_question_text(body=body)

Add a new QuestionnaireTemplateQuestionText

Add a new QuestionnaireTemplateQuestionText

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
api_instance = bumbal.QuestionnaireTemplateQuestionTextApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateQuestionTextModel() # QuestionnaireTemplateQuestionTextModel | QuestionnaireTemplateQuestionText object that needs to be created (optional)

try:
    # Add a new QuestionnaireTemplateQuestionText
    api_response = api_instance.create_questionnaire_template_question_text(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionTextApi->create_questionnaire_template_question_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateQuestionTextModel**](QuestionnaireTemplateQuestionTextModel.md)| QuestionnaireTemplateQuestionText object that needs to be created | [optional] 

### Return type

[**ApiResponse50**](ApiResponse50.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_questionnaire_template_question_text**
> ApiResponse49 delete_questionnaire_template_question_text(notification_id)

Delete an QuestionnaireTemplateQuestionText entry

Delete an QuestionnaireTemplateQuestionText entry

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
api_instance = bumbal.QuestionnaireTemplateQuestionTextApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of QuestionnaireTemplateQuestionText to delete

try:
    # Delete an QuestionnaireTemplateQuestionText entry
    api_response = api_instance.delete_questionnaire_template_question_text(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionTextApi->delete_questionnaire_template_question_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of QuestionnaireTemplateQuestionText to delete | 

### Return type

[**ApiResponse49**](ApiResponse49.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_questionnaire_template_question_text**
> QuestionnaireTemplateQuestionTextListResponse retrieve_list_questionnaire_template_question_text(arguments)

Retrieve List of QuestionnaireTemplateQuestionText

Retrieve List of QuestionnaireTemplateQuestionText

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
api_instance = bumbal.QuestionnaireTemplateQuestionTextApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireTemplateQuestionTextRetrieveListArguments() # QuestionnaireTemplateQuestionTextRetrieveListArguments | QuestionnaireTemplateQuestionText RetrieveList Arguments

try:
    # Retrieve List of QuestionnaireTemplateQuestionText
    api_response = api_instance.retrieve_list_questionnaire_template_question_text(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionTextApi->retrieve_list_questionnaire_template_question_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireTemplateQuestionTextRetrieveListArguments**](QuestionnaireTemplateQuestionTextRetrieveListArguments.md)| QuestionnaireTemplateQuestionText RetrieveList Arguments | 

### Return type

[**QuestionnaireTemplateQuestionTextListResponse**](QuestionnaireTemplateQuestionTextListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_questionnaire_template_question_text**
> QuestionnaireTemplateQuestionTextModel retrieve_questionnaire_template_question_text(notification_id)

Retrieve a QuestionnaireTemplateQuestionText

Retrieve an QuestionnaireTemplateQuestionText

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
api_instance = bumbal.QuestionnaireTemplateQuestionTextApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of QuestionnaireTemplateQuestionText to retrieve

try:
    # Retrieve a QuestionnaireTemplateQuestionText
    api_response = api_instance.retrieve_questionnaire_template_question_text(notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionTextApi->retrieve_questionnaire_template_question_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of QuestionnaireTemplateQuestionText to retrieve | 

### Return type

[**QuestionnaireTemplateQuestionTextModel**](QuestionnaireTemplateQuestionTextModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_questionnaire_template_question_text**
> ApiResponse set_questionnaire_template_question_text(body=body)

Set (create or update) a QuestionnaireTemplateQuestionText

Set (create or update) a d=QuestionnaireTemplateQuestionText. If id or links are set in the data, and a corresponding QuestionnaireTemplateQuestionText is found in Bumbal, an update will be performed.

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
api_instance = bumbal.QuestionnaireTemplateQuestionTextApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateQuestionTextModel() # QuestionnaireTemplateQuestionTextModel | QuestionnaireTemplateQuestionText object (optional)

try:
    # Set (create or update) a QuestionnaireTemplateQuestionText
    api_response = api_instance.set_questionnaire_template_question_text(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionTextApi->set_questionnaire_template_question_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateQuestionTextModel**](QuestionnaireTemplateQuestionTextModel.md)| QuestionnaireTemplateQuestionText object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_questionnaire_template_question_text**
> ApiResponse48 update_questionnaire_template_question_text(notification_id, body=body)

Update a specific QuestionnaireTemplateQuestionText object

Update a specific QuestionnaireTemplateQuestionText object

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
api_instance = bumbal.QuestionnaireTemplateQuestionTextApi(bumbal.ApiClient(configuration))
notification_id = 789 # int | ID of the QuestionnaireTemplateQuestionText object to update
body = bumbal.QuestionnaireTemplateQuestionTextModel() # QuestionnaireTemplateQuestionTextModel | QuestionnaireTemplateQuestionText object that needs to be updated (optional)

try:
    # Update a specific QuestionnaireTemplateQuestionText object
    api_response = api_instance.update_questionnaire_template_question_text(notification_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateQuestionTextApi->update_questionnaire_template_question_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_id** | **int**| ID of the QuestionnaireTemplateQuestionText object to update | 
 **body** | [**QuestionnaireTemplateQuestionTextModel**](QuestionnaireTemplateQuestionTextModel.md)| QuestionnaireTemplateQuestionText object that needs to be updated | [optional] 

### Return type

[**ApiResponse48**](ApiResponse48.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

