# SettingsModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**settings_group_id** | **int** | SettingsGroup id of this setting. Possible values: 1: general, 2: address, 3: package, 4: activity, 5: equipment, 6: note, 7: optimisation, 8: filters | [optional] 
**settings_group_name** | **str** | SettingsGroup name of this setting | [optional] 
**key** | **str** | Unique string key for setting identification | [optional] 
**value** | **str** | Set value for setting | [optional] 
**value_options** | [**list[ValueOptionModel]**](ValueOptionModel.md) |  | [optional] 
**setting_updated_at** | **datetime** | updated_at date time | [optional] 
**setting_updated_by** | **int** | updated_by user id | [optional] 
**setting_updated_by_user** | [**UsersModel**](UsersModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


