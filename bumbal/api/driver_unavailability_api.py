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


class DriverUnavailabilityApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_driver_unavailability(self, **kwargs):  # noqa: E501
        """Add a new DriverUnavailability  # noqa: E501

        Add a new DriverUnavailability  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_driver_unavailability(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverUnavailabilityModel body: DriverUnavailability object that needs to be created
        :return: ApiResponse4
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_driver_unavailability_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_driver_unavailability_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_driver_unavailability_with_http_info(self, **kwargs):  # noqa: E501
        """Add a new DriverUnavailability  # noqa: E501

        Add a new DriverUnavailability  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_driver_unavailability_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverUnavailabilityModel body: DriverUnavailability object that needs to be created
        :return: ApiResponse4
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
                    " to method create_driver_unavailability" % key
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
            '/driver-unavailability', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse4',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_driver_unavailability(self, driverunavailability_id, **kwargs):  # noqa: E501
        """Delete a DriverUnavailability entry  # noqa: E501

        Delete a Metadata entry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_driver_unavailability(driverunavailability_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driverunavailability_id: ID of DriverUnavailability to delete (required)
        :return: ApiResponse2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_driver_unavailability_with_http_info(driverunavailability_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_driver_unavailability_with_http_info(driverunavailability_id, **kwargs)  # noqa: E501
            return data

    def delete_driver_unavailability_with_http_info(self, driverunavailability_id, **kwargs):  # noqa: E501
        """Delete a DriverUnavailability entry  # noqa: E501

        Delete a Metadata entry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_driver_unavailability_with_http_info(driverunavailability_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driverunavailability_id: ID of DriverUnavailability to delete (required)
        :return: ApiResponse2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['driverunavailability_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_driver_unavailability" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'driverunavailability_id' is set
        if self.api_client.client_side_validation and ('driverunavailability_id' not in params or
                                                       params['driverunavailability_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `driverunavailability_id` when calling `delete_driver_unavailability`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'driverunavailability_id' in params:
            path_params['driverunavailabilityId'] = params['driverunavailability_id']  # noqa: E501

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
            '/driver-unavailability/{driverunavailabilityId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_driver_unavailability(self, driverunavailability_id, **kwargs):  # noqa: E501
        """Retrieve a DriverUnavailability  # noqa: E501

        Retrieve an DriverUnavailability  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_driver_unavailability(driverunavailability_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driverunavailability_id: ID of DriverUnavailability to retrieve (required)
        :param bool include_object_type_name: Show the name of the object type
        :param bool include_record_info: Show the record info
        :return: DriverUnavailabilityModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_driver_unavailability_with_http_info(driverunavailability_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_driver_unavailability_with_http_info(driverunavailability_id, **kwargs)  # noqa: E501
            return data

    def retrieve_driver_unavailability_with_http_info(self, driverunavailability_id, **kwargs):  # noqa: E501
        """Retrieve a DriverUnavailability  # noqa: E501

        Retrieve an DriverUnavailability  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_driver_unavailability_with_http_info(driverunavailability_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driverunavailability_id: ID of DriverUnavailability to retrieve (required)
        :param bool include_object_type_name: Show the name of the object type
        :param bool include_record_info: Show the record info
        :return: DriverUnavailabilityModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['driverunavailability_id', 'include_object_type_name', 'include_record_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_driver_unavailability" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'driverunavailability_id' is set
        if self.api_client.client_side_validation and ('driverunavailability_id' not in params or
                                                       params['driverunavailability_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `driverunavailability_id` when calling `retrieve_driver_unavailability`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'driverunavailability_id' in params:
            path_params['driverunavailabilityId'] = params['driverunavailability_id']  # noqa: E501

        query_params = []
        if 'include_object_type_name' in params:
            query_params.append(('include_object_type_name', params['include_object_type_name']))  # noqa: E501
        if 'include_record_info' in params:
            query_params.append(('include_record_info', params['include_record_info']))  # noqa: E501

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
            '/driver-unavailability/{driverunavailabilityId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DriverUnavailabilityModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_list_driver_unavailability(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of DriverUnavailability  # noqa: E501

        Retrieve List of DriverUnavailability  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_driver_unavailability(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverUnavailabilityRetrieveListArguments arguments: DriverUnavailability RetrieveList Arguments (required)
        :return: DriverUnavailabilityListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_list_driver_unavailability_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_list_driver_unavailability_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def retrieve_list_driver_unavailability_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of DriverUnavailability  # noqa: E501

        Retrieve List of DriverUnavailability  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_driver_unavailability_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverUnavailabilityRetrieveListArguments arguments: DriverUnavailability RetrieveList Arguments (required)
        :return: DriverUnavailabilityListResponse
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
                    " to method retrieve_list_driver_unavailability" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `retrieve_list_driver_unavailability`")  # noqa: E501

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
            '/driver-unavailability', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DriverUnavailabilityListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_driver_unavailability(self, **kwargs):  # noqa: E501
        """Set (create or update) a driver unavailability  # noqa: E501

        Set (create or update) a driver unavailability. If id or links are set in the data, and a corresponding driver unavailability is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_driver_unavailability(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverUnavailabilityModel body: DriverUnavailability object
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_driver_unavailability_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.set_driver_unavailability_with_http_info(**kwargs)  # noqa: E501
            return data

    def set_driver_unavailability_with_http_info(self, **kwargs):  # noqa: E501
        """Set (create or update) a driver unavailability  # noqa: E501

        Set (create or update) a driver unavailability. If id or links are set in the data, and a corresponding driver unavailability is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_driver_unavailability_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverUnavailabilityModel body: DriverUnavailability object
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
                    " to method set_driver_unavailability" % key
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
            '/driver-unavailability/set', 'POST',
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

    def update_driver_unavailability(self, driverunavailability_id, **kwargs):  # noqa: E501
        """Update a specific DriverUnavailability object  # noqa: E501

        Update a specific DriverUnavailability object  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_driver_unavailability(driverunavailability_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driverunavailability_id: ID of the DriverUnavailability object to update (required)
        :param DriverUnavailabilityModel body: DriverUnavailability object that needs to be updated
        :return: ApiResponse1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_driver_unavailability_with_http_info(driverunavailability_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_driver_unavailability_with_http_info(driverunavailability_id, **kwargs)  # noqa: E501
            return data

    def update_driver_unavailability_with_http_info(self, driverunavailability_id, **kwargs):  # noqa: E501
        """Update a specific DriverUnavailability object  # noqa: E501

        Update a specific DriverUnavailability object  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_driver_unavailability_with_http_info(driverunavailability_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driverunavailability_id: ID of the DriverUnavailability object to update (required)
        :param DriverUnavailabilityModel body: DriverUnavailability object that needs to be updated
        :return: ApiResponse1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['driverunavailability_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_driver_unavailability" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'driverunavailability_id' is set
        if self.api_client.client_side_validation and ('driverunavailability_id' not in params or
                                                       params['driverunavailability_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `driverunavailability_id` when calling `update_driver_unavailability`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'driverunavailability_id' in params:
            path_params['driverunavailabilityId'] = params['driverunavailability_id']  # noqa: E501

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
            '/driver-unavailability/{driverunavailabilityId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
