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


class SettingsFiltersModel(object):
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
        'settings_group_id': 'list[int]',
        'settings_group_name': 'list[str]',
        'key': 'list[str]',
        'search_text': 'str',
        'updated_at_since': 'datetime',
        'updated_at_till': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'settings_group_id': 'settings_group_id',
        'settings_group_name': 'settings_group_name',
        'key': 'key',
        'search_text': 'search_text',
        'updated_at_since': 'updated_at_since',
        'updated_at_till': 'updated_at_till'
    }

    def __init__(self, id=None, settings_group_id=None, settings_group_name=None, key=None, search_text=None, updated_at_since=None, updated_at_till=None, _configuration=None):  # noqa: E501
        """SettingsFiltersModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._settings_group_id = None
        self._settings_group_name = None
        self._key = None
        self._search_text = None
        self._updated_at_since = None
        self._updated_at_till = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if settings_group_id is not None:
            self.settings_group_id = settings_group_id
        if settings_group_name is not None:
            self.settings_group_name = settings_group_name
        if key is not None:
            self.key = key
        if search_text is not None:
            self.search_text = search_text
        if updated_at_since is not None:
            self.updated_at_since = updated_at_since
        if updated_at_till is not None:
            self.updated_at_till = updated_at_till

    @property
    def id(self):
        """Gets the id of this SettingsFiltersModel.  # noqa: E501

          # noqa: E501

        :return: The id of this SettingsFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SettingsFiltersModel.

          # noqa: E501

        :param id: The id of this SettingsFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._id = id

    @property
    def settings_group_id(self):
        """Gets the settings_group_id of this SettingsFiltersModel.  # noqa: E501

        SettingsGroup id of this setting. Possible values: 1: general, 2: address, 3: package, 4: activity, 5: equipment, 6: note, 7: optimisation, 8: filters  # noqa: E501

        :return: The settings_group_id of this SettingsFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._settings_group_id

    @settings_group_id.setter
    def settings_group_id(self, settings_group_id):
        """Sets the settings_group_id of this SettingsFiltersModel.

        SettingsGroup id of this setting. Possible values: 1: general, 2: address, 3: package, 4: activity, 5: equipment, 6: note, 7: optimisation, 8: filters  # noqa: E501

        :param settings_group_id: The settings_group_id of this SettingsFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._settings_group_id = settings_group_id

    @property
    def settings_group_name(self):
        """Gets the settings_group_name of this SettingsFiltersModel.  # noqa: E501

        SettingsGroup name of this setting  # noqa: E501

        :return: The settings_group_name of this SettingsFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._settings_group_name

    @settings_group_name.setter
    def settings_group_name(self, settings_group_name):
        """Sets the settings_group_name of this SettingsFiltersModel.

        SettingsGroup name of this setting  # noqa: E501

        :param settings_group_name: The settings_group_name of this SettingsFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._settings_group_name = settings_group_name

    @property
    def key(self):
        """Gets the key of this SettingsFiltersModel.  # noqa: E501

        Unique string key for setting identification  # noqa: E501

        :return: The key of this SettingsFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SettingsFiltersModel.

        Unique string key for setting identification  # noqa: E501

        :param key: The key of this SettingsFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._key = key

    @property
    def search_text(self):
        """Gets the search_text of this SettingsFiltersModel.  # noqa: E501

        free search through text and numeric type columns  # noqa: E501

        :return: The search_text of this SettingsFiltersModel.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this SettingsFiltersModel.

        free search through text and numeric type columns  # noqa: E501

        :param search_text: The search_text of this SettingsFiltersModel.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

    @property
    def updated_at_since(self):
        """Gets the updated_at_since of this SettingsFiltersModel.  # noqa: E501

        Show updated since  # noqa: E501

        :return: The updated_at_since of this SettingsFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_since

    @updated_at_since.setter
    def updated_at_since(self, updated_at_since):
        """Sets the updated_at_since of this SettingsFiltersModel.

        Show updated since  # noqa: E501

        :param updated_at_since: The updated_at_since of this SettingsFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_since = updated_at_since

    @property
    def updated_at_till(self):
        """Gets the updated_at_till of this SettingsFiltersModel.  # noqa: E501

        Show updated till  # noqa: E501

        :return: The updated_at_till of this SettingsFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_till

    @updated_at_till.setter
    def updated_at_till(self, updated_at_till):
        """Sets the updated_at_till of this SettingsFiltersModel.

        Show updated till  # noqa: E501

        :param updated_at_till: The updated_at_till of this SettingsFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_till = updated_at_till

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
        if issubclass(SettingsFiltersModel, dict):
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
        if not isinstance(other, SettingsFiltersModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsFiltersModel):
            return True

        return self.to_dict() != other.to_dict()