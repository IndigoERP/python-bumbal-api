# bumbal.QuestionnaireAnswerApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_questionnaire_answer**](QuestionnaireAnswerApi.md#create_questionnaire_answer) | **POST** /questionnaire-answer | Add a new QuestionnaireAnswer
[**delete_questionnaire_answer**](QuestionnaireAnswerApi.md#delete_questionnaire_answer) | **DELETE** /questionnaire-answer/{questionnaire-answerId} | Delete an QuestionnaireAnswer entry
[**retrieve_list_questionnaire_answer**](QuestionnaireAnswerApi.md#retrieve_list_questionnaire_answer) | **PUT** /questionnaire-answer | Retrieve List of QuestionnaireAnswer
[**retrieve_questionnaire_answer**](QuestionnaireAnswerApi.md#retrieve_questionnaire_answer) | **GET** /questionnaire-answer/{questionnaire-answerId} | Retrieve a QuestionnaireAnswer
[**set_questionnaire_answer**](QuestionnaireAnswerApi.md#set_questionnaire_answer) | **POST** /questionnaire-answer/set | Set (create or update) a QuestionnaireAnswer
[**update_questionnaire_answer**](QuestionnaireAnswerApi.md#update_questionnaire_answer) | **PUT** /questionnaire-answer/{questionnaire-answerId} | Update a specific QuestionnaireAnswer object


# **create_questionnaire_answer**
> ApiResponse26 create_questionnaire_answer(body=body)

Add a new QuestionnaireAnswer

Add a new QuestionnaireAnswer

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
api_instance = bumbal.QuestionnaireAnswerApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireAnswerModel() # QuestionnaireAnswerModel | QuestionnaireAnswer object that needs to be created (optional)

try:
    # Add a new QuestionnaireAnswer
    api_response = api_instance.create_questionnaire_answer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireAnswerApi->create_questionnaire_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireAnswerModel**](QuestionnaireAnswerModel.md)| QuestionnaireAnswer object that needs to be created | [optional] 

### Return type

[**ApiResponse26**](ApiResponse26.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_questionnaire_answer**
> ApiResponse24 delete_questionnaire_answer(questionnaire_answer_id)

Delete an QuestionnaireAnswer entry

Delete an QuestionnaireAnswer entry

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
api_instance = bumbal.QuestionnaireAnswerApi(bumbal.ApiClient(configuration))
questionnaire_answer_id = 789 # int | ID of QuestionnaireAnswer to delete

try:
    # Delete an QuestionnaireAnswer entry
    api_response = api_instance.delete_questionnaire_answer(questionnaire_answer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireAnswerApi->delete_questionnaire_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_answer_id** | **int**| ID of QuestionnaireAnswer to delete | 

### Return type

[**ApiResponse24**](ApiResponse24.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_questionnaire_answer**
> QuestionnaireAnswerListResponse retrieve_list_questionnaire_answer(arguments)

Retrieve List of QuestionnaireAnswer

Retrieve List of QuestionnaireAnswer

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
api_instance = bumbal.QuestionnaireAnswerApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireAnswerRetrieveListArguments() # QuestionnaireAnswerRetrieveListArguments | QuestionnaireAnswer RetrieveList Arguments

try:
    # Retrieve List of QuestionnaireAnswer
    api_response = api_instance.retrieve_list_questionnaire_answer(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireAnswerApi->retrieve_list_questionnaire_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireAnswerRetrieveListArguments**](QuestionnaireAnswerRetrieveListArguments.md)| QuestionnaireAnswer RetrieveList Arguments | 

### Return type

[**QuestionnaireAnswerListResponse**](QuestionnaireAnswerListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_questionnaire_answer**
> QuestionnaireAnswerModel retrieve_questionnaire_answer(questionnaire_answer_id)

Retrieve a QuestionnaireAnswer

Retrieve an QuestionnaireAnswer

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
api_instance = bumbal.QuestionnaireAnswerApi(bumbal.ApiClient(configuration))
questionnaire_answer_id = 789 # int | ID of QuestionnaireAnswer to retrieve

try:
    # Retrieve a QuestionnaireAnswer
    api_response = api_instance.retrieve_questionnaire_answer(questionnaire_answer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireAnswerApi->retrieve_questionnaire_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_answer_id** | **int**| ID of QuestionnaireAnswer to retrieve | 

### Return type

[**QuestionnaireAnswerModel**](QuestionnaireAnswerModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_questionnaire_answer**
> ApiResponse set_questionnaire_answer(body=body)

Set (create or update) a QuestionnaireAnswer

Set (create or update) a QuestionnaireAnswer. If id or links are set in the data, and a corresponding QuestionnaireAnswer is found in Bumbal, an update will be performed.

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
api_instance = bumbal.QuestionnaireAnswerApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireAnswerModel() # QuestionnaireAnswerModel | QuestionnaireAnswer object (optional)

try:
    # Set (create or update) a QuestionnaireAnswer
    api_response = api_instance.set_questionnaire_answer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireAnswerApi->set_questionnaire_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireAnswerModel**](QuestionnaireAnswerModel.md)| QuestionnaireAnswer object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_questionnaire_answer**
> ApiResponse23 update_questionnaire_answer(questionnaire_answer_id, body=body)

Update a specific QuestionnaireAnswer object

Update a specific QuestionnaireAnswer object

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
api_instance = bumbal.QuestionnaireAnswerApi(bumbal.ApiClient(configuration))
questionnaire_answer_id = 789 # int | ID of the QuestionnaireAnswer object to update
body = bumbal.QuestionnaireAnswerModel() # QuestionnaireAnswerModel | QuestionnaireAnswer object that needs to be updated (optional)

try:
    # Update a specific QuestionnaireAnswer object
    api_response = api_instance.update_questionnaire_answer(questionnaire_answer_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireAnswerApi->update_questionnaire_answer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_answer_id** | **int**| ID of the QuestionnaireAnswer object to update | 
 **body** | [**QuestionnaireAnswerModel**](QuestionnaireAnswerModel.md)| QuestionnaireAnswer object that needs to be updated | [optional] 

### Return type

[**ApiResponse23**](ApiResponse23.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

