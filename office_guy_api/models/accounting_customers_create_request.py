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


class AccountingCustomersCreateRequest(object):
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
        'details': 'AccountingTypedCustomer',
        'credentials': 'CoreAPICredentials'
    }

    attribute_map = {
        'details': 'Details',
        'credentials': 'Credentials'
    }

    def __init__(self, details=None, credentials=None):  # noqa: E501
        """AccountingCustomersCreateRequest - a model defined in Swagger"""  # noqa: E501

        self._details = None
        self._credentials = None
        self.discriminator = None

        self.details = details
        self.credentials = credentials

    @property
    def details(self):
        """Gets the details of this AccountingCustomersCreateRequest.  # noqa: E501

        Customer details  # noqa: E501

        :return: The details of this AccountingCustomersCreateRequest.  # noqa: E501
        :rtype: AccountingTypedCustomer
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this AccountingCustomersCreateRequest.

        Customer details  # noqa: E501

        :param details: The details of this AccountingCustomersCreateRequest.  # noqa: E501
        :type: AccountingTypedCustomer
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

    @property
    def credentials(self):
        """Gets the credentials of this AccountingCustomersCreateRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this AccountingCustomersCreateRequest.  # noqa: E501
        :rtype: CoreAPICredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this AccountingCustomersCreateRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this AccountingCustomersCreateRequest.  # noqa: E501
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
        if issubclass(AccountingCustomersCreateRequest, dict):
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
        if not isinstance(other, AccountingCustomersCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
