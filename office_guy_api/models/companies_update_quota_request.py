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


class CompaniesUpdateQuotaRequest(object):
    swagger_types = {
        'credentials': 'CoreAPICredentials',
        'application_name': 'str',
        'quota': 'int',
        'increase': 'bool',
    }

    attribute_map = {
        'credentials': 'Credentials',
        'application_name': 'ApplicationName',
        'quota': 'Quota',
        'increase': 'Increase',
    }

    def __init__(self,
                 credentials=None,
                 application_name=None,
                 quota=None,
                 increase=None):  # noqa: E501
        self._credentials = credentials
        self._application_name = application_name
        self._quota = quota
        self._increase = increase


        if credentials is not None:
            self._credentials = credentials
        if application_name is not None:
            self._application_name = application_name
        if increase is not None:
            self._increase = increase

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def company(self, credentials):
        if credentials is None:
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, quota):
        if quota is None:
            raise ValueError("Invalid value for `quota`, must not be `None`")  # noqa: E501

        self._quota = quota

    @property
    def application_name(self):
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        if application_name is None:
            raise ValueError("Invalid value for `application_name`, must not be `None`")  # noqa: E501

        self._application_name = application_name

    @property
    def increase(self):
        return self._increase

    @increase.setter
    def increase(self, increase):
        if increase is None:
            raise ValueError("Invalid value for `increase`, must not be `None`")  # noqa: E501

        self._increase = increase

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
        if issubclass(CompaniesUpdateQuotaRequest, dict):
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
        if not isinstance(other, CompaniesUpdateQuotaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
