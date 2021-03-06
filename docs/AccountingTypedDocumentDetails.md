# AccountingTypedDocumentDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_draft** | **bool** | Save document as draft&lt;div&gt;&lt;i&gt;Leave empty for final document&lt;/i&gt;&lt;/div&gt; | [optional] 
**_date** | **datetime** | Document date&lt;div&gt;&lt;i&gt;Defaults to the current date&lt;/i&gt;&lt;/div&gt; | [optional] 
**customer** | [**AccountingTypedCustomer**](AccountingTypedCustomer.md) | Customer | 
**send_by_email** | [**AccountingTypedDocumentSendByEmail**](AccountingTypedDocumentSendByEmail.md) | Send document by email after creation | [optional] 
**language** | **str** | Document language&lt;div&gt;&lt;i&gt;Defaults to the company language&lt;/i&gt;&lt;/div&gt; | [optional] 
**currency** | **str** | Document currency&lt;div&gt;&lt;i&gt;Defaults to the company currency&lt;/i&gt;&lt;/div&gt; | [optional] 
**type** | **str** | Document type | 
**description** | **str** | Document description. The description is shown in the printed document. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


