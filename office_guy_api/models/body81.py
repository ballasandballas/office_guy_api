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


class Body81(object):
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
        'mode': 'Object',
        'amount': 'float',
        'payments_non_first_count': 'int',
        'payments_first_amount': 'float',
        'payments_non_first_amount': 'float',
        'currency': 'Object',
        'identifier': 'str',
        'merchant_number': 'str',
        'redirect_url': 'str',
        'credentials': 'Object'
    }
    if hasattr(CreditGuyGatewayBeginRedirectRequest, "swagger_types"):
        swagger_types.update(CreditGuyGatewayBeginRedirectRequest.swagger_types)

    attribute_map = {
        'mode': 'Mode',
        'amount': 'Amount',
        'payments_non_first_count': 'PaymentsNonFirstCount',
        'payments_first_amount': 'PaymentsFirstAmount',
        'payments_non_first_amount': 'PaymentsNonFirstAmount',
        'currency': 'Currency',
        'identifier': 'Identifier',
        'merchant_number': 'MerchantNumber',
        'redirect_url': 'RedirectURL',
        'credentials': 'Credentials'
    }
    if hasattr(CreditGuyGatewayBeginRedirectRequest, "attribute_map"):
        attribute_map.update(CreditGuyGatewayBeginRedirectRequest.attribute_map)

    def __init__(self, mode=None, amount=None, payments_non_first_count=None, payments_first_amount=None, payments_non_first_amount=None, currency=None, identifier=None, merchant_number=None, redirect_url=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body81 - a model defined in Swagger"""  # noqa: E501
        self._mode = None
        self._amount = None
        self._payments_non_first_count = None
        self._payments_first_amount = None
        self._payments_non_first_amount = None
        self._currency = None
        self._identifier = None
        self._merchant_number = None
        self._redirect_url = None
        self._credentials = None
        self.discriminator = None
        self.mode = mode
        if amount is not None:
            self.amount = amount
        if payments_non_first_count is not None:
            self.payments_non_first_count = payments_non_first_count
        if payments_first_amount is not None:
            self.payments_first_amount = payments_first_amount
        if payments_non_first_amount is not None:
            self.payments_non_first_amount = payments_non_first_amount
        if currency is not None:
            self.currency = currency
        if identifier is not None:
            self.identifier = identifier
        if merchant_number is not None:
            self.merchant_number = merchant_number
        if redirect_url is not None:
            self.redirect_url = redirect_url
        self.credentials = credentials
        CreditGuyGatewayBeginRedirectRequest.__init__(self, *args, **kwargs)

    @property
    def mode(self):
        """Gets the mode of this Body81.  # noqa: E501

        Transaction type  # noqa: E501

        :return: The mode of this Body81.  # noqa: E501
        :rtype: Object
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Body81.

        Transaction type  # noqa: E501

        :param mode: The mode of this Body81.  # noqa: E501
        :type: Object
        """
        if mode is None:
            raise ValueError("Invalid value for `mode`, must not be `None`")  # noqa: E501

        self._mode = mode

    @property
    def amount(self):
        """Gets the amount of this Body81.  # noqa: E501

        Transaction amount  # noqa: E501

        :return: The amount of this Body81.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Body81.

        Transaction amount  # noqa: E501

        :param amount: The amount of this Body81.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def payments_non_first_count(self):
        """Gets the payments_non_first_count of this Body81.  # noqa: E501

        Non-first payments count<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :return: The payments_non_first_count of this Body81.  # noqa: E501
        :rtype: int
        """
        return self._payments_non_first_count

    @payments_non_first_count.setter
    def payments_non_first_count(self, payments_non_first_count):
        """Sets the payments_non_first_count of this Body81.

        Non-first payments count<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :param payments_non_first_count: The payments_non_first_count of this Body81.  # noqa: E501
        :type: int
        """

        self._payments_non_first_count = payments_non_first_count

    @property
    def payments_first_amount(self):
        """Gets the payments_first_amount of this Body81.  # noqa: E501

        First payment amount<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :return: The payments_first_amount of this Body81.  # noqa: E501
        :rtype: float
        """
        return self._payments_first_amount

    @payments_first_amount.setter
    def payments_first_amount(self, payments_first_amount):
        """Sets the payments_first_amount of this Body81.

        First payment amount<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :param payments_first_amount: The payments_first_amount of this Body81.  # noqa: E501
        :type: float
        """

        self._payments_first_amount = payments_first_amount

    @property
    def payments_non_first_amount(self):
        """Gets the payments_non_first_amount of this Body81.  # noqa: E501

        Non-first payment amount<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :return: The payments_non_first_amount of this Body81.  # noqa: E501
        :rtype: float
        """
        return self._payments_non_first_amount

    @payments_non_first_amount.setter
    def payments_non_first_amount(self, payments_non_first_amount):
        """Sets the payments_non_first_amount of this Body81.

        Non-first payment amount<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :param payments_non_first_amount: The payments_non_first_amount of this Body81.  # noqa: E501
        :type: float
        """

        self._payments_non_first_amount = payments_non_first_amount

    @property
    def currency(self):
        """Gets the currency of this Body81.  # noqa: E501

        Transaction currency<div><i>Defaults to ILS</i></div>  # noqa: E501

        :return: The currency of this Body81.  # noqa: E501
        :rtype: Object
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Body81.

        Transaction currency<div><i>Defaults to ILS</i></div>  # noqa: E501

        :param currency: The currency of this Body81.  # noqa: E501
        :type: Object
        """

        self._currency = currency

    @property
    def identifier(self):
        """Gets the identifier of this Body81.  # noqa: E501

        Transaction identifier.<div><i>This parameter will be returned during redirect.</i></div>  # noqa: E501

        :return: The identifier of this Body81.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Body81.

        Transaction identifier.<div><i>This parameter will be returned during redirect.</i></div>  # noqa: E501

        :param identifier: The identifier of this Body81.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def merchant_number(self):
        """Gets the merchant_number of this Body81.  # noqa: E501

        Shva merchant number (Terminal number).<div><i>This parameter should only be used when multiple merchants are defined in the company.</i></div>  # noqa: E501

        :return: The merchant_number of this Body81.  # noqa: E501
        :rtype: str
        """
        return self._merchant_number

    @merchant_number.setter
    def merchant_number(self, merchant_number):
        """Sets the merchant_number of this Body81.

        Shva merchant number (Terminal number).<div><i>This parameter should only be used when multiple merchants are defined in the company.</i></div>  # noqa: E501

        :param merchant_number: The merchant_number of this Body81.  # noqa: E501
        :type: str
        """

        self._merchant_number = merchant_number

    @property
    def redirect_url(self):
        """Gets the redirect_url of this Body81.  # noqa: E501

        Redirect URL<div><i>Leave this empty to use the default RedirectURL</i></div>  # noqa: E501

        :return: The redirect_url of this Body81.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this Body81.

        Redirect URL<div><i>Leave this empty to use the default RedirectURL</i></div>  # noqa: E501

        :param redirect_url: The redirect_url of this Body81.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def credentials(self):
        """Gets the credentials of this Body81.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body81.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body81.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body81.  # noqa: E501
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
        if issubclass(Body81, dict):
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
        if not isinstance(other, Body81):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
