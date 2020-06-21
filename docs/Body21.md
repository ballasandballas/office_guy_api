# Body21

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**Object**](Object.md) | General document details | 
**items** | [**list[AccountingTypedDocumentItem]**](AccountingTypedDocumentItem.md) | Document items&lt;div&gt;&lt;i&gt;Can be used in Invoice, Invoice/Receipt, Proforma invoice etc.&lt;/i&gt;&lt;/div&gt; | [optional] 
**payments** | [**list[AccountingTypedDocumentPayment]**](AccountingTypedDocumentPayment.md) | Document payments (Can be used in invoice+receipt/receipt)&lt;div&gt;&lt;i&gt;Please note each payment should contain a single details object (Cash/BankTransfer/Cheque/CreditCard/Other), multiple payments are handled through the payments array.&lt;/i&gt;&lt;/div&gt; | [optional] 
**vat_included** | **bool** | Is VAT included in the prices?&lt;div&gt;&lt;i&gt;Leave empty for false.  Relevant for items only.&lt;/i&gt;&lt;/div&gt; | [optional] 
**vat_rate** | **float** | Document VAT Rate&lt;div&gt;&lt;i&gt;Leave empty for company default.  Relevant for items only.&lt;/i&gt;&lt;/div&gt; | [optional] 
**original_document_id** | **int** | Original document identifier.&lt;div&gt;&lt;i&gt;This allows keeping a relationship between an original and a created document (such as credits for debit invoices)&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**Object**](Object.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

