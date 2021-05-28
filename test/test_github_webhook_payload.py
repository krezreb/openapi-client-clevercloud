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
from openapi_client.model.github_commit import GithubCommit
from openapi_client.model.github_webhook_pusher import GithubWebhookPusher
from openapi_client.model.github_webhook_repository import GithubWebhookRepository
from openapi_client.model.github_webhook_sender import GithubWebhookSender
globals()['GithubCommit'] = GithubCommit
globals()['GithubWebhookPusher'] = GithubWebhookPusher
globals()['GithubWebhookRepository'] = GithubWebhookRepository
globals()['GithubWebhookSender'] = GithubWebhookSender
from openapi_client.model.github_webhook_payload import GithubWebhookPayload


class TestGithubWebhookPayload(unittest.TestCase):
    """GithubWebhookPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGithubWebhookPayload(self):
        """Test GithubWebhookPayload"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GithubWebhookPayload()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
