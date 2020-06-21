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


class AllOfResponseAccountingGeneralGetExchangeRateResponseData(object):
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
        'rate': 'float'
    }
    if hasattr(AccountingGeneralGetExchangeRateResponse, "swagger_types"):
        swagger_types.update(AccountingGeneralGetExchangeRateResponse.swagger_types)

    attribute_map = {
        'rate': 'Rate'
    }
    if hasattr(AccountingGeneralGetExchangeRateResponse, "attribute_map"):
        attribute_map.update(AccountingGeneralGetExchangeRateResponse.attribute_map)

    def __init__(self, rate=None, *args, **kwargs):  # noqa: E501
        """AllOfResponseAccountingGeneralGetExchangeRateResponseData - a model defined in Swagger"""  # noqa: E501
        self._rate = None
        self.discriminator = None
        if rate is not None:
            self.rate = rate
        AccountingGeneralGetExchangeRateResponse.__init__(self, *args, **kwargs)

    @property
    def rate(self):
        """Gets the rate of this AllOfResponseAccountingGeneralGetExchangeRateResponseData.  # noqa: E501


        :return: The rate of this AllOfResponseAccountingGeneralGetExchangeRateResponseData.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this AllOfResponseAccountingGeneralGetExchangeRateResponseData.


        :param rate: The rate of this AllOfResponseAccountingGeneralGetExchangeRateResponseData.  # noqa: E501
        :type: float
        """

        self._rate = rate

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
        if issubclass(AllOfResponseAccountingGeneralGetExchangeRateResponseData, dict):
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
        if not isinstance(other, AllOfResponseAccountingGeneralGetExchangeRateResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
