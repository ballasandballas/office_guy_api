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


class Body207(object):
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
        'items': 'list[BillingTypedChargeItem]',
        'vat_included': 'bool',
        'document_type': 'Object',
        'redirect_url': 'str',
        'external_identifier': 'str',
        'maximum_payments': 'int',
        'send_update_by_email_address': 'str',
        'expiration_hours': 'int',
        'theme': 'Object',
        'language': 'Object',
        'header': 'str',
        'update_organization_on_success': 'bool',
        'update_organization_on_failure': 'bool',
        'update_customer_on_success': 'bool',
        'document_description': 'str',
        'credentials': 'Object'
    }
    if hasattr(BillingPaymentsBeginRedirectRequest, "swagger_types"):
        swagger_types.update(BillingPaymentsBeginRedirectRequest.swagger_types)

    attribute_map = {
        'customer': 'Customer',
        'items': 'Items',
        'vat_included': 'VATIncluded',
        'document_type': 'DocumentType',
        'redirect_url': 'RedirectURL',
        'external_identifier': 'ExternalIdentifier',
        'maximum_payments': 'MaximumPayments',
        'send_update_by_email_address': 'SendUpdateByEmailAddress',
        'expiration_hours': 'ExpirationHours',
        'theme': 'Theme',
        'language': 'Language',
        'header': 'Header',
        'update_organization_on_success': 'UpdateOrganizationOnSuccess',
        'update_organization_on_failure': 'UpdateOrganizationOnFailure',
        'update_customer_on_success': 'UpdateCustomerOnSuccess',
        'document_description': 'DocumentDescription',
        'credentials': 'Credentials'
    }
    if hasattr(BillingPaymentsBeginRedirectRequest, "attribute_map"):
        attribute_map.update(BillingPaymentsBeginRedirectRequest.attribute_map)

    def __init__(self, customer=None, items=None, vat_included=None, document_type=None, redirect_url=None, external_identifier=None, maximum_payments=None, send_update_by_email_address=None, expiration_hours=None, theme=None, language=None, header=None, update_organization_on_success=None, update_organization_on_failure=None, update_customer_on_success=None, document_description=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body207 - a model defined in Swagger"""  # noqa: E501
        self._customer = None
        self._items = None
        self._vat_included = None
        self._document_type = None
        self._redirect_url = None
        self._external_identifier = None
        self._maximum_payments = None
        self._send_update_by_email_address = None
        self._expiration_hours = None
        self._theme = None
        self._language = None
        self._header = None
        self._update_organization_on_success = None
        self._update_organization_on_failure = None
        self._update_customer_on_success = None
        self._document_description = None
        self._credentials = None
        self.discriminator = None
        self.customer = customer
        self.items = items
        if vat_included is not None:
            self.vat_included = vat_included
        if document_type is not None:
            self.document_type = document_type
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if external_identifier is not None:
            self.external_identifier = external_identifier
        if maximum_payments is not None:
            self.maximum_payments = maximum_payments
        if send_update_by_email_address is not None:
            self.send_update_by_email_address = send_update_by_email_address
        if expiration_hours is not None:
            self.expiration_hours = expiration_hours
        if theme is not None:
            self.theme = theme
        if language is not None:
            self.language = language
        if header is not None:
            self.header = header
        if update_organization_on_success is not None:
            self.update_organization_on_success = update_organization_on_success
        if update_organization_on_failure is not None:
            self.update_organization_on_failure = update_organization_on_failure
        if update_customer_on_success is not None:
            self.update_customer_on_success = update_customer_on_success
        if document_description is not None:
            self.document_description = document_description
        self.credentials = credentials
        BillingPaymentsBeginRedirectRequest.__init__(self, *args, **kwargs)

    @property
    def customer(self):
        """Gets the customer of this Body207.  # noqa: E501

        Customer  # noqa: E501

        :return: The customer of this Body207.  # noqa: E501
        :rtype: Object
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Body207.

        Customer  # noqa: E501

        :param customer: The customer of this Body207.  # noqa: E501
        :type: Object
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def items(self):
        """Gets the items of this Body207.  # noqa: E501

        Items  # noqa: E501

        :return: The items of this Body207.  # noqa: E501
        :rtype: list[BillingTypedChargeItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Body207.

        Items  # noqa: E501

        :param items: The items of this Body207.  # noqa: E501
        :type: list[BillingTypedChargeItem]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

    @property
    def vat_included(self):
        """Gets the vat_included of this Body207.  # noqa: E501

        Is VAT included in the prices?<div><i>Leave empty for false.  Relevant for items only.</i></div>  # noqa: E501

        :return: The vat_included of this Body207.  # noqa: E501
        :rtype: bool
        """
        return self._vat_included

    @vat_included.setter
    def vat_included(self, vat_included):
        """Sets the vat_included of this Body207.

        Is VAT included in the prices?<div><i>Leave empty for false.  Relevant for items only.</i></div>  # noqa: E501

        :param vat_included: The vat_included of this Body207.  # noqa: E501
        :type: bool
        """

        self._vat_included = vat_included

    @property
    def document_type(self):
        """Gets the document_type of this Body207.  # noqa: E501

        Created document type<div><i>Leave empty for default</i></div>  # noqa: E501

        :return: The document_type of this Body207.  # noqa: E501
        :rtype: Object
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this Body207.

        Created document type<div><i>Leave empty for default</i></div>  # noqa: E501

        :param document_type: The document_type of this Body207.  # noqa: E501
        :type: Object
        """

        self._document_type = document_type

    @property
    def redirect_url(self):
        """Gets the redirect_url of this Body207.  # noqa: E501

        URL to redirect the user on successful payment.<div><i>The following parameters will be added to the URL:  OG-CustomerID: Customer identifier  OG-PaymentID: Payment identifier  OG-ExternalIdentifier: The original ExternalIdentifier  When empty, the user will be redirected the the customer payments history page</i></div>  # noqa: E501

        :return: The redirect_url of this Body207.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this Body207.

        URL to redirect the user on successful payment.<div><i>The following parameters will be added to the URL:  OG-CustomerID: Customer identifier  OG-PaymentID: Payment identifier  OG-ExternalIdentifier: The original ExternalIdentifier  When empty, the user will be redirected the the customer payments history page</i></div>  # noqa: E501

        :param redirect_url: The redirect_url of this Body207.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def external_identifier(self):
        """Gets the external_identifier of this Body207.  # noqa: E501

        External identifier.<div><i>This identifier will be appended to the RedirectURL on successful payment.</i></div>  # noqa: E501

        :return: The external_identifier of this Body207.  # noqa: E501
        :rtype: str
        """
        return self._external_identifier

    @external_identifier.setter
    def external_identifier(self, external_identifier):
        """Sets the external_identifier of this Body207.

        External identifier.<div><i>This identifier will be appended to the RedirectURL on successful payment.</i></div>  # noqa: E501

        :param external_identifier: The external_identifier of this Body207.  # noqa: E501
        :type: str
        """

        self._external_identifier = external_identifier

    @property
    def maximum_payments(self):
        """Gets the maximum_payments of this Body207.  # noqa: E501

        Maximum payments (installments) allowed on the payment page.<div><i>By default, the maximum payments count is set according to the purchase pages application settings.  Set to 0 to disable payments.</i></div>  # noqa: E501

        :return: The maximum_payments of this Body207.  # noqa: E501
        :rtype: int
        """
        return self._maximum_payments

    @maximum_payments.setter
    def maximum_payments(self, maximum_payments):
        """Sets the maximum_payments of this Body207.

        Maximum payments (installments) allowed on the payment page.<div><i>By default, the maximum payments count is set according to the purchase pages application settings.  Set to 0 to disable payments.</i></div>  # noqa: E501

        :param maximum_payments: The maximum_payments of this Body207.  # noqa: E501
        :type: int
        """

        self._maximum_payments = maximum_payments

    @property
    def send_update_by_email_address(self):
        """Gets the send_update_by_email_address of this Body207.  # noqa: E501

        Email address to which the result document will be created following payments.  # noqa: E501

        :return: The send_update_by_email_address of this Body207.  # noqa: E501
        :rtype: str
        """
        return self._send_update_by_email_address

    @send_update_by_email_address.setter
    def send_update_by_email_address(self, send_update_by_email_address):
        """Sets the send_update_by_email_address of this Body207.

        Email address to which the result document will be created following payments.  # noqa: E501

        :param send_update_by_email_address: The send_update_by_email_address of this Body207.  # noqa: E501
        :type: str
        """

        self._send_update_by_email_address = send_update_by_email_address

    @property
    def expiration_hours(self):
        """Gets the expiration_hours of this Body207.  # noqa: E501

        Number of hours, in which the direct URL will expire.<div><i>Defaults to 1 hours. Maximum of 240 hours (10 days).</i></div>  # noqa: E501

        :return: The expiration_hours of this Body207.  # noqa: E501
        :rtype: int
        """
        return self._expiration_hours

    @expiration_hours.setter
    def expiration_hours(self, expiration_hours):
        """Sets the expiration_hours of this Body207.

        Number of hours, in which the direct URL will expire.<div><i>Defaults to 1 hours. Maximum of 240 hours (10 days).</i></div>  # noqa: E501

        :param expiration_hours: The expiration_hours of this Body207.  # noqa: E501
        :type: int
        """

        self._expiration_hours = expiration_hours

    @property
    def theme(self):
        """Gets the theme of this Body207.  # noqa: E501

        Payment page theme  # noqa: E501

        :return: The theme of this Body207.  # noqa: E501
        :rtype: Object
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this Body207.

        Payment page theme  # noqa: E501

        :param theme: The theme of this Body207.  # noqa: E501
        :type: Object
        """

        self._theme = theme

    @property
    def language(self):
        """Gets the language of this Body207.  # noqa: E501

        Payment page language<div><i>Defaults to Hebrew</i></div>  # noqa: E501

        :return: The language of this Body207.  # noqa: E501
        :rtype: Object
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Body207.

        Payment page language<div><i>Defaults to Hebrew</i></div>  # noqa: E501

        :param language: The language of this Body207.  # noqa: E501
        :type: Object
        """

        self._language = language

    @property
    def header(self):
        """Gets the header of this Body207.  # noqa: E501

        Payment page header<div><i>Defaults to the company name</i></div>  # noqa: E501

        :return: The header of this Body207.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this Body207.

        Payment page header<div><i>Defaults to the company name</i></div>  # noqa: E501

        :param header: The header of this Body207.  # noqa: E501
        :type: str
        """

        self._header = header

    @property
    def update_organization_on_success(self):
        """Gets the update_organization_on_success of this Body207.  # noqa: E501

        Send payment notification to organization on successful payment  # noqa: E501

        :return: The update_organization_on_success of this Body207.  # noqa: E501
        :rtype: bool
        """
        return self._update_organization_on_success

    @update_organization_on_success.setter
    def update_organization_on_success(self, update_organization_on_success):
        """Sets the update_organization_on_success of this Body207.

        Send payment notification to organization on successful payment  # noqa: E501

        :param update_organization_on_success: The update_organization_on_success of this Body207.  # noqa: E501
        :type: bool
        """

        self._update_organization_on_success = update_organization_on_success

    @property
    def update_organization_on_failure(self):
        """Gets the update_organization_on_failure of this Body207.  # noqa: E501

        Send payment notification to organization on failed payment  # noqa: E501

        :return: The update_organization_on_failure of this Body207.  # noqa: E501
        :rtype: bool
        """
        return self._update_organization_on_failure

    @update_organization_on_failure.setter
    def update_organization_on_failure(self, update_organization_on_failure):
        """Sets the update_organization_on_failure of this Body207.

        Send payment notification to organization on failed payment  # noqa: E501

        :param update_organization_on_failure: The update_organization_on_failure of this Body207.  # noqa: E501
        :type: bool
        """

        self._update_organization_on_failure = update_organization_on_failure

    @property
    def update_customer_on_success(self):
        """Gets the update_customer_on_success of this Body207.  # noqa: E501

        Send payment notification to customer on successful payment.  # noqa: E501

        :return: The update_customer_on_success of this Body207.  # noqa: E501
        :rtype: bool
        """
        return self._update_customer_on_success

    @update_customer_on_success.setter
    def update_customer_on_success(self, update_customer_on_success):
        """Sets the update_customer_on_success of this Body207.

        Send payment notification to customer on successful payment.  # noqa: E501

        :param update_customer_on_success: The update_customer_on_success of this Body207.  # noqa: E501
        :type: bool
        """

        self._update_customer_on_success = update_customer_on_success

    @property
    def document_description(self):
        """Gets the document_description of this Body207.  # noqa: E501

        Document description (the description is printed on the document)  # noqa: E501

        :return: The document_description of this Body207.  # noqa: E501
        :rtype: str
        """
        return self._document_description

    @document_description.setter
    def document_description(self, document_description):
        """Sets the document_description of this Body207.

        Document description (the description is printed on the document)  # noqa: E501

        :param document_description: The document_description of this Body207.  # noqa: E501
        :type: str
        """

        self._document_description = document_description

    @property
    def credentials(self):
        """Gets the credentials of this Body207.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body207.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body207.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body207.  # noqa: E501
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
        if issubclass(Body207, dict):
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
        if not isinstance(other, Body207):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
