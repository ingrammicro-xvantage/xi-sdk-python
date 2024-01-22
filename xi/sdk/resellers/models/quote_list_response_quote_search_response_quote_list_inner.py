# coding: utf-8

"""
    Reseller API

    For Resellers. <br> Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class QuoteListResponseQuoteSearchResponseQuoteListInner(BaseModel):
    """
    QuoteListResponseQuoteSearchResponseQuoteListInner
    """ # noqa: E501
    quote_name: Optional[StrictStr] = Field(default=None, description="Quote Name given to quote by sales team or system generated. Generally used as a reference to identify the quote.", alias="quoteName")
    quote_number: Optional[StrictStr] = Field(default=None, description="Unique identifier generated by Ingram Micro's CRM specific to each quote. When applying a filter to the quoteNumber and including a partial quote number in the filter, all quotes containing any information included in the filter can be retrieved as a subset of all available customer quotes.", alias="quoteNumber")
    revision_number: Optional[StrictInt] = Field(default=None, description="When a quote has been revised and updated, the quote number remains the same throughout the lifecycle of the quote, however, a Revision number is updated for each revision of the quote. The revision numbers is associated with the Unique Quote Number.", alias="revisionNumber")
    end_user_name: Optional[StrictStr] = Field(default=None, description="End User Name is the end customer name that is associated with a quote in Ingram Micro's CRM", alias="endUserName")
    bid_number: Optional[StrictStr] = Field(default=None, description="Special Pricing Bid Number, also refers to as Dart Number relates to a unique pricing deal associated with a vendor for the quote.", alias="bidNumber")
    total_amount: Optional[StrictStr] = Field(default=None, description="Total amount of quoted price for all products in the quote.", alias="totalAmount")
    quote_status: Optional[StrictStr] = Field(default=None, description="This refers to the primary status of the quote. API responses will return: Active", alias="quoteStatus")
    created_date: Optional[date] = Field(default=None, description="Date the Quote was initially Created", alias="createdDate")
    last_modified_date: Optional[date] = Field(default=None, description="Date the Quote was last updated or modified.", alias="lastModifiedDate")
    quote_expiry_date: Optional[date] = Field(default=None, description="Date the Quote Expires", alias="quoteExpiryDate")
    __properties: ClassVar[List[str]] = ["quoteName", "quoteNumber", "revisionNumber", "endUserName", "bidNumber", "totalAmount", "quoteStatus", "createdDate", "lastModifiedDate", "quoteExpiryDate"]

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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QuoteListResponseQuoteSearchResponseQuoteListInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of QuoteListResponseQuoteSearchResponseQuoteListInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quoteName": obj.get("quoteName"),
            "quoteNumber": obj.get("quoteNumber"),
            "revisionNumber": obj.get("revisionNumber"),
            "endUserName": obj.get("endUserName"),
            "bidNumber": obj.get("bidNumber"),
            "totalAmount": obj.get("totalAmount"),
            "quoteStatus": obj.get("quoteStatus"),
            "createdDate": obj.get("createdDate"),
            "lastModifiedDate": obj.get("lastModifiedDate"),
            "quoteExpiryDate": obj.get("quoteExpiryDate")
        })
        return _obj

