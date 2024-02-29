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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_estimated_dates_inner_ship_ship_date_range import OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailB2BLinesInnerMultipleShipmentsInner(BaseModel):
    """
    OrderDetailB2BLinesInnerMultipleShipmentsInner
    """ # noqa: E501
    line_number: Optional[StrictStr] = Field(default=None, description="Line number.", alias="lineNumber")
    requested_quantity: Optional[StrictInt] = Field(default=None, description="Requested quantity.", alias="requestedQuantity")
    confirmed_quantity: Optional[StrictInt] = Field(default=None, description="Confirmed quantity.", alias="confirmedQuantity")
    date_type: Optional[StrictStr] = Field(default=None, description="Date type. Example Single or multiple dates.", alias="dateType")
    date_range: Optional[OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange] = Field(default=None, alias="dateRange")
    source: Optional[StrictStr] = Field(default=None, description="Source.")
    description: Optional[StrictStr] = Field(default=None, description="Description.")
    var_date: Optional[StrictStr] = Field(default=None, description="Date.", alias="date")
    delivery_date: Optional[StrictStr] = Field(default=None, description="Delivery date.", alias="deliveryDate")
    __properties: ClassVar[List[str]] = ["lineNumber", "requestedQuantity", "confirmedQuantity", "dateType", "dateRange", "source", "description", "date", "deliveryDate"]

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
        """Create an instance of OrderDetailB2BLinesInnerMultipleShipmentsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of date_range
        if self.date_range:
            _dict['dateRange'] = self.date_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderDetailB2BLinesInnerMultipleShipmentsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lineNumber": obj.get("lineNumber"),
            "requestedQuantity": obj.get("requestedQuantity"),
            "confirmedQuantity": obj.get("confirmedQuantity"),
            "dateType": obj.get("dateType"),
            "dateRange": OrderDetailB2BLinesInnerEstimatedDatesInnerShipShipDateRange.from_dict(obj["dateRange"]) if obj.get("dateRange") is not None else None,
            "source": obj.get("source"),
            "description": obj.get("description"),
            "date": obj.get("date"),
            "deliveryDate": obj.get("deliveryDate")
        })
        return _obj


