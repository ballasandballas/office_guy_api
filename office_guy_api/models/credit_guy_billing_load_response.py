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


class CreditGuyBillingLoadResponse(object):
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
        'transaction_i_ds': 'list[int]'
    }

    attribute_map = {
        'transaction_i_ds': 'TransactionIDs'
    }

    def __init__(self, transaction_i_ds=None):  # noqa: E501
        """CreditGuyBillingLoadResponse - a model defined in Swagger"""  # noqa: E501
        self._transaction_i_ds = None
        self.discriminator = None
        if transaction_i_ds is not None:
            self.transaction_i_ds = transaction_i_ds

    @property
    def transaction_i_ds(self):
        """Gets the transaction_i_ds of this CreditGuyBillingLoadResponse.  # noqa: E501

        Loaded transactions identifiers  # noqa: E501

        :return: The transaction_i_ds of this CreditGuyBillingLoadResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._transaction_i_ds

    @transaction_i_ds.setter
    def transaction_i_ds(self, transaction_i_ds):
        """Sets the transaction_i_ds of this CreditGuyBillingLoadResponse.

        Loaded transactions identifiers  # noqa: E501

        :param transaction_i_ds: The transaction_i_ds of this CreditGuyBillingLoadResponse.  # noqa: E501
        :type: list[int]
        """

        self._transaction_i_ds = transaction_i_ds

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
        if issubclass(CreditGuyBillingLoadResponse, dict):
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
        if not isinstance(other, CreditGuyBillingLoadResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
