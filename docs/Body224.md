# Body224

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**Object**](Object.md) | Customer | 
**recurring_customer_item_id** | **int** | Recurring customer item identifier | 
**unit_price** | **float** | Unit price | [optional] 
**quantity** | **float** | Quantity&lt;div&gt;&lt;i&gt;Defaults to 1&lt;/i&gt;&lt;/div&gt; | [optional] 
**recurrence** | **int** | Number of pending recurring payments&lt;div&gt;&lt;i&gt;For instance, for a total of 1 year of monthly payments, specify 12  Setting this to 0 will result in continuous payments.  Please note this parameter cannot be used when the LastPaymentDate parameter is set.&lt;/i&gt;&lt;/div&gt; | [optional] 
**next_payment_date** | **datetime** | Next payment date | [optional] 
**last_payment_date** | **datetime** | Last payment date.&lt;div&gt;&lt;i&gt;Please note this parameter cannot be used when the Recurrence parameter is set.&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**Object**](Object.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

