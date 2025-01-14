# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.async_order_create_dto import AsyncOrderCreateDTO

class TestAsyncOrderCreateDTO(unittest.TestCase):
    """AsyncOrderCreateDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AsyncOrderCreateDTO:
        """Test AsyncOrderCreateDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AsyncOrderCreateDTO`
        """
        model = AsyncOrderCreateDTO()
        if include_optional:
            return AsyncOrderCreateDTO(
                quote_number = '',
                customer_order_number = '',
                end_customer_order_number = '',
                notes = '',
                bill_to_address_id = '',
                special_bid_number = '',
                internal_comments = '',
                accept_back_order = True,
                vend_auth_number = '',
                reseller_info = xi.sdk.resellers.models.async_order_create_dto_reseller_info.AsyncOrderCreateDTO_resellerInfo(
                    reseller_id = '', 
                    company_name = '', 
                    contact = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    address_line4 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    phone_number = '', 
                    email = '', ),
                end_user_info = xi.sdk.resellers.models.async_order_create_dto_end_user_info.AsyncOrderCreateDTO_endUserInfo(
                    end_user_id = '', 
                    end_user_type = '', 
                    company_name = '', 
                    name1 = '', 
                    name2 = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    contact = '', 
                    name3 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    address_line4 = '', 
                    country_code = '', 
                    phone_number = '', 
                    email = '', ),
                ship_to_info = xi.sdk.resellers.models.async_order_create_dto_ship_to_info.AsyncOrderCreateDTO_shipToInfo(
                    address_id = '', 
                    contact = '', 
                    company_name = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    address_line4 = '', 
                    name1 = '', 
                    name2 = '', 
                    city = '', 
                    state = '', 
                    postal_code = '', 
                    country_code = '', 
                    email = '', 
                    shipping_notes = '', 
                    phone_number = '', ),
                shipment_details = xi.sdk.resellers.models.async_order_create_dto_shipment_details.AsyncOrderCreateDTO_shipmentDetails(
                    carrier_code = '', 
                    requested_delivery_date = '', 
                    ship_complete = '', 
                    shipping_instructions = '', 
                    freight_account_number = '', 
                    signature_required = True, ),
                additional_attributes = [
                    xi.sdk.resellers.models.async_order_create_dto_additional_attributes_inner.AsyncOrderCreateDTO_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ],
                vmfadditional_attributes = [
                    xi.sdk.resellers.models.async_order_create_dto_vmfadditional_attributes_inner.AsyncOrderCreateDTO_vmfadditionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ],
                lines = [
                    xi.sdk.resellers.models.async_order_create_dto_lines_inner.AsyncOrderCreateDTO_lines_inner(
                        customer_line_number = '', 
                        ingram_part_number = '', 
                        quantity = '', 
                        unit_price = '', 
                        special_bid_number = '', 
                        end_user_price = '', 
                        notes = '', 
                        end_user_info = [
                            xi.sdk.resellers.models.async_order_create_dto_lines_inner_end_user_info_inner.AsyncOrderCreateDTO_lines_inner_endUserInfo_inner(
                                end_user_id = '', 
                                end_user_type = '', 
                                company_name = '', 
                                name1 = '', 
                                name2 = '', 
                                contact_id = '', 
                                address_line1 = '', 
                                address_line2 = '', 
                                address_line3 = '', 
                                contact = '', 
                                city = '', 
                                state = '', 
                                postal_code = '', 
                                address_line4 = '', 
                                country_code = '', 
                                phone_number = '', 
                                email = '', )
                            ], )
                    ],
                warranty_info = [
                    xi.sdk.resellers.models.async_order_create_dto_warranty_info_inner.AsyncOrderCreateDTO_warrantyInfo_inner(
                        hardware_line_link = '', 
                        warranty_line_link = '', 
                        direct_line_link = '', 
                        serial_info = [
                            xi.sdk.resellers.models.async_order_create_dto_warranty_info_inner_serial_info_inner.AsyncOrderCreateDTO_warrantyInfo_inner_serialInfo_inner(
                                date_of_purchase = '', 
                                ship_date = '', 
                                primary_serial_number = '', 
                                secondary_serial_number = '', )
                            ], 
                        vmf_additional_attributes_lines = [
                            xi.sdk.resellers.models.async_order_create_dto_warranty_info_inner_vmf_additional_attributes_lines_inner.AsyncOrderCreateDTO_warrantyInfo_inner_vmfAdditionalAttributesLines_inner(
                                attribute_name = '', 
                                attribute_value = '', )
                            ], )
                    ]
            )
        else:
            return AsyncOrderCreateDTO(
        )
        """

    def testAsyncOrderCreateDTO(self):
        """Test AsyncOrderCreateDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
