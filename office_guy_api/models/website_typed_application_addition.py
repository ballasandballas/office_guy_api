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


class WebsiteTypedApplicationAddition(object):
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
        'type': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'type': 'Type',
        'quantity': 'Quantity'
    }

    def __init__(self, type=None, quantity=None):  # noqa: E501
        """WebsiteTypedApplicationAddition - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._quantity = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if quantity is not None:
            self.quantity = quantity

    @property
    def type(self):
        """Gets the type of this WebsiteTypedApplicationAddition.  # noqa: E501

        Addition type  # noqa: E501

        :return: The type of this WebsiteTypedApplicationAddition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebsiteTypedApplicationAddition.

        Addition type  # noqa: E501

        :param type: The type of this WebsiteTypedApplicationAddition.  # noqa: E501
        :type: str
        """
        allowed_values = ["Accounting_Documents_100", "Accounting_Documents_500", "Billing_Payments_100", "Billing_Payments_500", "Users_APIKeys_5", "Users_User_1"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def quantity(self):
        """Gets the quantity of this WebsiteTypedApplicationAddition.  # noqa: E501

        Addition quantity multiplier<div><i>Defaults to 1</i></div>  # noqa: E501

        :return: The quantity of this WebsiteTypedApplicationAddition.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this WebsiteTypedApplicationAddition.

        Addition quantity multiplier<div><i>Defaults to 1</i></div>  # noqa: E501

        :param quantity: The quantity of this WebsiteTypedApplicationAddition.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(WebsiteTypedApplicationAddition, dict):
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
        if not isinstance(other, WebsiteTypedApplicationAddition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
