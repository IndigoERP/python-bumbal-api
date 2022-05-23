# bumbal.AddressApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_address**](AddressApi.md#delete_address) | **DELETE** /address/{addressId} | Delete an address
[**retrieve_address**](AddressApi.md#retrieve_address) | **GET** /address/{addressId} | Retrieve a Address
[**retrieve_list_address**](AddressApi.md#retrieve_list_address) | **PUT** /address | Retrieve List of Addresses
[**reverse_geo_code_address**](AddressApi.md#reverse_geo_code_address) | **POST** /address/reverse-geo-code | Reverse Geo Code an address
[**set_address**](AddressApi.md#set_address) | **POST** /address/set | Add a new Address
[**update_address**](AddressApi.md#update_address) | **PUT** /address/{addressId} | Update a address
[**validate_address**](AddressApi.md#validate_address) | **GET** /address/validate | Validate an address


# **delete_address**
> ApiResponse delete_address(address_id)

Delete an address

Delete an address

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
api_instance = bumbal.AddressApi(bumbal.ApiClient(configuration))
address_id = 789 # int | ID of the address to delete

try:
    # Delete an address
    api_response = api_instance.delete_address(address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->delete_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**| ID of the address to delete | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_address**
> AddressModel retrieve_address(address_id)

Retrieve a Address

Retrieve an Address

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
api_instance = bumbal.AddressApi(bumbal.ApiClient(configuration))
address_id = 789 # int | ID of address to retrieve

try:
    # Retrieve a Address
    api_response = api_instance.retrieve_address(address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->retrieve_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**| ID of address to retrieve | 

### Return type

[**AddressModel**](AddressModel.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_list_address**
> AddressListResponse retrieve_list_address(arguments)

Retrieve List of Addresses

Retrieve List of Addresses

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
api_instance = bumbal.AddressApi(bumbal.ApiClient(configuration))
arguments = bumbal.AddressRetrieveListArguments() # AddressRetrieveListArguments | Address RetrieveList Arguments

try:
    # Retrieve List of Addresses
    api_response = api_instance.retrieve_list_address(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->retrieve_list_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**AddressRetrieveListArguments**](AddressRetrieveListArguments.md)| Address RetrieveList Arguments | 

### Return type

[**AddressListResponse**](AddressListResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverse_geo_code_address**
> AddressReverseGeoCodeResponse reverse_geo_code_address(arguments)

Reverse Geo Code an address

Reverse Geo Code an address

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
api_instance = bumbal.AddressApi(bumbal.ApiClient(configuration))
arguments = bumbal.AddressReverseGeoCodeArguments() # AddressReverseGeoCodeArguments | Address Reverse GeoCode Arguments

try:
    # Reverse Geo Code an address
    api_response = api_instance.reverse_geo_code_address(arguments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->reverse_geo_code_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arguments** | [**AddressReverseGeoCodeArguments**](AddressReverseGeoCodeArguments.md)| Address Reverse GeoCode Arguments | 

### Return type

[**AddressReverseGeoCodeResponse**](AddressReverseGeoCodeResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_address**
> ApiResponse set_address(body=body)

Add a new Address

Add a new Address

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
api_instance = bumbal.AddressApi(bumbal.ApiClient(configuration))
body = bumbal.AddressModel() # AddressModel | Address object that needs to be created (optional)

try:
    # Add a new Address
    api_response = api_instance.set_address(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->set_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddressModel**](AddressModel.md)| Address object that needs to be created | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_address**
> ApiResponse update_address(address_id, body=body)

Update a address

Update a address

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
api_instance = bumbal.AddressApi(bumbal.ApiClient(configuration))
address_id = 789 # int | ID of address to update
body = bumbal.AddressModel() # AddressModel | Address object that needs to be updated (optional)

try:
    # Update a address
    api_response = api_instance.update_address(address_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->update_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**| ID of address to update | 
 **body** | [**AddressModel**](AddressModel.md)| Address object that needs to be updated | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_address**
> AddressValidationResponse validate_address(city, iso_country, street=street, house_nr=house_nr, house_nr_addendum=house_nr_addendum, zipcode=zipcode, minimum_certainty=minimum_certainty)

Validate an address

Validate an address

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
api_instance = bumbal.AddressApi(bumbal.ApiClient(configuration))
city = 'city_example' # str | City
iso_country = 'iso_country_example' # str | Country in ISO 3166-1 alpha 2
street = 'street_example' # str | Street (optional)
house_nr = 'house_nr_example' # str | House Number (optional)
house_nr_addendum = 'house_nr_addendum_example' # str | House Number Annex (optional)
zipcode = 'zipcode_example' # str | Zipcode (optional)
minimum_certainty = 56 # int | Minimum required certainty as an int between 0 and 100 (optional)

try:
    # Validate an address
    api_response = api_instance.validate_address(city, iso_country, street=street, house_nr=house_nr, house_nr_addendum=house_nr_addendum, zipcode=zipcode, minimum_certainty=minimum_certainty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->validate_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**| City | 
 **iso_country** | **str**| Country in ISO 3166-1 alpha 2 | 
 **street** | **str**| Street | [optional] 
 **house_nr** | **str**| House Number | [optional] 
 **house_nr_addendum** | **str**| House Number Annex | [optional] 
 **zipcode** | **str**| Zipcode | [optional] 
 **minimum_certainty** | **int**| Minimum required certainty as an int between 0 and 100 | [optional] 

### Return type

[**AddressValidationResponse**](AddressValidationResponse.md)

### Authorization

[api_key](../README.md#api_key), [jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

