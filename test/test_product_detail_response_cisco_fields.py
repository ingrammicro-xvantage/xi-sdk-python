# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.product_detail_response_cisco_fields import ProductDetailResponseCiscoFields

class TestProductDetailResponseCiscoFields(unittest.TestCase):
    """ProductDetailResponseCiscoFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductDetailResponseCiscoFields:
        """Test ProductDetailResponseCiscoFields
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductDetailResponseCiscoFields`
        """
        model = ProductDetailResponseCiscoFields()
        if include_optional:
            return ProductDetailResponseCiscoFields(
                product_sub_group = '',
                service_program_name = '',
                item_catalog_category = '',
                configuration_indicator = '',
                internal_business_entity = '',
                item_type = '',
                global_list_price = ''
            )
        else:
            return ProductDetailResponseCiscoFields(
        )
        """

    def testProductDetailResponseCiscoFields(self):
        """Test ProductDetailResponseCiscoFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
