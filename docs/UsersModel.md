# UsersModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**uuid** | **str** | unique per user | [optional] 
**role_id** | **int** | id of the user role, 1: Guest, 2: Driver, 3: Planner, 4: Manager, 5: Admin | [optional] 
**role_name** | **str** | Role name | [optional] 
**party_id** | **int** | Associated Party ID | [optional] 
**party_name** | **str** |  | [optional] 
**first_name** | **str** | First name | [optional] 
**name_prefix** | **str** | Name prefix | [optional] 
**last_name** | **str** | Last name | [optional] 
**full_name** | **str** | Full name | [optional] 
**initials** | **str** | user password (set only, no read) | [optional] 
**email** | **str** | user email (used for login) | [optional] 
**password** | **str** | user password (set only, no read) | [optional] 
**lang_code** | **str** | lang code (nl &#x3D; default) | [optional] 
**address_id** | **int** | id of the user address | [optional] 
**addresses** | [**list[AddressModel]**](AddressModel.md) | user address (mostly interesting for drivers) | [optional] 
**pause_id** | **int** | id of the pause to be applied by default for new user routes | [optional] 
**speed_factor** | **float** | Speed Factor | [optional] 
**duration_factor** | **float** | Duration Factor | [optional] 
**activated** | **bool** | Whether user is activated or not | [optional] 
**removed** | **bool** | Whether user is removed or not | [optional] 
**active** | **bool** | Whether user is still active or not | [optional] 
**tags** | [**list[TagModel]**](TagModel.md) |  | [optional] 
**tag_names** | **list[str]** | Tag names | [optional] 
**zones** | [**list[ZoneModel]**](ZoneModel.md) |  | [optional] 
**zone_names** | **list[str]** | Zone names | [optional] 
**links** | [**list[LinkModel]**](LinkModel.md) |  | [optional] 
**meta_data** | [**list[MetaDataModel]**](MetaDataModel.md) |  | [optional] 
**driver_unavailabilities** | [**list[DriverUnavailabilityModel]**](DriverUnavailabilityModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


