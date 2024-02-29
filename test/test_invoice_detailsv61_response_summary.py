# coding: utf-8

"""
    XI Sdk Resellers

    For Ingram Micro Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.invoice_detailsv61_response_summary import InvoiceDetailsv61ResponseSummary

class TestInvoiceDetailsv61ResponseSummary(unittest.TestCase):
    """InvoiceDetailsv61ResponseSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailsv61ResponseSummary:
        """Test InvoiceDetailsv61ResponseSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailsv61ResponseSummary`
        """
        model = InvoiceDetailsv61ResponseSummary()
        if include_optional:
            return InvoiceDetailsv61ResponseSummary(
                lines = xi.sdk.resellers.models.invoice_detailsv6_1_response_summary_lines.InvoiceDetailsv6_1Response_summary_lines(
                    product_line_count = 56, 
                    product_line_total_quantity = 56, ),
                misc_charges = [
                    xi.sdk.resellers.models.invoice_detailsv6_1_response_summary_misc_charges_inner.InvoiceDetailsv6_1Response_summary_miscCharges_inner(
                        charge_description = '', 
                        misc_charge_line_count = 56, 
                        misc_charge_line_total = 1.337, 
                        charge_line_reference = '', 
                        is_non_misc = '', )
                    ],
                totals = xi.sdk.resellers.models.invoice_detailsv6_1_response_summary_totals.InvoiceDetailsv6_1Response_summary_totals(
                    net_invoice_amount = 1.337, 
                    discount_amount = 1.337, 
                    discount_type = '', 
                    total_tax_amount = 1.337, 
                    invoices_amount_due = 1.337, 
                    freight_amount = 1.337, ),
                foreign_fx_totals = xi.sdk.resellers.models.invoice_detailsv6_1_response_summary_foreign_fx_totals.InvoiceDetailsv6_1Response_summary_foreignFxTotals(
                    foreign_currency_code = '', 
                    foreign_currency_fx_rate = 1.337, 
                    foreign_total_taxable_amount = '', 
                    foreign_total_tax_amount = 1.337, 
                    foreign_invoice_amount_due = '', )
            )
        else:
            return InvoiceDetailsv61ResponseSummary(
        )
        """

    def testInvoiceDetailsv61ResponseSummary(self):
        """Test InvoiceDetailsv61ResponseSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
