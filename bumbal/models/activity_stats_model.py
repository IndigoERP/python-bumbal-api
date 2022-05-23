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


class ActivityStatsModel(object):
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
        'nr_of_package_lines': 'int',
        'nr_of_bundled_activities': 'int',
        'nr_of_transactions': 'int',
        'nr_of_notes': 'int',
        'nr_of_irregularities': 'int',
        'nr_of_files': 'int'
    }

    attribute_map = {
        'nr_of_package_lines': 'nr_of_package_lines',
        'nr_of_bundled_activities': 'nr_of_bundled_activities',
        'nr_of_transactions': 'nr_of_transactions',
        'nr_of_notes': 'nr_of_notes',
        'nr_of_irregularities': 'nr_of_irregularities',
        'nr_of_files': 'nr_of_files'
    }

    def __init__(self, nr_of_package_lines=None, nr_of_bundled_activities=None, nr_of_transactions=None, nr_of_notes=None, nr_of_irregularities=None, nr_of_files=None, _configuration=None):  # noqa: E501
        """ActivityStatsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._nr_of_package_lines = None
        self._nr_of_bundled_activities = None
        self._nr_of_transactions = None
        self._nr_of_notes = None
        self._nr_of_irregularities = None
        self._nr_of_files = None
        self.discriminator = None

        if nr_of_package_lines is not None:
            self.nr_of_package_lines = nr_of_package_lines
        if nr_of_bundled_activities is not None:
            self.nr_of_bundled_activities = nr_of_bundled_activities
        if nr_of_transactions is not None:
            self.nr_of_transactions = nr_of_transactions
        if nr_of_notes is not None:
            self.nr_of_notes = nr_of_notes
        if nr_of_irregularities is not None:
            self.nr_of_irregularities = nr_of_irregularities
        if nr_of_files is not None:
            self.nr_of_files = nr_of_files

    @property
    def nr_of_package_lines(self):
        """Gets the nr_of_package_lines of this ActivityStatsModel.  # noqa: E501

        nr of package lines  # noqa: E501

        :return: The nr_of_package_lines of this ActivityStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._nr_of_package_lines

    @nr_of_package_lines.setter
    def nr_of_package_lines(self, nr_of_package_lines):
        """Sets the nr_of_package_lines of this ActivityStatsModel.

        nr of package lines  # noqa: E501

        :param nr_of_package_lines: The nr_of_package_lines of this ActivityStatsModel.  # noqa: E501
        :type: int
        """

        self._nr_of_package_lines = nr_of_package_lines

    @property
    def nr_of_bundled_activities(self):
        """Gets the nr_of_bundled_activities of this ActivityStatsModel.  # noqa: E501

        nr of bundled activities  # noqa: E501

        :return: The nr_of_bundled_activities of this ActivityStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._nr_of_bundled_activities

    @nr_of_bundled_activities.setter
    def nr_of_bundled_activities(self, nr_of_bundled_activities):
        """Sets the nr_of_bundled_activities of this ActivityStatsModel.

        nr of bundled activities  # noqa: E501

        :param nr_of_bundled_activities: The nr_of_bundled_activities of this ActivityStatsModel.  # noqa: E501
        :type: int
        """

        self._nr_of_bundled_activities = nr_of_bundled_activities

    @property
    def nr_of_transactions(self):
        """Gets the nr_of_transactions of this ActivityStatsModel.  # noqa: E501

        nr of transactions  # noqa: E501

        :return: The nr_of_transactions of this ActivityStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._nr_of_transactions

    @nr_of_transactions.setter
    def nr_of_transactions(self, nr_of_transactions):
        """Sets the nr_of_transactions of this ActivityStatsModel.

        nr of transactions  # noqa: E501

        :param nr_of_transactions: The nr_of_transactions of this ActivityStatsModel.  # noqa: E501
        :type: int
        """

        self._nr_of_transactions = nr_of_transactions

    @property
    def nr_of_notes(self):
        """Gets the nr_of_notes of this ActivityStatsModel.  # noqa: E501

        nr of notes  # noqa: E501

        :return: The nr_of_notes of this ActivityStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._nr_of_notes

    @nr_of_notes.setter
    def nr_of_notes(self, nr_of_notes):
        """Sets the nr_of_notes of this ActivityStatsModel.

        nr of notes  # noqa: E501

        :param nr_of_notes: The nr_of_notes of this ActivityStatsModel.  # noqa: E501
        :type: int
        """

        self._nr_of_notes = nr_of_notes

    @property
    def nr_of_irregularities(self):
        """Gets the nr_of_irregularities of this ActivityStatsModel.  # noqa: E501

        nr of irregularities  # noqa: E501

        :return: The nr_of_irregularities of this ActivityStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._nr_of_irregularities

    @nr_of_irregularities.setter
    def nr_of_irregularities(self, nr_of_irregularities):
        """Sets the nr_of_irregularities of this ActivityStatsModel.

        nr of irregularities  # noqa: E501

        :param nr_of_irregularities: The nr_of_irregularities of this ActivityStatsModel.  # noqa: E501
        :type: int
        """

        self._nr_of_irregularities = nr_of_irregularities

    @property
    def nr_of_files(self):
        """Gets the nr_of_files of this ActivityStatsModel.  # noqa: E501

        nr of files  # noqa: E501

        :return: The nr_of_files of this ActivityStatsModel.  # noqa: E501
        :rtype: int
        """
        return self._nr_of_files

    @nr_of_files.setter
    def nr_of_files(self, nr_of_files):
        """Sets the nr_of_files of this ActivityStatsModel.

        nr of files  # noqa: E501

        :param nr_of_files: The nr_of_files of this ActivityStatsModel.  # noqa: E501
        :type: int
        """

        self._nr_of_files = nr_of_files

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
        if issubclass(ActivityStatsModel, dict):
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
        if not isinstance(other, ActivityStatsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActivityStatsModel):
            return True

        return self.to_dict() != other.to_dict()
