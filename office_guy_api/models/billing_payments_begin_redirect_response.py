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


class BillingPaymentsBeginRedirectResponse(object):
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
        'redirect_url': 'str'
    }

    attribute_map = {
        'redirect_url': 'RedirectURL'
    }

    def __init__(self, redirect_url=None):  # noqa: E501
        """BillingPaymentsBeginRedirectResponse - a model defined in Swagger"""  # noqa: E501

        self._redirect_url = None
        self.discriminator = None

        if redirect_url is not None:
            self.redirect_url = redirect_url

    @property
    def redirect_url(self):
        """Gets the redirect_url of this BillingPaymentsBeginRedirectResponse.  # noqa: E501

        Payment page URL.<div><i>Redirect your user to this page, in order to continue the payment process.</i></div>  # noqa: E501

        :return: The redirect_url of this BillingPaymentsBeginRedirectResponse.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this BillingPaymentsBeginRedirectResponse.

        Payment page URL.<div><i>Redirect your user to this page, in order to continue the payment process.</i></div>  # noqa: E501

        :param redirect_url: The redirect_url of this BillingPaymentsBeginRedirectResponse.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

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
        if issubclass(BillingPaymentsBeginRedirectResponse, dict):
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
        if not isinstance(other, BillingPaymentsBeginRedirectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
