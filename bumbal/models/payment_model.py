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


class PaymentModel(object):
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
        'active': 'bool',
        'activity_id': 'int',
        'amount': 'int',
        'title': 'str'
    }

    attribute_map = {
        'id': 'id',
        'active': 'active',
        'activity_id': 'activity_id',
        'amount': 'amount',
        'title': 'title'
    }

    def __init__(self, id=None, active=None, activity_id=None, amount=None, title=None, _configuration=None):  # noqa: E501
        """PaymentModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._active = None
        self._activity_id = None
        self._amount = None
        self._title = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if active is not None:
            self.active = active
        if activity_id is not None:
            self.activity_id = activity_id
        if amount is not None:
            self.amount = amount
        if title is not None:
            self.title = title

    @property
    def id(self):
        """Gets the id of this PaymentModel.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this PaymentModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentModel.

        Unique Identifier  # noqa: E501

        :param id: The id of this PaymentModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def active(self):
        """Gets the active of this PaymentModel.  # noqa: E501

        if active=0: Payment has been removed and is no longer visible in any bumbal interface  # noqa: E501

        :return: The active of this PaymentModel.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PaymentModel.

        if active=0: Payment has been removed and is no longer visible in any bumbal interface  # noqa: E501

        :param active: The active of this PaymentModel.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def activity_id(self):
        """Gets the activity_id of this PaymentModel.  # noqa: E501

        id of the activity this payment is bound to  # noqa: E501

        :return: The activity_id of this PaymentModel.  # noqa: E501
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this PaymentModel.

        id of the activity this payment is bound to  # noqa: E501

        :param activity_id: The activity_id of this PaymentModel.  # noqa: E501
        :type: int
        """

        self._activity_id = activity_id

    @property
    def amount(self):
        """Gets the amount of this PaymentModel.  # noqa: E501

        amount of the payment in cents  # noqa: E501

        :return: The amount of this PaymentModel.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentModel.

        amount of the payment in cents  # noqa: E501

        :param amount: The amount of this PaymentModel.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def title(self):
        """Gets the title of this PaymentModel.  # noqa: E501

        title of the payment  # noqa: E501

        :return: The title of this PaymentModel.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PaymentModel.

        title of the payment  # noqa: E501

        :param title: The title of this PaymentModel.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(PaymentModel, dict):
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
        if not isinstance(other, PaymentModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentModel):
            return True

        return self.to_dict() != other.to_dict()
