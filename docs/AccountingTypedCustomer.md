# AccountingTypedCustomer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_identifier** | **str** | Customer external identifier.&lt;div&gt;&lt;i&gt;External identifier from calling application.  Optional field&lt;/i&gt;&lt;/div&gt; | [optional] 
**no_vat** | **bool** | NoVAT indication&lt;div&gt;&lt;i&gt;Set to true for VAT exempt customers  Defaults to False&lt;/i&gt;&lt;/div&gt; | [optional] 
**search_mode** | [**AllOfAccountingTypedCustomerSearchMode**](AllOfAccountingTypedCustomerSearchMode.md) | Customer searching mode&lt;div&gt;&lt;i&gt;Defaults to None&lt;/i&gt;&lt;/div&gt; | [optional] 
**name** | **str** | Customer full name (or company name)&lt;div&gt;&lt;i&gt;Required for creating new customer  (Leave empty to search by other fields)&lt;/i&gt;&lt;/div&gt; | [optional] 
**phone** | **str** | Customer phone number&lt;div&gt;&lt;i&gt;Optional field&lt;/i&gt;&lt;/div&gt; | [optional] 
**email_address** | **str** | Customer email address&lt;div&gt;&lt;i&gt;Optional field&lt;/i&gt;&lt;/div&gt; | [optional] 
**city** | **str** | Customer city&lt;div&gt;&lt;i&gt;Optional field&lt;/i&gt;&lt;/div&gt; | [optional] 
**address** | **str** | Customer address&lt;div&gt;&lt;i&gt;Optional field&lt;/i&gt;&lt;/div&gt; | [optional] 
**zip_code** | **str** | Customer ZipCode&lt;div&gt;&lt;i&gt;Optional field&lt;/i&gt;&lt;/div&gt; | [optional] 
**company_number** | **str** | Customer registered company number (VAT number)&lt;div&gt;&lt;i&gt;Optional field&lt;/i&gt;&lt;/div&gt; | [optional] 
**id** | **int** | OfficeGuy identifier&lt;div&gt;&lt;i&gt;Leave empty to create a new entity or search by other fields when applicable&lt;/i&gt;&lt;/div&gt; | [optional] 
**folder** | **str** | Folder identifier.&lt;div&gt;&lt;i&gt;Can be either application folder name, or FolderID.&lt;/i&gt;&lt;/div&gt; | [optional] 
**properties** | **dict(str, object)** | Entity fields | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

