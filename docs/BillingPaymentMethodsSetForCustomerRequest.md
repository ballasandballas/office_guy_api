# BillingPaymentMethodsSetForCustomerRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**AccountingTypedCustomer**](AccountingTypedCustomer.md) | Customer details | 
**payment_method** | [**BillingTypedPaymentMethod**](BillingTypedPaymentMethod.md) | Payment method | [optional] 
**single_use_token** | **str** | Single use token, for all payment details (CardNumber, Expiration, CVV, CitizenID).&lt;div&gt;&lt;i&gt;Used primarily by the Payments JavaScript API.&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**CoreAPICredentials**](CoreAPICredentials.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


