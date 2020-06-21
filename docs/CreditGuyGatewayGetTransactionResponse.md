# CreditGuyGatewayGetTransactionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Shva result code | [optional] 
**description** | **str** | Shva result description | [optional] 
**merchant_number** | **str** | Shva merchant number (Terminal number) | [optional] 
**auth_number** | **str** | Charge authorization number | [optional] 
**acquirer** | **int** | Card acquirer | [optional] 
**brand** | **int** | Card brand | [optional] 
**issuer** | **int** | Card issuer | [optional] 
**file_number** | **str** | Shva file number | [optional] 
**checkout_index** | **str** | Shva checkout index | [optional] 
**checkout_record_index** | **str** | Shva checkout record index | [optional] 
**reference_number** | **int** | Shva reference number | [optional] 
**card_token** | **str** | Card token | [optional] 
**card_fp_token** | **str** | Format preserved token | [optional] 
**card_pattern** | **str** | Card number pattern (including the last 4 digits) | [optional] 
**card_expiration** | **datetime** | Credit card expiration | [optional] 
**parameters** | **list[str]** | Card parameters, as specified in the card parameters folder. | [optional] 
**citizen_id** | **str** | Israeli Citizen ID / Passport Number | [optional] 
**result_record** | **str** | Full result record received from Shva | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

