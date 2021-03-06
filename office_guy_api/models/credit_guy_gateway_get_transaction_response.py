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


class CreditGuyGatewayGetTransactionResponse(object):
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
        'code': 'str',
        'description': 'str',
        'merchant_number': 'str',
        'auth_number': 'str',
        'acquirer': 'int',
        'brand': 'int',
        'issuer': 'int',
        'file_number': 'str',
        'checkout_index': 'str',
        'checkout_record_index': 'str',
        'reference_number': 'int',
        'card_token': 'str',
        'card_fp_token': 'str',
        'card_pattern': 'str',
        'card_expiration': 'datetime',
        'parameters': 'list[str]',
        'citizen_id': 'str',
        'result_record': 'str'
    }

    attribute_map = {
        'code': 'Code',
        'description': 'Description',
        'merchant_number': 'MerchantNumber',
        'auth_number': 'AuthNumber',
        'acquirer': 'Acquirer',
        'brand': 'Brand',
        'issuer': 'Issuer',
        'file_number': 'FileNumber',
        'checkout_index': 'CheckoutIndex',
        'checkout_record_index': 'CheckoutRecordIndex',
        'reference_number': 'ReferenceNumber',
        'card_token': 'CardToken',
        'card_fp_token': 'CardFPToken',
        'card_pattern': 'CardPattern',
        'card_expiration': 'CardExpiration',
        'parameters': 'Parameters',
        'citizen_id': 'CitizenID',
        'result_record': 'ResultRecord'
    }

    def __init__(self, code=None, description=None, merchant_number=None, auth_number=None, acquirer=None, brand=None, issuer=None, file_number=None, checkout_index=None, checkout_record_index=None, reference_number=None, card_token=None, card_fp_token=None, card_pattern=None, card_expiration=None, parameters=None, citizen_id=None, result_record=None):  # noqa: E501
        """CreditGuyGatewayGetTransactionResponse - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._description = None
        self._merchant_number = None
        self._auth_number = None
        self._acquirer = None
        self._brand = None
        self._issuer = None
        self._file_number = None
        self._checkout_index = None
        self._checkout_record_index = None
        self._reference_number = None
        self._card_token = None
        self._card_fp_token = None
        self._card_pattern = None
        self._card_expiration = None
        self._parameters = None
        self._citizen_id = None
        self._result_record = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if merchant_number is not None:
            self.merchant_number = merchant_number
        if auth_number is not None:
            self.auth_number = auth_number
        if acquirer is not None:
            self.acquirer = acquirer
        if brand is not None:
            self.brand = brand
        if issuer is not None:
            self.issuer = issuer
        if file_number is not None:
            self.file_number = file_number
        if checkout_index is not None:
            self.checkout_index = checkout_index
        if checkout_record_index is not None:
            self.checkout_record_index = checkout_record_index
        if reference_number is not None:
            self.reference_number = reference_number
        if card_token is not None:
            self.card_token = card_token
        if card_fp_token is not None:
            self.card_fp_token = card_fp_token
        if card_pattern is not None:
            self.card_pattern = card_pattern
        if card_expiration is not None:
            self.card_expiration = card_expiration
        if parameters is not None:
            self.parameters = parameters
        if citizen_id is not None:
            self.citizen_id = citizen_id
        if result_record is not None:
            self.result_record = result_record

    @property
    def code(self):
        """Gets the code of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Shva result code  # noqa: E501

        :return: The code of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreditGuyGatewayGetTransactionResponse.

        Shva result code  # noqa: E501

        :param code: The code of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Shva result description  # noqa: E501

        :return: The description of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreditGuyGatewayGetTransactionResponse.

        Shva result description  # noqa: E501

        :param description: The description of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def merchant_number(self):
        """Gets the merchant_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Shva merchant number (Terminal number)  # noqa: E501

        :return: The merchant_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._merchant_number

    @merchant_number.setter
    def merchant_number(self, merchant_number):
        """Sets the merchant_number of this CreditGuyGatewayGetTransactionResponse.

        Shva merchant number (Terminal number)  # noqa: E501

        :param merchant_number: The merchant_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._merchant_number = merchant_number

    @property
    def auth_number(self):
        """Gets the auth_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Charge authorization number  # noqa: E501

        :return: The auth_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._auth_number

    @auth_number.setter
    def auth_number(self, auth_number):
        """Sets the auth_number of this CreditGuyGatewayGetTransactionResponse.

        Charge authorization number  # noqa: E501

        :param auth_number: The auth_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._auth_number = auth_number

    @property
    def acquirer(self):
        """Gets the acquirer of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Card acquirer  # noqa: E501

        :return: The acquirer of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._acquirer

    @acquirer.setter
    def acquirer(self, acquirer):
        """Sets the acquirer of this CreditGuyGatewayGetTransactionResponse.

        Card acquirer  # noqa: E501

        :param acquirer: The acquirer of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: int
        """

        self._acquirer = acquirer

    @property
    def brand(self):
        """Gets the brand of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Card brand  # noqa: E501

        :return: The brand of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this CreditGuyGatewayGetTransactionResponse.

        Card brand  # noqa: E501

        :param brand: The brand of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: int
        """

        self._brand = brand

    @property
    def issuer(self):
        """Gets the issuer of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Card issuer  # noqa: E501

        :return: The issuer of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CreditGuyGatewayGetTransactionResponse.

        Card issuer  # noqa: E501

        :param issuer: The issuer of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: int
        """

        self._issuer = issuer

    @property
    def file_number(self):
        """Gets the file_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Shva file number  # noqa: E501

        :return: The file_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        """Sets the file_number of this CreditGuyGatewayGetTransactionResponse.

        Shva file number  # noqa: E501

        :param file_number: The file_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._file_number = file_number

    @property
    def checkout_index(self):
        """Gets the checkout_index of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Shva checkout index  # noqa: E501

        :return: The checkout_index of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._checkout_index

    @checkout_index.setter
    def checkout_index(self, checkout_index):
        """Sets the checkout_index of this CreditGuyGatewayGetTransactionResponse.

        Shva checkout index  # noqa: E501

        :param checkout_index: The checkout_index of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._checkout_index = checkout_index

    @property
    def checkout_record_index(self):
        """Gets the checkout_record_index of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Shva checkout record index  # noqa: E501

        :return: The checkout_record_index of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._checkout_record_index

    @checkout_record_index.setter
    def checkout_record_index(self, checkout_record_index):
        """Sets the checkout_record_index of this CreditGuyGatewayGetTransactionResponse.

        Shva checkout record index  # noqa: E501

        :param checkout_record_index: The checkout_record_index of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._checkout_record_index = checkout_record_index

    @property
    def reference_number(self):
        """Gets the reference_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Shva reference number  # noqa: E501

        :return: The reference_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this CreditGuyGatewayGetTransactionResponse.

        Shva reference number  # noqa: E501

        :param reference_number: The reference_number of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: int
        """

        self._reference_number = reference_number

    @property
    def card_token(self):
        """Gets the card_token of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Card token  # noqa: E501

        :return: The card_token of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._card_token

    @card_token.setter
    def card_token(self, card_token):
        """Sets the card_token of this CreditGuyGatewayGetTransactionResponse.

        Card token  # noqa: E501

        :param card_token: The card_token of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._card_token = card_token

    @property
    def card_fp_token(self):
        """Gets the card_fp_token of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Format preserved token  # noqa: E501

        :return: The card_fp_token of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._card_fp_token

    @card_fp_token.setter
    def card_fp_token(self, card_fp_token):
        """Sets the card_fp_token of this CreditGuyGatewayGetTransactionResponse.

        Format preserved token  # noqa: E501

        :param card_fp_token: The card_fp_token of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._card_fp_token = card_fp_token

    @property
    def card_pattern(self):
        """Gets the card_pattern of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Card number pattern (including the last 4 digits)  # noqa: E501

        :return: The card_pattern of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._card_pattern

    @card_pattern.setter
    def card_pattern(self, card_pattern):
        """Sets the card_pattern of this CreditGuyGatewayGetTransactionResponse.

        Card number pattern (including the last 4 digits)  # noqa: E501

        :param card_pattern: The card_pattern of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._card_pattern = card_pattern

    @property
    def card_expiration(self):
        """Gets the card_expiration of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Credit card expiration  # noqa: E501

        :return: The card_expiration of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._card_expiration

    @card_expiration.setter
    def card_expiration(self, card_expiration):
        """Sets the card_expiration of this CreditGuyGatewayGetTransactionResponse.

        Credit card expiration  # noqa: E501

        :param card_expiration: The card_expiration of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: datetime
        """

        self._card_expiration = card_expiration

    @property
    def parameters(self):
        """Gets the parameters of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Card parameters, as specified in the card parameters folder.  # noqa: E501

        :return: The parameters of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this CreditGuyGatewayGetTransactionResponse.

        Card parameters, as specified in the card parameters folder.  # noqa: E501

        :param parameters: The parameters of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: list[str]
        """

        self._parameters = parameters

    @property
    def citizen_id(self):
        """Gets the citizen_id of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Israeli Citizen ID / Passport Number  # noqa: E501

        :return: The citizen_id of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._citizen_id

    @citizen_id.setter
    def citizen_id(self, citizen_id):
        """Sets the citizen_id of this CreditGuyGatewayGetTransactionResponse.

        Israeli Citizen ID / Passport Number  # noqa: E501

        :param citizen_id: The citizen_id of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._citizen_id = citizen_id

    @property
    def result_record(self):
        """Gets the result_record of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501

        Full result record received from Shva  # noqa: E501

        :return: The result_record of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_record

    @result_record.setter
    def result_record(self, result_record):
        """Sets the result_record of this CreditGuyGatewayGetTransactionResponse.

        Full result record received from Shva  # noqa: E501

        :param result_record: The result_record of this CreditGuyGatewayGetTransactionResponse.  # noqa: E501
        :type: str
        """

        self._result_record = result_record

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
        if issubclass(CreditGuyGatewayGetTransactionResponse, dict):
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
        if not isinstance(other, CreditGuyGatewayGetTransactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
