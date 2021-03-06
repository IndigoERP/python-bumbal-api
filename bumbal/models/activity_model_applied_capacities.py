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


class ActivityModelAppliedCapacities(object):
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
        'applied_capacities': 'AppliedCapacitiesModel'
    }

    attribute_map = {
        'applied_capacities': 'applied_capacities'
    }

    def __init__(self, applied_capacities=None, _configuration=None):  # noqa: E501
        """ActivityModelAppliedCapacities - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._applied_capacities = None
        self.discriminator = None

        if applied_capacities is not None:
            self.applied_capacities = applied_capacities

    @property
    def applied_capacities(self):
        """Gets the applied_capacities of this ActivityModelAppliedCapacities.  # noqa: E501

          # noqa: E501

        :return: The applied_capacities of this ActivityModelAppliedCapacities.  # noqa: E501
        :rtype: AppliedCapacitiesModel
        """
        return self._applied_capacities

    @applied_capacities.setter
    def applied_capacities(self, applied_capacities):
        """Sets the applied_capacities of this ActivityModelAppliedCapacities.

          # noqa: E501

        :param applied_capacities: The applied_capacities of this ActivityModelAppliedCapacities.  # noqa: E501
        :type: AppliedCapacitiesModel
        """

        self._applied_capacities = applied_capacities

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
        if issubclass(ActivityModelAppliedCapacities, dict):
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
        if not isinstance(other, ActivityModelAppliedCapacities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActivityModelAppliedCapacities):
            return True

        return self.to_dict() != other.to_dict()
