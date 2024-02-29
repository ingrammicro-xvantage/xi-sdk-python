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
from xi.sdk.resellers.models.validate_quote_response_lines_inner import ValidateQuoteResponseLinesInner
from xi.sdk.resellers.models.validate_quote_response_vmf_additional_attributes_inner import ValidateQuoteResponseVmfAdditionalAttributesInner
from typing import Optional, Set
from typing_extensions import Self

class ValidateQuoteResponse(BaseModel):
    """
    ValidateQuoteResponse
    """ # noqa: E501
    quote_number: Optional[StrictStr] = Field(default=None, description="A unique identifier generated by Ingram Micro's CRM specific to each quote.", alias="quoteNumber")
    vendor_name: Optional[StrictStr] = Field(default=None, description="The name of the vendor.", alias="vendorName")
    vmf_additional_attributes: Optional[List[ValidateQuoteResponseVmfAdditionalAttributesInner]] = Field(default=None, description="The object containing the list of fields required at a header level by the vendor.", alias="vmfAdditionalAttributes")
    lines: Optional[List[ValidateQuoteResponseLinesInner]] = Field(default=None, description="The object containing the lines from the quote.")
    quote_type: Optional[StrictInt] = Field(default=None, alias="quoteType")
    vendor_group_name: Optional[StrictStr] = Field(default=None, alias="vendorGroupName")
    vendor_quote_number: Optional[StrictStr] = Field(default=None, alias="vendorQuoteNumber")
    vendor_master_number: Optional[StrictStr] = Field(default=None, alias="vendorMasterNumber")
    __properties: ClassVar[List[str]] = ["quoteNumber", "vendorName", "vmfAdditionalAttributes", "lines", "quoteType", "vendorGroupName", "vendorQuoteNumber", "vendorMasterNumber"]

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
        """Create an instance of ValidateQuoteResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in vmf_additional_attributes (list)
        _items = []
        if self.vmf_additional_attributes:
            for _item in self.vmf_additional_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vmfAdditionalAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidateQuoteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quoteNumber": obj.get("quoteNumber"),
            "vendorName": obj.get("vendorName"),
            "vmfAdditionalAttributes": [ValidateQuoteResponseVmfAdditionalAttributesInner.from_dict(_item) for _item in obj["vmfAdditionalAttributes"]] if obj.get("vmfAdditionalAttributes") is not None else None,
            "lines": [ValidateQuoteResponseLinesInner.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "quoteType": obj.get("quoteType"),
            "vendorGroupName": obj.get("vendorGroupName"),
            "vendorQuoteNumber": obj.get("vendorQuoteNumber"),
            "vendorMasterNumber": obj.get("vendorMasterNumber")
        })
        return _obj


