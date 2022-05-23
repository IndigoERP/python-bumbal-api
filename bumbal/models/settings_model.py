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


class SettingsModel(object):
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
        'settings_group_id': 'int',
        'settings_group_name': 'str',
        'key': 'str',
        'value': 'str',
        'value_options': 'list[ValueOptionModel]',
        'setting_updated_at': 'datetime',
        'setting_updated_by': 'int',
        'setting_updated_by_user': 'UsersModel'
    }

    attribute_map = {
        'id': 'id',
        'settings_group_id': 'settings_group_id',
        'settings_group_name': 'settings_group_name',
        'key': 'key',
        'value': 'value',
        'value_options': 'value_options',
        'setting_updated_at': 'setting_updated_at',
        'setting_updated_by': 'setting_updated_by',
        'setting_updated_by_user': 'setting_updated_by_user'
    }

    def __init__(self, id=None, settings_group_id=None, settings_group_name=None, key=None, value=None, value_options=None, setting_updated_at=None, setting_updated_by=None, setting_updated_by_user=None, _configuration=None):  # noqa: E501
        """SettingsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._settings_group_id = None
        self._settings_group_name = None
        self._key = None
        self._value = None
        self._value_options = None
        self._setting_updated_at = None
        self._setting_updated_by = None
        self._setting_updated_by_user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if settings_group_id is not None:
            self.settings_group_id = settings_group_id
        if settings_group_name is not None:
            self.settings_group_name = settings_group_name
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if value_options is not None:
            self.value_options = value_options
        if setting_updated_at is not None:
            self.setting_updated_at = setting_updated_at
        if setting_updated_by is not None:
            self.setting_updated_by = setting_updated_by
        if setting_updated_by_user is not None:
            self.setting_updated_by_user = setting_updated_by_user

    @property
    def id(self):
        """Gets the id of this SettingsModel.  # noqa: E501

          # noqa: E501

        :return: The id of this SettingsModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SettingsModel.

          # noqa: E501

        :param id: The id of this SettingsModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def settings_group_id(self):
        """Gets the settings_group_id of this SettingsModel.  # noqa: E501

        SettingsGroup id of this setting. Possible values: 1: general, 2: address, 3: package, 4: activity, 5: equipment, 6: note, 7: optimisation, 8: filters  # noqa: E501

        :return: The settings_group_id of this SettingsModel.  # noqa: E501
        :rtype: int
        """
        return self._settings_group_id

    @settings_group_id.setter
    def settings_group_id(self, settings_group_id):
        """Sets the settings_group_id of this SettingsModel.

        SettingsGroup id of this setting. Possible values: 1: general, 2: address, 3: package, 4: activity, 5: equipment, 6: note, 7: optimisation, 8: filters  # noqa: E501

        :param settings_group_id: The settings_group_id of this SettingsModel.  # noqa: E501
        :type: int
        """

        self._settings_group_id = settings_group_id

    @property
    def settings_group_name(self):
        """Gets the settings_group_name of this SettingsModel.  # noqa: E501

        SettingsGroup name of this setting  # noqa: E501

        :return: The settings_group_name of this SettingsModel.  # noqa: E501
        :rtype: str
        """
        return self._settings_group_name

    @settings_group_name.setter
    def settings_group_name(self, settings_group_name):
        """Sets the settings_group_name of this SettingsModel.

        SettingsGroup name of this setting  # noqa: E501

        :param settings_group_name: The settings_group_name of this SettingsModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["general", "address", "package", "activity", "equipment", "note", "optimisation", "filters"]  # noqa: E501
        if (self._configuration.client_side_validation and
                settings_group_name not in allowed_values):
            raise ValueError(
                "Invalid value for `settings_group_name` ({0}), must be one of {1}"  # noqa: E501
                .format(settings_group_name, allowed_values)
            )

        self._settings_group_name = settings_group_name

    @property
    def key(self):
        """Gets the key of this SettingsModel.  # noqa: E501

        Unique string key for setting identification  # noqa: E501

        :return: The key of this SettingsModel.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SettingsModel.

        Unique string key for setting identification  # noqa: E501

        :param key: The key of this SettingsModel.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def value(self):
        """Gets the value of this SettingsModel.  # noqa: E501

        Set value for setting  # noqa: E501

        :return: The value of this SettingsModel.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SettingsModel.

        Set value for setting  # noqa: E501

        :param value: The value of this SettingsModel.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def value_options(self):
        """Gets the value_options of this SettingsModel.  # noqa: E501

          # noqa: E501

        :return: The value_options of this SettingsModel.  # noqa: E501
        :rtype: list[ValueOptionModel]
        """
        return self._value_options

    @value_options.setter
    def value_options(self, value_options):
        """Sets the value_options of this SettingsModel.

          # noqa: E501

        :param value_options: The value_options of this SettingsModel.  # noqa: E501
        :type: list[ValueOptionModel]
        """

        self._value_options = value_options

    @property
    def setting_updated_at(self):
        """Gets the setting_updated_at of this SettingsModel.  # noqa: E501

        updated_at date time  # noqa: E501

        :return: The setting_updated_at of this SettingsModel.  # noqa: E501
        :rtype: datetime
        """
        return self._setting_updated_at

    @setting_updated_at.setter
    def setting_updated_at(self, setting_updated_at):
        """Sets the setting_updated_at of this SettingsModel.

        updated_at date time  # noqa: E501

        :param setting_updated_at: The setting_updated_at of this SettingsModel.  # noqa: E501
        :type: datetime
        """

        self._setting_updated_at = setting_updated_at

    @property
    def setting_updated_by(self):
        """Gets the setting_updated_by of this SettingsModel.  # noqa: E501

        updated_by user id  # noqa: E501

        :return: The setting_updated_by of this SettingsModel.  # noqa: E501
        :rtype: int
        """
        return self._setting_updated_by

    @setting_updated_by.setter
    def setting_updated_by(self, setting_updated_by):
        """Sets the setting_updated_by of this SettingsModel.

        updated_by user id  # noqa: E501

        :param setting_updated_by: The setting_updated_by of this SettingsModel.  # noqa: E501
        :type: int
        """

        self._setting_updated_by = setting_updated_by

    @property
    def setting_updated_by_user(self):
        """Gets the setting_updated_by_user of this SettingsModel.  # noqa: E501

          # noqa: E501

        :return: The setting_updated_by_user of this SettingsModel.  # noqa: E501
        :rtype: UsersModel
        """
        return self._setting_updated_by_user

    @setting_updated_by_user.setter
    def setting_updated_by_user(self, setting_updated_by_user):
        """Sets the setting_updated_by_user of this SettingsModel.

          # noqa: E501

        :param setting_updated_by_user: The setting_updated_by_user of this SettingsModel.  # noqa: E501
        :type: UsersModel
        """

        self._setting_updated_by_user = setting_updated_by_user

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
        if issubclass(SettingsModel, dict):
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
        if not isinstance(other, SettingsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsModel):
            return True

        return self.to_dict() != other.to_dict()