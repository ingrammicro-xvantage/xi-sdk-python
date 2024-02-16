# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner import OrderDetailB2BLinesInnerEstimatedDatesInner

class TestOrderDetailB2BLinesInnerEstimatedDatesInner(unittest.TestCase):
    """OrderDetailB2BLinesInnerEstimatedDatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInnerEstimatedDatesInner:
        """Test OrderDetailB2BLinesInnerEstimatedDatesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInnerEstimatedDatesInner`
        """
        model = OrderDetailB2BLinesInnerEstimatedDatesInner()
        if include_optional:
            return OrderDetailB2BLinesInnerEstimatedDatesInner(
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
                    delivered_date = '', )
            )
        else:
            return OrderDetailB2BLinesInnerEstimatedDatesInner(
        )
        """

    def testOrderDetailB2BLinesInnerEstimatedDatesInner(self):
        """Test OrderDetailB2BLinesInnerEstimatedDatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
