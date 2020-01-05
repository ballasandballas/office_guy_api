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


class SMSSMSListSendersResponse(object):
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
        'senders': 'list[str]'
    }

    attribute_map = {
        'senders': 'Senders'
    }

    def __init__(self, senders=None):  # noqa: E501
        """SMSSMSListSendersResponse - a model defined in Swagger"""  # noqa: E501

        self._senders = None
        self.discriminator = None

        if senders is not None:
            self.senders = senders

    @property
    def senders(self):
        """Gets the senders of this SMSSMSListSendersResponse.  # noqa: E501

        Verified sender numbers  # noqa: E501

        :return: The senders of this SMSSMSListSendersResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._senders

    @senders.setter
    def senders(self, senders):
        """Sets the senders of this SMSSMSListSendersResponse.

        Verified sender numbers  # noqa: E501

        :param senders: The senders of this SMSSMSListSendersResponse.  # noqa: E501
        :type: list[str]
        """

        self._senders = senders

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
        if issubclass(SMSSMSListSendersResponse, dict):
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
        if not isinstance(other, SMSSMSListSendersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other