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


class FileOptionsModel(object):
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
        'include_meta_data': 'bool',
        'include_tag_type_name': 'bool',
        'include_file_tags': 'bool',
        'include_file_record_info': 'bool',
        'include_file_base64': 'bool',
        'include_links': 'bool'
    }

    attribute_map = {
        'include_meta_data': 'include_meta_data',
        'include_tag_type_name': 'include_tag_type_name',
        'include_file_tags': 'include_file_tags',
        'include_file_record_info': 'include_file_record_info',
        'include_file_base64': 'include_file_base64',
        'include_links': 'include_links'
    }

    def __init__(self, include_meta_data=None, include_tag_type_name=None, include_file_tags=None, include_file_record_info=None, include_file_base64=None, include_links=None, _configuration=None):  # noqa: E501
        """FileOptionsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._include_meta_data = None
        self._include_tag_type_name = None
        self._include_file_tags = None
        self._include_file_record_info = None
        self._include_file_base64 = None
        self._include_links = None
        self.discriminator = None

        if include_meta_data is not None:
            self.include_meta_data = include_meta_data
        if include_tag_type_name is not None:
            self.include_tag_type_name = include_tag_type_name
        if include_file_tags is not None:
            self.include_file_tags = include_file_tags
        if include_file_record_info is not None:
            self.include_file_record_info = include_file_record_info
        if include_file_base64 is not None:
            self.include_file_base64 = include_file_base64
        if include_links is not None:
            self.include_links = include_links

    @property
    def include_meta_data(self):
        """Gets the include_meta_data of this FileOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_meta_data of this FileOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_meta_data

    @include_meta_data.setter
    def include_meta_data(self, include_meta_data):
        """Sets the include_meta_data of this FileOptionsModel.

          # noqa: E501

        :param include_meta_data: The include_meta_data of this FileOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_meta_data = include_meta_data

    @property
    def include_tag_type_name(self):
        """Gets the include_tag_type_name of this FileOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_tag_type_name of this FileOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_tag_type_name

    @include_tag_type_name.setter
    def include_tag_type_name(self, include_tag_type_name):
        """Sets the include_tag_type_name of this FileOptionsModel.

          # noqa: E501

        :param include_tag_type_name: The include_tag_type_name of this FileOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_tag_type_name = include_tag_type_name

    @property
    def include_file_tags(self):
        """Gets the include_file_tags of this FileOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_file_tags of this FileOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_file_tags

    @include_file_tags.setter
    def include_file_tags(self, include_file_tags):
        """Sets the include_file_tags of this FileOptionsModel.

          # noqa: E501

        :param include_file_tags: The include_file_tags of this FileOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_file_tags = include_file_tags

    @property
    def include_file_record_info(self):
        """Gets the include_file_record_info of this FileOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_file_record_info of this FileOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_file_record_info

    @include_file_record_info.setter
    def include_file_record_info(self, include_file_record_info):
        """Sets the include_file_record_info of this FileOptionsModel.

          # noqa: E501

        :param include_file_record_info: The include_file_record_info of this FileOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_file_record_info = include_file_record_info

    @property
    def include_file_base64(self):
        """Gets the include_file_base64 of this FileOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_file_base64 of this FileOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_file_base64

    @include_file_base64.setter
    def include_file_base64(self, include_file_base64):
        """Sets the include_file_base64 of this FileOptionsModel.

          # noqa: E501

        :param include_file_base64: The include_file_base64 of this FileOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_file_base64 = include_file_base64

    @property
    def include_links(self):
        """Gets the include_links of this FileOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_links of this FileOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_links

    @include_links.setter
    def include_links(self, include_links):
        """Sets the include_links of this FileOptionsModel.

          # noqa: E501

        :param include_links: The include_links of this FileOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_links = include_links

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
        if issubclass(FileOptionsModel, dict):
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
        if not isinstance(other, FileOptionsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileOptionsModel):
            return True

        return self.to_dict() != other.to_dict()