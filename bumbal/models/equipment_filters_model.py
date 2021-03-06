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


class EquipmentFiltersModel(object):
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
        'equipment_type_id': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'equipment_type_id': 'equipment_type_id'
    }

    def __init__(self, id=None, equipment_type_id=None, _configuration=None):  # noqa: E501
        """EquipmentFiltersModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._equipment_type_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if equipment_type_id is not None:
            self.equipment_type_id = equipment_type_id

    @property
    def id(self):
        """Gets the id of this EquipmentFiltersModel.  # noqa: E501

        Equipment ID  # noqa: E501

        :return: The id of this EquipmentFiltersModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquipmentFiltersModel.

        Equipment ID  # noqa: E501

        :param id: The id of this EquipmentFiltersModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def equipment_type_id(self):
        """Gets the equipment_type_id of this EquipmentFiltersModel.  # noqa: E501

        Equipment Type ID's  # noqa: E501

        :return: The equipment_type_id of this EquipmentFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._equipment_type_id

    @equipment_type_id.setter
    def equipment_type_id(self, equipment_type_id):
        """Sets the equipment_type_id of this EquipmentFiltersModel.

        Equipment Type ID's  # noqa: E501

        :param equipment_type_id: The equipment_type_id of this EquipmentFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._equipment_type_id = equipment_type_id

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
        if issubclass(EquipmentFiltersModel, dict):
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
        if not isinstance(other, EquipmentFiltersModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquipmentFiltersModel):
            return True

        return self.to_dict() != other.to_dict()
