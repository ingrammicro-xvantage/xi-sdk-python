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

from datetime import date
from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateRequestShipmentDetails(BaseModel):
    """
    Shipping details for the order provided by the customer.
    """ # noqa: E501
    carrier_code: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="The code for the shipping carrier for the line item.", alias="carrierCode")
    freight_account_number: Optional[StrictStr] = Field(default=None, description="The reseller 's shipping account number with carrier. Used to bill the shipping carrier directly from the reseller's account with the carrier.", alias="freightAccountNumber")
    ship_complete: Optional[Annotated[str, Field(strict=True, max_length=1)]] = Field(default=None, description="Specifies whether the shipment will be shipped only when all products are fulfilled. The value of this field along with acceptBackOrder field decides the value of backorderflag. If this field is set, acceptBackOrder field is ignored. Possible values for this field are true, C, P, E.    With value as true or C, backorderflag will be set as C.    With value as P, or E, backorderflag will be set as P or E respectively.    C = Ship complete at distribution level.    P = ship complete at line level.    E = ship complete across all distributions. ", alias="shipComplete")
    requested_delivery_date: Optional[date] = Field(default=None, description="The reseller-requested delivery date in UTC format. Delivery date is not guaranteed.", alias="requestedDeliveryDate")
    signature_required: Optional[StrictBool] = Field(default=None, description="Specifies whether a signature is required for delivery. Default is False.", alias="signatureRequired")
    shipping_instructions: Optional[Annotated[str, Field(strict=True, max_length=132)]] = Field(default=None, alias="shippingInstructions")
    __properties: ClassVar[List[str]] = ["carrierCode", "freightAccountNumber", "shipComplete", "requestedDeliveryDate", "signatureRequired", "shippingInstructions"]

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
        """Create an instance of OrderCreateRequestShipmentDetails from a JSON string"""
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
        """Create an instance of OrderCreateRequestShipmentDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "carrierCode": obj.get("carrierCode"),
            "freightAccountNumber": obj.get("freightAccountNumber"),
            "shipComplete": obj.get("shipComplete"),
            "requestedDeliveryDate": obj.get("requestedDeliveryDate"),
            "signatureRequired": obj.get("signatureRequired"),
            "shippingInstructions": obj.get("shippingInstructions")
        })
        return _obj


