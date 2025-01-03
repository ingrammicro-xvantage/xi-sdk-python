# coding: utf-8

"""
    XI Sdk Resellers

    For Resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.price_and_availability_response_inner_discounts_inner_quantity_discounts_inner import PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner
from xi.sdk.resellers.models.price_and_availability_response_inner_discounts_inner_special_pricing_inner import PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner
from typing import Optional, Set
from typing_extensions import Self

class PriceAndAvailabilityResponseInnerDiscountsInner(BaseModel):
    """
    PriceAndAvailabilityResponseInnerDiscountsInner
    """ # noqa: E501
    special_pricing: Optional[List[PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner]] = Field(default=None, alias="specialPricing")
    quantity_discounts: Optional[List[PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner]] = Field(default=None, alias="quantityDiscounts")
    __properties: ClassVar[List[str]] = ["specialPricing", "quantityDiscounts"]

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
        """Create an instance of PriceAndAvailabilityResponseInnerDiscountsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in special_pricing (list)
        _items = []
        if self.special_pricing:
            for _item_special_pricing in self.special_pricing:
                if _item_special_pricing:
                    _items.append(_item_special_pricing.to_dict())
            _dict['specialPricing'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in quantity_discounts (list)
        _items = []
        if self.quantity_discounts:
            for _item_quantity_discounts in self.quantity_discounts:
                if _item_quantity_discounts:
                    _items.append(_item_quantity_discounts.to_dict())
            _dict['quantityDiscounts'] = _items
        # set to None if quantity_discounts (nullable) is None
        # and model_fields_set contains the field
        if self.quantity_discounts is None and "quantity_discounts" in self.model_fields_set:
            _dict['quantityDiscounts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceAndAvailabilityResponseInnerDiscountsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "specialPricing": [PriceAndAvailabilityResponseInnerDiscountsInnerSpecialPricingInner.from_dict(_item) for _item in obj["specialPricing"]] if obj.get("specialPricing") is not None else None,
            "quantityDiscounts": [PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner.from_dict(_item) for _item in obj["quantityDiscounts"]] if obj.get("quantityDiscounts") is not None else None
        })
        return _obj


