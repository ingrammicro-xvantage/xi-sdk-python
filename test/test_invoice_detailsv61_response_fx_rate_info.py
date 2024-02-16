# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.invoice_detailsv61_response_fx_rate_info import InvoiceDetailsv61ResponseFxRateInfo

class TestInvoiceDetailsv61ResponseFxRateInfo(unittest.TestCase):
    """InvoiceDetailsv61ResponseFxRateInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailsv61ResponseFxRateInfo:
        """Test InvoiceDetailsv61ResponseFxRateInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailsv61ResponseFxRateInfo`
        """
        model = InvoiceDetailsv61ResponseFxRateInfo()
        if include_optional:
            return InvoiceDetailsv61ResponseFxRateInfo(
                currency_code = '',
                company_currency = '',
                invoice_currency = '',
                currency_fx_rate = 1.337
            )
        else:
            return InvoiceDetailsv61ResponseFxRateInfo(
        )
        """

    def testInvoiceDetailsv61ResponseFxRateInfo(self):
        """Test InvoiceDetailsv61ResponseFxRateInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
