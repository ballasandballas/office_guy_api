# Body73

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**param_j** | [**Object**](Object.md) | Transaction type | 
**card_number** | **str** | Full card number&lt;div&gt;&lt;i&gt;Leave this empty when using FormatPreservingToken/CardToken/SingleUseToken&lt;/i&gt;&lt;/div&gt; | [optional] 
**format_preserving_token** | **str** | Format preserving card number&lt;div&gt;&lt;i&gt;Leave this empty when using CardNumber/CardToken/SingleUseToken&lt;/i&gt;&lt;/div&gt; | [optional] 
**card_token** | **str** | Card token&lt;div&gt;&lt;i&gt;Leave this empty when using CardNumber/FormatPreservingToken/SingleUseToken&lt;/i&gt;&lt;/div&gt; | [optional] 
**single_use_token** | **str** | Single use token, for all payment details (CardNumber, Expiration, CVV, CitizenID).&lt;div&gt;&lt;i&gt;Used primarily by the Payments JavaScript API.  (Leave this empty when using CardNumber/FormatPreservingToken/CardToken)&lt;/i&gt;&lt;/div&gt; | [optional] 
**expiration_month** | **int** | Card expiration month (1-12)&lt;div&gt;&lt;i&gt;Leave this empty when using SingleUseToken&lt;/i&gt;&lt;/div&gt; | [optional] 
**expiration_year** | **int** | Card expiration year (4 digits)&lt;div&gt;&lt;i&gt;Leave this empty when using SingleUseToken&lt;/i&gt;&lt;/div&gt; | [optional] 
**amount** | **float** | Transaction amount&lt;div&gt;&lt;i&gt;Leave this empty when using ParamJ &#x3D; CheckDetails&lt;/i&gt;&lt;/div&gt; | [optional] 
**payments_non_first_count** | **int** | Non-first payments count&lt;div&gt;&lt;i&gt;Leave this empty for non-payments transaction&lt;/i&gt;&lt;/div&gt; | [optional] 
**payments_first_amount** | **float** | First payment amount&lt;div&gt;&lt;i&gt;Leave this empty for non-payments transaction&lt;/i&gt;&lt;/div&gt; | [optional] 
**payments_non_first_amount** | **float** | Non-first payment amount&lt;div&gt;&lt;i&gt;Leave this empty for non-payments transaction&lt;/i&gt;&lt;/div&gt; | [optional] 
**auth_number** | **str** | Transaction authorization number | [optional] 
**cvv** | **str** | Card CVV/CVV2 | [optional] 
**track2** | **str** | Card Track2 | [optional] 
**citizen_id** | **str** | Israel Citizen ID / Passport Number | [optional] 
**currency** | [**Object**](Object.md) | Transaction currency&lt;div&gt;&lt;i&gt;Defaults to ILS&lt;/i&gt;&lt;/div&gt; | [optional] 
**language** | **str** | Transaction language&lt;div&gt;&lt;i&gt;Leave this empty to use the company default language&lt;/i&gt;&lt;/div&gt; | [optional] 
**unique_identifier** | **str** | Unique transaction identifier.&lt;div&gt;&lt;i&gt;This parameter can be used for preventing duplicate transactions&lt;/i&gt;&lt;/div&gt; | [optional] 
**merchant_number** | **str** | Shva merchant number (Terminal number).&lt;div&gt;&lt;i&gt;This parameter should only be used when multiple merchants are defined in the company.&lt;/i&gt;&lt;/div&gt; | [optional] 
**transaction_type** | [**Object**](Object.md) | Transaction type. This allows crediting or cancelling existing transaction.&lt;div&gt;&lt;i&gt;Defaults to Debit&lt;/i&gt;&lt;/div&gt; | [optional] 
**custom_data_1** | **str** | Custom user supplied data&lt;div&gt;&lt;i&gt;Supports up to 100 chars in each field&lt;/i&gt;&lt;/div&gt; | [optional] 
**custom_data_2** | **str** | Custom user supplied data&lt;div&gt;&lt;i&gt;Supports up to 100 chars in each field&lt;/i&gt;&lt;/div&gt; | [optional] 
**custom_data_3** | **str** | Custom user supplied data&lt;div&gt;&lt;i&gt;Supports up to 100 chars in each field&lt;/i&gt;&lt;/div&gt; | [optional] 
**custom_data_4** | **str** | Custom user supplied data&lt;div&gt;&lt;i&gt;Supports up to 100 chars in each field&lt;/i&gt;&lt;/div&gt; | [optional] 
**custom_data_5** | **str** | Custom user supplied data&lt;div&gt;&lt;i&gt;Supports up to 100 chars in each field&lt;/i&gt;&lt;/div&gt; | [optional] 
**multi_supplier_number** | **str** | Multi supplier number. | [optional] 
**credentials** | [**Object**](Object.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

