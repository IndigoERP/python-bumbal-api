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


class AssignmentFiltersModel(object):
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
        'nr': 'list[str]',
        'date_time_from': 'datetime',
        'date_time_to': 'datetime',
        'date_time_from_since': 'datetime',
        'date_time_from_till': 'datetime',
        'date_time_to_since': 'datetime',
        'date_time_to_till': 'datetime',
        'links': 'list[object]',
        'updated_at_since': 'datetime',
        'updated_at_till': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'nr': 'nr',
        'date_time_from': 'date_time_from',
        'date_time_to': 'date_time_to',
        'date_time_from_since': 'date_time_from_since',
        'date_time_from_till': 'date_time_from_till',
        'date_time_to_since': 'date_time_to_since',
        'date_time_to_till': 'date_time_to_till',
        'links': 'links',
        'updated_at_since': 'updated_at_since',
        'updated_at_till': 'updated_at_till'
    }

    def __init__(self, id=None, nr=None, date_time_from=None, date_time_to=None, date_time_from_since=None, date_time_from_till=None, date_time_to_since=None, date_time_to_till=None, links=None, updated_at_since=None, updated_at_till=None, _configuration=None):  # noqa: E501
        """AssignmentFiltersModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._nr = None
        self._date_time_from = None
        self._date_time_to = None
        self._date_time_from_since = None
        self._date_time_from_till = None
        self._date_time_to_since = None
        self._date_time_to_till = None
        self._links = None
        self._updated_at_since = None
        self._updated_at_till = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if nr is not None:
            self.nr = nr
        if date_time_from is not None:
            self.date_time_from = date_time_from
        if date_time_to is not None:
            self.date_time_to = date_time_to
        if date_time_from_since is not None:
            self.date_time_from_since = date_time_from_since
        if date_time_from_till is not None:
            self.date_time_from_till = date_time_from_till
        if date_time_to_since is not None:
            self.date_time_to_since = date_time_to_since
        if date_time_to_till is not None:
            self.date_time_to_till = date_time_to_till
        if links is not None:
            self.links = links
        if updated_at_since is not None:
            self.updated_at_since = updated_at_since
        if updated_at_till is not None:
            self.updated_at_till = updated_at_till

    @property
    def id(self):
        """Gets the id of this AssignmentFiltersModel.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this AssignmentFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssignmentFiltersModel.

        Unique Identifier  # noqa: E501

        :param id: The id of this AssignmentFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._id = id

    @property
    def nr(self):
        """Gets the nr of this AssignmentFiltersModel.  # noqa: E501

        Number of this assignment  # noqa: E501

        :return: The nr of this AssignmentFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._nr

    @nr.setter
    def nr(self, nr):
        """Sets the nr of this AssignmentFiltersModel.

        Number of this assignment  # noqa: E501

        :param nr: The nr of this AssignmentFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._nr = nr

    @property
    def date_time_from(self):
        """Gets the date_time_from of this AssignmentFiltersModel.  # noqa: E501

        DateTime From  # noqa: E501

        :return: The date_time_from of this AssignmentFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_from

    @date_time_from.setter
    def date_time_from(self, date_time_from):
        """Sets the date_time_from of this AssignmentFiltersModel.

        DateTime From  # noqa: E501

        :param date_time_from: The date_time_from of this AssignmentFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_from = date_time_from

    @property
    def date_time_to(self):
        """Gets the date_time_to of this AssignmentFiltersModel.  # noqa: E501

        DateTime To  # noqa: E501

        :return: The date_time_to of this AssignmentFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_to

    @date_time_to.setter
    def date_time_to(self, date_time_to):
        """Sets the date_time_to of this AssignmentFiltersModel.

        DateTime To  # noqa: E501

        :param date_time_to: The date_time_to of this AssignmentFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_to = date_time_to

    @property
    def date_time_from_since(self):
        """Gets the date_time_from_since of this AssignmentFiltersModel.  # noqa: E501

        filter assignments with a DateTime From since this input  # noqa: E501

        :return: The date_time_from_since of this AssignmentFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_from_since

    @date_time_from_since.setter
    def date_time_from_since(self, date_time_from_since):
        """Sets the date_time_from_since of this AssignmentFiltersModel.

        filter assignments with a DateTime From since this input  # noqa: E501

        :param date_time_from_since: The date_time_from_since of this AssignmentFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_from_since = date_time_from_since

    @property
    def date_time_from_till(self):
        """Gets the date_time_from_till of this AssignmentFiltersModel.  # noqa: E501

        filter assignments with a DateTime From till this input  # noqa: E501

        :return: The date_time_from_till of this AssignmentFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_from_till

    @date_time_from_till.setter
    def date_time_from_till(self, date_time_from_till):
        """Sets the date_time_from_till of this AssignmentFiltersModel.

        filter assignments with a DateTime From till this input  # noqa: E501

        :param date_time_from_till: The date_time_from_till of this AssignmentFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_from_till = date_time_from_till

    @property
    def date_time_to_since(self):
        """Gets the date_time_to_since of this AssignmentFiltersModel.  # noqa: E501

        filter assignments with a DateTime To since this input  # noqa: E501

        :return: The date_time_to_since of this AssignmentFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_to_since

    @date_time_to_since.setter
    def date_time_to_since(self, date_time_to_since):
        """Sets the date_time_to_since of this AssignmentFiltersModel.

        filter assignments with a DateTime To since this input  # noqa: E501

        :param date_time_to_since: The date_time_to_since of this AssignmentFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_to_since = date_time_to_since

    @property
    def date_time_to_till(self):
        """Gets the date_time_to_till of this AssignmentFiltersModel.  # noqa: E501

        filter assignments with a DateTime To till this input  # noqa: E501

        :return: The date_time_to_till of this AssignmentFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_to_till

    @date_time_to_till.setter
    def date_time_to_till(self, date_time_to_till):
        """Sets the date_time_to_till of this AssignmentFiltersModel.

        filter assignments with a DateTime To till this input  # noqa: E501

        :param date_time_to_till: The date_time_to_till of this AssignmentFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_to_till = date_time_to_till

    @property
    def links(self):
        """Gets the links of this AssignmentFiltersModel.  # noqa: E501

        Activity Link ids  # noqa: E501

        :return: The links of this AssignmentFiltersModel.  # noqa: E501
        :rtype: list[object]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AssignmentFiltersModel.

        Activity Link ids  # noqa: E501

        :param links: The links of this AssignmentFiltersModel.  # noqa: E501
        :type: list[object]
        """

        self._links = links

    @property
    def updated_at_since(self):
        """Gets the updated_at_since of this AssignmentFiltersModel.  # noqa: E501

        Show updated since  # noqa: E501

        :return: The updated_at_since of this AssignmentFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_since

    @updated_at_since.setter
    def updated_at_since(self, updated_at_since):
        """Sets the updated_at_since of this AssignmentFiltersModel.

        Show updated since  # noqa: E501

        :param updated_at_since: The updated_at_since of this AssignmentFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_since = updated_at_since

    @property
    def updated_at_till(self):
        """Gets the updated_at_till of this AssignmentFiltersModel.  # noqa: E501

        Show updated till  # noqa: E501

        :return: The updated_at_till of this AssignmentFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_till

    @updated_at_till.setter
    def updated_at_till(self, updated_at_till):
        """Sets the updated_at_till of this AssignmentFiltersModel.

        Show updated till  # noqa: E501

        :param updated_at_till: The updated_at_till of this AssignmentFiltersModel.  # noqa: E501
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
        if issubclass(AssignmentFiltersModel, dict):
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
        if not isinstance(other, AssignmentFiltersModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssignmentFiltersModel):
            return True

        return self.to_dict() != other.to_dict()
