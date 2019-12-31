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


class WebsiteCompaniesCreateResponse(object):
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
        'company_id': 'int',
        'api_key': 'str',
        'api_public_key': 'str',
        'user_password': 'str',
        'user_encrypted_password': 'str'
    }

    attribute_map = {
        'company_id': 'CompanyID',
        'api_key': 'APIKey',
        'api_public_key': 'APIPublicKey',
        'user_password': 'UserPassword',
        'user_encrypted_password': 'UserEncryptedPassword'
    }

    def __init__(self, company_id=None, api_key=None, api_public_key=None, user_password=None, user_encrypted_password=None):  # noqa: E501
        """WebsiteCompaniesCreateResponse - a model defined in Swagger"""  # noqa: E501

        self._company_id = None
        self._api_key = None
        self._api_public_key = None
        self._user_password = None
        self._user_encrypted_password = None
        self.discriminator = None

        if company_id is not None:
            self.company_id = company_id
        if api_key is not None:
            self.api_key = api_key
        if api_public_key is not None:
            self.api_public_key = api_public_key
        if user_password is not None:
            self.user_password = user_password
        if user_encrypted_password is not None:
            self.user_encrypted_password = user_encrypted_password

    @property
    def company_id(self):
        """Gets the company_id of this WebsiteCompaniesCreateResponse.  # noqa: E501

        Created company identifier  # noqa: E501

        :return: The company_id of this WebsiteCompaniesCreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this WebsiteCompaniesCreateResponse.

        Created company identifier  # noqa: E501

        :param company_id: The company_id of this WebsiteCompaniesCreateResponse.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def api_key(self):
        """Gets the api_key of this WebsiteCompaniesCreateResponse.  # noqa: E501

        API Key for future calls  # noqa: E501

        :return: The api_key of this WebsiteCompaniesCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this WebsiteCompaniesCreateResponse.

        API Key for future calls  # noqa: E501

        :param api_key: The api_key of this WebsiteCompaniesCreateResponse.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def api_public_key(self):
        """Gets the api_public_key of this WebsiteCompaniesCreateResponse.  # noqa: E501

        Public API Key for future calls  # noqa: E501

        :return: The api_public_key of this WebsiteCompaniesCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_public_key

    @api_public_key.setter
    def api_public_key(self, api_public_key):
        """Sets the api_public_key of this WebsiteCompaniesCreateResponse.

        Public API Key for future calls  # noqa: E501

        :param api_public_key: The api_public_key of this WebsiteCompaniesCreateResponse.  # noqa: E501
        :type: str
        """

        self._api_public_key = api_public_key

    @property
    def user_password(self):
        """Gets the user_password of this WebsiteCompaniesCreateResponse.  # noqa: E501

        Created user password<div><i>Returned only when new user is created</i></div>  # noqa: E501

        :return: The user_password of this WebsiteCompaniesCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """Sets the user_password of this WebsiteCompaniesCreateResponse.

        Created user password<div><i>Returned only when new user is created</i></div>  # noqa: E501

        :param user_password: The user_password of this WebsiteCompaniesCreateResponse.  # noqa: E501
        :type: str
        """

        self._user_password = user_password

    @property
    def user_encrypted_password(self):
        """Gets the user_encrypted_password of this WebsiteCompaniesCreateResponse.  # noqa: E501

        Created user encrypted password<div><i>Returned only when new user is created</i></div>  # noqa: E501

        :return: The user_encrypted_password of this WebsiteCompaniesCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_encrypted_password

    @user_encrypted_password.setter
    def user_encrypted_password(self, user_encrypted_password):
        """Sets the user_encrypted_password of this WebsiteCompaniesCreateResponse.

        Created user encrypted password<div><i>Returned only when new user is created</i></div>  # noqa: E501

        :param user_encrypted_password: The user_encrypted_password of this WebsiteCompaniesCreateResponse.  # noqa: E501
        :type: str
        """

        self._user_encrypted_password = user_encrypted_password

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
        if issubclass(WebsiteCompaniesCreateResponse, dict):
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
        if not isinstance(other, WebsiteCompaniesCreateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
