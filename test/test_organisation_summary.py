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
from openapi_client.model.addon_summary import AddonSummary
from openapi_client.model.application_summary import ApplicationSummary
from openapi_client.model.o_auth1_consumer_summary import OAuth1ConsumerSummary
from openapi_client.model.provider_summary import ProviderSummary
globals()['AddonSummary'] = AddonSummary
globals()['ApplicationSummary'] = ApplicationSummary
globals()['OAuth1ConsumerSummary'] = OAuth1ConsumerSummary
globals()['ProviderSummary'] = ProviderSummary
from openapi_client.model.organisation_summary import OrganisationSummary


class TestOrganisationSummary(unittest.TestCase):
    """OrganisationSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganisationSummary(self):
        """Test OrganisationSummary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrganisationSummary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
