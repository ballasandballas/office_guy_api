# Body242

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | **list[str]** | Recipients | 
**text** | **str** | Body (formatted as HTML) | 
**save_draft** | **bool** | Save as draft? (Prevents automatic sending)&lt;div&gt;&lt;i&gt;Defaults to false (No draft)&lt;/i&gt;&lt;/div&gt; | [optional] 
**schedule** | **datetime** | Schedule sending for a future date&lt;div&gt;&lt;i&gt;Not supported for draft saving&lt;/i&gt;&lt;/div&gt; | [optional] 
**sender** | **str** | Sender number&lt;div&gt;&lt;i&gt;Sender number should be verified prior to sending SMS messages&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**Object**](Object.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

