# AccountingTypedDocumentItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **float** | Quantity&lt;div&gt;&lt;i&gt;Defaults to 1&lt;/i&gt;&lt;/div&gt; | [optional] 
**unit_price** | **float** | Unit price in ILS&lt;div&gt;&lt;i&gt;Single unit price.  Leave this empty for non-ILS documents and automatic exchange rate.&lt;/i&gt;&lt;/div&gt; | [optional] 
**total_price** | **float** | Total price in ILS&lt;div&gt;&lt;i&gt;Leave this empty to auto calculate on ILS documents: Total price - Unit price * Quantity.  Leave this empty for non-ILS documents and automatic exchange rate.&lt;/i&gt;&lt;/div&gt; | [optional] 
**document_currency_unit_price** | **float** | Unit price in document currency&lt;div&gt;&lt;i&gt;Single unit price in the document currency.  Leave this empty for ILS documents / automatic exchange rate.&lt;/i&gt;&lt;/div&gt; | [optional] 
**document_currency_total_price** | **float** | Total price in document currency&lt;div&gt;&lt;i&gt;Leave this empty to auto calculate: Total price - Unit price * Quantity.  Leave this empty for ILS documents / automatic exchange rate.&lt;/i&gt;&lt;/div&gt; | [optional] 
**item** | [**AllOfAccountingTypedDocumentItemItem**](AllOfAccountingTypedDocumentItemItem.md) | Item details | [optional] 
**description** | **str** | Document description. The description is shown in the printed document. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

