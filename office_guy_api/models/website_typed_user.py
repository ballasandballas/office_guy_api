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


class WebsiteTypedUser(object):
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
        'name': 'str',
        'email_address': 'str',
        'password': 'str',
        'phone': 'str',
        'skip_activation': 'bool'
    }

    attribute_map = {
        'name': 'Name',
        'email_address': 'EmailAddress',
        'password': 'Password',
        'phone': 'Phone',
        'skip_activation': 'SkipActivation'
    }

    def __init__(self, name=None, email_address=None, password=None, phone=None, skip_activation=None):  # noqa: E501
        """WebsiteTypedUser - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._email_address = None
        self._password = None
        self._phone = None
        self._skip_activation = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if email_address is not None:
            self.email_address = email_address
        if password is not None:
            self.password = password
        if phone is not None:
            self.phone = phone
        if skip_activation is not None:
            self.skip_activation = skip_activation

    @property
    def name(self):
        """Gets the name of this WebsiteTypedUser.  # noqa: E501

        User full name  # noqa: E501

        :return: The name of this WebsiteTypedUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebsiteTypedUser.

        User full name  # noqa: E501

        :param name: The name of this WebsiteTypedUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email_address(self):
        """Gets the email_address of this WebsiteTypedUser.  # noqa: E501

        User email address  # noqa: E501

        :return: The email_address of this WebsiteTypedUser.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this WebsiteTypedUser.

        User email address  # noqa: E501

        :param email_address: The email_address of this WebsiteTypedUser.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def password(self):
        """Gets the password of this WebsiteTypedUser.  # noqa: E501

        User password (raw)  # noqa: E501

        :return: The password of this WebsiteTypedUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this WebsiteTypedUser.

        User password (raw)  # noqa: E501

        :param password: The password of this WebsiteTypedUser.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def phone(self):
        """Gets the phone of this WebsiteTypedUser.  # noqa: E501

        User phone number  # noqa: E501

        :return: The phone of this WebsiteTypedUser.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this WebsiteTypedUser.

        User phone number  # noqa: E501

        :param phone: The phone of this WebsiteTypedUser.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def skip_activation(self):
        """Gets the skip_activation of this WebsiteTypedUser.  # noqa: E501

        Allows skipping email activation before user can login.<div><i>Leave empty for false (Require activation)</i></div>  # noqa: E501

        :return: The skip_activation of this WebsiteTypedUser.  # noqa: E501
        :rtype: bool
        """
        return self._skip_activation

    @skip_activation.setter
    def skip_activation(self, skip_activation):
        """Sets the skip_activation of this WebsiteTypedUser.

        Allows skipping email activation before user can login.<div><i>Leave empty for false (Require activation)</i></div>  # noqa: E501

        :param skip_activation: The skip_activation of this WebsiteTypedUser.  # noqa: E501
        :type: bool
        """

        self._skip_activation = skip_activation

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
        if issubclass(WebsiteTypedUser, dict):
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
        if not isinstance(other, WebsiteTypedUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
