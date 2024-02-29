# coding: utf-8

"""
    XI Sdk Resellers

    For Ingram Micro Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.returns_create_request import ReturnsCreateRequest

class TestReturnsCreateRequest(unittest.TestCase):
    """ReturnsCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReturnsCreateRequest:
        """Test ReturnsCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReturnsCreateRequest`
        """
        model = ReturnsCreateRequest()
        if include_optional:
            return ReturnsCreateRequest(
                list = [
                    xi.sdk.resellers.models.returns_create_request_list_inner.returnsCreateRequest_list_inner(
                        invoice_number = '', 
                        invoice_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        customer_order_number = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        serial_number = '', 
                        quantity = 56, 
                        primary_reason = '', 
                        secondary_reason = '', 
                        notes = '', 
                        reference_number = '', 
                        bill_to_address_id = '', 
                        ship_from_info = [
                            xi.sdk.resellers.models.returns_create_request_list_inner_ship_from_info_inner.returnsCreateRequest_list_inner_shipFromInfo_inner(
                                company_name = '', 
                                contact = '', 
                                address_line1 = '', 
                                address_line2 = '', 
                                address_line3 = '', 
                                city = '', 
                                state = '', 
                                postal_code = '', 
                                country_code = '', 
                                email = '', 
                                phone_number = '', )
                            ], 
                        number_of_boxes = 56, )
                    ]
            )
        else:
            return ReturnsCreateRequest(
        )
        """

    def testReturnsCreateRequest(self):
        """Test ReturnsCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
