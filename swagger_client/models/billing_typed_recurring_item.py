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


class BillingTypedRecurringItem(object):
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
        'duration_days': 'int',
        'duration_months': 'int',
        'id': 'int',
        'name': 'str',
        'price': 'float',
        'currency': 'str',
        'cost': 'float',
        'external_identifier': 'str',
        'search_mode': 'str'
    }

    attribute_map = {
        'duration_days': 'Duration_Days',
        'duration_months': 'Duration_Months',
        'id': 'ID',
        'name': 'Name',
        'price': 'Price',
        'currency': 'Currency',
        'cost': 'Cost',
        'external_identifier': 'ExternalIdentifier',
        'search_mode': 'SearchMode'
    }

    def __init__(self, duration_days=None, duration_months=None, id=None, name=None, price=None, currency=None, cost=None, external_identifier=None, search_mode=None):  # noqa: E501
        """BillingTypedRecurringItem - a model defined in Swagger"""  # noqa: E501

        self._duration_days = None
        self._duration_months = None
        self._id = None
        self._name = None
        self._price = None
        self._currency = None
        self._cost = None
        self._external_identifier = None
        self._search_mode = None
        self.discriminator = None

        if duration_days is not None:
            self.duration_days = duration_days
        if duration_months is not None:
            self.duration_months = duration_months
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if currency is not None:
            self.currency = currency
        if cost is not None:
            self.cost = cost
        if external_identifier is not None:
            self.external_identifier = external_identifier
        if search_mode is not None:
            self.search_mode = search_mode

    @property
    def duration_days(self):
        """Gets the duration_days of this BillingTypedRecurringItem.  # noqa: E501

        Recurring duration/interval in days  # noqa: E501

        :return: The duration_days of this BillingTypedRecurringItem.  # noqa: E501
        :rtype: int
        """
        return self._duration_days

    @duration_days.setter
    def duration_days(self, duration_days):
        """Sets the duration_days of this BillingTypedRecurringItem.

        Recurring duration/interval in days  # noqa: E501

        :param duration_days: The duration_days of this BillingTypedRecurringItem.  # noqa: E501
        :type: int
        """

        self._duration_days = duration_days

    @property
    def duration_months(self):
        """Gets the duration_months of this BillingTypedRecurringItem.  # noqa: E501

        Recurring duration/interval in months  # noqa: E501

        :return: The duration_months of this BillingTypedRecurringItem.  # noqa: E501
        :rtype: int
        """
        return self._duration_months

    @duration_months.setter
    def duration_months(self, duration_months):
        """Sets the duration_months of this BillingTypedRecurringItem.

        Recurring duration/interval in months  # noqa: E501

        :param duration_months: The duration_months of this BillingTypedRecurringItem.  # noqa: E501
        :type: int
        """

        self._duration_months = duration_months

    @property
    def id(self):
        """Gets the id of this BillingTypedRecurringItem.  # noqa: E501

        OfficeGuy identifier  # noqa: E501

        :return: The id of this BillingTypedRecurringItem.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BillingTypedRecurringItem.

        OfficeGuy identifier  # noqa: E501

        :param id: The id of this BillingTypedRecurringItem.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BillingTypedRecurringItem.  # noqa: E501

        Item name  # noqa: E501

        :return: The name of this BillingTypedRecurringItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BillingTypedRecurringItem.

        Item name  # noqa: E501

        :param name: The name of this BillingTypedRecurringItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def price(self):
        """Gets the price of this BillingTypedRecurringItem.  # noqa: E501

        Item price (for single unit)  # noqa: E501

        :return: The price of this BillingTypedRecurringItem.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BillingTypedRecurringItem.

        Item price (for single unit)  # noqa: E501

        :param price: The price of this BillingTypedRecurringItem.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def currency(self):
        """Gets the currency of this BillingTypedRecurringItem.  # noqa: E501

        Price currency<div><i>Leave empty for company default</i></div>  # noqa: E501

        :return: The currency of this BillingTypedRecurringItem.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this BillingTypedRecurringItem.

        Price currency<div><i>Leave empty for company default</i></div>  # noqa: E501

        :param currency: The currency of this BillingTypedRecurringItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["ILS", "USD", "EUR", "CAD", "CHF", "GBP", "AUD"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def cost(self):
        """Gets the cost of this BillingTypedRecurringItem.  # noqa: E501

        Item cost (for single unit)  # noqa: E501

        :return: The cost of this BillingTypedRecurringItem.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this BillingTypedRecurringItem.

        Item cost (for single unit)  # noqa: E501

        :param cost: The cost of this BillingTypedRecurringItem.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def external_identifier(self):
        """Gets the external_identifier of this BillingTypedRecurringItem.  # noqa: E501

        Customer external identifier  # noqa: E501

        :return: The external_identifier of this BillingTypedRecurringItem.  # noqa: E501
        :rtype: str
        """
        return self._external_identifier

    @external_identifier.setter
    def external_identifier(self, external_identifier):
        """Sets the external_identifier of this BillingTypedRecurringItem.

        Customer external identifier  # noqa: E501

        :param external_identifier: The external_identifier of this BillingTypedRecurringItem.  # noqa: E501
        :type: str
        """

        self._external_identifier = external_identifier

    @property
    def search_mode(self):
        """Gets the search_mode of this BillingTypedRecurringItem.  # noqa: E501


        :return: The search_mode of this BillingTypedRecurringItem.  # noqa: E501
        :rtype: str
        """
        return self._search_mode

    @search_mode.setter
    def search_mode(self, search_mode):
        """Sets the search_mode of this BillingTypedRecurringItem.


        :param search_mode: The search_mode of this BillingTypedRecurringItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["Automatic", "None", "ExternalIdentifier", "Name"]  # noqa: E501
        if search_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `search_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(search_mode, allowed_values)
            )

        self._search_mode = search_mode

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
        if issubclass(BillingTypedRecurringItem, dict):
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
        if not isinstance(other, BillingTypedRecurringItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
