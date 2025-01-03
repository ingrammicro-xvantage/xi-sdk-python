# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.product_search_response import ProductSearchResponse

class TestProductSearchResponse(unittest.TestCase):
    """ProductSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductSearchResponse:
        """Test ProductSearchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductSearchResponse`
        """
        model = ProductSearchResponse()
        if include_optional:
            return ProductSearchResponse(
                records_found = 56,
                page_size = 56,
                page_number = 56,
                catalog = [
                    xi.sdk.resellers.models.product_search_response_catalog_inner.ProductSearch_Response_catalog_inner(
                        description = '', 
                        category = '', 
                        sub_category = '', 
                        product_type = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        upc_code = '', 
                        vendor_name = '', 
                        end_user_required = '', 
                        has_discounts = '', 
                        type = '', 
                        discontinued = '', 
                        new_product = '', 
                        direct_ship = '', 
                        has_warranty = '', 
                        links = [
                            xi.sdk.resellers.models.product_search_response_catalog_inner_links_inner.ProductSearch_Response_catalog_inner_links_inner(
                                topic = '', 
                                href = '', 
                                type = '', )
                            ], 
                        extra_description = '', 
                        replacement_sku = '', 
                        authorized_to_purchase = '', )
                    ],
                subscription_catalog = [
                    xi.sdk.resellers.models.product_search_response_subscription_catalog_inner.ProductSearch_Response_subscriptionCatalog_inner(
                        group_name = '', 
                        group_description = '', 
                        number_of_plans = '', 
                        link = '', 
                        plans = [
                            xi.sdk.resellers.models.product_search_response_subscription_catalog_inner_plans_inner.ProductSearch_Response_subscriptionCatalog_inner_plans_inner(
                                plan_id = '', 
                                plan_name = '', 
                                plan_description = '', 
                                subscription_period_summary = [
                                    xi.sdk.resellers.models.product_search_response_subscription_catalog_inner_plans_inner_subscription_period_summary_inner.ProductSearch_Response_subscriptionCatalog_inner_plans_inner_subscriptionPeriodSummary_inner(
                                        subscription_period_unit = '', 
                                        subscription_period = '', )
                                    ], 
                                links = [
                                    xi.sdk.resellers.models.product_search_response_subscription_catalog_inner_plans_inner_links_inner.ProductSearch_Response_subscriptionCatalog_inner_plans_inner_links_inner(
                                        topic = '', 
                                        href = '', 
                                        type = '', )
                                    ], )
                            ], )
                    ],
                next_page = '',
                previous_page = ''
            )
        else:
            return ProductSearchResponse(
        )
        """

    def testProductSearchResponse(self):
        """Test ProductSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
