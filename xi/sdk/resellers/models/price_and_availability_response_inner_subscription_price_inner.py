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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_billing_period import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerBillingPeriod
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_groups_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerGroupsInner
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_options_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner
from xi.sdk.resellers.models.price_and_availability_response_inner_subscription_price_inner_subscription_period_inner import PriceAndAvailabilityResponseInnerSubscriptionPriceInnerSubscriptionPeriodInner
from typing import Optional, Set
from typing_extensions import Self

class PriceAndAvailabilityResponseInnerSubscriptionPriceInner(BaseModel):
    """
    PriceAndAvailabilityResponseInnerSubscriptionPriceInner
    """ # noqa: E501
    index: Optional[Union[StrictFloat, StrictInt]] = None
    plan_id: Optional[StrictStr] = Field(default=None, description="Id of the plan.", alias="planId")
    plan_uid: Optional[StrictStr] = Field(default=None, alias="planUId")
    plan_name: Optional[StrictStr] = Field(default=None, description="Name of the plan.", alias="planName")
    plan_description: Optional[StrictStr] = Field(default=None, description="The description of the plan.", alias="planDescription")
    groups: Optional[List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerGroupsInner]] = None
    billing_period: Optional[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerBillingPeriod] = Field(default=None, alias="billingPeriod")
    subscription_period: Optional[List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerSubscriptionPeriodInner]] = Field(default=None, alias="subscriptionPeriod")
    options: Optional[List[PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner]] = None
    __properties: ClassVar[List[str]] = ["index", "planId", "planUId", "planName", "planDescription", "groups", "billingPeriod", "subscriptionPeriod", "options"]

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
        """Create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of billing_period
        if self.billing_period:
            _dict['billingPeriod'] = self.billing_period.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subscription_period (list)
        _items = []
        if self.subscription_period:
            for _item_subscription_period in self.subscription_period:
                if _item_subscription_period:
                    _items.append(_item_subscription_period.to_dict())
            _dict['subscriptionPeriod'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item_options in self.options:
                if _item_options:
                    _items.append(_item_options.to_dict())
            _dict['options'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceAndAvailabilityResponseInnerSubscriptionPriceInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "index": obj.get("index"),
            "planId": obj.get("planId"),
            "planUId": obj.get("planUId"),
            "planName": obj.get("planName"),
            "planDescription": obj.get("planDescription"),
            "groups": [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerGroupsInner.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "billingPeriod": PriceAndAvailabilityResponseInnerSubscriptionPriceInnerBillingPeriod.from_dict(obj["billingPeriod"]) if obj.get("billingPeriod") is not None else None,
            "subscriptionPeriod": [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerSubscriptionPeriodInner.from_dict(_item) for _item in obj["subscriptionPeriod"]] if obj.get("subscriptionPeriod") is not None else None,
            "options": [PriceAndAvailabilityResponseInnerSubscriptionPriceInnerOptionsInner.from_dict(_item) for _item in obj["options"]] if obj.get("options") is not None else None
        })
        return _obj


