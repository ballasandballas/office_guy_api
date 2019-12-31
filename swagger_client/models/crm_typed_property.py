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


class CRMTypedProperty(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'category': 'str',
        'value_type': 'str',
        'api_name': 'str',
        'required': 'bool'
    }

    attribute_map = {
        'id': 'ID',
        'name': 'Name',
        'description': 'Description',
        'category': 'Category',
        'value_type': 'ValueType',
        'api_name': 'APIName',
        'required': 'Required'
    }

    def __init__(self, id=None, name=None, description=None, category=None, value_type=None, api_name=None, required=None):  # noqa: E501
        """CRMTypedProperty - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._category = None
        self._value_type = None
        self._api_name = None
        self._required = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if value_type is not None:
            self.value_type = value_type
        if api_name is not None:
            self.api_name = api_name
        if required is not None:
            self.required = required

    @property
    def id(self):
        """Gets the id of this CRMTypedProperty.  # noqa: E501


        :return: The id of this CRMTypedProperty.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CRMTypedProperty.


        :param id: The id of this CRMTypedProperty.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CRMTypedProperty.  # noqa: E501


        :return: The name of this CRMTypedProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CRMTypedProperty.


        :param name: The name of this CRMTypedProperty.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CRMTypedProperty.  # noqa: E501


        :return: The description of this CRMTypedProperty.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CRMTypedProperty.


        :param description: The description of this CRMTypedProperty.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """Gets the category of this CRMTypedProperty.  # noqa: E501


        :return: The category of this CRMTypedProperty.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CRMTypedProperty.


        :param category: The category of this CRMTypedProperty.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def value_type(self):
        """Gets the value_type of this CRMTypedProperty.  # noqa: E501


        :return: The value_type of this CRMTypedProperty.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this CRMTypedProperty.


        :param value_type: The value_type of this CRMTypedProperty.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

    @property
    def api_name(self):
        """Gets the api_name of this CRMTypedProperty.  # noqa: E501


        :return: The api_name of this CRMTypedProperty.  # noqa: E501
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        """Sets the api_name of this CRMTypedProperty.


        :param api_name: The api_name of this CRMTypedProperty.  # noqa: E501
        :type: str
        """

        self._api_name = api_name

    @property
    def required(self):
        """Gets the required of this CRMTypedProperty.  # noqa: E501


        :return: The required of this CRMTypedProperty.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this CRMTypedProperty.


        :param required: The required of this CRMTypedProperty.  # noqa: E501
        :type: bool
        """

        self._required = required

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
        if issubclass(CRMTypedProperty, dict):
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
        if not isinstance(other, CRMTypedProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
