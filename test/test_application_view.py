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
from openapi_client.model.deployment_info_view import DeploymentInfoView
from openapi_client.model.flavor_view import FlavorView
from openapi_client.model.instance_view import InstanceView
from openapi_client.model.vhost_view import VhostView
globals()['DeploymentInfoView'] = DeploymentInfoView
globals()['FlavorView'] = FlavorView
globals()['InstanceView'] = InstanceView
globals()['VhostView'] = VhostView
from openapi_client.model.application_view import ApplicationView


class TestApplicationView(unittest.TestCase):
    """ApplicationView unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationView(self):
        """Test ApplicationView"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationView()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
