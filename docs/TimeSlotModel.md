# TimeSlotModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**time_slot_type** | **str** | Time Slot Type. first-entry (:1), planned (:2), actual (:3) | [optional] 
**time_slot_type_id** | **int** | Time Slot Type ID, by default 1 if left out of the request. 1: first-entry, 2: planned, 3: actual | [optional] 
**activity_id** | **int** | Activity ID to which this TimeSlot belongs | [optional] 
**date_from** | **date** |  | [optional] 
**time_from** | **str** |  | [optional] 
**date_time_from** | **datetime** |  | [optional] 
**date_to** | **date** |  | [optional] 
**time_to** | **str** |  | [optional] 
**date_time_to** | **datetime** |  | [optional] 
**planned** | **bool** | true if this time_slot was used to plan the activity within | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


