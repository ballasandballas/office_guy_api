# BillingRecurringChargeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**AllOfBillingRecurringChargeRequestCustomer**](AllOfBillingRecurringChargeRequestCustomer.md) | Customer | 
**payment_method** | [**AllOfBillingRecurringChargeRequestPaymentMethod**](AllOfBillingRecurringChargeRequestPaymentMethod.md) | Payment method details&lt;div&gt;&lt;i&gt;Leave this empty to use the customer payment method, or when using the SingleUseToken&lt;/i&gt;&lt;/div&gt; | [optional] 
**single_use_token** | **str** | Single use token, for all payment details (CardNumber, Expiration, CVV, CitizenID).&lt;div&gt;&lt;i&gt;Used primarily by the Payments JavaScript API.&lt;/i&gt;&lt;/div&gt; | [optional] 
**items** | [**list[BillingTypedChargeRecurringItem]**](BillingTypedChargeRecurringItem.md) | Items | 
**update_customer_by_email** | **bool** | Update customer by email&lt;div&gt;&lt;i&gt;Defaults to False&lt;/i&gt;&lt;/div&gt; | [optional] 
**update_customer_by_email_attach_document** | **bool** | Attach invoice/receipt to email&lt;div&gt;&lt;i&gt;Defaults to False&lt;/i&gt;&lt;/div&gt; | [optional] 
**authorise_only** | **bool** | Should the transaction be committed, or authorized only.&lt;div&gt;&lt;i&gt;Leave empty for \&quot;False\&quot; (Auto-Commit).  This field could be used for testing the Charge action easily.  Please note, when using AuthoriseOnly, documents will be created as \&quot;Draft\&quot;, and recurring items will be created as cancelled.&lt;/i&gt;&lt;/div&gt; | [optional] 
**document_type** | [**AllOfBillingRecurringChargeRequestDocumentType**](AllOfBillingRecurringChargeRequestDocumentType.md) | Created document type&lt;div&gt;&lt;i&gt;Leave empty for default&lt;/i&gt;&lt;/div&gt; | [optional] 
**send_copy_to_organization** | **bool** | Send email to the organization as well.  Defaults to the accounting application settings.&lt;div&gt;&lt;i&gt;Relevant when using UpdateCustomerByEmail.&lt;/i&gt;&lt;/div&gt; | [optional] 
**vat_included** | **bool** | Is VAT included in the prices?&lt;div&gt;&lt;i&gt;Leave empty for false.  Relevant for items only.&lt;/i&gt;&lt;/div&gt; | [optional] 
**attribution_offset** | **int** | Attribution offset in months | [optional] 
**credit_card_payments_count** | **int** | Credit card payments count.  Please note this is not the recurrence (how many months the transaction should last), this parameter shouldn&#x27;t be used on most use cases.&lt;div&gt;&lt;i&gt;Leave this empty to disable payments and use standard direct debit.&lt;/i&gt;&lt;/div&gt; | [optional] 
**merchant_number** | **str** | Shva merchant number (Terminal number).&lt;div&gt;&lt;i&gt;This parameter should only be used when multiple merchants are defined in the company.&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**AllOfBillingRecurringChargeRequestCredentials**](AllOfBillingRecurringChargeRequestCredentials.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

