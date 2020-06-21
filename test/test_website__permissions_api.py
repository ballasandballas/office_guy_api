# coding: utf-8

"""
    OfficeGuy API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2020-06-20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import office_guy_api
from api.website__permissions_api import WebsitePermissionsApi  # noqa: E501
from office_guy_api.rest import ApiException


class TestWebsitePermissionsApi(unittest.TestCase):
    """WebsitePermissionsApi unit test stubs"""

    def setUp(self):
        self.api = api.website__permissions_api.WebsitePermissionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_website_permissions_remove(self):
        """Test case for website_permissions_remove

        Remove user permission  # noqa: E501
        """
        pass

    def test_website_permissions_set(self):
        """Test case for website_permissions_set

        Grant user permission  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
