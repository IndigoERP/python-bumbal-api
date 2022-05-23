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


class PortalSettingOptionsModel(object):
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
        'include_portal_name': 'bool'
    }

    attribute_map = {
        'include_portal_name': 'include_portal_name'
    }

    def __init__(self, include_portal_name=None, _configuration=None):  # noqa: E501
        """PortalSettingOptionsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._include_portal_name = None
        self.discriminator = None

        if include_portal_name is not None:
            self.include_portal_name = include_portal_name

    @property
    def include_portal_name(self):
        """Gets the include_portal_name of this PortalSettingOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_portal_name of this PortalSettingOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_portal_name

    @include_portal_name.setter
    def include_portal_name(self, include_portal_name):
        """Sets the include_portal_name of this PortalSettingOptionsModel.

          # noqa: E501

        :param include_portal_name: The include_portal_name of this PortalSettingOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_portal_name = include_portal_name

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
        if issubclass(PortalSettingOptionsModel, dict):
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
        if not isinstance(other, PortalSettingOptionsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortalSettingOptionsModel):
            return True

        return self.to_dict() != other.to_dict()
