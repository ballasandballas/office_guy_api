# coding: utf-8

"""
    OfficeGuy API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccountingDocumentsCreateRequest(object):
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
        'details': 'AccountingTypedDocumentDetails',
        'items': 'list[AccountingTypedDocumentItem]',
        'payments': 'list[AccountingTypedDocumentPayment]',
        'vat_included': 'bool',
        'vat_rate': 'float',
        'original_document_id': 'int',
        'credentials': 'CoreAPICredentials'
    }

    attribute_map = {
        'details': 'Details',
        'items': 'Items',
        'payments': 'Payments',
        'vat_included': 'VATIncluded',
        'vat_rate': 'VATRate',
        'original_document_id': 'OriginalDocumentID',
        'credentials': 'Credentials'
    }

    def __init__(self, details=None, items=None, payments=None, vat_included=None, vat_rate=None, original_document_id=None, credentials=None):  # noqa: E501
        """AccountingDocumentsCreateRequest - a model defined in Swagger"""  # noqa: E501

        self._details = None
        self._items = None
        self._payments = None
        self._vat_included = None
        self._vat_rate = None
        self._original_document_id = None
        self._credentials = None
        self.discriminator = None

        self.details = details
        if items is not None:
            self.items = items
        if payments is not None:
            self.payments = payments
        if vat_included is not None:
            self.vat_included = vat_included
        if vat_rate is not None:
            self.vat_rate = vat_rate
        if original_document_id is not None:
            self.original_document_id = original_document_id
        self.credentials = credentials

    @property
    def details(self):
        """Gets the details of this AccountingDocumentsCreateRequest.  # noqa: E501

        General document details  # noqa: E501

        :return: The details of this AccountingDocumentsCreateRequest.  # noqa: E501
        :rtype: AccountingTypedDocumentDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this AccountingDocumentsCreateRequest.

        General document details  # noqa: E501

        :param details: The details of this AccountingDocumentsCreateRequest.  # noqa: E501
        :type: AccountingTypedDocumentDetails
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

    @property
    def items(self):
        """Gets the items of this AccountingDocumentsCreateRequest.  # noqa: E501

        Document items<div><i>Can be used in Invoice, Invoice/Receipt, Proforma invoice etc.</i></div>  # noqa: E501

        :return: The items of this AccountingDocumentsCreateRequest.  # noqa: E501
        :rtype: list[AccountingTypedDocumentItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this AccountingDocumentsCreateRequest.

        Document items<div><i>Can be used in Invoice, Invoice/Receipt, Proforma invoice etc.</i></div>  # noqa: E501

        :param items: The items of this AccountingDocumentsCreateRequest.  # noqa: E501
        :type: list[AccountingTypedDocumentItem]
        """

        self._items = items

    @property
    def payments(self):
        """Gets the payments of this AccountingDocumentsCreateRequest.  # noqa: E501

        Document payments (Can be used in invoice+receipt/receipt)<div><i>Please note each payment should contain a single details object (Cash/BankTransfer/Cheque/CreditCard/Other), multiple payments are handled through the payments array.</i></div>  # noqa: E501

        :return: The payments of this AccountingDocumentsCreateRequest.  # noqa: E501
        :rtype: list[AccountingTypedDocumentPayment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this AccountingDocumentsCreateRequest.

        Document payments (Can be used in invoice+receipt/receipt)<div><i>Please note each payment should contain a single details object (Cash/BankTransfer/Cheque/CreditCard/Other), multiple payments are handled through the payments array.</i></div>  # noqa: E501

        :param payments: The payments of this AccountingDocumentsCreateRequest.  # noqa: E501
        :type: list[AccountingTypedDocumentPayment]
        """

        self._payments = payments

    @property
    def vat_included(self):
        """Gets the vat_included of this AccountingDocumentsCreateRequest.  # noqa: E501

        Is VAT included in the prices?<div><i>Leave empty for false.  Relevant for items only.</i></div>  # noqa: E501

        :return: The vat_included of this AccountingDocumentsCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._vat_included

    @vat_included.setter
    def vat_included(self, vat_included):
        """Sets the vat_included of this AccountingDocumentsCreateRequest.

        Is VAT included in the prices?<div><i>Leave empty for false.  Relevant for items only.</i></div>  # noqa: E501

        :param vat_included: The vat_included of this AccountingDocumentsCreateRequest.  # noqa: E501
        :type: bool
        """

        self._vat_included = vat_included

    @property
    def vat_rate(self):
        """Gets the vat_rate of this AccountingDocumentsCreateRequest.  # noqa: E501

        Document VAT Rate<div><i>Leave empty for company default.  Relevant for items only.</i></div>  # noqa: E501

        :return: The vat_rate of this AccountingDocumentsCreateRequest.  # noqa: E501
        :rtype: float
        """
        return self._vat_rate

    @vat_rate.setter
    def vat_rate(self, vat_rate):
        """Sets the vat_rate of this AccountingDocumentsCreateRequest.

        Document VAT Rate<div><i>Leave empty for company default.  Relevant for items only.</i></div>  # noqa: E501

        :param vat_rate: The vat_rate of this AccountingDocumentsCreateRequest.  # noqa: E501
        :type: float
        """

        self._vat_rate = vat_rate

    @property
    def original_document_id(self):
        """Gets the original_document_id of this AccountingDocumentsCreateRequest.  # noqa: E501

        Original document identifier.<div><i>This allows keeping a relationship between an original and a created document (such as credits for debit invoices)</i></div>  # noqa: E501

        :return: The original_document_id of this AccountingDocumentsCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._original_document_id

    @original_document_id.setter
    def original_document_id(self, original_document_id):
        """Sets the original_document_id of this AccountingDocumentsCreateRequest.

        Original document identifier.<div><i>This allows keeping a relationship between an original and a created document (such as credits for debit invoices)</i></div>  # noqa: E501

        :param original_document_id: The original_document_id of this AccountingDocumentsCreateRequest.  # noqa: E501
        :type: int
        """

        self._original_document_id = original_document_id

    @property
    def credentials(self):
        """Gets the credentials of this AccountingDocumentsCreateRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this AccountingDocumentsCreateRequest.  # noqa: E501
        :rtype: CoreAPICredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this AccountingDocumentsCreateRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this AccountingDocumentsCreateRequest.  # noqa: E501
        :type: CoreAPICredentials
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
        if issubclass(AccountingDocumentsCreateRequest, dict):
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
        if not isinstance(other, AccountingDocumentsCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
