# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from xi.sdk.resellers.models.product_detail_response import ProductDetailResponse

class TestProductDetailResponse(unittest.TestCase):
    """ProductDetailResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductDetailResponse:
        """Test ProductDetailResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductDetailResponse`
        """
        model = ProductDetailResponse()
        if include_optional:
            return ProductDetailResponse(
                ingram_part_number = '',
                vendor_part_number = '',
                customer_part_number = '',
                product_authorized = '',
                description = '',
                product_detail_description = '',
                upc = '',
                product_category = '',
                product_subcategory = '',
                vendor_name = '',
                vendor_number = '',
                product_status_code = '',
                product_class = '',
                indicators = xi.sdk.resellers.models.product_detail_response_indicators.ProductDetailResponse_indicators(
                    has_warranty = True, 
                    is_new_product = True, 
                    has_return_limits = True, 
                    is_back_order_allowed = True, 
                    is_shipped_from_partner = True, 
                    is_replacement_product = True, 
                    is_directship = True, 
                    is_downloadable = True, 
                    is_digital_type = True, 
                    sku_type = '', 
                    has_std_special_price = True, 
                    has_acop_special_price = True, 
                    has_acop_quantity_break = True, 
                    has_std_web_discount = True, 
                    has_special_bid = True, 
                    is_exportable_to_country = True, 
                    is_discontinued_product = True, 
                    is_refurbished_product = True, 
                    is_returnable_product = True, 
                    is_ingram_ship = True, 
                    is_enduser_required = True, 
                    is_heavy_weight = True, 
                    has_ltl = True, 
                    is_clearance_product = True, 
                    has_bundle = True, 
                    is_oversize_product = True, 
                    is_preorder_product = True, 
                    is_license_product = True, 
                    is_directship_orderable = True, 
                    is_service_sku = True, 
                    is_configurable = True, ),
                cisco_fields = xi.sdk.resellers.models.product_detail_response_cisco_fields.ProductDetailResponse_ciscoFields(
                    product_sub_group = '', 
                    service_program_name = '', 
                    item_catalog_category = '', 
                    configuration_indicator = '', 
                    internal_business_entity = '', 
                    item_type = '', 
                    global_list_price = '', ),
                technical_specifications = [
                    xi.sdk.resellers.models.product_detail_response_technical_specifications_inner.ProductDetailResponse_technicalSpecifications_inner(
                        headername = '', 
                        attributevalue = '', 
                        attributedisplay = '', 
                        attributename = '', )
                    ],
                warranty_information = [
                    None
                    ],
                additional_information = xi.sdk.resellers.models.product_detail_response_additional_information.ProductDetailResponse_additionalInformation(
                    product_weight = [
                        xi.sdk.resellers.models.product_detail_response_additional_information_product_weight_inner.ProductDetailResponse_additionalInformation_productWeight_inner(
                            plant_id = '', 
                            weight = 1.337, 
                            weight_unit = '', )
                        ], 
                    is_bulk_freight = True, 
                    height = '', 
                    width = '', 
                    length = '', 
                    net_weight = '', 
                    dimension_unit = '', )
            )
        else:
            return ProductDetailResponse(
        )
        """

    def testProductDetailResponse(self):
        """Test ProductDetailResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
