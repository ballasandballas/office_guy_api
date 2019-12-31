# AccountingDocumentsSendRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | Document identifier | [optional] 
**document_type** | **str** | Document type | [optional] 
**document_number** | **int** | Document number | [optional] 
**email_address** | **str** | Email address&lt;div&gt;&lt;i&gt;Defaults to the customer email address&lt;/i&gt;&lt;/div&gt; | [optional] 
**sender_user_id** | **int** | Sender user ID&lt;div&gt;&lt;i&gt;Defaults to the company owner&lt;/i&gt;&lt;/div&gt; | [optional] 
**original** | **bool** | Send original document if possible&lt;div&gt;&lt;i&gt;Defaults to False&lt;/i&gt;&lt;/div&gt; | [optional] 
**language** | **str** | Email language&lt;div&gt;&lt;i&gt;Defaults to the company language&lt;/i&gt;&lt;/div&gt; | [optional] 
**personal_message** | **str** | Personal message | [optional] 
**credentials** | [**CoreAPICredentials**](CoreAPICredentials.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


