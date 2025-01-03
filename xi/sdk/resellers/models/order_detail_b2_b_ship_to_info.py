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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailB2BShipToInfo(BaseModel):
    """
    The shipping information provided by the reseller for order delivery.
    """ # noqa: E501
    contact: Optional[StrictStr] = Field(default=None, description="The company contact provided by the reseller.")
    company_name: Optional[StrictStr] = Field(default=None, description="The name of the company the order will be shipped to.", alias="companyName")
    address_line1: Optional[StrictStr] = Field(default=None, description="The address line 1 the order will be shipped to.", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="The address line 2 the order will be shipped to.", alias="addressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="The address line 3 the order will be shipped to.", alias="addressLine3")
    city: Optional[StrictStr] = Field(default=None, description="The city the order will be shipped to.")
    state: Optional[StrictStr] = Field(default=None, description="The state the order will be shipped to.")
    postal_code: Optional[StrictStr] = Field(default=None, description="The zip or postal code the order will be shipped to.", alias="postalCode")
    country_code: Optional[StrictStr] = Field(default=None, description="The two-character ISO country code the order will be shipped to.", alias="countryCode")
    phone_number: Optional[StrictStr] = Field(default=None, description="The company contact phone number.", alias="phoneNumber")
    email: Optional[StrictStr] = Field(default=None, description="The company contact email address.")
    __properties: ClassVar[List[str]] = ["contact", "companyName", "addressLine1", "addressLine2", "addressLine3", "city", "state", "postalCode", "countryCode", "phoneNumber", "email"]

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
        """Create an instance of OrderDetailB2BShipToInfo from a JSON string"""
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
        """Create an instance of OrderDetailB2BShipToInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact": obj.get("contact"),
            "companyName": obj.get("companyName"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postalCode": obj.get("postalCode"),
            "countryCode": obj.get("countryCode"),
            "phoneNumber": obj.get("phoneNumber"),
            "email": obj.get("email")
        })
        return _obj


