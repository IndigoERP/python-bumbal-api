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


class ApiResponse11(object):
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
        'type': 'str',
        'code': 'float',
        'additional_data': 'object'
    }

    attribute_map = {
        'message': 'message',
        'type': 'type',
        'code': 'code',
        'additional_data': 'additional_data'
    }

    def __init__(self, message=None, type=None, code=None, additional_data=None, _configuration=None):  # noqa: E501
        """ApiResponse11 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._message = None
        self._type = None
        self._code = None
        self._additional_data = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if type is not None:
            self.type = type
        if code is not None:
            self.code = code
        if additional_data is not None:
            self.additional_data = additional_data

    @property
    def message(self):
        """Gets the message of this ApiResponse11.  # noqa: E501

        Message describing the code  # noqa: E501

        :return: The message of this ApiResponse11.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ApiResponse11.

        Message describing the code  # noqa: E501

        :param message: The message of this ApiResponse11.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def type(self):
        """Gets the type of this ApiResponse11.  # noqa: E501

        Ready  # noqa: E501

        :return: The type of this ApiResponse11.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiResponse11.

        Ready  # noqa: E501

        :param type: The type of this ApiResponse11.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def code(self):
        """Gets the code of this ApiResponse11.  # noqa: E501

          # noqa: E501

        :return: The code of this ApiResponse11.  # noqa: E501
        :rtype: float
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ApiResponse11.

          # noqa: E501

        :param code: The code of this ApiResponse11.  # noqa: E501
        :type: float
        """

        self._code = code

    @property
    def additional_data(self):
        """Gets the additional_data of this ApiResponse11.  # noqa: E501


        :return: The additional_data of this ApiResponse11.  # noqa: E501
        :rtype: object
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data):
        """Sets the additional_data of this ApiResponse11.


        :param additional_data: The additional_data of this ApiResponse11.  # noqa: E501
        :type: object
        """

        self._additional_data = additional_data

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
        if issubclass(ApiResponse11, dict):
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
        if not isinstance(other, ApiResponse11):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiResponse11):
            return True

        return self.to_dict() != other.to_dict()
