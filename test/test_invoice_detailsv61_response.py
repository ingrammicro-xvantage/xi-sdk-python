# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.invoice_detailsv61_response import InvoiceDetailsv61Response

class TestInvoiceDetailsv61Response(unittest.TestCase):
    """InvoiceDetailsv61Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailsv61Response:
        """Test InvoiceDetailsv61Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailsv61Response`
        """
        model = InvoiceDetailsv61Response()
        if include_optional:
            return InvoiceDetailsv61Response(
                invoice_number = '',
                invoice_status = '',
                invoice_date = '',
                customer_order_number = '',
                end_customer_order_number = '',
                order_number = '',
                order_date = '',
                bill_to_id = '',
                invoice_type = '',
                invoice_due_date = '',
                customer_country_code = '',
                customer_number = '',
                ingram_order_number = '',
                notes = '',
                payment_terms_info = xi.sdk.resellers.models.invoice_detailsv6_1_response_payment_terms_info.InvoiceDetailsv6_1Response_paymentTermsInfo(
                    payment_terms_code = '', 
                    payment_terms_description = '', 
                    payment_terms_due_date = '', ),
                bill_to_info = xi.sdk.resellers.models.invoice_detailsv6_1_response_bill_to_info.InvoiceDetailsv6_1Response_billToInfo(
                    contact = '', 
                    company_name = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = '', 
                    email = '', ),
                ship_to_info = xi.sdk.resellers.models.invoice_detailsv6_1_response_ship_to_info.InvoiceDetailsv6_1Response_shipToInfo(
                    contact = '', 
                    company_name = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = '', 
                    email = '', ),
                lines = [
                    xi.sdk.resellers.models.invoice_detailsv6_1_response_lines_inner.InvoiceDetailsv6_1Response_lines_inner(
                        ingram_line_number = '', 
                        customer_line_number = '0', 
                        ingram_part_number = '', 
                        upc = '', 
                        vendor_part_number = '', 
                        customer_part_number = '', 
                        vendor_name = '', 
                        product_description = '', 
                        unit_weight = 1.337, 
                        quantity = 56, 
                        unit_price = 1.337, 
                        unit_of_measure = '', 
                        currency_code = '', 
                        extended_price = 1.337, 
                        tax_percentage = 1.337, 
                        tax_rate = 1.337, 
                        tax_amount = 1.337, 
                        serial_numbers = [
                            xi.sdk.resellers.models.invoice_detailsv6_1_response_lines_inner_serial_numbers_inner.InvoiceDetailsv6_1Response_lines_inner_serialNumbers_inner(
                                serial_number = '', )
                            ], 
                        quantity_ordered = 56, 
                        quantity_shipped = 56, )
                    ],
                fx_rate_info = xi.sdk.resellers.models.invoice_detailsv6_1_response_fx_rate_info.InvoiceDetailsv6_1Response_fxRateInfo(
                    currency_code = '', 
                    company_currency = '', 
                    invoice_currency = '', 
                    currency_fx_rate = 1.337, ),
                summary = xi.sdk.resellers.models.invoice_detailsv6_1_response_summary.InvoiceDetailsv6_1Response_summary(
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
                        invoiced_amount_due = 1.337, 
                        freight_amount = 1.337, ), 
                    foreign_fx_totals = xi.sdk.resellers.models.invoice_detailsv6_1_response_summary_foreign_fx_totals.InvoiceDetailsv6_1Response_summary_foreignFxTotals(
                        foreign_currency_code = '', 
                        foreign_currency_fx_rate = 1.337, 
                        foreign_total_taxable_amount = '', 
                        foreign_total_tax_amount = 1.337, 
                        foreign_invoice_amount_due = '', ), )
            )
        else:
            return InvoiceDetailsv61Response(
        )
        """

    def testInvoiceDetailsv61Response(self):
        """Test InvoiceDetailsv61Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
