# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.error_response_errors_inner_fields_inner import ErrorResponseErrorsInnerFieldsInner

class TestErrorResponseErrorsInnerFieldsInner(unittest.TestCase):
    """ErrorResponseErrorsInnerFieldsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorResponseErrorsInnerFieldsInner:
        """Test ErrorResponseErrorsInnerFieldsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorResponseErrorsInnerFieldsInner`
        """
        model = ErrorResponseErrorsInnerFieldsInner()
        if include_optional:
            return ErrorResponseErrorsInnerFieldsInner(
                field = '',
                value = '',
                message = ''
            )
        else:
            return ErrorResponseErrorsInnerFieldsInner(
        )
        """

    def testErrorResponseErrorsInnerFieldsInner(self):
        """Test ErrorResponseErrorsInnerFieldsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
