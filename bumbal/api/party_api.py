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


class PartyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_party(self, **kwargs):  # noqa: E501
        """Create or update an Party  # noqa: E501

        Create or update an Party. If id or links are set in the data, and a corresponding party    *     is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_party(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PartyModel body: Party object
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_party_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_party_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_party_with_http_info(self, **kwargs):  # noqa: E501
        """Create or update an Party  # noqa: E501

        Create or update an Party. If id or links are set in the data, and a corresponding party    *     is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_party_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PartyModel body: Party object
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
                    " to method create_party" % key
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
            '/party', 'POST',
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

    def delete_party(self, party_id, **kwargs):  # noqa: E501
        """Delete an party  # noqa: E501

        Delete an party  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_party(party_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int party_id: ID of the party to delete (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_party_with_http_info(party_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_party_with_http_info(party_id, **kwargs)  # noqa: E501
            return data

    def delete_party_with_http_info(self, party_id, **kwargs):  # noqa: E501
        """Delete an party  # noqa: E501

        Delete an party  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_party_with_http_info(party_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int party_id: ID of the party to delete (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['party_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_party" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'party_id' is set
        if self.api_client.client_side_validation and ('party_id' not in params or
                                                       params['party_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `party_id` when calling `delete_party`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'party_id' in params:
            path_params['partyId'] = params['party_id']  # noqa: E501

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
            '/party/{partyId}', 'DELETE',
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

    def retrieve_list_party(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Parties  # noqa: E501

        Retrieve List of Parties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_party(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PartyRetrieveListArguments arguments: Party RetrieveList Arguments (required)
        :return: PartyListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_list_party_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_list_party_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def retrieve_list_party_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Parties  # noqa: E501

        Retrieve List of Parties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_party_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PartyRetrieveListArguments arguments: Party RetrieveList Arguments (required)
        :return: PartyListResponse
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
                    " to method retrieve_list_party" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `retrieve_list_party`")  # noqa: E501

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
            '/party', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PartyListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_party(self, party_id, **kwargs):  # noqa: E501
        """Find party by ID  # noqa: E501

        Returns a single party  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_party(party_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int party_id: ID of party to return (required)
        :return: PartyModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_party_with_http_info(party_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_party_with_http_info(party_id, **kwargs)  # noqa: E501
            return data

    def retrieve_party_with_http_info(self, party_id, **kwargs):  # noqa: E501
        """Find party by ID  # noqa: E501

        Returns a single party  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_party_with_http_info(party_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int party_id: ID of party to return (required)
        :return: PartyModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['party_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_party" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'party_id' is set
        if self.api_client.client_side_validation and ('party_id' not in params or
                                                       params['party_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `party_id` when calling `retrieve_party`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'party_id' in params:
            path_params['partyId'] = params['party_id']  # noqa: E501

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
            '/party/{partyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PartyModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_party(self, **kwargs):  # noqa: E501
        """Set (create or update) an Party  # noqa: E501

        Set (create or update) an Party. If id or links are set in the data, and a corresponding party             is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_party(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PartyModel body: Party object
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_party_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.set_party_with_http_info(**kwargs)  # noqa: E501
            return data

    def set_party_with_http_info(self, **kwargs):  # noqa: E501
        """Set (create or update) an Party  # noqa: E501

        Set (create or update) an Party. If id or links are set in the data, and a corresponding party             is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_party_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PartyModel body: Party object
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
                    " to method set_party" % key
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
            '/party/set', 'POST',
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

    def update_party(self, party_id, **kwargs):  # noqa: E501
        """Update a party  # noqa: E501

        Update a party  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_party(party_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int party_id: ID of party to update (required)
        :param PartyModel body: Party object that needs to be updated
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_party_with_http_info(party_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_party_with_http_info(party_id, **kwargs)  # noqa: E501
            return data

    def update_party_with_http_info(self, party_id, **kwargs):  # noqa: E501
        """Update a party  # noqa: E501

        Update a party  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_party_with_http_info(party_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int party_id: ID of party to update (required)
        :param PartyModel body: Party object that needs to be updated
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['party_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_party" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'party_id' is set
        if self.api_client.client_side_validation and ('party_id' not in params or
                                                       params['party_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `party_id` when calling `update_party`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'party_id' in params:
            path_params['partyId'] = params['party_id']  # noqa: E501

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
            '/party/{partyId}', 'PUT',
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
