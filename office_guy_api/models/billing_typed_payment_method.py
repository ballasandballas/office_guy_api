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


class BillingTypedPaymentMethod(object):
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
        'id': 'int',
        'customer_id': 'int',
        'credit_card_number': 'str',
        'credit_card_last_digits': 'str',
        'credit_card_expiration_month': 'int',
        'credit_card_expiration_year': 'int',
        'credit_card_cvv': 'str',
        'credit_card_track2': 'str',
        'credit_card_citizen_id': 'str',
        'credit_card_card_mask': 'str',
        'credit_card_token': 'str',
        'direct_debit_bank': 'int',
        'direct_debit_branch': 'int',
        'direct_debit_account': 'int',
        'direct_debit_expiration_date': 'datetime',
        'direct_debit_maximum_amount': 'int',
        'type': 'AllOfBillingTypedPaymentMethodType'
    }

    attribute_map = {
        'id': 'ID',
        'customer_id': 'CustomerID',
        'credit_card_number': 'CreditCard_Number',
        'credit_card_last_digits': 'CreditCard_LastDigits',
        'credit_card_expiration_month': 'CreditCard_ExpirationMonth',
        'credit_card_expiration_year': 'CreditCard_ExpirationYear',
        'credit_card_cvv': 'CreditCard_CVV',
        'credit_card_track2': 'CreditCard_Track2',
        'credit_card_citizen_id': 'CreditCard_CitizenID',
        'credit_card_card_mask': 'CreditCard_CardMask',
        'credit_card_token': 'CreditCard_Token',
        'direct_debit_bank': 'DirectDebit_Bank',
        'direct_debit_branch': 'DirectDebit_Branch',
        'direct_debit_account': 'DirectDebit_Account',
        'direct_debit_expiration_date': 'DirectDebit_ExpirationDate',
        'direct_debit_maximum_amount': 'DirectDebit_MaximumAmount',
        'type': 'Type'
    }

    def __init__(self, id=None, customer_id=None, credit_card_number=None, credit_card_last_digits=None, credit_card_expiration_month=None, credit_card_expiration_year=None, credit_card_cvv=None, credit_card_track2=None, credit_card_citizen_id=None, credit_card_card_mask=None, credit_card_token=None, direct_debit_bank=None, direct_debit_branch=None, direct_debit_account=None, direct_debit_expiration_date=None, direct_debit_maximum_amount=None, type=None):  # noqa: E501
        """BillingTypedPaymentMethod - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._customer_id = None
        self._credit_card_number = None
        self._credit_card_last_digits = None
        self._credit_card_expiration_month = None
        self._credit_card_expiration_year = None
        self._credit_card_cvv = None
        self._credit_card_track2 = None
        self._credit_card_citizen_id = None
        self._credit_card_card_mask = None
        self._credit_card_token = None
        self._direct_debit_bank = None
        self._direct_debit_branch = None
        self._direct_debit_account = None
        self._direct_debit_expiration_date = None
        self._direct_debit_maximum_amount = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if customer_id is not None:
            self.customer_id = customer_id
        if credit_card_number is not None:
            self.credit_card_number = credit_card_number
        if credit_card_last_digits is not None:
            self.credit_card_last_digits = credit_card_last_digits
        if credit_card_expiration_month is not None:
            self.credit_card_expiration_month = credit_card_expiration_month
        if credit_card_expiration_year is not None:
            self.credit_card_expiration_year = credit_card_expiration_year
        if credit_card_cvv is not None:
            self.credit_card_cvv = credit_card_cvv
        if credit_card_track2 is not None:
            self.credit_card_track2 = credit_card_track2
        if credit_card_citizen_id is not None:
            self.credit_card_citizen_id = credit_card_citizen_id
        if credit_card_card_mask is not None:
            self.credit_card_card_mask = credit_card_card_mask
        if credit_card_token is not None:
            self.credit_card_token = credit_card_token
        if direct_debit_bank is not None:
            self.direct_debit_bank = direct_debit_bank
        if direct_debit_branch is not None:
            self.direct_debit_branch = direct_debit_branch
        if direct_debit_account is not None:
            self.direct_debit_account = direct_debit_account
        if direct_debit_expiration_date is not None:
            self.direct_debit_expiration_date = direct_debit_expiration_date
        if direct_debit_maximum_amount is not None:
            self.direct_debit_maximum_amount = direct_debit_maximum_amount
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this BillingTypedPaymentMethod.  # noqa: E501


        :return: The id of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BillingTypedPaymentMethod.


        :param id: The id of this BillingTypedPaymentMethod.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def customer_id(self):
        """Gets the customer_id of this BillingTypedPaymentMethod.  # noqa: E501


        :return: The customer_id of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this BillingTypedPaymentMethod.


        :param customer_id: The customer_id of this BillingTypedPaymentMethod.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def credit_card_number(self):
        """Gets the credit_card_number of this BillingTypedPaymentMethod.  # noqa: E501

        Credit card full number<div><i>Required for credit card</i></div>  # noqa: E501

        :return: The credit_card_number of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_number

    @credit_card_number.setter
    def credit_card_number(self, credit_card_number):
        """Sets the credit_card_number of this BillingTypedPaymentMethod.

        Credit card full number<div><i>Required for credit card</i></div>  # noqa: E501

        :param credit_card_number: The credit_card_number of this BillingTypedPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_number = credit_card_number

    @property
    def credit_card_last_digits(self):
        """Gets the credit_card_last_digits of this BillingTypedPaymentMethod.  # noqa: E501

        Credit card last 4 digits<div><i>Shouldn't be input by API caller</i></div>  # noqa: E501

        :return: The credit_card_last_digits of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_last_digits

    @credit_card_last_digits.setter
    def credit_card_last_digits(self, credit_card_last_digits):
        """Sets the credit_card_last_digits of this BillingTypedPaymentMethod.

        Credit card last 4 digits<div><i>Shouldn't be input by API caller</i></div>  # noqa: E501

        :param credit_card_last_digits: The credit_card_last_digits of this BillingTypedPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_last_digits = credit_card_last_digits

    @property
    def credit_card_expiration_month(self):
        """Gets the credit_card_expiration_month of this BillingTypedPaymentMethod.  # noqa: E501

        Credit card expiration month (1-2 digits)<div><i>Required for credit card</i></div>  # noqa: E501

        :return: The credit_card_expiration_month of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._credit_card_expiration_month

    @credit_card_expiration_month.setter
    def credit_card_expiration_month(self, credit_card_expiration_month):
        """Sets the credit_card_expiration_month of this BillingTypedPaymentMethod.

        Credit card expiration month (1-2 digits)<div><i>Required for credit card</i></div>  # noqa: E501

        :param credit_card_expiration_month: The credit_card_expiration_month of this BillingTypedPaymentMethod.  # noqa: E501
        :type: int
        """

        self._credit_card_expiration_month = credit_card_expiration_month

    @property
    def credit_card_expiration_year(self):
        """Gets the credit_card_expiration_year of this BillingTypedPaymentMethod.  # noqa: E501

        Credit card expiration year (4 digits)<div><i>Required for credit card</i></div>  # noqa: E501

        :return: The credit_card_expiration_year of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._credit_card_expiration_year

    @credit_card_expiration_year.setter
    def credit_card_expiration_year(self, credit_card_expiration_year):
        """Sets the credit_card_expiration_year of this BillingTypedPaymentMethod.

        Credit card expiration year (4 digits)<div><i>Required for credit card</i></div>  # noqa: E501

        :param credit_card_expiration_year: The credit_card_expiration_year of this BillingTypedPaymentMethod.  # noqa: E501
        :type: int
        """

        self._credit_card_expiration_year = credit_card_expiration_year

    @property
    def credit_card_cvv(self):
        """Gets the credit_card_cvv of this BillingTypedPaymentMethod.  # noqa: E501

        Credit card CVV/CVV2<div><i>Required when CVV is required by credit company</i></div>  # noqa: E501

        :return: The credit_card_cvv of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_cvv

    @credit_card_cvv.setter
    def credit_card_cvv(self, credit_card_cvv):
        """Sets the credit_card_cvv of this BillingTypedPaymentMethod.

        Credit card CVV/CVV2<div><i>Required when CVV is required by credit company</i></div>  # noqa: E501

        :param credit_card_cvv: The credit_card_cvv of this BillingTypedPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_cvv = credit_card_cvv

    @property
    def credit_card_track2(self):
        """Gets the credit_card_track2 of this BillingTypedPaymentMethod.  # noqa: E501

        Credit card Track2  # noqa: E501

        :return: The credit_card_track2 of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_track2

    @credit_card_track2.setter
    def credit_card_track2(self, credit_card_track2):
        """Sets the credit_card_track2 of this BillingTypedPaymentMethod.

        Credit card Track2  # noqa: E501

        :param credit_card_track2: The credit_card_track2 of this BillingTypedPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_track2 = credit_card_track2

    @property
    def credit_card_citizen_id(self):
        """Gets the credit_card_citizen_id of this BillingTypedPaymentMethod.  # noqa: E501

        Credit card owner Israel Citizen ID / Passport Number<div><i>Required when Citizen ID is required by credit company</i></div>  # noqa: E501

        :return: The credit_card_citizen_id of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_citizen_id

    @credit_card_citizen_id.setter
    def credit_card_citizen_id(self, credit_card_citizen_id):
        """Sets the credit_card_citizen_id of this BillingTypedPaymentMethod.

        Credit card owner Israel Citizen ID / Passport Number<div><i>Required when Citizen ID is required by credit company</i></div>  # noqa: E501

        :param credit_card_citizen_id: The credit_card_citizen_id of this BillingTypedPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_citizen_id = credit_card_citizen_id

    @property
    def credit_card_card_mask(self):
        """Gets the credit_card_card_mask of this BillingTypedPaymentMethod.  # noqa: E501

        Credit card mask<div><i>Shouldn't be input by API caller</i></div>  # noqa: E501

        :return: The credit_card_card_mask of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_card_mask

    @credit_card_card_mask.setter
    def credit_card_card_mask(self, credit_card_card_mask):
        """Sets the credit_card_card_mask of this BillingTypedPaymentMethod.

        Credit card mask<div><i>Shouldn't be input by API caller</i></div>  # noqa: E501

        :param credit_card_card_mask: The credit_card_card_mask of this BillingTypedPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_card_mask = credit_card_card_mask

    @property
    def credit_card_token(self):
        """Gets the credit_card_token of this BillingTypedPaymentMethod.  # noqa: E501

        Credit card token  # noqa: E501

        :return: The credit_card_token of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._credit_card_token

    @credit_card_token.setter
    def credit_card_token(self, credit_card_token):
        """Sets the credit_card_token of this BillingTypedPaymentMethod.

        Credit card token  # noqa: E501

        :param credit_card_token: The credit_card_token of this BillingTypedPaymentMethod.  # noqa: E501
        :type: str
        """

        self._credit_card_token = credit_card_token

    @property
    def direct_debit_bank(self):
        """Gets the direct_debit_bank of this BillingTypedPaymentMethod.  # noqa: E501

        Direct debit bank number<div><i>For instance, 12 indicates Bank Hapoalim.</i></div>  # noqa: E501

        :return: The direct_debit_bank of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._direct_debit_bank

    @direct_debit_bank.setter
    def direct_debit_bank(self, direct_debit_bank):
        """Sets the direct_debit_bank of this BillingTypedPaymentMethod.

        Direct debit bank number<div><i>For instance, 12 indicates Bank Hapoalim.</i></div>  # noqa: E501

        :param direct_debit_bank: The direct_debit_bank of this BillingTypedPaymentMethod.  # noqa: E501
        :type: int
        """

        self._direct_debit_bank = direct_debit_bank

    @property
    def direct_debit_branch(self):
        """Gets the direct_debit_branch of this BillingTypedPaymentMethod.  # noqa: E501

        Direct debit bank branch number  # noqa: E501

        :return: The direct_debit_branch of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._direct_debit_branch

    @direct_debit_branch.setter
    def direct_debit_branch(self, direct_debit_branch):
        """Sets the direct_debit_branch of this BillingTypedPaymentMethod.

        Direct debit bank branch number  # noqa: E501

        :param direct_debit_branch: The direct_debit_branch of this BillingTypedPaymentMethod.  # noqa: E501
        :type: int
        """

        self._direct_debit_branch = direct_debit_branch

    @property
    def direct_debit_account(self):
        """Gets the direct_debit_account of this BillingTypedPaymentMethod.  # noqa: E501

        Direct debit bank account number  # noqa: E501

        :return: The direct_debit_account of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._direct_debit_account

    @direct_debit_account.setter
    def direct_debit_account(self, direct_debit_account):
        """Sets the direct_debit_account of this BillingTypedPaymentMethod.

        Direct debit bank account number  # noqa: E501

        :param direct_debit_account: The direct_debit_account of this BillingTypedPaymentMethod.  # noqa: E501
        :type: int
        """

        self._direct_debit_account = direct_debit_account

    @property
    def direct_debit_expiration_date(self):
        """Gets the direct_debit_expiration_date of this BillingTypedPaymentMethod.  # noqa: E501

        Direct debit expiration date  # noqa: E501

        :return: The direct_debit_expiration_date of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: datetime
        """
        return self._direct_debit_expiration_date

    @direct_debit_expiration_date.setter
    def direct_debit_expiration_date(self, direct_debit_expiration_date):
        """Sets the direct_debit_expiration_date of this BillingTypedPaymentMethod.

        Direct debit expiration date  # noqa: E501

        :param direct_debit_expiration_date: The direct_debit_expiration_date of this BillingTypedPaymentMethod.  # noqa: E501
        :type: datetime
        """

        self._direct_debit_expiration_date = direct_debit_expiration_date

    @property
    def direct_debit_maximum_amount(self):
        """Gets the direct_debit_maximum_amount of this BillingTypedPaymentMethod.  # noqa: E501

        Direct debit maximum charge amount  # noqa: E501

        :return: The direct_debit_maximum_amount of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: int
        """
        return self._direct_debit_maximum_amount

    @direct_debit_maximum_amount.setter
    def direct_debit_maximum_amount(self, direct_debit_maximum_amount):
        """Sets the direct_debit_maximum_amount of this BillingTypedPaymentMethod.

        Direct debit maximum charge amount  # noqa: E501

        :param direct_debit_maximum_amount: The direct_debit_maximum_amount of this BillingTypedPaymentMethod.  # noqa: E501
        :type: int
        """

        self._direct_debit_maximum_amount = direct_debit_maximum_amount

    @property
    def type(self):
        """Gets the type of this BillingTypedPaymentMethod.  # noqa: E501

        Payment method type  # noqa: E501

        :return: The type of this BillingTypedPaymentMethod.  # noqa: E501
        :rtype: AllOfBillingTypedPaymentMethodType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BillingTypedPaymentMethod.

        Payment method type  # noqa: E501

        :param type: The type of this BillingTypedPaymentMethod.  # noqa: E501
        :type: AllOfBillingTypedPaymentMethodType
        """

        self._type = type

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
        if issubclass(BillingTypedPaymentMethod, dict):
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
        if not isinstance(other, BillingTypedPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
