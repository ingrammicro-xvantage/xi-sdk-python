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

class QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser(BaseModel):
    """
    QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser
    """ # noqa: E501
    end_user_name: Optional[StrictStr] = Field(default=None, alias="endUserName")
    end_user_address: Optional[StrictStr] = Field(default=None, alias="endUserAddress")
    end_user_address2: Optional[StrictStr] = Field(default=None, alias="endUserAddress2")
    end_user_address3: Optional[StrictStr] = Field(default=None, alias="endUserAddress3")
    end_user_city: Optional[StrictStr] = Field(default=None, alias="endUserCity")
    end_user_state: Optional[StrictStr] = Field(default=None, alias="endUserState")
    end_user_email: Optional[StrictStr] = Field(default=None, alias="endUserEmail")
    end_user_phone: Optional[StrictStr] = Field(default=None, alias="endUserPhone")
    end_user_zip_code: Optional[StrictStr] = Field(default=None, alias="endUserZipCode")
    end_user_contact_name: Optional[StrictStr] = Field(default=None, alias="endUserContactName")
    end_user_market_segment: Optional[StrictStr] = Field(default=None, alias="endUserMarketSegment")
    __properties: ClassVar[List[str]] = ["endUserName", "endUserAddress", "endUserAddress2", "endUserAddress3", "endUserCity", "endUserState", "endUserEmail", "endUserPhone", "endUserZipCode", "endUserContactName", "endUserMarketSegment"]

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
        """Create an instance of QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser from a JSON string"""
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
        """Create an instance of QuoteDetailsQuoteDetailResponseRetrieveQuoteResponseEndUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endUserName": obj.get("endUserName"),
            "endUserAddress": obj.get("endUserAddress"),
            "endUserAddress2": obj.get("endUserAddress2"),
            "endUserAddress3": obj.get("endUserAddress3"),
            "endUserCity": obj.get("endUserCity"),
            "endUserState": obj.get("endUserState"),
            "endUserEmail": obj.get("endUserEmail"),
            "endUserPhone": obj.get("endUserPhone"),
            "endUserZipCode": obj.get("endUserZipCode"),
            "endUserContactName": obj.get("endUserContactName"),
            "endUserMarketSegment": obj.get("endUserMarketSegment")
        })
        return _obj


