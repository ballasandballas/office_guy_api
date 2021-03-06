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


class BillingPaymentsChargeResponse(object):
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
        'payment': 'BillingTypedPayment',
        'document_id': 'int',
        'document_number': 'int',
        'customer_id': 'int',
        'document_download_url': 'str'
    }

    attribute_map = {
        'payment': 'Payment',
        'document_id': 'DocumentID',
        'document_number': 'DocumentNumber',
        'customer_id': 'CustomerID',
        'document_download_url': 'DocumentDownloadURL'
    }

    def __init__(self, payment=None, document_id=None, document_number=None, customer_id=None, document_download_url=None):  # noqa: E501
        """BillingPaymentsChargeResponse - a model defined in Swagger"""  # noqa: E501

        self._payment = None
        self._document_id = None
        self._document_number = None
        self._customer_id = None
        self._document_download_url = None
        self.discriminator = None

        if payment is not None:
            self.payment = payment
        if document_id is not None:
            self.document_id = document_id
        if document_number is not None:
            self.document_number = document_number
        if customer_id is not None:
            self.customer_id = customer_id
        if document_download_url is not None:
            self.document_download_url = document_download_url

    @property
    def payment(self):
        """Gets the payment of this BillingPaymentsChargeResponse.  # noqa: E501


        :return: The payment of this BillingPaymentsChargeResponse.  # noqa: E501
        :rtype: BillingTypedPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this BillingPaymentsChargeResponse.


        :param payment: The payment of this BillingPaymentsChargeResponse.  # noqa: E501
        :type: BillingTypedPayment
        """

        self._payment = payment

    @property
    def document_id(self):
        """Gets the document_id of this BillingPaymentsChargeResponse.  # noqa: E501

        Document ID (OfficeGuy identifier)  # noqa: E501

        :return: The document_id of this BillingPaymentsChargeResponse.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this BillingPaymentsChargeResponse.

        Document ID (OfficeGuy identifier)  # noqa: E501

        :param document_id: The document_id of this BillingPaymentsChargeResponse.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def document_number(self):
        """Gets the document_number of this BillingPaymentsChargeResponse.  # noqa: E501

        Document number  # noqa: E501

        :return: The document_number of this BillingPaymentsChargeResponse.  # noqa: E501
        :rtype: int
        """
        return self._document_number

    @document_number.setter
    def document_number(self, document_number):
        """Sets the document_number of this BillingPaymentsChargeResponse.

        Document number  # noqa: E501

        :param document_number: The document_number of this BillingPaymentsChargeResponse.  # noqa: E501
        :type: int
        """

        self._document_number = document_number

    @property
    def customer_id(self):
        """Gets the customer_id of this BillingPaymentsChargeResponse.  # noqa: E501

        Customer number  # noqa: E501

        :return: The customer_id of this BillingPaymentsChargeResponse.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this BillingPaymentsChargeResponse.

        Customer number  # noqa: E501

        :param customer_id: The customer_id of this BillingPaymentsChargeResponse.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def document_download_url(self):
        """Gets the document_download_url of this BillingPaymentsChargeResponse.  # noqa: E501

        Document download URL<div><i>Produced document will be original (on first fetching), or certified copy.</i></div>  # noqa: E501

        :return: The document_download_url of this BillingPaymentsChargeResponse.  # noqa: E501
        :rtype: str
        """
        return self._document_download_url

    @document_download_url.setter
    def document_download_url(self, document_download_url):
        """Sets the document_download_url of this BillingPaymentsChargeResponse.

        Document download URL<div><i>Produced document will be original (on first fetching), or certified copy.</i></div>  # noqa: E501

        :param document_download_url: The document_download_url of this BillingPaymentsChargeResponse.  # noqa: E501
        :type: str
        """

        self._document_download_url = document_download_url

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
        if issubclass(BillingPaymentsChargeResponse, dict):
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
        if not isinstance(other, BillingPaymentsChargeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
