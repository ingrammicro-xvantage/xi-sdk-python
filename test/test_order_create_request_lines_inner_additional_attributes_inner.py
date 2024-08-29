# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_request_lines_inner_additional_attributes_inner import OrderCreateRequestLinesInnerAdditionalAttributesInner

class TestOrderCreateRequestLinesInnerAdditionalAttributesInner(unittest.TestCase):
    """OrderCreateRequestLinesInnerAdditionalAttributesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateRequestLinesInnerAdditionalAttributesInner:
        """Test OrderCreateRequestLinesInnerAdditionalAttributesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateRequestLinesInnerAdditionalAttributesInner`
        """
        model = OrderCreateRequestLinesInnerAdditionalAttributesInner()
        if include_optional:
            return OrderCreateRequestLinesInnerAdditionalAttributesInner(
                attribute_name = '',
                attribute_value = ''
            )
        else:
            return OrderCreateRequestLinesInnerAdditionalAttributesInner(
        )
        """

    def testOrderCreateRequestLinesInnerAdditionalAttributesInner(self):
        """Test OrderCreateRequestLinesInnerAdditionalAttributesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
