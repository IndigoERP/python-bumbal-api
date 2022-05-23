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


class NotificationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_notification(self, **kwargs):  # noqa: E501
        """Add a new Notification  # noqa: E501

        Add a new Notification  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_notification(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NotificationModel body: Notification object that needs to be created
        :return: ApiResponse20
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_notification_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_notification_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_notification_with_http_info(self, **kwargs):  # noqa: E501
        """Add a new Notification  # noqa: E501

        Add a new Notification  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_notification_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NotificationModel body: Notification object that needs to be created
        :return: ApiResponse20
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
                    " to method create_notification" % key
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
            '/notification', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse20',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_notification(self, notification_id, **kwargs):  # noqa: E501
        """Delete an Notification entry  # noqa: E501

        Delete an Notification entry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_notification(notification_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int notification_id: ID of Notification to delete (required)
        :return: ApiResponse17
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_notification_with_http_info(notification_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_notification_with_http_info(notification_id, **kwargs)  # noqa: E501
            return data

    def delete_notification_with_http_info(self, notification_id, **kwargs):  # noqa: E501
        """Delete an Notification entry  # noqa: E501

        Delete an Notification entry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_notification_with_http_info(notification_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int notification_id: ID of Notification to delete (required)
        :return: ApiResponse17
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['notification_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notification_id' is set
        if self.api_client.client_side_validation and ('notification_id' not in params or
                                                       params['notification_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `notification_id` when calling `delete_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'notification_id' in params:
            path_params['notificationId'] = params['notification_id']  # noqa: E501

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
            '/notification/{notificationId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse17',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_list_notification(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Notification  # noqa: E501

        Retrieve List of Notification  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_notification(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NotificationRetrieveListArguments arguments: Notification RetrieveList Arguments (required)
        :return: NotificationListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_list_notification_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_list_notification_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def retrieve_list_notification_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Notification  # noqa: E501

        Retrieve List of Notification  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_notification_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NotificationRetrieveListArguments arguments: Notification RetrieveList Arguments (required)
        :return: NotificationListResponse
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
                    " to method retrieve_list_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `retrieve_list_notification`")  # noqa: E501

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
            '/notification', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotificationListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_notification(self, notification_id, **kwargs):  # noqa: E501
        """Retrieve a Notification  # noqa: E501

        Retrieve an Notification  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_notification(notification_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int notification_id: ID of Notification to retrieve (required)
        :param bool include_category_type_name: Show the name of the category type
        :param bool include_record_info: Show the record info
        :return: NotificationModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_notification_with_http_info(notification_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_notification_with_http_info(notification_id, **kwargs)  # noqa: E501
            return data

    def retrieve_notification_with_http_info(self, notification_id, **kwargs):  # noqa: E501
        """Retrieve a Notification  # noqa: E501

        Retrieve an Notification  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_notification_with_http_info(notification_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int notification_id: ID of Notification to retrieve (required)
        :param bool include_category_type_name: Show the name of the category type
        :param bool include_record_info: Show the record info
        :return: NotificationModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['notification_id', 'include_category_type_name', 'include_record_info']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notification_id' is set
        if self.api_client.client_side_validation and ('notification_id' not in params or
                                                       params['notification_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `notification_id` when calling `retrieve_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'notification_id' in params:
            path_params['notificationId'] = params['notification_id']  # noqa: E501

        query_params = []
        if 'include_category_type_name' in params:
            query_params.append(('include_category_type_name', params['include_category_type_name']))  # noqa: E501
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
            '/notification/{notificationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotificationModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_notification(self, **kwargs):  # noqa: E501
        """Set (create or update) a notification  # noqa: E501

        Set (create or update) a notification. If id or links are set in the data, and a corresponding notification is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_notification(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NotificationModel body: Notification object
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_notification_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.set_notification_with_http_info(**kwargs)  # noqa: E501
            return data

    def set_notification_with_http_info(self, **kwargs):  # noqa: E501
        """Set (create or update) a notification  # noqa: E501

        Set (create or update) a notification. If id or links are set in the data, and a corresponding notification is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_notification_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NotificationModel body: Notification object
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
                    " to method set_notification" % key
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
            '/notification/set', 'POST',
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

    def update_notification(self, notification_id, **kwargs):  # noqa: E501
        """Update a specific Notification object  # noqa: E501

        Update a specific Notification object  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_notification(notification_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int notification_id: ID of the Notification object to update (required)
        :param NotificationModel body: Notification object that needs to be updated
        :return: ApiResponse16
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_notification_with_http_info(notification_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_notification_with_http_info(notification_id, **kwargs)  # noqa: E501
            return data

    def update_notification_with_http_info(self, notification_id, **kwargs):  # noqa: E501
        """Update a specific Notification object  # noqa: E501

        Update a specific Notification object  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_notification_with_http_info(notification_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int notification_id: ID of the Notification object to update (required)
        :param NotificationModel body: Notification object that needs to be updated
        :return: ApiResponse16
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['notification_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notification_id' is set
        if self.api_client.client_side_validation and ('notification_id' not in params or
                                                       params['notification_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `notification_id` when calling `update_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'notification_id' in params:
            path_params['notificationId'] = params['notification_id']  # noqa: E501

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
            '/notification/{notificationId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse16',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
