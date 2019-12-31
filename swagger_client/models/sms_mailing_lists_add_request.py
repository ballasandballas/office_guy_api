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


class SMSMailingListsAddRequest(object):
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
        'mailing_list_id': 'int',
        'phone_number': 'str',
        'name': 'str',
        'credentials': 'CoreAPICredentials'
    }

    attribute_map = {
        'mailing_list_id': 'MailingListID',
        'phone_number': 'PhoneNumber',
        'name': 'Name',
        'credentials': 'Credentials'
    }

    def __init__(self, mailing_list_id=None, phone_number=None, name=None, credentials=None):  # noqa: E501
        """SMSMailingListsAddRequest - a model defined in Swagger"""  # noqa: E501

        self._mailing_list_id = None
        self._phone_number = None
        self._name = None
        self._credentials = None
        self.discriminator = None

        self.mailing_list_id = mailing_list_id
        self.phone_number = phone_number
        if name is not None:
            self.name = name
        self.credentials = credentials

    @property
    def mailing_list_id(self):
        """Gets the mailing_list_id of this SMSMailingListsAddRequest.  # noqa: E501

        Mailing list ID  # noqa: E501

        :return: The mailing_list_id of this SMSMailingListsAddRequest.  # noqa: E501
        :rtype: int
        """
        return self._mailing_list_id

    @mailing_list_id.setter
    def mailing_list_id(self, mailing_list_id):
        """Sets the mailing_list_id of this SMSMailingListsAddRequest.

        Mailing list ID  # noqa: E501

        :param mailing_list_id: The mailing_list_id of this SMSMailingListsAddRequest.  # noqa: E501
        :type: int
        """
        if mailing_list_id is None:
            raise ValueError("Invalid value for `mailing_list_id`, must not be `None`")  # noqa: E501

        self._mailing_list_id = mailing_list_id

    @property
    def phone_number(self):
        """Gets the phone_number of this SMSMailingListsAddRequest.  # noqa: E501

        Recipient phone number  # noqa: E501

        :return: The phone_number of this SMSMailingListsAddRequest.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this SMSMailingListsAddRequest.

        Recipient phone number  # noqa: E501

        :param phone_number: The phone_number of this SMSMailingListsAddRequest.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def name(self):
        """Gets the name of this SMSMailingListsAddRequest.  # noqa: E501

        Recipient name  # noqa: E501

        :return: The name of this SMSMailingListsAddRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SMSMailingListsAddRequest.

        Recipient name  # noqa: E501

        :param name: The name of this SMSMailingListsAddRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def credentials(self):
        """Gets the credentials of this SMSMailingListsAddRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this SMSMailingListsAddRequest.  # noqa: E501
        :rtype: CoreAPICredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this SMSMailingListsAddRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this SMSMailingListsAddRequest.  # noqa: E501
        :type: CoreAPICredentials
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
        if issubclass(SMSMailingListsAddRequest, dict):
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
        if not isinstance(other, SMSMailingListsAddRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
