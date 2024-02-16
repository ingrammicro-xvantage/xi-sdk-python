# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.order_modify_response import OrderModifyResponse

class TestOrderModifyResponse(unittest.TestCase):
    """OrderModifyResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderModifyResponse:
        """Test OrderModifyResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderModifyResponse`
        """
        model = OrderModifyResponse()
        if include_optional:
            return OrderModifyResponse(
                serviceresponse = xi.sdk.resellers.models.order_modify_response_serviceresponse.orderModifyResponse_serviceresponse(
                    responsepreamble = xi.sdk.resellers.models.order_modify_response_serviceresponse_responsepreamble.orderModifyResponse_serviceresponse_responsepreamble(
                        responsestatus = '', 
                        responsemessage = '', ), 
                    ordermodifyresponse = xi.sdk.resellers.models.order_modify_response_serviceresponse_ordermodifyresponse.orderModifyResponse_serviceresponse_ordermodifyresponse(
                        responseflag = '', 
                        errortype = '', 
                        acktriggered = '', 
                        warncode = '', 
                        headerresponse = '', ), )
            )
        else:
            return OrderModifyResponse(
        )
        """

    def testOrderModifyResponse(self):
        """Test OrderModifyResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
