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


class NoteFiltersModel(object):
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
        'updated_at_since': 'datetime',
        'updated_at_till': 'datetime',
        'object_type': 'list[int]',
        'object_type_name': 'list[str]',
        'note_category_id': 'list[int]',
        'note_category_name': 'list[str]',
        'object_id': 'list[int]',
        'title': 'list[str]',
        'content': 'list[str]'
    }

    attribute_map = {
        'updated_at_since': 'updated_at_since',
        'updated_at_till': 'updated_at_till',
        'object_type': 'object_type',
        'object_type_name': 'object_type_name',
        'note_category_id': 'note_category_id',
        'note_category_name': 'note_category_name',
        'object_id': 'object_id',
        'title': 'title',
        'content': 'content'
    }

    def __init__(self, updated_at_since=None, updated_at_till=None, object_type=None, object_type_name=None, note_category_id=None, note_category_name=None, object_id=None, title=None, content=None, _configuration=None):  # noqa: E501
        """NoteFiltersModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._updated_at_since = None
        self._updated_at_till = None
        self._object_type = None
        self._object_type_name = None
        self._note_category_id = None
        self._note_category_name = None
        self._object_id = None
        self._title = None
        self._content = None
        self.discriminator = None

        if updated_at_since is not None:
            self.updated_at_since = updated_at_since
        if updated_at_till is not None:
            self.updated_at_till = updated_at_till
        if object_type is not None:
            self.object_type = object_type
        if object_type_name is not None:
            self.object_type_name = object_type_name
        if note_category_id is not None:
            self.note_category_id = note_category_id
        if note_category_name is not None:
            self.note_category_name = note_category_name
        if object_id is not None:
            self.object_id = object_id
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content

    @property
    def updated_at_since(self):
        """Gets the updated_at_since of this NoteFiltersModel.  # noqa: E501

        Show updated since  # noqa: E501

        :return: The updated_at_since of this NoteFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_since

    @updated_at_since.setter
    def updated_at_since(self, updated_at_since):
        """Sets the updated_at_since of this NoteFiltersModel.

        Show updated since  # noqa: E501

        :param updated_at_since: The updated_at_since of this NoteFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_since = updated_at_since

    @property
    def updated_at_till(self):
        """Gets the updated_at_till of this NoteFiltersModel.  # noqa: E501

        Show updated till  # noqa: E501

        :return: The updated_at_till of this NoteFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_till

    @updated_at_till.setter
    def updated_at_till(self, updated_at_till):
        """Sets the updated_at_till of this NoteFiltersModel.

        Show updated till  # noqa: E501

        :param updated_at_till: The updated_at_till of this NoteFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_till = updated_at_till

    @property
    def object_type(self):
        """Gets the object_type of this NoteFiltersModel.  # noqa: E501

        Object type IDs  # noqa: E501

        :return: The object_type of this NoteFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this NoteFiltersModel.

        Object type IDs  # noqa: E501

        :param object_type: The object_type of this NoteFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._object_type = object_type

    @property
    def object_type_name(self):
        """Gets the object_type_name of this NoteFiltersModel.  # noqa: E501

        Object type names  # noqa: E501

        :return: The object_type_name of this NoteFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._object_type_name

    @object_type_name.setter
    def object_type_name(self, object_type_name):
        """Sets the object_type_name of this NoteFiltersModel.

        Object type names  # noqa: E501

        :param object_type_name: The object_type_name of this NoteFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._object_type_name = object_type_name

    @property
    def note_category_id(self):
        """Gets the note_category_id of this NoteFiltersModel.  # noqa: E501

        Note category id  # noqa: E501

        :return: The note_category_id of this NoteFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._note_category_id

    @note_category_id.setter
    def note_category_id(self, note_category_id):
        """Sets the note_category_id of this NoteFiltersModel.

        Note category id  # noqa: E501

        :param note_category_id: The note_category_id of this NoteFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._note_category_id = note_category_id

    @property
    def note_category_name(self):
        """Gets the note_category_name of this NoteFiltersModel.  # noqa: E501

        Note category name  # noqa: E501

        :return: The note_category_name of this NoteFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._note_category_name

    @note_category_name.setter
    def note_category_name(self, note_category_name):
        """Sets the note_category_name of this NoteFiltersModel.

        Note category name  # noqa: E501

        :param note_category_name: The note_category_name of this NoteFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._note_category_name = note_category_name

    @property
    def object_id(self):
        """Gets the object_id of this NoteFiltersModel.  # noqa: E501

        Object ID  # noqa: E501

        :return: The object_id of this NoteFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this NoteFiltersModel.

        Object ID  # noqa: E501

        :param object_id: The object_id of this NoteFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._object_id = object_id

    @property
    def title(self):
        """Gets the title of this NoteFiltersModel.  # noqa: E501

        Note titles  # noqa: E501

        :return: The title of this NoteFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NoteFiltersModel.

        Note titles  # noqa: E501

        :param title: The title of this NoteFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._title = title

    @property
    def content(self):
        """Gets the content of this NoteFiltersModel.  # noqa: E501

        Note content  # noqa: E501

        :return: The content of this NoteFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this NoteFiltersModel.

        Note content  # noqa: E501

        :param content: The content of this NoteFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._content = content

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
        if issubclass(NoteFiltersModel, dict):
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
        if not isinstance(other, NoteFiltersModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NoteFiltersModel):
            return True

        return self.to_dict() != other.to_dict()
