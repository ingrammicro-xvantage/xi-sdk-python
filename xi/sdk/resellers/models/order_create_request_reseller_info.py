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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateRequestResellerInfo(BaseModel):
    """
    The address and contact information provided by the reseller.
    """ # noqa: E501
    reseller_id: Optional[StrictStr] = Field(default=None, description="The reseller's Id.", alias="resellerId")
    company_name: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, description="The reseller's company name.", alias="companyName")
    contact: Optional[StrictStr] = Field(default=None, description="The reseller's contact name.")
    address_line1: Optional[Annotated[str, Field(strict=True, max_length=70)]] = Field(default=None, description="The reseller's street address.", alias="addressLine1")
    address_line2: Optional[Annotated[str, Field(strict=True, max_length=70)]] = Field(default=None, description="The reseller's building or apartment number.", alias="addressLine2")
    address_line3: Optional[Annotated[str, Field(strict=True, max_length=70)]] = Field(default=None, description="The reseller's address line 3.", alias="addressLine3")
    city: Optional[Annotated[str, Field(strict=True, max_length=25)]] = Field(default=None, description="The reseller's city.")
    state: Optional[Annotated[str, Field(strict=True, max_length=3)]] = Field(default=None, description="The reseller's state.")
    postal_code: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="The reseller's zip or postal code.", alias="postalCode")
    country_code: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="The reseller's two-character ISO country code.", alias="countryCode")
    phone_number: Optional[StrictInt] = Field(default=None, description="The reseller's phone number.", alias="phoneNumber")
    email: Optional[StrictStr] = Field(default=None, description="The reseller's email address.")
    __properties: ClassVar[List[str]] = ["resellerId", "companyName", "contact", "addressLine1", "addressLine2", "addressLine3", "city", "state", "postalCode", "countryCode", "phoneNumber", "email"]

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
        """Create an instance of OrderCreateRequestResellerInfo from a JSON string"""
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
        """Create an instance of OrderCreateRequestResellerInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resellerId": obj.get("resellerId"),
            "companyName": obj.get("companyName"),
            "contact": obj.get("contact"),
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


