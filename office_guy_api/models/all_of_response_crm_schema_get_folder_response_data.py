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


class AllOfResponseCRMSchemaGetFolderResponseData(object):
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
        'folder': 'Object',
        'properties': 'list[CRMTypedProperty]'
    }
    if hasattr(CRMSchemaGetFolderResponse, "swagger_types"):
        swagger_types.update(CRMSchemaGetFolderResponse.swagger_types)

    attribute_map = {
        'folder': 'Folder',
        'properties': 'Properties'
    }
    if hasattr(CRMSchemaGetFolderResponse, "attribute_map"):
        attribute_map.update(CRMSchemaGetFolderResponse.attribute_map)

    def __init__(self, folder=None, properties=None, *args, **kwargs):  # noqa: E501
        """AllOfResponseCRMSchemaGetFolderResponseData - a model defined in Swagger"""  # noqa: E501
        self._folder = None
        self._properties = None
        self.discriminator = None
        if folder is not None:
            self.folder = folder
        if properties is not None:
            self.properties = properties
        CRMSchemaGetFolderResponse.__init__(self, *args, **kwargs)

    @property
    def folder(self):
        """Gets the folder of this AllOfResponseCRMSchemaGetFolderResponseData.  # noqa: E501


        :return: The folder of this AllOfResponseCRMSchemaGetFolderResponseData.  # noqa: E501
        :rtype: Object
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this AllOfResponseCRMSchemaGetFolderResponseData.


        :param folder: The folder of this AllOfResponseCRMSchemaGetFolderResponseData.  # noqa: E501
        :type: Object
        """

        self._folder = folder

    @property
    def properties(self):
        """Gets the properties of this AllOfResponseCRMSchemaGetFolderResponseData.  # noqa: E501


        :return: The properties of this AllOfResponseCRMSchemaGetFolderResponseData.  # noqa: E501
        :rtype: list[CRMTypedProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this AllOfResponseCRMSchemaGetFolderResponseData.


        :param properties: The properties of this AllOfResponseCRMSchemaGetFolderResponseData.  # noqa: E501
        :type: list[CRMTypedProperty]
        """

        self._properties = properties

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
        if issubclass(AllOfResponseCRMSchemaGetFolderResponseData, dict):
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
        if not isinstance(other, AllOfResponseCRMSchemaGetFolderResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other