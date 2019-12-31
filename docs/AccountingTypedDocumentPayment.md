# AccountingTypedDocumentPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Received payment amount&lt;div&gt;&lt;i&gt;Leave this empty for non-ILS documents and automatic exchange rate&lt;/i&gt;&lt;/div&gt; | [optional] 
**document_currency_amount** | **float** | Received payment amount&lt;div&gt;&lt;i&gt;Leave this empty for ILS documents / automatic exchange rate&lt;/i&gt;&lt;/div&gt; | [optional] 
**details_general** | [**AccountingTypedPaymentGeneral**](AccountingTypedPaymentGeneral.md) | General details&lt;div&gt;&lt;i&gt;Provide when payment method isn&#39;t detailed&lt;/i&gt;&lt;/div&gt; | [optional] 
**details_cash** | [**AccountingTypedPaymentCash**](AccountingTypedPaymentCash.md) | Cash details&lt;div&gt;&lt;i&gt;Provide when payment was made using cash&lt;/i&gt;&lt;/div&gt; | [optional] 
**details_bank_transfer** | [**AccountingTypedPaymentBankTransfer**](AccountingTypedPaymentBankTransfer.md) | Bank transfer details&lt;div&gt;&lt;i&gt;Provide when payment was made using bank transfer&lt;/i&gt;&lt;/div&gt; | [optional] 
**details_cheque** | [**AccountingTypedPaymentCheque**](AccountingTypedPaymentCheque.md) | Cheque details&lt;div&gt;&lt;i&gt;Provide when payment was made using cheque&lt;/i&gt;&lt;/div&gt; | [optional] 
**details_credit_card** | [**AccountingTypedPaymentCreditCard**](AccountingTypedPaymentCreditCard.md) | Credit card details&lt;div&gt;&lt;i&gt;Provide when payment was made using external credit card&lt;/i&gt;&lt;/div&gt; | [optional] 
**details_other** | [**AccountingTypedPaymentOther**](AccountingTypedPaymentOther.md) | Other details&lt;div&gt;&lt;i&gt;Provide when payment was made using custom payment method&lt;/i&gt;&lt;/div&gt; | [optional] 
**details_digital** | [**AccountingTypedPaymentDigital**](AccountingTypedPaymentDigital.md) | Digital details&lt;div&gt;&lt;i&gt;Provide when payment was made using digital payment method&lt;/i&gt;&lt;/div&gt; | [optional] 
**details_tax_withholding** | [**AccountingTypedPaymentTaxWithholding**](AccountingTypedPaymentTaxWithholding.md) | Tax Withholding details&lt;div&gt;&lt;i&gt;Provide when taxwithholding&lt;/i&gt;&lt;/div&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


