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


class ApiResponse28(object):
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
        'message': 'str',
        'code': 'float'
    }

    attribute_map = {
        'message': 'message',
        'code': 'code'
    }

    def __init__(self, message=None, code=None, _configuration=None):  # noqa: E501
        """ApiResponse28 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._code = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    @property
    def message(self):
        """Gets the message of this ApiResponse28.  # noqa: E501

        Message describing the error  # noqa: E501

        :return: The message of this ApiResponse28.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ApiResponse28.

        Message describing the error  # noqa: E501

        :param message: The message of this ApiResponse28.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def code(self):
        """Gets the code of this ApiResponse28.  # noqa: E501

        Error code  # noqa: E501

        :return: The code of this ApiResponse28.  # noqa: E501
        :rtype: float
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ApiResponse28.

        Error code  # noqa: E501

        :param code: The code of this ApiResponse28.  # noqa: E501
        :type: float
        """

        self._code = code

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
        if issubclass(ApiResponse28, dict):
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
        if not isinstance(other, ApiResponse28):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiResponse28):
            return True

        return self.to_dict() != other.to_dict()