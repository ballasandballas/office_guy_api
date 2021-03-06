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


class CreditGuyBillingLoadRequestLoadRequestTransaction(object):
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
        'format_preserving_token': 'str',
        'card_token': 'str',
        'expiration_month': 'int',
        'expiration_year': 'int',
        'amount': 'float',
        'payments_non_first_count': 'int',
        'payments_first_amount': 'float',
        'payments_non_first_amount': 'float',
        'auth_number': 'str',
        'citizen_id': 'str',
        'currency': 'str',
        'unique_identifier': 'str',
        'merchant_number': 'str',
        'custom_data_1': 'str',
        'custom_data_2': 'str',
        'custom_data_3': 'str',
        'custom_data_4': 'str',
        'custom_data_5': 'str'
    }

    attribute_map = {
        'format_preserving_token': 'FormatPreservingToken',
        'card_token': 'CardToken',
        'expiration_month': 'ExpirationMonth',
        'expiration_year': 'ExpirationYear',
        'amount': 'Amount',
        'payments_non_first_count': 'PaymentsNonFirstCount',
        'payments_first_amount': 'PaymentsFirstAmount',
        'payments_non_first_amount': 'PaymentsNonFirstAmount',
        'auth_number': 'AuthNumber',
        'citizen_id': 'CitizenID',
        'currency': 'Currency',
        'unique_identifier': 'UniqueIdentifier',
        'merchant_number': 'MerchantNumber',
        'custom_data_1': 'CustomData_1',
        'custom_data_2': 'CustomData_2',
        'custom_data_3': 'CustomData_3',
        'custom_data_4': 'CustomData_4',
        'custom_data_5': 'CustomData_5'
    }

    def __init__(self, format_preserving_token=None, card_token=None, expiration_month=None, expiration_year=None, amount=None, payments_non_first_count=None, payments_first_amount=None, payments_non_first_amount=None, auth_number=None, citizen_id=None, currency=None, unique_identifier=None, merchant_number=None, custom_data_1=None, custom_data_2=None, custom_data_3=None, custom_data_4=None, custom_data_5=None):  # noqa: E501
        """CreditGuyBillingLoadRequestLoadRequestTransaction - a model defined in Swagger"""  # noqa: E501

        self._format_preserving_token = None
        self._card_token = None
        self._expiration_month = None
        self._expiration_year = None
        self._amount = None
        self._payments_non_first_count = None
        self._payments_first_amount = None
        self._payments_non_first_amount = None
        self._auth_number = None
        self._citizen_id = None
        self._currency = None
        self._unique_identifier = None
        self._merchant_number = None
        self._custom_data_1 = None
        self._custom_data_2 = None
        self._custom_data_3 = None
        self._custom_data_4 = None
        self._custom_data_5 = None
        self.discriminator = None

        if format_preserving_token is not None:
            self.format_preserving_token = format_preserving_token
        if card_token is not None:
            self.card_token = card_token
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.amount = amount
        if payments_non_first_count is not None:
            self.payments_non_first_count = payments_non_first_count
        if payments_first_amount is not None:
            self.payments_first_amount = payments_first_amount
        if payments_non_first_amount is not None:
            self.payments_non_first_amount = payments_non_first_amount
        if auth_number is not None:
            self.auth_number = auth_number
        if citizen_id is not None:
            self.citizen_id = citizen_id
        if currency is not None:
            self.currency = currency
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier
        if merchant_number is not None:
            self.merchant_number = merchant_number
        if custom_data_1 is not None:
            self.custom_data_1 = custom_data_1
        if custom_data_2 is not None:
            self.custom_data_2 = custom_data_2
        if custom_data_3 is not None:
            self.custom_data_3 = custom_data_3
        if custom_data_4 is not None:
            self.custom_data_4 = custom_data_4
        if custom_data_5 is not None:
            self.custom_data_5 = custom_data_5

    @property
    def format_preserving_token(self):
        """Gets the format_preserving_token of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The format_preserving_token of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._format_preserving_token

    @format_preserving_token.setter
    def format_preserving_token(self, format_preserving_token):
        """Sets the format_preserving_token of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param format_preserving_token: The format_preserving_token of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._format_preserving_token = format_preserving_token

    @property
    def card_token(self):
        """Gets the card_token of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The card_token of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._card_token

    @card_token.setter
    def card_token(self, card_token):
        """Sets the card_token of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param card_token: The card_token of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._card_token = card_token

    @property
    def expiration_month(self):
        """Gets the expiration_month of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The expiration_month of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: int
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """Sets the expiration_month of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param expiration_month: The expiration_month of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: int
        """
        if expiration_month is None:
            raise ValueError("Invalid value for `expiration_month`, must not be `None`")  # noqa: E501

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """Gets the expiration_year of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The expiration_year of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: int
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """Sets the expiration_year of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param expiration_year: The expiration_year of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: int
        """
        if expiration_year is None:
            raise ValueError("Invalid value for `expiration_year`, must not be `None`")  # noqa: E501

        self._expiration_year = expiration_year

    @property
    def amount(self):
        """Gets the amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param amount: The amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def payments_non_first_count(self):
        """Gets the payments_non_first_count of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The payments_non_first_count of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: int
        """
        return self._payments_non_first_count

    @payments_non_first_count.setter
    def payments_non_first_count(self, payments_non_first_count):
        """Sets the payments_non_first_count of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param payments_non_first_count: The payments_non_first_count of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: int
        """

        self._payments_non_first_count = payments_non_first_count

    @property
    def payments_first_amount(self):
        """Gets the payments_first_amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The payments_first_amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: float
        """
        return self._payments_first_amount

    @payments_first_amount.setter
    def payments_first_amount(self, payments_first_amount):
        """Sets the payments_first_amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param payments_first_amount: The payments_first_amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: float
        """

        self._payments_first_amount = payments_first_amount

    @property
    def payments_non_first_amount(self):
        """Gets the payments_non_first_amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The payments_non_first_amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: float
        """
        return self._payments_non_first_amount

    @payments_non_first_amount.setter
    def payments_non_first_amount(self, payments_non_first_amount):
        """Sets the payments_non_first_amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param payments_non_first_amount: The payments_non_first_amount of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: float
        """

        self._payments_non_first_amount = payments_non_first_amount

    @property
    def auth_number(self):
        """Gets the auth_number of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The auth_number of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._auth_number

    @auth_number.setter
    def auth_number(self, auth_number):
        """Sets the auth_number of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param auth_number: The auth_number of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._auth_number = auth_number

    @property
    def citizen_id(self):
        """Gets the citizen_id of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The citizen_id of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._citizen_id

    @citizen_id.setter
    def citizen_id(self, citizen_id):
        """Sets the citizen_id of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param citizen_id: The citizen_id of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._citizen_id = citizen_id

    @property
    def currency(self):
        """Gets the currency of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The currency of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param currency: The currency of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """
        allowed_values = ["ILS", "USD", "EURO"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The unique_identifier of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param unique_identifier: The unique_identifier of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

    @property
    def merchant_number(self):
        """Gets the merchant_number of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The merchant_number of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._merchant_number

    @merchant_number.setter
    def merchant_number(self, merchant_number):
        """Sets the merchant_number of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param merchant_number: The merchant_number of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._merchant_number = merchant_number

    @property
    def custom_data_1(self):
        """Gets the custom_data_1 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The custom_data_1 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._custom_data_1

    @custom_data_1.setter
    def custom_data_1(self, custom_data_1):
        """Sets the custom_data_1 of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param custom_data_1: The custom_data_1 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._custom_data_1 = custom_data_1

    @property
    def custom_data_2(self):
        """Gets the custom_data_2 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The custom_data_2 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._custom_data_2

    @custom_data_2.setter
    def custom_data_2(self, custom_data_2):
        """Sets the custom_data_2 of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param custom_data_2: The custom_data_2 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._custom_data_2 = custom_data_2

    @property
    def custom_data_3(self):
        """Gets the custom_data_3 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The custom_data_3 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._custom_data_3

    @custom_data_3.setter
    def custom_data_3(self, custom_data_3):
        """Sets the custom_data_3 of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param custom_data_3: The custom_data_3 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._custom_data_3 = custom_data_3

    @property
    def custom_data_4(self):
        """Gets the custom_data_4 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The custom_data_4 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._custom_data_4

    @custom_data_4.setter
    def custom_data_4(self, custom_data_4):
        """Sets the custom_data_4 of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param custom_data_4: The custom_data_4 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._custom_data_4 = custom_data_4

    @property
    def custom_data_5(self):
        """Gets the custom_data_5 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501


        :return: The custom_data_5 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :rtype: str
        """
        return self._custom_data_5

    @custom_data_5.setter
    def custom_data_5(self, custom_data_5):
        """Sets the custom_data_5 of this CreditGuyBillingLoadRequestLoadRequestTransaction.


        :param custom_data_5: The custom_data_5 of this CreditGuyBillingLoadRequestLoadRequestTransaction.  # noqa: E501
        :type: str
        """

        self._custom_data_5 = custom_data_5

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
        if issubclass(CreditGuyBillingLoadRequestLoadRequestTransaction, dict):
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
        if not isinstance(other, CreditGuyBillingLoadRequestLoadRequestTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
