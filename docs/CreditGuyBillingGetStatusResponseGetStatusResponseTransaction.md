# CreditGuyBillingGetStatusResponseGetStatusResponseTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | OfficeGuy transaction identifier | [optional] 
**checkout_index** | **str** | Checkout index (Voucher number part 1) | [optional] 
**checkout_record_index** | **str** | Checkout record index (Voucher number part 2) | [optional] 
**reference_number** | **int** | Reference number (Deposit identifier) | [optional] 
**auth_number** | **str** | Authorization number | [optional] 
**unique_identifier** | **str** | Unique transaction identifier, as input during Load | [optional] 
**status** | [**AllOfCreditGuyBillingGetStatusResponseGetStatusResponseTransactionStatus**](AllOfCreditGuyBillingGetStatusResponseGetStatusResponseTransactionStatus.md) | Transaction status | [optional] 
**result_code** | **str** | Transaction Shva result code | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

