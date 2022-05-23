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


class EquipmentOptionsModel(object):
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
        'include_equipment_type_name': 'bool',
        'include_equipment_tags': 'bool',
        'include_tag_type_name': 'bool',
        'include_equipment_meta_data': 'bool',
        'include_equipment_files': 'bool',
        'include_equipment_files_meta_data': 'bool',
        'include_equipment_notes': 'bool',
        'include_equipment_note_tags': 'bool',
        'include_equipment_links': 'bool',
        'include_capacities': 'bool',
        'include_applied_capacities': 'bool'
    }

    attribute_map = {
        'include_equipment_type_name': 'include_equipment_type_name',
        'include_equipment_tags': 'include_equipment_tags',
        'include_tag_type_name': 'include_tag_type_name',
        'include_equipment_meta_data': 'include_equipment_meta_data',
        'include_equipment_files': 'include_equipment_files',
        'include_equipment_files_meta_data': 'include_equipment_files_meta_data',
        'include_equipment_notes': 'include_equipment_notes',
        'include_equipment_note_tags': 'include_equipment_note_tags',
        'include_equipment_links': 'include_equipment_links',
        'include_capacities': 'include_capacities',
        'include_applied_capacities': 'include_applied_capacities'
    }

    def __init__(self, include_equipment_type_name=None, include_equipment_tags=None, include_tag_type_name=None, include_equipment_meta_data=None, include_equipment_files=None, include_equipment_files_meta_data=None, include_equipment_notes=None, include_equipment_note_tags=None, include_equipment_links=None, include_capacities=None, include_applied_capacities=None, _configuration=None):  # noqa: E501
        """EquipmentOptionsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._include_equipment_type_name = None
        self._include_equipment_tags = None
        self._include_tag_type_name = None
        self._include_equipment_meta_data = None
        self._include_equipment_files = None
        self._include_equipment_files_meta_data = None
        self._include_equipment_notes = None
        self._include_equipment_note_tags = None
        self._include_equipment_links = None
        self._include_capacities = None
        self._include_applied_capacities = None
        self.discriminator = None

        if include_equipment_type_name is not None:
            self.include_equipment_type_name = include_equipment_type_name
        if include_equipment_tags is not None:
            self.include_equipment_tags = include_equipment_tags
        if include_tag_type_name is not None:
            self.include_tag_type_name = include_tag_type_name
        if include_equipment_meta_data is not None:
            self.include_equipment_meta_data = include_equipment_meta_data
        if include_equipment_files is not None:
            self.include_equipment_files = include_equipment_files
        if include_equipment_files_meta_data is not None:
            self.include_equipment_files_meta_data = include_equipment_files_meta_data
        if include_equipment_notes is not None:
            self.include_equipment_notes = include_equipment_notes
        if include_equipment_note_tags is not None:
            self.include_equipment_note_tags = include_equipment_note_tags
        if include_equipment_links is not None:
            self.include_equipment_links = include_equipment_links
        if include_capacities is not None:
            self.include_capacities = include_capacities
        if include_applied_capacities is not None:
            self.include_applied_capacities = include_applied_capacities

    @property
    def include_equipment_type_name(self):
        """Gets the include_equipment_type_name of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_equipment_type_name of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_equipment_type_name

    @include_equipment_type_name.setter
    def include_equipment_type_name(self, include_equipment_type_name):
        """Sets the include_equipment_type_name of this EquipmentOptionsModel.

          # noqa: E501

        :param include_equipment_type_name: The include_equipment_type_name of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_equipment_type_name = include_equipment_type_name

    @property
    def include_equipment_tags(self):
        """Gets the include_equipment_tags of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_equipment_tags of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_equipment_tags

    @include_equipment_tags.setter
    def include_equipment_tags(self, include_equipment_tags):
        """Sets the include_equipment_tags of this EquipmentOptionsModel.

          # noqa: E501

        :param include_equipment_tags: The include_equipment_tags of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_equipment_tags = include_equipment_tags

    @property
    def include_tag_type_name(self):
        """Gets the include_tag_type_name of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_tag_type_name of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_tag_type_name

    @include_tag_type_name.setter
    def include_tag_type_name(self, include_tag_type_name):
        """Sets the include_tag_type_name of this EquipmentOptionsModel.

          # noqa: E501

        :param include_tag_type_name: The include_tag_type_name of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_tag_type_name = include_tag_type_name

    @property
    def include_equipment_meta_data(self):
        """Gets the include_equipment_meta_data of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_equipment_meta_data of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_equipment_meta_data

    @include_equipment_meta_data.setter
    def include_equipment_meta_data(self, include_equipment_meta_data):
        """Sets the include_equipment_meta_data of this EquipmentOptionsModel.

          # noqa: E501

        :param include_equipment_meta_data: The include_equipment_meta_data of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_equipment_meta_data = include_equipment_meta_data

    @property
    def include_equipment_files(self):
        """Gets the include_equipment_files of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_equipment_files of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_equipment_files

    @include_equipment_files.setter
    def include_equipment_files(self, include_equipment_files):
        """Sets the include_equipment_files of this EquipmentOptionsModel.

          # noqa: E501

        :param include_equipment_files: The include_equipment_files of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_equipment_files = include_equipment_files

    @property
    def include_equipment_files_meta_data(self):
        """Gets the include_equipment_files_meta_data of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_equipment_files_meta_data of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_equipment_files_meta_data

    @include_equipment_files_meta_data.setter
    def include_equipment_files_meta_data(self, include_equipment_files_meta_data):
        """Sets the include_equipment_files_meta_data of this EquipmentOptionsModel.

          # noqa: E501

        :param include_equipment_files_meta_data: The include_equipment_files_meta_data of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_equipment_files_meta_data = include_equipment_files_meta_data

    @property
    def include_equipment_notes(self):
        """Gets the include_equipment_notes of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_equipment_notes of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_equipment_notes

    @include_equipment_notes.setter
    def include_equipment_notes(self, include_equipment_notes):
        """Sets the include_equipment_notes of this EquipmentOptionsModel.

          # noqa: E501

        :param include_equipment_notes: The include_equipment_notes of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_equipment_notes = include_equipment_notes

    @property
    def include_equipment_note_tags(self):
        """Gets the include_equipment_note_tags of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_equipment_note_tags of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_equipment_note_tags

    @include_equipment_note_tags.setter
    def include_equipment_note_tags(self, include_equipment_note_tags):
        """Sets the include_equipment_note_tags of this EquipmentOptionsModel.

          # noqa: E501

        :param include_equipment_note_tags: The include_equipment_note_tags of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_equipment_note_tags = include_equipment_note_tags

    @property
    def include_equipment_links(self):
        """Gets the include_equipment_links of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_equipment_links of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_equipment_links

    @include_equipment_links.setter
    def include_equipment_links(self, include_equipment_links):
        """Sets the include_equipment_links of this EquipmentOptionsModel.

          # noqa: E501

        :param include_equipment_links: The include_equipment_links of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_equipment_links = include_equipment_links

    @property
    def include_capacities(self):
        """Gets the include_capacities of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_capacities of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_capacities

    @include_capacities.setter
    def include_capacities(self, include_capacities):
        """Sets the include_capacities of this EquipmentOptionsModel.

          # noqa: E501

        :param include_capacities: The include_capacities of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_capacities = include_capacities

    @property
    def include_applied_capacities(self):
        """Gets the include_applied_capacities of this EquipmentOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_applied_capacities of this EquipmentOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_applied_capacities

    @include_applied_capacities.setter
    def include_applied_capacities(self, include_applied_capacities):
        """Sets the include_applied_capacities of this EquipmentOptionsModel.

          # noqa: E501

        :param include_applied_capacities: The include_applied_capacities of this EquipmentOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_applied_capacities = include_applied_capacities

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
        if issubclass(EquipmentOptionsModel, dict):
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
        if not isinstance(other, EquipmentOptionsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquipmentOptionsModel):
            return True

        return self.to_dict() != other.to_dict()