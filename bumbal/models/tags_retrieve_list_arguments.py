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


class TagsRetrieveListArguments(object):
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
        'options': 'TagsOptionsModel',
        'filters': 'TagsFiltersModel',
        'limit': 'int',
        'offset': 'int',
        'search_text': 'str',
        'count_only': 'bool'
    }

    attribute_map = {
        'options': 'options',
        'filters': 'filters',
        'limit': 'limit',
        'offset': 'offset',
        'search_text': 'search_text',
        'count_only': 'count_only'
    }

    def __init__(self, options=None, filters=None, limit=None, offset=None, search_text=None, count_only=None, _configuration=None):  # noqa: E501
        """TagsRetrieveListArguments - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._options = None
        self._filters = None
        self._limit = None
        self._offset = None
        self._search_text = None
        self._count_only = None
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
        if count_only is not None:
            self.count_only = count_only

    @property
    def options(self):
        """Gets the options of this TagsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The options of this TagsRetrieveListArguments.  # noqa: E501
        :rtype: TagsOptionsModel
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this TagsRetrieveListArguments.

          # noqa: E501

        :param options: The options of this TagsRetrieveListArguments.  # noqa: E501
        :type: TagsOptionsModel
        """

        self._options = options

    @property
    def filters(self):
        """Gets the filters of this TagsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The filters of this TagsRetrieveListArguments.  # noqa: E501
        :rtype: TagsFiltersModel
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this TagsRetrieveListArguments.

          # noqa: E501

        :param filters: The filters of this TagsRetrieveListArguments.  # noqa: E501
        :type: TagsFiltersModel
        """

        self._filters = filters

    @property
    def limit(self):
        """Gets the limit of this TagsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The limit of this TagsRetrieveListArguments.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this TagsRetrieveListArguments.

          # noqa: E501

        :param limit: The limit of this TagsRetrieveListArguments.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this TagsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The offset of this TagsRetrieveListArguments.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TagsRetrieveListArguments.

          # noqa: E501

        :param offset: The offset of this TagsRetrieveListArguments.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def search_text(self):
        """Gets the search_text of this TagsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The search_text of this TagsRetrieveListArguments.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this TagsRetrieveListArguments.

          # noqa: E501

        :param search_text: The search_text of this TagsRetrieveListArguments.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

    @property
    def count_only(self):
        """Gets the count_only of this TagsRetrieveListArguments.  # noqa: E501

          # noqa: E501

        :return: The count_only of this TagsRetrieveListArguments.  # noqa: E501
        :rtype: bool
        """
        return self._count_only

    @count_only.setter
    def count_only(self, count_only):
        """Sets the count_only of this TagsRetrieveListArguments.

          # noqa: E501

        :param count_only: The count_only of this TagsRetrieveListArguments.  # noqa: E501
        :type: bool
        """

        self._count_only = count_only

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
        if issubclass(TagsRetrieveListArguments, dict):
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
        if not isinstance(other, TagsRetrieveListArguments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TagsRetrieveListArguments):
            return True

        return self.to_dict() != other.to_dict()
