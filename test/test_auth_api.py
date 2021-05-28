"""
    Clever-Cloud API

    Public API for managing Clever-Cloud data and products  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: support@clever-cloud.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.auth_api import AuthApi  # noqa: E501


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self):
        self.api = AuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authorize_form(self):
        """Test case for authorize_form

        """
        pass

    def test_authorize_token(self):
        """Test case for authorize_token

        """
        pass

    def test_get_available_rights(self):
        """Test case for get_available_rights

        """
        pass

    def test_get_login_data(self):
        """Test case for get_login_data

        """
        pass

    def test_post_access_token_request(self):
        """Test case for post_access_token_request

        """
        pass

    def test_post_access_token_request_query(self):
        """Test case for post_access_token_request_query

        """
        pass

    def test_post_authorize(self):
        """Test case for post_authorize

        """
        pass

    def test_post_req_token_request(self):
        """Test case for post_req_token_request

        """
        pass

    def test_post_req_token_request_query_string(self):
        """Test case for post_req_token_request_query_string

        """
        pass


if __name__ == '__main__':
    unittest.main()