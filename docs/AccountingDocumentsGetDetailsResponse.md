# AccountingDocumentsGetDetailsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**AllOfAccountingDocumentsGetDetailsResponseDocument**](AllOfAccountingDocumentsGetDetailsResponseDocument.md) |  | [optional] 
**items** | [**list[AccountingTypedDocumentItem]**](AccountingTypedDocumentItem.md) |  | [optional] 
**payments** | [**list[AccountingTypedDocumentPayment]**](AccountingTypedDocumentPayment.md) |  | [optional] 
**document_download_url** | **str** | Document download URL&lt;div&gt;&lt;i&gt;Produced document will be original on first visit, or certified copy on additional visits.&lt;/i&gt;&lt;/div&gt; | [optional] 
**document_id** | **int** | OfficeGuy Document identifier&lt;div&gt;&lt;i&gt;DocumentID is an internal identifier (also known as Card Number on OfficeGuy). Keep this for further API calls.&lt;/i&gt;&lt;/div&gt; | [optional] 
**document_number** | **int** | Document number&lt;div&gt;&lt;i&gt;For instance, for Invoice #1000, the DocumentNumber will be 1000.&lt;/i&gt;&lt;/div&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

