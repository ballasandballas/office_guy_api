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


class Body171(object):
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
        'fax_number': 'str',
        'file_bytes': 'str',
        'filename': 'str',
        'save_draft': 'bool',
        'credentials': 'Object'
    }
    if hasattr(FaxFaxSendRequest, "swagger_types"):
        swagger_types.update(FaxFaxSendRequest.swagger_types)

    attribute_map = {
        'fax_number': 'FaxNumber',
        'file_bytes': 'FileBytes',
        'filename': 'Filename',
        'save_draft': 'SaveDraft',
        'credentials': 'Credentials'
    }
    if hasattr(FaxFaxSendRequest, "attribute_map"):
        attribute_map.update(FaxFaxSendRequest.attribute_map)

    def __init__(self, fax_number=None, file_bytes=None, filename=None, save_draft=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body171 - a model defined in Swagger"""  # noqa: E501
        self._fax_number = None
        self._file_bytes = None
        self._filename = None
        self._save_draft = None
        self._credentials = None
        self.discriminator = None
        self.fax_number = fax_number
        self.file_bytes = file_bytes
        self.filename = filename
        if save_draft is not None:
            self.save_draft = save_draft
        self.credentials = credentials
        FaxFaxSendRequest.__init__(self, *args, **kwargs)

    @property
    def fax_number(self):
        """Gets the fax_number of this Body171.  # noqa: E501


        :return: The fax_number of this Body171.  # noqa: E501
        :rtype: str
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number):
        """Sets the fax_number of this Body171.


        :param fax_number: The fax_number of this Body171.  # noqa: E501
        :type: str
        """
        if fax_number is None:
            raise ValueError("Invalid value for `fax_number`, must not be `None`")  # noqa: E501

        self._fax_number = fax_number

    @property
    def file_bytes(self):
        """Gets the file_bytes of this Body171.  # noqa: E501


        :return: The file_bytes of this Body171.  # noqa: E501
        :rtype: str
        """
        return self._file_bytes

    @file_bytes.setter
    def file_bytes(self, file_bytes):
        """Sets the file_bytes of this Body171.


        :param file_bytes: The file_bytes of this Body171.  # noqa: E501
        :type: str
        """
        if file_bytes is None:
            raise ValueError("Invalid value for `file_bytes`, must not be `None`")  # noqa: E501

        self._file_bytes = file_bytes

    @property
    def filename(self):
        """Gets the filename of this Body171.  # noqa: E501


        :return: The filename of this Body171.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Body171.


        :param filename: The filename of this Body171.  # noqa: E501
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def save_draft(self):
        """Gets the save_draft of this Body171.  # noqa: E501


        :return: The save_draft of this Body171.  # noqa: E501
        :rtype: bool
        """
        return self._save_draft

    @save_draft.setter
    def save_draft(self, save_draft):
        """Sets the save_draft of this Body171.


        :param save_draft: The save_draft of this Body171.  # noqa: E501
        :type: bool
        """

        self._save_draft = save_draft

    @property
    def credentials(self):
        """Gets the credentials of this Body171.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body171.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body171.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body171.  # noqa: E501
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
        if issubclass(Body171, dict):
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
        if not isinstance(other, Body171):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
