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


class Body264(object):
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
        'company': 'Object',
        'user': 'Object',
        'applications': 'list[WebsiteTypedApplication]',
        'application_additions': 'list[WebsiteTypedApplicationAddition]',
        'hide_from_companies_list': 'bool',
        'credentials': 'Object'
    }
    if hasattr(WebsiteCompaniesCreateRequest, "swagger_types"):
        swagger_types.update(WebsiteCompaniesCreateRequest.swagger_types)

    attribute_map = {
        'company': 'Company',
        'user': 'User',
        'applications': 'Applications',
        'application_additions': 'ApplicationAdditions',
        'hide_from_companies_list': 'HideFromCompaniesList',
        'credentials': 'Credentials'
    }
    if hasattr(WebsiteCompaniesCreateRequest, "attribute_map"):
        attribute_map.update(WebsiteCompaniesCreateRequest.attribute_map)

    def __init__(self, company=None, user=None, applications=None, application_additions=None, hide_from_companies_list=None, credentials=None, *args, **kwargs):  # noqa: E501
        """Body264 - a model defined in Swagger"""  # noqa: E501
        self._company = None
        self._user = None
        self._applications = None
        self._application_additions = None
        self._hide_from_companies_list = None
        self._credentials = None
        self.discriminator = None
        self.company = company
        if user is not None:
            self.user = user
        if applications is not None:
            self.applications = applications
        if application_additions is not None:
            self.application_additions = application_additions
        if hide_from_companies_list is not None:
            self.hide_from_companies_list = hide_from_companies_list
        self.credentials = credentials
        WebsiteCompaniesCreateRequest.__init__(self, *args, **kwargs)

    @property
    def company(self):
        """Gets the company of this Body264.  # noqa: E501

        Company details  # noqa: E501

        :return: The company of this Body264.  # noqa: E501
        :rtype: Object
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Body264.

        Company details  # noqa: E501

        :param company: The company of this Body264.  # noqa: E501
        :type: Object
        """
        if company is None:
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company

    @property
    def user(self):
        """Gets the user of this Body264.  # noqa: E501

        Company owner<div><i>Leave empty to set calling company owners as owners</i></div>  # noqa: E501

        :return: The user of this Body264.  # noqa: E501
        :rtype: Object
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Body264.

        Company owner<div><i>Leave empty to set calling company owners as owners</i></div>  # noqa: E501

        :param user: The user of this Body264.  # noqa: E501
        :type: Object
        """

        self._user = user

    @property
    def applications(self):
        """Gets the applications of this Body264.  # noqa: E501

        List of applications to be installed on the created company.<div><i>Please note installing applications might incur additional charges.</i></div>  # noqa: E501

        :return: The applications of this Body264.  # noqa: E501
        :rtype: list[WebsiteTypedApplication]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this Body264.

        List of applications to be installed on the created company.<div><i>Please note installing applications might incur additional charges.</i></div>  # noqa: E501

        :param applications: The applications of this Body264.  # noqa: E501
        :type: list[WebsiteTypedApplication]
        """

        self._applications = applications

    @property
    def application_additions(self):
        """Gets the application_additions of this Body264.  # noqa: E501

        List of applications additions to be installed on the created company.<div><i>Please note this will incur additional charges.</i></div>  # noqa: E501

        :return: The application_additions of this Body264.  # noqa: E501
        :rtype: list[WebsiteTypedApplicationAddition]
        """
        return self._application_additions

    @application_additions.setter
    def application_additions(self, application_additions):
        """Sets the application_additions of this Body264.

        List of applications additions to be installed on the created company.<div><i>Please note this will incur additional charges.</i></div>  # noqa: E501

        :param application_additions: The application_additions of this Body264.  # noqa: E501
        :type: list[WebsiteTypedApplicationAddition]
        """

        self._application_additions = application_additions

    @property
    def hide_from_companies_list(self):
        """Gets the hide_from_companies_list of this Body264.  # noqa: E501

        Allows hiding the created company from the user companies list<div><i>Defaults to False</i></div>  # noqa: E501

        :return: The hide_from_companies_list of this Body264.  # noqa: E501
        :rtype: bool
        """
        return self._hide_from_companies_list

    @hide_from_companies_list.setter
    def hide_from_companies_list(self, hide_from_companies_list):
        """Sets the hide_from_companies_list of this Body264.

        Allows hiding the created company from the user companies list<div><i>Defaults to False</i></div>  # noqa: E501

        :param hide_from_companies_list: The hide_from_companies_list of this Body264.  # noqa: E501
        :type: bool
        """

        self._hide_from_companies_list = hide_from_companies_list

    @property
    def credentials(self):
        """Gets the credentials of this Body264.  # noqa: E501

        Company API credentials  # noqa: E501

        :return: The credentials of this Body264.  # noqa: E501
        :rtype: Object
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this Body264.

        Company API credentials  # noqa: E501

        :param credentials: The credentials of this Body264.  # noqa: E501
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
        if issubclass(Body264, dict):
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
        if not isinstance(other, Body264):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
