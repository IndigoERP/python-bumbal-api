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


class ServiceWindowsSchemeFiltersModel(object):
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
        'id': 'list[int]',
        'name': 'list[str]',
        'tag_names': 'list[str]',
        'tag_ids': 'list[int]',
        'zone_names': 'list[str]',
        'zone_ids': 'list[int]',
        'brand_names': 'list[str]',
        'brand_ids': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tag_names': 'tag_names',
        'tag_ids': 'tag_ids',
        'zone_names': 'zone_names',
        'zone_ids': 'zone_ids',
        'brand_names': 'brand_names',
        'brand_ids': 'brand_ids'
    }

    def __init__(self, id=None, name=None, tag_names=None, tag_ids=None, zone_names=None, zone_ids=None, brand_names=None, brand_ids=None, _configuration=None):  # noqa: E501
        """ServiceWindowsSchemeFiltersModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._tag_names = None
        self._tag_ids = None
        self._zone_names = None
        self._zone_ids = None
        self._brand_names = None
        self._brand_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tag_names is not None:
            self.tag_names = tag_names
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if zone_names is not None:
            self.zone_names = zone_names
        if zone_ids is not None:
            self.zone_ids = zone_ids
        if brand_names is not None:
            self.brand_names = brand_names
        if brand_ids is not None:
            self.brand_ids = brand_ids

    @property
    def id(self):
        """Gets the id of this ServiceWindowsSchemeFiltersModel.  # noqa: E501

        Service window scheme id's to filter by  # noqa: E501

        :return: The id of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceWindowsSchemeFiltersModel.

        Service window scheme id's to filter by  # noqa: E501

        :param id: The id of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ServiceWindowsSchemeFiltersModel.  # noqa: E501

        Name of the service windows scheme(s) to filter by  # noqa: E501

        :return: The name of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceWindowsSchemeFiltersModel.

        Name of the service windows scheme(s) to filter by  # noqa: E501

        :param name: The name of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._name = name

    @property
    def tag_names(self):
        """Gets the tag_names of this ServiceWindowsSchemeFiltersModel.  # noqa: E501

        tags to filter by  # noqa: E501

        :return: The tag_names of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """Sets the tag_names of this ServiceWindowsSchemeFiltersModel.

        tags to filter by  # noqa: E501

        :param tag_names: The tag_names of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._tag_names = tag_names

    @property
    def tag_ids(self):
        """Gets the tag_ids of this ServiceWindowsSchemeFiltersModel.  # noqa: E501

        tag ID's to filter by  # noqa: E501

        :return: The tag_ids of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this ServiceWindowsSchemeFiltersModel.

        tag ID's to filter by  # noqa: E501

        :param tag_ids: The tag_ids of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._tag_ids = tag_ids

    @property
    def zone_names(self):
        """Gets the zone_names of this ServiceWindowsSchemeFiltersModel.  # noqa: E501

        zones to filter by  # noqa: E501

        :return: The zone_names of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_names

    @zone_names.setter
    def zone_names(self, zone_names):
        """Sets the zone_names of this ServiceWindowsSchemeFiltersModel.

        zones to filter by  # noqa: E501

        :param zone_names: The zone_names of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._zone_names = zone_names

    @property
    def zone_ids(self):
        """Gets the zone_ids of this ServiceWindowsSchemeFiltersModel.  # noqa: E501

        zone ID's to filter by  # noqa: E501

        :return: The zone_ids of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this ServiceWindowsSchemeFiltersModel.

        zone ID's to filter by  # noqa: E501

        :param zone_ids: The zone_ids of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._zone_ids = zone_ids

    @property
    def brand_names(self):
        """Gets the brand_names of this ServiceWindowsSchemeFiltersModel.  # noqa: E501

        brands to filter by  # noqa: E501

        :return: The brand_names of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._brand_names

    @brand_names.setter
    def brand_names(self, brand_names):
        """Sets the brand_names of this ServiceWindowsSchemeFiltersModel.

        brands to filter by  # noqa: E501

        :param brand_names: The brand_names of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._brand_names = brand_names

    @property
    def brand_ids(self):
        """Gets the brand_ids of this ServiceWindowsSchemeFiltersModel.  # noqa: E501

        brand ID's to filter by  # noqa: E501

        :return: The brand_ids of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._brand_ids

    @brand_ids.setter
    def brand_ids(self, brand_ids):
        """Sets the brand_ids of this ServiceWindowsSchemeFiltersModel.

        brand ID's to filter by  # noqa: E501

        :param brand_ids: The brand_ids of this ServiceWindowsSchemeFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._brand_ids = brand_ids

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
        if issubclass(ServiceWindowsSchemeFiltersModel, dict):
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
        if not isinstance(other, ServiceWindowsSchemeFiltersModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceWindowsSchemeFiltersModel):
            return True

        return self.to_dict() != other.to_dict()