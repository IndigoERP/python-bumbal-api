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


class AddActivitiesToRouteArguments(object):
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
        'route_id': 'int',
        'activities': 'list[ActivityForToRouteModel]',
        'options': 'dict(str, bool)'
    }

    attribute_map = {
        'route_id': 'route_id',
        'activities': 'activities',
        'options': 'options'
    }

    def __init__(self, route_id=None, activities=None, options=None, _configuration=None):  # noqa: E501
        """AddActivitiesToRouteArguments - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._route_id = None
        self._activities = None
        self._options = None
        self.discriminator = None

        if route_id is not None:
            self.route_id = route_id
        if activities is not None:
            self.activities = activities
        if options is not None:
            self.options = options

    @property
    def route_id(self):
        """Gets the route_id of this AddActivitiesToRouteArguments.  # noqa: E501

        Unique ID of Route  # noqa: E501

        :return: The route_id of this AddActivitiesToRouteArguments.  # noqa: E501
        :rtype: int
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id):
        """Sets the route_id of this AddActivitiesToRouteArguments.

        Unique ID of Route  # noqa: E501

        :param route_id: The route_id of this AddActivitiesToRouteArguments.  # noqa: E501
        :type: int
        """

        self._route_id = route_id

    @property
    def activities(self):
        """Gets the activities of this AddActivitiesToRouteArguments.  # noqa: E501

          # noqa: E501

        :return: The activities of this AddActivitiesToRouteArguments.  # noqa: E501
        :rtype: list[ActivityForToRouteModel]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this AddActivitiesToRouteArguments.

          # noqa: E501

        :param activities: The activities of this AddActivitiesToRouteArguments.  # noqa: E501
        :type: list[ActivityForToRouteModel]
        """

        self._activities = activities

    @property
    def options(self):
        """Gets the options of this AddActivitiesToRouteArguments.  # noqa: E501

          # noqa: E501

        :return: The options of this AddActivitiesToRouteArguments.  # noqa: E501
        :rtype: dict(str, bool)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this AddActivitiesToRouteArguments.

          # noqa: E501

        :param options: The options of this AddActivitiesToRouteArguments.  # noqa: E501
        :type: dict(str, bool)
        """

        self._options = options

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
        if issubclass(AddActivitiesToRouteArguments, dict):
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
        if not isinstance(other, AddActivitiesToRouteArguments):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddActivitiesToRouteArguments):
            return True

        return self.to_dict() != other.to_dict()
