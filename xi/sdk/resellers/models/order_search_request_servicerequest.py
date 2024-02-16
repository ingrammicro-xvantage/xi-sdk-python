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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from xi.sdk.resellers.models.order_search_request_servicerequest_order_lookup_request import OrderSearchRequestServicerequestOrderLookupRequest
from xi.sdk.resellers.models.order_search_request_servicerequest_requestpreamble import OrderSearchRequestServicerequestRequestpreamble
from typing import Optional, Set
from typing_extensions import Self

class OrderSearchRequestServicerequest(BaseModel):
    """
    OrderSearchRequestServicerequest
    """ # noqa: E501
    requestpreamble: OrderSearchRequestServicerequestRequestpreamble
    order_lookup_request: Optional[OrderSearchRequestServicerequestOrderLookupRequest] = Field(default=None, alias="orderLookupRequest")
    __properties: ClassVar[List[str]] = ["requestpreamble", "orderLookupRequest"]

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
        """Create an instance of OrderSearchRequestServicerequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of requestpreamble
        if self.requestpreamble:
            _dict['requestpreamble'] = self.requestpreamble.to_dict()
        # override the default output from pydantic by calling `to_dict()` of order_lookup_request
        if self.order_lookup_request:
            _dict['orderLookupRequest'] = self.order_lookup_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderSearchRequestServicerequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "requestpreamble": OrderSearchRequestServicerequestRequestpreamble.from_dict(obj["requestpreamble"]) if obj.get("requestpreamble") is not None else None,
            "orderLookupRequest": OrderSearchRequestServicerequestOrderLookupRequest.from_dict(obj["orderLookupRequest"]) if obj.get("orderLookupRequest") is not None else None
        })
        return _obj


