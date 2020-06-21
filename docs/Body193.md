# Body193

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**Object**](Object.md) | Customer | 
**payment_method** | [**Object**](Object.md) | Payment method details&lt;div&gt;&lt;i&gt;Leave this empty to use the customer payment method, or when using the SingleUseToken&lt;/i&gt;&lt;/div&gt; | [optional] 
**single_use_token** | **str** | Single use token, for all payment details (CardNumber, Expiration, CVV, CitizenID).&lt;div&gt;&lt;i&gt;Used primarily by the Payments JavaScript API.&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_auth_number** | **str** | Transaction authorization number, as received from a previous Gateway Transaction | [optional] 
**items** | [**list[BillingTypedChargeItem]**](BillingTypedChargeItem.md) | Items | 
**payments_count** | **int** | Payments count&lt;div&gt;&lt;i&gt;Leave this empty to disable payments&lt;/i&gt;&lt;/div&gt; | [optional] 
**payments_first_amount** | **float** | First payment amount&lt;div&gt;&lt;i&gt;Leave this empty to disable payments / automatic payments calculating&lt;/i&gt;&lt;/div&gt; | [optional] 
**payments_non_first_amount** | **float** | Non-first payment amount&lt;div&gt;&lt;i&gt;Leave this empty to disable payments / automatic payments calculating&lt;/i&gt;&lt;/div&gt; | [optional] 
**update_customer_by_email** | **bool** | Update customer by email (notification email, with invoice/receipt download link)&lt;div&gt;&lt;i&gt;Leave this empty to disable email sending feature&lt;/i&gt;&lt;/div&gt; | [optional] 
**update_customer_by_email_attach_document** | **bool** | Attach invoice/receipt to email&lt;div&gt;&lt;i&gt;Defaults to False&lt;/i&gt;&lt;/div&gt; | [optional] 
**update_customer_by_email_language** | [**Object**](Object.md) | Update email language&lt;div&gt;&lt;i&gt;Defaults to the company language&lt;/i&gt;&lt;/div&gt; | [optional] 
**send_document_by_email** | **bool** | Send invoice/receipt by email | [optional] 
**send_document_by_email_language** | [**Object**](Object.md) | Send document email language&lt;div&gt;&lt;i&gt;Defaults to the company language&lt;/i&gt;&lt;/div&gt; | [optional] 
**document_language** | [**Object**](Object.md) | Document language&lt;div&gt;&lt;i&gt;Defaults to the company language&lt;/i&gt;&lt;/div&gt; | [optional] 
**document_description** | **str** | Document description (the description is printed on the document) | [optional] 
**vat_included** | **bool** | Is VAT included in the prices?&lt;div&gt;&lt;i&gt;Defaults to false&lt;/i&gt;&lt;/div&gt; | [optional] 
**vat_rate** | **float** | Document VAT Rate&lt;div&gt;&lt;i&gt;Leave empty for company default.  Relevant for items only.&lt;/i&gt;&lt;/div&gt; | [optional] 
**authorise_only** | **bool** | Should the transaction be committed, or authorized only.&lt;div&gt;&lt;i&gt;Leave empty for \&quot;False\&quot; (Auto-Commit).  This field could be used for testing the Charge action easily.  Please note, when using AuthoriseOnly, documents will be issued as \&quot;Draft\&quot;.&lt;/i&gt;&lt;/div&gt; | [optional] 
**draft_document** | **bool** | Create draft document?&lt;div&gt;&lt;i&gt;Leave empty to use the application setting.  Please note, when using AuthoriseOnly, documents will always be issued as \&quot;Draft\&quot;.&lt;/i&gt;&lt;/div&gt; | [optional] 
**document_type** | [**Object**](Object.md) | Create document type&lt;div&gt;&lt;i&gt;Leave empty for default&lt;/i&gt;&lt;/div&gt; | [optional] 
**support_credit** | **bool** | Allow credit instead of charge (debit), in case the total is less than 0?&lt;div&gt;&lt;i&gt;Defaults to false&lt;/i&gt;&lt;/div&gt; | [optional] 
**merchant_number** | **str** | Shva merchant number (Terminal number).&lt;div&gt;&lt;i&gt;This parameter should only be used when multiple merchants are defined in the company.&lt;/i&gt;&lt;/div&gt; | [optional] 
**send_copy_to_organization** | **bool** | Send email to the organization as well.  Defaults to the accounting application settings.&lt;div&gt;&lt;i&gt;Relevant when using either UpdateCustomerByEmail or SendDocumentByEmail.&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**Object**](Object.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

