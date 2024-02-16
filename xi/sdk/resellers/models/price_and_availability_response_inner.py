# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.price_and_availability_response_inner_availability import PriceAndAvailabilityResponseInnerAvailability
from xi.sdk.resellers.models.price_and_availability_response_inner_discounts_inner import PriceAndAvailabilityResponseInnerDiscountsInner
from xi.sdk.resellers.models.price_and_availability_response_inner_pricing import PriceAndAvailabilityResponseInnerPricing
from xi.sdk.resellers.models.price_and_availability_response_inner_reserve_inventory_details_inner import PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner
from xi.sdk.resellers.models.price_and_availability_response_inner_service_fees_inner import PriceAndAvailabilityResponseInnerServiceFeesInner
from typing import Optional, Set
from typing_extensions import Self

class PriceAndAvailabilityResponseInner(BaseModel):
    """
    PriceAndAvailabilityResponseInner
    """ # noqa: E501
    product_status_code: Optional[StrictStr] = Field(default=None, description="Codes signifying whether the sku is active or not.", alias="productStatusCode")
    product_status_message: Optional[StrictStr] = Field(default=None, description="Message returned saying whether sku is active.", alias="productStatusMessage")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="Ingram Micro unique part number for the product.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="Vendor’s part number for the product.", alias="vendorPartNumber")
    extended_vendor_part_number: Optional[StrictStr] = Field(default=None, description="Extended Vendor Part Number. *Currently, this feature is not available in these countries (Mexico, Turkey, New Zealand, Colombia, Chile, Brazil, Peru, Western Sahara).", alias="extendedVendorPartNumber")
    customer_part_number: Optional[StrictStr] = Field(default=None, description="Reseller / end-user’s part number for the product.", alias="customerPartNumber")
    upc: Optional[StrictStr] = Field(default=None, description="The UPC code for the product. Consists of 12 numeric digits that are uniquely assigned to each trade item.")
    part_number_type: Optional[StrictStr] = Field(default=None, description="Number type of the part.", alias="partNumberType")
    vendor_number: Optional[StrictStr] = Field(default=None, description="Vendor number that identifies the product.", alias="vendorNumber")
    vendor_name: Optional[StrictStr] = Field(default=None, description="Vendor name for the order.", alias="vendorName")
    description: Optional[StrictStr] = Field(default=None, description="The description given for the product.")
    product_class: Optional[StrictStr] = Field(default=None, description="Indicates whether the product is directly shipped from the vendor’s warehouse or if the product ships from Ingram Micro’s warehouse. Class Codes are Ingram classifications on how skus are stocked A = Product that is stocked usually in all IM warehouses and replenished on a regular basis. B = Product that is stocked in limited IM warehouses and replenished on a regular basis C = Product that is stocked in fewer IM warehouses and replenished on a regular basis. D = Product that Ingram Micro has elected to discontinue. E = Product that will be phased out later, according to the vendor. You may not want to replenish this product, but instead sell down what is in stock. F = Product that we carry for a specific customer or supplier under a contractual agreement. N = New Sku. Classification before first receipt O = Discontinued product to be liquidated S= Order for Specialized Demand (Order to backorder) X= direct ship from Vendor V = product that vendor has elected to discontinue.", alias="productClass")
    uom: Optional[StrictStr] = Field(default=None, description="The description given for the product.")
    product_status: Optional[StrictStr] = Field(default=None, description="Status that gives whether the product is Active.", alias="productStatus")
    accept_back_order: Optional[StrictBool] = Field(default=None, description="Boolean that indicates if the product accepts backorder.", alias="acceptBackOrder")
    product_authorized: Optional[StrictBool] = Field(default=None, description="Boolean that indicates whether a product is authorized.", alias="productAuthorized")
    returnable_product: Optional[StrictBool] = Field(default=None, description="Boolean that indicates if the product can be returned.", alias="returnableProduct")
    end_user_info_required: Optional[StrictBool] = Field(default=None, description="Boolean that indicates  if end user information is required.", alias="endUserInfoRequired")
    govt_special_price_available: Optional[StrictBool] = Field(default=None, description="Boolean that indicates if special pricing is available for the product.", alias="govtSpecialPriceAvailable")
    govt_program_type: Optional[StrictStr] = Field(default=None, description="Program type, “PA” for government orders, “ED” for education order.", alias="govtProgramType")
    govt_end_user_type: Optional[StrictStr] = Field(default=None, description="Type of end user of the program. F = Federal, S = State, E = Local, K = K-12 school, and H = Higher Education.", alias="govtEndUserType")
    availability: Optional[PriceAndAvailabilityResponseInnerAvailability] = None
    reserve_inventory_details: Optional[List[PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner]] = Field(default=None, alias="reserveInventoryDetails")
    pricing: Optional[PriceAndAvailabilityResponseInnerPricing] = None
    discounts: Optional[List[PriceAndAvailabilityResponseInnerDiscountsInner]] = None
    bundle_part_indicator: Optional[StrictBool] = Field(default=None, description="True of false value to indicate whether it’s bundle part. *Currently, this feature is not available in these countries (Mexico, Turkey, New Zealand, Colombia, Chile, Brazil, Peru, Western Sahara).", alias="bundlePartIndicator")
    service_fees: Optional[List[PriceAndAvailabilityResponseInnerServiceFeesInner]] = Field(default=None, description="*Currently, this feature is not available in these countries (Mexico, Turkey, New Zealand, Colombia, Chile, Brazil, Peru, Western Sahara).", alias="serviceFees")
    __properties: ClassVar[List[str]] = ["productStatusCode", "productStatusMessage", "ingramPartNumber", "vendorPartNumber", "extendedVendorPartNumber", "customerPartNumber", "upc", "partNumberType", "vendorNumber", "vendorName", "description", "productClass", "uom", "productStatus", "acceptBackOrder", "productAuthorized", "returnableProduct", "endUserInfoRequired", "govtSpecialPriceAvailable", "govtProgramType", "govtEndUserType", "availability", "reserveInventoryDetails", "pricing", "discounts", "bundlePartIndicator", "serviceFees"]

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
        """Create an instance of PriceAndAvailabilityResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of availability
        if self.availability:
            _dict['availability'] = self.availability.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reserve_inventory_details (list)
        _items = []
        if self.reserve_inventory_details:
            for _item in self.reserve_inventory_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['reserveInventoryDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of pricing
        if self.pricing:
            _dict['pricing'] = self.pricing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in discounts (list)
        _items = []
        if self.discounts:
            for _item in self.discounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['discounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in service_fees (list)
        _items = []
        if self.service_fees:
            for _item in self.service_fees:
                if _item:
                    _items.append(_item.to_dict())
            _dict['serviceFees'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceAndAvailabilityResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "productStatusCode": obj.get("productStatusCode"),
            "productStatusMessage": obj.get("productStatusMessage"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "extendedVendorPartNumber": obj.get("extendedVendorPartNumber"),
            "customerPartNumber": obj.get("customerPartNumber"),
            "upc": obj.get("upc"),
            "partNumberType": obj.get("partNumberType"),
            "vendorNumber": obj.get("vendorNumber"),
            "vendorName": obj.get("vendorName"),
            "description": obj.get("description"),
            "productClass": obj.get("productClass"),
            "uom": obj.get("uom"),
            "productStatus": obj.get("productStatus"),
            "acceptBackOrder": obj.get("acceptBackOrder"),
            "productAuthorized": obj.get("productAuthorized"),
            "returnableProduct": obj.get("returnableProduct"),
            "endUserInfoRequired": obj.get("endUserInfoRequired"),
            "govtSpecialPriceAvailable": obj.get("govtSpecialPriceAvailable"),
            "govtProgramType": obj.get("govtProgramType"),
            "govtEndUserType": obj.get("govtEndUserType"),
            "availability": PriceAndAvailabilityResponseInnerAvailability.from_dict(obj["availability"]) if obj.get("availability") is not None else None,
            "reserveInventoryDetails": [PriceAndAvailabilityResponseInnerReserveInventoryDetailsInner.from_dict(_item) for _item in obj["reserveInventoryDetails"]] if obj.get("reserveInventoryDetails") is not None else None,
            "pricing": PriceAndAvailabilityResponseInnerPricing.from_dict(obj["pricing"]) if obj.get("pricing") is not None else None,
            "discounts": [PriceAndAvailabilityResponseInnerDiscountsInner.from_dict(_item) for _item in obj["discounts"]] if obj.get("discounts") is not None else None,
            "bundlePartIndicator": obj.get("bundlePartIndicator"),
            "serviceFees": [PriceAndAvailabilityResponseInnerServiceFeesInner.from_dict(_item) for _item in obj["serviceFees"]] if obj.get("serviceFees") is not None else None
        })
        return _obj


