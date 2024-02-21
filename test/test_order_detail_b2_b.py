# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b import OrderDetailB2B

class TestOrderDetailB2B(unittest.TestCase):
    """OrderDetailB2B unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2B:
        """Test OrderDetailB2B
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2B`
        """
        model = OrderDetailB2B()
        if include_optional:
            return OrderDetailB2B(
                ingram_order_number = '',
                ingram_order_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                order_type = '',
                customer_order_number = '',
                end_customer_order_number = '',
                web_order_id = '',
                vendor_sales_order_number = '',
                ingram_purchase_order_number = '',
                order_status = '',
                order_total = 1.337,
                order_sub_total = 1.337,
                freight_charges = 1.337,
                currency_code = '',
                total_weight = 1.337,
                total_tax = 1.337,
                total_fees = 1.337,
                payment_terms = '',
                notes = '',
                bill_to_info = xi.sdk.resellers.models.order_detail_b2_b_bill_to_info.OrderDetailB2B_billToInfo(
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
                ship_to_info = xi.sdk.resellers.models.order_detail_b2_b_ship_to_info.OrderDetailB2B_shipToInfo(
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
                end_user_info = xi.sdk.resellers.models.order_detail_b2_b_end_user_info.OrderDetailB2B_endUserInfo(
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
                    xi.sdk.resellers.models.order_detail_b2_b_lines_inner.OrderDetailB2B_lines_inner(
                        sub_order_number = '', 
                        ingram_order_line_number = '', 
                        vendor_sales_order_line_number = '', 
                        customer_line_number = '', 
                        line_status = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        vendor_name = '', 
                        part_description = '', 
                        unit_weight = 1.337, 
                        weight_uom = '', 
                        unit_price = 1.337, 
                        upc_code = '', 
                        extended_price = 1.337, 
                        tax_amount = 1.337, 
                        currency_code = '', 
                        quantity_ordered = 56, 
                        quantity_confirmed = 56, 
                        quantity_back_ordered = 56, 
                        special_bid_number = '', 
                        requested_deliverydate = '', 
                        promised_delivery_date = '', 
                        back_order_eta_date = '', 
                        line_notes = '', 
                        shipment_details = [
                            xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner.OrderDetailB2B_lines_inner_shipmentDetails_inner(
                                quantity = 56, 
                                delivery_number = '', 
                                estimated_ship_date = '', 
                                shipped_date = '', 
                                estimated_delivery_date = '', 
                                ship_from_warehouse_id = '', 
                                ship_from_location = '', 
                                invoice_number = '', 
                                invoice_date = '', 
                                carrier_details = [
                                    xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner.OrderDetailB2B_lines_inner_shipmentDetails_inner_carrierDetails_inner(
                                        carrier_code = '', 
                                        carrier_name = '', 
                                        quantity = 56, 
                                        shipped_date = '', 
                                        estimated_delivery_date = '', 
                                        delivered_date = '', 
                                        carrier_pickup_date = '', 
                                        tracking_details = [
                                            xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner.OrderDetailB2B_lines_inner_shipmentDetails_inner_carrierDetails_inner_trackingDetails_inner(
                                                tracking_number = '', 
                                                tracking_url = '', 
                                                package_weight = '', 
                                                carton_number = '', 
                                                quantity_in_box = '', 
                                                serial_numbers = [
                                                    xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner_serial_numbers_inner.OrderDetailB2B_lines_inner_shipmentDetails_inner_carrierDetails_inner_trackingDetails_inner_serialNumbers_inner(
                                                        serial_number = '', )
                                                    ], )
                                            ], )
                                    ], )
                            ], 
                        service_contract_info = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info.OrderDetailB2B_lines_inner_serviceContractInfo(
                            contract_info = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_contract_info.OrderDetailB2B_lines_inner_serviceContractInfo_contractInfo(
                                contract_description = '', 
                                contract_number = '', 
                                contract_status = '', 
                                contract_start_date = '', 
                                contract_end_date = '', 
                                contract_duration = '', ), 
                            subscriptions = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_subscriptions.OrderDetailB2B_lines_inner_serviceContractInfo_subscriptions(
                                subscription_id = '', 
                                subscription_term = '', 
                                renewal_term = '', 
                                billing_model = '', 
                                subcription_start_date = '', 
                                subcription_end_date = '', ), 
                            license_info = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_service_contract_info_license_info.OrderDetailB2B_lines_inner_serviceContractInfo_licenseInfo(
                                license_number = [
                                    ''
                                    ], 
                                license_start_date = '', 
                                license_end_date = '', 
                                description = '', 
                                quantity = '', ), ), 
                        additional_attributes = [
                            xi.sdk.resellers.models.order_detail_b2_b_lines_inner_additional_attributes_inner.OrderDetailB2B_lines_inner_additionalAttributes_inner(
                                attribute_name = '', 
                                attribute_value = '', )
                            ], 
                        links = [
                            xi.sdk.resellers.models.order_detail_b2_b_lines_inner_links_inner.OrderDetailB2B_lines_inner_links_inner(
                                topic = '', 
                                href = '', 
                                type = '', )
                            ], 
                        estimated_dates = [
                            xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner.OrderDetailB2B_lines_inner_estimatedDates_inner(
                                ship = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship.OrderDetailB2B_lines_inner_estimatedDates_inner_ship(
                                    ship_date_type = '', 
                                    ship_date_range = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship_ship_date_range.OrderDetailB2B_lines_inner_estimatedDates_inner_ship_shipDateRange(
                                        start_date = '', 
                                        end_date = '', ), 
                                    ship_source = '', 
                                    ship_description = '', 
                                    ship_date = '', ), 
                                delivery = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_delivery.OrderDetailB2B_lines_inner_estimatedDates_inner_delivery(
                                    delivery_date_type = '', 
                                    delivery_date_range = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_delivery_delivery_date_range.OrderDetailB2B_lines_inner_estimatedDates_inner_delivery_deliveryDateRange(
                                        start_date = '', 
                                        end_date = '', ), 
                                    delivery_source = '', 
                                    delivery_description = '', 
                                    delivered_date = '', ), )
                            ], 
                        schedule_lines = [
                            xi.sdk.resellers.models.order_detail_b2_b_lines_inner_schedule_lines_inner.OrderDetailB2B_lines_inner_scheduleLines_inner(
                                line_number = '', 
                                schedule_line_date = '', 
                                requested_quantity = '', 
                                confirmed_quantity = '', 
                                goods_issue_date = '', )
                            ], 
                        multiple_shipments = [
                            xi.sdk.resellers.models.order_detail_b2_b_lines_inner_multiple_shipments_inner.OrderDetailB2B_lines_inner_multipleShipments_inner(
                                line_number = '', 
                                requested_quantity = '', 
                                confirmed_quantity = '', 
                                data_type = '', 
                                date_range = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship_ship_date_range.OrderDetailB2B_lines_inner_estimatedDates_inner_ship_shipDateRange(
                                    start_date = '', 
                                    end_date = '', ), 
                                source = '', 
                                description = '', 
                                date = '', 
                                delivery_date = '', )
                            ], )
                    ],
                miscellaneous_charges = [
                    xi.sdk.resellers.models.order_detail_b2_b_miscellaneous_charges_inner.OrderDetailB2B_miscellaneousCharges_inner(
                        sub_order_number = '', 
                        charge_line_reference = '', 
                        charge_description = '', 
                        charge_amount = '', )
                    ],
                additional_attributes = [
                    xi.sdk.resellers.models.order_detail_b2_b_additional_attributes_inner.OrderDetailB2B_additionalAttributes_inner(
                        attribute_name = '', 
                        attribute_value = '', )
                    ]
            )
        else:
            return OrderDetailB2B(
        )
        """

    def testOrderDetailB2B(self):
        """Test OrderDetailB2B"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
