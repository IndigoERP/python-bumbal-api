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


class FileModel(object):
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
        'uuid': 'str',
        'file_type_id': 'int',
        'file_type_name': 'str',
        'object_id': 'int',
        'object_type': 'int',
        'object_type_name': 'str',
        'reference': 'str',
        'location': 'str',
        'base64': 'str',
        'meta_data': 'list[MetaDataModel]',
        'created_by': 'int',
        'updated_by': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'links': 'list[LinkModel]'
    }

    attribute_map = {
        'id': 'id',
        'uuid': 'uuid',
        'file_type_id': 'file_type_id',
        'file_type_name': 'file_type_name',
        'object_id': 'object_id',
        'object_type': 'object_type',
        'object_type_name': 'object_type_name',
        'reference': 'reference',
        'location': 'location',
        'base64': 'base64',
        'meta_data': 'meta_data',
        'created_by': 'created_by',
        'updated_by': 'updated_by',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'links': 'links'
    }

    def __init__(self, id=None, uuid=None, file_type_id=None, file_type_name=None, object_id=None, object_type=None, object_type_name=None, reference=None, location=None, base64=None, meta_data=None, created_by=None, updated_by=None, created_at=None, updated_at=None, links=None, _configuration=None):  # noqa: E501
        """FileModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._uuid = None
        self._file_type_id = None
        self._file_type_name = None
        self._object_id = None
        self._object_type = None
        self._object_type_name = None
        self._reference = None
        self._location = None
        self._base64 = None
        self._meta_data = None
        self._created_by = None
        self._updated_by = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if uuid is not None:
            self.uuid = uuid
        if file_type_id is not None:
            self.file_type_id = file_type_id
        if file_type_name is not None:
            self.file_type_name = file_type_name
        if object_id is not None:
            self.object_id = object_id
        if object_type is not None:
            self.object_type = object_type
        if object_type_name is not None:
            self.object_type_name = object_type_name
        if reference is not None:
            self.reference = reference
        if location is not None:
            self.location = location
        if base64 is not None:
            self.base64 = base64
        if meta_data is not None:
            self.meta_data = meta_data
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The id of this FileModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileModel.

          # noqa: E501

        :param id: The id of this FileModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The uuid of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this FileModel.

          # noqa: E501

        :param uuid: The uuid of this FileModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def file_type_id(self):
        """Gets the file_type_id of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The file_type_id of this FileModel.  # noqa: E501
        :rtype: int
        """
        return self._file_type_id

    @file_type_id.setter
    def file_type_id(self, file_type_id):
        """Sets the file_type_id of this FileModel.

          # noqa: E501

        :param file_type_id: The file_type_id of this FileModel.  # noqa: E501
        :type: int
        """

        self._file_type_id = file_type_id

    @property
    def file_type_name(self):
        """Gets the file_type_name of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The file_type_name of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._file_type_name

    @file_type_name.setter
    def file_type_name(self, file_type_name):
        """Sets the file_type_name of this FileModel.

          # noqa: E501

        :param file_type_name: The file_type_name of this FileModel.  # noqa: E501
        :type: str
        """

        self._file_type_name = file_type_name

    @property
    def object_id(self):
        """Gets the object_id of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The object_id of this FileModel.  # noqa: E501
        :rtype: int
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this FileModel.

          # noqa: E501

        :param object_id: The object_id of this FileModel.  # noqa: E501
        :type: int
        """

        self._object_id = object_id

    @property
    def object_type(self):
        """Gets the object_type of this FileModel.  # noqa: E501

        Object type ID  # noqa: E501

        :return: The object_type of this FileModel.  # noqa: E501
        :rtype: int
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this FileModel.

        Object type ID  # noqa: E501

        :param object_type: The object_type of this FileModel.  # noqa: E501
        :type: int
        """

        self._object_type = object_type

    @property
    def object_type_name(self):
        """Gets the object_type_name of this FileModel.  # noqa: E501

        Object type name  # noqa: E501

        :return: The object_type_name of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._object_type_name

    @object_type_name.setter
    def object_type_name(self, object_type_name):
        """Sets the object_type_name of this FileModel.

        Object type name  # noqa: E501

        :param object_type_name: The object_type_name of this FileModel.  # noqa: E501
        :type: str
        """

        self._object_type_name = object_type_name

    @property
    def reference(self):
        """Gets the reference of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The reference of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this FileModel.

          # noqa: E501

        :param reference: The reference of this FileModel.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def location(self):
        """Gets the location of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The location of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this FileModel.

          # noqa: E501

        :param location: The location of this FileModel.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def base64(self):
        """Gets the base64 of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The base64 of this FileModel.  # noqa: E501
        :rtype: str
        """
        return self._base64

    @base64.setter
    def base64(self, base64):
        """Sets the base64 of this FileModel.

          # noqa: E501

        :param base64: The base64 of this FileModel.  # noqa: E501
        :type: str
        """

        self._base64 = base64

    @property
    def meta_data(self):
        """Gets the meta_data of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The meta_data of this FileModel.  # noqa: E501
        :rtype: list[MetaDataModel]
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this FileModel.

          # noqa: E501

        :param meta_data: The meta_data of this FileModel.  # noqa: E501
        :type: list[MetaDataModel]
        """

        self._meta_data = meta_data

    @property
    def created_by(self):
        """Gets the created_by of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The created_by of this FileModel.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this FileModel.

          # noqa: E501

        :param created_by: The created_by of this FileModel.  # noqa: E501
        :type: int
        """

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The updated_by of this FileModel.  # noqa: E501
        :rtype: int
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this FileModel.

          # noqa: E501

        :param updated_by: The updated_by of this FileModel.  # noqa: E501
        :type: int
        """

        self._updated_by = updated_by

    @property
    def created_at(self):
        """Gets the created_at of this FileModel.  # noqa: E501

        created_at  # noqa: E501

        :return: The created_at of this FileModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FileModel.

        created_at  # noqa: E501

        :param created_at: The created_at of this FileModel.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FileModel.  # noqa: E501

        updated_at  # noqa: E501

        :return: The updated_at of this FileModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FileModel.

        updated_at  # noqa: E501

        :param updated_at: The updated_at of this FileModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def links(self):
        """Gets the links of this FileModel.  # noqa: E501

          # noqa: E501

        :return: The links of this FileModel.  # noqa: E501
        :rtype: list[LinkModel]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this FileModel.

          # noqa: E501

        :param links: The links of this FileModel.  # noqa: E501
        :type: list[LinkModel]
        """

        self._links = links

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
        if issubclass(FileModel, dict):
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
        if not isinstance(other, FileModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileModel):
            return True

        return self.to_dict() != other.to_dict()
