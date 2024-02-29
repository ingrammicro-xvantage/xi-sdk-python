# coding: utf-8

"""
    XI Sdk Resellers

    For Ingram Micro Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.get_reseller_v6_validate_quote500_response import GetResellerV6ValidateQuote500Response

class TestGetResellerV6ValidateQuote500Response(unittest.TestCase):
    """GetResellerV6ValidateQuote500Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetResellerV6ValidateQuote500Response:
        """Test GetResellerV6ValidateQuote500Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetResellerV6ValidateQuote500Response`
        """
        model = GetResellerV6ValidateQuote500Response()
        if include_optional:
            return GetResellerV6ValidateQuote500Response(
                traceid = '',
                type = '',
                message = '',
                fields = [
                    None
                    ]
            )
        else:
            return GetResellerV6ValidateQuote500Response(
        )
        """

    def testGetResellerV6ValidateQuote500Response(self):
        """Test GetResellerV6ValidateQuote500Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
