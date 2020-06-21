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


class AccountingTypedDocumentSendByEmail(object):
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
        'email_address': 'str',
        'original': 'bool',
        'send_as_payment_request': 'bool'
    }

    attribute_map = {
        'email_address': 'EmailAddress',
        'original': 'Original',
        'send_as_payment_request': 'SendAsPaymentRequest'
    }

    def __init__(self, email_address=None, original=None, send_as_payment_request=None):  # noqa: E501
        """AccountingTypedDocumentSendByEmail - a model defined in Swagger"""  # noqa: E501
        self._email_address = None
        self._original = None
        self._send_as_payment_request = None
        self.discriminator = None
        if email_address is not None:
            self.email_address = email_address
        if original is not None:
            self.original = original
        if send_as_payment_request is not None:
            self.send_as_payment_request = send_as_payment_request

    @property
    def email_address(self):
        """Gets the email_address of this AccountingTypedDocumentSendByEmail.  # noqa: E501

        Recipient email address<div><i>Defaults to the customer email address</i></div>  # noqa: E501

        :return: The email_address of this AccountingTypedDocumentSendByEmail.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this AccountingTypedDocumentSendByEmail.

        Recipient email address<div><i>Defaults to the customer email address</i></div>  # noqa: E501

        :param email_address: The email_address of this AccountingTypedDocumentSendByEmail.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def original(self):
        """Gets the original of this AccountingTypedDocumentSendByEmail.  # noqa: E501

        Send original document / copy?  # noqa: E501

        :return: The original of this AccountingTypedDocumentSendByEmail.  # noqa: E501
        :rtype: bool
        """
        return self._original

    @original.setter
    def original(self, original):
        """Sets the original of this AccountingTypedDocumentSendByEmail.

        Send original document / copy?  # noqa: E501

        :param original: The original of this AccountingTypedDocumentSendByEmail.  # noqa: E501
        :type: bool
        """

        self._original = original

    @property
    def send_as_payment_request(self):
        """Gets the send_as_payment_request of this AccountingTypedDocumentSendByEmail.  # noqa: E501

        Send document as a payment request  # noqa: E501

        :return: The send_as_payment_request of this AccountingTypedDocumentSendByEmail.  # noqa: E501
        :rtype: bool
        """
        return self._send_as_payment_request

    @send_as_payment_request.setter
    def send_as_payment_request(self, send_as_payment_request):
        """Sets the send_as_payment_request of this AccountingTypedDocumentSendByEmail.

        Send document as a payment request  # noqa: E501

        :param send_as_payment_request: The send_as_payment_request of this AccountingTypedDocumentSendByEmail.  # noqa: E501
        :type: bool
        """

        self._send_as_payment_request = send_as_payment_request

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
        if issubclass(AccountingTypedDocumentSendByEmail, dict):
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
        if not isinstance(other, AccountingTypedDocumentSendByEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
