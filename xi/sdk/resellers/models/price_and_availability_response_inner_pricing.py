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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class PriceAndAvailabilityResponseInnerPricing(BaseModel):
    """
    PriceAndAvailabilityResponseInnerPricing
    """ # noqa: E501
    currency_code: Optional[StrictStr] = Field(default=None, description="The 3-digit ISO currency code.", alias="currencyCode")
    retail_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The retail price of the product.", alias="retailPrice")
    map_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Minimum Advertised Price (MAP). If required by the vendor, resellers can not sell below MAP price.", alias="mapPrice")
    customer_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The price customer pays after all special pricing and discounts have been applied.", alias="customerPrice")
    special_bid_pricing_available: Optional[StrictBool] = Field(default=None, description="Boolean values specifies whether special Bid discounts are available for the product.", alias="specialBidPricingAvailable")
    web_discounts_available: Optional[StrictBool] = Field(default=None, description="Boolean values specifies whether web Discounts are available for the product.", alias="webDiscountsAvailable")
    __properties: ClassVar[List[str]] = ["currencyCode", "retailPrice", "mapPrice", "customerPrice", "specialBidPricingAvailable", "webDiscountsAvailable"]

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
        """Create an instance of PriceAndAvailabilityResponseInnerPricing from a JSON string"""
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
        """Create an instance of PriceAndAvailabilityResponseInnerPricing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currencyCode": obj.get("currencyCode"),
            "retailPrice": obj.get("retailPrice"),
            "mapPrice": obj.get("mapPrice"),
            "customerPrice": obj.get("customerPrice"),
            "specialBidPricingAvailable": obj.get("specialBidPricingAvailable"),
            "webDiscountsAvailable": obj.get("webDiscountsAvailable")
        })
        return _obj


