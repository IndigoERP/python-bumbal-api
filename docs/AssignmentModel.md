# AssignmentModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID of this Assignment | [optional] 
**party_id** | **int** | Party ID | [optional] 
**booking_account_id** | **int** | Booking account ID | [optional] 
**tag_names** | **list[str]** | Tag names | [optional] 
**tag_ids** | **list[int]** | Tag ids | [optional] 
**activities** | [**list[ActivityModel]**](ActivityModel.md) |  | [optional] 
**booking_account** | [**PartyModel**](PartyModel.md) |  | [optional] 
**status_id** | **int** | Status ID of this Assignment | [optional] 
**nr** | **str** | Non-Unique number of this Assignment | [optional] 
**party_link** | [**list[LinkModel]**](LinkModel.md) |  | [optional] 
**account_name** | **str** | Account Name associated with this Assignment | [optional] 
**party_name** | **str** | Party Name associated with this Assignment | [optional] 
**reference** | **str** | Reference text of this Assignment | [optional] 
**description** | **str** | Description text of this Assignment | [optional] 
**remarks** | **str** | Remarks about this Assignment | [optional] 
**date_time_from** | **datetime** | Earliest start time of all Activities is this Assignment | [optional] 
**date_time_to** | **datetime** | Latest end time of all Activities is this Assignment | [optional] 
**multi_day** | **bool** | Multi day type assignment | [optional] 
**links** | [**list[LinkModel]**](LinkModel.md) |  | [optional] 
**meta_data** | [**list[MetaDataModel]**](MetaDataModel.md) |  | [optional] 
**notes** | [**list[NoteModel]**](NoteModel.md) |  | [optional] 
**files** | [**list[FileModel]**](FileModel.md) |  | [optional] 
**assignment_created_at** | **datetime** | created_at date time | [optional] 
**assignment_updated_at** | **datetime** | updated_at date time | [optional] 
**assignment_created_by** | **int** | created_by user id | [optional] 
**assignment_updated_by** | **int** | updated_by user id | [optional] 
**assignment_created_by_user** | [**UsersModel**](UsersModel.md) |  | [optional] 
**assignment_updated_by_user** | [**UsersModel**](UsersModel.md) |  | [optional] 
**assignment_active** | **bool** | Assignment is active (&#x3D;true). Inactive assignments are not automatically considered in any of the application algorithms and will not be shown in the Bumbal Gui. | [optional] 
**assignment_removed** | **bool** | Assignment is removed (&#x3D;true). Removed assignments are not automatically considered in any of the application algorithms and will not be shown in the Bumbal Gui. Removed assignments are usually irrepairable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


