# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_v7_response201 import OrderCreateV7Response201

class TestOrderCreateV7Response201(unittest.TestCase):
    """OrderCreateV7Response201 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateV7Response201:
        """Test OrderCreateV7Response201
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateV7Response201`
        """
        model = OrderCreateV7Response201()
        if include_optional:
            return OrderCreateV7Response201(
                quote_number = '',
                confirmation_number = '987654322',
                message = ''
            )
        else:
            return OrderCreateV7Response201(
        )
        """

    def testOrderCreateV7Response201(self):
        """Test OrderCreateV7Response201"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
