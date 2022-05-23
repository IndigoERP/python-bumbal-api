# NotificationModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Identifier | [optional] 
**object_type** | **int** | Object type ID | [optional] 
**title** | **str** | Notification title | [optional] 
**object_type_name** | **str** | Object type name | [optional] 
**object_id** | **int** | Object ID | [optional] 
**notification_category_id** | **int** | Notification category id | [optional] 
**notification_category_name** | **str** | Notification category name | [optional] 
**updated_by_name** | **str** | Notification updated by user full name | [optional] 
**content** | **str** | Notification content | [optional] 
**active** | **bool** | if active&#x3D;0: note has been removed and is no longer visible in any bumbal interface | [optional] 
**notification_created_at** | **datetime** | created_at date time | [optional] 
**notification_updated_at** | **datetime** | updated_at date time | [optional] 
**notification_created_by** | **int** | created_by user id | [optional] 
**notification_updated_by** | **int** | updated_by user id | [optional] 
**users** | [**list[UserNotificationModel]**](UserNotificationModel.md) |  | [optional] 
**role_names** | **list[str]** | Roles to enable notification for, works only on create, ignored on update | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


