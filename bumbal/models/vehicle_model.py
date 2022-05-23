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


class VehicleModel(object):
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
        'vehicle_type_id': 'int',
        'vehicle_type_name': 'str',
        'name': 'str',
        'registration_nr': 'str',
        'max_speed': 'int',
        'speed_factor': 'float',
        'start_duration': 'int',
        'end_duration': 'int',
        'duration_factor': 'float',
        'cost_per_meter': 'float',
        'cost_per_route': 'float',
        'cost_per_driving_minute': 'float',
        'cost_per_waiting_minute': 'float',
        'cost_per_service_minute': 'float',
        'applied_capacities': 'object',
        'capacities': 'list[CapacityModel]',
        'tags': 'list[TagModel]',
        'meta_data': 'list[MetaDataModel]',
        'links': 'list[LinkModel]',
        'files': 'list[FileModel]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'updated_by_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'vehicle_type_id': 'vehicle_type_id',
        'vehicle_type_name': 'vehicle_type_name',
        'name': 'name',
        'registration_nr': 'registration_nr',
        'max_speed': 'max_speed',
        'speed_factor': 'speed_factor',
        'start_duration': 'start_duration',
        'end_duration': 'end_duration',
        'duration_factor': 'duration_factor',
        'cost_per_meter': 'cost_per_meter',
        'cost_per_route': 'cost_per_route',
        'cost_per_driving_minute': 'cost_per_driving_minute',
        'cost_per_waiting_minute': 'cost_per_waiting_minute',
        'cost_per_service_minute': 'cost_per_service_minute',
        'applied_capacities': 'applied_capacities',
        'capacities': 'capacities',
        'tags': 'tags',
        'meta_data': 'meta_data',
        'links': 'links',
        'files': 'files',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'updated_by_name': 'updated_by_name'
    }

    def __init__(self, id=None, vehicle_type_id=None, vehicle_type_name=None, name=None, registration_nr=None, max_speed=None, speed_factor=None, start_duration=None, end_duration=None, duration_factor=None, cost_per_meter=None, cost_per_route=None, cost_per_driving_minute=None, cost_per_waiting_minute=None, cost_per_service_minute=None, applied_capacities=None, capacities=None, tags=None, meta_data=None, links=None, files=None, created_at=None, updated_at=None, updated_by_name=None, _configuration=None):  # noqa: E501
        """VehicleModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._vehicle_type_id = None
        self._vehicle_type_name = None
        self._name = None
        self._registration_nr = None
        self._max_speed = None
        self._speed_factor = None
        self._start_duration = None
        self._end_duration = None
        self._duration_factor = None
        self._cost_per_meter = None
        self._cost_per_route = None
        self._cost_per_driving_minute = None
        self._cost_per_waiting_minute = None
        self._cost_per_service_minute = None
        self._applied_capacities = None
        self._capacities = None
        self._tags = None
        self._meta_data = None
        self._links = None
        self._files = None
        self._created_at = None
        self._updated_at = None
        self._updated_by_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vehicle_type_id is not None:
            self.vehicle_type_id = vehicle_type_id
        if vehicle_type_name is not None:
            self.vehicle_type_name = vehicle_type_name
        if name is not None:
            self.name = name
        if registration_nr is not None:
            self.registration_nr = registration_nr
        if max_speed is not None:
            self.max_speed = max_speed
        if speed_factor is not None:
            self.speed_factor = speed_factor
        if start_duration is not None:
            self.start_duration = start_duration
        if end_duration is not None:
            self.end_duration = end_duration
        if duration_factor is not None:
            self.duration_factor = duration_factor
        if cost_per_meter is not None:
            self.cost_per_meter = cost_per_meter
        if cost_per_route is not None:
            self.cost_per_route = cost_per_route
        if cost_per_driving_minute is not None:
            self.cost_per_driving_minute = cost_per_driving_minute
        if cost_per_waiting_minute is not None:
            self.cost_per_waiting_minute = cost_per_waiting_minute
        if cost_per_service_minute is not None:
            self.cost_per_service_minute = cost_per_service_minute
        if applied_capacities is not None:
            self.applied_capacities = applied_capacities
        if capacities is not None:
            self.capacities = capacities
        if tags is not None:
            self.tags = tags
        if meta_data is not None:
            self.meta_data = meta_data
        if links is not None:
            self.links = links
        if files is not None:
            self.files = files
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by_name is not None:
            self.updated_by_name = updated_by_name

    @property
    def id(self):
        """Gets the id of this VehicleModel.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this VehicleModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VehicleModel.

        Unique Identifier  # noqa: E501

        :param id: The id of this VehicleModel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def vehicle_type_id(self):
        """Gets the vehicle_type_id of this VehicleModel.  # noqa: E501

        Bumbal id for vehicle_type  # noqa: E501

        :return: The vehicle_type_id of this VehicleModel.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_type_id

    @vehicle_type_id.setter
    def vehicle_type_id(self, vehicle_type_id):
        """Sets the vehicle_type_id of this VehicleModel.

        Bumbal id for vehicle_type  # noqa: E501

        :param vehicle_type_id: The vehicle_type_id of this VehicleModel.  # noqa: E501
        :type: int
        """
        allowed_values = [1, 2, 3, 4]  # noqa: E501
        if (self._configuration.client_side_validation and
                vehicle_type_id not in allowed_values):
            raise ValueError(
                "Invalid value for `vehicle_type_id` ({0}), must be one of {1}"  # noqa: E501
                .format(vehicle_type_id, allowed_values)
            )

        self._vehicle_type_id = vehicle_type_id

    @property
    def vehicle_type_name(self):
        """Gets the vehicle_type_name of this VehicleModel.  # noqa: E501

        Bumbal id for vehicle_type  # noqa: E501

        :return: The vehicle_type_name of this VehicleModel.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_type_name

    @vehicle_type_name.setter
    def vehicle_type_name(self, vehicle_type_name):
        """Sets the vehicle_type_name of this VehicleModel.

        Bumbal id for vehicle_type  # noqa: E501

        :param vehicle_type_name: The vehicle_type_name of this VehicleModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["car", "small_truck", "truck", "bike"]  # noqa: E501
        if (self._configuration.client_side_validation and
                vehicle_type_name not in allowed_values):
            raise ValueError(
                "Invalid value for `vehicle_type_name` ({0}), must be one of {1}"  # noqa: E501
                .format(vehicle_type_name, allowed_values)
            )

        self._vehicle_type_name = vehicle_type_name

    @property
    def name(self):
        """Gets the name of this VehicleModel.  # noqa: E501

        name  # noqa: E501

        :return: The name of this VehicleModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VehicleModel.

        name  # noqa: E501

        :param name: The name of this VehicleModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def registration_nr(self):
        """Gets the registration_nr of this VehicleModel.  # noqa: E501

        registration_nr  # noqa: E501

        :return: The registration_nr of this VehicleModel.  # noqa: E501
        :rtype: str
        """
        return self._registration_nr

    @registration_nr.setter
    def registration_nr(self, registration_nr):
        """Sets the registration_nr of this VehicleModel.

        registration_nr  # noqa: E501

        :param registration_nr: The registration_nr of this VehicleModel.  # noqa: E501
        :type: str
        """

        self._registration_nr = registration_nr

    @property
    def max_speed(self):
        """Gets the max_speed of this VehicleModel.  # noqa: E501

        Max Speed in km/h  # noqa: E501

        :return: The max_speed of this VehicleModel.  # noqa: E501
        :rtype: int
        """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        """Sets the max_speed of this VehicleModel.

        Max Speed in km/h  # noqa: E501

        :param max_speed: The max_speed of this VehicleModel.  # noqa: E501
        :type: int
        """

        self._max_speed = max_speed

    @property
    def speed_factor(self):
        """Gets the speed_factor of this VehicleModel.  # noqa: E501

        Speed Factor  # noqa: E501

        :return: The speed_factor of this VehicleModel.  # noqa: E501
        :rtype: float
        """
        return self._speed_factor

    @speed_factor.setter
    def speed_factor(self, speed_factor):
        """Sets the speed_factor of this VehicleModel.

        Speed Factor  # noqa: E501

        :param speed_factor: The speed_factor of this VehicleModel.  # noqa: E501
        :type: float
        """

        self._speed_factor = speed_factor

    @property
    def start_duration(self):
        """Gets the start_duration of this VehicleModel.  # noqa: E501

        Start duration of using this vehicle in minutes  # noqa: E501

        :return: The start_duration of this VehicleModel.  # noqa: E501
        :rtype: int
        """
        return self._start_duration

    @start_duration.setter
    def start_duration(self, start_duration):
        """Sets the start_duration of this VehicleModel.

        Start duration of using this vehicle in minutes  # noqa: E501

        :param start_duration: The start_duration of this VehicleModel.  # noqa: E501
        :type: int
        """

        self._start_duration = start_duration

    @property
    def end_duration(self):
        """Gets the end_duration of this VehicleModel.  # noqa: E501

        End duration of using this vehicle in minutes  # noqa: E501

        :return: The end_duration of this VehicleModel.  # noqa: E501
        :rtype: int
        """
        return self._end_duration

    @end_duration.setter
    def end_duration(self, end_duration):
        """Sets the end_duration of this VehicleModel.

        End duration of using this vehicle in minutes  # noqa: E501

        :param end_duration: The end_duration of this VehicleModel.  # noqa: E501
        :type: int
        """

        self._end_duration = end_duration

    @property
    def duration_factor(self):
        """Gets the duration_factor of this VehicleModel.  # noqa: E501

        Duration Factor  # noqa: E501

        :return: The duration_factor of this VehicleModel.  # noqa: E501
        :rtype: float
        """
        return self._duration_factor

    @duration_factor.setter
    def duration_factor(self, duration_factor):
        """Sets the duration_factor of this VehicleModel.

        Duration Factor  # noqa: E501

        :param duration_factor: The duration_factor of this VehicleModel.  # noqa: E501
        :type: float
        """

        self._duration_factor = duration_factor

    @property
    def cost_per_meter(self):
        """Gets the cost_per_meter of this VehicleModel.  # noqa: E501

        Cost per meter  # noqa: E501

        :return: The cost_per_meter of this VehicleModel.  # noqa: E501
        :rtype: float
        """
        return self._cost_per_meter

    @cost_per_meter.setter
    def cost_per_meter(self, cost_per_meter):
        """Sets the cost_per_meter of this VehicleModel.

        Cost per meter  # noqa: E501

        :param cost_per_meter: The cost_per_meter of this VehicleModel.  # noqa: E501
        :type: float
        """

        self._cost_per_meter = cost_per_meter

    @property
    def cost_per_route(self):
        """Gets the cost_per_route of this VehicleModel.  # noqa: E501

        Cost per route  # noqa: E501

        :return: The cost_per_route of this VehicleModel.  # noqa: E501
        :rtype: float
        """
        return self._cost_per_route

    @cost_per_route.setter
    def cost_per_route(self, cost_per_route):
        """Sets the cost_per_route of this VehicleModel.

        Cost per route  # noqa: E501

        :param cost_per_route: The cost_per_route of this VehicleModel.  # noqa: E501
        :type: float
        """

        self._cost_per_route = cost_per_route

    @property
    def cost_per_driving_minute(self):
        """Gets the cost_per_driving_minute of this VehicleModel.  # noqa: E501

        Cost per driving minute  # noqa: E501

        :return: The cost_per_driving_minute of this VehicleModel.  # noqa: E501
        :rtype: float
        """
        return self._cost_per_driving_minute

    @cost_per_driving_minute.setter
    def cost_per_driving_minute(self, cost_per_driving_minute):
        """Sets the cost_per_driving_minute of this VehicleModel.

        Cost per driving minute  # noqa: E501

        :param cost_per_driving_minute: The cost_per_driving_minute of this VehicleModel.  # noqa: E501
        :type: float
        """

        self._cost_per_driving_minute = cost_per_driving_minute

    @property
    def cost_per_waiting_minute(self):
        """Gets the cost_per_waiting_minute of this VehicleModel.  # noqa: E501

        Cost per waiting minute  # noqa: E501

        :return: The cost_per_waiting_minute of this VehicleModel.  # noqa: E501
        :rtype: float
        """
        return self._cost_per_waiting_minute

    @cost_per_waiting_minute.setter
    def cost_per_waiting_minute(self, cost_per_waiting_minute):
        """Sets the cost_per_waiting_minute of this VehicleModel.

        Cost per waiting minute  # noqa: E501

        :param cost_per_waiting_minute: The cost_per_waiting_minute of this VehicleModel.  # noqa: E501
        :type: float
        """

        self._cost_per_waiting_minute = cost_per_waiting_minute

    @property
    def cost_per_service_minute(self):
        """Gets the cost_per_service_minute of this VehicleModel.  # noqa: E501

        Cost per service minute  # noqa: E501

        :return: The cost_per_service_minute of this VehicleModel.  # noqa: E501
        :rtype: float
        """
        return self._cost_per_service_minute

    @cost_per_service_minute.setter
    def cost_per_service_minute(self, cost_per_service_minute):
        """Sets the cost_per_service_minute of this VehicleModel.

        Cost per service minute  # noqa: E501

        :param cost_per_service_minute: The cost_per_service_minute of this VehicleModel.  # noqa: E501
        :type: float
        """

        self._cost_per_service_minute = cost_per_service_minute

    @property
    def applied_capacities(self):
        """Gets the applied_capacities of this VehicleModel.  # noqa: E501

          # noqa: E501

        :return: The applied_capacities of this VehicleModel.  # noqa: E501
        :rtype: object
        """
        return self._applied_capacities

    @applied_capacities.setter
    def applied_capacities(self, applied_capacities):
        """Sets the applied_capacities of this VehicleModel.

          # noqa: E501

        :param applied_capacities: The applied_capacities of this VehicleModel.  # noqa: E501
        :type: object
        """

        self._applied_capacities = applied_capacities

    @property
    def capacities(self):
        """Gets the capacities of this VehicleModel.  # noqa: E501

          # noqa: E501

        :return: The capacities of this VehicleModel.  # noqa: E501
        :rtype: list[CapacityModel]
        """
        return self._capacities

    @capacities.setter
    def capacities(self, capacities):
        """Sets the capacities of this VehicleModel.

          # noqa: E501

        :param capacities: The capacities of this VehicleModel.  # noqa: E501
        :type: list[CapacityModel]
        """

        self._capacities = capacities

    @property
    def tags(self):
        """Gets the tags of this VehicleModel.  # noqa: E501

          # noqa: E501

        :return: The tags of this VehicleModel.  # noqa: E501
        :rtype: list[TagModel]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VehicleModel.

          # noqa: E501

        :param tags: The tags of this VehicleModel.  # noqa: E501
        :type: list[TagModel]
        """

        self._tags = tags

    @property
    def meta_data(self):
        """Gets the meta_data of this VehicleModel.  # noqa: E501

          # noqa: E501

        :return: The meta_data of this VehicleModel.  # noqa: E501
        :rtype: list[MetaDataModel]
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this VehicleModel.

          # noqa: E501

        :param meta_data: The meta_data of this VehicleModel.  # noqa: E501
        :type: list[MetaDataModel]
        """

        self._meta_data = meta_data

    @property
    def links(self):
        """Gets the links of this VehicleModel.  # noqa: E501

          # noqa: E501

        :return: The links of this VehicleModel.  # noqa: E501
        :rtype: list[LinkModel]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VehicleModel.

          # noqa: E501

        :param links: The links of this VehicleModel.  # noqa: E501
        :type: list[LinkModel]
        """

        self._links = links

    @property
    def files(self):
        """Gets the files of this VehicleModel.  # noqa: E501

          # noqa: E501

        :return: The files of this VehicleModel.  # noqa: E501
        :rtype: list[FileModel]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this VehicleModel.

          # noqa: E501

        :param files: The files of this VehicleModel.  # noqa: E501
        :type: list[FileModel]
        """

        self._files = files

    @property
    def created_at(self):
        """Gets the created_at of this VehicleModel.  # noqa: E501

        created_at date time  # noqa: E501

        :return: The created_at of this VehicleModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VehicleModel.

        created_at date time  # noqa: E501

        :param created_at: The created_at of this VehicleModel.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this VehicleModel.  # noqa: E501

        updated_at date time  # noqa: E501

        :return: The updated_at of this VehicleModel.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VehicleModel.

        updated_at date time  # noqa: E501

        :param updated_at: The updated_at of this VehicleModel.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def updated_by_name(self):
        """Gets the updated_by_name of this VehicleModel.  # noqa: E501

        Vehicle updated by user full name  # noqa: E501

        :return: The updated_by_name of this VehicleModel.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_name

    @updated_by_name.setter
    def updated_by_name(self, updated_by_name):
        """Sets the updated_by_name of this VehicleModel.

        Vehicle updated by user full name  # noqa: E501

        :param updated_by_name: The updated_by_name of this VehicleModel.  # noqa: E501
        :type: str
        """

        self._updated_by_name = updated_by_name

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
        if issubclass(VehicleModel, dict):
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
        if not isinstance(other, VehicleModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VehicleModel):
            return True

        return self.to_dict() != other.to_dict()