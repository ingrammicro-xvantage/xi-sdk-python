# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.multi_sku_price_and_stock_request_servicerequest_priceandstockrequest_item import MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem

class TestMultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem(unittest.TestCase):
    """MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem:
        """Test MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem`
        """
        model = MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem()
        if include_optional:
            return MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem(
                index = 56,
                ingrampartnumber = '',
                vendorpartnumber = '',
                upc = '',
                customerpartnumber = '',
                warehouseidlist = ''
            )
        else:
            return MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem(
        )
        """

    def testMultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem(self):
        """Test MultiSKUPriceAndStockRequestServicerequestPriceandstockrequestItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
