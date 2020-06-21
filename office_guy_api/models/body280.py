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


class Body280(object):
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
        'applications': 'list[WebsiteTypedApplication]',
        'credentials': 'Object'
    }
    if hasattr(WebsiteCompaniesInstallApplicationsRequest, "swagger_types"):
        swagger_types.update(WebsiteCompaniesInstallApplicationsRequest.swagger_types)

    attribute_map = {
        'applications': 'Applications',
        'credentials': 'Credentials'
    }
    if hasattr(WebsiteCompaniesInstallApplicationsRequest, "attribute_map"):
        attribute_map.update(WebsiteCompaniesInstallApplicationsRequest.attribute_map)

    def __init__(self, applications=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body280 - a model defined in Swagger"""  # noqa: E501
        self._applications = None
        self._credentials = None
        self.discriminator = None
        self.applications = applications
        self.credentials = credentials
        WebsiteCompaniesInstallApplicationsRequest.__init__(self, *args, **kwargs)

    @property
    def applications(self):
        """Gets the applications of this Body280.  # noqa: E501

        List of applications to be installed.<div><i>Please note this may incur additional charges.</i></div>  # noqa: E501

        :return: The applications of this Body280.  # noqa: E501
        :rtype: list[WebsiteTypedApplication]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this Body280.

        List of applications to be installed.<div><i>Please note this may incur additional charges.</i></div>  # noqa: E501

        :param applications: The applications of this Body280.  # noqa: E501
        :type: list[WebsiteTypedApplication]
        """
        if applications is None:
            raise ValueError("Invalid value for `applications`, must not be `None`")  # noqa: E501

        self._applications = applications

    @property
    def credentials(self):
        """Gets the credentials of this Body280.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body280.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body280.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body280.  # noqa: E501
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
        if issubclass(Body280, dict):
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
        if not isinstance(other, Body280):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
