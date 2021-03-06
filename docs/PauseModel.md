# PauseModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Identifier | [optional] 
**drive_time_mode** | **bool** | Determines if pause is a drivetime pause or a timewindow pause | [optional] 
**name** | **str** | Name of pause | [optional] 
**initial_driving_duration** | **int** | initial driving time in minutes until first possibility of starting pause. (Only used in servicewindow pause) | [optional] 
**max_driving_duration** | **int** | max driving time in minutes before a pause must be started | [optional] 
**pause_duration** | **int** | (total) duration for pause(s) in minutes | [optional] 
**possible_split** | **list[int]** | A list of durations in minutes by which the total duration of the pause may be split. (Only used in servicewindow pause) | [optional] 
**earliest_time** | **str** | Earliest time. (Only used in drivetime pause) | [optional] 
**latest_time** | **str** | Latest time. (Only used in drivetime pause) | [optional] 
**links** | [**list[LinkModel]**](LinkModel.md) |  | [optional] 
**meta_data** | [**list[MetaDataModel]**](MetaDataModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


