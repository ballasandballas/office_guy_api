# Body82

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**Object**](Object.md) | Transaction type | 
**amount** | **float** | Transaction amount | [optional] 
**payments_non_first_count** | **int** | Non-first payments count&lt;div&gt;&lt;i&gt;Leave this empty for non-payments transaction&lt;/i&gt;&lt;/div&gt; | [optional] 
**payments_first_amount** | **float** | First payment amount&lt;div&gt;&lt;i&gt;Leave this empty for non-payments transaction&lt;/i&gt;&lt;/div&gt; | [optional] 
**payments_non_first_amount** | **float** | Non-first payment amount&lt;div&gt;&lt;i&gt;Leave this empty for non-payments transaction&lt;/i&gt;&lt;/div&gt; | [optional] 
**currency** | [**Object**](Object.md) | Transaction currency&lt;div&gt;&lt;i&gt;Defaults to ILS&lt;/i&gt;&lt;/div&gt; | [optional] 
**identifier** | **str** | Transaction identifier.&lt;div&gt;&lt;i&gt;This parameter will be returned during redirect.&lt;/i&gt;&lt;/div&gt; | [optional] 
**merchant_number** | **str** | Shva merchant number (Terminal number).&lt;div&gt;&lt;i&gt;This parameter should only be used when multiple merchants are defined in the company.&lt;/i&gt;&lt;/div&gt; | [optional] 
**redirect_url** | **str** | Redirect URL&lt;div&gt;&lt;i&gt;Leave this empty to use the default RedirectURL&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**Object**](Object.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

