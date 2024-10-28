# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInner

class TestPriceAndAvailabilityResponseInnerSubscriptionPriceInner(unittest.TestCase):
    """PriceAndAvailabilityResponseInnerSubscriptionPriceInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityResponseInnerSubscriptionPriceInner:
        """Test PriceAndAvailabilityResponseInnerSubscriptionPriceInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityResponseInnerSubscriptionPriceInner`
        """
        model = PriceAndAvailabilityResponseInnerSubscriptionPriceInner()
        if include_optional:
            return PriceAndAvailabilityResponseInnerSubscriptionPriceInner(
                plan_id = '',
                plan_name = '',
                plan_description = 1.337,
                groups = [
                    xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_groups_inner.PriceAndAvailabilityResponse_inner_subscriptionPrice_inner_groups_inner(
                        group_name = '', 
                        group_description = '', )
                    ],
                billing_period = [
                    xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_billing_period_inner.PriceAndAvailabilityResponse_inner_subscriptionPrice_inner_billingPeriod_inner(
                        billing_period_unit = '', 
                        billing_period = '', )
                    ],
                subscription_period = [
                    xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_subscription_period_inner.PriceAndAvailabilityResponse_inner_subscriptionPrice_inner_subscriptionPeriod_inner(
                        subscription_period_unit = '', 
                        subscription_period = '', )
                    ],
                options = [
                    xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner.PriceAndAvailabilityResponse_inner_subscriptionPrice_inner_options_inner(
                        resource_id = '', 
                        resource_name = '', 
                        vendor_part_number = '', 
                        min_units = '', 
                        max_units = '', 
                        recurringpricemodel = '', 
                        unit_of_measure = '', 
                        resource_pricing = [
                            xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_resource_pricing_inner.PriceAndAvailabilityResponse_inner_subscriptionPrice_inner_options_inner_resourcePricing_inner(
                                name = '', 
                                quantity = 56, 
                                msrp = 1.337, 
                                unit_price = 1.337, 
                                margin = 1.337, 
                                currency_code = '', 
                                subscription_period = '', )
                            ], 
                        discounts = [
                            xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner.PriceAndAvailabilityResponse_inner_subscriptionPrice_inner_options_inner_discounts_inner(
                                volume_discounts = [
                                    xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_volume_discounts_inner.PriceAndAvailabilityResponse_inner_subscriptionPrice_inner_options_inner_discounts_inner_volumeDiscounts_inner(
                                        currency_code = '', 
                                        quantity = 56, 
                                        msrp = 1.337, 
                                        unit_price = 1.337, 
                                        margin = 1.337, )
                                    ], 
                                special_pricing = [
                                    xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_special_pricing_inner.PriceAndAvailabilityResponse_inner_subscriptionPrice_inner_options_inner_discounts_inner_specialPricing_inner(
                                        currency_code = '', 
                                        discount = 1.337, 
                                        discount_type = '', 
                                        discount_qty_limit = 56, 
                                        discount_expiry_date = '', 
                                        vendor_program_name = '', )
                                    ], )
                            ], 
                        fees = [
                            xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_fees_inner.PriceAndAvailabilityResponse_inner_subscriptionPrice_inner_options_inner_fees_inner(
                                price = 1.337, 
                                type = '', )
                            ], )
                    ]
            )
        else:
            return PriceAndAvailabilityResponseInnerSubscriptionPriceInner(
        )
        """

    def testPriceAndAvailabilityResponseInnerSubscriptionPriceInner(self):
        """Test PriceAndAvailabilityResponseInnerSubscriptionPriceInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
