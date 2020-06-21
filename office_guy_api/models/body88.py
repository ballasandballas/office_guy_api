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


class Body88(object):
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
        'get_format_preserving': 'bool',
        'card_number': 'str',
        'force_format_preserving_token': 'str',
        'credentials': 'Object'
    }
    if hasattr(CreditGuyVaultTokenizeRequest, "swagger_types"):
        swagger_types.update(CreditGuyVaultTokenizeRequest.swagger_types)

    attribute_map = {
        'get_format_preserving': 'GetFormatPreserving',
        'card_number': 'CardNumber',
        'force_format_preserving_token': 'ForceFormatPreservingToken',
        'credentials': 'Credentials'
    }
    if hasattr(CreditGuyVaultTokenizeRequest, "attribute_map"):
        attribute_map.update(CreditGuyVaultTokenizeRequest.attribute_map)

    def __init__(self, get_format_preserving=None, card_number=None, force_format_preserving_token=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body88 - a model defined in Swagger"""  # noqa: E501
        self._get_format_preserving = None
        self._card_number = None
        self._force_format_preserving_token = None
        self._credentials = None
        self.discriminator = None
        if get_format_preserving is not None:
            self.get_format_preserving = get_format_preserving
        self.card_number = card_number
        self.force_format_preserving_token = force_format_preserving_token
        self.credentials = credentials
        CreditGuyVaultTokenizeRequest.__init__(self, *args, **kwargs)

    @property
    def get_format_preserving(self):
        """Gets the get_format_preserving of this Body88.  # noqa: E501

        Should tokenize method also return format preserved token, or only Guid token<div><i>Defaults to False</i></div>  # noqa: E501

        :return: The get_format_preserving of this Body88.  # noqa: E501
        :rtype: bool
        """
        return self._get_format_preserving

    @get_format_preserving.setter
    def get_format_preserving(self, get_format_preserving):
        """Sets the get_format_preserving of this Body88.

        Should tokenize method also return format preserved token, or only Guid token<div><i>Defaults to False</i></div>  # noqa: E501

        :param get_format_preserving: The get_format_preserving of this Body88.  # noqa: E501
        :type: bool
        """

        self._get_format_preserving = get_format_preserving

    @property
    def card_number(self):
        """Gets the card_number of this Body88.  # noqa: E501

        Full card number to tokenize  # noqa: E501

        :return: The card_number of this Body88.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this Body88.

        Full card number to tokenize  # noqa: E501

        :param card_number: The card_number of this Body88.  # noqa: E501
        :type: str
        """
        if card_number is None:
            raise ValueError("Invalid value for `card_number`, must not be `None`")  # noqa: E501

        self._card_number = card_number

    @property
    def force_format_preserving_token(self):
        """Gets the force_format_preserving_token of this Body88.  # noqa: E501

        Forced format preserving token  This can be useful when migrating from another credit card gateway to OfficeGuy.  Please note the format preserving token should be a RANDOM identifier, which can't be reverse engineered into the card number (encoding/encrypting etc. isn't supported).  # noqa: E501

        :return: The force_format_preserving_token of this Body88.  # noqa: E501
        :rtype: str
        """
        return self._force_format_preserving_token

    @force_format_preserving_token.setter
    def force_format_preserving_token(self, force_format_preserving_token):
        """Sets the force_format_preserving_token of this Body88.

        Forced format preserving token  This can be useful when migrating from another credit card gateway to OfficeGuy.  Please note the format preserving token should be a RANDOM identifier, which can't be reverse engineered into the card number (encoding/encrypting etc. isn't supported).  # noqa: E501

        :param force_format_preserving_token: The force_format_preserving_token of this Body88.  # noqa: E501
        :type: str
        """
        if force_format_preserving_token is None:
            raise ValueError("Invalid value for `force_format_preserving_token`, must not be `None`")  # noqa: E501

        self._force_format_preserving_token = force_format_preserving_token

    @property
    def credentials(self):
        """Gets the credentials of this Body88.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body88.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body88.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body88.  # noqa: E501
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
        if issubclass(Body88, dict):
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
        if not isinstance(other, Body88):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
