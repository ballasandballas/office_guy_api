# AccountingTypedDocumentDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_draft** | **bool** | Save document as draft&lt;div&gt;&lt;i&gt;Leave empty for final document&lt;/i&gt;&lt;/div&gt; | [optional] 
**_date** | **datetime** | Document date&lt;div&gt;&lt;i&gt;Defaults to the current date&lt;/i&gt;&lt;/div&gt; | [optional] 
**customer** | [**AllOfAccountingTypedDocumentDetailsCustomer**](AllOfAccountingTypedDocumentDetailsCustomer.md) | Customer | 
**send_by_email** | [**AllOfAccountingTypedDocumentDetailsSendByEmail**](AllOfAccountingTypedDocumentDetailsSendByEmail.md) | Send document by email after creation | [optional] 
**language** | [**AllOfAccountingTypedDocumentDetailsLanguage**](AllOfAccountingTypedDocumentDetailsLanguage.md) | Document language&lt;div&gt;&lt;i&gt;Defaults to the company language&lt;/i&gt;&lt;/div&gt; | [optional] 
**currency** | [**AllOfAccountingTypedDocumentDetailsCurrency**](AllOfAccountingTypedDocumentDetailsCurrency.md) | Document currency&lt;div&gt;&lt;i&gt;Defaults to the company currency&lt;/i&gt;&lt;/div&gt; | [optional] 
**type** | [**AllOfAccountingTypedDocumentDetailsType**](AllOfAccountingTypedDocumentDetailsType.md) | Document type | 
**description** | **str** | Document description. The description is shown in the printed document. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

