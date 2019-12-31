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


class CoreTypedOrder(object):
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
        '_property': 'str',
        'descending': 'bool'
    }

    attribute_map = {
        '_property': 'Property',
        'descending': 'Descending'
    }

    def __init__(self, _property=None, descending=None):  # noqa: E501
        """CoreTypedOrder - a model defined in Swagger"""  # noqa: E501

        self.__property = None
        self._descending = None
        self.discriminator = None

        if _property is not None:
            self._property = _property
        if descending is not None:
            self.descending = descending

    @property
    def _property(self):
        """Gets the _property of this CoreTypedOrder.  # noqa: E501

        Property to order by (sort)  # noqa: E501

        :return: The _property of this CoreTypedOrder.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this CoreTypedOrder.

        Property to order by (sort)  # noqa: E501

        :param _property: The _property of this CoreTypedOrder.  # noqa: E501
        :type: str
        """

        self.__property = _property

    @property
    def descending(self):
        """Gets the descending of this CoreTypedOrder.  # noqa: E501

        Sort ascending/descending<div><i>(Defaults to ascending)</i></div>  # noqa: E501

        :return: The descending of this CoreTypedOrder.  # noqa: E501
        :rtype: bool
        """
        return self._descending

    @descending.setter
    def descending(self, descending):
        """Sets the descending of this CoreTypedOrder.

        Sort ascending/descending<div><i>(Defaults to ascending)</i></div>  # noqa: E501

        :param descending: The descending of this CoreTypedOrder.  # noqa: E501
        :type: bool
        """

        self._descending = descending

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
        if issubclass(CoreTypedOrder, dict):
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
        if not isinstance(other, CoreTypedOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
