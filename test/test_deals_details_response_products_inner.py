# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.deals_details_response_products_inner import DealsDetailsResponseProductsInner

class TestDealsDetailsResponseProductsInner(unittest.TestCase):
    """DealsDetailsResponseProductsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DealsDetailsResponseProductsInner:
        """Test DealsDetailsResponseProductsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DealsDetailsResponseProductsInner`
        """
        model = DealsDetailsResponseProductsInner()
        if include_optional:
            return DealsDetailsResponseProductsInner(
                ingram_part_number = '',
                vendor_part_number = '',
                upc = '',
                product_description = '',
                msrp = 1.337,
                extended_msrp = 1.337,
                standard_price = 1.337,
                approved_quantity = 56,
                remaining_quantity = 56,
                comments = '',
                special_conditions = '',
                start_date = '',
                expiration_date = '',
                days_remaining = 56
            )
        else:
            return DealsDetailsResponseProductsInner(
        )
        """

    def testDealsDetailsResponseProductsInner(self):
        """Test DealsDetailsResponseProductsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
