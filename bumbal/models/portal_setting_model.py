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


class PortalSettingModel(object):
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
        'id': 'int',
        'name': 'str',
        'value': 'str',
        'portal_setting_group_name': 'str',
        'portal_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'value': 'value',
        'portal_setting_group_name': 'portal_setting_group_name',
        'portal_name': 'portal_name'
    }

    def __init__(self, id=None, name=None, value=None, portal_setting_group_name=None, portal_name=None, _configuration=None):  # noqa: E501
        """PortalSettingModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._value = None
        self._portal_setting_group_name = None
        self._portal_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if portal_setting_group_name is not None:
            self.portal_setting_group_name = portal_setting_group_name
        if portal_name is not None:
            self.portal_name = portal_name

    @property
    def id(self):
        """Gets the id of this PortalSettingModel.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this PortalSettingModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortalSettingModel.

        Unique Identifier  # noqa: E501

        :param id: The id of this PortalSettingModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PortalSettingModel.  # noqa: E501

        Name of portal setting  # noqa: E501

        :return: The name of this PortalSettingModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PortalSettingModel.

        Name of portal setting  # noqa: E501

        :param name: The name of this PortalSettingModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this PortalSettingModel.  # noqa: E501

        Value of portal setting  # noqa: E501

        :return: The value of this PortalSettingModel.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PortalSettingModel.

        Value of portal setting  # noqa: E501

        :param value: The value of this PortalSettingModel.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def portal_setting_group_name(self):
        """Gets the portal_setting_group_name of this PortalSettingModel.  # noqa: E501

        Name of portal settings group  # noqa: E501

        :return: The portal_setting_group_name of this PortalSettingModel.  # noqa: E501
        :rtype: str
        """
        return self._portal_setting_group_name

    @portal_setting_group_name.setter
    def portal_setting_group_name(self, portal_setting_group_name):
        """Sets the portal_setting_group_name of this PortalSettingModel.

        Name of portal settings group  # noqa: E501

        :param portal_setting_group_name: The portal_setting_group_name of this PortalSettingModel.  # noqa: E501
        :type: str
        """

        self._portal_setting_group_name = portal_setting_group_name

    @property
    def portal_name(self):
        """Gets the portal_name of this PortalSettingModel.  # noqa: E501

        Name of portal  # noqa: E501

        :return: The portal_name of this PortalSettingModel.  # noqa: E501
        :rtype: str
        """
        return self._portal_name

    @portal_name.setter
    def portal_name(self, portal_name):
        """Sets the portal_name of this PortalSettingModel.

        Name of portal  # noqa: E501

        :param portal_name: The portal_name of this PortalSettingModel.  # noqa: E501
        :type: str
        """

        self._portal_name = portal_name

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
        if issubclass(PortalSettingModel, dict):
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
        if not isinstance(other, PortalSettingModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortalSettingModel):
            return True

        return self.to_dict() != other.to_dict()
