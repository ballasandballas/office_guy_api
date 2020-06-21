# AllOfBillingPaymentMethodsSetForCustomerResponsePaymentMethod

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**customer_id** | **int** |  | [optional] 
**credit_card_number** | **str** | Credit card full number&lt;div&gt;&lt;i&gt;Required for credit card&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_last_digits** | **str** | Credit card last 4 digits&lt;div&gt;&lt;i&gt;Shouldn&#x27;t be input by API caller&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_expiration_month** | **int** | Credit card expiration month (1-2 digits)&lt;div&gt;&lt;i&gt;Required for credit card&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_expiration_year** | **int** | Credit card expiration year (4 digits)&lt;div&gt;&lt;i&gt;Required for credit card&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_cvv** | **str** | Credit card CVV/CVV2&lt;div&gt;&lt;i&gt;Required when CVV is required by credit company&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_track2** | **str** | Credit card Track2 | [optional] 
**credit_card_citizen_id** | **str** | Credit card owner Israel Citizen ID / Passport Number&lt;div&gt;&lt;i&gt;Required when Citizen ID is required by credit company&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_card_mask** | **str** | Credit card mask&lt;div&gt;&lt;i&gt;Shouldn&#x27;t be input by API caller&lt;/i&gt;&lt;/div&gt; | [optional] 
**credit_card_token** | **str** | Credit card token | [optional] 
**direct_debit_bank** | **int** | Direct debit bank number&lt;div&gt;&lt;i&gt;For instance, 12 indicates Bank Hapoalim.&lt;/i&gt;&lt;/div&gt; | [optional] 
**direct_debit_branch** | **int** | Direct debit bank branch number | [optional] 
**direct_debit_account** | **int** | Direct debit bank account number | [optional] 
**direct_debit_expiration_date** | **datetime** | Direct debit expiration date | [optional] 
**direct_debit_maximum_amount** | **int** | Direct debit maximum charge amount | [optional] 
**type** | [**Object**](Object.md) | Payment method type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

