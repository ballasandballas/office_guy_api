# BillingTypedRecurringItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration_days** | **int** | Recurring duration/interval in days | [optional] 
**duration_months** | **int** | Recurring duration/interval in months | [optional] 
**id** | **int** | OfficeGuy identifier | [optional] 
**name** | **str** | Item name | [optional] 
**price** | **float** | Item price (for single unit) | [optional] 
**currency** | [**AllOfBillingTypedRecurringItemCurrency**](AllOfBillingTypedRecurringItemCurrency.md) | Price currency&lt;div&gt;&lt;i&gt;Leave empty for company default&lt;/i&gt;&lt;/div&gt; | [optional] 
**cost** | **float** | Item cost (for single unit) | [optional] 
**external_identifier** | **str** | Customer external identifier | [optional] 
**search_mode** | [**AllOfBillingTypedRecurringItemSearchMode**](AllOfBillingTypedRecurringItemSearchMode.md) |  | [optional] 
**properties** | **dict(str, object)** | Entity fields | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

