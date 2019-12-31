# BillingTypedPaymentMethod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**customer_id** | **int** |  | [optional] 
**credit_card_number** | **str** | Credit card full number&lt;div&gt;&lt;i&gt;Required for credit card&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_last_digits** | **str** | Credit card last 4 digits&lt;div&gt;&lt;i&gt;Shouldn&#39;t be input by API caller&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_expiration_month** | **int** | Credit card expiration month (1-2 digits)&lt;div&gt;&lt;i&gt;Required for credit card&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_expiration_year** | **int** | Credit card expiration year (4 digits)&lt;div&gt;&lt;i&gt;Required for credit card&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_cvv** | **str** | Credit card CVV/CVV2&lt;div&gt;&lt;i&gt;Required when CVV is required by credit company&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_track2** | **str** | Credit card Track2 | [optional] 
**credit_card_citizen_id** | **str** | Credit card owner Israel Citizen ID / Passport Number&lt;div&gt;&lt;i&gt;Required when Citizen ID is required by credit company&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_card_mask** | **str** | Credit card mask&lt;div&gt;&lt;i&gt;Shouldn&#39;t be input by API caller&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_token** | **str** | Credit card token | [optional] 
**type** | **str** | Payment method type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


