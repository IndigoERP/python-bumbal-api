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


class AutoPlanResponse(object):
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
        'token': 'str',
        'status': 'str',
        'affected_activities': 'list[ActivityModel]',
        'unavailable_timewindows': 'list[TimeSlotModel]',
        'latest_analyzed_date': 'date'
    }

    attribute_map = {
        'token': 'token',
        'status': 'status',
        'affected_activities': 'affected_activities',
        'unavailable_timewindows': 'unavailable_timewindows',
        'latest_analyzed_date': 'latest_analyzed_date'
    }

    def __init__(self, token=None, status=None, affected_activities=None, unavailable_timewindows=None, latest_analyzed_date=None, _configuration=None):  # noqa: E501
        """AutoPlanResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._token = None
        self._status = None
        self._affected_activities = None
        self._unavailable_timewindows = None
        self._latest_analyzed_date = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if status is not None:
            self.status = status
        if affected_activities is not None:
            self.affected_activities = affected_activities
        if unavailable_timewindows is not None:
            self.unavailable_timewindows = unavailable_timewindows
        if latest_analyzed_date is not None:
            self.latest_analyzed_date = latest_analyzed_date

    @property
    def token(self):
        """Gets the token of this AutoPlanResponse.  # noqa: E501

        token for the auto plan job  # noqa: E501

        :return: The token of this AutoPlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AutoPlanResponse.

        token for the auto plan job  # noqa: E501

        :param token: The token of this AutoPlanResponse.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def status(self):
        """Gets the status of this AutoPlanResponse.  # noqa: E501

        current status for request  # noqa: E501

        :return: The status of this AutoPlanResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AutoPlanResponse.

        current status for request  # noqa: E501

        :param status: The status of this AutoPlanResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["not_ready", "done", "cancelled"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def affected_activities(self):
        """Gets the affected_activities of this AutoPlanResponse.  # noqa: E501

          # noqa: E501

        :return: The affected_activities of this AutoPlanResponse.  # noqa: E501
        :rtype: list[ActivityModel]
        """
        return self._affected_activities

    @affected_activities.setter
    def affected_activities(self, affected_activities):
        """Sets the affected_activities of this AutoPlanResponse.

          # noqa: E501

        :param affected_activities: The affected_activities of this AutoPlanResponse.  # noqa: E501
        :type: list[ActivityModel]
        """

        self._affected_activities = affected_activities

    @property
    def unavailable_timewindows(self):
        """Gets the unavailable_timewindows of this AutoPlanResponse.  # noqa: E501

          # noqa: E501

        :return: The unavailable_timewindows of this AutoPlanResponse.  # noqa: E501
        :rtype: list[TimeSlotModel]
        """
        return self._unavailable_timewindows

    @unavailable_timewindows.setter
    def unavailable_timewindows(self, unavailable_timewindows):
        """Sets the unavailable_timewindows of this AutoPlanResponse.

          # noqa: E501

        :param unavailable_timewindows: The unavailable_timewindows of this AutoPlanResponse.  # noqa: E501
        :type: list[TimeSlotModel]
        """

        self._unavailable_timewindows = unavailable_timewindows

    @property
    def latest_analyzed_date(self):
        """Gets the latest_analyzed_date of this AutoPlanResponse.  # noqa: E501

          # noqa: E501

        :return: The latest_analyzed_date of this AutoPlanResponse.  # noqa: E501
        :rtype: date
        """
        return self._latest_analyzed_date

    @latest_analyzed_date.setter
    def latest_analyzed_date(self, latest_analyzed_date):
        """Sets the latest_analyzed_date of this AutoPlanResponse.

          # noqa: E501

        :param latest_analyzed_date: The latest_analyzed_date of this AutoPlanResponse.  # noqa: E501
        :type: date
        """

        self._latest_analyzed_date = latest_analyzed_date

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
        if issubclass(AutoPlanResponse, dict):
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
        if not isinstance(other, AutoPlanResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoPlanResponse):
            return True

        return self.to_dict() != other.to_dict()
