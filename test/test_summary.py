"""
    Clever-Cloud API

    Public API for managing Clever-Cloud data and products  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: support@clever-cloud.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.organisation_summary import OrganisationSummary
from openapi_client.model.user_summary import UserSummary
globals()['OrganisationSummary'] = OrganisationSummary
globals()['UserSummary'] = UserSummary
from openapi_client.model.summary import Summary


class TestSummary(unittest.TestCase):
    """Summary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSummary(self):
        """Test Summary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Summary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()