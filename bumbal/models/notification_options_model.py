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


class NotificationOptionsModel(object):
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
        'include_notification_files': 'bool',
        'include_updated_by': 'bool',
        'include_record_info': 'bool',
        'include_object_type_name': 'bool',
        'include_notification_category_name': 'bool',
        'include_user_notification': 'bool'
    }

    attribute_map = {
        'include_notification_files': 'include_notification_files',
        'include_updated_by': 'include_updated_by',
        'include_record_info': 'include_record_info',
        'include_object_type_name': 'include_object_type_name',
        'include_notification_category_name': 'include_notification_category_name',
        'include_user_notification': 'include_user_notification'
    }

    def __init__(self, include_notification_files=None, include_updated_by=None, include_record_info=None, include_object_type_name=None, include_notification_category_name=None, include_user_notification=None, _configuration=None):  # noqa: E501
        """NotificationOptionsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._include_notification_files = None
        self._include_updated_by = None
        self._include_record_info = None
        self._include_object_type_name = None
        self._include_notification_category_name = None
        self._include_user_notification = None
        self.discriminator = None

        if include_notification_files is not None:
            self.include_notification_files = include_notification_files
        if include_updated_by is not None:
            self.include_updated_by = include_updated_by
        if include_record_info is not None:
            self.include_record_info = include_record_info
        if include_object_type_name is not None:
            self.include_object_type_name = include_object_type_name
        if include_notification_category_name is not None:
            self.include_notification_category_name = include_notification_category_name
        if include_user_notification is not None:
            self.include_user_notification = include_user_notification

    @property
    def include_notification_files(self):
        """Gets the include_notification_files of this NotificationOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_notification_files of this NotificationOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_notification_files

    @include_notification_files.setter
    def include_notification_files(self, include_notification_files):
        """Sets the include_notification_files of this NotificationOptionsModel.

          # noqa: E501

        :param include_notification_files: The include_notification_files of this NotificationOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_notification_files = include_notification_files

    @property
    def include_updated_by(self):
        """Gets the include_updated_by of this NotificationOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_updated_by of this NotificationOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_updated_by

    @include_updated_by.setter
    def include_updated_by(self, include_updated_by):
        """Sets the include_updated_by of this NotificationOptionsModel.

          # noqa: E501

        :param include_updated_by: The include_updated_by of this NotificationOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_updated_by = include_updated_by

    @property
    def include_record_info(self):
        """Gets the include_record_info of this NotificationOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_record_info of this NotificationOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_record_info

    @include_record_info.setter
    def include_record_info(self, include_record_info):
        """Sets the include_record_info of this NotificationOptionsModel.

          # noqa: E501

        :param include_record_info: The include_record_info of this NotificationOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_record_info = include_record_info

    @property
    def include_object_type_name(self):
        """Gets the include_object_type_name of this NotificationOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_object_type_name of this NotificationOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_object_type_name

    @include_object_type_name.setter
    def include_object_type_name(self, include_object_type_name):
        """Sets the include_object_type_name of this NotificationOptionsModel.

          # noqa: E501

        :param include_object_type_name: The include_object_type_name of this NotificationOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_object_type_name = include_object_type_name

    @property
    def include_notification_category_name(self):
        """Gets the include_notification_category_name of this NotificationOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_notification_category_name of this NotificationOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_notification_category_name

    @include_notification_category_name.setter
    def include_notification_category_name(self, include_notification_category_name):
        """Sets the include_notification_category_name of this NotificationOptionsModel.

          # noqa: E501

        :param include_notification_category_name: The include_notification_category_name of this NotificationOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_notification_category_name = include_notification_category_name

    @property
    def include_user_notification(self):
        """Gets the include_user_notification of this NotificationOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_user_notification of this NotificationOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_user_notification

    @include_user_notification.setter
    def include_user_notification(self, include_user_notification):
        """Sets the include_user_notification of this NotificationOptionsModel.

          # noqa: E501

        :param include_user_notification: The include_user_notification of this NotificationOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_user_notification = include_user_notification

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
        if issubclass(NotificationOptionsModel, dict):
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
        if not isinstance(other, NotificationOptionsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NotificationOptionsModel):
            return True

        return self.to_dict() != other.to_dict()
