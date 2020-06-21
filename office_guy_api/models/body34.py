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


class Body34(object):
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
        'document_id': 'int',
        'credentials': 'Object'
    }
    if hasattr(AccountingDocumentsMoveToBooksRequest, "swagger_types"):
        swagger_types.update(AccountingDocumentsMoveToBooksRequest.swagger_types)

    attribute_map = {
        'document_id': 'DocumentID',
        'credentials': 'Credentials'
    }
    if hasattr(AccountingDocumentsMoveToBooksRequest, "attribute_map"):
        attribute_map.update(AccountingDocumentsMoveToBooksRequest.attribute_map)

    def __init__(self, document_id=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body34 - a model defined in Swagger"""  # noqa: E501
        self._document_id = None
        self._credentials = None
        self.discriminator = None
        self.document_id = document_id
        self.credentials = credentials
        AccountingDocumentsMoveToBooksRequest.__init__(self, *args, **kwargs)

    @property
    def document_id(self):
        """Gets the document_id of this Body34.  # noqa: E501

        Document identifier  # noqa: E501

        :return: The document_id of this Body34.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Body34.

        Document identifier  # noqa: E501

        :param document_id: The document_id of this Body34.  # noqa: E501
        :type: int
        """
        if document_id is None:
            raise ValueError("Invalid value for `document_id`, must not be `None`")  # noqa: E501

        self._document_id = document_id

    @property
    def credentials(self):
        """Gets the credentials of this Body34.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body34.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body34.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body34.  # noqa: E501
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
        if issubclass(Body34, dict):
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
        if not isinstance(other, Body34):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
