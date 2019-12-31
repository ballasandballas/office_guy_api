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


class SMSMailingListListResponse(object):
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
        'mailing_lists': 'list[SMSTypedMailingList]'
    }

    attribute_map = {
        'mailing_lists': 'MailingLists'
    }

    def __init__(self, mailing_lists=None):  # noqa: E501
        """SMSMailingListListResponse - a model defined in Swagger"""  # noqa: E501

        self._mailing_lists = None
        self.discriminator = None

        if mailing_lists is not None:
            self.mailing_lists = mailing_lists

    @property
    def mailing_lists(self):
        """Gets the mailing_lists of this SMSMailingListListResponse.  # noqa: E501

        Mailing lists  # noqa: E501

        :return: The mailing_lists of this SMSMailingListListResponse.  # noqa: E501
        :rtype: list[SMSTypedMailingList]
        """
        return self._mailing_lists

    @mailing_lists.setter
    def mailing_lists(self, mailing_lists):
        """Sets the mailing_lists of this SMSMailingListListResponse.

        Mailing lists  # noqa: E501

        :param mailing_lists: The mailing_lists of this SMSMailingListListResponse.  # noqa: E501
        :type: list[SMSTypedMailingList]
        """

        self._mailing_lists = mailing_lists

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
        if issubclass(SMSMailingListListResponse, dict):
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
        if not isinstance(other, SMSMailingListListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
