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


class PackageTypeModel(object):
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
        'name': 'str',
        'active': 'bool',
        'links': 'list[LinkModel]',
        'meta_data': 'list[MetaDataModel]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'created_by': 'int',
        'updated_by': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'active': 'active',
        'links': 'links',
        'meta_data': 'meta_data',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'created_by': 'created_by',
        'updated_by': 'updated_by'
    }

    def __init__(self, id=None, name=None, active=None, links=None, meta_data=None, created_at=None, updated_at=None, created_by=None, updated_by=None, _configuration=None):  # noqa: E501
        """PackageTypeModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._active = None
        self._links = None
        self._meta_data = None
        self._created_at = None
        self._updated_at = None
        self._created_by = None
        self._updated_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if active is not None:
            self.active = active
        if links is not None:
            self.links = links
        if meta_data is not None:
            self.meta_data = meta_data
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by

    @property
    def id(self):
        """Gets the id of this PackageTypeModel.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this PackageTypeModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PackageTypeModel.

        Unique Identifier  # noqa: E501

        :param id: The id of this PackageTypeModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PackageTypeModel.  # noqa: E501

        Type of the Packages in the package line  # noqa: E501

        :return: The name of this PackageTypeModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PackageTypeModel.

        Type of the Packages in the package line  # noqa: E501

        :param name: The name of this PackageTypeModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def active(self):
        """Gets the active of this PackageTypeModel.  # noqa: E501

        if active=0: package line has been removed and is no longer visible in any bumbal interface  # noqa: E501

        :return: The active of this PackageTypeModel.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PackageTypeModel.

        if active=0: package line has been removed and is no longer visible in any bumbal interface  # noqa: E501

        :param active: The active of this PackageTypeModel.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def links(self):
        """Gets the links of this PackageTypeModel.  # noqa: E501

          # noqa: E501

        :return: The links of this PackageTypeModel.  # noqa: E501
        :rtype: list[LinkModel]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PackageTypeModel.

          # noqa: E501

        :param links: The links of this PackageTypeModel.  # noqa: E501
        :type: list[LinkModel]
        """

        self._links = links

    @property
    def meta_data(self):
        """Gets the meta_data of this PackageTypeModel.  # noqa: E501

          # noqa: E501

        :return: The meta_data of this PackageTypeModel.  # noqa: E501
        :rtype: list[MetaDataModel]
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this PackageTypeModel.

          # noqa: E501

        :param meta_data: The meta_data of this PackageTypeModel.  # noqa: E501
        :type: list[MetaDataModel]
        """

        self._meta_data = meta_data

    @property
    def created_at(self):
        """Gets the created_at of this PackageTypeModel.  # noqa: E501

        created_at date time  # noqa: E501

        :return: The created_at of this PackageTypeModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PackageTypeModel.

        created_at date time  # noqa: E501

        :param created_at: The created_at of this PackageTypeModel.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PackageTypeModel.  # noqa: E501

        updated_at date time  # noqa: E501

        :return: The updated_at of this PackageTypeModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PackageTypeModel.

        updated_at date time  # noqa: E501

        :param updated_at: The updated_at of this PackageTypeModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def created_by(self):
        """Gets the created_by of this PackageTypeModel.  # noqa: E501

        created_by user id  # noqa: E501

        :return: The created_by of this PackageTypeModel.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this PackageTypeModel.

        created_by user id  # noqa: E501

        :param created_by: The created_by of this PackageTypeModel.  # noqa: E501
        :type: int
        """

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this PackageTypeModel.  # noqa: E501

        updated_by user id  # noqa: E501

        :return: The updated_by of this PackageTypeModel.  # noqa: E501
        :rtype: int
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this PackageTypeModel.

        updated_by user id  # noqa: E501

        :param updated_by: The updated_by of this PackageTypeModel.  # noqa: E501
        :type: int
        """

        self._updated_by = updated_by

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
        if issubclass(PackageTypeModel, dict):
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
        if not isinstance(other, PackageTypeModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PackageTypeModel):
            return True

        return self.to_dict() != other.to_dict()
