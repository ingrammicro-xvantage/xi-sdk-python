# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse import MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse

class TestMultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse(unittest.TestCase):
    """MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse:
        """Test MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse`
        """
        model = MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse()
        if include_optional:
            return MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse(
                details = [
                    xi.sdk.resellers.models.multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner.multiSKUPriceAndStockResponse_serviceresponse_priceandstockresponse_details_inner(
                        itemstatus = '', 
                        statusmessage = '', 
                        ingrampartnumber = '', 
                        vendorpartnumber = '', 
                        globalskuid = '', 
                        customerprice = '', 
                        partdescription1 = '', 
                        partdescription2 = '', 
                        vendornumber = '', 
                        vendorname = '', 
                        cpucode = '', 
                        class = 'A-Stocked product in all IM warehouses', 
                        skustatus = '', 
                        mediacpu = '', 
                        categorysubcategory = '', 
                        retailprice = 1.337, 
                        newmedia = '', 
                        enduserrequired = 'Y-End user data required', 
                        backorderflag = 'Y- Can be backordered', 
                        skuauthorized = '', 
                        extendedvendorpartnumber = '', 
                        warehousedetails = [
                            xi.sdk.resellers.models.multi_sku_price_and_stock_response_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner.multiSKUPriceAndStockResponse_serviceresponse_priceandstockresponse_details_inner_warehousedetails_inner(
                                warehouseid = '10-Mira Loma CA', 
                                warehousedescription = '', 
                                availablequantity = 56, 
                                onorderquantity = 56, 
                                onholdquantity = '', 
                                etadate = '', )
                            ], )
                    ]
            )
        else:
            return MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse(
        )
        """

    def testMultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse(self):
        """Test MultiSKUPriceAndStockResponseServiceresponsePriceandstockresponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
