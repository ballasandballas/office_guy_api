# WebsiteCompaniesCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**WebsiteTypedCompany**](WebsiteTypedCompany.md) | Company details | 
**user** | [**WebsiteTypedUser**](WebsiteTypedUser.md) | Company owner&lt;div&gt;&lt;i&gt;Leave empty to set calling company owners as owners&lt;/i&gt;&lt;/div&gt; | [optional] 
**applications** | **list[str]** | List of applications to be installed on the created company.&lt;div&gt;&lt;i&gt;Please note installing applications might incur additional charges.&lt;/i&gt;&lt;/div&gt; | [optional] 
**application_additions** | [**list[WebsiteTypedApplicationAddition]**](WebsiteTypedApplicationAddition.md) | List of applications additions to be installed on the created company.&lt;div&gt;&lt;i&gt;Please note this will incur additional charges.&lt;/i&gt;&lt;/div&gt; | [optional] 
**hide_from_companies_list** | **bool** | Allows hiding the created company from the user companies list&lt;div&gt;&lt;i&gt;Defaults to False&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**CoreAPICredentials**](CoreAPICredentials.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


