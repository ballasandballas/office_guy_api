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


class AllOfResponseBillingRecurringListForCustomerResponseData(object):
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
        'recurring_items': 'list[BillingTypedRecurringCustomerItem]'
    }
    if hasattr(BillingRecurringListForCustomerResponse, "swagger_types"):
        swagger_types.update(BillingRecurringListForCustomerResponse.swagger_types)

    attribute_map = {
        'recurring_items': 'RecurringItems'
    }
    if hasattr(BillingRecurringListForCustomerResponse, "attribute_map"):
        attribute_map.update(BillingRecurringListForCustomerResponse.attribute_map)

    def __init__(self, recurring_items=None, *args, **kwargs):  # noqa: E501
        """AllOfResponseBillingRecurringListForCustomerResponseData - a model defined in Swagger"""  # noqa: E501
        self._recurring_items = None
        self.discriminator = None
        if recurring_items is not None:
            self.recurring_items = recurring_items
        BillingRecurringListForCustomerResponse.__init__(self, *args, **kwargs)

    @property
    def recurring_items(self):
        """Gets the recurring_items of this AllOfResponseBillingRecurringListForCustomerResponseData.  # noqa: E501


        :return: The recurring_items of this AllOfResponseBillingRecurringListForCustomerResponseData.  # noqa: E501
        :rtype: list[BillingTypedRecurringCustomerItem]
        """
        return self._recurring_items

    @recurring_items.setter
    def recurring_items(self, recurring_items):
        """Sets the recurring_items of this AllOfResponseBillingRecurringListForCustomerResponseData.


        :param recurring_items: The recurring_items of this AllOfResponseBillingRecurringListForCustomerResponseData.  # noqa: E501
        :type: list[BillingTypedRecurringCustomerItem]
        """

        self._recurring_items = recurring_items

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
        if issubclass(AllOfResponseBillingRecurringListForCustomerResponseData, dict):
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
        if not isinstance(other, AllOfResponseBillingRecurringListForCustomerResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other