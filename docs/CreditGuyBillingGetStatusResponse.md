# CreditGuyBillingGetStatusResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transmit_pending** | **int** | Transactions pending transmit | [optional] 
**transmit_failed** | **int** | Transactions failed on Shva | [optional] 
**deposit_pending** | **int** | Transactions successfully deposited on Shva | [optional] 
**deposit_failed** | **int** | Transactions failed while depositing on Shva | [optional] 
**deposit_finished** | **int** | Transactions deposited successfully on Shva | [optional] 
**finished** | **bool** | Indication whether the billing process has finished | [optional] 
**transactions** | [**list[CreditGuyBillingGetStatusResponseGetStatusResponseTransaction]**](CreditGuyBillingGetStatusResponseGetStatusResponseTransaction.md) | Detailed list of transactions (Returned when ListTransactions &#x3D; true) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


