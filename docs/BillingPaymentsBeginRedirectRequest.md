# BillingPaymentsBeginRedirectRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**AccountingTypedCustomer**](AccountingTypedCustomer.md) | Customer | 
**items** | [**list[BillingTypedChargeItem]**](BillingTypedChargeItem.md) | Items | 
**vat_included** | **bool** | Is VAT included in the prices?&lt;div&gt;&lt;i&gt;Leave empty for false.  Relevant for items only.&lt;/i&gt;&lt;/div&gt; | [optional] 
**document_type** | **str** | Created document type&lt;div&gt;&lt;i&gt;Leave empty for default&lt;/i&gt;&lt;/div&gt; | [optional] 
**redirect_url** | **str** | URL to redirect the user on successful payment.&lt;div&gt;&lt;i&gt;The following parameters will be added to the URL:  OG-CustomerID: Customer identifier  OG-PaymentID: Payment identifier  OG-ExternalIdentifier: The original ExternalIdentifier  When empty, the user will be redirected the the customer payments history page&lt;/i&gt;&lt;/div&gt; | [optional] 
**external_identifier** | **str** | External identifier.&lt;div&gt;&lt;i&gt;This identifier will be appended to the RedirectURL on successful payment.&lt;/i&gt;&lt;/div&gt; | [optional] 
**maximum_payments** | **int** | Maximum payments (installments) allowed on the payment page.&lt;div&gt;&lt;i&gt;By default, the maximum payments count is set according to the purchase pages application settings.  Set to 0 to disable payments.&lt;/i&gt;&lt;/div&gt; | [optional] 
**send_update_by_email_address** | **str** | Email address to which the result document will be created following payments. | [optional] 
**expiration_hours** | **int** | Number of hours, in which the direct URL will expire.&lt;div&gt;&lt;i&gt;Defaults to 1 hours. Maximum of 240 hours (10 days).&lt;/i&gt;&lt;/div&gt; | [optional] 
**theme** | **str** | Payment page theme | [optional] 
**language** | **str** | Payment page language&lt;div&gt;&lt;i&gt;Defaults to Hebrew&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**CoreAPICredentials**](CoreAPICredentials.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


