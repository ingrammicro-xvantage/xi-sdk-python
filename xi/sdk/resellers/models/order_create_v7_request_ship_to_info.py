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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateV7RequestShipToInfo(BaseModel):
    """
    The shipping information provided by the reseller.
    """ # noqa: E501
    address_id: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="The ID references the resellers address in Ingram Micro's system for shipping. Provided to resellers during the onboarding process.", alias="addressId")
    contact: Optional[Annotated[str, Field(strict=True, max_length=70)]] = Field(default=None, description="The company contact provided by the reseller.")
    company_name: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, description="The reseller's company name or the End-User's Name", alias="companyName")
    address_line1: Optional[Annotated[str, Field(strict=True, max_length=70)]] = Field(default=None, description="The street address and building or house number the order will be shipped to.", alias="addressLine1")
    address_line2: Optional[Annotated[str, Field(strict=True, max_length=70)]] = Field(default=None, description="The apartment number the order will be shipped to.", alias="addressLine2")
    city: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="The city the order will be shipped to.")
    state: Optional[Annotated[str, Field(strict=True, max_length=3)]] = Field(default=None, description="The state the order will be shipped to.")
    postal_code: Optional[StrictStr] = Field(default=None, description="End User Name", alias="postalCode")
    country_code: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="The zip or postal code the order will be shipped to.", alias="countryCode")
    email: Optional[StrictStr] = Field(default=None, description="The company contact email address.")
    shipping_notes: Optional[StrictStr] = Field(default=None, alias="shippingNotes")
    phone_number: Optional[StrictStr] = Field(default=None, description="The company contact phone number.", alias="phoneNumber")
    __properties: ClassVar[List[str]] = ["addressId", "contact", "companyName", "addressLine1", "addressLine2", "city", "state", "postalCode", "countryCode", "email", "shippingNotes", "phoneNumber"]

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
        """Create an instance of OrderCreateV7RequestShipToInfo from a JSON string"""
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
        """Create an instance of OrderCreateV7RequestShipToInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addressId": obj.get("addressId"),
            "contact": obj.get("contact"),
            "companyName": obj.get("companyName"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "postalCode": obj.get("postalCode"),
            "countryCode": obj.get("countryCode"),
            "email": obj.get("email"),
            "shippingNotes": obj.get("shippingNotes"),
            "phoneNumber": obj.get("phoneNumber")
        })
        return _obj


