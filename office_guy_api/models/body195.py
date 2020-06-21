# coding: utf-8

"""
    OfficeGuy API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2020-06-20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Body195(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'customer': 'Object',
        'payment_method': 'Object',
        'single_use_token': 'str',
        'credit_card_auth_number': 'str',
        'items': 'list[BillingTypedChargeItem]',
        'payments_count': 'int',
        'payments_first_amount': 'float',
        'payments_non_first_amount': 'float',
        'update_customer_by_email': 'bool',
        'update_customer_by_email_attach_document': 'bool',
        'update_customer_by_email_language': 'Object',
        'send_document_by_email': 'bool',
        'send_document_by_email_language': 'Object',
        'document_language': 'Object',
        'document_description': 'str',
        'vat_included': 'bool',
        'vat_rate': 'float',
        'authorise_only': 'bool',
        'draft_document': 'bool',
        'document_type': 'Object',
        'support_credit': 'bool',
        'merchant_number': 'str',
        'send_copy_to_organization': 'bool',
        'credentials': 'Object'
    }
    if hasattr(BillingPaymentsChargeRequest, "swagger_types"):
        swagger_types.update(BillingPaymentsChargeRequest.swagger_types)

    attribute_map = {
        'customer': 'Customer',
        'payment_method': 'PaymentMethod',
        'single_use_token': 'SingleUseToken',
        'credit_card_auth_number': 'CreditCardAuthNumber',
        'items': 'Items',
        'payments_count': 'Payments_Count',
        'payments_first_amount': 'Payments_FirstAmount',
        'payments_non_first_amount': 'Payments_NonFirstAmount',
        'update_customer_by_email': 'UpdateCustomerByEmail',
        'update_customer_by_email_attach_document': 'UpdateCustomerByEmail_AttachDocument',
        'update_customer_by_email_language': 'UpdateCustomerByEmail_Language',
        'send_document_by_email': 'SendDocumentByEmail',
        'send_document_by_email_language': 'SendDocumentByEmail_Language',
        'document_language': 'DocumentLanguage',
        'document_description': 'DocumentDescription',
        'vat_included': 'VATIncluded',
        'vat_rate': 'VATRate',
        'authorise_only': 'AuthoriseOnly',
        'draft_document': 'DraftDocument',
        'document_type': 'DocumentType',
        'support_credit': 'SupportCredit',
        'merchant_number': 'MerchantNumber',
        'send_copy_to_organization': 'SendCopyToOrganization',
        'credentials': 'Credentials'
    }
    if hasattr(BillingPaymentsChargeRequest, "attribute_map"):
        attribute_map.update(BillingPaymentsChargeRequest.attribute_map)

    def __init__(self, customer=None, payment_method=None, single_use_token=None, credit_card_auth_number=None, items=None, payments_count=None, payments_first_amount=None, payments_non_first_amount=None, update_customer_by_email=None, update_customer_by_email_attach_document=None, update_customer_by_email_language=None, send_document_by_email=None, send_document_by_email_language=None, document_language=None, document_description=None, vat_included=None, vat_rate=None, authorise_only=None, draft_document=None, document_type=None, support_credit=None, merchant_number=None, send_copy_to_organization=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body195 - a model defined in Swagger"""  # noqa: E501
        self._customer = None
        self._payment_method = None
        self._single_use_token = None
        self._credit_card_auth_number = None
        self._items = None
        self._payments_count = None
        self._payments_first_amount = None
        self._payments_non_first_amount = None
        self._update_customer_by_email = None
        self._update_customer_by_email_attach_document = None
        self._update_customer_by_email_language = None
        self._send_document_by_email = None
        self._send_document_by_email_language = None
        self._document_language = None
        self._document_description = None
        self._vat_included = None
        self._vat_rate = None
        self._authorise_only = None
        self._draft_document = None
        self._document_type = None
        self._support_credit = None
        self._merchant_number = None
        self._send_copy_to_organization = None
        self._credentials = None
        self.discriminator = None
        self.customer = customer
        if payment_method is not None:
            self.payment_method = payment_method
        if single_use_token is not None:
            self.single_use_token = single_use_token
        if credit_card_auth_number is not None:
            self.credit_card_auth_number = credit_card_auth_number
        self.items = items
        if payments_count is not None:
            self.payments_count = payments_count
        if payments_first_amount is not None:
            self.payments_first_amount = payments_first_amount
        if payments_non_first_amount is not None:
            self.payments_non_first_amount = payments_non_first_amount
        if update_customer_by_email is not None:
            self.update_customer_by_email = update_customer_by_email
        if update_customer_by_email_attach_document is not None:
            self.update_customer_by_email_attach_document = update_customer_by_email_attach_document
        if update_customer_by_email_language is not None:
            self.update_customer_by_email_language = update_customer_by_email_language
        if send_document_by_email is not None:
            self.send_document_by_email = send_document_by_email
        if send_document_by_email_language is not None:
            self.send_document_by_email_language = send_document_by_email_language
        if document_language is not None:
            self.document_language = document_language
        if document_description is not None:
            self.document_description = document_description
        if vat_included is not None:
            self.vat_included = vat_included
        if vat_rate is not None:
            self.vat_rate = vat_rate
        if authorise_only is not None:
            self.authorise_only = authorise_only
        if draft_document is not None:
            self.draft_document = draft_document
        if document_type is not None:
            self.document_type = document_type
        if support_credit is not None:
            self.support_credit = support_credit
        if merchant_number is not None:
            self.merchant_number = merchant_number
        if send_copy_to_organization is not None:
            self.send_copy_to_organization = send_copy_to_organization
        self.credentials = credentials
        BillingPaymentsChargeRequest.__init__(self, *args, **kwargs)

    @property
    def customer(self):
        """Gets the customer of this Body195.  # noqa: E501

        Customer  # noqa: E501

        :return: The customer of this Body195.  # noqa: E501
        :rtype: Object
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Body195.

        Customer  # noqa: E501

        :param customer: The customer of this Body195.  # noqa: E501
        :type: Object
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def payment_method(self):
        """Gets the payment_method of this Body195.  # noqa: E501

        Payment method details<div><i>Leave this empty to use the customer payment method, or when using the SingleUseToken</i></div>  # noqa: E501

        :return: The payment_method of this Body195.  # noqa: E501
        :rtype: Object
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Body195.

        Payment method details<div><i>Leave this empty to use the customer payment method, or when using the SingleUseToken</i></div>  # noqa: E501

        :param payment_method: The payment_method of this Body195.  # noqa: E501
        :type: Object
        """

        self._payment_method = payment_method

    @property
    def single_use_token(self):
        """Gets the single_use_token of this Body195.  # noqa: E501

        Single use token, for all payment details (CardNumber, Expiration, CVV, CitizenID).<div><i>Used primarily by the Payments JavaScript API.</i></div>  # noqa: E501

        :return: The single_use_token of this Body195.  # noqa: E501
        :rtype: str
        """
        return self._single_use_token

    @single_use_token.setter
    def single_use_token(self, single_use_token):
        """Sets the single_use_token of this Body195.

        Single use token, for all payment details (CardNumber, Expiration, CVV, CitizenID).<div><i>Used primarily by the Payments JavaScript API.</i></div>  # noqa: E501

        :param single_use_token: The single_use_token of this Body195.  # noqa: E501
        :type: str
        """

        self._single_use_token = single_use_token

    @property
    def credit_card_auth_number(self):
        """Gets the credit_card_auth_number of this Body195.  # noqa: E501

        Transaction authorization number, as received from a previous Gateway Transaction  # noqa: E501

        :return: The credit_card_auth_number of this Body195.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_auth_number

    @credit_card_auth_number.setter
    def credit_card_auth_number(self, credit_card_auth_number):
        """Sets the credit_card_auth_number of this Body195.

        Transaction authorization number, as received from a previous Gateway Transaction  # noqa: E501

        :param credit_card_auth_number: The credit_card_auth_number of this Body195.  # noqa: E501
        :type: str
        """

        self._credit_card_auth_number = credit_card_auth_number

    @property
    def items(self):
        """Gets the items of this Body195.  # noqa: E501

        Items  # noqa: E501

        :return: The items of this Body195.  # noqa: E501
        :rtype: list[BillingTypedChargeItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Body195.

        Items  # noqa: E501

        :param items: The items of this Body195.  # noqa: E501
        :type: list[BillingTypedChargeItem]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def payments_count(self):
        """Gets the payments_count of this Body195.  # noqa: E501

        Payments count<div><i>Leave this empty to disable payments</i></div>  # noqa: E501

        :return: The payments_count of this Body195.  # noqa: E501
        :rtype: int
        """
        return self._payments_count

    @payments_count.setter
    def payments_count(self, payments_count):
        """Sets the payments_count of this Body195.

        Payments count<div><i>Leave this empty to disable payments</i></div>  # noqa: E501

        :param payments_count: The payments_count of this Body195.  # noqa: E501
        :type: int
        """

        self._payments_count = payments_count

    @property
    def payments_first_amount(self):
        """Gets the payments_first_amount of this Body195.  # noqa: E501

        First payment amount<div><i>Leave this empty to disable payments / automatic payments calculating</i></div>  # noqa: E501

        :return: The payments_first_amount of this Body195.  # noqa: E501
        :rtype: float
        """
        return self._payments_first_amount

    @payments_first_amount.setter
    def payments_first_amount(self, payments_first_amount):
        """Sets the payments_first_amount of this Body195.

        First payment amount<div><i>Leave this empty to disable payments / automatic payments calculating</i></div>  # noqa: E501

        :param payments_first_amount: The payments_first_amount of this Body195.  # noqa: E501
        :type: float
        """

        self._payments_first_amount = payments_first_amount

    @property
    def payments_non_first_amount(self):
        """Gets the payments_non_first_amount of this Body195.  # noqa: E501

        Non-first payment amount<div><i>Leave this empty to disable payments / automatic payments calculating</i></div>  # noqa: E501

        :return: The payments_non_first_amount of this Body195.  # noqa: E501
        :rtype: float
        """
        return self._payments_non_first_amount

    @payments_non_first_amount.setter
    def payments_non_first_amount(self, payments_non_first_amount):
        """Sets the payments_non_first_amount of this Body195.

        Non-first payment amount<div><i>Leave this empty to disable payments / automatic payments calculating</i></div>  # noqa: E501

        :param payments_non_first_amount: The payments_non_first_amount of this Body195.  # noqa: E501
        :type: float
        """

        self._payments_non_first_amount = payments_non_first_amount

    @property
    def update_customer_by_email(self):
        """Gets the update_customer_by_email of this Body195.  # noqa: E501

        Update customer by email (notification email, with invoice/receipt download link)<div><i>Leave this empty to disable email sending feature</i></div>  # noqa: E501

        :return: The update_customer_by_email of this Body195.  # noqa: E501
        :rtype: bool
        """
        return self._update_customer_by_email

    @update_customer_by_email.setter
    def update_customer_by_email(self, update_customer_by_email):
        """Sets the update_customer_by_email of this Body195.

        Update customer by email (notification email, with invoice/receipt download link)<div><i>Leave this empty to disable email sending feature</i></div>  # noqa: E501

        :param update_customer_by_email: The update_customer_by_email of this Body195.  # noqa: E501
        :type: bool
        """

        self._update_customer_by_email = update_customer_by_email

    @property
    def update_customer_by_email_attach_document(self):
        """Gets the update_customer_by_email_attach_document of this Body195.  # noqa: E501

        Attach invoice/receipt to email<div><i>Defaults to False</i></div>  # noqa: E501

        :return: The update_customer_by_email_attach_document of this Body195.  # noqa: E501
        :rtype: bool
        """
        return self._update_customer_by_email_attach_document

    @update_customer_by_email_attach_document.setter
    def update_customer_by_email_attach_document(self, update_customer_by_email_attach_document):
        """Sets the update_customer_by_email_attach_document of this Body195.

        Attach invoice/receipt to email<div><i>Defaults to False</i></div>  # noqa: E501

        :param update_customer_by_email_attach_document: The update_customer_by_email_attach_document of this Body195.  # noqa: E501
        :type: bool
        """

        self._update_customer_by_email_attach_document = update_customer_by_email_attach_document

    @property
    def update_customer_by_email_language(self):
        """Gets the update_customer_by_email_language of this Body195.  # noqa: E501

        Update email language<div><i>Defaults to the company language</i></div>  # noqa: E501

        :return: The update_customer_by_email_language of this Body195.  # noqa: E501
        :rtype: Object
        """
        return self._update_customer_by_email_language

    @update_customer_by_email_language.setter
    def update_customer_by_email_language(self, update_customer_by_email_language):
        """Sets the update_customer_by_email_language of this Body195.

        Update email language<div><i>Defaults to the company language</i></div>  # noqa: E501

        :param update_customer_by_email_language: The update_customer_by_email_language of this Body195.  # noqa: E501
        :type: Object
        """

        self._update_customer_by_email_language = update_customer_by_email_language

    @property
    def send_document_by_email(self):
        """Gets the send_document_by_email of this Body195.  # noqa: E501

        Send invoice/receipt by email  # noqa: E501

        :return: The send_document_by_email of this Body195.  # noqa: E501
        :rtype: bool
        """
        return self._send_document_by_email

    @send_document_by_email.setter
    def send_document_by_email(self, send_document_by_email):
        """Sets the send_document_by_email of this Body195.

        Send invoice/receipt by email  # noqa: E501

        :param send_document_by_email: The send_document_by_email of this Body195.  # noqa: E501
        :type: bool
        """

        self._send_document_by_email = send_document_by_email

    @property
    def send_document_by_email_language(self):
        """Gets the send_document_by_email_language of this Body195.  # noqa: E501

        Send document email language<div><i>Defaults to the company language</i></div>  # noqa: E501

        :return: The send_document_by_email_language of this Body195.  # noqa: E501
        :rtype: Object
        """
        return self._send_document_by_email_language

    @send_document_by_email_language.setter
    def send_document_by_email_language(self, send_document_by_email_language):
        """Sets the send_document_by_email_language of this Body195.

        Send document email language<div><i>Defaults to the company language</i></div>  # noqa: E501

        :param send_document_by_email_language: The send_document_by_email_language of this Body195.  # noqa: E501
        :type: Object
        """

        self._send_document_by_email_language = send_document_by_email_language

    @property
    def document_language(self):
        """Gets the document_language of this Body195.  # noqa: E501

        Document language<div><i>Defaults to the company language</i></div>  # noqa: E501

        :return: The document_language of this Body195.  # noqa: E501
        :rtype: Object
        """
        return self._document_language

    @document_language.setter
    def document_language(self, document_language):
        """Sets the document_language of this Body195.

        Document language<div><i>Defaults to the company language</i></div>  # noqa: E501

        :param document_language: The document_language of this Body195.  # noqa: E501
        :type: Object
        """

        self._document_language = document_language

    @property
    def document_description(self):
        """Gets the document_description of this Body195.  # noqa: E501

        Document description (the description is printed on the document)  # noqa: E501

        :return: The document_description of this Body195.  # noqa: E501
        :rtype: str
        """
        return self._document_description

    @document_description.setter
    def document_description(self, document_description):
        """Sets the document_description of this Body195.

        Document description (the description is printed on the document)  # noqa: E501

        :param document_description: The document_description of this Body195.  # noqa: E501
        :type: str
        """

        self._document_description = document_description

    @property
    def vat_included(self):
        """Gets the vat_included of this Body195.  # noqa: E501

        Is VAT included in the prices?<div><i>Defaults to false</i></div>  # noqa: E501

        :return: The vat_included of this Body195.  # noqa: E501
        :rtype: bool
        """
        return self._vat_included

    @vat_included.setter
    def vat_included(self, vat_included):
        """Sets the vat_included of this Body195.

        Is VAT included in the prices?<div><i>Defaults to false</i></div>  # noqa: E501

        :param vat_included: The vat_included of this Body195.  # noqa: E501
        :type: bool
        """

        self._vat_included = vat_included

    @property
    def vat_rate(self):
        """Gets the vat_rate of this Body195.  # noqa: E501

        Document VAT Rate<div><i>Leave empty for company default.  Relevant for items only.</i></div>  # noqa: E501

        :return: The vat_rate of this Body195.  # noqa: E501
        :rtype: float
        """
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, vat_rate):
        """Sets the vat_rate of this Body195.

        Document VAT Rate<div><i>Leave empty for company default.  Relevant for items only.</i></div>  # noqa: E501

        :param vat_rate: The vat_rate of this Body195.  # noqa: E501
        :type: float
        """

        self._vat_rate = vat_rate

    @property
    def authorise_only(self):
        """Gets the authorise_only of this Body195.  # noqa: E501

        Should the transaction be committed, or authorized only.<div><i>Leave empty for \"False\" (Auto-Commit).  This field could be used for testing the Charge action easily.  Please note, when using AuthoriseOnly, documents will be issued as \"Draft\".</i></div>  # noqa: E501

        :return: The authorise_only of this Body195.  # noqa: E501
        :rtype: bool
        """
        return self._authorise_only

    @authorise_only.setter
    def authorise_only(self, authorise_only):
        """Sets the authorise_only of this Body195.

        Should the transaction be committed, or authorized only.<div><i>Leave empty for \"False\" (Auto-Commit).  This field could be used for testing the Charge action easily.  Please note, when using AuthoriseOnly, documents will be issued as \"Draft\".</i></div>  # noqa: E501

        :param authorise_only: The authorise_only of this Body195.  # noqa: E501
        :type: bool
        """

        self._authorise_only = authorise_only

    @property
    def draft_document(self):
        """Gets the draft_document of this Body195.  # noqa: E501

        Create draft document?<div><i>Leave empty to use the application setting.  Please note, when using AuthoriseOnly, documents will always be issued as \"Draft\".</i></div>  # noqa: E501

        :return: The draft_document of this Body195.  # noqa: E501
        :rtype: bool
        """
        return self._draft_document

    @draft_document.setter
    def draft_document(self, draft_document):
        """Sets the draft_document of this Body195.

        Create draft document?<div><i>Leave empty to use the application setting.  Please note, when using AuthoriseOnly, documents will always be issued as \"Draft\".</i></div>  # noqa: E501

        :param draft_document: The draft_document of this Body195.  # noqa: E501
        :type: bool
        """

        self._draft_document = draft_document

    @property
    def document_type(self):
        """Gets the document_type of this Body195.  # noqa: E501

        Create document type<div><i>Leave empty for default</i></div>  # noqa: E501

        :return: The document_type of this Body195.  # noqa: E501
        :rtype: Object
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this Body195.

        Create document type<div><i>Leave empty for default</i></div>  # noqa: E501

        :param document_type: The document_type of this Body195.  # noqa: E501
        :type: Object
        """

        self._document_type = document_type

    @property
    def support_credit(self):
        """Gets the support_credit of this Body195.  # noqa: E501

        Allow credit instead of charge (debit), in case the total is less than 0?<div><i>Defaults to false</i></div>  # noqa: E501

        :return: The support_credit of this Body195.  # noqa: E501
        :rtype: bool
        """
        return self._support_credit

    @support_credit.setter
    def support_credit(self, support_credit):
        """Sets the support_credit of this Body195.

        Allow credit instead of charge (debit), in case the total is less than 0?<div><i>Defaults to false</i></div>  # noqa: E501

        :param support_credit: The support_credit of this Body195.  # noqa: E501
        :type: bool
        """

        self._support_credit = support_credit

    @property
    def merchant_number(self):
        """Gets the merchant_number of this Body195.  # noqa: E501

        Shva merchant number (Terminal number).<div><i>This parameter should only be used when multiple merchants are defined in the company.</i></div>  # noqa: E501

        :return: The merchant_number of this Body195.  # noqa: E501
        :rtype: str
        """
        return self._merchant_number

    @merchant_number.setter
    def merchant_number(self, merchant_number):
        """Sets the merchant_number of this Body195.

        Shva merchant number (Terminal number).<div><i>This parameter should only be used when multiple merchants are defined in the company.</i></div>  # noqa: E501

        :param merchant_number: The merchant_number of this Body195.  # noqa: E501
        :type: str
        """

        self._merchant_number = merchant_number

    @property
    def send_copy_to_organization(self):
        """Gets the send_copy_to_organization of this Body195.  # noqa: E501

        Send email to the organization as well.  Defaults to the accounting application settings.<div><i>Relevant when using either UpdateCustomerByEmail or SendDocumentByEmail.</i></div>  # noqa: E501

        :return: The send_copy_to_organization of this Body195.  # noqa: E501
        :rtype: bool
        """
        return self._send_copy_to_organization

    @send_copy_to_organization.setter
    def send_copy_to_organization(self, send_copy_to_organization):
        """Sets the send_copy_to_organization of this Body195.

        Send email to the organization as well.  Defaults to the accounting application settings.<div><i>Relevant when using either UpdateCustomerByEmail or SendDocumentByEmail.</i></div>  # noqa: E501

        :param send_copy_to_organization: The send_copy_to_organization of this Body195.  # noqa: E501
        :type: bool
        """

        self._send_copy_to_organization = send_copy_to_organization

    @property
    def credentials(self):
        """Gets the credentials of this Body195.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body195.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body195.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body195.  # noqa: E501
        :type: Object
        """
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Body195, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Body195):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other