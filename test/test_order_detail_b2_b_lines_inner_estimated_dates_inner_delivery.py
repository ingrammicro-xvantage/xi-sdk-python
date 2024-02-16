# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_delivery import OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery

class TestOrderDetailB2BLinesInnerEstimatedDatesInnerDelivery(unittest.TestCase):
    """OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery:
        """Test OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery`
        """
        model = OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery()
        if include_optional:
            return OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery(
                delivery_date_type = '',
                delivery_date_range = xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_delivery_delivery_date_range.OrderDetailB2B_lines_inner_estimatedDates_inner_delivery_deliveryDateRange(
                    start_date = '', 
                    end_date = '', ),
                delivery_source = '',
                delivery_description = '',
                delivered_date = ''
            )
        else:
            return OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery(
        )
        """

    def testOrderDetailB2BLinesInnerEstimatedDatesInnerDelivery(self):
        """Test OrderDetailB2BLinesInnerEstimatedDatesInnerDelivery"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
