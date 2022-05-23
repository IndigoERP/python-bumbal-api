# VehicleModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Identifier | [optional] 
**vehicle_type_id** | **int** | Bumbal id for vehicle_type | [optional] 
**vehicle_type_name** | **str** | Bumbal id for vehicle_type | [optional] 
**name** | **str** | name | [optional] 
**registration_nr** | **str** | registration_nr | [optional] 
**max_speed** | **int** | Max Speed in km/h | [optional] 
**speed_factor** | **float** | Speed Factor | [optional] 
**start_duration** | **int** | Start duration of using this vehicle in minutes | [optional] 
**end_duration** | **int** | End duration of using this vehicle in minutes | [optional] 
**duration_factor** | **float** | Duration Factor | [optional] 
**cost_per_meter** | **float** | Cost per meter | [optional] 
**cost_per_route** | **float** | Cost per route | [optional] 
**cost_per_driving_minute** | **float** | Cost per driving minute | [optional] 
**cost_per_waiting_minute** | **float** | Cost per waiting minute | [optional] 
**cost_per_service_minute** | **float** | Cost per service minute | [optional] 
**applied_capacities** | **object** |  | [optional] 
**capacities** | [**list[CapacityModel]**](CapacityModel.md) |  | [optional] 
**tags** | [**list[TagModel]**](TagModel.md) |  | [optional] 
**meta_data** | [**list[MetaDataModel]**](MetaDataModel.md) |  | [optional] 
**links** | [**list[LinkModel]**](LinkModel.md) |  | [optional] 
**files** | [**list[FileModel]**](FileModel.md) |  | [optional] 
**created_at** | **datetime** | created_at date time | [optional] 
**updated_at** | **datetime** | updated_at date time | [optional] 
**updated_by_name** | **str** | Vehicle updated by user full name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


