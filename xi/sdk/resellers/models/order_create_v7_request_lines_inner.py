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
from typing_extensions import Annotated
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_additional_attributes_inner import OrderCreateV7RequestLinesInnerAdditionalAttributesInner
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_end_user_info_inner import OrderCreateV7RequestLinesInnerEndUserInfoInner
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_vmf_additional_attributes_lines_inner import OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner
from xi.sdk.resellers.models.order_create_v7_request_lines_inner_warranty_info_inner import OrderCreateV7RequestLinesInnerWarrantyInfoInner
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateV7RequestLinesInner(BaseModel):
    """
    OrderCreateV7RequestLinesInner
    """ # noqa: E501
    customer_line_number: Optional[Annotated[str, Field(strict=True, max_length=3)]] = Field(default=None, description="The reseller's line item number for reference in their system. The customer line number needs to be a unique numeric value between 1 and 884. In the event we receive duplicate values or alphanumeric values in the customer line number, we will re-sequence the customer line number. To prevent re-sequencing, please use a unique numeric value between 1 and 884 in the customer line number.", alias="customerLineNumber")
    ingram_part_number: Optional[Annotated[str, Field(strict=True, max_length=18)]] = Field(default=None, description="The unique IngramMicro part number.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="The vendor's part number for the line item.", alias="vendorPartNumber")
    quantity: Optional[StrictInt] = Field(default=None, description="The requested quantity of the line item.")
    unit_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The reseller-requested unit price for the line item. The unit price is not guaranteed.", alias="unitPrice")
    special_bid_number: Optional[Annotated[str, Field(strict=True, max_length=36)]] = Field(default=None, description="The line-level bid number provided to the reseller by the vendor for special pricing and discounts. Used to track the bid number in the case of split orders or where different line items have different bid numbers. Line-level bid number take precedence over header-level bid numbers.", alias="specialBidNumber")
    end_user_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The end-user price. Required for Export Orders.", alias="endUserPrice")
    notes: Optional[StrictStr] = Field(default=None, description="The attribute field data.")
    end_user_info: Optional[List[OrderCreateV7RequestLinesInnerEndUserInfoInner]] = Field(default=None, alias="endUserInfo")
    additional_attributes: Optional[List[OrderCreateV7RequestLinesInnerAdditionalAttributesInner]] = Field(default=None, alias="additionalAttributes")
    warranty_info: Optional[List[OrderCreateV7RequestLinesInnerWarrantyInfoInner]] = Field(default=None, alias="warrantyInfo")
    vmf_additional_attributes_lines: Optional[List[OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner]] = Field(default=None, alias="vmfAdditionalAttributesLines")
    __properties: ClassVar[List[str]] = ["customerLineNumber", "ingramPartNumber", "vendorPartNumber", "quantity", "unitPrice", "specialBidNumber", "endUserPrice", "notes", "endUserInfo", "additionalAttributes", "warrantyInfo", "vmfAdditionalAttributesLines"]

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
        """Create an instance of OrderCreateV7RequestLinesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in end_user_info (list)
        _items = []
        if self.end_user_info:
            for _item_end_user_info in self.end_user_info:
                if _item_end_user_info:
                    _items.append(_item_end_user_info.to_dict())
            _dict['endUserInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item_additional_attributes in self.additional_attributes:
                if _item_additional_attributes:
                    _items.append(_item_additional_attributes.to_dict())
            _dict['additionalAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warranty_info (list)
        _items = []
        if self.warranty_info:
            for _item_warranty_info in self.warranty_info:
                if _item_warranty_info:
                    _items.append(_item_warranty_info.to_dict())
            _dict['warrantyInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vmf_additional_attributes_lines (list)
        _items = []
        if self.vmf_additional_attributes_lines:
            for _item_vmf_additional_attributes_lines in self.vmf_additional_attributes_lines:
                if _item_vmf_additional_attributes_lines:
                    _items.append(_item_vmf_additional_attributes_lines.to_dict())
            _dict['vmfAdditionalAttributesLines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderCreateV7RequestLinesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customerLineNumber": obj.get("customerLineNumber"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "quantity": obj.get("quantity"),
            "unitPrice": obj.get("unitPrice"),
            "specialBidNumber": obj.get("specialBidNumber"),
            "endUserPrice": obj.get("endUserPrice"),
            "notes": obj.get("notes"),
            "endUserInfo": [OrderCreateV7RequestLinesInnerEndUserInfoInner.from_dict(_item) for _item in obj["endUserInfo"]] if obj.get("endUserInfo") is not None else None,
            "additionalAttributes": [OrderCreateV7RequestLinesInnerAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None,
            "warrantyInfo": [OrderCreateV7RequestLinesInnerWarrantyInfoInner.from_dict(_item) for _item in obj["warrantyInfo"]] if obj.get("warrantyInfo") is not None else None,
            "vmfAdditionalAttributesLines": [OrderCreateV7RequestLinesInnerVmfAdditionalAttributesLinesInner.from_dict(_item) for _item in obj["vmfAdditionalAttributesLines"]] if obj.get("vmfAdditionalAttributesLines") is not None else None
        })
        return _obj


