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


class CreditGuyGatewayGetReferenceNumbersRequest(object):
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
        'i_ds': 'list[int]',
        'unique_identifiers': 'list[str]',
        'credentials': 'CoreAPIPublicCredentials'
    }

    attribute_map = {
        'i_ds': 'IDs',
        'unique_identifiers': 'UniqueIdentifiers',
        'credentials': 'Credentials'
    }

    def __init__(self, i_ds=None, unique_identifiers=None, credentials=None):  # noqa: E501
        """CreditGuyGatewayGetReferenceNumbersRequest - a model defined in Swagger"""  # noqa: E501

        self._i_ds = None
        self._unique_identifiers = None
        self._credentials = None
        self.discriminator = None

        if i_ds is not None:
            self.i_ds = i_ds
        if unique_identifiers is not None:
            self.unique_identifiers = unique_identifiers
        self.credentials = credentials

    @property
    def i_ds(self):
        """Gets the i_ds of this CreditGuyGatewayGetReferenceNumbersRequest.  # noqa: E501

        Transaction IDs (Maximum of 1000 identifiers)  # noqa: E501

        :return: The i_ds of this CreditGuyGatewayGetReferenceNumbersRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._i_ds

    @i_ds.setter
    def i_ds(self, i_ds):
        """Sets the i_ds of this CreditGuyGatewayGetReferenceNumbersRequest.

        Transaction IDs (Maximum of 1000 identifiers)  # noqa: E501

        :param i_ds: The i_ds of this CreditGuyGatewayGetReferenceNumbersRequest.  # noqa: E501
        :type: list[int]
        """

        self._i_ds = i_ds

    @property
    def unique_identifiers(self):
        """Gets the unique_identifiers of this CreditGuyGatewayGetReferenceNumbersRequest.  # noqa: E501

        Unique transaction identifer (Maximum of 1000 identifiers)  # noqa: E501

        :return: The unique_identifiers of this CreditGuyGatewayGetReferenceNumbersRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._unique_identifiers

    @unique_identifiers.setter
    def unique_identifiers(self, unique_identifiers):
        """Sets the unique_identifiers of this CreditGuyGatewayGetReferenceNumbersRequest.

        Unique transaction identifer (Maximum of 1000 identifiers)  # noqa: E501

        :param unique_identifiers: The unique_identifiers of this CreditGuyGatewayGetReferenceNumbersRequest.  # noqa: E501
        :type: list[str]
        """

        self._unique_identifiers = unique_identifiers

    @property
    def credentials(self):
        """Gets the credentials of this CreditGuyGatewayGetReferenceNumbersRequest.  # noqa: E501

        Company API public credentials  # noqa: E501

        :return: The credentials of this CreditGuyGatewayGetReferenceNumbersRequest.  # noqa: E501
        :rtype: CoreAPIPublicCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this CreditGuyGatewayGetReferenceNumbersRequest.

        Company API public credentials  # noqa: E501

        :param credentials: The credentials of this CreditGuyGatewayGetReferenceNumbersRequest.  # noqa: E501
        :type: CoreAPIPublicCredentials
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
        if issubclass(CreditGuyGatewayGetReferenceNumbersRequest, dict):
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
        if not isinstance(other, CreditGuyGatewayGetReferenceNumbersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
