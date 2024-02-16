# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_response_orders_inner import OrderCreateResponseOrdersInner

class TestOrderCreateResponseOrdersInner(unittest.TestCase):
    """OrderCreateResponseOrdersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateResponseOrdersInner:
        """Test OrderCreateResponseOrdersInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateResponseOrdersInner`
        """
        model = OrderCreateResponseOrdersInner()
        if include_optional:
            return OrderCreateResponseOrdersInner(
                number_of_lines_with_success = 56,
                number_of_lines_with_error = 56,
                number_of_lines_with_warning = 56,
                ingram_order_number = '',
                ingram_order_date = '',
                notes = '',
                order_type = '',
                order_total = 1.337,
                freight_charges = 1.337,
                total_tax = 1.337,
                currency_code = '',
                lines = [
                    xi.sdk.resellers.models.order_create_response_orders_inner_lines_inner.OrderCreateResponse_orders_inner_lines_inner(
                        sub_order_number = '', 
                        ingram_line_number = '', 
                        customer_line_number = '', 
                        line_status = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        unit_price = 1.337, 
                        extended_unit_price = 1.337, 
                        quantity_ordered = 56, 
                        quantity_confirmed = 56, 
                        quantity_back_ordered = 56, 
                        special_bid_number = '', 
                        notes = '', 
                        shipment_details = [
                            xi.sdk.resellers.models.order_create_response_orders_inner_lines_inner_shipment_details_inner.OrderCreateResponse_orders_inner_lines_inner_shipmentDetails_inner(
                                carrier_code = '', 
                                carrier_name = '', 
                                ship_from_warehouse_id = '', 
                                ship_from_location = '', 
                                freight_account_number = '', 
                                signature_required = '', 
                                shipping_instructions = '', )
                            ], 
                        additional_attributes = [
                            xi.sdk.resellers.models.order_create_response_orders_inner_lines_inner_additional_attributes_inner.OrderCreateResponse_orders_inner_lines_inner_additionalAttributes_inner(
                                attribute_name = '', 
                                attribute_value = '', )
                            ], )
                    ],
                miscellaneous_charges = [
                    xi.sdk.resellers.models.order_create_response_orders_inner_miscellaneous_charges_inner.OrderCreateResponse_orders_inner_miscellaneousCharges_inner(
                        sub_order_number = '', 
                        charge_line_reference = '', 
                        charge_description = '', 
                        charge_amount = 1.337, )
                    ],
                links = [
                    xi.sdk.resellers.models.order_create_response_orders_inner_links_inner.OrderCreateResponse_orders_inner_links_inner(
                        topic = '', 
                        href = '', 
                        type = '', )
                    ],
                rejected_line_items = [
                    xi.sdk.resellers.models.order_create_response_orders_inner_rejected_line_items_inner.OrderCreateResponse_orders_inner_rejectedLineItems_inner(
                        customer_linenumber = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        quantity_ordered = 56, 
                        reject_code = '', 
                        reject_reason = '', )
                    ],
                additional_attributes = [
                    xi.sdk.resellers.models.order_create_response_orders_inner_additional_attributes_inner.OrderCreateResponse_orders_inner_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ]
            )
        else:
            return OrderCreateResponseOrdersInner(
        )
        """

    def testOrderCreateResponseOrdersInner(self):
        """Test OrderCreateResponseOrdersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
