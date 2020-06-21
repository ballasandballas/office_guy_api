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


class Body75(object):
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
        'param_j': 'Object',
        'card_number': 'str',
        'format_preserving_token': 'str',
        'card_token': 'str',
        'single_use_token': 'str',
        'expiration_month': 'int',
        'expiration_year': 'int',
        'amount': 'float',
        'payments_non_first_count': 'int',
        'payments_first_amount': 'float',
        'payments_non_first_amount': 'float',
        'auth_number': 'str',
        'cvv': 'str',
        'track2': 'str',
        'citizen_id': 'str',
        'currency': 'Object',
        'language': 'str',
        'unique_identifier': 'str',
        'merchant_number': 'str',
        'transaction_type': 'Object',
        'custom_data_1': 'str',
        'custom_data_2': 'str',
        'custom_data_3': 'str',
        'custom_data_4': 'str',
        'custom_data_5': 'str',
        'multi_supplier_number': 'str',
        'credentials': 'Object'
    }
    if hasattr(CreditGuyGatewayTransactionRequest, "swagger_types"):
        swagger_types.update(CreditGuyGatewayTransactionRequest.swagger_types)

    attribute_map = {
        'param_j': 'ParamJ',
        'card_number': 'CardNumber',
        'format_preserving_token': 'FormatPreservingToken',
        'card_token': 'CardToken',
        'single_use_token': 'SingleUseToken',
        'expiration_month': 'ExpirationMonth',
        'expiration_year': 'ExpirationYear',
        'amount': 'Amount',
        'payments_non_first_count': 'PaymentsNonFirstCount',
        'payments_first_amount': 'PaymentsFirstAmount',
        'payments_non_first_amount': 'PaymentsNonFirstAmount',
        'auth_number': 'AuthNumber',
        'cvv': 'CVV',
        'track2': 'Track2',
        'citizen_id': 'CitizenID',
        'currency': 'Currency',
        'language': 'Language',
        'unique_identifier': 'UniqueIdentifier',
        'merchant_number': 'MerchantNumber',
        'transaction_type': 'TransactionType',
        'custom_data_1': 'CustomData_1',
        'custom_data_2': 'CustomData_2',
        'custom_data_3': 'CustomData_3',
        'custom_data_4': 'CustomData_4',
        'custom_data_5': 'CustomData_5',
        'multi_supplier_number': 'MultiSupplierNumber',
        'credentials': 'Credentials'
    }
    if hasattr(CreditGuyGatewayTransactionRequest, "attribute_map"):
        attribute_map.update(CreditGuyGatewayTransactionRequest.attribute_map)

    def __init__(self, param_j=None, card_number=None, format_preserving_token=None, card_token=None, single_use_token=None, expiration_month=None, expiration_year=None, amount=None, payments_non_first_count=None, payments_first_amount=None, payments_non_first_amount=None, auth_number=None, cvv=None, track2=None, citizen_id=None, currency=None, language=None, unique_identifier=None, merchant_number=None, transaction_type=None, custom_data_1=None, custom_data_2=None, custom_data_3=None, custom_data_4=None, custom_data_5=None, multi_supplier_number=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body75 - a model defined in Swagger"""  # noqa: E501
        self._param_j = None
        self._card_number = None
        self._format_preserving_token = None
        self._card_token = None
        self._single_use_token = None
        self._expiration_month = None
        self._expiration_year = None
        self._amount = None
        self._payments_non_first_count = None
        self._payments_first_amount = None
        self._payments_non_first_amount = None
        self._auth_number = None
        self._cvv = None
        self._track2 = None
        self._citizen_id = None
        self._currency = None
        self._language = None
        self._unique_identifier = None
        self._merchant_number = None
        self._transaction_type = None
        self._custom_data_1 = None
        self._custom_data_2 = None
        self._custom_data_3 = None
        self._custom_data_4 = None
        self._custom_data_5 = None
        self._multi_supplier_number = None
        self._credentials = None
        self.discriminator = None
        self.param_j = param_j
        if card_number is not None:
            self.card_number = card_number
        if format_preserving_token is not None:
            self.format_preserving_token = format_preserving_token
        if card_token is not None:
            self.card_token = card_token
        if single_use_token is not None:
            self.single_use_token = single_use_token
        if expiration_month is not None:
            self.expiration_month = expiration_month
        if expiration_year is not None:
            self.expiration_year = expiration_year
        if amount is not None:
            self.amount = amount
        if payments_non_first_count is not None:
            self.payments_non_first_count = payments_non_first_count
        if payments_first_amount is not None:
            self.payments_first_amount = payments_first_amount
        if payments_non_first_amount is not None:
            self.payments_non_first_amount = payments_non_first_amount
        if auth_number is not None:
            self.auth_number = auth_number
        if cvv is not None:
            self.cvv = cvv
        if track2 is not None:
            self.track2 = track2
        if citizen_id is not None:
            self.citizen_id = citizen_id
        if currency is not None:
            self.currency = currency
        if language is not None:
            self.language = language
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier
        if merchant_number is not None:
            self.merchant_number = merchant_number
        if transaction_type is not None:
            self.transaction_type = transaction_type
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
        if multi_supplier_number is not None:
            self.multi_supplier_number = multi_supplier_number
        self.credentials = credentials
        CreditGuyGatewayTransactionRequest.__init__(self, *args, **kwargs)

    @property
    def param_j(self):
        """Gets the param_j of this Body75.  # noqa: E501

        Transaction type  # noqa: E501

        :return: The param_j of this Body75.  # noqa: E501
        :rtype: Object
        """
        return self._param_j

    @param_j.setter
    def param_j(self, param_j):
        """Sets the param_j of this Body75.

        Transaction type  # noqa: E501

        :param param_j: The param_j of this Body75.  # noqa: E501
        :type: Object
        """
        if param_j is None:
            raise ValueError("Invalid value for `param_j`, must not be `None`")  # noqa: E501

        self._param_j = param_j

    @property
    def card_number(self):
        """Gets the card_number of this Body75.  # noqa: E501

        Full card number<div><i>Leave this empty when using FormatPreservingToken/CardToken/SingleUseToken</i></div>  # noqa: E501

        :return: The card_number of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this Body75.

        Full card number<div><i>Leave this empty when using FormatPreservingToken/CardToken/SingleUseToken</i></div>  # noqa: E501

        :param card_number: The card_number of this Body75.  # noqa: E501
        :type: str
        """

        self._card_number = card_number

    @property
    def format_preserving_token(self):
        """Gets the format_preserving_token of this Body75.  # noqa: E501

        Format preserving card number<div><i>Leave this empty when using CardNumber/CardToken/SingleUseToken</i></div>  # noqa: E501

        :return: The format_preserving_token of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._format_preserving_token

    @format_preserving_token.setter
    def format_preserving_token(self, format_preserving_token):
        """Sets the format_preserving_token of this Body75.

        Format preserving card number<div><i>Leave this empty when using CardNumber/CardToken/SingleUseToken</i></div>  # noqa: E501

        :param format_preserving_token: The format_preserving_token of this Body75.  # noqa: E501
        :type: str
        """

        self._format_preserving_token = format_preserving_token

    @property
    def card_token(self):
        """Gets the card_token of this Body75.  # noqa: E501

        Card token<div><i>Leave this empty when using CardNumber/FormatPreservingToken/SingleUseToken</i></div>  # noqa: E501

        :return: The card_token of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._card_token

    @card_token.setter
    def card_token(self, card_token):
        """Sets the card_token of this Body75.

        Card token<div><i>Leave this empty when using CardNumber/FormatPreservingToken/SingleUseToken</i></div>  # noqa: E501

        :param card_token: The card_token of this Body75.  # noqa: E501
        :type: str
        """

        self._card_token = card_token

    @property
    def single_use_token(self):
        """Gets the single_use_token of this Body75.  # noqa: E501

        Single use token, for all payment details (CardNumber, Expiration, CVV, CitizenID).<div><i>Used primarily by the Payments JavaScript API.  (Leave this empty when using CardNumber/FormatPreservingToken/CardToken)</i></div>  # noqa: E501

        :return: The single_use_token of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._single_use_token

    @single_use_token.setter
    def single_use_token(self, single_use_token):
        """Sets the single_use_token of this Body75.

        Single use token, for all payment details (CardNumber, Expiration, CVV, CitizenID).<div><i>Used primarily by the Payments JavaScript API.  (Leave this empty when using CardNumber/FormatPreservingToken/CardToken)</i></div>  # noqa: E501

        :param single_use_token: The single_use_token of this Body75.  # noqa: E501
        :type: str
        """

        self._single_use_token = single_use_token

    @property
    def expiration_month(self):
        """Gets the expiration_month of this Body75.  # noqa: E501

        Card expiration month (1-12)<div><i>Leave this empty when using SingleUseToken</i></div>  # noqa: E501

        :return: The expiration_month of this Body75.  # noqa: E501
        :rtype: int
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """Sets the expiration_month of this Body75.

        Card expiration month (1-12)<div><i>Leave this empty when using SingleUseToken</i></div>  # noqa: E501

        :param expiration_month: The expiration_month of this Body75.  # noqa: E501
        :type: int
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """Gets the expiration_year of this Body75.  # noqa: E501

        Card expiration year (4 digits)<div><i>Leave this empty when using SingleUseToken</i></div>  # noqa: E501

        :return: The expiration_year of this Body75.  # noqa: E501
        :rtype: int
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """Sets the expiration_year of this Body75.

        Card expiration year (4 digits)<div><i>Leave this empty when using SingleUseToken</i></div>  # noqa: E501

        :param expiration_year: The expiration_year of this Body75.  # noqa: E501
        :type: int
        """

        self._expiration_year = expiration_year

    @property
    def amount(self):
        """Gets the amount of this Body75.  # noqa: E501

        Transaction amount<div><i>Leave this empty when using ParamJ = CheckDetails</i></div>  # noqa: E501

        :return: The amount of this Body75.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Body75.

        Transaction amount<div><i>Leave this empty when using ParamJ = CheckDetails</i></div>  # noqa: E501

        :param amount: The amount of this Body75.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def payments_non_first_count(self):
        """Gets the payments_non_first_count of this Body75.  # noqa: E501

        Non-first payments count<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :return: The payments_non_first_count of this Body75.  # noqa: E501
        :rtype: int
        """
        return self._payments_non_first_count

    @payments_non_first_count.setter
    def payments_non_first_count(self, payments_non_first_count):
        """Sets the payments_non_first_count of this Body75.

        Non-first payments count<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :param payments_non_first_count: The payments_non_first_count of this Body75.  # noqa: E501
        :type: int
        """

        self._payments_non_first_count = payments_non_first_count

    @property
    def payments_first_amount(self):
        """Gets the payments_first_amount of this Body75.  # noqa: E501

        First payment amount<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :return: The payments_first_amount of this Body75.  # noqa: E501
        :rtype: float
        """
        return self._payments_first_amount

    @payments_first_amount.setter
    def payments_first_amount(self, payments_first_amount):
        """Sets the payments_first_amount of this Body75.

        First payment amount<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :param payments_first_amount: The payments_first_amount of this Body75.  # noqa: E501
        :type: float
        """

        self._payments_first_amount = payments_first_amount

    @property
    def payments_non_first_amount(self):
        """Gets the payments_non_first_amount of this Body75.  # noqa: E501

        Non-first payment amount<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :return: The payments_non_first_amount of this Body75.  # noqa: E501
        :rtype: float
        """
        return self._payments_non_first_amount

    @payments_non_first_amount.setter
    def payments_non_first_amount(self, payments_non_first_amount):
        """Sets the payments_non_first_amount of this Body75.

        Non-first payment amount<div><i>Leave this empty for non-payments transaction</i></div>  # noqa: E501

        :param payments_non_first_amount: The payments_non_first_amount of this Body75.  # noqa: E501
        :type: float
        """

        self._payments_non_first_amount = payments_non_first_amount

    @property
    def auth_number(self):
        """Gets the auth_number of this Body75.  # noqa: E501

        Transaction authorization number  # noqa: E501

        :return: The auth_number of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._auth_number

    @auth_number.setter
    def auth_number(self, auth_number):
        """Sets the auth_number of this Body75.

        Transaction authorization number  # noqa: E501

        :param auth_number: The auth_number of this Body75.  # noqa: E501
        :type: str
        """

        self._auth_number = auth_number

    @property
    def cvv(self):
        """Gets the cvv of this Body75.  # noqa: E501

        Card CVV/CVV2  # noqa: E501

        :return: The cvv of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        """Sets the cvv of this Body75.

        Card CVV/CVV2  # noqa: E501

        :param cvv: The cvv of this Body75.  # noqa: E501
        :type: str
        """

        self._cvv = cvv

    @property
    def track2(self):
        """Gets the track2 of this Body75.  # noqa: E501

        Card Track2  # noqa: E501

        :return: The track2 of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._track2

    @track2.setter
    def track2(self, track2):
        """Sets the track2 of this Body75.

        Card Track2  # noqa: E501

        :param track2: The track2 of this Body75.  # noqa: E501
        :type: str
        """

        self._track2 = track2

    @property
    def citizen_id(self):
        """Gets the citizen_id of this Body75.  # noqa: E501

        Israel Citizen ID / Passport Number  # noqa: E501

        :return: The citizen_id of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._citizen_id

    @citizen_id.setter
    def citizen_id(self, citizen_id):
        """Sets the citizen_id of this Body75.

        Israel Citizen ID / Passport Number  # noqa: E501

        :param citizen_id: The citizen_id of this Body75.  # noqa: E501
        :type: str
        """

        self._citizen_id = citizen_id

    @property
    def currency(self):
        """Gets the currency of this Body75.  # noqa: E501

        Transaction currency<div><i>Defaults to ILS</i></div>  # noqa: E501

        :return: The currency of this Body75.  # noqa: E501
        :rtype: Object
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Body75.

        Transaction currency<div><i>Defaults to ILS</i></div>  # noqa: E501

        :param currency: The currency of this Body75.  # noqa: E501
        :type: Object
        """

        self._currency = currency

    @property
    def language(self):
        """Gets the language of this Body75.  # noqa: E501

        Transaction language<div><i>Leave this empty to use the company default language</i></div>  # noqa: E501

        :return: The language of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Body75.

        Transaction language<div><i>Leave this empty to use the company default language</i></div>  # noqa: E501

        :param language: The language of this Body75.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this Body75.  # noqa: E501

        Unique transaction identifier.<div><i>This parameter can be used for preventing duplicate transactions</i></div>  # noqa: E501

        :return: The unique_identifier of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this Body75.

        Unique transaction identifier.<div><i>This parameter can be used for preventing duplicate transactions</i></div>  # noqa: E501

        :param unique_identifier: The unique_identifier of this Body75.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

    @property
    def merchant_number(self):
        """Gets the merchant_number of this Body75.  # noqa: E501

        Shva merchant number (Terminal number).<div><i>This parameter should only be used when multiple merchants are defined in the company.</i></div>  # noqa: E501

        :return: The merchant_number of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._merchant_number

    @merchant_number.setter
    def merchant_number(self, merchant_number):
        """Sets the merchant_number of this Body75.

        Shva merchant number (Terminal number).<div><i>This parameter should only be used when multiple merchants are defined in the company.</i></div>  # noqa: E501

        :param merchant_number: The merchant_number of this Body75.  # noqa: E501
        :type: str
        """

        self._merchant_number = merchant_number

    @property
    def transaction_type(self):
        """Gets the transaction_type of this Body75.  # noqa: E501

        Transaction type. This allows crediting or cancelling existing transaction.<div><i>Defaults to Debit</i></div>  # noqa: E501

        :return: The transaction_type of this Body75.  # noqa: E501
        :rtype: Object
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this Body75.

        Transaction type. This allows crediting or cancelling existing transaction.<div><i>Defaults to Debit</i></div>  # noqa: E501

        :param transaction_type: The transaction_type of this Body75.  # noqa: E501
        :type: Object
        """

        self._transaction_type = transaction_type

    @property
    def custom_data_1(self):
        """Gets the custom_data_1 of this Body75.  # noqa: E501

        Custom user supplied data<div><i>Supports up to 100 chars in each field</i></div>  # noqa: E501

        :return: The custom_data_1 of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._custom_data_1

    @custom_data_1.setter
    def custom_data_1(self, custom_data_1):
        """Sets the custom_data_1 of this Body75.

        Custom user supplied data<div><i>Supports up to 100 chars in each field</i></div>  # noqa: E501

        :param custom_data_1: The custom_data_1 of this Body75.  # noqa: E501
        :type: str
        """

        self._custom_data_1 = custom_data_1

    @property
    def custom_data_2(self):
        """Gets the custom_data_2 of this Body75.  # noqa: E501

        Custom user supplied data<div><i>Supports up to 100 chars in each field</i></div>  # noqa: E501

        :return: The custom_data_2 of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._custom_data_2

    @custom_data_2.setter
    def custom_data_2(self, custom_data_2):
        """Sets the custom_data_2 of this Body75.

        Custom user supplied data<div><i>Supports up to 100 chars in each field</i></div>  # noqa: E501

        :param custom_data_2: The custom_data_2 of this Body75.  # noqa: E501
        :type: str
        """

        self._custom_data_2 = custom_data_2

    @property
    def custom_data_3(self):
        """Gets the custom_data_3 of this Body75.  # noqa: E501

        Custom user supplied data<div><i>Supports up to 100 chars in each field</i></div>  # noqa: E501

        :return: The custom_data_3 of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._custom_data_3

    @custom_data_3.setter
    def custom_data_3(self, custom_data_3):
        """Sets the custom_data_3 of this Body75.

        Custom user supplied data<div><i>Supports up to 100 chars in each field</i></div>  # noqa: E501

        :param custom_data_3: The custom_data_3 of this Body75.  # noqa: E501
        :type: str
        """

        self._custom_data_3 = custom_data_3

    @property
    def custom_data_4(self):
        """Gets the custom_data_4 of this Body75.  # noqa: E501

        Custom user supplied data<div><i>Supports up to 100 chars in each field</i></div>  # noqa: E501

        :return: The custom_data_4 of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._custom_data_4

    @custom_data_4.setter
    def custom_data_4(self, custom_data_4):
        """Sets the custom_data_4 of this Body75.

        Custom user supplied data<div><i>Supports up to 100 chars in each field</i></div>  # noqa: E501

        :param custom_data_4: The custom_data_4 of this Body75.  # noqa: E501
        :type: str
        """

        self._custom_data_4 = custom_data_4

    @property
    def custom_data_5(self):
        """Gets the custom_data_5 of this Body75.  # noqa: E501

        Custom user supplied data<div><i>Supports up to 100 chars in each field</i></div>  # noqa: E501

        :return: The custom_data_5 of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._custom_data_5

    @custom_data_5.setter
    def custom_data_5(self, custom_data_5):
        """Sets the custom_data_5 of this Body75.

        Custom user supplied data<div><i>Supports up to 100 chars in each field</i></div>  # noqa: E501

        :param custom_data_5: The custom_data_5 of this Body75.  # noqa: E501
        :type: str
        """

        self._custom_data_5 = custom_data_5

    @property
    def multi_supplier_number(self):
        """Gets the multi_supplier_number of this Body75.  # noqa: E501

        Multi supplier number.  # noqa: E501

        :return: The multi_supplier_number of this Body75.  # noqa: E501
        :rtype: str
        """
        return self._multi_supplier_number

    @multi_supplier_number.setter
    def multi_supplier_number(self, multi_supplier_number):
        """Sets the multi_supplier_number of this Body75.

        Multi supplier number.  # noqa: E501

        :param multi_supplier_number: The multi_supplier_number of this Body75.  # noqa: E501
        :type: str
        """

        self._multi_supplier_number = multi_supplier_number

    @property
    def credentials(self):
        """Gets the credentials of this Body75.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body75.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body75.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body75.  # noqa: E501
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
        if issubclass(Body75, dict):
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
        if not isinstance(other, Body75):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
