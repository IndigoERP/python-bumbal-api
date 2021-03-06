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


class AssignmentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_assignment(self, assignment_id, **kwargs):  # noqa: E501
        """Delete an assignment  # noqa: E501

        Delete an assignment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_assignment(assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assignment_id: ID of the assignment to delete (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_assignment_with_http_info(assignment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_assignment_with_http_info(assignment_id, **kwargs)  # noqa: E501
            return data

    def delete_assignment_with_http_info(self, assignment_id, **kwargs):  # noqa: E501
        """Delete an assignment  # noqa: E501

        Delete an assignment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_assignment_with_http_info(assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assignment_id: ID of the assignment to delete (required)
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assignment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assignment_id' is set
        if self.api_client.client_side_validation and ('assignment_id' not in params or
                                                       params['assignment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `assignment_id` when calling `delete_assignment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assignment_id' in params:
            path_params['assignmentId'] = params['assignment_id']  # noqa: E501

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
            '/assignment/{assignmentId}', 'DELETE',
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

    def retrieve_assignment(self, assignment_id, **kwargs):  # noqa: E501
        """Find assignment by ID  # noqa: E501

        Returns a single assignment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_assignment(assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assignment_id: ID of assignment to return (required)
        :param bool include_activities: Include activities belonging to assignment
        :param bool include_meta_data: Include meta data
        :param bool include_links: Include links
        :param bool include_files: Include files
        :param bool include_tag_ids: Include tag ids
        :param bool include_tag_names: Include tag names
        :param bool include_booking_account: Include booking account
        :param bool include_record_info: Include record info
        :param bool include_record_object: Include record object
        :return: AssignmentModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_assignment_with_http_info(assignment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_assignment_with_http_info(assignment_id, **kwargs)  # noqa: E501
            return data

    def retrieve_assignment_with_http_info(self, assignment_id, **kwargs):  # noqa: E501
        """Find assignment by ID  # noqa: E501

        Returns a single assignment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_assignment_with_http_info(assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assignment_id: ID of assignment to return (required)
        :param bool include_activities: Include activities belonging to assignment
        :param bool include_meta_data: Include meta data
        :param bool include_links: Include links
        :param bool include_files: Include files
        :param bool include_tag_ids: Include tag ids
        :param bool include_tag_names: Include tag names
        :param bool include_booking_account: Include booking account
        :param bool include_record_info: Include record info
        :param bool include_record_object: Include record object
        :return: AssignmentModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assignment_id', 'include_activities', 'include_meta_data', 'include_links', 'include_files', 'include_tag_ids', 'include_tag_names', 'include_booking_account', 'include_record_info', 'include_record_object']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assignment_id' is set
        if self.api_client.client_side_validation and ('assignment_id' not in params or
                                                       params['assignment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `assignment_id` when calling `retrieve_assignment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assignment_id' in params:
            path_params['assignmentId'] = params['assignment_id']  # noqa: E501

        query_params = []
        if 'include_activities' in params:
            query_params.append(('include_activities', params['include_activities']))  # noqa: E501
        if 'include_meta_data' in params:
            query_params.append(('include_meta_data', params['include_meta_data']))  # noqa: E501
        if 'include_links' in params:
            query_params.append(('include_links', params['include_links']))  # noqa: E501
        if 'include_files' in params:
            query_params.append(('include_files', params['include_files']))  # noqa: E501
        if 'include_tag_ids' in params:
            query_params.append(('include_tag_ids', params['include_tag_ids']))  # noqa: E501
        if 'include_tag_names' in params:
            query_params.append(('include_tag_names', params['include_tag_names']))  # noqa: E501
        if 'include_booking_account' in params:
            query_params.append(('include_booking_account', params['include_booking_account']))  # noqa: E501
        if 'include_record_info' in params:
            query_params.append(('include_record_info', params['include_record_info']))  # noqa: E501
        if 'include_record_object' in params:
            query_params.append(('include_record_object', params['include_record_object']))  # noqa: E501

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
            '/assignment/{assignmentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssignmentModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_list_assignment(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Assignments  # noqa: E501

        Retrieve List of Assignments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_assignment(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssignmentRetrieveListArguments arguments: Assignment RetrieveList Arguments (required)
        :return: AssignmentListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_list_assignment_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_list_assignment_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def retrieve_list_assignment_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Assignments  # noqa: E501

        Retrieve List of Assignments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_assignment_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssignmentRetrieveListArguments arguments: Assignment RetrieveList Arguments (required)
        :return: AssignmentListResponse
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
                    " to method retrieve_list_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `retrieve_list_assignment`")  # noqa: E501

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
            '/assignment', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssignmentListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_assignment(self, **kwargs):  # noqa: E501
        """Set (create or update) an Assignment  # noqa: E501

        Set (create or update) an Assignment. If id or links are set in the data, and a corresponding assignment is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_assignment(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssignmentModel body: Assignment object
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.set_assignment_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.set_assignment_with_http_info(**kwargs)  # noqa: E501
            return data

    def set_assignment_with_http_info(self, **kwargs):  # noqa: E501
        """Set (create or update) an Assignment  # noqa: E501

        Set (create or update) an Assignment. If id or links are set in the data, and a corresponding assignment is found in Bumbal, an update will be performed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_assignment_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssignmentModel body: Assignment object
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
                    " to method set_assignment" % key
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
            '/assignment/set', 'POST',
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

    def update_assignment(self, assignment_id, **kwargs):  # noqa: E501
        """Update a assignment  # noqa: E501

        Update a assignment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_assignment(assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assignment_id: ID of assignment to update (required)
        :param AssignmentModel body: Assignment object that needs to be updated
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_assignment_with_http_info(assignment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_assignment_with_http_info(assignment_id, **kwargs)  # noqa: E501
            return data

    def update_assignment_with_http_info(self, assignment_id, **kwargs):  # noqa: E501
        """Update a assignment  # noqa: E501

        Update a assignment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_assignment_with_http_info(assignment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int assignment_id: ID of assignment to update (required)
        :param AssignmentModel body: Assignment object that needs to be updated
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assignment_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_assignment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assignment_id' is set
        if self.api_client.client_side_validation and ('assignment_id' not in params or
                                                       params['assignment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `assignment_id` when calling `update_assignment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assignment_id' in params:
            path_params['assignmentId'] = params['assignment_id']  # noqa: E501

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
            '/assignment/{assignmentId}', 'PUT',
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
