# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_create_v7_request_shipment_details import OrderCreateV7RequestShipmentDetails

class TestOrderCreateV7RequestShipmentDetails(unittest.TestCase):
    """OrderCreateV7RequestShipmentDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderCreateV7RequestShipmentDetails:
        """Test OrderCreateV7RequestShipmentDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderCreateV7RequestShipmentDetails`
        """
        model = OrderCreateV7RequestShipmentDetails()
        if include_optional:
            return OrderCreateV7RequestShipmentDetails(
                carrier_code = '',
                requested_delivery_date = '',
                ship_complete = '',
                shipping_instructions = '',
                freight_account_number = '',
                signature_required = True
            )
        else:
            return OrderCreateV7RequestShipmentDetails(
        )
        """

    def testOrderCreateV7RequestShipmentDetails(self):
        """Test OrderCreateV7RequestShipmentDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
