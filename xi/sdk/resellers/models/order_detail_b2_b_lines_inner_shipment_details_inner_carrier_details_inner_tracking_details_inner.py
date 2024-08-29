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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner_shipment_details_inner_carrier_details_inner_tracking_details_inner_serial_numbers_inner import OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInnerSerialNumbersInner
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner(BaseModel):
    """
    OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner
    """ # noqa: E501
    tracking_number: Optional[StrictStr] = Field(default=None, description="The tracking number for the shipment containing the line item.", alias="trackingNumber")
    tracking_url: Optional[StrictStr] = Field(default=None, description="The tracking URL for the shipment containing the line item.", alias="trackingUrl")
    package_weight: Optional[StrictStr] = Field(default=None, description="The weight of the package for the line item.", alias="packageWeight")
    carton_number: Optional[StrictStr] = Field(default=None, description="The shipment carton number that contains the line item.", alias="cartonNumber")
    quantity_in_box: Optional[StrictStr] = Field(default=None, description="The quantity of line items in the box.", alias="quantityInBox")
    serial_numbers: Optional[List[OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInnerSerialNumbersInner]] = Field(default=None, description="A list of serial numbers of the line items contained in the shipment.", alias="serialNumbers")
    __properties: ClassVar[List[str]] = ["trackingNumber", "trackingUrl", "packageWeight", "cartonNumber", "quantityInBox", "serialNumbers"]

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
        """Create an instance of OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in serial_numbers (list)
        _items = []
        if self.serial_numbers:
            for _item_serial_numbers in self.serial_numbers:
                if _item_serial_numbers:
                    _items.append(_item_serial_numbers.to_dict())
            _dict['serialNumbers'] = _items
        # set to None if serial_numbers (nullable) is None
        # and model_fields_set contains the field
        if self.serial_numbers is None and "serial_numbers" in self.model_fields_set:
            _dict['serialNumbers'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "trackingNumber": obj.get("trackingNumber"),
            "trackingUrl": obj.get("trackingUrl"),
            "packageWeight": obj.get("packageWeight"),
            "cartonNumber": obj.get("cartonNumber"),
            "quantityInBox": obj.get("quantityInBox"),
            "serialNumbers": [OrderDetailB2BLinesInnerShipmentDetailsInnerCarrierDetailsInnerTrackingDetailsInnerSerialNumbersInner.from_dict(_item) for _item in obj["serialNumbers"]] if obj.get("serialNumbers") is not None else None
        })
        return _obj


