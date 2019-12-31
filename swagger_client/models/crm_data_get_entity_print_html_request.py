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


class CRMDataGetEntityPrintHTMLRequest(object):
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
        'schema_id': 'int',
        'entity_id': 'int',
        'pdf': 'bool',
        'credentials': 'CoreAPICredentials'
    }

    attribute_map = {
        'schema_id': 'SchemaID',
        'entity_id': 'EntityID',
        'pdf': 'PDF',
        'credentials': 'Credentials'
    }

    def __init__(self, schema_id=None, entity_id=None, pdf=None, credentials=None):  # noqa: E501
        """CRMDataGetEntityPrintHTMLRequest - a model defined in Swagger"""  # noqa: E501

        self._schema_id = None
        self._entity_id = None
        self._pdf = None
        self._credentials = None
        self.discriminator = None

        self.schema_id = schema_id
        self.entity_id = entity_id
        if pdf is not None:
            self.pdf = pdf
        self.credentials = credentials

    @property
    def schema_id(self):
        """Gets the schema_id of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501

        Schema identifier  # noqa: E501

        :return: The schema_id of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501
        :rtype: int
        """
        return self._schema_id

    @schema_id.setter
    def schema_id(self, schema_id):
        """Sets the schema_id of this CRMDataGetEntityPrintHTMLRequest.

        Schema identifier  # noqa: E501

        :param schema_id: The schema_id of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501
        :type: int
        """
        if schema_id is None:
            raise ValueError("Invalid value for `schema_id`, must not be `None`")  # noqa: E501

        self._schema_id = schema_id

    @property
    def entity_id(self):
        """Gets the entity_id of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501

        Entity identifier  # noqa: E501

        :return: The entity_id of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this CRMDataGetEntityPrintHTMLRequest.

        Entity identifier  # noqa: E501

        :param entity_id: The entity_id of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501
        :type: int
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def pdf(self):
        """Gets the pdf of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501

        Get PDF instead of HTML<div><i>Defaults to False</i></div>  # noqa: E501

        :return: The pdf of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501
        :rtype: bool
        """
        return self._pdf

    @pdf.setter
    def pdf(self, pdf):
        """Sets the pdf of this CRMDataGetEntityPrintHTMLRequest.

        Get PDF instead of HTML<div><i>Defaults to False</i></div>  # noqa: E501

        :param pdf: The pdf of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501
        :type: bool
        """

        self._pdf = pdf

    @property
    def credentials(self):
        """Gets the credentials of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501
        :rtype: CoreAPICredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this CRMDataGetEntityPrintHTMLRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this CRMDataGetEntityPrintHTMLRequest.  # noqa: E501
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
        if issubclass(CRMDataGetEntityPrintHTMLRequest, dict):
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
        if not isinstance(other, CRMDataGetEntityPrintHTMLRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
