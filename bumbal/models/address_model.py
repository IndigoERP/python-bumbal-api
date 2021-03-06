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


class AddressModel(object):
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
        'address_id': 'int',
        'party_id': 'int',
        'party_name': 'str',
        'code': 'str',
        'summary': 'str',
        'full_name': 'str',
        'name_1': 'str',
        'name_2': 'str',
        'street_1': 'str',
        'street_2': 'str',
        'full_addressline': 'str',
        'house_nr': 'str',
        'house_nr_addendum': 'str',
        'zipcode': 'str',
        'city': 'str',
        'state': 'str',
        'iso_country': 'str',
        'country_name': 'str',
        'time_from': 'str',
        'time_to': 'str',
        'duration': 'int',
        'address_type_names': 'list[str]',
        'emails': 'list[EmailModel]',
        'phone_nrs': 'list[PhoneNrModel]',
        'latitude': 'str',
        'longitude': 'str',
        'contact_person': 'str',
        'user_id': 'int',
        'links': 'list[LinkModel]',
        'meta_data': 'list[MetaDataModel]',
        'notes': 'list[NoteModel]',
        'files': 'list[FileModel]',
        'tag_names': 'list[str]',
        'tags': 'list[TagModel]'
    }

    attribute_map = {
        'id': 'id',
        'address_id': 'address_id',
        'party_id': 'party_id',
        'party_name': 'party_name',
        'code': 'code',
        'summary': 'summary',
        'full_name': 'full_name',
        'name_1': 'name_1',
        'name_2': 'name_2',
        'street_1': 'street_1',
        'street_2': 'street_2',
        'full_addressline': 'full_addressline',
        'house_nr': 'house_nr',
        'house_nr_addendum': 'house_nr_addendum',
        'zipcode': 'zipcode',
        'city': 'city',
        'state': 'state',
        'iso_country': 'iso_country',
        'country_name': 'country_name',
        'time_from': 'time_from',
        'time_to': 'time_to',
        'duration': 'duration',
        'address_type_names': 'address_type_names',
        'emails': 'emails',
        'phone_nrs': 'phone_nrs',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'contact_person': 'contact_person',
        'user_id': 'user_id',
        'links': 'links',
        'meta_data': 'meta_data',
        'notes': 'notes',
        'files': 'files',
        'tag_names': 'tag_names',
        'tags': 'tags'
    }

    def __init__(self, id=None, address_id=None, party_id=None, party_name=None, code=None, summary=None, full_name=None, name_1=None, name_2=None, street_1=None, street_2=None, full_addressline=None, house_nr=None, house_nr_addendum=None, zipcode=None, city=None, state=None, iso_country=None, country_name=None, time_from=None, time_to=None, duration=None, address_type_names=None, emails=None, phone_nrs=None, latitude=None, longitude=None, contact_person=None, user_id=None, links=None, meta_data=None, notes=None, files=None, tag_names=None, tags=None, _configuration=None):  # noqa: E501
        """AddressModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._address_id = None
        self._party_id = None
        self._party_name = None
        self._code = None
        self._summary = None
        self._full_name = None
        self._name_1 = None
        self._name_2 = None
        self._street_1 = None
        self._street_2 = None
        self._full_addressline = None
        self._house_nr = None
        self._house_nr_addendum = None
        self._zipcode = None
        self._city = None
        self._state = None
        self._iso_country = None
        self._country_name = None
        self._time_from = None
        self._time_to = None
        self._duration = None
        self._address_type_names = None
        self._emails = None
        self._phone_nrs = None
        self._latitude = None
        self._longitude = None
        self._contact_person = None
        self._user_id = None
        self._links = None
        self._meta_data = None
        self._notes = None
        self._files = None
        self._tag_names = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if address_id is not None:
            self.address_id = address_id
        if party_id is not None:
            self.party_id = party_id
        if party_name is not None:
            self.party_name = party_name
        if code is not None:
            self.code = code
        if summary is not None:
            self.summary = summary
        if full_name is not None:
            self.full_name = full_name
        if name_1 is not None:
            self.name_1 = name_1
        if name_2 is not None:
            self.name_2 = name_2
        if street_1 is not None:
            self.street_1 = street_1
        if street_2 is not None:
            self.street_2 = street_2
        if full_addressline is not None:
            self.full_addressline = full_addressline
        if house_nr is not None:
            self.house_nr = house_nr
        if house_nr_addendum is not None:
            self.house_nr_addendum = house_nr_addendum
        if zipcode is not None:
            self.zipcode = zipcode
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if iso_country is not None:
            self.iso_country = iso_country
        if country_name is not None:
            self.country_name = country_name
        if time_from is not None:
            self.time_from = time_from
        if time_to is not None:
            self.time_to = time_to
        if duration is not None:
            self.duration = duration
        if address_type_names is not None:
            self.address_type_names = address_type_names
        if emails is not None:
            self.emails = emails
        if phone_nrs is not None:
            self.phone_nrs = phone_nrs
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if contact_person is not None:
            self.contact_person = contact_person
        if user_id is not None:
            self.user_id = user_id
        if links is not None:
            self.links = links
        if meta_data is not None:
            self.meta_data = meta_data
        if notes is not None:
            self.notes = notes
        if files is not None:
            self.files = files
        if tag_names is not None:
            self.tag_names = tag_names
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The id of this AddressModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddressModel.

          # noqa: E501

        :param id: The id of this AddressModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def address_id(self):
        """Gets the address_id of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The address_id of this AddressModel.  # noqa: E501
        :rtype: int
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """Sets the address_id of this AddressModel.

          # noqa: E501

        :param address_id: The address_id of this AddressModel.  # noqa: E501
        :type: int
        """

        self._address_id = address_id

    @property
    def party_id(self):
        """Gets the party_id of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The party_id of this AddressModel.  # noqa: E501
        :rtype: int
        """
        return self._party_id

    @party_id.setter
    def party_id(self, party_id):
        """Sets the party_id of this AddressModel.

          # noqa: E501

        :param party_id: The party_id of this AddressModel.  # noqa: E501
        :type: int
        """

        self._party_id = party_id

    @property
    def party_name(self):
        """Gets the party_name of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The party_name of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._party_name

    @party_name.setter
    def party_name(self, party_name):
        """Sets the party_name of this AddressModel.

          # noqa: E501

        :param party_name: The party_name of this AddressModel.  # noqa: E501
        :type: str
        """

        self._party_name = party_name

    @property
    def code(self):
        """Gets the code of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The code of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AddressModel.

          # noqa: E501

        :param code: The code of this AddressModel.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def summary(self):
        """Gets the summary of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The summary of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this AddressModel.

          # noqa: E501

        :param summary: The summary of this AddressModel.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def full_name(self):
        """Gets the full_name of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The full_name of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this AddressModel.

          # noqa: E501

        :param full_name: The full_name of this AddressModel.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def name_1(self):
        """Gets the name_1 of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The name_1 of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._name_1

    @name_1.setter
    def name_1(self, name_1):
        """Sets the name_1 of this AddressModel.

          # noqa: E501

        :param name_1: The name_1 of this AddressModel.  # noqa: E501
        :type: str
        """

        self._name_1 = name_1

    @property
    def name_2(self):
        """Gets the name_2 of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The name_2 of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._name_2

    @name_2.setter
    def name_2(self, name_2):
        """Sets the name_2 of this AddressModel.

          # noqa: E501

        :param name_2: The name_2 of this AddressModel.  # noqa: E501
        :type: str
        """

        self._name_2 = name_2

    @property
    def street_1(self):
        """Gets the street_1 of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The street_1 of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._street_1

    @street_1.setter
    def street_1(self, street_1):
        """Sets the street_1 of this AddressModel.

          # noqa: E501

        :param street_1: The street_1 of this AddressModel.  # noqa: E501
        :type: str
        """

        self._street_1 = street_1

    @property
    def street_2(self):
        """Gets the street_2 of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The street_2 of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._street_2

    @street_2.setter
    def street_2(self, street_2):
        """Sets the street_2 of this AddressModel.

          # noqa: E501

        :param street_2: The street_2 of this AddressModel.  # noqa: E501
        :type: str
        """

        self._street_2 = street_2

    @property
    def full_addressline(self):
        """Gets the full_addressline of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The full_addressline of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._full_addressline

    @full_addressline.setter
    def full_addressline(self, full_addressline):
        """Sets the full_addressline of this AddressModel.

          # noqa: E501

        :param full_addressline: The full_addressline of this AddressModel.  # noqa: E501
        :type: str
        """

        self._full_addressline = full_addressline

    @property
    def house_nr(self):
        """Gets the house_nr of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The house_nr of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._house_nr

    @house_nr.setter
    def house_nr(self, house_nr):
        """Sets the house_nr of this AddressModel.

          # noqa: E501

        :param house_nr: The house_nr of this AddressModel.  # noqa: E501
        :type: str
        """

        self._house_nr = house_nr

    @property
    def house_nr_addendum(self):
        """Gets the house_nr_addendum of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The house_nr_addendum of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._house_nr_addendum

    @house_nr_addendum.setter
    def house_nr_addendum(self, house_nr_addendum):
        """Sets the house_nr_addendum of this AddressModel.

          # noqa: E501

        :param house_nr_addendum: The house_nr_addendum of this AddressModel.  # noqa: E501
        :type: str
        """

        self._house_nr_addendum = house_nr_addendum

    @property
    def zipcode(self):
        """Gets the zipcode of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The zipcode of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this AddressModel.

          # noqa: E501

        :param zipcode: The zipcode of this AddressModel.  # noqa: E501
        :type: str
        """

        self._zipcode = zipcode

    @property
    def city(self):
        """Gets the city of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The city of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this AddressModel.

          # noqa: E501

        :param city: The city of this AddressModel.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The state of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AddressModel.

          # noqa: E501

        :param state: The state of this AddressModel.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def iso_country(self):
        """Gets the iso_country of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The iso_country of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._iso_country

    @iso_country.setter
    def iso_country(self, iso_country):
        """Sets the iso_country of this AddressModel.

          # noqa: E501

        :param iso_country: The iso_country of this AddressModel.  # noqa: E501
        :type: str
        """

        self._iso_country = iso_country

    @property
    def country_name(self):
        """Gets the country_name of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The country_name of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this AddressModel.

          # noqa: E501

        :param country_name: The country_name of this AddressModel.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    @property
    def time_from(self):
        """Gets the time_from of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The time_from of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._time_from

    @time_from.setter
    def time_from(self, time_from):
        """Sets the time_from of this AddressModel.

          # noqa: E501

        :param time_from: The time_from of this AddressModel.  # noqa: E501
        :type: str
        """

        self._time_from = time_from

    @property
    def time_to(self):
        """Gets the time_to of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The time_to of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._time_to

    @time_to.setter
    def time_to(self, time_to):
        """Sets the time_to of this AddressModel.

          # noqa: E501

        :param time_to: The time_to of this AddressModel.  # noqa: E501
        :type: str
        """

        self._time_to = time_to

    @property
    def duration(self):
        """Gets the duration of this AddressModel.  # noqa: E501

        Default duration for activities on this address in minutes  # noqa: E501

        :return: The duration of this AddressModel.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AddressModel.

        Default duration for activities on this address in minutes  # noqa: E501

        :param duration: The duration of this AddressModel.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def address_type_names(self):
        """Gets the address_type_names of this AddressModel.  # noqa: E501

        Address Type names  # noqa: E501

        :return: The address_type_names of this AddressModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._address_type_names

    @address_type_names.setter
    def address_type_names(self, address_type_names):
        """Sets the address_type_names of this AddressModel.

        Address Type names  # noqa: E501

        :param address_type_names: The address_type_names of this AddressModel.  # noqa: E501
        :type: list[str]
        """

        self._address_type_names = address_type_names

    @property
    def emails(self):
        """Gets the emails of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The emails of this AddressModel.  # noqa: E501
        :rtype: list[EmailModel]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this AddressModel.

          # noqa: E501

        :param emails: The emails of this AddressModel.  # noqa: E501
        :type: list[EmailModel]
        """

        self._emails = emails

    @property
    def phone_nrs(self):
        """Gets the phone_nrs of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The phone_nrs of this AddressModel.  # noqa: E501
        :rtype: list[PhoneNrModel]
        """
        return self._phone_nrs

    @phone_nrs.setter
    def phone_nrs(self, phone_nrs):
        """Sets the phone_nrs of this AddressModel.

          # noqa: E501

        :param phone_nrs: The phone_nrs of this AddressModel.  # noqa: E501
        :type: list[PhoneNrModel]
        """

        self._phone_nrs = phone_nrs

    @property
    def latitude(self):
        """Gets the latitude of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The latitude of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this AddressModel.

          # noqa: E501

        :param latitude: The latitude of this AddressModel.  # noqa: E501
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The longitude of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this AddressModel.

          # noqa: E501

        :param longitude: The longitude of this AddressModel.  # noqa: E501
        :type: str
        """

        self._longitude = longitude

    @property
    def contact_person(self):
        """Gets the contact_person of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The contact_person of this AddressModel.  # noqa: E501
        :rtype: str
        """
        return self._contact_person

    @contact_person.setter
    def contact_person(self, contact_person):
        """Sets the contact_person of this AddressModel.

          # noqa: E501

        :param contact_person: The contact_person of this AddressModel.  # noqa: E501
        :type: str
        """

        self._contact_person = contact_person

    @property
    def user_id(self):
        """Gets the user_id of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The user_id of this AddressModel.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AddressModel.

          # noqa: E501

        :param user_id: The user_id of this AddressModel.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def links(self):
        """Gets the links of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The links of this AddressModel.  # noqa: E501
        :rtype: list[LinkModel]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AddressModel.

          # noqa: E501

        :param links: The links of this AddressModel.  # noqa: E501
        :type: list[LinkModel]
        """

        self._links = links

    @property
    def meta_data(self):
        """Gets the meta_data of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The meta_data of this AddressModel.  # noqa: E501
        :rtype: list[MetaDataModel]
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this AddressModel.

          # noqa: E501

        :param meta_data: The meta_data of this AddressModel.  # noqa: E501
        :type: list[MetaDataModel]
        """

        self._meta_data = meta_data

    @property
    def notes(self):
        """Gets the notes of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The notes of this AddressModel.  # noqa: E501
        :rtype: list[NoteModel]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this AddressModel.

          # noqa: E501

        :param notes: The notes of this AddressModel.  # noqa: E501
        :type: list[NoteModel]
        """

        self._notes = notes

    @property
    def files(self):
        """Gets the files of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The files of this AddressModel.  # noqa: E501
        :rtype: list[FileModel]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this AddressModel.

          # noqa: E501

        :param files: The files of this AddressModel.  # noqa: E501
        :type: list[FileModel]
        """

        self._files = files

    @property
    def tag_names(self):
        """Gets the tag_names of this AddressModel.  # noqa: E501

        Tag names  # noqa: E501

        :return: The tag_names of this AddressModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        """Sets the tag_names of this AddressModel.

        Tag names  # noqa: E501

        :param tag_names: The tag_names of this AddressModel.  # noqa: E501
        :type: list[str]
        """

        self._tag_names = tag_names

    @property
    def tags(self):
        """Gets the tags of this AddressModel.  # noqa: E501

          # noqa: E501

        :return: The tags of this AddressModel.  # noqa: E501
        :rtype: list[TagModel]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AddressModel.

          # noqa: E501

        :param tags: The tags of this AddressModel.  # noqa: E501
        :type: list[TagModel]
        """

        self._tags = tags

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
        if issubclass(AddressModel, dict):
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
        if not isinstance(other, AddressModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddressModel):
            return True

        return self.to_dict() != other.to_dict()
