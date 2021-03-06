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


class LetterByClickLetterByClickGetTrackingCodeRequest(object):
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
        'external_code': 'str',
        'credentials': 'CoreAPICredentials'
    }

    attribute_map = {
        'external_code': 'ExternalCode',
        'credentials': 'Credentials'
    }

    def __init__(self, external_code=None, credentials=None):  # noqa: E501
        """LetterByClickLetterByClickGetTrackingCodeRequest - a model defined in Swagger"""  # noqa: E501

        self._external_code = None
        self._credentials = None
        self.discriminator = None

        if external_code is not None:
            self.external_code = external_code
        self.credentials = credentials

    @property
    def external_code(self):
        """Gets the external_code of this LetterByClickLetterByClickGetTrackingCodeRequest.  # noqa: E501

        External code returned from the SendDocument API  # noqa: E501

        :return: The external_code of this LetterByClickLetterByClickGetTrackingCodeRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_code

    @external_code.setter
    def external_code(self, external_code):
        """Sets the external_code of this LetterByClickLetterByClickGetTrackingCodeRequest.

        External code returned from the SendDocument API  # noqa: E501

        :param external_code: The external_code of this LetterByClickLetterByClickGetTrackingCodeRequest.  # noqa: E501
        :type: str
        """

        self._external_code = external_code

    @property
    def credentials(self):
        """Gets the credentials of this LetterByClickLetterByClickGetTrackingCodeRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this LetterByClickLetterByClickGetTrackingCodeRequest.  # noqa: E501
        :rtype: CoreAPICredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this LetterByClickLetterByClickGetTrackingCodeRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this LetterByClickLetterByClickGetTrackingCodeRequest.  # noqa: E501
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
        if issubclass(LetterByClickLetterByClickGetTrackingCodeRequest, dict):
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
        if not isinstance(other, LetterByClickLetterByClickGetTrackingCodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
