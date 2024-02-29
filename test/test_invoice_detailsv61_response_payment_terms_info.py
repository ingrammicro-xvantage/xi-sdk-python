# coding: utf-8

"""
    XI Sdk Resellers

    For Ingram Micro Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.invoice_detailsv61_response_payment_terms_info import InvoiceDetailsv61ResponsePaymentTermsInfo

class TestInvoiceDetailsv61ResponsePaymentTermsInfo(unittest.TestCase):
    """InvoiceDetailsv61ResponsePaymentTermsInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetailsv61ResponsePaymentTermsInfo:
        """Test InvoiceDetailsv61ResponsePaymentTermsInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetailsv61ResponsePaymentTermsInfo`
        """
        model = InvoiceDetailsv61ResponsePaymentTermsInfo()
        if include_optional:
            return InvoiceDetailsv61ResponsePaymentTermsInfo(
                payment_terms_code = '',
                payment_terms_description = '',
                payment_terms_due_date = ''
            )
        else:
            return InvoiceDetailsv61ResponsePaymentTermsInfo(
        )
        """

    def testInvoiceDetailsv61ResponsePaymentTermsInfo(self):
        """Test InvoiceDetailsv61ResponsePaymentTermsInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
