# NoteModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Identifier | [optional] 
**object_type_name** | **str** | Object type name | [optional] 
**object_id** | **int** | Object ID | [optional] 
**object_link** | [**LinkModel**](LinkModel.md) |  | [optional] 
**note_category_id** | **int** | Note category id | [optional] 
**note_category_name** | **str** | Note category name | [optional] 
**visible_for_driver** | **bool** | Notition is visible in driver App | [optional] 
**title** | **str** | Note title | [optional] 
**updated_by_name** | **str** | Note updated by user full name | [optional] 
**content** | **str** | Note content | [optional] 
**files** | [**list[FileModel]**](FileModel.md) |  | [optional] 
**links** | [**list[LinkModel]**](LinkModel.md) |  | [optional] 
**meta_data** | [**list[MetaDataModel]**](MetaDataModel.md) |  | [optional] 
**active** | **bool** | if active&#x3D;0: note has been removed and is no longer visible in any bumbal interface | [optional] 
**created_at** | **datetime** | created_at date time | [optional] 
**updated_at** | **datetime** | updated_at date time | [optional] 
**created_by** | **int** | created_by user id | [optional] 
**updated_by** | **int** | updated_by user id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


