# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.product_detail_response_technical_specifications_inner import ProductDetailResponseTechnicalSpecificationsInner

class TestProductDetailResponseTechnicalSpecificationsInner(unittest.TestCase):
    """ProductDetailResponseTechnicalSpecificationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductDetailResponseTechnicalSpecificationsInner:
        """Test ProductDetailResponseTechnicalSpecificationsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductDetailResponseTechnicalSpecificationsInner`
        """
        model = ProductDetailResponseTechnicalSpecificationsInner()
        if include_optional:
            return ProductDetailResponseTechnicalSpecificationsInner(
                headername = '',
                attributevalue = '',
                attributedisplay = '',
                attributename = ''
            )
        else:
            return ProductDetailResponseTechnicalSpecificationsInner(
        )
        """

    def testProductDetailResponseTechnicalSpecificationsInner(self):
        """Test ProductDetailResponseTechnicalSpecificationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
