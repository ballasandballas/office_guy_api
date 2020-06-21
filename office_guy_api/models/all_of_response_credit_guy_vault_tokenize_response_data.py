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


class AllOfResponseCreditGuyVaultTokenizeResponseData(object):
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
        'token': 'str',
        'format_preserving_token': 'str'
    }
    if hasattr(CreditGuyVaultTokenizeResponse, "swagger_types"):
        swagger_types.update(CreditGuyVaultTokenizeResponse.swagger_types)

    attribute_map = {
        'token': 'Token',
        'format_preserving_token': 'FormatPreservingToken'
    }
    if hasattr(CreditGuyVaultTokenizeResponse, "attribute_map"):
        attribute_map.update(CreditGuyVaultTokenizeResponse.attribute_map)

    def __init__(self, token=None, format_preserving_token=None, *args, **kwargs):  # noqa: E501
        """AllOfResponseCreditGuyVaultTokenizeResponseData - a model defined in Swagger"""  # noqa: E501
        self._token = None
        self._format_preserving_token = None
        self.discriminator = None
        if token is not None:
            self.token = token
        if format_preserving_token is not None:
            self.format_preserving_token = format_preserving_token
        CreditGuyVaultTokenizeResponse.__init__(self, *args, **kwargs)

    @property
    def token(self):
        """Gets the token of this AllOfResponseCreditGuyVaultTokenizeResponseData.  # noqa: E501

        Card token  # noqa: E501

        :return: The token of this AllOfResponseCreditGuyVaultTokenizeResponseData.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AllOfResponseCreditGuyVaultTokenizeResponseData.

        Card token  # noqa: E501

        :param token: The token of this AllOfResponseCreditGuyVaultTokenizeResponseData.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def format_preserving_token(self):
        """Gets the format_preserving_token of this AllOfResponseCreditGuyVaultTokenizeResponseData.  # noqa: E501

        Format preserved token<div><i>Returned when GetFormatPreserving is used</i></div>  # noqa: E501

        :return: The format_preserving_token of this AllOfResponseCreditGuyVaultTokenizeResponseData.  # noqa: E501
        :rtype: str
        """
        return self._format_preserving_token

    @format_preserving_token.setter
    def format_preserving_token(self, format_preserving_token):
        """Sets the format_preserving_token of this AllOfResponseCreditGuyVaultTokenizeResponseData.

        Format preserved token<div><i>Returned when GetFormatPreserving is used</i></div>  # noqa: E501

        :param format_preserving_token: The format_preserving_token of this AllOfResponseCreditGuyVaultTokenizeResponseData.  # noqa: E501
        :type: str
        """

        self._format_preserving_token = format_preserving_token

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
        if issubclass(AllOfResponseCreditGuyVaultTokenizeResponseData, dict):
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
        if not isinstance(other, AllOfResponseCreditGuyVaultTokenizeResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
