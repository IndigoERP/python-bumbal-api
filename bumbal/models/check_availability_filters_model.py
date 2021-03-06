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


class CheckAvailabilityFiltersModel(object):
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
        'route_id': 'list[int]',
        'date_from': 'date',
        'date_to': 'date',
        'max_nr_of_days_with_availability': 'int'
    }

    attribute_map = {
        'route_id': 'route_id',
        'date_from': 'date_from',
        'date_to': 'date_to',
        'max_nr_of_days_with_availability': 'max_nr_of_days_with_availability'
    }

    def __init__(self, route_id=None, date_from=None, date_to=None, max_nr_of_days_with_availability=None, _configuration=None):  # noqa: E501
        """CheckAvailabilityFiltersModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._route_id = None
        self._date_from = None
        self._date_to = None
        self._max_nr_of_days_with_availability = None
        self.discriminator = None

        if route_id is not None:
            self.route_id = route_id
        if date_from is not None:
            self.date_from = date_from
        if date_to is not None:
            self.date_to = date_to
        if max_nr_of_days_with_availability is not None:
            self.max_nr_of_days_with_availability = max_nr_of_days_with_availability

    @property
    def route_id(self):
        """Gets the route_id of this CheckAvailabilityFiltersModel.  # noqa: E501

        Route id  # noqa: E501

        :return: The route_id of this CheckAvailabilityFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id):
        """Sets the route_id of this CheckAvailabilityFiltersModel.

        Route id  # noqa: E501

        :param route_id: The route_id of this CheckAvailabilityFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._route_id = route_id

    @property
    def date_from(self):
        """Gets the date_from of this CheckAvailabilityFiltersModel.  # noqa: E501

          # noqa: E501

        :return: The date_from of this CheckAvailabilityFiltersModel.  # noqa: E501
        :rtype: date
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this CheckAvailabilityFiltersModel.

          # noqa: E501

        :param date_from: The date_from of this CheckAvailabilityFiltersModel.  # noqa: E501
        :type: date
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this CheckAvailabilityFiltersModel.  # noqa: E501

          # noqa: E501

        :return: The date_to of this CheckAvailabilityFiltersModel.  # noqa: E501
        :rtype: date
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this CheckAvailabilityFiltersModel.

          # noqa: E501

        :param date_to: The date_to of this CheckAvailabilityFiltersModel.  # noqa: E501
        :type: date
        """

        self._date_to = date_to

    @property
    def max_nr_of_days_with_availability(self):
        """Gets the max_nr_of_days_with_availability of this CheckAvailabilityFiltersModel.  # noqa: E501

        Availability check will continue to analyse days until there is no availability in the system anymore or the number of days with available time slots has reached the max_nr_of_days_with_availability  # noqa: E501

        :return: The max_nr_of_days_with_availability of this CheckAvailabilityFiltersModel.  # noqa: E501
        :rtype: int
        """
        return self._max_nr_of_days_with_availability

    @max_nr_of_days_with_availability.setter
    def max_nr_of_days_with_availability(self, max_nr_of_days_with_availability):
        """Sets the max_nr_of_days_with_availability of this CheckAvailabilityFiltersModel.

        Availability check will continue to analyse days until there is no availability in the system anymore or the number of days with available time slots has reached the max_nr_of_days_with_availability  # noqa: E501

        :param max_nr_of_days_with_availability: The max_nr_of_days_with_availability of this CheckAvailabilityFiltersModel.  # noqa: E501
        :type: int
        """

        self._max_nr_of_days_with_availability = max_nr_of_days_with_availability

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
        if issubclass(CheckAvailabilityFiltersModel, dict):
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
        if not isinstance(other, CheckAvailabilityFiltersModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CheckAvailabilityFiltersModel):
            return True

        return self.to_dict() != other.to_dict()
