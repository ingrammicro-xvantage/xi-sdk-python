# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

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
            include_option is a boolean, when False only required
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
