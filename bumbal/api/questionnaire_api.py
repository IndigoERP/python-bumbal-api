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


class QuestionnaireApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_language(self, arguments, **kwargs):  # noqa: E501
        """change language of a Questionnaire  # noqa: E501

        change language of a Questionnaire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_language(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionnaireChangeLanguageArguments arguments: Request Arguments (required)
        :return: QuestionnaireChangeLanguageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_language_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.change_language_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def change_language_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """change language of a Questionnaire  # noqa: E501

        change language of a Questionnaire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_language_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionnaireChangeLanguageArguments arguments: Request Arguments (required)
        :return: QuestionnaireChangeLanguageResponse
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
                    " to method change_language" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `change_language`")  # noqa: E501

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
            '/questionnaire/change-language', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuestionnaireChangeLanguageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_questionnaire(self, notification_id, **kwargs):  # noqa: E501
        """Delete an Questionnaire entry  # noqa: E501

        Delete an Questionnaire entry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_questionnaire(notification_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int notification_id: ID of Questionnaire to delete (required)
        :return: ApiResponse27
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_questionnaire_with_http_info(notification_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_questionnaire_with_http_info(notification_id, **kwargs)  # noqa: E501
            return data

    def delete_questionnaire_with_http_info(self, notification_id, **kwargs):  # noqa: E501
        """Delete an Questionnaire entry  # noqa: E501

        Delete an Questionnaire entry  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_questionnaire_with_http_info(notification_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int notification_id: ID of Questionnaire to delete (required)
        :return: ApiResponse27
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
                    " to method delete_questionnaire" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notification_id' is set
        if self.api_client.client_side_validation and ('notification_id' not in params or
                                                       params['notification_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `notification_id` when calling `delete_questionnaire`")  # noqa: E501

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
            '/questionnaire/{questionnaireId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponse27',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_next_question(self, arguments, **kwargs):  # noqa: E501
        """getNextQuestion of an Questionnaire  # noqa: E501

        getNextQuestion of an Questionnaire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_next_question(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionnaireGetNextQuestionArguments arguments: Request Arguments (required)
        :return: QuestionnaireQuestionModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_next_question_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_next_question_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def get_next_question_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """getNextQuestion of an Questionnaire  # noqa: E501

        getNextQuestion of an Questionnaire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_next_question_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionnaireGetNextQuestionArguments arguments: Request Arguments (required)
        :return: QuestionnaireQuestionModel
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
                    " to method get_next_question" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `get_next_question`")  # noqa: E501

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
            '/questionnaire/get-next-question', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuestionnaireQuestionModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_previous_question(self, arguments, **kwargs):  # noqa: E501
        """getPreviousQuestion of an Questionnaire  # noqa: E501

        getPreviousQuestion of an Questionnaire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_previous_question(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionnaireGetPreviousQuestionArguments arguments: Request Arguments (required)
        :return: QuestionnaireQuestionModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_previous_question_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.get_previous_question_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def get_previous_question_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """getPreviousQuestion of an Questionnaire  # noqa: E501

        getPreviousQuestion of an Questionnaire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_previous_question_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionnaireGetPreviousQuestionArguments arguments: Request Arguments (required)
        :return: QuestionnaireQuestionModel
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
                    " to method get_previous_question" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `get_previous_question`")  # noqa: E501

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
            '/questionnaire/get-previous-question', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuestionnaireQuestionModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_list_questionnaire(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Questionnaire  # noqa: E501

        Retrieve List of Questionnaire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_questionnaire(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionnaireRetrieveListArguments arguments: Questionnaire RetrieveList Arguments (required)
        :return: QuestionnaireListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_list_questionnaire_with_http_info(arguments, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_list_questionnaire_with_http_info(arguments, **kwargs)  # noqa: E501
            return data

    def retrieve_list_questionnaire_with_http_info(self, arguments, **kwargs):  # noqa: E501
        """Retrieve List of Questionnaire  # noqa: E501

        Retrieve List of Questionnaire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_list_questionnaire_with_http_info(arguments, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QuestionnaireRetrieveListArguments arguments: Questionnaire RetrieveList Arguments (required)
        :return: QuestionnaireListResponse
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
                    " to method retrieve_list_questionnaire" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'arguments' is set
        if self.api_client.client_side_validation and ('arguments' not in params or
                                                       params['arguments'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `arguments` when calling `retrieve_list_questionnaire`")  # noqa: E501

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
            '/questionnaire', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuestionnaireListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_questionnaire(self, notification_id, include_answers, **kwargs):  # noqa: E501
        """Retrieve a Questionnaire  # noqa: E501

        Retrieve an Questionnaire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_questionnaire(notification_id, include_answers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int notification_id: ID of Questionnaire to retrieve (required)
        :param bool include_answers: Include answers (required)
        :return: QuestionnaireModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_questionnaire_with_http_info(notification_id, include_answers, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_questionnaire_with_http_info(notification_id, include_answers, **kwargs)  # noqa: E501
            return data

    def retrieve_questionnaire_with_http_info(self, notification_id, include_answers, **kwargs):  # noqa: E501
        """Retrieve a Questionnaire  # noqa: E501

        Retrieve an Questionnaire  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_questionnaire_with_http_info(notification_id, include_answers, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int notification_id: ID of Questionnaire to retrieve (required)
        :param bool include_answers: Include answers (required)
        :return: QuestionnaireModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['notification_id', 'include_answers']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_questionnaire" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notification_id' is set
        if self.api_client.client_side_validation and ('notification_id' not in params or
                                                       params['notification_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `notification_id` when calling `retrieve_questionnaire`")  # noqa: E501
        # verify the required parameter 'include_answers' is set
        if self.api_client.client_side_validation and ('include_answers' not in params or
                                                       params['include_answers'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `include_answers` when calling `retrieve_questionnaire`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'notification_id' in params:
            path_params['notificationId'] = params['notification_id']  # noqa: E501
        if 'include_answers' in params:
            path_params['include_answers'] = params['include_answers']  # noqa: E501

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
            '/questionnaire/{questionnaireId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuestionnaireModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
