# AvailabilityTimeSlotModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**key** | **str** | unique key per analyzed time slot, uuid type | [optional] 
**date_time_from** | **datetime** |  | [optional] 
**date_time_to** | **datetime** |  | [optional] 
**proposed_plan_date_time_from** | **datetime** |  | [optional] 
**proposed_plan_date_time_to** | **datetime** |  | [optional] 
**proposed_driver** | [**DriverModel**](DriverModel.md) |  | [optional] 
**impact** | [**list[AvailabilityTimeSlotImpactModel]**](AvailabilityTimeSlotImpactModel.md) |  | [optional] 
**follow_up_time_slots** | [**list[AvailabilityFollowUpTimeSlotModel]**](AvailabilityFollowUpTimeSlotModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


