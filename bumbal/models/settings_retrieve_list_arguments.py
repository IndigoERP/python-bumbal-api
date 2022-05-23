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


class SettingsRetrieveListArguments(object):
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
        'options': 'SettingsOptionsModel',
        'filters': 'SettingsFiltersModel',
        'limit': 'int',
        'offset': 'int',
        'search_text': 'str'
    }

    attribute_map = {
        'options': 'options',
        'filters': 'filters',
        'limit': 'limit',
        'offset': 'offset',
        'search_text': 'search_text'
    }

    def __init__(self, options=None, filters=None, limit=None, offset=None, search_text=None, _configuration=None):  # noqa: E501
        """SettingsRetrieveListArguments - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._options = None
        self._filters = None
        self._limit = None
        self._offset = None
        self._search_text = None
        self.discriminator = None

        if options is not None:
            self.options = options
        if filters is not None:
            self.filters = filters
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if search_text is not None:
            self.search_text = search_text

    @property
    def options(self):
        """Gets the options of this SettingsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The options of this SettingsRetrieveListArguments.  # noqa: E501
        :rtype: SettingsOptionsModel
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this SettingsRetrieveListArguments.

          # noqa: E501

        :param options: The options of this SettingsRetrieveListArguments.  # noqa: E501
        :type: SettingsOptionsModel
        """

        self._options = options

    @property
    def filters(self):
        """Gets the filters of this SettingsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The filters of this SettingsRetrieveListArguments.  # noqa: E501
        :rtype: SettingsFiltersModel
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this SettingsRetrieveListArguments.

          # noqa: E501

        :param filters: The filters of this SettingsRetrieveListArguments.  # noqa: E501
        :type: SettingsFiltersModel
        """

        self._filters = filters

    @property
    def limit(self):
        """Gets the limit of this SettingsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The limit of this SettingsRetrieveListArguments.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SettingsRetrieveListArguments.

          # noqa: E501

        :param limit: The limit of this SettingsRetrieveListArguments.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this SettingsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The offset of this SettingsRetrieveListArguments.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SettingsRetrieveListArguments.

          # noqa: E501

        :param offset: The offset of this SettingsRetrieveListArguments.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def search_text(self):
        """Gets the search_text of this SettingsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The search_text of this SettingsRetrieveListArguments.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this SettingsRetrieveListArguments.

          # noqa: E501

        :param search_text: The search_text of this SettingsRetrieveListArguments.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

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
        if issubclass(SettingsRetrieveListArguments, dict):
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
        if not isinstance(other, SettingsRetrieveListArguments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SettingsRetrieveListArguments):
            return True

        return self.to_dict() != other.to_dict()
