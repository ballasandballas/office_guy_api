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


class AccountingGeneralSetNextDocumentNumberRequest(object):
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
        'type': 'str',
        'next_document_number': 'int',
        'credentials': 'CoreAPICredentials'
    }

    attribute_map = {
        'type': 'Type',
        'next_document_number': 'NextDocumentNumber',
        'credentials': 'Credentials'
    }

    def __init__(self, type=None, next_document_number=None, credentials=None):  # noqa: E501
        """AccountingGeneralSetNextDocumentNumberRequest - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._next_document_number = None
        self._credentials = None
        self.discriminator = None

        self.type = type
        self.next_document_number = next_document_number
        self.credentials = credentials

    @property
    def type(self):
        """Gets the type of this AccountingGeneralSetNextDocumentNumberRequest.  # noqa: E501

        Document type  # noqa: E501

        :return: The type of this AccountingGeneralSetNextDocumentNumberRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountingGeneralSetNextDocumentNumberRequest.

        Document type  # noqa: E501

        :param type: The type of this AccountingGeneralSetNextDocumentNumberRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Invoice", "InvoiceAndReceipt", "Receipt", "ProformaInvoice", "DonationReceipt", "CreditInvoice", "CreditInvoiceAndReceipt", "CreditReceipt", "Order", "DeliveryNote", "GoodsReturnNote", "PurchasingOrder", "PriceQuotation", "PaymentRequest", "CreditDonationReceipt"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def next_document_number(self):
        """Gets the next_document_number of this AccountingGeneralSetNextDocumentNumberRequest.  # noqa: E501

        Next document number to set.<div><i>Note that the document number has to be higher than the last issued document number.  By default, all documents numbers are set to 1000.</i></div>  # noqa: E501

        :return: The next_document_number of this AccountingGeneralSetNextDocumentNumberRequest.  # noqa: E501
        :rtype: int
        """
        return self._next_document_number

    @next_document_number.setter
    def next_document_number(self, next_document_number):
        """Sets the next_document_number of this AccountingGeneralSetNextDocumentNumberRequest.

        Next document number to set.<div><i>Note that the document number has to be higher than the last issued document number.  By default, all documents numbers are set to 1000.</i></div>  # noqa: E501

        :param next_document_number: The next_document_number of this AccountingGeneralSetNextDocumentNumberRequest.  # noqa: E501
        :type: int
        """
        if next_document_number is None:
            raise ValueError("Invalid value for `next_document_number`, must not be `None`")  # noqa: E501

        self._next_document_number = next_document_number

    @property
    def credentials(self):
        """Gets the credentials of this AccountingGeneralSetNextDocumentNumberRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this AccountingGeneralSetNextDocumentNumberRequest.  # noqa: E501
        :rtype: CoreAPICredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this AccountingGeneralSetNextDocumentNumberRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this AccountingGeneralSetNextDocumentNumberRequest.  # noqa: E501
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
        if issubclass(AccountingGeneralSetNextDocumentNumberRequest, dict):
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
        if not isinstance(other, AccountingGeneralSetNextDocumentNumberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
