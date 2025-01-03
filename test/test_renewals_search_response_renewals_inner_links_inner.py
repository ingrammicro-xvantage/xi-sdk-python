# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.renewals_search_response_renewals_inner_links_inner import RenewalsSearchResponseRenewalsInnerLinksInner

class TestRenewalsSearchResponseRenewalsInnerLinksInner(unittest.TestCase):
    """RenewalsSearchResponseRenewalsInnerLinksInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenewalsSearchResponseRenewalsInnerLinksInner:
        """Test RenewalsSearchResponseRenewalsInnerLinksInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenewalsSearchResponseRenewalsInnerLinksInner`
        """
        model = RenewalsSearchResponseRenewalsInnerLinksInner()
        if include_optional:
            return RenewalsSearchResponseRenewalsInnerLinksInner(
                topic = '',
                href = '',
                type = ''
            )
        else:
            return RenewalsSearchResponseRenewalsInnerLinksInner(
        )
        """

    def testRenewalsSearchResponseRenewalsInnerLinksInner(self):
        """Test RenewalsSearchResponseRenewalsInnerLinksInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
