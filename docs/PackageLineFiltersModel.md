# PackageLineFiltersModel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at_since** | **datetime** | Show updated since | [optional] 
**updated_at_till** | **datetime** | Show updated till | [optional] 
**id** | **list[int]** | Bumbal package line id&#39;s | [optional] 
**nr** | **list[str]** | PackageLine numbers | [optional] 
**status_id** | **list[int]** | StatusIds of PackageLine, 31: package_line_cancelled, 23: package_line_incomplete, 24: package_line_new, 42: package_line_awaiting, 25: package_line_accepted, 10: package_line_planned, 11: package_line_in_progress, 12: package_line_executed | [optional] 
**active** | **list[int]** | Active status of PackageLine, 0 values represent deleted PackageLines | [optional] 
**status_name** | **list[str]** | PackageLine Status | [optional] 
**nr_of_packages** | **float** | Number of packages in package line | [optional] 
**package_type_name** | **list[str]** | Type of the Packages | [optional] 
**package_type_id** | **list[int]** | ID of the package type for the packages | [optional] 
**applied_capacities** | **object** |  | [optional] 
**capacities** | [**list[CapacityModel]**](CapacityModel.md) |  | [optional] 
**barcode** | **list[str]** | barcode for packages | [optional] 
**adr** | **bool** | boolean for whether or not the packages in package line should be considered as ADR | [optional] 
**adr_class** | **list[int]** | ADR class of packages in package line | [optional] 
**adr_un_nr** | **list[int]** | ADR UN Nr of packages in package line | [optional] 
**temp** | **bool** | boolean for whether or not the packages in package line should be considered as temperature dependent | [optional] 
**temp_min** | **float** | minimum temperature for packages in package line | [optional] 
**temp_max** | **float** | maximum temperature for packages in package line | [optional] 
**hs_code** | **list[str]** | Harmonized System code for packages | [optional] 
**description** | **str** | description of this package_line | [optional] 
**links** | [**list[LinkModel]**](LinkModel.md) |  | [optional] 
**activity_links** | [**list[LinkModel]**](LinkModel.md) |  | [optional] 
**activity_id** | **list[int]** | Activity id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


