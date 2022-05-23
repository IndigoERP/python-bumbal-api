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


class RoutesEtaFiltersModel(object):
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
        'date_time_from': 'datetime',
        'date_time_to': 'datetime',
        'earliest_date_time_since': 'datetime',
        'earliest_date_time_till': 'datetime',
        'latest_date_time_since': 'datetime',
        'latest_date_time_till': 'datetime',
        'updated_at': 'datetime',
        'updated_at_since': 'datetime',
        'updated_at_till': 'datetime',
        'status_id': 'list[int]',
        'driver_id': 'list[int]',
        'recurrence_id': 'int',
        'tag_names': 'list[str]',
        'zone_names': 'list[str]',
        'optimized': 'list[bool]',
        'blocked': 'list[bool]'
    }

    attribute_map = {
        'id': 'id',
        'date_time_from': 'date_time_from',
        'date_time_to': 'date_time_to',
        'earliest_date_time_since': 'earliest_date_time_since',
        'earliest_date_time_till': 'earliest_date_time_till',
        'latest_date_time_since': 'latest_date_time_since',
        'latest_date_time_till': 'latest_date_time_till',
        'updated_at': 'updated_at',
        'updated_at_since': 'updated_at_since',
        'updated_at_till': 'updated_at_till',
        'status_id': 'status_id',
        'driver_id': 'driver_id',
        'recurrence_id': 'recurrence_id',
        'tag_names': 'tag_names',
        'zone_names': 'zone_names',
        'optimized': 'optimized',
        'blocked': 'blocked'
    }

    def __init__(self, id=None, date_time_from=None, date_time_to=None, earliest_date_time_since=None, earliest_date_time_till=None, latest_date_time_since=None, latest_date_time_till=None, updated_at=None, updated_at_since=None, updated_at_till=None, status_id=None, driver_id=None, recurrence_id=None, tag_names=None, zone_names=None, optimized=None, blocked=None, _configuration=None):  # noqa: E501
        """RoutesEtaFiltersModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._date_time_from = None
        self._date_time_to = None
        self._earliest_date_time_since = None
        self._earliest_date_time_till = None
        self._latest_date_time_since = None
        self._latest_date_time_till = None
        self._updated_at = None
        self._updated_at_since = None
        self._updated_at_till = None
        self._status_id = None
        self._driver_id = None
        self._recurrence_id = None
        self._tag_names = None
        self._zone_names = None
        self._optimized = None
        self._blocked = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if date_time_from is not None:
            self.date_time_from = date_time_from
        if date_time_to is not None:
            self.date_time_to = date_time_to
        if earliest_date_time_since is not None:
            self.earliest_date_time_since = earliest_date_time_since
        if earliest_date_time_till is not None:
            self.earliest_date_time_till = earliest_date_time_till
        if latest_date_time_since is not None:
            self.latest_date_time_since = latest_date_time_since
        if latest_date_time_till is not None:
            self.latest_date_time_till = latest_date_time_till
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_at_since is not None:
            self.updated_at_since = updated_at_since
        if updated_at_till is not None:
            self.updated_at_till = updated_at_till
        if status_id is not None:
            self.status_id = status_id
        if driver_id is not None:
            self.driver_id = driver_id
        if recurrence_id is not None:
            self.recurrence_id = recurrence_id
        if tag_names is not None:
            self.tag_names = tag_names
        if zone_names is not None:
            self.zone_names = zone_names
        if optimized is not None:
            self.optimized = optimized
        if blocked is not None:
            self.blocked = blocked

    @property
    def id(self):
        """Gets the id of this RoutesEtaFiltersModel.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoutesEtaFiltersModel.

        Unique Identifier  # noqa: E501

        :param id: The id of this RoutesEtaFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._id = id

    @property
    def date_time_from(self):
        """Gets the date_time_from of this RoutesEtaFiltersModel.  # noqa: E501

          # noqa: E501

        :return: The date_time_from of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_from

    @date_time_from.setter
    def date_time_from(self, date_time_from):
        """Sets the date_time_from of this RoutesEtaFiltersModel.

          # noqa: E501

        :param date_time_from: The date_time_from of this RoutesEtaFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_from = date_time_from

    @property
    def date_time_to(self):
        """Gets the date_time_to of this RoutesEtaFiltersModel.  # noqa: E501

          # noqa: E501

        :return: The date_time_to of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_to

    @date_time_to.setter
    def date_time_to(self, date_time_to):
        """Sets the date_time_to of this RoutesEtaFiltersModel.

          # noqa: E501

        :param date_time_to: The date_time_to of this RoutesEtaFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_to = date_time_to

    @property
    def earliest_date_time_since(self):
        """Gets the earliest_date_time_since of this RoutesEtaFiltersModel.  # noqa: E501

        filter routes with an Earliest DateTime To since this input  # noqa: E501

        :return: The earliest_date_time_since of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._earliest_date_time_since

    @earliest_date_time_since.setter
    def earliest_date_time_since(self, earliest_date_time_since):
        """Sets the earliest_date_time_since of this RoutesEtaFiltersModel.

        filter routes with an Earliest DateTime To since this input  # noqa: E501

        :param earliest_date_time_since: The earliest_date_time_since of this RoutesEtaFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._earliest_date_time_since = earliest_date_time_since

    @property
    def earliest_date_time_till(self):
        """Gets the earliest_date_time_till of this RoutesEtaFiltersModel.  # noqa: E501

        filter routes with an Earliest DateTime To till this input  # noqa: E501

        :return: The earliest_date_time_till of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._earliest_date_time_till

    @earliest_date_time_till.setter
    def earliest_date_time_till(self, earliest_date_time_till):
        """Sets the earliest_date_time_till of this RoutesEtaFiltersModel.

        filter routes with an Earliest DateTime To till this input  # noqa: E501

        :param earliest_date_time_till: The earliest_date_time_till of this RoutesEtaFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._earliest_date_time_till = earliest_date_time_till

    @property
    def latest_date_time_since(self):
        """Gets the latest_date_time_since of this RoutesEtaFiltersModel.  # noqa: E501

        filter routes with an Latest DateTime To since this input  # noqa: E501

        :return: The latest_date_time_since of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._latest_date_time_since

    @latest_date_time_since.setter
    def latest_date_time_since(self, latest_date_time_since):
        """Sets the latest_date_time_since of this RoutesEtaFiltersModel.

        filter routes with an Latest DateTime To since this input  # noqa: E501

        :param latest_date_time_since: The latest_date_time_since of this RoutesEtaFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._latest_date_time_since = latest_date_time_since

    @property
    def latest_date_time_till(self):
        """Gets the latest_date_time_till of this RoutesEtaFiltersModel.  # noqa: E501

        filter routes with an Latest DateTime To till this input  # noqa: E501

        :return: The latest_date_time_till of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._latest_date_time_till

    @latest_date_time_till.setter
    def latest_date_time_till(self, latest_date_time_till):
        """Sets the latest_date_time_till of this RoutesEtaFiltersModel.

        filter routes with an Latest DateTime To till this input  # noqa: E501

        :param latest_date_time_till: The latest_date_time_till of this RoutesEtaFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._latest_date_time_till = latest_date_time_till

    @property
    def updated_at(self):
        """Gets the updated_at of this RoutesEtaFiltersModel.  # noqa: E501

          # noqa: E501

        :return: The updated_at of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this RoutesEtaFiltersModel.

          # noqa: E501

        :param updated_at: The updated_at of this RoutesEtaFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def updated_at_since(self):
        """Gets the updated_at_since of this RoutesEtaFiltersModel.  # noqa: E501

        filter routes with an updated at date-time since this input  # noqa: E501

        :return: The updated_at_since of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_since

    @updated_at_since.setter
    def updated_at_since(self, updated_at_since):
        """Sets the updated_at_since of this RoutesEtaFiltersModel.

        filter routes with an updated at date-time since this input  # noqa: E501

        :param updated_at_since: The updated_at_since of this RoutesEtaFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_since = updated_at_since

    @property
    def updated_at_till(self):
        """Gets the updated_at_till of this RoutesEtaFiltersModel.  # noqa: E501

        filter routes with an updated at date-time till this input  # noqa: E501

        :return: The updated_at_till of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_till

    @updated_at_till.setter
    def updated_at_till(self, updated_at_till):
        """Sets the updated_at_till of this RoutesEtaFiltersModel.

        filter routes with an updated at date-time till this input  # noqa: E501

        :param updated_at_till: The updated_at_till of this RoutesEtaFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_till = updated_at_till

    @property
    def status_id(self):
        """Gets the status_id of this RoutesEtaFiltersModel.  # noqa: E501

          # noqa: E501

        :return: The status_id of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this RoutesEtaFiltersModel.

          # noqa: E501

        :param status_id: The status_id of this RoutesEtaFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._status_id = status_id

    @property
    def driver_id(self):
        """Gets the driver_id of this RoutesEtaFiltersModel.  # noqa: E501

          # noqa: E501

        :return: The driver_id of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._driver_id

    @driver_id.setter
    def driver_id(self, driver_id):
        """Sets the driver_id of this RoutesEtaFiltersModel.

          # noqa: E501

        :param driver_id: The driver_id of this RoutesEtaFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._driver_id = driver_id

    @property
    def recurrence_id(self):
        """Gets the recurrence_id of this RoutesEtaFiltersModel.  # noqa: E501

        Recurrence ID  # noqa: E501

        :return: The recurrence_id of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: int
        """
        return self._recurrence_id

    @recurrence_id.setter
    def recurrence_id(self, recurrence_id):
        """Sets the recurrence_id of this RoutesEtaFiltersModel.

        Recurrence ID  # noqa: E501

        :param recurrence_id: The recurrence_id of this RoutesEtaFiltersModel.  # noqa: E501
        :type: int
        """

        self._recurrence_id = recurrence_id

    @property
    def tag_names(self):
        """Gets the tag_names of this RoutesEtaFiltersModel.  # noqa: E501

        Tag names  # noqa: E501

        :return: The tag_names of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """Sets the tag_names of this RoutesEtaFiltersModel.

        Tag names  # noqa: E501

        :param tag_names: The tag_names of this RoutesEtaFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._tag_names = tag_names

    @property
    def zone_names(self):
        """Gets the zone_names of this RoutesEtaFiltersModel.  # noqa: E501

        Zone names  # noqa: E501

        :return: The zone_names of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._zone_names

    @zone_names.setter
    def zone_names(self, zone_names):
        """Sets the zone_names of this RoutesEtaFiltersModel.

        Zone names  # noqa: E501

        :param zone_names: The zone_names of this RoutesEtaFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._zone_names = zone_names

    @property
    def optimized(self):
        """Gets the optimized of this RoutesEtaFiltersModel.  # noqa: E501

        Optimized status of Route.  # noqa: E501

        :return: The optimized of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: list[bool]
        """
        return self._optimized

    @optimized.setter
    def optimized(self, optimized):
        """Sets the optimized of this RoutesEtaFiltersModel.

        Optimized status of Route.  # noqa: E501

        :param optimized: The optimized of this RoutesEtaFiltersModel.  # noqa: E501
        :type: list[bool]
        """

        self._optimized = optimized

    @property
    def blocked(self):
        """Gets the blocked of this RoutesEtaFiltersModel.  # noqa: E501

        Blocked status of Route  # noqa: E501

        :return: The blocked of this RoutesEtaFiltersModel.  # noqa: E501
        :rtype: list[bool]
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """Sets the blocked of this RoutesEtaFiltersModel.

        Blocked status of Route  # noqa: E501

        :param blocked: The blocked of this RoutesEtaFiltersModel.  # noqa: E501
        :type: list[bool]
        """

        self._blocked = blocked

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
        if issubclass(RoutesEtaFiltersModel, dict):
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
        if not isinstance(other, RoutesEtaFiltersModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoutesEtaFiltersModel):
            return True

        return self.to_dict() != other.to_dict()