# bumbal.PaymentApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment**](PaymentApi.md#create_payment) | **POST** /payment | Add a new Payment
[**delete_payment**](PaymentApi.md#delete_payment) | **DELETE** /payment/{paymentId} | Delete an Payment entry
[**retrieve_list_payment**](PaymentApi.md#retrieve_list_payment) | **PUT** /payment | Retrieve List of Payment
[**retrieve_payment**](PaymentApi.md#retrieve_payment) | **GET** /payment/{paymentId} | Retrieve a Payment
[**set_payment**](PaymentApi.md#set_payment) | **POST** /payment/set | Set (create or update) a Payment
[**update_payment**](PaymentApi.md#update_payment) | **PUT** /payment/{paymentId} | Update a specific Payment object


# **create_payment**
> PaymentCreateResponse create_payment(body=body)

Add a new Payment

Add a new Payment

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
api_instance = bumbal.PaymentApi(bumbal.ApiClient(configuration))
body = bumbal.PaymentModel() # PaymentModel | Payment object that needs to be created (optional)

try:
    # Add a new Payment
    api_response = api_instance.create_payment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->create_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentModel**](PaymentModel.md)| Payment object that needs to be created | [optional] 

### Return type

[**PaymentCreateResponse**](PaymentCreateResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment**
> PaymentDeleteResponse delete_payment(payment_id)

Delete an Payment entry

Delete an Payment entry

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
api_instance = bumbal.PaymentApi(bumbal.ApiClient(configuration))
payment_id = 789 # int | ID of Payment to delete

try:
    # Delete an Payment entry
    api_response = api_instance.delete_payment(payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->delete_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **int**| ID of Payment to delete | 

### Return type

[**PaymentDeleteResponse**](PaymentDeleteResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_payment**
> PaymentListResponse retrieve_list_payment(arguments)

Retrieve List of Payment

Retrieve List of Payment

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
api_instance = bumbal.PaymentApi(bumbal.ApiClient(configuration))
arguments = bumbal.PaymentRetrieveListArguments() # PaymentRetrieveListArguments | Payment RetrieveList Arguments

try:
    # Retrieve List of Payment
    api_response = api_instance.retrieve_list_payment(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->retrieve_list_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**PaymentRetrieveListArguments**](PaymentRetrieveListArguments.md)| Payment RetrieveList Arguments | 

### Return type

[**PaymentListResponse**](PaymentListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_payment**
> PaymentModel retrieve_payment(payment_id)

Retrieve a Payment

Retrieve an Payment

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
api_instance = bumbal.PaymentApi(bumbal.ApiClient(configuration))
payment_id = 789 # int | ID of Payment to retrieve

try:
    # Retrieve a Payment
    api_response = api_instance.retrieve_payment(payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->retrieve_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **int**| ID of Payment to retrieve | 

### Return type

[**PaymentModel**](PaymentModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_payment**
> PaymentSetResponse set_payment(body=body)

Set (create or update) a Payment

Set (create or update) a d=Payment. If id or links are set in the data, and a corresponding Payment is found in Bumbal, an update will be performed.

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
api_instance = bumbal.PaymentApi(bumbal.ApiClient(configuration))
body = bumbal.PaymentModel() # PaymentModel | Payment object (optional)

try:
    # Set (create or update) a Payment
    api_response = api_instance.set_payment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->set_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentModel**](PaymentModel.md)| Payment object | [optional] 

### Return type

[**PaymentSetResponse**](PaymentSetResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment**
> PaymentUpdateResponse update_payment(payment_id, body=body)

Update a specific Payment object

Update a specific Payment object

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
api_instance = bumbal.PaymentApi(bumbal.ApiClient(configuration))
payment_id = 789 # int | ID of the Payment object to update
body = bumbal.PaymentModel() # PaymentModel | Payment object that needs to be updated (optional)

try:
    # Update a specific Payment object
    api_response = api_instance.update_payment(payment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentApi->update_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **int**| ID of the Payment object to update | 
 **body** | [**PaymentModel**](PaymentModel.md)| Payment object that needs to be updated | [optional] 

### Return type

[**PaymentUpdateResponse**](PaymentUpdateResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

