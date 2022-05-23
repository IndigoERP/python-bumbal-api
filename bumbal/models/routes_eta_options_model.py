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


class RoutesEtaOptionsModel(object):
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
        'include_address': 'bool',
        'include_address_object': 'bool',
        'include_route_status': 'bool',
        'include_route_tags': 'bool',
        'include_tags': 'bool',
        'include_tag_names': 'bool',
        'include_driver': 'bool',
        'include_driver_links': 'bool',
        'include_car': 'bool',
        'include_car_links': 'bool',
        'include_vehicle': 'bool',
        'include_vehicle_links': 'bool',
        'include_trailer': 'bool',
        'include_trailer_links': 'bool',
        'include_driver_info': 'bool',
        'include_equipment_info_car': 'bool',
        'include_equipment': 'bool',
        'include_gps_locations': 'bool',
        'include_pause': 'bool',
        'include_activity_ids': 'bool',
        'include_latest_position': 'bool',
        'include_zones': 'bool',
        'include_zone_names': 'bool',
        'include_notes': 'bool',
        'include_meta_data': 'bool'
    }

    attribute_map = {
        'include_address': 'include_address',
        'include_address_object': 'include_address_object',
        'include_route_status': 'include_route_status',
        'include_route_tags': 'include_route_tags',
        'include_tags': 'include_tags',
        'include_tag_names': 'include_tag_names',
        'include_driver': 'include_driver',
        'include_driver_links': 'include_driver_links',
        'include_car': 'include_car',
        'include_car_links': 'include_car_links',
        'include_vehicle': 'include_vehicle',
        'include_vehicle_links': 'include_vehicle_links',
        'include_trailer': 'include_trailer',
        'include_trailer_links': 'include_trailer_links',
        'include_driver_info': 'include_driver_info',
        'include_equipment_info_car': 'include_equipment_info_car',
        'include_equipment': 'include_equipment',
        'include_gps_locations': 'include_gps_locations',
        'include_pause': 'include_pause',
        'include_activity_ids': 'include_activity_ids',
        'include_latest_position': 'include_latest_position',
        'include_zones': 'include_zones',
        'include_zone_names': 'include_zone_names',
        'include_notes': 'include_notes',
        'include_meta_data': 'include_meta_data'
    }

    def __init__(self, include_address=None, include_address_object=None, include_route_status=None, include_route_tags=None, include_tags=None, include_tag_names=None, include_driver=None, include_driver_links=None, include_car=None, include_car_links=None, include_vehicle=None, include_vehicle_links=None, include_trailer=None, include_trailer_links=None, include_driver_info=None, include_equipment_info_car=None, include_equipment=None, include_gps_locations=None, include_pause=None, include_activity_ids=None, include_latest_position=None, include_zones=None, include_zone_names=None, include_notes=None, include_meta_data=None, _configuration=None):  # noqa: E501
        """RoutesEtaOptionsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._include_address = None
        self._include_address_object = None
        self._include_route_status = None
        self._include_route_tags = None
        self._include_tags = None
        self._include_tag_names = None
        self._include_driver = None
        self._include_driver_links = None
        self._include_car = None
        self._include_car_links = None
        self._include_vehicle = None
        self._include_vehicle_links = None
        self._include_trailer = None
        self._include_trailer_links = None
        self._include_driver_info = None
        self._include_equipment_info_car = None
        self._include_equipment = None
        self._include_gps_locations = None
        self._include_pause = None
        self._include_activity_ids = None
        self._include_latest_position = None
        self._include_zones = None
        self._include_zone_names = None
        self._include_notes = None
        self._include_meta_data = None
        self.discriminator = None

        if include_address is not None:
            self.include_address = include_address
        if include_address_object is not None:
            self.include_address_object = include_address_object
        if include_route_status is not None:
            self.include_route_status = include_route_status
        if include_route_tags is not None:
            self.include_route_tags = include_route_tags
        if include_tags is not None:
            self.include_tags = include_tags
        if include_tag_names is not None:
            self.include_tag_names = include_tag_names
        if include_driver is not None:
            self.include_driver = include_driver
        if include_driver_links is not None:
            self.include_driver_links = include_driver_links
        if include_car is not None:
            self.include_car = include_car
        if include_car_links is not None:
            self.include_car_links = include_car_links
        if include_vehicle is not None:
            self.include_vehicle = include_vehicle
        if include_vehicle_links is not None:
            self.include_vehicle_links = include_vehicle_links
        if include_trailer is not None:
            self.include_trailer = include_trailer
        if include_trailer_links is not None:
            self.include_trailer_links = include_trailer_links
        if include_driver_info is not None:
            self.include_driver_info = include_driver_info
        if include_equipment_info_car is not None:
            self.include_equipment_info_car = include_equipment_info_car
        if include_equipment is not None:
            self.include_equipment = include_equipment
        if include_gps_locations is not None:
            self.include_gps_locations = include_gps_locations
        if include_pause is not None:
            self.include_pause = include_pause
        if include_activity_ids is not None:
            self.include_activity_ids = include_activity_ids
        if include_latest_position is not None:
            self.include_latest_position = include_latest_position
        if include_zones is not None:
            self.include_zones = include_zones
        if include_zone_names is not None:
            self.include_zone_names = include_zone_names
        if include_notes is not None:
            self.include_notes = include_notes
        if include_meta_data is not None:
            self.include_meta_data = include_meta_data

    @property
    def include_address(self):
        """Gets the include_address of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_address of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_address

    @include_address.setter
    def include_address(self, include_address):
        """Sets the include_address of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_address: The include_address of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_address = include_address

    @property
    def include_address_object(self):
        """Gets the include_address_object of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_address_object of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_address_object

    @include_address_object.setter
    def include_address_object(self, include_address_object):
        """Sets the include_address_object of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_address_object: The include_address_object of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_address_object = include_address_object

    @property
    def include_route_status(self):
        """Gets the include_route_status of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_route_status of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_route_status

    @include_route_status.setter
    def include_route_status(self, include_route_status):
        """Sets the include_route_status of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_route_status: The include_route_status of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_route_status = include_route_status

    @property
    def include_route_tags(self):
        """Gets the include_route_tags of this RoutesEtaOptionsModel.  # noqa: E501

        Deprecated! use include_tags  # noqa: E501

        :return: The include_route_tags of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_route_tags

    @include_route_tags.setter
    def include_route_tags(self, include_route_tags):
        """Sets the include_route_tags of this RoutesEtaOptionsModel.

        Deprecated! use include_tags  # noqa: E501

        :param include_route_tags: The include_route_tags of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_route_tags = include_route_tags

    @property
    def include_tags(self):
        """Gets the include_tags of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_tags of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_tags

    @include_tags.setter
    def include_tags(self, include_tags):
        """Sets the include_tags of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_tags: The include_tags of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_tags = include_tags

    @property
    def include_tag_names(self):
        """Gets the include_tag_names of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_tag_names of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_tag_names

    @include_tag_names.setter
    def include_tag_names(self, include_tag_names):
        """Sets the include_tag_names of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_tag_names: The include_tag_names of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_tag_names = include_tag_names

    @property
    def include_driver(self):
        """Gets the include_driver of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_driver of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_driver

    @include_driver.setter
    def include_driver(self, include_driver):
        """Sets the include_driver of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_driver: The include_driver of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_driver = include_driver

    @property
    def include_driver_links(self):
        """Gets the include_driver_links of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_driver_links of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_driver_links

    @include_driver_links.setter
    def include_driver_links(self, include_driver_links):
        """Sets the include_driver_links of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_driver_links: The include_driver_links of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_driver_links = include_driver_links

    @property
    def include_car(self):
        """Gets the include_car of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_car of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_car

    @include_car.setter
    def include_car(self, include_car):
        """Sets the include_car of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_car: The include_car of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_car = include_car

    @property
    def include_car_links(self):
        """Gets the include_car_links of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_car_links of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_car_links

    @include_car_links.setter
    def include_car_links(self, include_car_links):
        """Sets the include_car_links of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_car_links: The include_car_links of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_car_links = include_car_links

    @property
    def include_vehicle(self):
        """Gets the include_vehicle of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_vehicle of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_vehicle

    @include_vehicle.setter
    def include_vehicle(self, include_vehicle):
        """Sets the include_vehicle of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_vehicle: The include_vehicle of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_vehicle = include_vehicle

    @property
    def include_vehicle_links(self):
        """Gets the include_vehicle_links of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_vehicle_links of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_vehicle_links

    @include_vehicle_links.setter
    def include_vehicle_links(self, include_vehicle_links):
        """Sets the include_vehicle_links of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_vehicle_links: The include_vehicle_links of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_vehicle_links = include_vehicle_links

    @property
    def include_trailer(self):
        """Gets the include_trailer of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_trailer of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_trailer

    @include_trailer.setter
    def include_trailer(self, include_trailer):
        """Sets the include_trailer of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_trailer: The include_trailer of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_trailer = include_trailer

    @property
    def include_trailer_links(self):
        """Gets the include_trailer_links of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_trailer_links of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_trailer_links

    @include_trailer_links.setter
    def include_trailer_links(self, include_trailer_links):
        """Sets the include_trailer_links of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_trailer_links: The include_trailer_links of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_trailer_links = include_trailer_links

    @property
    def include_driver_info(self):
        """Gets the include_driver_info of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_driver_info of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_driver_info

    @include_driver_info.setter
    def include_driver_info(self, include_driver_info):
        """Sets the include_driver_info of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_driver_info: The include_driver_info of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_driver_info = include_driver_info

    @property
    def include_equipment_info_car(self):
        """Gets the include_equipment_info_car of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_equipment_info_car of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_equipment_info_car

    @include_equipment_info_car.setter
    def include_equipment_info_car(self, include_equipment_info_car):
        """Sets the include_equipment_info_car of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_equipment_info_car: The include_equipment_info_car of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_equipment_info_car = include_equipment_info_car

    @property
    def include_equipment(self):
        """Gets the include_equipment of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_equipment of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_equipment

    @include_equipment.setter
    def include_equipment(self, include_equipment):
        """Sets the include_equipment of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_equipment: The include_equipment of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_equipment = include_equipment

    @property
    def include_gps_locations(self):
        """Gets the include_gps_locations of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_gps_locations of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_gps_locations

    @include_gps_locations.setter
    def include_gps_locations(self, include_gps_locations):
        """Sets the include_gps_locations of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_gps_locations: The include_gps_locations of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_gps_locations = include_gps_locations

    @property
    def include_pause(self):
        """Gets the include_pause of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_pause of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_pause

    @include_pause.setter
    def include_pause(self, include_pause):
        """Sets the include_pause of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_pause: The include_pause of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_pause = include_pause

    @property
    def include_activity_ids(self):
        """Gets the include_activity_ids of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_activity_ids of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_activity_ids

    @include_activity_ids.setter
    def include_activity_ids(self, include_activity_ids):
        """Sets the include_activity_ids of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_activity_ids: The include_activity_ids of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_activity_ids = include_activity_ids

    @property
    def include_latest_position(self):
        """Gets the include_latest_position of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_latest_position of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_latest_position

    @include_latest_position.setter
    def include_latest_position(self, include_latest_position):
        """Sets the include_latest_position of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_latest_position: The include_latest_position of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_latest_position = include_latest_position

    @property
    def include_zones(self):
        """Gets the include_zones of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_zones of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_zones

    @include_zones.setter
    def include_zones(self, include_zones):
        """Sets the include_zones of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_zones: The include_zones of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_zones = include_zones

    @property
    def include_zone_names(self):
        """Gets the include_zone_names of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_zone_names of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_zone_names

    @include_zone_names.setter
    def include_zone_names(self, include_zone_names):
        """Sets the include_zone_names of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_zone_names: The include_zone_names of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_zone_names = include_zone_names

    @property
    def include_notes(self):
        """Gets the include_notes of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_notes of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_notes

    @include_notes.setter
    def include_notes(self, include_notes):
        """Sets the include_notes of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_notes: The include_notes of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_notes = include_notes

    @property
    def include_meta_data(self):
        """Gets the include_meta_data of this RoutesEtaOptionsModel.  # noqa: E501

          # noqa: E501

        :return: The include_meta_data of this RoutesEtaOptionsModel.  # noqa: E501
        :rtype: bool
        """
        return self._include_meta_data

    @include_meta_data.setter
    def include_meta_data(self, include_meta_data):
        """Sets the include_meta_data of this RoutesEtaOptionsModel.

          # noqa: E501

        :param include_meta_data: The include_meta_data of this RoutesEtaOptionsModel.  # noqa: E501
        :type: bool
        """

        self._include_meta_data = include_meta_data

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
        if issubclass(RoutesEtaOptionsModel, dict):
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
        if not isinstance(other, RoutesEtaOptionsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoutesEtaOptionsModel):
            return True

        return self.to_dict() != other.to_dict()
