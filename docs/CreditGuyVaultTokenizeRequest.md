# CreditGuyVaultTokenizeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**get_format_preserving** | **bool** | Should tokenize method also return format preserved token, or only Guid token&lt;div&gt;&lt;i&gt;Defaults to False&lt;/i&gt;&lt;/div&gt; | [optional] 
**card_number** | **str** | Full card number to tokenize | 
**force_format_preserving_token** | **str** | Forced format preserving token  This can be useful when migrating from another credit card gateway to OfficeGuy.  Please note the format preserving token should be a RANDOM identifier, which can&#39;t be reverse engineered into the card number (encoding/encrypting etc. isn&#39;t supported). | 
**credentials** | [**CoreAPICredentials**](CoreAPICredentials.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


