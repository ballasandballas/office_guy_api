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


class AccountingGeneralGetExchangeRateRequest(object):
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
        '_date': 'datetime',
        'currency_from': 'str',
        'currency_to': 'str',
        'credentials': 'AllOfAccountingGeneralGetExchangeRateRequestCredentials'
    }

    attribute_map = {
        '_date': 'Date',
        'currency_from': 'Currency_From',
        'currency_to': 'Currency_To',
        'credentials': 'Credentials'
    }

    def __init__(self, _date=None, currency_from=None, currency_to=None, credentials=None):  # noqa: E501
        """AccountingGeneralGetExchangeRateRequest - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._currency_from = None
        self._currency_to = None
        self._credentials = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if currency_from is not None:
            self.currency_from = currency_from
        if currency_to is not None:
            self.currency_to = currency_to
        self.credentials = credentials

    @property
    def _date(self):
        """Gets the _date of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501

        Defaults to current date  # noqa: E501

        :return: The _date of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AccountingGeneralGetExchangeRateRequest.

        Defaults to current date  # noqa: E501

        :param _date: The _date of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def currency_from(self):
        """Gets the currency_from of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501

        Original currency<div><i>Defaults to USD</i></div>  # noqa: E501

        :return: The currency_from of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_from

    @currency_from.setter
    def currency_from(self, currency_from):
        """Sets the currency_from of this AccountingGeneralGetExchangeRateRequest.

        Original currency<div><i>Defaults to USD</i></div>  # noqa: E501

        :param currency_from: The currency_from of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501
        :type: str
        """

        self._currency_from = currency_from

    @property
    def currency_to(self):
        """Gets the currency_to of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501

        Target currency<div><i>Defaults to ILS</i></div>  # noqa: E501

        :return: The currency_to of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency_to

    @currency_to.setter
    def currency_to(self, currency_to):
        """Sets the currency_to of this AccountingGeneralGetExchangeRateRequest.

        Target currency<div><i>Defaults to ILS</i></div>  # noqa: E501

        :param currency_to: The currency_to of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501
        :type: str
        """

        self._currency_to = currency_to

    @property
    def credentials(self):
        """Gets the credentials of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501
        :rtype: AllOfAccountingGeneralGetExchangeRateRequestCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this AccountingGeneralGetExchangeRateRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this AccountingGeneralGetExchangeRateRequest.  # noqa: E501
        :type: AllOfAccountingGeneralGetExchangeRateRequestCredentials
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
        if issubclass(AccountingGeneralGetExchangeRateRequest, dict):
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
        if not isinstance(other, AccountingGeneralGetExchangeRateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
