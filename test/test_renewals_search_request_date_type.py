# coding: utf-8

"""
    XI Sdk Resellers

    For Ingram Micro Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.renewals_search_request_date_type import RenewalsSearchRequestDateType

class TestRenewalsSearchRequestDateType(unittest.TestCase):
    """RenewalsSearchRequestDateType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenewalsSearchRequestDateType:
        """Test RenewalsSearchRequestDateType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenewalsSearchRequestDateType`
        """
        model = RenewalsSearchRequestDateType()
        if include_optional:
            return RenewalsSearchRequestDateType(
                start_date = xi.sdk.resellers.models.renewals_search_request_date_type_start_date.renewalsSearchRequest_dateType_startDate(
                    custom_start_date = '', 
                    custom_end_date = '', ),
                end_date = xi.sdk.resellers.models.renewals_search_request_date_type_end_date.renewalsSearchRequest_dateType_endDate(
                    custom_start_date = '', 
                    custom_end_date = '', ),
                invoice_date = xi.sdk.resellers.models.renewals_search_request_date_type_invoice_date.renewalsSearchRequest_dateType_invoiceDate(
                    custom_start_date = '', 
                    custom_end_date = '', ),
                expiration_date = xi.sdk.resellers.models.renewals_search_request_date_type_expiration_date.renewalsSearchRequest_dateType_expirationDate(
                    custom_start_date = '', 
                    custom_end_date = '', )
            )
        else:
            return RenewalsSearchRequestDateType(
        )
        """

    def testRenewalsSearchRequestDateType(self):
        """Test RenewalsSearchRequestDateType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
