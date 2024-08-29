# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.post_createorder_v7400_response import PostCreateorderV7400Response

class TestPostCreateorderV7400Response(unittest.TestCase):
    """PostCreateorderV7400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostCreateorderV7400Response:
        """Test PostCreateorderV7400Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCreateorderV7400Response`
        """
        model = PostCreateorderV7400Response()
        if include_optional:
            return PostCreateorderV7400Response(
                traceid = '',
                type = '',
                message = '',
                fields = [
                    xi.sdk.resellers.models.post_createorder_v7_400_response_fields_inner.post_createorder_v7_400_response_fields_inner(
                        field = '', 
                        message = '', 
                        value = '', )
                    ]
            )
        else:
            return PostCreateorderV7400Response(
        )
        """

    def testPostCreateorderV7400Response(self):
        """Test PostCreateorderV7400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
