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


class Body66(object):
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
        'billing_identifier': 'str',
        'credentials': 'Object'
    }
    if hasattr(CreditGuyBillingProcessRequest, "swagger_types"):
        swagger_types.update(CreditGuyBillingProcessRequest.swagger_types)

    attribute_map = {
        'billing_identifier': 'BillingIdentifier',
        'credentials': 'Credentials'
    }
    if hasattr(CreditGuyBillingProcessRequest, "attribute_map"):
        attribute_map.update(CreditGuyBillingProcessRequest.attribute_map)

    def __init__(self, billing_identifier=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body66 - a model defined in Swagger"""  # noqa: E501
        self._billing_identifier = None
        self._credentials = None
        self.discriminator = None
        self.billing_identifier = billing_identifier
        self.credentials = credentials
        CreditGuyBillingProcessRequest.__init__(self, *args, **kwargs)

    @property
    def billing_identifier(self):
        """Gets the billing_identifier of this Body66.  # noqa: E501

        Unique billing process identifier  # noqa: E501

        :return: The billing_identifier of this Body66.  # noqa: E501
        :rtype: str
        """
        return self._billing_identifier

    @billing_identifier.setter
    def billing_identifier(self, billing_identifier):
        """Sets the billing_identifier of this Body66.

        Unique billing process identifier  # noqa: E501

        :param billing_identifier: The billing_identifier of this Body66.  # noqa: E501
        :type: str
        """
        if billing_identifier is None:
            raise ValueError("Invalid value for `billing_identifier`, must not be `None`")  # noqa: E501

        self._billing_identifier = billing_identifier

    @property
    def credentials(self):
        """Gets the credentials of this Body66.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body66.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body66.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body66.  # noqa: E501
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
        if issubclass(Body66, dict):
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
        if not isinstance(other, Body66):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
