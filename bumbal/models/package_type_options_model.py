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


class PackageTypeOptionsModel(object):
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
        'include_record_info': 'bool',
        'include_links': 'bool',
        'include_meta_data': 'bool'
    }

    attribute_map = {
        'include_record_info': 'include_record_info',
        'include_links': 'include_links',
        'include_meta_data': 'include_meta_data'
    }

    def __init__(self, include_record_info=None, include_links=None, include_meta_data=None, _configuration=None):  # noqa: E501
        """PackageTypeOptionsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._include_record_info = None
        self._include_links = None
        self._include_meta_data = None
        self.discriminator = None

        if include_record_info is not None:
            self.include_record_info = include_record_info
        if include_links is not None:
            self.include_links = include_links
        if include_meta_data is not None:
            self.include_meta_data = include_meta_data

    @property
    def include_record_info(self):
        """Gets the include_record_info of this PackageTypeOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_record_info of this PackageTypeOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_record_info

    @include_record_info.setter
    def include_record_info(self, include_record_info):
        """Sets the include_record_info of this PackageTypeOptionsModel.

          # noqa: E501

        :param include_record_info: The include_record_info of this PackageTypeOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_record_info = include_record_info

    @property
    def include_links(self):
        """Gets the include_links of this PackageTypeOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_links of this PackageTypeOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_links

    @include_links.setter
    def include_links(self, include_links):
        """Sets the include_links of this PackageTypeOptionsModel.

          # noqa: E501

        :param include_links: The include_links of this PackageTypeOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_links = include_links

    @property
    def include_meta_data(self):
        """Gets the include_meta_data of this PackageTypeOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_meta_data of this PackageTypeOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_meta_data

    @include_meta_data.setter
    def include_meta_data(self, include_meta_data):
        """Sets the include_meta_data of this PackageTypeOptionsModel.

          # noqa: E501

        :param include_meta_data: The include_meta_data of this PackageTypeOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_meta_data = include_meta_data

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
        if issubclass(PackageTypeOptionsModel, dict):
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
        if not isinstance(other, PackageTypeOptionsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PackageTypeOptionsModel):
            return True

        return self.to_dict() != other.to_dict()
