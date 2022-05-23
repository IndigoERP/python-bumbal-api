# RouteFiltersModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **list[int]** | Unique Identifier | [optional] 
**co_driver_ids** | **list[int]** | Unique Identifier | [optional] 
**nr** | **list[str]** | Route nr | [optional] 
**date_time_from** | **datetime** |  | [optional] 
**date_time_to** | **datetime** |  | [optional] 
**earliest_date_time_since** | **datetime** | filter routes with an Earliest DateTime To since this input | [optional] 
**earliest_date_time_till** | **datetime** | filter routes with an Earliest DateTime To till this input | [optional] 
**latest_date_time_since** | **datetime** | filter routes with an Latest DateTime To since this input | [optional] 
**latest_date_time_till** | **datetime** | filter routes with an Latest DateTime To till this input | [optional] 
**updated_at** | **datetime** |  | [optional] 
**updated_at_since** | **datetime** | filter routes with an updated at date-time since this input | [optional] 
**updated_at_till** | **datetime** | filter routes with an updated at date-time till this input | [optional] 
**status_id** | **list[int]** |  | [optional] 
**driver_id** | **list[int]** |  | [optional] 
**recurrence_id** | **int** | Recurrence ID | [optional] 
**tag_names** | **list[str]** | Tag names | [optional] 
**zone_names** | **list[str]** | Zone names | [optional] 
**optimized** | **list[bool]** | Optimized status of Route. | [optional] 
**blocked** | **list[bool]** | Blocked status of Route | [optional] 
**nr_of_stops** | **list[int]** | Number of stops | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


