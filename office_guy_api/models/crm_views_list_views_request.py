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


class CRMViewsListViewsRequest(object):
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
        'folder_id': 'int',
        'credentials': 'CoreAPICredentials'
    }

    attribute_map = {
        'folder_id': 'FolderID',
        'credentials': 'Credentials'
    }

    def __init__(self, folder_id=None, credentials=None):  # noqa: E501
        """CRMViewsListViewsRequest - a model defined in Swagger"""  # noqa: E501

        self._folder_id = None
        self._credentials = None
        self.discriminator = None

        if folder_id is not None:
            self.folder_id = folder_id
        self.credentials = credentials

    @property
    def folder_id(self):
        """Gets the folder_id of this CRMViewsListViewsRequest.  # noqa: E501


        :return: The folder_id of this CRMViewsListViewsRequest.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this CRMViewsListViewsRequest.


        :param folder_id: The folder_id of this CRMViewsListViewsRequest.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def credentials(self):
        """Gets the credentials of this CRMViewsListViewsRequest.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this CRMViewsListViewsRequest.  # noqa: E501
        :rtype: CoreAPICredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this CRMViewsListViewsRequest.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this CRMViewsListViewsRequest.  # noqa: E501
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
        if issubclass(CRMViewsListViewsRequest, dict):
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
        if not isinstance(other, CRMViewsListViewsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other