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


class BillingTypedPayment(object):
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
        '_date': 'datetime',
        'valid_payment': 'bool',
        'status': 'str',
        'status_description': 'str',
        'amount': 'float',
        'payment_method': 'BillingTypedPaymentMethod',
        'auth_number': 'str',
        'recurring_customer_item_i_ds': 'list[int]'
    }

    attribute_map = {
        'id': 'ID',
        'customer_id': 'CustomerID',
        '_date': 'Date',
        'valid_payment': 'ValidPayment',
        'status': 'Status',
        'status_description': 'StatusDescription',
        'amount': 'Amount',
        'payment_method': 'PaymentMethod',
        'auth_number': 'AuthNumber',
        'recurring_customer_item_i_ds': 'RecurringCustomerItemIDs'
    }

    def __init__(self, id=None, customer_id=None, _date=None, valid_payment=None, status=None, status_description=None, amount=None, payment_method=None, auth_number=None, recurring_customer_item_i_ds=None):  # noqa: E501
        """BillingTypedPayment - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._customer_id = None
        self.__date = None
        self._valid_payment = None
        self._status = None
        self._status_description = None
        self._amount = None
        self._payment_method = None
        self._auth_number = None
        self._recurring_customer_item_i_ds = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if customer_id is not None:
            self.customer_id = customer_id
        if _date is not None:
            self._date = _date
        if valid_payment is not None:
            self.valid_payment = valid_payment
        if status is not None:
            self.status = status
        if status_description is not None:
            self.status_description = status_description
        if amount is not None:
            self.amount = amount
        if payment_method is not None:
            self.payment_method = payment_method
        if auth_number is not None:
            self.auth_number = auth_number
        if recurring_customer_item_i_ds is not None:
            self.recurring_customer_item_i_ds = recurring_customer_item_i_ds

    @property
    def id(self):
        """Gets the id of this BillingTypedPayment.  # noqa: E501

        Payment identifier  # noqa: E501

        :return: The id of this BillingTypedPayment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BillingTypedPayment.

        Payment identifier  # noqa: E501

        :param id: The id of this BillingTypedPayment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def customer_id(self):
        """Gets the customer_id of this BillingTypedPayment.  # noqa: E501

        Customer identifier  # noqa: E501

        :return: The customer_id of this BillingTypedPayment.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this BillingTypedPayment.

        Customer identifier  # noqa: E501

        :param customer_id: The customer_id of this BillingTypedPayment.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def _date(self):
        """Gets the _date of this BillingTypedPayment.  # noqa: E501

        Payment date  # noqa: E501

        :return: The _date of this BillingTypedPayment.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this BillingTypedPayment.

        Payment date  # noqa: E501

        :param _date: The _date of this BillingTypedPayment.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def valid_payment(self):
        """Gets the valid_payment of this BillingTypedPayment.  # noqa: E501

        Indicates if the payment is valid  # noqa: E501

        :return: The valid_payment of this BillingTypedPayment.  # noqa: E501
        :rtype: bool
        """
        return self._valid_payment

    @valid_payment.setter
    def valid_payment(self, valid_payment):
        """Sets the valid_payment of this BillingTypedPayment.

        Indicates if the payment is valid  # noqa: E501

        :param valid_payment: The valid_payment of this BillingTypedPayment.  # noqa: E501
        :type: bool
        """

        self._valid_payment = valid_payment

    @property
    def status(self):
        """Gets the status of this BillingTypedPayment.  # noqa: E501

        Payment status  # noqa: E501

        :return: The status of this BillingTypedPayment.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BillingTypedPayment.

        Payment status  # noqa: E501

        :param status: The status of this BillingTypedPayment.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_description(self):
        """Gets the status_description of this BillingTypedPayment.  # noqa: E501

        Payment status description  # noqa: E501

        :return: The status_description of this BillingTypedPayment.  # noqa: E501
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description):
        """Sets the status_description of this BillingTypedPayment.

        Payment status description  # noqa: E501

        :param status_description: The status_description of this BillingTypedPayment.  # noqa: E501
        :type: str
        """

        self._status_description = status_description

    @property
    def amount(self):
        """Gets the amount of this BillingTypedPayment.  # noqa: E501

        Payment amount  # noqa: E501

        :return: The amount of this BillingTypedPayment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BillingTypedPayment.

        Payment amount  # noqa: E501

        :param amount: The amount of this BillingTypedPayment.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def payment_method(self):
        """Gets the payment_method of this BillingTypedPayment.  # noqa: E501

        Payment method details  # noqa: E501

        :return: The payment_method of this BillingTypedPayment.  # noqa: E501
        :rtype: BillingTypedPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this BillingTypedPayment.

        Payment method details  # noqa: E501

        :param payment_method: The payment_method of this BillingTypedPayment.  # noqa: E501
        :type: BillingTypedPaymentMethod
        """

        self._payment_method = payment_method

    @property
    def auth_number(self):
        """Gets the auth_number of this BillingTypedPayment.  # noqa: E501

        Authorization number  # noqa: E501

        :return: The auth_number of this BillingTypedPayment.  # noqa: E501
        :rtype: str
        """
        return self._auth_number

    @auth_number.setter
    def auth_number(self, auth_number):
        """Sets the auth_number of this BillingTypedPayment.

        Authorization number  # noqa: E501

        :param auth_number: The auth_number of this BillingTypedPayment.  # noqa: E501
        :type: str
        """

        self._auth_number = auth_number

    @property
    def recurring_customer_item_i_ds(self):
        """Gets the recurring_customer_item_i_ds of this BillingTypedPayment.  # noqa: E501

        Relevant only for payments originating from recurring payments  # noqa: E501

        :return: The recurring_customer_item_i_ds of this BillingTypedPayment.  # noqa: E501
        :rtype: list[int]
        """
        return self._recurring_customer_item_i_ds

    @recurring_customer_item_i_ds.setter
    def recurring_customer_item_i_ds(self, recurring_customer_item_i_ds):
        """Sets the recurring_customer_item_i_ds of this BillingTypedPayment.

        Relevant only for payments originating from recurring payments  # noqa: E501

        :param recurring_customer_item_i_ds: The recurring_customer_item_i_ds of this BillingTypedPayment.  # noqa: E501
        :type: list[int]
        """

        self._recurring_customer_item_i_ds = recurring_customer_item_i_ds

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
        if issubclass(BillingTypedPayment, dict):
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
        if not isinstance(other, BillingTypedPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
