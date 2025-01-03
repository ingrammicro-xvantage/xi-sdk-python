# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_status_async_notification_request_resource_inner import OrderStatusAsyncNotificationRequestResourceInner

class TestOrderStatusAsyncNotificationRequestResourceInner(unittest.TestCase):
    """OrderStatusAsyncNotificationRequestResourceInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderStatusAsyncNotificationRequestResourceInner:
        """Test OrderStatusAsyncNotificationRequestResourceInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderStatusAsyncNotificationRequestResourceInner`
        """
        model = OrderStatusAsyncNotificationRequestResourceInner()
        if include_optional:
            return OrderStatusAsyncNotificationRequestResourceInner(
                event_type = '',
                order_number = '',
                customer_order_number = '',
                order_entry_time_stamp = '',
                lines = [
                    xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_lines_inner.OrderStatusAsyncNotificationRequest_resource_inner_lines_inner(
                        line_number = '', 
                        sub_order_number = '', 
                        line_status = '', 
                        ingram_part_number = '', 
                        vendor_part_number = '', 
                        requested_quantity = '', 
                        shipped_quantity = '', 
                        backordered_quantity = '', 
                        shipment_details = [
                            xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner.OrderStatusAsyncNotificationRequest_resource_inner_lines_inner_shipmentDetails_inner(
                                shipment_date = '', 
                                ship_from_warehouse_id = '', 
                                warehouse_name = '', 
                                carrier_code = '', 
                                carrier_name = '', 
                                package_details = [
                                    xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_lines_inner_shipment_details_inner_package_details_inner.OrderStatusAsyncNotificationRequest_resource_inner_lines_inner_shipmentDetails_inner_packageDetails_inner(
                                        carton_number = '', 
                                        quantity_inbox = '', 
                                        tracking_number = '', )
                                    ], )
                            ], 
                        serial_number_details = [
                            xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_lines_inner_serial_number_details_inner.OrderStatusAsyncNotificationRequest_resource_inner_lines_inner_serialNumberDetails_inner(
                                serial_number = '', )
                            ], )
                    ],
                links = [
                    xi.sdk.resellers.models.order_status_async_notification_request_resource_inner_links_inner.OrderStatusAsyncNotificationRequest_resource_inner_links_inner(
                        topic = '', 
                        href = '', 
                        type = '', )
                    ]
            )
        else:
            return OrderStatusAsyncNotificationRequestResourceInner(
        )
        """

    def testOrderStatusAsyncNotificationRequestResourceInner(self):
        """Test OrderStatusAsyncNotificationRequestResourceInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
