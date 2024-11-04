# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_resource_pricing_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner

class TestPriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner(unittest.TestCase):
    """PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner:
        """Test PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner`
        """
        model = PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner()
        if include_optional:
            return PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner(
                name = '',
                quantity = 56,
                msrp = 1.337,
                unit_price = 1.337,
                margin = 1.337,
                currency_code = '',
                subscription_period = ''
            )
        else:
            return PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner(
        )
        """

    def testPriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner(self):
        """Test PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerResourcePricingInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()