# bumbal.QuestionnaireTemplateGetLanguagesApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_questionnaire_template_languages**](QuestionnaireTemplateGetLanguagesApi.md#get_questionnaire_template_languages) | **GET** /questionnaire-template/get-languages/{questionnaire-templateId} | Retrieves all set languages for an QuestionnaireTemplate entry


# **get_questionnaire_template_languages**
> ApiResponse34 get_questionnaire_template_languages(questionnaire_template_id)

Retrieves all set languages for an QuestionnaireTemplate entry

Retrieves all set languages for an QuestionnaireTemplate entry

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
api_instance = bumbal.QuestionnaireTemplateGetLanguagesApi(bumbal.ApiClient(configuration))
questionnaire_template_id = 789 # int | ID of QuestionnaireTemplate

try:
    # Retrieves all set languages for an QuestionnaireTemplate entry
    api_response = api_instance.get_questionnaire_template_languages(questionnaire_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateGetLanguagesApi->get_questionnaire_template_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_template_id** | **int**| ID of QuestionnaireTemplate | 

### Return type

[**ApiResponse34**](ApiResponse34.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

