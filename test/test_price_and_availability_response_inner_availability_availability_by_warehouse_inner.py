# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.price_and_availability_response_inner_availability_availability_by_warehouse_inner import PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner

class TestPriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner(unittest.TestCase):
    """PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner:
        """Test PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner`
        """
        model = PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner()
        if include_optional:
            return PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner(
                location = '',
                warehouse_id = '',
                quantity_available = 56,
                quantity_backordered = 56,
                quantity_backordered_eta = '',
                quantity_on_order = 56,
                back_order_info = [
                    xi.sdk.resellers.models.price_and_availability_response_inner_availability_availability_by_warehouse_inner_back_order_info_inner.PriceAndAvailabilityResponse_inner_availability_availabilityByWarehouse_inner_backOrderInfo_inner(
                        quantity = 56, 
                        eta_date = '', )
                    ]
            )
        else:
            return PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner(
        )
        """

    def testPriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner(self):
        """Test PriceAndAvailabilityResponseInnerAvailabilityAvailabilityByWarehouseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
