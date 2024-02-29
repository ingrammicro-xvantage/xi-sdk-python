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
from xi.sdk.resellers.models.invoice_detailsv61_response_summary_foreign_fx_totals import InvoiceDetailsv61ResponseSummaryForeignFxTotals
from xi.sdk.resellers.models.invoice_detailsv61_response_summary_lines import InvoiceDetailsv61ResponseSummaryLines
from xi.sdk.resellers.models.invoice_detailsv61_response_summary_misc_charges_inner import InvoiceDetailsv61ResponseSummaryMiscChargesInner
from xi.sdk.resellers.models.invoice_detailsv61_response_summary_totals import InvoiceDetailsv61ResponseSummaryTotals
from typing import Optional, Set
from typing_extensions import Self

class InvoiceDetailsv61ResponseSummary(BaseModel):
    """
    InvoiceDetailsv61ResponseSummary
    """ # noqa: E501
    lines: Optional[InvoiceDetailsv61ResponseSummaryLines] = None
    misc_charges: Optional[List[InvoiceDetailsv61ResponseSummaryMiscChargesInner]] = Field(default=None, description="Miscellaneous charges.", alias="miscCharges")
    totals: Optional[InvoiceDetailsv61ResponseSummaryTotals] = None
    foreign_fx_totals: Optional[InvoiceDetailsv61ResponseSummaryForeignFxTotals] = Field(default=None, alias="foreignFxTotals")
    __properties: ClassVar[List[str]] = ["lines", "miscCharges", "totals", "foreignFxTotals"]

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
        """Create an instance of InvoiceDetailsv61ResponseSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of lines
        if self.lines:
            _dict['lines'] = self.lines.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in misc_charges (list)
        _items = []
        if self.misc_charges:
            for _item in self.misc_charges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['miscCharges'] = _items
        # override the default output from pydantic by calling `to_dict()` of totals
        if self.totals:
            _dict['totals'] = self.totals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of foreign_fx_totals
        if self.foreign_fx_totals:
            _dict['foreignFxTotals'] = self.foreign_fx_totals.to_dict()
        # set to None if misc_charges (nullable) is None
        # and model_fields_set contains the field
        if self.misc_charges is None and "misc_charges" in self.model_fields_set:
            _dict['miscCharges'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceDetailsv61ResponseSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lines": InvoiceDetailsv61ResponseSummaryLines.from_dict(obj["lines"]) if obj.get("lines") is not None else None,
            "miscCharges": [InvoiceDetailsv61ResponseSummaryMiscChargesInner.from_dict(_item) for _item in obj["miscCharges"]] if obj.get("miscCharges") is not None else None,
            "totals": InvoiceDetailsv61ResponseSummaryTotals.from_dict(obj["totals"]) if obj.get("totals") is not None else None,
            "foreignFxTotals": InvoiceDetailsv61ResponseSummaryForeignFxTotals.from_dict(obj["foreignFxTotals"]) if obj.get("foreignFxTotals") is not None else None
        })
        return _obj


