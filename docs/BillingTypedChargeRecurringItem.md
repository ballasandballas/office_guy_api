# BillingTypedChargeRecurringItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**AllOfBillingTypedChargeRecurringItemItem**](AllOfBillingTypedChargeRecurringItemItem.md) | Item | 
**quantity** | **float** | Quantity&lt;div&gt;&lt;i&gt;Defaults to 1&lt;/i&gt;&lt;/div&gt; | [optional] 
**unit_price** | **float** | Single unit price in payment currency | [optional] 
**currency** | [**AllOfBillingTypedChargeRecurringItemCurrency**](AllOfBillingTypedChargeRecurringItemCurrency.md) | Price currency&lt;div&gt;&lt;i&gt;Leave empty for company default currency&lt;/i&gt;&lt;/div&gt; | [optional] 
**date_start** | **datetime** | First payment date&lt;div&gt;&lt;i&gt;Defaults to current date&lt;/i&gt;&lt;/div&gt; | [optional] 
**description** | **str** | Recurring record description | [optional] 
**duration_days** | **int** | Recurring duration/interval in days&lt;div&gt;&lt;i&gt;For instance, for monthly payments, specify 0. For weekly payments, specify 7.&lt;/i&gt;&lt;/div&gt; | [optional] 
**duration_months** | **int** | Recurring duration/interval in months&lt;div&gt;&lt;i&gt;For instance, for monthly payments, specify 1&lt;/i&gt;&lt;/div&gt; | [optional] 
**recurrence** | **int** | Number of recurring payments&lt;div&gt;&lt;i&gt;For instance, for 1 year of monthly payments, specify 12.  Setting this to null or 0 will result in continuous payments&lt;/i&gt;&lt;/div&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

