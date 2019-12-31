# LetterByClickLetterByClickSendDocumentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_id** | **str** | Template background ID&lt;div&gt;&lt;i&gt;This field is supplied by Beeri  Defaults to the application settings.&lt;/i&gt;&lt;/div&gt; | [optional] 
**recipient_address_line1** | **str** | Recipient address line #1 | 
**recipient_address_line2** | **str** | Recipient address line #2 | [optional] 
**recipient_address_line3** | **str** | Recipient address line #3 | [optional] 
**recipient_city** | **str** | Recipient city | [optional] 
**recipient_post_code** | **str** | Recipient post code (zipcode) | [optional] 
**recipient_title** | **str** | Recipient title (name) | [optional] 
**pdf** | **str** | PDF file contents. Only A4 pages are supported.&lt;div&gt;&lt;i&gt;Shouldn&#39;t be specified when using the SendMultipartDocument API method&lt;/i&gt;&lt;/div&gt; | 
**sender_address** | **list[str]** | Specify up to 7 lines&lt;div&gt;&lt;i&gt;Defaults to the application settings.&lt;/i&gt;&lt;/div&gt; | [optional] 
**return_address** | **list[str]** | Return address, specify up to 7 lines.&lt;div&gt;&lt;i&gt;Defaults to the application settings.&lt;/i&gt;&lt;/div&gt; | [optional] 
**color** | **bool** | Indicates whether to print with Full Color (true) or black-white (false)&lt;div&gt;&lt;i&gt;Defaults to Black-White (False)&lt;/i&gt;&lt;/div&gt; | [optional] 
**double_sided** | **bool** | Indicates whether to print on both page sides (true) or single-sided (false)&lt;div&gt;&lt;i&gt;Defaults to Single-Sided (False)&lt;/i&gt;&lt;/div&gt; | [optional] 
**mail_type** | **str** | Mail type (Regular, Registered, Delivery Confirmation or Scanned Delivery Confirmation)&lt;div&gt;&lt;i&gt;Defaults to Regular&lt;/i&gt;&lt;/div&gt; | [optional] 
**live_mode** | **bool** | Indicated whether this is a live or a test API call.&lt;div&gt;&lt;i&gt;Defaults to test (False)&lt;/i&gt;&lt;/div&gt; | [optional] 
**auto_rotate** | **bool** | Indicated whether to auto rotate the document to portrait if needed.  Please note this incurs performance hit, and should only be used when necessary.&lt;div&gt;&lt;i&gt;Defaults to False&lt;/i&gt;&lt;/div&gt; | [optional] 
**credentials** | [**CoreAPICredentials**](CoreAPICredentials.md) | Company API credentials | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


