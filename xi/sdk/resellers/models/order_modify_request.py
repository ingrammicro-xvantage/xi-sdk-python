# coding: utf-8

"""
    XI Sdk Resellers

    For Ingram Micro Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from xi.sdk.resellers.models.order_modify_request_additional_attributes_inner import OrderModifyRequestAdditionalAttributesInner
from xi.sdk.resellers.models.order_modify_request_lines_inner import OrderModifyRequestLinesInner
from xi.sdk.resellers.models.order_modify_request_ship_to_info import OrderModifyRequestShipToInfo
from typing import Optional, Set
from typing_extensions import Self

class OrderModifyRequest(BaseModel):
    """
    OrderModifyRequest
    """ # noqa: E501
    notes: Optional[Annotated[str, Field(strict=True, max_length=132)]] = Field(default=None, description="Shipment-level notes.")
    ship_to_info: Optional[OrderModifyRequestShipToInfo] = Field(default=None, alias="shipToInfo")
    lines: Optional[List[OrderModifyRequestLinesInner]] = Field(default=None, description="The order line items.")
    additional_attributes: Optional[List[OrderModifyRequestAdditionalAttributesInner]] = Field(default=None, description="Header-level additional attributes.", alias="additionalAttributes")
    __properties: ClassVar[List[str]] = ["notes", "shipToInfo", "lines", "additionalAttributes"]

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
        """Create an instance of OrderModifyRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ship_to_info
        if self.ship_to_info:
            _dict['shipToInfo'] = self.ship_to_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item in self.additional_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderModifyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "notes": obj.get("notes"),
            "shipToInfo": OrderModifyRequestShipToInfo.from_dict(obj["shipToInfo"]) if obj.get("shipToInfo") is not None else None,
            "lines": [OrderModifyRequestLinesInner.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "additionalAttributes": [OrderModifyRequestAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None
        })
        return _obj


