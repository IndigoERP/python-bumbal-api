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


class FileCopyArguments(object):
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
        'source_file_id': 'int',
        'target_object_id': 'int',
        'target_object_type': 'int'
    }

    attribute_map = {
        'source_file_id': 'source_file_id',
        'target_object_id': 'target_object_id',
        'target_object_type': 'target_object_type'
    }

    def __init__(self, source_file_id=None, target_object_id=None, target_object_type=None, _configuration=None):  # noqa: E501
        """FileCopyArguments - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._source_file_id = None
        self._target_object_id = None
        self._target_object_type = None
        self.discriminator = None

        if source_file_id is not None:
            self.source_file_id = source_file_id
        if target_object_id is not None:
            self.target_object_id = target_object_id
        if target_object_type is not None:
            self.target_object_type = target_object_type

    @property
    def source_file_id(self):
        """Gets the source_file_id of this FileCopyArguments.  # noqa: E501

          # noqa: E501

        :return: The source_file_id of this FileCopyArguments.  # noqa: E501
        :rtype: int
        """
        return self._source_file_id

    @source_file_id.setter
    def source_file_id(self, source_file_id):
        """Sets the source_file_id of this FileCopyArguments.

          # noqa: E501

        :param source_file_id: The source_file_id of this FileCopyArguments.  # noqa: E501
        :type: int
        """

        self._source_file_id = source_file_id

    @property
    def target_object_id(self):
        """Gets the target_object_id of this FileCopyArguments.  # noqa: E501

          # noqa: E501

        :return: The target_object_id of this FileCopyArguments.  # noqa: E501
        :rtype: int
        """
        return self._target_object_id

    @target_object_id.setter
    def target_object_id(self, target_object_id):
        """Sets the target_object_id of this FileCopyArguments.

          # noqa: E501

        :param target_object_id: The target_object_id of this FileCopyArguments.  # noqa: E501
        :type: int
        """

        self._target_object_id = target_object_id

    @property
    def target_object_type(self):
        """Gets the target_object_type of this FileCopyArguments.  # noqa: E501

          # noqa: E501

        :return: The target_object_type of this FileCopyArguments.  # noqa: E501
        :rtype: int
        """
        return self._target_object_type

    @target_object_type.setter
    def target_object_type(self, target_object_type):
        """Sets the target_object_type of this FileCopyArguments.

          # noqa: E501

        :param target_object_type: The target_object_type of this FileCopyArguments.  # noqa: E501
        :type: int
        """

        self._target_object_type = target_object_type

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
        if issubclass(FileCopyArguments, dict):
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
        if not isinstance(other, FileCopyArguments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileCopyArguments):
            return True

        return self.to_dict() != other.to_dict()