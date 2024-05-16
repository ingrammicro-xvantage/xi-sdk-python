# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.post_async_order_create_v7400_response_fields_inner import PostAsyncOrderCreateV7400ResponseFieldsInner

class TestPostAsyncOrderCreateV7400ResponseFieldsInner(unittest.TestCase):
    """PostAsyncOrderCreateV7400ResponseFieldsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostAsyncOrderCreateV7400ResponseFieldsInner:
        """Test PostAsyncOrderCreateV7400ResponseFieldsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostAsyncOrderCreateV7400ResponseFieldsInner`
        """
        model = PostAsyncOrderCreateV7400ResponseFieldsInner()
        if include_optional:
            return PostAsyncOrderCreateV7400ResponseFieldsInner(
                var_field = '',
                message = '',
                value = ''
            )
        else:
            return PostAsyncOrderCreateV7400ResponseFieldsInner(
        )
        """

    def testPostAsyncOrderCreateV7400ResponseFieldsInner(self):
        """Test PostAsyncOrderCreateV7400ResponseFieldsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()