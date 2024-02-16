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

class OrderCreateResponseShipToInfo(BaseModel):
    """
    The shipping information provided by the reseller.
    """ # noqa: E501
    address_id: Optional[StrictStr] = Field(default=None, description="The ID references the resellers address in Ingram Micro's system for shipping. Provided to resellers during the onboarding process.", alias="addressId")
    contact: Optional[StrictStr] = Field(default=None, description="The company contact provided by the reseller.")
    company_name: Optional[StrictStr] = Field(default=None, description="The name of the company the order will be shipped to.", alias="companyName")
    name1: Optional[StrictStr] = Field(default=None, description="name1")
    name2: Optional[StrictStr] = Field(default=None, description="name2")
    address_line1: Optional[StrictStr] = Field(default=None, description="The street address and building or house number the order will be shipped to.", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="The apartment number the order will be shipped to.", alias="addressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="Line 3 of the address the order will be shipped to.", alias="addressLine3")
    address_line4: Optional[StrictStr] = Field(default=None, description="Street address4", alias="addressLine4")
    city: Optional[StrictStr] = Field(default=None, description="The city the order will be shipped to.")
    state: Optional[StrictStr] = Field(default=None, description="The state the order will be shipped to.")
    postal_code: Optional[StrictStr] = Field(default=None, description="The zip or postal code the order will be shipped to.", alias="postalCode")
    country_code: Optional[StrictStr] = Field(default=None, description="The two-character ISO country code the order will be shipped to.", alias="countryCode")
    phone_number: Optional[StrictStr] = Field(default=None, description="The company contact phone number.", alias="phoneNumber")
    email: Optional[StrictStr] = Field(default=None, description="The company contact email address.")
    __properties: ClassVar[List[str]] = ["addressId", "contact", "companyName", "name1", "name2", "addressLine1", "addressLine2", "addressLine3", "addressLine4", "city", "state", "postalCode", "countryCode", "phoneNumber", "email"]

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
        """Create an instance of OrderCreateResponseShipToInfo from a JSON string"""
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
        """Create an instance of OrderCreateResponseShipToInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addressId": obj.get("addressId"),
            "contact": obj.get("contact"),
            "companyName": obj.get("companyName"),
            "name1": obj.get("name1"),
            "name2": obj.get("name2"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "addressLine4": obj.get("addressLine4"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postalCode": obj.get("postalCode"),
            "countryCode": obj.get("countryCode"),
            "phoneNumber": obj.get("phoneNumber"),
            "email": obj.get("email")
        })
        return _obj


