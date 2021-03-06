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


class PartyFiltersModel(object):
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
        'id': 'list[int]',
        'party_type_name': 'list[str]',
        'party_type_id': 'list[int]',
        'name_1': 'list[str]',
        'name_2': 'list[str]',
        'nr': 'list[str]',
        'contact_person': 'list[str]',
        'url': 'list[str]',
        'links': 'list[object]',
        'updated_at_since': 'datetime',
        'updated_at_till': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'party_type_name': 'party_type_name',
        'party_type_id': 'party_type_id',
        'name_1': 'name_1',
        'name_2': 'name_2',
        'nr': 'nr',
        'contact_person': 'contact_person',
        'url': 'url',
        'links': 'links',
        'updated_at_since': 'updated_at_since',
        'updated_at_till': 'updated_at_till'
    }

    def __init__(self, id=None, party_type_name=None, party_type_id=None, name_1=None, name_2=None, nr=None, contact_person=None, url=None, links=None, updated_at_since=None, updated_at_till=None, _configuration=None):  # noqa: E501
        """PartyFiltersModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._party_type_name = None
        self._party_type_id = None
        self._name_1 = None
        self._name_2 = None
        self._nr = None
        self._contact_person = None
        self._url = None
        self._links = None
        self._updated_at_since = None
        self._updated_at_till = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if party_type_name is not None:
            self.party_type_name = party_type_name
        if party_type_id is not None:
            self.party_type_id = party_type_id
        if name_1 is not None:
            self.name_1 = name_1
        if name_2 is not None:
            self.name_2 = name_2
        if nr is not None:
            self.nr = nr
        if contact_person is not None:
            self.contact_person = contact_person
        if url is not None:
            self.url = url
        if links is not None:
            self.links = links
        if updated_at_since is not None:
            self.updated_at_since = updated_at_since
        if updated_at_till is not None:
            self.updated_at_till = updated_at_till

    @property
    def id(self):
        """Gets the id of this PartyFiltersModel.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this PartyFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartyFiltersModel.

        Unique Identifier  # noqa: E501

        :param id: The id of this PartyFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._id = id

    @property
    def party_type_name(self):
        """Gets the party_type_name of this PartyFiltersModel.  # noqa: E501

        Type of this party  # noqa: E501

        :return: The party_type_name of this PartyFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._party_type_name

    @party_type_name.setter
    def party_type_name(self, party_type_name):
        """Sets the party_type_name of this PartyFiltersModel.

        Type of this party  # noqa: E501

        :param party_type_name: The party_type_name of this PartyFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._party_type_name = party_type_name

    @property
    def party_type_id(self):
        """Gets the party_type_id of this PartyFiltersModel.  # noqa: E501

        PartyTypeID of this party. 2 = contractor, 3 = booking  # noqa: E501

        :return: The party_type_id of this PartyFiltersModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._party_type_id

    @party_type_id.setter
    def party_type_id(self, party_type_id):
        """Sets the party_type_id of this PartyFiltersModel.

        PartyTypeID of this party. 2 = contractor, 3 = booking  # noqa: E501

        :param party_type_id: The party_type_id of this PartyFiltersModel.  # noqa: E501
        :type: list[int]
        """

        self._party_type_id = party_type_id

    @property
    def name_1(self):
        """Gets the name_1 of this PartyFiltersModel.  # noqa: E501

        Name 1 for party  # noqa: E501

        :return: The name_1 of this PartyFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._name_1

    @name_1.setter
    def name_1(self, name_1):
        """Sets the name_1 of this PartyFiltersModel.

        Name 1 for party  # noqa: E501

        :param name_1: The name_1 of this PartyFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._name_1 = name_1

    @property
    def name_2(self):
        """Gets the name_2 of this PartyFiltersModel.  # noqa: E501

        Name 2 for party  # noqa: E501

        :return: The name_2 of this PartyFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._name_2

    @name_2.setter
    def name_2(self, name_2):
        """Sets the name_2 of this PartyFiltersModel.

        Name 2 for party  # noqa: E501

        :param name_2: The name_2 of this PartyFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._name_2 = name_2

    @property
    def nr(self):
        """Gets the nr of this PartyFiltersModel.  # noqa: E501

        Number of this party  # noqa: E501

        :return: The nr of this PartyFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._nr

    @nr.setter
    def nr(self, nr):
        """Sets the nr of this PartyFiltersModel.

        Number of this party  # noqa: E501

        :param nr: The nr of this PartyFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._nr = nr

    @property
    def contact_person(self):
        """Gets the contact_person of this PartyFiltersModel.  # noqa: E501

        Contact person for party  # noqa: E501

        :return: The contact_person of this PartyFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this PartyFiltersModel.

        Contact person for party  # noqa: E501

        :param contact_person: The contact_person of this PartyFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._contact_person = contact_person

    @property
    def url(self):
        """Gets the url of this PartyFiltersModel.  # noqa: E501

        Url for party website  # noqa: E501

        :return: The url of this PartyFiltersModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PartyFiltersModel.

        Url for party website  # noqa: E501

        :param url: The url of this PartyFiltersModel.  # noqa: E501
        :type: list[str]
        """

        self._url = url

    @property
    def links(self):
        """Gets the links of this PartyFiltersModel.  # noqa: E501

        Activity Link ids  # noqa: E501

        :return: The links of this PartyFiltersModel.  # noqa: E501
        :rtype: list[object]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PartyFiltersModel.

        Activity Link ids  # noqa: E501

        :param links: The links of this PartyFiltersModel.  # noqa: E501
        :type: list[object]
        """

        self._links = links

    @property
    def updated_at_since(self):
        """Gets the updated_at_since of this PartyFiltersModel.  # noqa: E501

        Show updated since  # noqa: E501

        :return: The updated_at_since of this PartyFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_since

    @updated_at_since.setter
    def updated_at_since(self, updated_at_since):
        """Sets the updated_at_since of this PartyFiltersModel.

        Show updated since  # noqa: E501

        :param updated_at_since: The updated_at_since of this PartyFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_since = updated_at_since

    @property
    def updated_at_till(self):
        """Gets the updated_at_till of this PartyFiltersModel.  # noqa: E501

        Show updated till  # noqa: E501

        :return: The updated_at_till of this PartyFiltersModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_till

    @updated_at_till.setter
    def updated_at_till(self, updated_at_till):
        """Sets the updated_at_till of this PartyFiltersModel.

        Show updated till  # noqa: E501

        :param updated_at_till: The updated_at_till of this PartyFiltersModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at_till = updated_at_till

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
        if issubclass(PartyFiltersModel, dict):
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
        if not isinstance(other, PartyFiltersModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartyFiltersModel):
            return True

        return self.to_dict() != other.to_dict()
