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


class Body92(object):
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
        'card_number': 'str',
        'expiration_month': 'int',
        'expiration_year': 'int',
        'cvv': 'str',
        'citizen_id': 'str',
        'credentials_company_id': 'int',
        'credentials_api_public_key': 'str',
        'response_language': 'str'
    }

    attribute_map = {
        'card_number': 'CardNumber',
        'expiration_month': 'ExpirationMonth',
        'expiration_year': 'ExpirationYear',
        'cvv': 'CVV',
        'citizen_id': 'CitizenID',
        'credentials_company_id': 'Credentials.CompanyID',
        'credentials_api_public_key': 'Credentials.APIPublicKey',
        'response_language': 'ResponseLanguage'
    }

    def __init__(self, card_number=None, expiration_month=None, expiration_year=None, cvv=None, citizen_id=None, credentials_company_id=None, credentials_api_public_key=None, response_language=None):  # noqa: E501
        """Body92 - a model defined in Swagger"""  # noqa: E501
        self._card_number = None
        self._expiration_month = None
        self._expiration_year = None
        self._cvv = None
        self._citizen_id = None
        self._credentials_company_id = None
        self._credentials_api_public_key = None
        self._response_language = None
        self.discriminator = None
        self.card_number = card_number
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        if cvv is not None:
            self.cvv = cvv
        if citizen_id is not None:
            self.citizen_id = citizen_id
        if credentials_company_id is not None:
            self.credentials_company_id = credentials_company_id
        if credentials_api_public_key is not None:
            self.credentials_api_public_key = credentials_api_public_key
        if response_language is not None:
            self.response_language = response_language

    @property
    def card_number(self):
        """Gets the card_number of this Body92.  # noqa: E501


        :return: The card_number of this Body92.  # noqa: E501
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this Body92.


        :param card_number: The card_number of this Body92.  # noqa: E501
        :type: str
        """
        if card_number is None:
            raise ValueError("Invalid value for `card_number`, must not be `None`")  # noqa: E501

        self._card_number = card_number

    @property
    def expiration_month(self):
        """Gets the expiration_month of this Body92.  # noqa: E501


        :return: The expiration_month of this Body92.  # noqa: E501
        :rtype: int
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """Sets the expiration_month of this Body92.


        :param expiration_month: The expiration_month of this Body92.  # noqa: E501
        :type: int
        """
        if expiration_month is None:
            raise ValueError("Invalid value for `expiration_month`, must not be `None`")  # noqa: E501

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """Gets the expiration_year of this Body92.  # noqa: E501


        :return: The expiration_year of this Body92.  # noqa: E501
        :rtype: int
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """Sets the expiration_year of this Body92.


        :param expiration_year: The expiration_year of this Body92.  # noqa: E501
        :type: int
        """
        if expiration_year is None:
            raise ValueError("Invalid value for `expiration_year`, must not be `None`")  # noqa: E501

        self._expiration_year = expiration_year

    @property
    def cvv(self):
        """Gets the cvv of this Body92.  # noqa: E501


        :return: The cvv of this Body92.  # noqa: E501
        :rtype: str
        """
        return self._cvv

    @cvv.setter
    def cvv(self, cvv):
        """Sets the cvv of this Body92.


        :param cvv: The cvv of this Body92.  # noqa: E501
        :type: str
        """

        self._cvv = cvv

    @property
    def citizen_id(self):
        """Gets the citizen_id of this Body92.  # noqa: E501


        :return: The citizen_id of this Body92.  # noqa: E501
        :rtype: str
        """
        return self._citizen_id

    @citizen_id.setter
    def citizen_id(self, citizen_id):
        """Sets the citizen_id of this Body92.


        :param citizen_id: The citizen_id of this Body92.  # noqa: E501
        :type: str
        """

        self._citizen_id = citizen_id

    @property
    def credentials_company_id(self):
        """Gets the credentials_company_id of this Body92.  # noqa: E501


        :return: The credentials_company_id of this Body92.  # noqa: E501
        :rtype: int
        """
        return self._credentials_company_id

    @credentials_company_id.setter
    def credentials_company_id(self, credentials_company_id):
        """Sets the credentials_company_id of this Body92.


        :param credentials_company_id: The credentials_company_id of this Body92.  # noqa: E501
        :type: int
        """

        self._credentials_company_id = credentials_company_id

    @property
    def credentials_api_public_key(self):
        """Gets the credentials_api_public_key of this Body92.  # noqa: E501


        :return: The credentials_api_public_key of this Body92.  # noqa: E501
        :rtype: str
        """
        return self._credentials_api_public_key

    @credentials_api_public_key.setter
    def credentials_api_public_key(self, credentials_api_public_key):
        """Sets the credentials_api_public_key of this Body92.


        :param credentials_api_public_key: The credentials_api_public_key of this Body92.  # noqa: E501
        :type: str
        """

        self._credentials_api_public_key = credentials_api_public_key

    @property
    def response_language(self):
        """Gets the response_language of this Body92.  # noqa: E501


        :return: The response_language of this Body92.  # noqa: E501
        :rtype: str
        """
        return self._response_language

    @response_language.setter
    def response_language(self, response_language):
        """Sets the response_language of this Body92.


        :param response_language: The response_language of this Body92.  # noqa: E501
        :type: str
        """

        self._response_language = response_language

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
        if issubclass(Body92, dict):
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
        if not isinstance(other, Body92):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other