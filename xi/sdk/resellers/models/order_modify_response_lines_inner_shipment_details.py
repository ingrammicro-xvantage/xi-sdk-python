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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrderModifyResponseLinesInnerShipmentDetails(BaseModel):
    """
    Shipping details for the order provided by the reseller.
    """ # noqa: E501
    carrier_code: Optional[StrictStr] = Field(default=None, description="The carrier code for the shipment containing the line item.", alias="carrierCode")
    carrier_name: Optional[StrictStr] = Field(default=None, description="The name of the carrier of the shipment containing the line item.", alias="carrierName")
    freight_account_number: Optional[StrictStr] = Field(default=None, description="The reseller's shipping account number with carrier. Used to bill the shipping carrier directly from the reseller's account with the carrier.", alias="freightAccountNumber")
    __properties: ClassVar[List[str]] = ["carrierCode", "carrierName", "freightAccountNumber"]

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
        """Create an instance of OrderModifyResponseLinesInnerShipmentDetails from a JSON string"""
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
        """Create an instance of OrderModifyResponseLinesInnerShipmentDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "carrierCode": obj.get("carrierCode"),
            "carrierName": obj.get("carrierName"),
            "freightAccountNumber": obj.get("freightAccountNumber")
        })
        return _obj


