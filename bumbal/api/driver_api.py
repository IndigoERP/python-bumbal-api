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


class DriverApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_driver(self, **kwargs):  # noqa: E501
        """Add a driver  # noqa: E501

        Add a driver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_driver(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverModel body: Driver object that needs to be created
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_driver_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_driver_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_driver_with_http_info(self, **kwargs):  # noqa: E501
        """Add a driver  # noqa: E501

        Add a driver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_driver_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverModel body: Driver object that needs to be created
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
                    " to method create_driver" % key
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
            '/driver', 'POST',
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

    def delete_driver(self, driver_id, **kwargs):  # noqa: E501
        """Delete an driver  # noqa: E501

        Delete an driver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_driver(driver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driver_id: ID of the driver to delete (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_driver_with_http_info(driver_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_driver_with_http_info(driver_id, **kwargs)  # noqa: E501
            return data

    def delete_driver_with_http_info(self, driver_id, **kwargs):  # noqa: E501
        """Delete an driver  # noqa: E501

        Delete an driver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_driver_with_http_info(driver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driver_id: ID of the driver to delete (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['driver_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_driver" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'driver_id' is set
        if self.api_client.client_side_validation and ('driver_id' not in params or
                                                       params['driver_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `driver_id` when calling `delete_driver`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'driver_id' in params:
            path_params['driverId'] = params['driver_id']  # noqa: E501

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
            '/driver/{driverId}', 'DELETE',
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

    def retrieve_driver(self, driver_id, include_driver_tags, include_updated_by, **kwargs):  # noqa: E501
        """Find driver by ID  # noqa: E501

        Returns a single driver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_driver(driver_id, include_driver_tags, include_updated_by, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driver_id: ID of driver to return (required)
        :param bool include_driver_tags: a list of tags bound to driver (required)
        :param bool include_updated_by: include updated_by_name (required)
        :return: DriverModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_driver_with_http_info(driver_id, include_driver_tags, include_updated_by, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_driver_with_http_info(driver_id, include_driver_tags, include_updated_by, **kwargs)  # noqa: E501
            return data

    def retrieve_driver_with_http_info(self, driver_id, include_driver_tags, include_updated_by, **kwargs):  # noqa: E501
        """Find driver by ID  # noqa: E501

        Returns a single driver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_driver_with_http_info(driver_id, include_driver_tags, include_updated_by, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driver_id: ID of driver to return (required)
        :param bool include_driver_tags: a list of tags bound to driver (required)
        :param bool include_updated_by: include updated_by_name (required)
        :return: DriverModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['driver_id', 'include_driver_tags', 'include_updated_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_driver" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'driver_id' is set
        if self.api_client.client_side_validation and ('driver_id' not in params or
                                                       params['driver_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `driver_id` when calling `retrieve_driver`")  # noqa: E501
        # verify the required parameter 'include_driver_tags' is set
        if self.api_client.client_side_validation and ('include_driver_tags' not in params or
                                                       params['include_driver_tags'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `include_driver_tags` when calling `retrieve_driver`")  # noqa: E501
        # verify the required parameter 'include_updated_by' is set
        if self.api_client.client_side_validation and ('include_updated_by' not in params or
                                                       params['include_updated_by'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `include_updated_by` when calling `retrieve_driver`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'driver_id' in params:
            path_params['driverId'] = params['driver_id']  # noqa: E501

        query_params = []
        if 'include_driver_tags' in params:
            query_params.append(('include_driver_tags', params['include_driver_tags']))  # noqa: E501
        if 'include_updated_by' in params:
            query_params.append(('include_updated_by', params['include_updated_by']))  # noqa: E501

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
            '/driver/{driverId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DriverModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_list_driver(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Drivers  # noqa: E501

        Retrieve List of Drivers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_driver(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverRetrieveListArguments arguments: Driver RetrieveList Arguments (required)
        :return: DriverListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_list_driver_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_list_driver_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def retrieve_list_driver_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Drivers  # noqa: E501

        Retrieve List of Drivers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_driver_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverRetrieveListArguments arguments: Driver RetrieveList Arguments (required)
        :return: DriverListResponse
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
                    " to method retrieve_list_driver" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `retrieve_list_driver`")  # noqa: E501

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
            '/driver', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DriverListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_driver(self, **kwargs):  # noqa: E501
        """Set (create or update) a driver  # noqa: E501

        Set (create or update) a driver. If id or links are set in the data, and a corresponding driver is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_driver(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverModel body: Driver object
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_driver_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.set_driver_with_http_info(**kwargs)  # noqa: E501
            return data

    def set_driver_with_http_info(self, **kwargs):  # noqa: E501
        """Set (create or update) a driver  # noqa: E501

        Set (create or update) a driver. If id or links are set in the data, and a corresponding driver is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_driver_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DriverModel body: Driver object
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
                    " to method set_driver" % key
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
            '/driver/set', 'POST',
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

    def update_driver(self, driver_id, **kwargs):  # noqa: E501
        """Update a driver  # noqa: E501

        Update a driver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_driver(driver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driver_id: ID of driver to update (required)
        :param DriverModel body: Driver object that needs to be updated
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_driver_with_http_info(driver_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_driver_with_http_info(driver_id, **kwargs)  # noqa: E501
            return data

    def update_driver_with_http_info(self, driver_id, **kwargs):  # noqa: E501
        """Update a driver  # noqa: E501

        Update a driver  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_driver_with_http_info(driver_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int driver_id: ID of driver to update (required)
        :param DriverModel body: Driver object that needs to be updated
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['driver_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_driver" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'driver_id' is set
        if self.api_client.client_side_validation and ('driver_id' not in params or
                                                       params['driver_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `driver_id` when calling `update_driver`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'driver_id' in params:
            path_params['driverId'] = params['driver_id']  # noqa: E501

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
            '/driver/{driverId}', 'PUT',
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