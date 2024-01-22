# coding: utf-8

"""
    Reseller API

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi.sdk.resellers.models.quote_product_list import QuoteProductList

class TestQuoteProductList(unittest.TestCase):
    """QuoteProductList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteProductList:
        """Test QuoteProductList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteProductList`
        """
        model = QuoteProductList()
        if include_optional:
            return QuoteProductList(
                quote_product_guid = '',
                quantity = '',
                comments = '',
                bid_start_date = '',
                bid_expiry_date = '',
                sku = '',
                line_number = '',
                description = '',
                vendor_part_number = '',
                weight = '',
                is_suggestion_product = '',
                vpn_category = '',
                quote_products_supplier_part_auxiliary_id = '',
                quote_products_vendor = '',
                price = xi.sdk.resellers.models.quote_product_list_price.quoteProductList_price(
                    quote_price = 1.337, 
                    msrp = 1.337, 
                    extended_msrp = 1.337, 
                    extended_quote_price = 1.337, )
            )
        else:
            return QuoteProductList(
        )
        """

    def testQuoteProductList(self):
        """Test QuoteProductList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()