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
from office_guy_api.api.accounting__general_api import AccountingGeneralApi  # noqa: E501
from office_guy_api.rest import ApiException


class TestAccountingGeneralApi(unittest.TestCase):
    """AccountingGeneralApi unit test stubs"""

    def setUp(self):
        self.api = office_guy_api.api.accounting__general_api.AccountingGeneralApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accounting_general_get_exchange_rate(self):
        """Test case for accounting_general_get_exchange_rate

        Get foreign currency exchange rate  # noqa: E501
        """
        pass

    def test_accounting_general_get_vat_rate(self):
        """Test case for accounting_general_get_vat_rate

        Get VAT rate by date  # noqa: E501
        """
        pass

    def test_accounting_general_set_next_document_number(self):
        """Test case for accounting_general_set_next_document_number

        Sets the next document number for a document type.  # noqa: E501
        """
        pass

    def test_accounting_general_update_settings(self):
        """Test case for accounting_general_update_settings

        Update accounting application settings  # noqa: E501
        """
        pass

    def test_accounting_general_verify_bank_account(self):
        """Test case for accounting_general_verify_bank_account

        Verify bank account details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
