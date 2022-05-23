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


class NotificationCategoryListResponse(object):
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
        'items': 'list[NotificationCategoryModel]',
        'count_filtered': 'int',
        'count_unfiltered': 'int',
        'count_limited': 'int'
    }

    attribute_map = {
        'items': 'items',
        'count_filtered': 'count_filtered',
        'count_unfiltered': 'count_unfiltered',
        'count_limited': 'count_limited'
    }

    def __init__(self, items=None, count_filtered=None, count_unfiltered=None, count_limited=None, _configuration=None):  # noqa: E501
        """NotificationCategoryListResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._items = None
        self._count_filtered = None
        self._count_unfiltered = None
        self._count_limited = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if count_filtered is not None:
            self.count_filtered = count_filtered
        if count_unfiltered is not None:
            self.count_unfiltered = count_unfiltered
        if count_limited is not None:
            self.count_limited = count_limited

    @property
    def items(self):
        """Gets the items of this NotificationCategoryListResponse.  # noqa: E501

          # noqa: E501

        :return: The items of this NotificationCategoryListResponse.  # noqa: E501
        :rtype: list[NotificationCategoryModel]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this NotificationCategoryListResponse.

          # noqa: E501

        :param items: The items of this NotificationCategoryListResponse.  # noqa: E501
        :type: list[NotificationCategoryModel]
        """

        self._items = items

    @property
    def count_filtered(self):
        """Gets the count_filtered of this NotificationCategoryListResponse.  # noqa: E501

        Count of total items with filters in place  # noqa: E501

        :return: The count_filtered of this NotificationCategoryListResponse.  # noqa: E501
        :rtype: int
        """
        return self._count_filtered

    @count_filtered.setter
    def count_filtered(self, count_filtered):
        """Sets the count_filtered of this NotificationCategoryListResponse.

        Count of total items with filters in place  # noqa: E501

        :param count_filtered: The count_filtered of this NotificationCategoryListResponse.  # noqa: E501
        :type: int
        """

        self._count_filtered = count_filtered

    @property
    def count_unfiltered(self):
        """Gets the count_unfiltered of this NotificationCategoryListResponse.  # noqa: E501

        Count of total items without filters in place  # noqa: E501

        :return: The count_unfiltered of this NotificationCategoryListResponse.  # noqa: E501
        :rtype: int
        """
        return self._count_unfiltered

    @count_unfiltered.setter
    def count_unfiltered(self, count_unfiltered):
        """Sets the count_unfiltered of this NotificationCategoryListResponse.

        Count of total items without filters in place  # noqa: E501

        :param count_unfiltered: The count_unfiltered of this NotificationCategoryListResponse.  # noqa: E501
        :type: int
        """

        self._count_unfiltered = count_unfiltered

    @property
    def count_limited(self):
        """Gets the count_limited of this NotificationCategoryListResponse.  # noqa: E501

        Count of items with limit in place  # noqa: E501

        :return: The count_limited of this NotificationCategoryListResponse.  # noqa: E501
        :rtype: int
        """
        return self._count_limited

    @count_limited.setter
    def count_limited(self, count_limited):
        """Sets the count_limited of this NotificationCategoryListResponse.

        Count of items with limit in place  # noqa: E501

        :param count_limited: The count_limited of this NotificationCategoryListResponse.  # noqa: E501
        :type: int
        """

        self._count_limited = count_limited

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
        if issubclass(NotificationCategoryListResponse, dict):
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
        if not isinstance(other, NotificationCategoryListResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationCategoryListResponse):
            return True

        return self.to_dict() != other.to_dict()
