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


class AutoPlanDataModel(object):
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
        'token': 'int',
        'availability_key': 'str',
        'activity': 'list[ActivityModel]'
    }

    attribute_map = {
        'token': 'token',
        'availability_key': 'availability_key',
        'activity': 'activity'
    }

    def __init__(self, token=None, availability_key=None, activity=None, _configuration=None):  # noqa: E501
        """AutoPlanDataModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._token = None
        self._availability_key = None
        self._activity = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if availability_key is not None:
            self.availability_key = availability_key
        if activity is not None:
            self.activity = activity

    @property
    def token(self):
        """Gets the token of this AutoPlanDataModel.  # noqa: E501

        unique per api request  # noqa: E501

        :return: The token of this AutoPlanDataModel.  # noqa: E501
        :rtype: int
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AutoPlanDataModel.

        unique per api request  # noqa: E501

        :param token: The token of this AutoPlanDataModel.  # noqa: E501
        :type: int
        """

        self._token = token

    @property
    def availability_key(self):
        """Gets the availability_key of this AutoPlanDataModel.  # noqa: E501

        unique key from availability result, used to reuse fromer result  # noqa: E501

        :return: The availability_key of this AutoPlanDataModel.  # noqa: E501
        :rtype: str
        """
        return self._availability_key

    @availability_key.setter
    def availability_key(self, availability_key):
        """Sets the availability_key of this AutoPlanDataModel.

        unique key from availability result, used to reuse fromer result  # noqa: E501

        :param availability_key: The availability_key of this AutoPlanDataModel.  # noqa: E501
        :type: str
        """

        self._availability_key = availability_key

    @property
    def activity(self):
        """Gets the activity of this AutoPlanDataModel.  # noqa: E501

          # noqa: E501

        :return: The activity of this AutoPlanDataModel.  # noqa: E501
        :rtype: list[ActivityModel]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this AutoPlanDataModel.

          # noqa: E501

        :param activity: The activity of this AutoPlanDataModel.  # noqa: E501
        :type: list[ActivityModel]
        """

        self._activity = activity

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
        if issubclass(AutoPlanDataModel, dict):
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
        if not isinstance(other, AutoPlanDataModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AutoPlanDataModel):
            return True

        return self.to_dict() != other.to_dict()
