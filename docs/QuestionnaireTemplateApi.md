# bumbal.QuestionnaireTemplateApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_questionnaire_template**](QuestionnaireTemplateApi.md#create_questionnaire_template) | **POST** /questionnaire-template | Add a new QuestionnaireTemplate
[**delete_questionnaire_template**](QuestionnaireTemplateApi.md#delete_questionnaire_template) | **DELETE** /questionnaire-template/{questionnaire-templateId} | Delete an QuestionnaireTemplate entry
[**retrieve_list_questionnaire_template**](QuestionnaireTemplateApi.md#retrieve_list_questionnaire_template) | **PUT** /questionnaire-template | Retrieve List of QuestionnaireTemplate
[**retrieve_questionnaire_template**](QuestionnaireTemplateApi.md#retrieve_questionnaire_template) | **GET** /questionnaire-template/{questionnaire-templateId} | Retrieve a QuestionnaireTemplate
[**set_questionnaire_template**](QuestionnaireTemplateApi.md#set_questionnaire_template) | **POST** /questionnaire-template/set | Set (create or update) a QuestionnaireTemplate
[**update_questionnaire_template**](QuestionnaireTemplateApi.md#update_questionnaire_template) | **PUT** /questionnaire-template/{questionnaire-templateId} | Update a specific QuestionnaireTemplate object


# **create_questionnaire_template**
> ApiResponse33 create_questionnaire_template(body=body)

Add a new QuestionnaireTemplate

Add a new QuestionnaireTemplate

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
api_instance = bumbal.QuestionnaireTemplateApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateModel() # QuestionnaireTemplateModel | QuestionnaireTemplate object that needs to be created (optional)

try:
    # Add a new QuestionnaireTemplate
    api_response = api_instance.create_questionnaire_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateApi->create_questionnaire_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateModel**](QuestionnaireTemplateModel.md)| QuestionnaireTemplate object that needs to be created | [optional] 

### Return type

[**ApiResponse33**](ApiResponse33.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_questionnaire_template**
> ApiResponse31 delete_questionnaire_template(questionnaire_template_id)

Delete an QuestionnaireTemplate entry

Delete an QuestionnaireTemplate entry

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
api_instance = bumbal.QuestionnaireTemplateApi(bumbal.ApiClient(configuration))
questionnaire_template_id = 789 # int | ID of QuestionnaireTemplate to delete

try:
    # Delete an QuestionnaireTemplate entry
    api_response = api_instance.delete_questionnaire_template(questionnaire_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateApi->delete_questionnaire_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_template_id** | **int**| ID of QuestionnaireTemplate to delete | 

### Return type

[**ApiResponse31**](ApiResponse31.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_questionnaire_template**
> QuestionnaireTemplateListResponse retrieve_list_questionnaire_template(arguments)

Retrieve List of QuestionnaireTemplate

Retrieve List of QuestionnaireTemplate

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
api_instance = bumbal.QuestionnaireTemplateApi(bumbal.ApiClient(configuration))
arguments = bumbal.QuestionnaireTemplateRetrieveListArguments() # QuestionnaireTemplateRetrieveListArguments | QuestionnaireTemplate RetrieveList Arguments

try:
    # Retrieve List of QuestionnaireTemplate
    api_response = api_instance.retrieve_list_questionnaire_template(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateApi->retrieve_list_questionnaire_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**QuestionnaireTemplateRetrieveListArguments**](QuestionnaireTemplateRetrieveListArguments.md)| QuestionnaireTemplate RetrieveList Arguments | 

### Return type

[**QuestionnaireTemplateListResponse**](QuestionnaireTemplateListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_questionnaire_template**
> QuestionnaireTemplateModel retrieve_questionnaire_template(questionnaire_template_id)

Retrieve a QuestionnaireTemplate

Retrieve an QuestionnaireTemplate

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
api_instance = bumbal.QuestionnaireTemplateApi(bumbal.ApiClient(configuration))
questionnaire_template_id = 789 # int | ID of QuestionnaireTemplate to retrieve

try:
    # Retrieve a QuestionnaireTemplate
    api_response = api_instance.retrieve_questionnaire_template(questionnaire_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateApi->retrieve_questionnaire_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_template_id** | **int**| ID of QuestionnaireTemplate to retrieve | 

### Return type

[**QuestionnaireTemplateModel**](QuestionnaireTemplateModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_questionnaire_template**
> ApiResponse set_questionnaire_template(body=body)

Set (create or update) a QuestionnaireTemplate

Set (create or update) a d=QuestionnaireTemplate. If id or links are set in the data, and a corresponding QuestionnaireTemplate is found in Bumbal, an update will be performed.

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
api_instance = bumbal.QuestionnaireTemplateApi(bumbal.ApiClient(configuration))
body = bumbal.QuestionnaireTemplateModel() # QuestionnaireTemplateModel | QuestionnaireTemplate object (optional)

try:
    # Set (create or update) a QuestionnaireTemplate
    api_response = api_instance.set_questionnaire_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateApi->set_questionnaire_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionnaireTemplateModel**](QuestionnaireTemplateModel.md)| QuestionnaireTemplate object | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_questionnaire_template**
> ApiResponse30 update_questionnaire_template(questionnaire_template_id, body=body)

Update a specific QuestionnaireTemplate object

Update a specific QuestionnaireTemplate object

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
api_instance = bumbal.QuestionnaireTemplateApi(bumbal.ApiClient(configuration))
questionnaire_template_id = 789 # int | ID of the QuestionnaireTemplate object to update
body = bumbal.QuestionnaireTemplateModel() # QuestionnaireTemplateModel | QuestionnaireTemplate object that needs to be updated (optional)

try:
    # Update a specific QuestionnaireTemplate object
    api_response = api_instance.update_questionnaire_template(questionnaire_template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionnaireTemplateApi->update_questionnaire_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaire_template_id** | **int**| ID of the QuestionnaireTemplate object to update | 
 **body** | [**QuestionnaireTemplateModel**](QuestionnaireTemplateModel.md)| QuestionnaireTemplate object that needs to be updated | [optional] 

### Return type

[**ApiResponse30**](ApiResponse30.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

