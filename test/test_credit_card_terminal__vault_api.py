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
from office_guy_api.api.credit_card_terminal__vault_api import CreditCardTerminalVaultApi  # noqa: E501
from office_guy_api.rest import ApiException


class TestCreditCardTerminalVaultApi(unittest.TestCase):
    """CreditCardTerminalVaultApi unit test stubs"""

    def setUp(self):
        self.api = office_guy_api.api.credit_card_terminal__vault_api.CreditCardTerminalVaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_credit_guy_vault_tokenize(self):
        """Test case for credit_guy_vault_tokenize

        Tokenize card (card number-&gt;token)  # noqa: E501
        """
        pass

    def test_credit_guy_vault_tokenize_single_use(self):
        """Test case for credit_guy_vault_tokenize_single_use

        Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.  # noqa: E501
        """
        pass

    def test_credit_guy_vault_tokenize_single_use_json(self):
        """Test case for credit_guy_vault_tokenize_single_use_json

        Tokenize payment details (Card Number, Expiration, CVV, CitizenID) for single usage.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()