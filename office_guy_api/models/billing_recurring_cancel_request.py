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


class BillingRecurringCancelRequest(object):
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
        'customer': 'AllOfBillingRecurringCancelRequestCustomer',
        'recurring_customer_item_id': 'int',
        'credentials': 'AllOfBillingRecurringCancelRequestCredentials'
    }

    attribute_map = {
        'customer': 'Customer',
        'recurring_customer_item_id': 'RecurringCustomerItemID',
        'credentials': 'Credentials'
    }

    def __init__(self, customer=None, recurring_customer_item_id=None, credentials=None):  # noqa: E501
        """BillingRecurringCancelRequest - a model defined in Swagger"""  # noqa: E501
        self._customer = None
        self._recurring_customer_item_id = None
        self._credentials = None
        self.discriminator = None
        self.customer = customer
        self.recurring_customer_item_id = recurring_customer_item_id
        self.credentials = credentials

    @property
    def customer(self):
        """Gets the customer of this BillingRecurringCancelRequest.  # noqa: E501

        Customer  # noqa: E501

        :return: The customer of this BillingRecurringCancelRequest.  # noqa: E501
        :rtype: AllOfBillingRecurringCancelRequestCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this BillingRecurringCancelRequest.

        Customer  # noqa: E501

        :param customer: The customer of this BillingRecurringCancelRequest.  # noqa: E501
        :type: AllOfBillingRecurringCancelRequestCustomer
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def recurring_customer_item_id(self):
        """Gets the recurring_customer_item_id of this BillingRecurringCancelRequest.  # noqa: E501

        Recurring customer item identifier  # noqa: E501

        :return: The recurring_customer_item_id of this BillingRecurringCancelRequest.  # noqa: E501
        :rtype: int
        """
        return self._recurring_customer_item_id

    @recurring_customer_item_id.setter
    def recurring_customer_item_id(self, recurring_customer_item_id):
        """Sets the recurring_customer_item_id of this BillingRecurringCancelRequest.

        Recurring customer item identifier  # noqa: E501

        :param recurring_customer_item_id: The recurring_customer_item_id of this BillingRecurringCancelRequest.  # noqa: E501
        :type: int
        """
        if recurring_customer_item_id is None:
            raise ValueError("Invalid value for `recurring_customer_item_id`, must not be `None`")  # noqa: E501

        self._recurring_customer_item_id = recurring_customer_item_id

    @property
    def credentials(self):
        """Gets the credentials of this BillingRecurringCancelRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this BillingRecurringCancelRequest.  # noqa: E501
        :rtype: AllOfBillingRecurringCancelRequestCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this BillingRecurringCancelRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this BillingRecurringCancelRequest.  # noqa: E501
        :type: AllOfBillingRecurringCancelRequestCredentials
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
        if issubclass(BillingRecurringCancelRequest, dict):
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
        if not isinstance(other, BillingRecurringCancelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
