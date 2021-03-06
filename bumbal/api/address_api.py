# coding: utf-8

"""
    Bumbal Client Api

    Bumbal API documentation  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: gerb@bumbal.eu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bumbal.api_client import ApiClient


class AddressApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_address(self, address_id, **kwargs):  # noqa: E501
        """Delete an address  # noqa: E501

        Delete an address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_address(address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int address_id: ID of the address to delete (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_address_with_http_info(address_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_address_with_http_info(address_id, **kwargs)  # noqa: E501
            return data

    def delete_address_with_http_info(self, address_id, **kwargs):  # noqa: E501
        """Delete an address  # noqa: E501

        Delete an address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_address_with_http_info(address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int address_id: ID of the address to delete (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address_id' is set
        if self.api_client.client_side_validation and ('address_id' not in params or
                                                       params['address_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `address_id` when calling `delete_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/address/{addressId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_address(self, address_id, **kwargs):  # noqa: E501
        """Retrieve a Address  # noqa: E501

        Retrieve an Address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_address(address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int address_id: ID of address to retrieve (required)
        :return: AddressModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_address_with_http_info(address_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_address_with_http_info(address_id, **kwargs)  # noqa: E501
            return data

    def retrieve_address_with_http_info(self, address_id, **kwargs):  # noqa: E501
        """Retrieve a Address  # noqa: E501

        Retrieve an Address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_address_with_http_info(address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int address_id: ID of address to retrieve (required)
        :return: AddressModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address_id' is set
        if self.api_client.client_side_validation and ('address_id' not in params or
                                                       params['address_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `address_id` when calling `retrieve_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/address/{addressId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddressModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_list_address(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Addresses  # noqa: E501

        Retrieve List of Addresses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_address(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddressRetrieveListArguments arguments: Address RetrieveList Arguments (required)
        :return: AddressListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_list_address_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_list_address_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def retrieve_list_address_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Addresses  # noqa: E501

        Retrieve List of Addresses  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_address_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddressRetrieveListArguments arguments: Address RetrieveList Arguments (required)
        :return: AddressListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['arguments']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_list_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `retrieve_list_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'arguments' in params:
            body_params = params['arguments']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/address', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddressListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reverse_geo_code_address(self, arguments, **kwargs):  # noqa: E501
        """Reverse Geo Code an address  # noqa: E501

        Reverse Geo Code an address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reverse_geo_code_address(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddressReverseGeoCodeArguments arguments: Address Reverse GeoCode Arguments (required)
        :return: AddressReverseGeoCodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reverse_geo_code_address_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.reverse_geo_code_address_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def reverse_geo_code_address_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """Reverse Geo Code an address  # noqa: E501

        Reverse Geo Code an address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reverse_geo_code_address_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddressReverseGeoCodeArguments arguments: Address Reverse GeoCode Arguments (required)
        :return: AddressReverseGeoCodeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['arguments']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reverse_geo_code_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `reverse_geo_code_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'arguments' in params:
            body_params = params['arguments']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/address/reverse-geo-code', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddressReverseGeoCodeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_address(self, **kwargs):  # noqa: E501
        """Add a new Address  # noqa: E501

        Add a new Address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_address(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddressModel body: Address object that needs to be created
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_address_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.set_address_with_http_info(**kwargs)  # noqa: E501
            return data

    def set_address_with_http_info(self, **kwargs):  # noqa: E501
        """Add a new Address  # noqa: E501

        Add a new Address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_address_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddressModel body: Address object that needs to be created
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_address" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/address/set', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_address(self, address_id, **kwargs):  # noqa: E501
        """Update a address  # noqa: E501

        Update a address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_address(address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int address_id: ID of address to update (required)
        :param AddressModel body: Address object that needs to be updated
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_address_with_http_info(address_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_address_with_http_info(address_id, **kwargs)  # noqa: E501
            return data

    def update_address_with_http_info(self, address_id, **kwargs):  # noqa: E501
        """Update a address  # noqa: E501

        Update a address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_address_with_http_info(address_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int address_id: ID of address to update (required)
        :param AddressModel body: Address object that needs to be updated
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'address_id' is set
        if self.api_client.client_side_validation and ('address_id' not in params or
                                                       params['address_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `address_id` when calling `update_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/address/{addressId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def validate_address(self, city, iso_country, **kwargs):  # noqa: E501
        """Validate an address  # noqa: E501

        Validate an address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_address(city, iso_country, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str city: City (required)
        :param str iso_country: Country in ISO 3166-1 alpha 2 (required)
        :param str street: Street
        :param str house_nr: House Number
        :param str house_nr_addendum: House Number Annex
        :param str zipcode: Zipcode
        :param int minimum_certainty: Minimum required certainty as an int between 0 and 100
        :return: AddressValidationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.validate_address_with_http_info(city, iso_country, **kwargs)  # noqa: E501
        else:
            (data) = self.validate_address_with_http_info(city, iso_country, **kwargs)  # noqa: E501
            return data

    def validate_address_with_http_info(self, city, iso_country, **kwargs):  # noqa: E501
        """Validate an address  # noqa: E501

        Validate an address  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.validate_address_with_http_info(city, iso_country, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str city: City (required)
        :param str iso_country: Country in ISO 3166-1 alpha 2 (required)
        :param str street: Street
        :param str house_nr: House Number
        :param str house_nr_addendum: House Number Annex
        :param str zipcode: Zipcode
        :param int minimum_certainty: Minimum required certainty as an int between 0 and 100
        :return: AddressValidationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['city', 'iso_country', 'street', 'house_nr', 'house_nr_addendum', 'zipcode', 'minimum_certainty']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'city' is set
        if self.api_client.client_side_validation and ('city' not in params or
                                                       params['city'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `city` when calling `validate_address`")  # noqa: E501
        # verify the required parameter 'iso_country' is set
        if self.api_client.client_side_validation and ('iso_country' not in params or
                                                       params['iso_country'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `iso_country` when calling `validate_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'street' in params:
            query_params.append(('street', params['street']))  # noqa: E501
        if 'house_nr' in params:
            query_params.append(('house_nr', params['house_nr']))  # noqa: E501
        if 'house_nr_addendum' in params:
            query_params.append(('house_nr_addendum', params['house_nr_addendum']))  # noqa: E501
        if 'zipcode' in params:
            query_params.append(('zipcode', params['zipcode']))  # noqa: E501
        if 'city' in params:
            query_params.append(('city', params['city']))  # noqa: E501
        if 'iso_country' in params:
            query_params.append(('iso_country', params['iso_country']))  # noqa: E501
        if 'minimum_certainty' in params:
            query_params.append(('minimum_certainty', params['minimum_certainty']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/address/validate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AddressValidationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
