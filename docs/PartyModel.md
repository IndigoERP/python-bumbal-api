# PartyModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Identifier | [optional] 
**party_type_name** | **str** | Type of this party | [optional] 
**party_type_id** | **int** | PartyTypeID of this party. 2 &#x3D; contractor, 3 &#x3D; booking | [optional] 
**name_1** | **str** | Name 1 for party | [optional] 
**name_2** | **str** | Name 2 for party | [optional] 
**nr** | **str** | Number of this party | [optional] 
**contact_person** | **str** | Contact person for party | [optional] 
**url** | **str** | Url for party website | [optional] 
**tags** | [**list[TagModel]**](TagModel.md) |  | [optional] 
**tag_names** | **list[str]** | Tag names | [optional] 
**tag_ids** | **list[int]** | Tag ids | [optional] 
**links** | [**list[LinkModel]**](LinkModel.md) |  | [optional] 
**meta_data** | [**list[MetaDataModel]**](MetaDataModel.md) |  | [optional] 
**notes** | [**list[NoteModel]**](NoteModel.md) |  | [optional] 
**files** | [**list[FileModel]**](FileModel.md) |  | [optional] 
**created_at** | **datetime** | created_at date time | [optional] 
**updated_at** | **datetime** | updated_at date time | [optional] 
**party_created_by_user** | [**UsersModel**](UsersModel.md) |  | [optional] 
**party_updated_by_user** | [**UsersModel**](UsersModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


