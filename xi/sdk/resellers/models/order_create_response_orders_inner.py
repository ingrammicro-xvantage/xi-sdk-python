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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.order_create_response_orders_inner_additional_attributes_inner import OrderCreateResponseOrdersInnerAdditionalAttributesInner
from xi.sdk.resellers.models.order_create_response_orders_inner_lines_inner import OrderCreateResponseOrdersInnerLinesInner
from xi.sdk.resellers.models.order_create_response_orders_inner_links_inner import OrderCreateResponseOrdersInnerLinksInner
from xi.sdk.resellers.models.order_create_response_orders_inner_miscellaneous_charges_inner import OrderCreateResponseOrdersInnerMiscellaneousChargesInner
from xi.sdk.resellers.models.order_create_response_orders_inner_rejected_line_items_inner import OrderCreateResponseOrdersInnerRejectedLineItemsInner
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateResponseOrdersInner(BaseModel):
    """
    OrderCreateResponseOrdersInner
    """ # noqa: E501
    number_of_lines_with_success: Optional[StrictInt] = Field(default=None, description="The number of lines in the order that were successful.", alias="numberOfLinesWithSuccess")
    number_of_lines_with_error: Optional[StrictInt] = Field(default=None, description="The number of lines in the order that have errors.", alias="numberOfLinesWithError")
    number_of_lines_with_warning: Optional[StrictInt] = Field(default=None, description="The number of lines in the order that have a warning.", alias="numberOfLinesWithWarning")
    ingram_order_number: Optional[StrictStr] = Field(default=None, description="The Ingram Micro order number.", alias="ingramOrderNumber")
    ingram_order_date: Optional[StrictStr] = Field(default=None, description="The date in UTC format that the order was created in Ingram Micro's system.", alias="ingramOrderDate")
    notes: Optional[StrictStr] = Field(default=None, description="Order-level notes.")
    order_type: Optional[StrictStr] = Field(default=None, description="The order typer. One of: S=Stocked PO D=Direct Ship PO", alias="orderType")
    order_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total price for the order.", alias="orderTotal")
    freight_charges: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total freight charges for the order.", alias="freightCharges")
    total_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total tax for the order.", alias="totalTax")
    currency_code: Optional[StrictStr] = Field(default=None, description="The country-specific three character ISO 4217 currency code used for the order.", alias="currencyCode")
    lines: Optional[List[OrderCreateResponseOrdersInnerLinesInner]] = Field(default=None, description="The line-level details for the order.")
    miscellaneous_charges: Optional[List[OrderCreateResponseOrdersInnerMiscellaneousChargesInner]] = Field(default=None, alias="miscellaneousCharges")
    links: Optional[List[OrderCreateResponseOrdersInnerLinksInner]] = Field(default=None, description="Link to Order Details for the order(s).")
    rejected_line_items: Optional[List[OrderCreateResponseOrdersInnerRejectedLineItemsInner]] = Field(default=None, description="A list of rejected line items.", alias="rejectedLineItems")
    additional_attributes: Optional[List[OrderCreateResponseOrdersInnerAdditionalAttributesInner]] = Field(default=None, alias="additionalAttributes")
    __properties: ClassVar[List[str]] = ["numberOfLinesWithSuccess", "numberOfLinesWithError", "numberOfLinesWithWarning", "ingramOrderNumber", "ingramOrderDate", "notes", "orderType", "orderTotal", "freightCharges", "totalTax", "currencyCode", "lines", "miscellaneousCharges", "links", "rejectedLineItems", "additionalAttributes"]

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
        """Create an instance of OrderCreateResponseOrdersInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item_lines in self.lines:
                if _item_lines:
                    _items.append(_item_lines.to_dict())
            _dict['lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in miscellaneous_charges (list)
        _items = []
        if self.miscellaneous_charges:
            for _item_miscellaneous_charges in self.miscellaneous_charges:
                if _item_miscellaneous_charges:
                    _items.append(_item_miscellaneous_charges.to_dict())
            _dict['miscellaneousCharges'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item_links in self.links:
                if _item_links:
                    _items.append(_item_links.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rejected_line_items (list)
        _items = []
        if self.rejected_line_items:
            for _item_rejected_line_items in self.rejected_line_items:
                if _item_rejected_line_items:
                    _items.append(_item_rejected_line_items.to_dict())
            _dict['rejectedLineItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item_additional_attributes in self.additional_attributes:
                if _item_additional_attributes:
                    _items.append(_item_additional_attributes.to_dict())
            _dict['additionalAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderCreateResponseOrdersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "numberOfLinesWithSuccess": obj.get("numberOfLinesWithSuccess"),
            "numberOfLinesWithError": obj.get("numberOfLinesWithError"),
            "numberOfLinesWithWarning": obj.get("numberOfLinesWithWarning"),
            "ingramOrderNumber": obj.get("ingramOrderNumber"),
            "ingramOrderDate": obj.get("ingramOrderDate"),
            "notes": obj.get("notes"),
            "orderType": obj.get("orderType"),
            "orderTotal": obj.get("orderTotal"),
            "freightCharges": obj.get("freightCharges"),
            "totalTax": obj.get("totalTax"),
            "currencyCode": obj.get("currencyCode"),
            "lines": [OrderCreateResponseOrdersInnerLinesInner.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "miscellaneousCharges": [OrderCreateResponseOrdersInnerMiscellaneousChargesInner.from_dict(_item) for _item in obj["miscellaneousCharges"]] if obj.get("miscellaneousCharges") is not None else None,
            "links": [OrderCreateResponseOrdersInnerLinksInner.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "rejectedLineItems": [OrderCreateResponseOrdersInnerRejectedLineItemsInner.from_dict(_item) for _item in obj["rejectedLineItems"]] if obj.get("rejectedLineItems") is not None else None,
            "additionalAttributes": [OrderCreateResponseOrdersInnerAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None
        })
        return _obj


