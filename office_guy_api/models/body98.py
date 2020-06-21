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


class Body98(object):
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
        'entity': 'Object',
        'credentials': 'Object'
    }
    if hasattr(CRMDataCreateEntityRequest, "swagger_types"):
        swagger_types.update(CRMDataCreateEntityRequest.swagger_types)

    attribute_map = {
        'entity': 'Entity',
        'credentials': 'Credentials'
    }
    if hasattr(CRMDataCreateEntityRequest, "attribute_map"):
        attribute_map.update(CRMDataCreateEntityRequest.attribute_map)

    def __init__(self, entity=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body98 - a model defined in Swagger"""  # noqa: E501
        self._entity = None
        self._credentials = None
        self.discriminator = None
        self.entity = entity
        self.credentials = credentials
        CRMDataCreateEntityRequest.__init__(self, *args, **kwargs)

    @property
    def entity(self):
        """Gets the entity of this Body98.  # noqa: E501

        The entity to be created  # noqa: E501

        :return: The entity of this Body98.  # noqa: E501
        :rtype: Object
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this Body98.

        The entity to be created  # noqa: E501

        :param entity: The entity of this Body98.  # noqa: E501
        :type: Object
        """
        if entity is None:
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501

        self._entity = entity

    @property
    def credentials(self):
        """Gets the credentials of this Body98.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body98.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body98.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body98.  # noqa: E501
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
        if issubclass(Body98, dict):
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
        if not isinstance(other, Body98):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
