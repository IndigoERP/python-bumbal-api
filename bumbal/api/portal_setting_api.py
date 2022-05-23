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


class PortalSettingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_portal_setting(self, **kwargs):  # noqa: E501
        """Add a new PortalSetting  # noqa: E501

        Add a new PortalSetting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_portal_setting(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortalSettingModel body: PortalSetting object that needs to be created
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_portal_setting_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_portal_setting_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_portal_setting_with_http_info(self, **kwargs):  # noqa: E501
        """Add a new PortalSetting  # noqa: E501

        Add a new PortalSetting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_portal_setting_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortalSettingModel body: PortalSetting object that needs to be created
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
                    " to method create_portal_setting" % key
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
            '/portal-setting', 'POST',
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

    def delete_portal_setting(self, portal_setting_id, **kwargs):  # noqa: E501
        """Delete a PortalSetting  # noqa: E501

        Delete a PortalSetting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_portal_setting(portal_setting_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int portal_setting_id: ID of portal-setting to delete (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_portal_setting_with_http_info(portal_setting_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_portal_setting_with_http_info(portal_setting_id, **kwargs)  # noqa: E501
            return data

    def delete_portal_setting_with_http_info(self, portal_setting_id, **kwargs):  # noqa: E501
        """Delete a PortalSetting  # noqa: E501

        Delete a PortalSetting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_portal_setting_with_http_info(portal_setting_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int portal_setting_id: ID of portal-setting to delete (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['portal_setting_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_portal_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'portal_setting_id' is set
        if self.api_client.client_side_validation and ('portal_setting_id' not in params or
                                                       params['portal_setting_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `portal_setting_id` when calling `delete_portal_setting`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'portal_setting_id' in params:
            path_params['portal-settingId'] = params['portal_setting_id']  # noqa: E501

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
            '/portal-setting/{portal-settingId}', 'DELETE',
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

    def retrieve_list_portal_setting(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Portal Settings  # noqa: E501

        Retrieve List of Portal Settings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_portal_setting(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortalSettingRetrieveListArguments arguments: PortalSetting RetrieveList Arguments (required)
        :return: PortalSettingListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_list_portal_setting_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_list_portal_setting_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def retrieve_list_portal_setting_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Portal Settings  # noqa: E501

        Retrieve List of Portal Settings  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_portal_setting_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortalSettingRetrieveListArguments arguments: PortalSetting RetrieveList Arguments (required)
        :return: PortalSettingListResponse
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
                    " to method retrieve_list_portal_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `retrieve_list_portal_setting`")  # noqa: E501

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
            '/portal-setting', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortalSettingListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_portal_setting(self, portal_setting_id, **kwargs):  # noqa: E501
        """Retrieve a PortalSetting  # noqa: E501

        Retrieve an PortalSetting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_portal_setting(portal_setting_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int portal_setting_id: ID of portal-setting to retrieve (required)
        :return: PortalSettingModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_portal_setting_with_http_info(portal_setting_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_portal_setting_with_http_info(portal_setting_id, **kwargs)  # noqa: E501
            return data

    def retrieve_portal_setting_with_http_info(self, portal_setting_id, **kwargs):  # noqa: E501
        """Retrieve a PortalSetting  # noqa: E501

        Retrieve an PortalSetting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_portal_setting_with_http_info(portal_setting_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int portal_setting_id: ID of portal-setting to retrieve (required)
        :return: PortalSettingModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['portal_setting_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_portal_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'portal_setting_id' is set
        if self.api_client.client_side_validation and ('portal_setting_id' not in params or
                                                       params['portal_setting_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `portal_setting_id` when calling `retrieve_portal_setting`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'portal_setting_id' in params:
            path_params['portal-settingId'] = params['portal_setting_id']  # noqa: E501

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
            '/portal-setting/{portal-settingId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortalSettingModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_portal_setting(self, **kwargs):  # noqa: E501
        """Set (create or update) a PortalSetting  # noqa: E501

        Set (create or update) a PortalSetting. If id or links are set in the data, and a corresponding portal-setting is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_portal_setting(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortalSettingModel body: PortalSetting object
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_portal_setting_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.set_portal_setting_with_http_info(**kwargs)  # noqa: E501
            return data

    def set_portal_setting_with_http_info(self, **kwargs):  # noqa: E501
        """Set (create or update) a PortalSetting  # noqa: E501

        Set (create or update) a PortalSetting. If id or links are set in the data, and a corresponding portal-setting is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_portal_setting_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PortalSettingModel body: PortalSetting object
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
                    " to method set_portal_setting" % key
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
            '/portal-setting/set', 'POST',
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

    def update_portal_setting(self, portal_setting_id, **kwargs):  # noqa: E501
        """Update a PortalSetting  # noqa: E501

        Update an PortalSetting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_portal_setting(portal_setting_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int portal_setting_id: ID of portal-setting to update (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_portal_setting_with_http_info(portal_setting_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_portal_setting_with_http_info(portal_setting_id, **kwargs)  # noqa: E501
            return data

    def update_portal_setting_with_http_info(self, portal_setting_id, **kwargs):  # noqa: E501
        """Update a PortalSetting  # noqa: E501

        Update an PortalSetting  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_portal_setting_with_http_info(portal_setting_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int portal_setting_id: ID of portal-setting to update (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['portal_setting_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_portal_setting" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'portal_setting_id' is set
        if self.api_client.client_side_validation and ('portal_setting_id' not in params or
                                                       params['portal_setting_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `portal_setting_id` when calling `update_portal_setting`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'portal_setting_id' in params:
            path_params['portal-settingId'] = params['portal_setting_id']  # noqa: E501

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
            '/portal-setting/{portal-settingId}', 'PUT',
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