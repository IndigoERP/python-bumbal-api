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


class CommunicationModel(object):
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
        'saywhen': 'bool',
        'bumbal': 'bool',
        'send_invite': 'bool',
        'send_reminder': 'bool',
        'send_pref_confirmation': 'bool',
        'send_planned': 'bool',
        'send_eta': 'bool',
        'send_executed': 'bool',
        'send_cancelled': 'bool',
        'email': 'str',
        'phone_nr': 'str',
        'saywhen_status_id': 'int',
        'saywhen_status_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'saywhen': 'saywhen',
        'bumbal': 'bumbal',
        'send_invite': 'send_invite',
        'send_reminder': 'send_reminder',
        'send_pref_confirmation': 'send_pref_confirmation',
        'send_planned': 'send_planned',
        'send_eta': 'send_eta',
        'send_executed': 'send_executed',
        'send_cancelled': 'send_cancelled',
        'email': 'email',
        'phone_nr': 'phone_nr',
        'saywhen_status_id': 'saywhen_status_id',
        'saywhen_status_name': 'saywhen_status_name'
    }

    def __init__(self, id=None, saywhen=None, bumbal=None, send_invite=None, send_reminder=None, send_pref_confirmation=None, send_planned=None, send_eta=None, send_executed=None, send_cancelled=None, email=None, phone_nr=None, saywhen_status_id=None, saywhen_status_name=None, _configuration=None):  # noqa: E501
        """CommunicationModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._saywhen = None
        self._bumbal = None
        self._send_invite = None
        self._send_reminder = None
        self._send_pref_confirmation = None
        self._send_planned = None
        self._send_eta = None
        self._send_executed = None
        self._send_cancelled = None
        self._email = None
        self._phone_nr = None
        self._saywhen_status_id = None
        self._saywhen_status_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if saywhen is not None:
            self.saywhen = saywhen
        if bumbal is not None:
            self.bumbal = bumbal
        if send_invite is not None:
            self.send_invite = send_invite
        if send_reminder is not None:
            self.send_reminder = send_reminder
        if send_pref_confirmation is not None:
            self.send_pref_confirmation = send_pref_confirmation
        if send_planned is not None:
            self.send_planned = send_planned
        if send_eta is not None:
            self.send_eta = send_eta
        if send_executed is not None:
            self.send_executed = send_executed
        if send_cancelled is not None:
            self.send_cancelled = send_cancelled
        if email is not None:
            self.email = email
        if phone_nr is not None:
            self.phone_nr = phone_nr
        if saywhen_status_id is not None:
            self.saywhen_status_id = saywhen_status_id
        if saywhen_status_name is not None:
            self.saywhen_status_name = saywhen_status_name

    @property
    def id(self):
        """Gets the id of this CommunicationModel.  # noqa: E501

          # noqa: E501

        :return: The id of this CommunicationModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommunicationModel.

          # noqa: E501

        :param id: The id of this CommunicationModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def saywhen(self):
        """Gets the saywhen of this CommunicationModel.  # noqa: E501

        Whether or not activity should be synced with Saywhen  # noqa: E501

        :return: The saywhen of this CommunicationModel.  # noqa: E501
        :rtype: bool
        """
        return self._saywhen

    @saywhen.setter
    def saywhen(self, saywhen):
        """Sets the saywhen of this CommunicationModel.

        Whether or not activity should be synced with Saywhen  # noqa: E501

        :param saywhen: The saywhen of this CommunicationModel.  # noqa: E501
        :type: bool
        """

        self._saywhen = saywhen

    @property
    def bumbal(self):
        """Gets the bumbal of this CommunicationModel.  # noqa: E501

        Whether or not activity is handled by Bumbal Communication Server  # noqa: E501

        :return: The bumbal of this CommunicationModel.  # noqa: E501
        :rtype: bool
        """
        return self._bumbal

    @bumbal.setter
    def bumbal(self, bumbal):
        """Sets the bumbal of this CommunicationModel.

        Whether or not activity is handled by Bumbal Communication Server  # noqa: E501

        :param bumbal: The bumbal of this CommunicationModel.  # noqa: E501
        :type: bool
        """

        self._bumbal = bumbal

    @property
    def send_invite(self):
        """Gets the send_invite of this CommunicationModel.  # noqa: E501

        Send invite  # noqa: E501

        :return: The send_invite of this CommunicationModel.  # noqa: E501
        :rtype: bool
        """
        return self._send_invite

    @send_invite.setter
    def send_invite(self, send_invite):
        """Sets the send_invite of this CommunicationModel.

        Send invite  # noqa: E501

        :param send_invite: The send_invite of this CommunicationModel.  # noqa: E501
        :type: bool
        """

        self._send_invite = send_invite

    @property
    def send_reminder(self):
        """Gets the send_reminder of this CommunicationModel.  # noqa: E501

        Send reminder  # noqa: E501

        :return: The send_reminder of this CommunicationModel.  # noqa: E501
        :rtype: bool
        """
        return self._send_reminder

    @send_reminder.setter
    def send_reminder(self, send_reminder):
        """Sets the send_reminder of this CommunicationModel.

        Send reminder  # noqa: E501

        :param send_reminder: The send_reminder of this CommunicationModel.  # noqa: E501
        :type: bool
        """

        self._send_reminder = send_reminder

    @property
    def send_pref_confirmation(self):
        """Gets the send_pref_confirmation of this CommunicationModel.  # noqa: E501

        Send confirmation on preferences received  # noqa: E501

        :return: The send_pref_confirmation of this CommunicationModel.  # noqa: E501
        :rtype: bool
        """
        return self._send_pref_confirmation

    @send_pref_confirmation.setter
    def send_pref_confirmation(self, send_pref_confirmation):
        """Sets the send_pref_confirmation of this CommunicationModel.

        Send confirmation on preferences received  # noqa: E501

        :param send_pref_confirmation: The send_pref_confirmation of this CommunicationModel.  # noqa: E501
        :type: bool
        """

        self._send_pref_confirmation = send_pref_confirmation

    @property
    def send_planned(self):
        """Gets the send_planned of this CommunicationModel.  # noqa: E501

        Send planned notice  # noqa: E501

        :return: The send_planned of this CommunicationModel.  # noqa: E501
        :rtype: bool
        """
        return self._send_planned

    @send_planned.setter
    def send_planned(self, send_planned):
        """Sets the send_planned of this CommunicationModel.

        Send planned notice  # noqa: E501

        :param send_planned: The send_planned of this CommunicationModel.  # noqa: E501
        :type: bool
        """

        self._send_planned = send_planned

    @property
    def send_eta(self):
        """Gets the send_eta of this CommunicationModel.  # noqa: E501

        Send eta notice  # noqa: E501

        :return: The send_eta of this CommunicationModel.  # noqa: E501
        :rtype: bool
        """
        return self._send_eta

    @send_eta.setter
    def send_eta(self, send_eta):
        """Sets the send_eta of this CommunicationModel.

        Send eta notice  # noqa: E501

        :param send_eta: The send_eta of this CommunicationModel.  # noqa: E501
        :type: bool
        """

        self._send_eta = send_eta

    @property
    def send_executed(self):
        """Gets the send_executed of this CommunicationModel.  # noqa: E501

        Send executed notice  # noqa: E501

        :return: The send_executed of this CommunicationModel.  # noqa: E501
        :rtype: bool
        """
        return self._send_executed

    @send_executed.setter
    def send_executed(self, send_executed):
        """Sets the send_executed of this CommunicationModel.

        Send executed notice  # noqa: E501

        :param send_executed: The send_executed of this CommunicationModel.  # noqa: E501
        :type: bool
        """

        self._send_executed = send_executed

    @property
    def send_cancelled(self):
        """Gets the send_cancelled of this CommunicationModel.  # noqa: E501

        Send cancelled notice  # noqa: E501

        :return: The send_cancelled of this CommunicationModel.  # noqa: E501
        :rtype: bool
        """
        return self._send_cancelled

    @send_cancelled.setter
    def send_cancelled(self, send_cancelled):
        """Sets the send_cancelled of this CommunicationModel.

        Send cancelled notice  # noqa: E501

        :param send_cancelled: The send_cancelled of this CommunicationModel.  # noqa: E501
        :type: bool
        """

        self._send_cancelled = send_cancelled

    @property
    def email(self):
        """Gets the email of this CommunicationModel.  # noqa: E501

        Email for customer communication  # noqa: E501

        :return: The email of this CommunicationModel.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CommunicationModel.

        Email for customer communication  # noqa: E501

        :param email: The email of this CommunicationModel.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone_nr(self):
        """Gets the phone_nr of this CommunicationModel.  # noqa: E501

        Phone nr for customer communication  # noqa: E501

        :return: The phone_nr of this CommunicationModel.  # noqa: E501
        :rtype: str
        """
        return self._phone_nr

    @phone_nr.setter
    def phone_nr(self, phone_nr):
        """Sets the phone_nr of this CommunicationModel.

        Phone nr for customer communication  # noqa: E501

        :param phone_nr: The phone_nr of this CommunicationModel.  # noqa: E501
        :type: str
        """

        self._phone_nr = phone_nr

    @property
    def saywhen_status_id(self):
        """Gets the saywhen_status_id of this CommunicationModel.  # noqa: E501

        Saywhen StatusId of this Activity, 1:cancelled, 2:offered, 3:preffed, 4:confirmed, 5:accepted, 6:planned, 7:scheduled, 8:started, 9:completed  # noqa: E501

        :return: The saywhen_status_id of this CommunicationModel.  # noqa: E501
        :rtype: int
        """
        return self._saywhen_status_id

    @saywhen_status_id.setter
    def saywhen_status_id(self, saywhen_status_id):
        """Sets the saywhen_status_id of this CommunicationModel.

        Saywhen StatusId of this Activity, 1:cancelled, 2:offered, 3:preffed, 4:confirmed, 5:accepted, 6:planned, 7:scheduled, 8:started, 9:completed  # noqa: E501

        :param saywhen_status_id: The saywhen_status_id of this CommunicationModel.  # noqa: E501
        :type: int
        """

        self._saywhen_status_id = saywhen_status_id

    @property
    def saywhen_status_name(self):
        """Gets the saywhen_status_name of this CommunicationModel.  # noqa: E501

        Saywhen Status name  # noqa: E501

        :return: The saywhen_status_name of this CommunicationModel.  # noqa: E501
        :rtype: str
        """
        return self._saywhen_status_name

    @saywhen_status_name.setter
    def saywhen_status_name(self, saywhen_status_name):
        """Sets the saywhen_status_name of this CommunicationModel.

        Saywhen Status name  # noqa: E501

        :param saywhen_status_name: The saywhen_status_name of this CommunicationModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["cancelled", "offered", "preffed", "confirmed", "accepted", "planned", "scheduled", "started", "completed"]  # noqa: E501
        if (self._configuration.client_side_validation and
                saywhen_status_name not in allowed_values):
            raise ValueError(
                "Invalid value for `saywhen_status_name` ({0}), must be one of {1}"  # noqa: E501
                .format(saywhen_status_name, allowed_values)
            )

        self._saywhen_status_name = saywhen_status_name

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
        if issubclass(CommunicationModel, dict):
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
        if not isinstance(other, CommunicationModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommunicationModel):
            return True

        return self.to_dict() != other.to_dict()
