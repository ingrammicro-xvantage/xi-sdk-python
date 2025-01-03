# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_v7_request import OrderCreateV7Request

class TestOrderCreateV7Request(unittest.TestCase):
    """OrderCreateV7Request unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateV7Request:
        """Test OrderCreateV7Request
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateV7Request`
        """
        model = OrderCreateV7Request()
        if include_optional:
            return OrderCreateV7Request(
                quote_number = '',
                customer_order_number = '',
                end_customer_order_number = '',
                notes = '',
                bill_to_address_id = '',
                special_bid_number = '',
                accept_back_order = True,
                vend_auth_number = '',
                reseller_info = xi.sdk.resellers.models.order_create_v7_request_reseller_info.order_create_v7_request_resellerInfo(
                    reseller_id = '', 
                    company_name = '', 
                    contact = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = 56, 
                    email = '', ),
                end_user_info = xi.sdk.resellers.models.order_create_v7_request_end_user_info.order_create_v7_request_endUserInfo(
                    end_user_id = '', 
                    contact = '', 
                    company_name = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = 56, 
                    email = '', ),
                ship_to_info = xi.sdk.resellers.models.order_create_v7_request_ship_to_info.order_create_v7_request_shipToInfo(
                    address_id = '', 
                    contact = '', 
                    company_name = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    email = '', 
                    shipping_notes = '', 
                    phone_number = '', ),
                shipment_details = xi.sdk.resellers.models.order_create_v7_request_shipment_details.order_create_v7_request_shipmentDetails(
                    carrier_code = '', 
                    requested_delivery_date = '', 
                    ship_complete = '', 
                    shipping_instructions = '', 
                    freight_account_number = '', 
                    signature_required = True, ),
                additional_attributes = [
                    xi.sdk.resellers.models.order_create_v7_request_additional_attributes_inner.order_create_v7_request_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ],
                vmf_additional_attributes = [
                    xi.sdk.resellers.models.order_create_v7_request_vmf_additional_attributes_inner.order_create_v7_request_vmfAdditionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ],
                lines = [
                    xi.sdk.resellers.models.order_create_v7_request_lines_inner.order_create_v7_request_lines_inner(
                        customer_line_number = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        quantity = 56, 
                        unit_price = 1.337, 
                        special_bid_number = '', 
                        end_user_price = 1.337, 
                        notes = '', 
                        end_user_info = [
                            xi.sdk.resellers.models.order_create_v7_request_lines_inner_end_user_info_inner.order_create_v7_request_lines_inner_endUserInfo_inner(
                                end_user_id = '', 
                                end_user_type = '', 
                                company_name = '', 
                                address_line1 = '', 
                                address_line2 = '', 
                                contact = '', 
                                city = '', 
                                state = '', 
                                postal_code = '', 
                                country_code = '', 
                                phone_number = '', 
                                email = '', )
                            ], 
                        additional_attributes = [
                            xi.sdk.resellers.models.order_create_v7_request_lines_inner_additional_attributes_inner.order_create_v7_request_lines_inner_additionalAttributes_inner(
                                attribute_name = '', 
                                attribute_value = '', )
                            ], 
                        warranty_info = [
                            xi.sdk.resellers.models.order_create_v7_request_lines_inner_warranty_info_inner.order_create_v7_request_lines_inner_warrantyInfo_inner(
                                hardware_line_link = '', 
                                warranty_line_link = '', 
                                direct_line_link = '', 
                                serial_info = [
                                    xi.sdk.resellers.models.order_create_v7_request_lines_inner_warranty_info_inner_serial_info_inner.order_create_v7_request_lines_inner_warrantyInfo_inner_serialInfo_inner(
                                        date_of_purchase = '', 
                                        ship_date = '', 
                                        primary_serial_number = '', 
                                        secondary_serial_number = '', )
                                    ], )
                            ], 
                        vmf_additional_attributes_lines = [
                            xi.sdk.resellers.models.order_create_v7_request_lines_inner_vmf_additional_attributes_lines_inner.order_create_v7_request_lines_inner_vmfAdditionalAttributesLines_inner(
                                attribute_name = '', 
                                attribute_value = '', )
                            ], )
                    ]
            )
        else:
            return OrderCreateV7Request(
        )
        """

    def testOrderCreateV7Request(self):
        """Test OrderCreateV7Request"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
