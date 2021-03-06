# coding: utf-8

"""
    Bumbal Client Api

    Bumbal API documentation  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: gerb@bumbal.eu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from bumbal.configuration import Configuration


class QuestionnaireChangeLanguageResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'success': 'list[int]',
        'failed': 'list[int]',
        'new_lang_code': 'str',
        'old_lang_code': 'str'
    }

    attribute_map = {
        'success': 'success',
        'failed': 'failed',
        'new_lang_code': 'new_lang_code',
        'old_lang_code': 'old_lang_code'
    }

    def __init__(self, success=None, failed=None, new_lang_code=None, old_lang_code=None, _configuration=None):  # noqa: E501
        """QuestionnaireChangeLanguageResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._success = None
        self._failed = None
        self._new_lang_code = None
        self._old_lang_code = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if failed is not None:
            self.failed = failed
        if new_lang_code is not None:
            self.new_lang_code = new_lang_code
        if old_lang_code is not None:
            self.old_lang_code = old_lang_code

    @property
    def success(self):
        """Gets the success of this QuestionnaireChangeLanguageResponse.  # noqa: E501

        List with answer id's succesful updated  # noqa: E501

        :return: The success of this QuestionnaireChangeLanguageResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this QuestionnaireChangeLanguageResponse.

        List with answer id's succesful updated  # noqa: E501

        :param success: The success of this QuestionnaireChangeLanguageResponse.  # noqa: E501
        :type: list[int]
        """

        self._success = success

    @property
    def failed(self):
        """Gets the failed of this QuestionnaireChangeLanguageResponse.  # noqa: E501

        List with answer id's failed to update  # noqa: E501

        :return: The failed of this QuestionnaireChangeLanguageResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this QuestionnaireChangeLanguageResponse.

        List with answer id's failed to update  # noqa: E501

        :param failed: The failed of this QuestionnaireChangeLanguageResponse.  # noqa: E501
        :type: list[int]
        """

        self._failed = failed

    @property
    def new_lang_code(self):
        """Gets the new_lang_code of this QuestionnaireChangeLanguageResponse.  # noqa: E501

        New Language Code  # noqa: E501

        :return: The new_lang_code of this QuestionnaireChangeLanguageResponse.  # noqa: E501
        :rtype: str
        """
        return self._new_lang_code

    @new_lang_code.setter
    def new_lang_code(self, new_lang_code):
        """Sets the new_lang_code of this QuestionnaireChangeLanguageResponse.

        New Language Code  # noqa: E501

        :param new_lang_code: The new_lang_code of this QuestionnaireChangeLanguageResponse.  # noqa: E501
        :type: str
        """

        self._new_lang_code = new_lang_code

    @property
    def old_lang_code(self):
        """Gets the old_lang_code of this QuestionnaireChangeLanguageResponse.  # noqa: E501

        Old Language code  # noqa: E501

        :return: The old_lang_code of this QuestionnaireChangeLanguageResponse.  # noqa: E501
        :rtype: str
        """
        return self._old_lang_code

    @old_lang_code.setter
    def old_lang_code(self, old_lang_code):
        """Sets the old_lang_code of this QuestionnaireChangeLanguageResponse.

        Old Language code  # noqa: E501

        :param old_lang_code: The old_lang_code of this QuestionnaireChangeLanguageResponse.  # noqa: E501
        :type: str
        """

        self._old_lang_code = old_lang_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(QuestionnaireChangeLanguageResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QuestionnaireChangeLanguageResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QuestionnaireChangeLanguageResponse):
            return True

        return self.to_dict() != other.to_dict()
