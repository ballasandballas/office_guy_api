# AccountingGeneralUpdateSettingsRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents_email_address_specified** | **bool** | Indicates if the DocumentsEmailAddress should be updated | [optional] 
**documents_email_address** | **str** | Email address display on all documents&lt;div&gt;&lt;i&gt;By default, the company email address will be displayed&lt;/i&gt;&lt;/div&gt; | [optional] 
**accountant_email_specified** | **bool** | Indicates if the AccountantEmail should be updated | [optional] 
**accountant_email** | **str** | Email address for sending all monthly documents each month | [optional] 
**income_tax_credit_for_donation** | **bool** | Indicates whether the NPO is 46a donations approved, and should be presented on donation receipts | [optional] 
**enable_custom_document_dates** | **bool** | Indicates documents can be created in any custom date.&lt;div&gt;&lt;i&gt;By default, documents can only be created in a sequence order.&lt;/i&gt;&lt;/div&gt; | [optional] 
**documents_theme** | [**AllOfAccountingGeneralUpdateSettingsRequestDocumentsTheme**](AllOfAccountingGeneralUpdateSettingsRequestDocumentsTheme.md) | Choose documents printing theme.&lt;div&gt;&lt;i&gt;By default, documents are created using the Material theme.&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**AllOfAccountingGeneralUpdateSettingsRequestCredentials**](AllOfAccountingGeneralUpdateSettingsRequestCredentials.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

