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


class TransactionModel(object):
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
        'transaction_type': 'int',
        'paid': 'bool',
        'failed': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'active': 'active',
        'activity_id': 'activity_id',
        'amount': 'amount',
        'transaction_type': 'transaction_type',
        'paid': 'paid',
        'failed': 'failed'
    }

    def __init__(self, id=None, active=None, activity_id=None, amount=None, transaction_type=None, paid=None, failed=None, _configuration=None):  # noqa: E501
        """TransactionModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._active = None
        self._activity_id = None
        self._amount = None
        self._transaction_type = None
        self._paid = None
        self._failed = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if active is not None:
            self.active = active
        if activity_id is not None:
            self.activity_id = activity_id
        if amount is not None:
            self.amount = amount
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if paid is not None:
            self.paid = paid
        if failed is not None:
            self.failed = failed

    @property
    def id(self):
        """Gets the id of this TransactionModel.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this TransactionModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionModel.

        Unique Identifier  # noqa: E501

        :param id: The id of this TransactionModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def active(self):
        """Gets the active of this TransactionModel.  # noqa: E501

        if active=0: Transaction has been removed and is no longer visible in any bumbal interface  # noqa: E501

        :return: The active of this TransactionModel.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this TransactionModel.

        if active=0: Transaction has been removed and is no longer visible in any bumbal interface  # noqa: E501

        :param active: The active of this TransactionModel.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def activity_id(self):
        """Gets the activity_id of this TransactionModel.  # noqa: E501

        activity id it belongs to  # noqa: E501

        :return: The activity_id of this TransactionModel.  # noqa: E501
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this TransactionModel.

        activity id it belongs to  # noqa: E501

        :param activity_id: The activity_id of this TransactionModel.  # noqa: E501
        :type: int
        """

        self._activity_id = activity_id

    @property
    def amount(self):
        """Gets the amount of this TransactionModel.  # noqa: E501

        amount in cents, 42 euro is 4200 cents  # noqa: E501

        :return: The amount of this TransactionModel.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionModel.

        amount in cents, 42 euro is 4200 cents  # noqa: E501

        :param amount: The amount of this TransactionModel.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def transaction_type(self):
        """Gets the transaction_type of this TransactionModel.  # noqa: E501

        Type of Transaction: 1 = cash, 2 = pin, 3 = online  # noqa: E501

        :return: The transaction_type of this TransactionModel.  # noqa: E501
        :rtype: int
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this TransactionModel.

        Type of Transaction: 1 = cash, 2 = pin, 3 = online  # noqa: E501

        :param transaction_type: The transaction_type of this TransactionModel.  # noqa: E501
        :type: int
        """

        self._transaction_type = transaction_type

    @property
    def paid(self):
        """Gets the paid of this TransactionModel.  # noqa: E501

        If paid = 0: the transaction has not been fullfilled yet  # noqa: E501

        :return: The paid of this TransactionModel.  # noqa: E501
        :rtype: bool
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """Sets the paid of this TransactionModel.

        If paid = 0: the transaction has not been fullfilled yet  # noqa: E501

        :param paid: The paid of this TransactionModel.  # noqa: E501
        :type: bool
        """

        self._paid = paid

    @property
    def failed(self):
        """Gets the failed of this TransactionModel.  # noqa: E501

        if failed = 1: the transaction has failed  # noqa: E501

        :return: The failed of this TransactionModel.  # noqa: E501
        :rtype: bool
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this TransactionModel.

        if failed = 1: the transaction has failed  # noqa: E501

        :param failed: The failed of this TransactionModel.  # noqa: E501
        :type: bool
        """

        self._failed = failed

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
        if issubclass(TransactionModel, dict):
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
        if not isinstance(other, TransactionModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionModel):
            return True

        return self.to_dict() != other.to_dict()
