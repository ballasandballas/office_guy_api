# coding: utf-8

"""
    OfficeGuy API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import office_guy_api
from office_guy_api.api.payments__payments_api import PaymentsPaymentsApi  # noqa: E501
from office_guy_api.rest import ApiException


class TestPaymentsPaymentsApi(unittest.TestCase):
    """PaymentsPaymentsApi unit test stubs"""

    def setUp(self):
        self.api = office_guy_api.api.payments__payments_api.PaymentsPaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_billing_payments_begin_redirect(self):
        """Test case for billing_payments_begin_redirect

        Begin redirect for transaction  # noqa: E501
        """
        pass

    def test_billing_payments_charge(self):
        """Test case for billing_payments_charge

        Charge customer  # noqa: E501
        """
        pass

    def test_billing_payments_get(self):
        """Test case for billing_payments_get

        Get payment details  # noqa: E501
        """
        pass

    def test_billing_payments_list(self):
        """Test case for billing_payments_list

        List payments  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
