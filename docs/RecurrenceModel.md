# RecurrenceModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Identifier | [optional] 
**name** | **str** | Recurrence name | [optional] 
**type_id** | **int** | recurrence type_id, 11:activity, 24:route | [optional] 
**type_name** | **int** | recurrence type_name, activity, route | [optional] 
**recurrence_type_name** | **str** | recurrence typename, activity or route | [optional] 
**start_date** | **datetime** | Start date | [optional] 
**end_date** | **datetime** | End date | [optional] 
**period_name** | **str** | period name | [optional] 
**period_id** | **int** | recurrence period_id, 1:day, 2:week, 3:month | [optional] 
**recurrence_period_name** | **str** | recurrence period name: day, week or month | [optional] 
**frequency** | **int** | period frequency of recurrence (2 &#x3D; repeat each 2 days/weeks/months) | [optional] 
**count** | **int** | nr of last recurrence to be created | [optional] 
**show_ahead** | **int** | nr of recurrences to show ahead in system | [optional] 
**current** | **int** | last created recurrence nr | [optional] 
**summary** | **str** | summary of recurrence | [optional] 
**next_run** | **datetime** | Next date on which a new recurrence will be added | [optional] 
**last_run** | **datetime** | Last date on which a new recurrence was added | [optional] 
**active** | **bool** | if active&#x3D;0: recurrence has been removed and is no longer visible in any bumbal interface | [optional] 
**tags** | [**list[TagModel]**](TagModel.md) |  | [optional] 
**meta_data** | [**list[MetaDataModel]**](MetaDataModel.md) |  | [optional] 
**created_at** | **datetime** | created_at date time | [optional] 
**updated_at** | **datetime** | updated_at date time | [optional] 
**updated_by_name** | **str** | Recurrence updated by user full name | [optional] 
**object_id** | **int** | ID of the object | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


