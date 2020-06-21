# CreditGuyBillingLoadRequestLoadRequestTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format_preserving_token** | **str** | Format preserving card number&lt;div&gt;&lt;i&gt;Leave this empty when using CardToken&lt;/i&gt;&lt;/div&gt; | [optional] 
**card_token** | **str** | Card token&lt;div&gt;&lt;i&gt;Leave this empty when using FormatPreservingToken&lt;/i&gt;&lt;/div&gt; | [optional] 
**expiration_month** | **int** | Card expiration month (1-12) | 
**expiration_year** | **int** | Card expiration year (4 digits) | 
**amount** | **float** | Transaction amount | 
**payments_non_first_count** | **int** | Non-first payments count&lt;div&gt;&lt;i&gt;Leave this empty for non-payments transaction&lt;/i&gt;&lt;/div&gt; | [optional] 
**payments_first_amount** | **float** | First payment amount&lt;div&gt;&lt;i&gt;Leave this empty for non-payments transaction&lt;/i&gt;&lt;/div&gt; | [optional] 
**payments_non_first_amount** | **float** | Non-first payment amount&lt;div&gt;&lt;i&gt;Leave this empty for non-payments transaction&lt;/i&gt;&lt;/div&gt; | [optional] 
**auth_number** | **str** | Transaction authorization number&lt;div&gt;&lt;i&gt;Leave this empty for J4+J5&lt;/i&gt;&lt;/div&gt; | [optional] 
**citizen_id** | **str** | Israel Citizen ID / Passport Number | [optional] 
**currency** | [**AllOfCreditGuyBillingLoadRequestLoadRequestTransactionCurrency**](AllOfCreditGuyBillingLoadRequestLoadRequestTransactionCurrency.md) | Transaction currency&lt;div&gt;&lt;i&gt;Defaults to ILS&lt;/i&gt;&lt;/div&gt; | [optional] 
**unique_identifier** | **str** | Unique transaction identifier.&lt;div&gt;&lt;i&gt;This parameter can be used for preventing duplicate transactions&lt;/i&gt;&lt;/div&gt; | [optional] 
**merchant_number** | **str** | Shva merchant number (Terminal number).&lt;div&gt;&lt;i&gt;This parameter should only be used when multiple merchants are defined in the company.&lt;/i&gt;&lt;/div&gt; | [optional] 
**custom_data_1** | **str** | Custom data #1 | [optional] 
**custom_data_2** | **str** | Custom data #2 | [optional] 
**custom_data_3** | **str** | Custom data #3 | [optional] 
**custom_data_4** | **str** | Custom data #4 | [optional] 
**custom_data_5** | **str** | Custom data #5 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

