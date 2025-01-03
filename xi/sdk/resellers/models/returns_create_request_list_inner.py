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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.returns_create_request_list_inner_ship_from_info_inner import ReturnsCreateRequestListInnerShipFromInfoInner
from typing import Optional, Set
from typing_extensions import Self

class ReturnsCreateRequestListInner(BaseModel):
    """
    ReturnsCreateRequestListInner
    """ # noqa: E501
    invoice_number: StrictStr = Field(description="The Invoice number of the order.", alias="invoiceNumber")
    invoice_date: date = Field(description="Date of an Invoice.", alias="invoiceDate")
    customer_order_number: Optional[StrictStr] = Field(default=None, description="The reseller's order number for reference in their system.", alias="customerOrderNumber")
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="Unique line number from Ingram.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="Vendor Part Number.", alias="vendorPartNumber")
    serial_number: Optional[StrictStr] = Field(default=None, description="Serial number of the product.", alias="serialNumber")
    quantity: StrictInt = Field(description="Return quantity of the product.")
    primary_reason: StrictStr = Field(description="Primary reason to return the product.", alias="primaryReason")
    secondary_reason: StrictStr = Field(description="Secondary reason to return the product.", alias="secondaryReason")
    notes: Optional[StrictStr] = Field(default=None, description="Return notes.")
    reference_number: Optional[StrictStr] = Field(default=None, description="Reference number to return the product.", alias="referenceNumber")
    bill_to_address_id: Optional[StrictStr] = Field(default=None, description="Suffix used to identify billing address.", alias="billToAddressId")
    ship_from_info: List[ReturnsCreateRequestListInnerShipFromInfoInner] = Field(alias="shipFromInfo")
    number_of_boxes: StrictInt = Field(description="Number of boxes to return.", alias="numberOfBoxes")
    __properties: ClassVar[List[str]] = ["invoiceNumber", "invoiceDate", "customerOrderNumber", "ingramPartNumber", "vendorPartNumber", "serialNumber", "quantity", "primaryReason", "secondaryReason", "notes", "referenceNumber", "billToAddressId", "shipFromInfo", "numberOfBoxes"]

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
        """Create an instance of ReturnsCreateRequestListInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ship_from_info (list)
        _items = []
        if self.ship_from_info:
            for _item_ship_from_info in self.ship_from_info:
                if _item_ship_from_info:
                    _items.append(_item_ship_from_info.to_dict())
            _dict['shipFromInfo'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReturnsCreateRequestListInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "invoiceNumber": obj.get("invoiceNumber"),
            "invoiceDate": obj.get("invoiceDate"),
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "serialNumber": obj.get("serialNumber"),
            "quantity": obj.get("quantity"),
            "primaryReason": obj.get("primaryReason"),
            "secondaryReason": obj.get("secondaryReason"),
            "notes": obj.get("notes"),
            "referenceNumber": obj.get("referenceNumber"),
            "billToAddressId": obj.get("billToAddressId"),
            "shipFromInfo": [ReturnsCreateRequestListInnerShipFromInfoInner.from_dict(_item) for _item in obj["shipFromInfo"]] if obj.get("shipFromInfo") is not None else None,
            "numberOfBoxes": obj.get("numberOfBoxes")
        })
        return _obj


