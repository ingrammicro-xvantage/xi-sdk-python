# coding: utf-8

"""
    XI Sdk Resellers

    For Ingram Micro Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.get_accesstoken500_response_fault import GetAccesstoken500ResponseFault

class TestGetAccesstoken500ResponseFault(unittest.TestCase):
    """GetAccesstoken500ResponseFault unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAccesstoken500ResponseFault:
        """Test GetAccesstoken500ResponseFault
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetAccesstoken500ResponseFault`
        """
        model = GetAccesstoken500ResponseFault()
        if include_optional:
            return GetAccesstoken500ResponseFault(
                faultstring = '',
                detail = xi.sdk.resellers.models.get_accesstoken_500_response_fault_detail.get_accesstoken_500_response_fault_detail(
                    errorcode = '', )
            )
        else:
            return GetAccesstoken500ResponseFault(
        )
        """

    def testGetAccesstoken500ResponseFault(self):
        """Test GetAccesstoken500ResponseFault"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
