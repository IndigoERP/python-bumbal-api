# bumbal.TransactionApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction**](TransactionApi.md#create_transaction) | **POST** /transaction | Add a new Transaction
[**delete_transaction**](TransactionApi.md#delete_transaction) | **DELETE** /transaction/{transactionId} | Delete an Transaction entry
[**retrieve_list_transaction**](TransactionApi.md#retrieve_list_transaction) | **PUT** /transaction | Retrieve List of Transaction
[**retrieve_transaction**](TransactionApi.md#retrieve_transaction) | **GET** /transaction/{transactionId} | Retrieve a Transaction
[**set_transaction**](TransactionApi.md#set_transaction) | **POST** /transaction/set | Set (create or update) a Transaction
[**token**](TransactionApi.md#token) | **POST** /transaction/token | get a transaction token
[**token_0**](TransactionApi.md#token_0) | **POST** /transaction/token-is-paid | set a transaction to paid with token
[**token_1**](TransactionApi.md#token_1) | **POST** /transaction/token-is-cancelled | set a transaction to cancelled with token
[**token_2**](TransactionApi.md#token_2) | **POST** /transaction/token-has-failed | set a transaction to failed with token
[**update_transaction**](TransactionApi.md#update_transaction) | **PUT** /transaction/{transactionId} | Update a specific Transaction object


# **create_transaction**
> TransactionCreateResponse create_transaction(body=body)

Add a new Transaction

Add a new Transaction

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
api_instance = bumbal.TransactionApi(bumbal.ApiClient(configuration))
body = bumbal.TransactionModel() # TransactionModel | Transaction object that needs to be created (optional)

try:
    # Add a new Transaction
    api_response = api_instance.create_transaction(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->create_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionModel**](TransactionModel.md)| Transaction object that needs to be created | [optional] 

### Return type

[**TransactionCreateResponse**](TransactionCreateResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction**
> TransactionDeleteResponse delete_transaction(transaction_id)

Delete an Transaction entry

Delete an Transaction entry

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
api_instance = bumbal.TransactionApi(bumbal.ApiClient(configuration))
transaction_id = 789 # int | ID of Transaction to delete

try:
    # Delete an Transaction entry
    api_response = api_instance.delete_transaction(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->delete_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**| ID of Transaction to delete | 

### Return type

[**TransactionDeleteResponse**](TransactionDeleteResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_transaction**
> TransactionListResponse retrieve_list_transaction(arguments)

Retrieve List of Transaction

Retrieve List of Transaction

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
api_instance = bumbal.TransactionApi(bumbal.ApiClient(configuration))
arguments = bumbal.TransactionRetrieveListArguments() # TransactionRetrieveListArguments | Transaction RetrieveList Arguments

try:
    # Retrieve List of Transaction
    api_response = api_instance.retrieve_list_transaction(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->retrieve_list_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**TransactionRetrieveListArguments**](TransactionRetrieveListArguments.md)| Transaction RetrieveList Arguments | 

### Return type

[**TransactionListResponse**](TransactionListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_transaction**
> TransactionModel retrieve_transaction(transaction_id)

Retrieve a Transaction

Retrieve an Transaction

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
api_instance = bumbal.TransactionApi(bumbal.ApiClient(configuration))
transaction_id = 789 # int | ID of Transaction to retrieve

try:
    # Retrieve a Transaction
    api_response = api_instance.retrieve_transaction(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->retrieve_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**| ID of Transaction to retrieve | 

### Return type

[**TransactionModel**](TransactionModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_transaction**
> TransactionSetResponse set_transaction(body=body)

Set (create or update) a Transaction

Set (create or update) a d=Transaction. If id or links are set in the data, and a corresponding Transaction is found in Bumbal, an update will be performed.

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
api_instance = bumbal.TransactionApi(bumbal.ApiClient(configuration))
body = bumbal.TransactionModel() # TransactionModel | Transaction object (optional)

try:
    # Set (create or update) a Transaction
    api_response = api_instance.set_transaction(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->set_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionModel**](TransactionModel.md)| Transaction object | [optional] 

### Return type

[**TransactionSetResponse**](TransactionSetResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token**
> TransactionTokenResponse token(arguments)

get a transaction token

get a transaction token

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
api_instance = bumbal.TransactionApi(bumbal.ApiClient(configuration))
arguments = bumbal.TransactionTokenArguments() # TransactionTokenArguments | Request Arguments

try:
    # get a transaction token
    api_response = api_instance.token(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**TransactionTokenArguments**](TransactionTokenArguments.md)| Request Arguments | 

### Return type

[**TransactionTokenResponse**](TransactionTokenResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_0**
> TransactionTokenIsPaidResponse token_0(arguments)

set a transaction to paid with token

set a transaction to paid with token

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
api_instance = bumbal.TransactionApi(bumbal.ApiClient(configuration))
arguments = bumbal.TransactionTokenIsPaidArguments() # TransactionTokenIsPaidArguments | Request Arguments

try:
    # set a transaction to paid with token
    api_response = api_instance.token_0(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->token_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**TransactionTokenIsPaidArguments**](TransactionTokenIsPaidArguments.md)| Request Arguments | 

### Return type

[**TransactionTokenIsPaidResponse**](TransactionTokenIsPaidResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_1**
> TransactionTokenIsCancelledResponse token_1(arguments)

set a transaction to cancelled with token

set a transaction to cancelled with token

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
api_instance = bumbal.TransactionApi(bumbal.ApiClient(configuration))
arguments = bumbal.TransactionTokenIsCancelledArguments() # TransactionTokenIsCancelledArguments | Request Arguments

try:
    # set a transaction to cancelled with token
    api_response = api_instance.token_1(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->token_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**TransactionTokenIsCancelledArguments**](TransactionTokenIsCancelledArguments.md)| Request Arguments | 

### Return type

[**TransactionTokenIsCancelledResponse**](TransactionTokenIsCancelledResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_2**
> TransactionTokenHasFailedResponse token_2(arguments)

set a transaction to failed with token

set a transaction to failed with token

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
api_instance = bumbal.TransactionApi(bumbal.ApiClient(configuration))
arguments = bumbal.TransactionTokenHasFailedArguments() # TransactionTokenHasFailedArguments | Request Arguments

try:
    # set a transaction to failed with token
    api_response = api_instance.token_2(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->token_2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**TransactionTokenHasFailedArguments**](TransactionTokenHasFailedArguments.md)| Request Arguments | 

### Return type

[**TransactionTokenHasFailedResponse**](TransactionTokenHasFailedResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_transaction**
> TransactionUpdateResponse update_transaction(transaction_id, body=body)

Update a specific Transaction object

Update a specific Transaction object

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
api_instance = bumbal.TransactionApi(bumbal.ApiClient(configuration))
transaction_id = 789 # int | ID of the Transaction object to update
body = bumbal.TransactionModel() # TransactionModel | Transaction object that needs to be updated (optional)

try:
    # Update a specific Transaction object
    api_response = api_instance.update_transaction(transaction_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionApi->update_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **int**| ID of the Transaction object to update | 
 **body** | [**TransactionModel**](TransactionModel.md)| Transaction object that needs to be updated | [optional] 

### Return type

[**TransactionUpdateResponse**](TransactionUpdateResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

