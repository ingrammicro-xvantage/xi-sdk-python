# coding: utf-8

"""
    Reseller API

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from xi.sdk.resellers.models.invoice_details import InvoiceDetails

class TestInvoiceDetails(unittest.TestCase):
    """InvoiceDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceDetails:
        """Test InvoiceDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceDetails`
        """
        model = InvoiceDetails()
        if include_optional:
            return InvoiceDetails(
                serviceresponse = xi.sdk.resellers.models.invoice_detail_response_serviceresponse.InvoiceDetailResponse_serviceresponse(
                    responsepreamble = xi.sdk.resellers.models.invoice_detail_response_serviceresponse_responsepreamble.InvoiceDetailResponse_serviceresponse_responsepreamble(
                        responsestatus = '', 
                        statuscode = '', 
                        responsemessage = '', ), 
                    invoicedetailresponse = xi.sdk.resellers.models.invoice_detail_response_serviceresponse_invoicedetailresponse.InvoiceDetailResponse_serviceresponse_invoicedetailresponse(
                        customernumber = '', 
                        invoicenumber = '', 
                        invoicedate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        invoicetype = '', 
                        customerordernumber = '', 
                        customerfreightamount = '', 
                        customerforeignfrightamt = '', 
                        totaltaxamount = '', 
                        totalamount = '', 
                        shiptosuffix = '', 
                        billtosuffix = '', 
                        freightamount = '', 
                        paymentterms = '', 
                        orderdate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        carrier = '', 
                        carrierdescription = '', 
                        discountamount = 1.337, 
                        taxtype = '', 
                        enduserponumber = '', 
                        freightforwardercode = '', 
                        creditmemoreasoncode = '', 
                        fulfillmentflag = '', 
                        holdreason = '', 
                        shipcomplete = '', 
                        shipdate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        companycurrency = '', 
                        currencycode = '', 
                        currencyrate = '', 
                        globalorderid = '', 
                        originalshipcode = '', 
                        ordertype = '', 
                        orderstatus = '', 
                        totalotherfees = 1.337, 
                        totalsales = '', 
                        weight = '', 
                        shippableswitch = '', 
                        soldto = xi.sdk.resellers.models.invoice_details/address_type/response.invoiceDetails.addressType.Response(
                            attention = '', 
                            name1 = '', 
                            name2 = '', 
                            addressline1 = '', 
                            addressline2 = '', 
                            addressline3 = '', 
                            city = '', 
                            state = '', 
                            postalcode = '', 
                            countrycode = '', 
                            fax = '', 
                            phonenumber = '', 
                            email = '', ), 
                        billto = xi.sdk.resellers.models.invoice_details/address_type/response.invoiceDetails.addressType.Response(
                            attention = '', 
                            name1 = '', 
                            name2 = '', 
                            addressline1 = '', 
                            addressline2 = '', 
                            addressline3 = '', 
                            city = '', 
                            state = '', 
                            postalcode = '', 
                            countrycode = '', 
                            fax = '', 
                            phonenumber = '', 
                            email = '', ), 
                        shoptoaddress = , 
                        lines = [
                            xi.sdk.resellers.models.invoice_details/product_line_type/response.invoiceDetails.productLineType.Response(
                                linenumber = '', 
                                linetype = '', 
                                partnumber = '', 
                                vendorpartnumber = '', 
                                partdescription = '', 
                                shipfrombranch = '', 
                                shippedquantity = '', 
                                orderedquantity = '', 
                                marginpercent = '', 
                                backorderquantity = '', 
                                backorderetadate = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                                extendedprice = '', 
                                specialbidnumber = '', 
                                ordersuffix = '', 
                                isacopapplied = '', 
                                unitprice = '', 
                                unitofmeasure = '', 
                                serialnumberdetails = [
                                    xi.sdk.resellers.models.product_line_type_serialnumberdetails_inner.productLineType_serialnumberdetails_inner(
                                        serialnumber = '', 
                                        deliverynumber = '', )
                                    ], 
                                trackingnumberdetails = [
                                    xi.sdk.resellers.models.product_line_type_trackingnumberdetails_inner.productLineType_trackingnumberdetails_inner(
                                        trackingnumber = '', )
                                    ], 
                                productextendedspecs = [
                                    xi.sdk.resellers.models.invoice_detail_response_serviceresponse_invoicedetailresponse_extendedspecs_inner.InvoiceDetailResponse_serviceresponse_invoicedetailresponse_extendedspecs_inner(
                                        attributename = '', 
                                        attributevalue = '', )
                                    ], )
                            ], 
                        extendedspecs = [
                            xi.sdk.resellers.models.invoice_detail_response_serviceresponse_invoicedetailresponse_extendedspecs_inner.InvoiceDetailResponse_serviceresponse_invoicedetailresponse_extendedspecs_inner(
                                attributename = '', 
                                attributevalue = '', )
                            ], 
                        miscfeeline = [
                            xi.sdk.resellers.models.invoice_detail_response_serviceresponse_invoicedetailresponse_miscfeeline_inner.InvoiceDetailResponse_serviceresponse_invoicedetailresponse_miscfeeline_inner(
                                code = '', 
                                description = '', 
                                chargeamount = '', )
                            ], ), )
            )
        else:
            return InvoiceDetails(
        )
        """

    def testInvoiceDetails(self):
        """Test InvoiceDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()