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


class CreditGuyGatewayTransactionResponse(object):
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
        'success': 'bool',
        'result_code': 'str',
        'result_description': 'str',
        'transaction_id': 'int',
        'file_number': 'str',
        'checkout_index': 'str',
        'checkout_record_index': 'str',
        'acquirer': 'int',
        'brand': 'int',
        'issuer': 'int',
        'auth_number': 'str',
        'card_token': 'str',
        'expiration_month': 'int',
        'expiration_year': 'int',
        'citizen_id': 'str'
    }

    attribute_map = {
        'success': 'Success',
        'result_code': 'ResultCode',
        'result_description': 'ResultDescription',
        'transaction_id': 'TransactionID',
        'file_number': 'FileNumber',
        'checkout_index': 'CheckoutIndex',
        'checkout_record_index': 'CheckoutRecordIndex',
        'acquirer': 'Acquirer',
        'brand': 'Brand',
        'issuer': 'Issuer',
        'auth_number': 'AuthNumber',
        'card_token': 'CardToken',
        'expiration_month': 'ExpirationMonth',
        'expiration_year': 'ExpirationYear',
        'citizen_id': 'CitizenID'
    }

    def __init__(self, success=None, result_code=None, result_description=None, transaction_id=None, file_number=None, checkout_index=None, checkout_record_index=None, acquirer=None, brand=None, issuer=None, auth_number=None, card_token=None, expiration_month=None, expiration_year=None, citizen_id=None):  # noqa: E501
        """CreditGuyGatewayTransactionResponse - a model defined in Swagger"""  # noqa: E501
        self._success = None
        self._result_code = None
        self._result_description = None
        self._transaction_id = None
        self._file_number = None
        self._checkout_index = None
        self._checkout_record_index = None
        self._acquirer = None
        self._brand = None
        self._issuer = None
        self._auth_number = None
        self._card_token = None
        self._expiration_month = None
        self._expiration_year = None
        self._citizen_id = None
        self.discriminator = None
        if success is not None:
            self.success = success
        if result_code is not None:
            self.result_code = result_code
        if result_description is not None:
            self.result_description = result_description
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if file_number is not None:
            self.file_number = file_number
        if checkout_index is not None:
            self.checkout_index = checkout_index
        if checkout_record_index is not None:
            self.checkout_record_index = checkout_record_index
        if acquirer is not None:
            self.acquirer = acquirer
        if brand is not None:
            self.brand = brand
        if issuer is not None:
            self.issuer = issuer
        if auth_number is not None:
            self.auth_number = auth_number
        if card_token is not None:
            self.card_token = card_token
        if expiration_month is not None:
            self.expiration_month = expiration_month
        if expiration_year is not None:
            self.expiration_year = expiration_year
        if citizen_id is not None:
            self.citizen_id = citizen_id

    @property
    def success(self):
        """Gets the success of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Is valid transaction  # noqa: E501

        :return: The success of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this CreditGuyGatewayTransactionResponse.

        Is valid transaction  # noqa: E501

        :param success: The success of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def result_code(self):
        """Gets the result_code of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Shva result code (000 is valid)  # noqa: E501

        :return: The result_code of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this CreditGuyGatewayTransactionResponse.

        Shva result code (000 is valid)  # noqa: E501

        :param result_code: The result_code of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: str
        """

        self._result_code = result_code

    @property
    def result_description(self):
        """Gets the result_description of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Shva result description  # noqa: E501

        :return: The result_description of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._result_description

    @result_description.setter
    def result_description(self, result_description):
        """Sets the result_description of this CreditGuyGatewayTransactionResponse.

        Shva result description  # noqa: E501

        :param result_description: The result_description of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: str
        """

        self._result_description = result_description

    @property
    def transaction_id(self):
        """Gets the transaction_id of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        CreditGuy transaction identifier  # noqa: E501

        :return: The transaction_id of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this CreditGuyGatewayTransactionResponse.

        CreditGuy transaction identifier  # noqa: E501

        :param transaction_id: The transaction_id of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: int
        """

        self._transaction_id = transaction_id

    @property
    def file_number(self):
        """Gets the file_number of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Shva file number  # noqa: E501

        :return: The file_number of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        """Sets the file_number of this CreditGuyGatewayTransactionResponse.

        Shva file number  # noqa: E501

        :param file_number: The file_number of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: str
        """

        self._file_number = file_number

    @property
    def checkout_index(self):
        """Gets the checkout_index of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Shva checkout index  # noqa: E501

        :return: The checkout_index of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._checkout_index

    @checkout_index.setter
    def checkout_index(self, checkout_index):
        """Sets the checkout_index of this CreditGuyGatewayTransactionResponse.

        Shva checkout index  # noqa: E501

        :param checkout_index: The checkout_index of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: str
        """

        self._checkout_index = checkout_index

    @property
    def checkout_record_index(self):
        """Gets the checkout_record_index of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Shva checkout record index  # noqa: E501

        :return: The checkout_record_index of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._checkout_record_index

    @checkout_record_index.setter
    def checkout_record_index(self, checkout_record_index):
        """Sets the checkout_record_index of this CreditGuyGatewayTransactionResponse.

        Shva checkout record index  # noqa: E501

        :param checkout_record_index: The checkout_record_index of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: str
        """

        self._checkout_record_index = checkout_record_index

    @property
    def acquirer(self):
        """Gets the acquirer of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Card acquirer  # noqa: E501

        :return: The acquirer of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._acquirer

    @acquirer.setter
    def acquirer(self, acquirer):
        """Sets the acquirer of this CreditGuyGatewayTransactionResponse.

        Card acquirer  # noqa: E501

        :param acquirer: The acquirer of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: int
        """

        self._acquirer = acquirer

    @property
    def brand(self):
        """Gets the brand of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Card brand  # noqa: E501

        :return: The brand of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this CreditGuyGatewayTransactionResponse.

        Card brand  # noqa: E501

        :param brand: The brand of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: int
        """

        self._brand = brand

    @property
    def issuer(self):
        """Gets the issuer of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Card issuer  # noqa: E501

        :return: The issuer of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CreditGuyGatewayTransactionResponse.

        Card issuer  # noqa: E501

        :param issuer: The issuer of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: int
        """

        self._issuer = issuer

    @property
    def auth_number(self):
        """Gets the auth_number of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Charge authorization number  # noqa: E501

        :return: The auth_number of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._auth_number

    @auth_number.setter
    def auth_number(self, auth_number):
        """Sets the auth_number of this CreditGuyGatewayTransactionResponse.

        Charge authorization number  # noqa: E501

        :param auth_number: The auth_number of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: str
        """

        self._auth_number = auth_number

    @property
    def card_token(self):
        """Gets the card_token of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Card token, this field may be stored on non-pci compliant systems  # noqa: E501

        :return: The card_token of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._card_token

    @card_token.setter
    def card_token(self, card_token):
        """Sets the card_token of this CreditGuyGatewayTransactionResponse.

        Card token, this field may be stored on non-pci compliant systems  # noqa: E501

        :param card_token: The card_token of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: str
        """

        self._card_token = card_token

    @property
    def expiration_month(self):
        """Gets the expiration_month of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Card expiration month (1-12), this field may be stored on non-pci compliant systems  # noqa: E501

        :return: The expiration_month of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """Sets the expiration_month of this CreditGuyGatewayTransactionResponse.

        Card expiration month (1-12), this field may be stored on non-pci compliant systems  # noqa: E501

        :param expiration_month: The expiration_month of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: int
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """Gets the expiration_year of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Card expiration year (4 digits), this field may be stored on non-pci compliant systems  # noqa: E501

        :return: The expiration_year of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: int
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """Sets the expiration_year of this CreditGuyGatewayTransactionResponse.

        Card expiration year (4 digits), this field may be stored on non-pci compliant systems  # noqa: E501

        :param expiration_year: The expiration_year of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: int
        """

        self._expiration_year = expiration_year

    @property
    def citizen_id(self):
        """Gets the citizen_id of this CreditGuyGatewayTransactionResponse.  # noqa: E501

        Israel Citizen ID / Passport Number, this field may be stored on non pci-compliant systems  # noqa: E501

        :return: The citizen_id of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :rtype: str
        """
        return self._citizen_id

    @citizen_id.setter
    def citizen_id(self, citizen_id):
        """Sets the citizen_id of this CreditGuyGatewayTransactionResponse.

        Israel Citizen ID / Passport Number, this field may be stored on non pci-compliant systems  # noqa: E501

        :param citizen_id: The citizen_id of this CreditGuyGatewayTransactionResponse.  # noqa: E501
        :type: str
        """

        self._citizen_id = citizen_id

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
        if issubclass(CreditGuyGatewayTransactionResponse, dict):
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
        if not isinstance(other, CreditGuyGatewayTransactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
