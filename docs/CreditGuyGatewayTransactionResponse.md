# CreditGuyGatewayTransactionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Is valid transaction | [optional] 
**result_code** | **str** | Shva result code (000 is valid) | [optional] 
**result_description** | **str** | Shva result description | [optional] 
**transaction_id** | **int** | CreditGuy transaction identifier | [optional] 
**file_number** | **str** | Shva file number | [optional] 
**checkout_index** | **str** | Shva checkout index | [optional] 
**checkout_record_index** | **str** | Shva checkout record index | [optional] 
**acquirer** | **int** | Card acquirer | [optional] 
**brand** | **int** | Card brand | [optional] 
**issuer** | **int** | Card issuer | [optional] 
**auth_number** | **str** | Charge authorization number | [optional] 
**card_token** | **str** | Card token, this field may be stored on non-pci compliant systems | [optional] 
**expiration_month** | **int** | Card expiration month (1-12), this field may be stored on non-pci compliant systems | [optional] 
**expiration_year** | **int** | Card expiration year (4 digits), this field may be stored on non-pci compliant systems | [optional] 
**citizen_id** | **str** | Israel Citizen ID / Passport Number, this field may be stored on non pci-compliant systems | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

