# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner(BaseModel):
    """
    PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner
    """ # noqa: E501
    discount_type: Optional[StrictStr] = Field(default=None, description="The type of discount being given to the customer.", alias="discountType")
    special_bid_numer: Optional[StrictStr] = Field(default=None, description="Pre-approved special pricing/bid number provided to the reseller by the vendor for special pricing and discounts. Used to track the bid number where different line items have different bid numbers. Line-level bid numbers take precedence over header-level bid numbers.", alias="specialBidNumer")
    special_pricing_discount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Special pricing discount amount given to the customer.", alias="specialPricingDiscount")
    special_pricing_effective_date: Optional[date] = Field(default=None, description="The effective date of the special pricing available to the customer.", alias="specialPricingEffectiveDate")
    special_pricing_expiration_date: Optional[date] = Field(default=None, description="The expiration date of the special pricing available to the customer.", alias="specialPricingExpirationDate")
    special_pricing_available_quantity: Optional[StrictInt] = Field(default=None, description="The available quantity of products with discounts.", alias="specialPricingAvailableQuantity")
    special_pricing_min_quantity: Optional[StrictInt] = Field(default=None, description="The minimum quantity of products that have to be purchased to ensure the discount is applied.", alias="specialPricingMinQuantity")
    government_discount_type: Optional[StrictStr] = Field(default=None, description="Type of Government Discount. *Currently, this discount is only available in the USA.", alias="governmentDiscountType")
    government_discounted_customer_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Government Discounted Customer Price. *Currently, this discount is only available in the USA.", alias="governmentDiscountedCustomerPrice")
    __properties: ClassVar[List[str]] = ["discountType", "specialBidNumer", "specialPricingDiscount", "specialPricingEffectiveDate", "specialPricingExpirationDate", "specialPricingAvailableQuantity", "specialPricingMinQuantity", "governmentDiscountType", "governmentDiscountedCustomerPrice"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "discountType": obj.get("discountType"),
            "specialBidNumer": obj.get("specialBidNumer"),
            "specialPricingDiscount": obj.get("specialPricingDiscount"),
            "specialPricingEffectiveDate": obj.get("specialPricingEffectiveDate"),
            "specialPricingExpirationDate": obj.get("specialPricingExpirationDate"),
            "specialPricingAvailableQuantity": obj.get("specialPricingAvailableQuantity"),
            "specialPricingMinQuantity": obj.get("specialPricingMinQuantity"),
            "governmentDiscountType": obj.get("governmentDiscountType"),
            "governmentDiscountedCustomerPrice": obj.get("governmentDiscountedCustomerPrice")
        })
        return _obj


