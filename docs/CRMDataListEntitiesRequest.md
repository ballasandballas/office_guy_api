# CRMDataListEntitiesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** | Folder identifier.&lt;div&gt;&lt;i&gt;Can be either application folder name, or FolderID.&lt;/i&gt;&lt;/div&gt; | [optional] 
**include_inherited_folders** | **bool** | Include entities from inherited folders | [optional] 
**filters** | [**list[CoreTypedFilter]**](CoreTypedFilter.md) | List filters | [optional] 
**order** | [**CoreTypedOrder**](CoreTypedOrder.md) | List results order (sort) | [optional] 
**paging** | [**CoreTypedPaging**](CoreTypedPaging.md) | List paging | [optional] 
**load_properties** | **bool** | Load results properties&lt;div&gt;&lt;i&gt;Defaults to false&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**CoreAPICredentials**](CoreAPICredentials.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


