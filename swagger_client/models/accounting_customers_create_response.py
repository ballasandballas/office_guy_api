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


class AccountingCustomersCreateResponse(object):
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
        'customer_id': 'int',
        'customer_history_url': 'str'
    }

    attribute_map = {
        'customer_id': 'CustomerID',
        'customer_history_url': 'CustomerHistoryURL'
    }

    def __init__(self, customer_id=None, customer_history_url=None):  # noqa: E501
        """AccountingCustomersCreateResponse - a model defined in Swagger"""  # noqa: E501

        self._customer_id = None
        self._customer_history_url = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if customer_history_url is not None:
            self.customer_history_url = customer_history_url

    @property
    def customer_id(self):
        """Gets the customer_id of this AccountingCustomersCreateResponse.  # noqa: E501

        Customer number  # noqa: E501

        :return: The customer_id of this AccountingCustomersCreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AccountingCustomersCreateResponse.

        Customer number  # noqa: E501

        :param customer_id: The customer_id of this AccountingCustomersCreateResponse.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def customer_history_url(self):
        """Gets the customer_history_url of this AccountingCustomersCreateResponse.  # noqa: E501

        Link to the customer details page (דף מידע ללקוח/ה)  # noqa: E501

        :return: The customer_history_url of this AccountingCustomersCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer_history_url

    @customer_history_url.setter
    def customer_history_url(self, customer_history_url):
        """Sets the customer_history_url of this AccountingCustomersCreateResponse.

        Link to the customer details page (דף מידע ללקוח/ה)  # noqa: E501

        :param customer_history_url: The customer_history_url of this AccountingCustomersCreateResponse.  # noqa: E501
        :type: str
        """

        self._customer_history_url = customer_history_url

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
        if issubclass(AccountingCustomersCreateResponse, dict):
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
        if not isinstance(other, AccountingCustomersCreateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
