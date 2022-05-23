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


class AvailabilityTimeSlotModel(object):
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
        'key': 'str',
        'date_time_from': 'datetime',
        'date_time_to': 'datetime',
        'proposed_plan_date_time_from': 'datetime',
        'proposed_plan_date_time_to': 'datetime',
        'proposed_driver': 'DriverModel',
        'impact': 'list[AvailabilityTimeSlotImpactModel]',
        'follow_up_time_slots': 'list[AvailabilityFollowUpTimeSlotModel]'
    }

    attribute_map = {
        'id': 'id',
        'key': 'key',
        'date_time_from': 'date_time_from',
        'date_time_to': 'date_time_to',
        'proposed_plan_date_time_from': 'proposed_plan_date_time_from',
        'proposed_plan_date_time_to': 'proposed_plan_date_time_to',
        'proposed_driver': 'proposed_driver',
        'impact': 'impact',
        'follow_up_time_slots': 'follow_up_time_slots'
    }

    def __init__(self, id=None, key=None, date_time_from=None, date_time_to=None, proposed_plan_date_time_from=None, proposed_plan_date_time_to=None, proposed_driver=None, impact=None, follow_up_time_slots=None, _configuration=None):  # noqa: E501
        """AvailabilityTimeSlotModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._key = None
        self._date_time_from = None
        self._date_time_to = None
        self._proposed_plan_date_time_from = None
        self._proposed_plan_date_time_to = None
        self._proposed_driver = None
        self._impact = None
        self._follow_up_time_slots = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if key is not None:
            self.key = key
        if date_time_from is not None:
            self.date_time_from = date_time_from
        if date_time_to is not None:
            self.date_time_to = date_time_to
        if proposed_plan_date_time_from is not None:
            self.proposed_plan_date_time_from = proposed_plan_date_time_from
        if proposed_plan_date_time_to is not None:
            self.proposed_plan_date_time_to = proposed_plan_date_time_to
        if proposed_driver is not None:
            self.proposed_driver = proposed_driver
        if impact is not None:
            self.impact = impact
        if follow_up_time_slots is not None:
            self.follow_up_time_slots = follow_up_time_slots

    @property
    def id(self):
        """Gets the id of this AvailabilityTimeSlotModel.  # noqa: E501

          # noqa: E501

        :return: The id of this AvailabilityTimeSlotModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AvailabilityTimeSlotModel.

          # noqa: E501

        :param id: The id of this AvailabilityTimeSlotModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def key(self):
        """Gets the key of this AvailabilityTimeSlotModel.  # noqa: E501

        unique key per analyzed time slot, uuid type  # noqa: E501

        :return: The key of this AvailabilityTimeSlotModel.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AvailabilityTimeSlotModel.

        unique key per analyzed time slot, uuid type  # noqa: E501

        :param key: The key of this AvailabilityTimeSlotModel.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def date_time_from(self):
        """Gets the date_time_from of this AvailabilityTimeSlotModel.  # noqa: E501

          # noqa: E501

        :return: The date_time_from of this AvailabilityTimeSlotModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_from

    @date_time_from.setter
    def date_time_from(self, date_time_from):
        """Sets the date_time_from of this AvailabilityTimeSlotModel.

          # noqa: E501

        :param date_time_from: The date_time_from of this AvailabilityTimeSlotModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_from = date_time_from

    @property
    def date_time_to(self):
        """Gets the date_time_to of this AvailabilityTimeSlotModel.  # noqa: E501

          # noqa: E501

        :return: The date_time_to of this AvailabilityTimeSlotModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_to

    @date_time_to.setter
    def date_time_to(self, date_time_to):
        """Sets the date_time_to of this AvailabilityTimeSlotModel.

          # noqa: E501

        :param date_time_to: The date_time_to of this AvailabilityTimeSlotModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_to = date_time_to

    @property
    def proposed_plan_date_time_from(self):
        """Gets the proposed_plan_date_time_from of this AvailabilityTimeSlotModel.  # noqa: E501

          # noqa: E501

        :return: The proposed_plan_date_time_from of this AvailabilityTimeSlotModel.  # noqa: E501
        :rtype: datetime
        """
        return self._proposed_plan_date_time_from

    @proposed_plan_date_time_from.setter
    def proposed_plan_date_time_from(self, proposed_plan_date_time_from):
        """Sets the proposed_plan_date_time_from of this AvailabilityTimeSlotModel.

          # noqa: E501

        :param proposed_plan_date_time_from: The proposed_plan_date_time_from of this AvailabilityTimeSlotModel.  # noqa: E501
        :type: datetime
        """

        self._proposed_plan_date_time_from = proposed_plan_date_time_from

    @property
    def proposed_plan_date_time_to(self):
        """Gets the proposed_plan_date_time_to of this AvailabilityTimeSlotModel.  # noqa: E501

          # noqa: E501

        :return: The proposed_plan_date_time_to of this AvailabilityTimeSlotModel.  # noqa: E501
        :rtype: datetime
        """
        return self._proposed_plan_date_time_to

    @proposed_plan_date_time_to.setter
    def proposed_plan_date_time_to(self, proposed_plan_date_time_to):
        """Sets the proposed_plan_date_time_to of this AvailabilityTimeSlotModel.

          # noqa: E501

        :param proposed_plan_date_time_to: The proposed_plan_date_time_to of this AvailabilityTimeSlotModel.  # noqa: E501
        :type: datetime
        """

        self._proposed_plan_date_time_to = proposed_plan_date_time_to

    @property
    def proposed_driver(self):
        """Gets the proposed_driver of this AvailabilityTimeSlotModel.  # noqa: E501

          # noqa: E501

        :return: The proposed_driver of this AvailabilityTimeSlotModel.  # noqa: E501
        :rtype: DriverModel
        """
        return self._proposed_driver

    @proposed_driver.setter
    def proposed_driver(self, proposed_driver):
        """Sets the proposed_driver of this AvailabilityTimeSlotModel.

          # noqa: E501

        :param proposed_driver: The proposed_driver of this AvailabilityTimeSlotModel.  # noqa: E501
        :type: DriverModel
        """

        self._proposed_driver = proposed_driver

    @property
    def impact(self):
        """Gets the impact of this AvailabilityTimeSlotModel.  # noqa: E501

          # noqa: E501

        :return: The impact of this AvailabilityTimeSlotModel.  # noqa: E501
        :rtype: list[AvailabilityTimeSlotImpactModel]
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this AvailabilityTimeSlotModel.

          # noqa: E501

        :param impact: The impact of this AvailabilityTimeSlotModel.  # noqa: E501
        :type: list[AvailabilityTimeSlotImpactModel]
        """

        self._impact = impact

    @property
    def follow_up_time_slots(self):
        """Gets the follow_up_time_slots of this AvailabilityTimeSlotModel.  # noqa: E501

          # noqa: E501

        :return: The follow_up_time_slots of this AvailabilityTimeSlotModel.  # noqa: E501
        :rtype: list[AvailabilityFollowUpTimeSlotModel]
        """
        return self._follow_up_time_slots

    @follow_up_time_slots.setter
    def follow_up_time_slots(self, follow_up_time_slots):
        """Sets the follow_up_time_slots of this AvailabilityTimeSlotModel.

          # noqa: E501

        :param follow_up_time_slots: The follow_up_time_slots of this AvailabilityTimeSlotModel.  # noqa: E501
        :type: list[AvailabilityFollowUpTimeSlotModel]
        """

        self._follow_up_time_slots = follow_up_time_slots

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
        if issubclass(AvailabilityTimeSlotModel, dict):
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
        if not isinstance(other, AvailabilityTimeSlotModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AvailabilityTimeSlotModel):
            return True

        return self.to_dict() != other.to_dict()