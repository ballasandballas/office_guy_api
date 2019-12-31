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


class ResponseCreditGuyBillingLoadResponse(object):
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
        'data': 'CreditGuyBillingLoadResponse',
        'status': 'str',
        'user_error_message': 'str',
        'technical_error_details': 'str'
    }

    attribute_map = {
        'data': 'Data',
        'status': 'Status',
        'user_error_message': 'UserErrorMessage',
        'technical_error_details': 'TechnicalErrorDetails'
    }

    def __init__(self, data=None, status=None, user_error_message=None, technical_error_details=None):  # noqa: E501
        """ResponseCreditGuyBillingLoadResponse - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._status = None
        self._user_error_message = None
        self._technical_error_details = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if status is not None:
            self.status = status
        if user_error_message is not None:
            self.user_error_message = user_error_message
        if technical_error_details is not None:
            self.technical_error_details = technical_error_details

    @property
    def data(self):
        """Gets the data of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501

        API specific response data  # noqa: E501

        :return: The data of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501
        :rtype: CreditGuyBillingLoadResponse
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ResponseCreditGuyBillingLoadResponse.

        API specific response data  # noqa: E501

        :param data: The data of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501
        :type: CreditGuyBillingLoadResponse
        """

        self._data = data

    @property
    def status(self):
        """Gets the status of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501

        Response status  # noqa: E501

        :return: The status of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseCreditGuyBillingLoadResponse.

        Response status  # noqa: E501

        :param status: The status of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Success", "BusinessError", "TechnicalError"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def user_error_message(self):
        """Gets the user_error_message of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501

        Error message, in a user readable format  # noqa: E501

        :return: The user_error_message of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_error_message

    @user_error_message.setter
    def user_error_message(self, user_error_message):
        """Sets the user_error_message of this ResponseCreditGuyBillingLoadResponse.

        Error message, in a user readable format  # noqa: E501

        :param user_error_message: The user_error_message of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501
        :type: str
        """

        self._user_error_message = user_error_message

    @property
    def technical_error_details(self):
        """Gets the technical_error_details of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501

        Technical error details, let us know if you received this.  # noqa: E501

        :return: The technical_error_details of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501
        :rtype: str
        """
        return self._technical_error_details

    @technical_error_details.setter
    def technical_error_details(self, technical_error_details):
        """Sets the technical_error_details of this ResponseCreditGuyBillingLoadResponse.

        Technical error details, let us know if you received this.  # noqa: E501

        :param technical_error_details: The technical_error_details of this ResponseCreditGuyBillingLoadResponse.  # noqa: E501
        :type: str
        """

        self._technical_error_details = technical_error_details

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
        if issubclass(ResponseCreditGuyBillingLoadResponse, dict):
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
        if not isinstance(other, ResponseCreditGuyBillingLoadResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
