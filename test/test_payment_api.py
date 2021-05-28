"""
    Clever-Cloud API

    Public API for managing Clever-Cloud data and products  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: support@clever-cloud.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.payment_api import PaymentApi  # noqa: E501


class TestPaymentApi(unittest.TestCase):
    """PaymentApi unit test stubs"""

    def setUp(self):
        self.api = PaymentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_vat(self):
        """Test case for check_vat

        """
        pass

    def test_end_payment_with_stripe(self):
        """Test case for end_payment_with_stripe

        """
        pass

    def test_get_available_payment_providers(self):
        """Test case for get_available_payment_providers

        """
        pass

    def test_get_coupon(self):
        """Test case for get_coupon

        """
        pass

    def test_get_invoice_status_button(self):
        """Test case for get_invoice_status_button

        """
        pass

    def test_get_stripe_token(self):
        """Test case for get_stripe_token

        """
        pass

    def test_stripe_sepa_webhook(self):
        """Test case for stripe_sepa_webhook

        """
        pass

    def test_update_stripe_payment(self):
        """Test case for update_stripe_payment

        """
        pass

    def test_validate(self):
        """Test case for validate

        """
        pass


if __name__ == '__main__':
    unittest.main()
