# CRMDataUpdateEntityRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**CoreTypedEntity**](CoreTypedEntity.md) | The entity to be updated | 
**create_if_missing** | **bool** | Should the update create the entity if it doesn&#39;t exist&lt;div&gt;&lt;i&gt;This can only be used when Entity.ID is 0  Defaults to false.&lt;/i&gt;&lt;/div&gt; | [optional] 
**remove_existing_properties** | **bool** | Should the update entity remove all existing properties, which didn&#39;t pass through the Entity.Properties list?&lt;div&gt;&lt;i&gt;Defaults to false&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**CoreAPICredentials**](CoreAPICredentials.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


