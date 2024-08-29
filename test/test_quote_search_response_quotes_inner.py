# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.quote_search_response_quotes_inner import QuoteSearchResponseQuotesInner

class TestQuoteSearchResponseQuotesInner(unittest.TestCase):
    """QuoteSearchResponseQuotesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteSearchResponseQuotesInner:
        """Test QuoteSearchResponseQuotesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteSearchResponseQuotesInner`
        """
        model = QuoteSearchResponseQuotesInner()
        if include_optional:
            return QuoteSearchResponseQuotesInner(
                quote_guid = '',
                quote_name = '',
                quote_number = '',
                revision = '',
                currency_code = '',
                end_user_contact = '',
                special_bid_number = '',
                quote_total = 1.337,
                quote_status = '',
                ingram_quote_date = '',
                last_modified_date = '',
                ingram_quote_expiry_date = '',
                end_user_name = '',
                vendor = '',
                created_by = '',
                quote_type = '',
                links = xi.sdk.resellers.models.quote_search_response_quotes_inner_links.QuoteSearchResponse_quotes_inner_links(
                    topic = '', 
                    href = '', 
                    type = '', )
            )
        else:
            return QuoteSearchResponseQuotesInner(
        )
        """

    def testQuoteSearchResponseQuotesInner(self):
        """Test QuoteSearchResponseQuotesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
