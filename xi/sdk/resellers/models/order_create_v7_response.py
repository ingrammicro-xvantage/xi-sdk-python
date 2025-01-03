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
from xi.sdk.resellers.models.order_create_v7_response_resource import OrderCreateV7ResponseResource
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateV7Response(BaseModel):
    """
    OrderCreateV7Response
    """ # noqa: E501
    topic: Optional[StrictStr] = Field(default=None, description="Field for identifying whether it is a reseller or vendor event. For eg, resellers/orders")
    event: Optional[StrictStr] = Field(default=None, description="The event sent in the request. For eg, im::create.")
    event_time_stamp: Optional[StrictStr] = Field(default=None, description="The timestamp at which the event was sent.", alias="eventTimeStamp")
    event_id: Optional[StrictStr] = Field(default=None, description="A unique id used as identifier for the sepcific event and used for generating the x-hub signature.", alias="eventId")
    event_type: Optional[StrictStr] = Field(default=None, description="The event name sent in the event request.", alias="eventType")
    resource: Optional[OrderCreateV7ResponseResource] = None
    __properties: ClassVar[List[str]] = ["topic", "event", "eventTimeStamp", "eventId", "eventType", "resource"]

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
        """Create an instance of OrderCreateV7Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of resource
        if self.resource:
            _dict['resource'] = self.resource.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderCreateV7Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "topic": obj.get("topic"),
            "event": obj.get("event"),
            "eventTimeStamp": obj.get("eventTimeStamp"),
            "eventId": obj.get("eventId"),
            "eventType": obj.get("eventType"),
            "resource": OrderCreateV7ResponseResource.from_dict(obj["resource"]) if obj.get("resource") is not None else None
        })
        return _obj


