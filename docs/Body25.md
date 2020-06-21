# Body25

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expense_number** | **str** | Expense invoice number | [optional] 
**expense_file** | **str** | Expense file contents | [optional] 
**supplier** | [**Object**](Object.md) | Expense supplier | [optional] 
**_date** | **datetime** | Expense date | [optional] 
**lines** | [**list[AccountingTypedDocumentExpenseItem]**](AccountingTypedDocumentExpenseItem.md) | Expense items and amounts | [optional] 
**payments** | [**list[AccountingTypedDocumentPayment]**](AccountingTypedDocumentPayment.md) | Document payments&lt;div&gt;&lt;i&gt;Please note each payment should contain a single details object (Cash/BankTransfer/Cheque/CreditCard/Other), multiple payments are handled through the payments array.&lt;/i&gt;&lt;/div&gt; | [optional] 
**description** | **str** | Expense description/remarks | [optional] 
**is_draft** | **bool** | Save document as draft | [optional] 
**vat_rate** | **float** | Document VAT Rate&lt;div&gt;&lt;i&gt;Leave empty for company default&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**Object**](Object.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

