# AllOfBillingPaymentsGetResponsePayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Payment identifier | [optional] 
**customer_id** | **int** | Customer identifier | [optional] 
**_date** | **datetime** | Payment date | [optional] 
**valid_payment** | **bool** | Indicates if the payment is valid | [optional] 
**status** | **str** | Payment status | [optional] 
**status_description** | **str** | Payment status description | [optional] 
**amount** | **float** | Payment amount | [optional] 
**payment_method** | [**Object**](Object.md) | Payment method details | [optional] 
**auth_number** | **str** | Authorization number | [optional] 
**recurring_customer_item_i_ds** | **list[int]** | Relevant only for payments originating from recurring payments | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

