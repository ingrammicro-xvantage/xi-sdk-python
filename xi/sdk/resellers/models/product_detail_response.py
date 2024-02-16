# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.product_detail_response_additional_information import ProductDetailResponseAdditionalInformation
from xi.sdk.resellers.models.product_detail_response_cisco_fields import ProductDetailResponseCiscoFields
from xi.sdk.resellers.models.product_detail_response_indicators import ProductDetailResponseIndicators
from xi.sdk.resellers.models.product_detail_response_technical_specifications_inner import ProductDetailResponseTechnicalSpecificationsInner
from typing import Optional, Set
from typing_extensions import Self

class ProductDetailResponse(BaseModel):
    """
    ProductDetailResponse
    """ # noqa: E501
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="Ingram Micro unique part number for the product.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="Vendor’s part number for the product.", alias="vendorPartNumber")
    customer_part_number: Optional[StrictStr] = Field(default=None, description="Reseller / end-user’s part number for the product.", alias="customerPartNumber")
    product_authorized: Optional[StrictStr] = Field(default=None, description="Boolean that indicates whether a product is authorized.", alias="productAuthorized")
    description: Optional[StrictStr] = Field(default=None, description="The description given for the product.")
    product_detail_description: Optional[StrictStr] = Field(default=None, description="The detailed description given for the product.", alias="productDetailDescription")
    upc: Optional[StrictStr] = Field(default=None, description="The UPC code for the product. Consists of 12 numeric digits that are uniquely assigned to each trade item.")
    product_category: Optional[StrictStr] = Field(default=None, description="The category of the product.", alias="productCategory")
    product_subcategory: Optional[StrictStr] = Field(default=None, description="The sub-category of the product.", alias="productSubcategory")
    vendor_name: Optional[StrictStr] = Field(default=None, description="Vendor name for the order.", alias="vendorName")
    vendor_number: Optional[StrictStr] = Field(default=None, description="Vendor number that identifies the product.", alias="vendorNumber")
    product_status_code: Optional[StrictStr] = Field(default=None, description="Status code of the product.", alias="productStatusCode")
    product_class: Optional[StrictStr] = Field(default=None, description="Indicates whether the product is directly shipped from the vendor’s warehouse or if the product ships from Ingram Micro’s warehouse. Class Codes are Ingram classifications on how skus are stocked A = Product that is stocked usually in all IM warehouses and replenished on a regular basis. B = Product that is stocked in limited IM warehouses and replenished on a regular basis C = Product that is stocked in fewer IM warehouses and replenished on a regular basis. D = Product that Ingram Micro has elected to discontinue. E = Product that will be phased out later, according to the vendor. You may not want to replenish this product, but instead sell down what is in stock. F = Product that we carry for a specific customer or supplier under a contractual agreement. N = New Sku. Classification before first receipt O = Discontinued product to be liquidated S= Order for Specialized Demand (Order to backorder) X= direct ship from Vendor V = product that vendor has elected to discontinue.", alias="productClass")
    indicators: Optional[ProductDetailResponseIndicators] = None
    cisco_fields: Optional[ProductDetailResponseCiscoFields] = Field(default=None, alias="ciscoFields")
    technical_specifications: Optional[List[ProductDetailResponseTechnicalSpecificationsInner]] = Field(default=None, description="Technical specifications of the product.", alias="technicalSpecifications")
    warranty_information: Optional[List[Dict[str, Any]]] = Field(default=None, description="Warranty information related to the product.", alias="warrantyInformation")
    additional_information: Optional[ProductDetailResponseAdditionalInformation] = Field(default=None, alias="additionalInformation")
    __properties: ClassVar[List[str]] = ["ingramPartNumber", "vendorPartNumber", "customerPartNumber", "productAuthorized", "description", "productDetailDescription", "upc", "productCategory", "productSubcategory", "vendorName", "vendorNumber", "productStatusCode", "productClass", "indicators", "ciscoFields", "technicalSpecifications", "warrantyInformation", "additionalInformation"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ProductDetailResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of indicators
        if self.indicators:
            _dict['indicators'] = self.indicators.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cisco_fields
        if self.cisco_fields:
            _dict['ciscoFields'] = self.cisco_fields.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in technical_specifications (list)
        _items = []
        if self.technical_specifications:
            for _item in self.technical_specifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['technicalSpecifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of additional_information
        if self.additional_information:
            _dict['additionalInformation'] = self.additional_information.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductDetailResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "customerPartNumber": obj.get("customerPartNumber"),
            "productAuthorized": obj.get("productAuthorized"),
            "description": obj.get("description"),
            "productDetailDescription": obj.get("productDetailDescription"),
            "upc": obj.get("upc"),
            "productCategory": obj.get("productCategory"),
            "productSubcategory": obj.get("productSubcategory"),
            "vendorName": obj.get("vendorName"),
            "vendorNumber": obj.get("vendorNumber"),
            "productStatusCode": obj.get("productStatusCode"),
            "productClass": obj.get("productClass"),
            "indicators": ProductDetailResponseIndicators.from_dict(obj["indicators"]) if obj.get("indicators") is not None else None,
            "ciscoFields": ProductDetailResponseCiscoFields.from_dict(obj["ciscoFields"]) if obj.get("ciscoFields") is not None else None,
            "technicalSpecifications": [ProductDetailResponseTechnicalSpecificationsInner.from_dict(_item) for _item in obj["technicalSpecifications"]] if obj.get("technicalSpecifications") is not None else None,
            "warrantyInformation": obj.get("warrantyInformation"),
            "additionalInformation": ProductDetailResponseAdditionalInformation.from_dict(obj["additionalInformation"]) if obj.get("additionalInformation") is not None else None
        })
        return _obj


