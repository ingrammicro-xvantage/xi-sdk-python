# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.invoice_detailsv61_response_summary_totals import InvoiceDetailsv61ResponseSummaryTotals

class TestInvoiceDetailsv61ResponseSummaryTotals(unittest.TestCase):
    """InvoiceDetailsv61ResponseSummaryTotals unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailsv61ResponseSummaryTotals:
        """Test InvoiceDetailsv61ResponseSummaryTotals
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailsv61ResponseSummaryTotals`
        """
        model = InvoiceDetailsv61ResponseSummaryTotals()
        if include_optional:
            return InvoiceDetailsv61ResponseSummaryTotals(
                net_invoice_amount = 1.337,
                discount_amount = 1.337,
                discount_type = '',
                total_tax_amount = 1.337,
                invoiced_amount_due = 1.337,
                freight_amount = 1.337
            )
        else:
            return InvoiceDetailsv61ResponseSummaryTotals(
        )
        """

    def testInvoiceDetailsv61ResponseSummaryTotals(self):
        """Test InvoiceDetailsv61ResponseSummaryTotals"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
