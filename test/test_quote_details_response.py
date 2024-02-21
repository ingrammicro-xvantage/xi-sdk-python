# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.quote_details_response import QuoteDetailsResponse

class TestQuoteDetailsResponse(unittest.TestCase):
    """QuoteDetailsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteDetailsResponse:
        """Test QuoteDetailsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteDetailsResponse`
        """
        model = QuoteDetailsResponse()
        if include_optional:
            return QuoteDetailsResponse(
                quote_name = '',
                quote_number = '',
                revision = '',
                ingram_quote_date = '',
                last_modified_date = '',
                ingram_quote_expiry_date = '',
                currency_code = '',
                closing_reason = '',
                special_bid_id = '',
                special_bid_effective_date = '',
                special_bid_expiration_date = '',
                status = '',
                customer_need = '',
                proposed_solution = '',
                intro_preamble = '',
                purchase_instructions = '',
                legal_terms = '',
                quote_type = '',
                lease_info = '',
                leasing_instructions = '',
                quote_syb_type = '',
                reseller_info = xi.sdk.resellers.models.quote_details_response_reseller_info.QuoteDetailsResponse_resellerInfo(
                    contact = '', 
                    company_name = '', 
                    email = '', 
                    phone_number = '', 
                    customer_number = '', ),
                end_user_info = xi.sdk.resellers.models.quote_details_response_end_user_info.QuoteDetailsResponse_endUserInfo(
                    contact = '', 
                    company_name = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    city = '', 
                    state = '', 
                    email = '', 
                    phone_number = '', 
                    postal_code = '', 
                    market_segment = '', ),
                products = [
                    xi.sdk.resellers.models.quote_details_response_products_inner.QuoteDetailsResponse_products_inner(
                        quote_product_guid = '', 
                        line_number = '', 
                        quantity = 56, 
                        notes = '', 
                        ean = '', 
                        co_o = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        description = '', 
                        weight = 56, 
                        weight_uom = '', 
                        is_suggestion_product = True, 
                        vpn_category = '', 
                        quote_products_supplier_part_auxiliary_id = '', 
                        vendor_name = '', 
                        terms = '', 
                        price = xi.sdk.resellers.models.quote_details_response_products_inner_price.QuoteDetailsResponse_products_inner_price(
                            quote_price = 56, 
                            msrp = 56, 
                            extended_msrp = 56, 
                            extended_quote_price = 56, 
                            discount_off_list = 1.337, ), )
                    ],
                products_count = 56,
                extended_msrp_total = 56,
                quantity_total = 56,
                extended_quote_price_total = 56,
                additional_attributes = [
                    xi.sdk.resellers.models.quote_details_response_additional_attributes_inner.QuoteDetailsResponse_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ]
            )
        else:
            return QuoteDetailsResponse(
        )
        """

    def testQuoteDetailsResponse(self):
        """Test QuoteDetailsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
