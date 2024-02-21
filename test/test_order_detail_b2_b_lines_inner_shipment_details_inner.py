# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner import OrderDetailB2BLinesInnerShipmentDetailsInner

class TestOrderDetailB2BLinesInnerShipmentDetailsInner(unittest.TestCase):
    """OrderDetailB2BLinesInnerShipmentDetailsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInnerShipmentDetailsInner:
        """Test OrderDetailB2BLinesInnerShipmentDetailsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInnerShipmentDetailsInner`
        """
        model = OrderDetailB2BLinesInnerShipmentDetailsInner()
        if include_optional:
            return OrderDetailB2BLinesInnerShipmentDetailsInner(
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
                    ]
            )
        else:
            return OrderDetailB2BLinesInnerShipmentDetailsInner(
        )
        """

    def testOrderDetailB2BLinesInnerShipmentDetailsInner(self):
        """Test OrderDetailB2BLinesInnerShipmentDetailsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
