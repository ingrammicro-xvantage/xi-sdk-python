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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_special_pricing_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner_discounts_inner_volume_discounts_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner
from typing import Optional, Set
from typing_extensions import Self

class PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner(BaseModel):
    """
    PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner
    """ # noqa: E501
    volume_discounts: Optional[List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner]] = Field(default=None, alias="volumeDiscounts")
    special_pricing: Optional[List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner]] = Field(default=None, alias="specialPricing")
    __properties: ClassVar[List[str]] = ["volumeDiscounts", "specialPricing"]

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
        """Create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in volume_discounts (list)
        _items = []
        if self.volume_discounts:
            for _item_volume_discounts in self.volume_discounts:
                if _item_volume_discounts:
                    _items.append(_item_volume_discounts.to_dict())
            _dict['volumeDiscounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in special_pricing (list)
        _items = []
        if self.special_pricing:
            for _item_special_pricing in self.special_pricing:
                if _item_special_pricing:
                    _items.append(_item_special_pricing.to_dict())
            _dict['specialPricing'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "volumeDiscounts": [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerVolumeDiscountsInner.from_dict(_item) for _item in obj["volumeDiscounts"]] if obj.get("volumeDiscounts") is not None else None,
            "specialPricing": [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInnerDiscountsInnerSpecialPricingInner.from_dict(_item) for _item in obj["specialPricing"]] if obj.get("specialPricing") is not None else None
        })
        return _obj


