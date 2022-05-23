# DriverModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Identifier | [optional] 
**pause_id** | **int** | id of pause scheme to apply | [optional] 
**uuid** | **str** | unique per user | [optional] 
**addresses** | [**list[AddressModel]**](AddressModel.md) | user address (mostly interesting for drivers) | [optional] 
**tag_names** | **list[str]** | Tag names | [optional] 
**tag_ids** | **list[int]** | Tag type ids | [optional] 
**first_name** | **str** | First Name | [optional] 
**last_name** | **str** | Last Name | [optional] 
**name_prefix** | **str** | Name Prefix | [optional] 
**full_name** | **str** | Full name | [optional] 
**initials** | **str** | Full name | [optional] 
**email** | **str** | Email | [optional] 
**tags** | [**list[TagModel]**](TagModel.md) |  | [optional] 
**zones** | [**list[ZoneModel]**](ZoneModel.md) |  | [optional] 
**zone_names** | **list[str]** | Zone names | [optional] 
**zone_ids** | **list[int]** | Zone ids | [optional] 
**links** | [**list[LinkModel]**](LinkModel.md) |  | [optional] 
**notes** | [**list[NoteModel]**](NoteModel.md) |  | [optional] 
**removed** | **bool** | Whether user is removed or not | [optional] 
**active** | **bool** | Whether user is still active or not | [optional] 
**meta_data** | [**list[MetaDataModel]**](MetaDataModel.md) |  | [optional] 
**files** | [**list[FileModel]**](FileModel.md) |  | [optional] 
**driver_created_at** | **datetime** | created_at date time | [optional] 
**driver_updated_at** | **datetime** | updated_at date time | [optional] 
**driver_created_by** | **int** | created_by user id | [optional] 
**driver_updated_by** | **int** | created_by user id | [optional] 
**updated_by_name** | **str** | Driver updated by user full name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


