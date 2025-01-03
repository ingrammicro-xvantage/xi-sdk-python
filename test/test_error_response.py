# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.error_response import ErrorResponse

class TestErrorResponse(unittest.TestCase):
    """ErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorResponse:
        """Test ErrorResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorResponse`
        """
        model = ErrorResponse()
        if include_optional:
            return ErrorResponse(
                errors = [
                    xi.sdk.resellers.models.error_response_errors_inner.ErrorResponse_errors_inner(
                        id = '', 
                        type = '', 
                        message = '', 
                        fields = [
                            xi.sdk.resellers.models.error_response_errors_inner_fields_inner.ErrorResponse_errors_inner_fields_inner(
                                field = '', 
                                value = '', 
                                message = '', )
                            ], )
                    ]
            )
        else:
            return ErrorResponse(
        )
        """

    def testErrorResponse(self):
        """Test ErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
