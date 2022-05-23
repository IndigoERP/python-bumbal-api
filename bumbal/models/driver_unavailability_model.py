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


class DriverUnavailabilityModel(object):
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
        'user_id': 'str',
        'reference': 'str',
        'date_time_to': 'datetime',
        'date_time_from': 'datetime',
        'user_link': 'LinkModel',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'links': 'list[LinkModel]',
        'active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'reference': 'reference',
        'date_time_to': 'date_time_to',
        'date_time_from': 'date_time_from',
        'user_link': 'user_link',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'links': 'links',
        'active': 'active'
    }

    def __init__(self, id=None, user_id=None, reference=None, date_time_to=None, date_time_from=None, user_link=None, created_at=None, updated_at=None, links=None, active=None, _configuration=None):  # noqa: E501
        """DriverUnavailabilityModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._user_id = None
        self._reference = None
        self._date_time_to = None
        self._date_time_from = None
        self._user_link = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self._active = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if reference is not None:
            self.reference = reference
        if date_time_to is not None:
            self.date_time_to = date_time_to
        if date_time_from is not None:
            self.date_time_from = date_time_from
        if user_link is not None:
            self.user_link = user_link
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if links is not None:
            self.links = links
        if active is not None:
            self.active = active

    @property
    def id(self):
        """Gets the id of this DriverUnavailabilityModel.  # noqa: E501

        Unique ID  # noqa: E501

        :return: The id of this DriverUnavailabilityModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DriverUnavailabilityModel.

        Unique ID  # noqa: E501

        :param id: The id of this DriverUnavailabilityModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this DriverUnavailabilityModel.  # noqa: E501

        The user_id of the DriverUnavailability  # noqa: E501

        :return: The user_id of this DriverUnavailabilityModel.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this DriverUnavailabilityModel.

        The user_id of the DriverUnavailability  # noqa: E501

        :param user_id: The user_id of this DriverUnavailabilityModel.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def reference(self):
        """Gets the reference of this DriverUnavailabilityModel.  # noqa: E501

        The reference of the DriverUnavailability  # noqa: E501

        :return: The reference of this DriverUnavailabilityModel.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this DriverUnavailabilityModel.

        The reference of the DriverUnavailability  # noqa: E501

        :param reference: The reference of this DriverUnavailabilityModel.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def date_time_to(self):
        """Gets the date_time_to of this DriverUnavailabilityModel.  # noqa: E501

        date_time_to date time  # noqa: E501

        :return: The date_time_to of this DriverUnavailabilityModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_to

    @date_time_to.setter
    def date_time_to(self, date_time_to):
        """Sets the date_time_to of this DriverUnavailabilityModel.

        date_time_to date time  # noqa: E501

        :param date_time_to: The date_time_to of this DriverUnavailabilityModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_to = date_time_to

    @property
    def date_time_from(self):
        """Gets the date_time_from of this DriverUnavailabilityModel.  # noqa: E501

        date_time_from date time  # noqa: E501

        :return: The date_time_from of this DriverUnavailabilityModel.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_from

    @date_time_from.setter
    def date_time_from(self, date_time_from):
        """Sets the date_time_from of this DriverUnavailabilityModel.

        date_time_from date time  # noqa: E501

        :param date_time_from: The date_time_from of this DriverUnavailabilityModel.  # noqa: E501
        :type: datetime
        """

        self._date_time_from = date_time_from

    @property
    def user_link(self):
        """Gets the user_link of this DriverUnavailabilityModel.  # noqa: E501

          # noqa: E501

        :return: The user_link of this DriverUnavailabilityModel.  # noqa: E501
        :rtype: LinkModel
        """
        return self._user_link

    @user_link.setter
    def user_link(self, user_link):
        """Sets the user_link of this DriverUnavailabilityModel.

          # noqa: E501

        :param user_link: The user_link of this DriverUnavailabilityModel.  # noqa: E501
        :type: LinkModel
        """

        self._user_link = user_link

    @property
    def created_at(self):
        """Gets the created_at of this DriverUnavailabilityModel.  # noqa: E501

        created_at date time  # noqa: E501

        :return: The created_at of this DriverUnavailabilityModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DriverUnavailabilityModel.

        created_at date time  # noqa: E501

        :param created_at: The created_at of this DriverUnavailabilityModel.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DriverUnavailabilityModel.  # noqa: E501

        updated_at date time  # noqa: E501

        :return: The updated_at of this DriverUnavailabilityModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DriverUnavailabilityModel.

        updated_at date time  # noqa: E501

        :param updated_at: The updated_at of this DriverUnavailabilityModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def links(self):
        """Gets the links of this DriverUnavailabilityModel.  # noqa: E501

          # noqa: E501

        :return: The links of this DriverUnavailabilityModel.  # noqa: E501
        :rtype: list[LinkModel]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DriverUnavailabilityModel.

          # noqa: E501

        :param links: The links of this DriverUnavailabilityModel.  # noqa: E501
        :type: list[LinkModel]
        """

        self._links = links

    @property
    def active(self):
        """Gets the active of this DriverUnavailabilityModel.  # noqa: E501

        if active=0: Driver Unavailability has been removed and is no longer visible in any bumbal interface  # noqa: E501

        :return: The active of this DriverUnavailabilityModel.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this DriverUnavailabilityModel.

        if active=0: Driver Unavailability has been removed and is no longer visible in any bumbal interface  # noqa: E501

        :param active: The active of this DriverUnavailabilityModel.  # noqa: E501
        :type: bool
        """

        self._active = active

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
        if issubclass(DriverUnavailabilityModel, dict):
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
        if not isinstance(other, DriverUnavailabilityModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DriverUnavailabilityModel):
            return True

        return self.to_dict() != other.to_dict()