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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from xi.sdk.resellers.models.async_order_create_dto_additional_attributes_inner import AsyncOrderCreateDTOAdditionalAttributesInner
from xi.sdk.resellers.models.async_order_create_dto_end_user_info import AsyncOrderCreateDTOEndUserInfo
from xi.sdk.resellers.models.async_order_create_dto_lines_inner import AsyncOrderCreateDTOLinesInner
from xi.sdk.resellers.models.async_order_create_dto_reseller_info import AsyncOrderCreateDTOResellerInfo
from xi.sdk.resellers.models.async_order_create_dto_ship_to_info import AsyncOrderCreateDTOShipToInfo
from xi.sdk.resellers.models.async_order_create_dto_shipment_details import AsyncOrderCreateDTOShipmentDetails
from xi.sdk.resellers.models.async_order_create_dto_vmfadditional_attributes_inner import AsyncOrderCreateDTOVmfadditionalAttributesInner
from xi.sdk.resellers.models.async_order_create_dto_warranty_info_inner import AsyncOrderCreateDTOWarrantyInfoInner
from typing import Optional, Set
from typing_extensions import Self

class AsyncOrderCreateDTO(BaseModel):
    """
    AsyncOrderCreateDTO
    """ # noqa: E501
    quote_number: Optional[Annotated[str, Field(strict=True, max_length=35)]] = Field(default=None, description="A unique identifier generated by Ingram Micro's CRM specific to each quote.", alias="quoteNumber")
    customer_order_number: Optional[Annotated[str, Field(strict=True, max_length=35)]] = Field(default=None, description="The reseller's order number for reference in their system.", alias="customerOrderNumber")
    end_customer_order_number: Optional[Annotated[str, Field(strict=True, max_length=35)]] = Field(default=None, description="The end customer's order number for reference in their system.", alias="endCustomerOrderNumber")
    notes: Optional[StrictStr] = Field(default=None, description="Order header level notes.")
    bill_to_address_id: Optional[StrictStr] = Field(default=None, description="Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit.", alias="billToAddressId")
    special_bid_number: Optional[StrictStr] = Field(default=None, description="The bid number is provided to the reseller by the vendor for special pricing and discounts. Line-level bid numbers take precedence over header-level bid numbers.", alias="specialBidNumber")
    internal_comments: Optional[StrictStr] = Field(default=None, description="need to replace with actual description", alias="internalComments")
    accept_back_order: Optional[StrictBool] = Field(default=None, description="ENUM [\"true\",\"false\"] - accept order if this item is backordered. This field along with shipComplete field decides the value of backorderflag. The value of this field is ignored when shipComplete field is present.", alias="acceptBackOrder")
    vend_auth_number: Optional[StrictStr] = Field(default=None, description="Authorization number provided by vendor to Ingram's reseller. Orders will be placed on hold without this value, vendor specific mandatory field - please reach out Ingram Sales team for list of vendor for whom this is mandatory.", alias="vendAuthNumber")
    reseller_info: Optional[AsyncOrderCreateDTOResellerInfo] = Field(default=None, alias="resellerInfo")
    end_user_info: Optional[AsyncOrderCreateDTOEndUserInfo] = Field(default=None, alias="endUserInfo")
    ship_to_info: Optional[AsyncOrderCreateDTOShipToInfo] = Field(default=None, alias="shipToInfo")
    shipment_details: Optional[AsyncOrderCreateDTOShipmentDetails] = Field(default=None, alias="shipmentDetails")
    additional_attributes: Optional[List[AsyncOrderCreateDTOAdditionalAttributesInner]] = Field(default=None, description="Additional order create attributes.", alias="additionalAttributes")
    vmfadditional_attributes: Optional[List[AsyncOrderCreateDTOVmfadditionalAttributesInner]] = Field(default=None, description="The object containing the list of fields required at a header level by the vendor.", alias="vmfadditionalAttributes")
    lines: Optional[List[AsyncOrderCreateDTOLinesInner]] = Field(default=None, description="The object containing the lines that require vendor mandatory fields.")
    warranty_info: Optional[List[AsyncOrderCreateDTOWarrantyInfoInner]] = Field(default=None, description="Warranty Information", alias="warrantyInfo")
    __properties: ClassVar[List[str]] = ["quoteNumber", "customerOrderNumber", "endCustomerOrderNumber", "notes", "billToAddressId", "specialBidNumber", "internalComments", "acceptBackOrder", "vendAuthNumber", "resellerInfo", "endUserInfo", "shipToInfo", "shipmentDetails", "additionalAttributes", "vmfadditionalAttributes", "lines", "warrantyInfo"]

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
        """Create an instance of AsyncOrderCreateDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reseller_info
        if self.reseller_info:
            _dict['resellerInfo'] = self.reseller_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_user_info
        if self.end_user_info:
            _dict['endUserInfo'] = self.end_user_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to_info
        if self.ship_to_info:
            _dict['shipToInfo'] = self.ship_to_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipment_details
        if self.shipment_details:
            _dict['shipmentDetails'] = self.shipment_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item in self.additional_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vmfadditional_attributes (list)
        _items = []
        if self.vmfadditional_attributes:
            for _item in self.vmfadditional_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vmfadditionalAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warranty_info (list)
        _items = []
        if self.warranty_info:
            for _item in self.warranty_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['warrantyInfo'] = _items
        # set to None if quote_number (nullable) is None
        # and model_fields_set contains the field
        if self.quote_number is None and "quote_number" in self.model_fields_set:
            _dict['quoteNumber'] = None

        # set to None if customer_order_number (nullable) is None
        # and model_fields_set contains the field
        if self.customer_order_number is None and "customer_order_number" in self.model_fields_set:
            _dict['customerOrderNumber'] = None

        # set to None if end_customer_order_number (nullable) is None
        # and model_fields_set contains the field
        if self.end_customer_order_number is None and "end_customer_order_number" in self.model_fields_set:
            _dict['endCustomerOrderNumber'] = None

        # set to None if bill_to_address_id (nullable) is None
        # and model_fields_set contains the field
        if self.bill_to_address_id is None and "bill_to_address_id" in self.model_fields_set:
            _dict['billToAddressId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AsyncOrderCreateDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quoteNumber": obj.get("quoteNumber"),
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "endCustomerOrderNumber": obj.get("endCustomerOrderNumber"),
            "notes": obj.get("notes"),
            "billToAddressId": obj.get("billToAddressId"),
            "specialBidNumber": obj.get("specialBidNumber"),
            "internalComments": obj.get("internalComments"),
            "acceptBackOrder": obj.get("acceptBackOrder"),
            "vendAuthNumber": obj.get("vendAuthNumber"),
            "resellerInfo": AsyncOrderCreateDTOResellerInfo.from_dict(obj["resellerInfo"]) if obj.get("resellerInfo") is not None else None,
            "endUserInfo": AsyncOrderCreateDTOEndUserInfo.from_dict(obj["endUserInfo"]) if obj.get("endUserInfo") is not None else None,
            "shipToInfo": AsyncOrderCreateDTOShipToInfo.from_dict(obj["shipToInfo"]) if obj.get("shipToInfo") is not None else None,
            "shipmentDetails": AsyncOrderCreateDTOShipmentDetails.from_dict(obj["shipmentDetails"]) if obj.get("shipmentDetails") is not None else None,
            "additionalAttributes": [AsyncOrderCreateDTOAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None,
            "vmfadditionalAttributes": [AsyncOrderCreateDTOVmfadditionalAttributesInner.from_dict(_item) for _item in obj["vmfadditionalAttributes"]] if obj.get("vmfadditionalAttributes") is not None else None,
            "lines": [AsyncOrderCreateDTOLinesInner.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "warrantyInfo": [AsyncOrderCreateDTOWarrantyInfoInner.from_dict(_item) for _item in obj["warrantyInfo"]] if obj.get("warrantyInfo") is not None else None
        })
        return _obj


