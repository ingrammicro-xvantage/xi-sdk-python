# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship import OrderDetailB2BLinesInnerEstimatedDatesInnerShip

class TestOrderDetailB2BLinesInnerEstimatedDatesInnerShip(unittest.TestCase):
    """OrderDetailB2BLinesInnerEstimatedDatesInnerShip unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInnerEstimatedDatesInnerShip:
        """Test OrderDetailB2BLinesInnerEstimatedDatesInnerShip
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInnerEstimatedDatesInnerShip`
        """
        model = OrderDetailB2BLinesInnerEstimatedDatesInnerShip()
        if include_optional:
            return OrderDetailB2BLinesInnerEstimatedDatesInnerShip(
                ship_date_type = '',
                ship_date_range = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship_ship_date_range.OrderDetailB2B_lines_inner_estimatedDates_inner_ship_shipDateRange(
                    start_date = '', 
                    end_date = '', ),
                ship_source = '',
                ship_description = '',
                ship_date = ''
            )
        else:
            return OrderDetailB2BLinesInnerEstimatedDatesInnerShip(
        )
        """

    def testOrderDetailB2BLinesInnerEstimatedDatesInnerShip(self):
        """Test OrderDetailB2BLinesInnerEstimatedDatesInnerShip"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
