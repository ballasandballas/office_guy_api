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
from office_guy_api.api.letter_by_click__letter_by_click_api import LetterByClickLetterByClickApi  # noqa: E501
from office_guy_api.rest import ApiException


class TestLetterByClickLetterByClickApi(unittest.TestCase):
    """LetterByClickLetterByClickApi unit test stubs"""

    def setUp(self):
        self.api = office_guy_api.api.letter_by_click__letter_by_click_api.LetterByClickLetterByClickApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_letter_by_click_letter_by_click_get_tracking_code(self):
        """Test case for letter_by_click_letter_by_click_get_tracking_code

        Get tracking code from Beeri's Letter by Click service.  Please note tracking codes are available ~30 minutes after sending the document using the API.  # noqa: E501
        """
        pass

    def test_letter_by_click_letter_by_click_send_document(self):
        """Test case for letter_by_click_letter_by_click_send_document

        Send mail through Beeri's Letter by Click service.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()