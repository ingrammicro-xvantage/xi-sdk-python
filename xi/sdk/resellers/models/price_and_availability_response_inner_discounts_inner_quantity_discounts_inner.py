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
from typing import Optional, Set
from typing_extensions import Self

class PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner(BaseModel):
    """
    PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner
    """ # noqa: E501
    condition_type: Optional[StrictStr] = Field(default=None, description="Indicates when the discount is applied after ordering the product.", alias="conditionType")
    currency_code: Optional[StrictStr] = Field(default=None, description="The country-specific three digit ISO 4217 currency code for the order.", alias="currencyCode")
    currency_type: Optional[StrictStr] = Field(default=None, description="Type of currency.", alias="currencyType")
    quantity: Optional[StrictInt] = Field(default=None, description="The total discounted quantity of the product.")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total price of all the discounts applied.")
    __properties: ClassVar[List[str]] = ["conditionType", "currencyCode", "currencyType", "quantity", "amount"]

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
        """Create an instance of PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner from a JSON string"""
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
        # set to None if condition_type (nullable) is None
        # and model_fields_set contains the field
        if self.condition_type is None and "condition_type" in self.model_fields_set:
            _dict['conditionType'] = None

        # set to None if currency_code (nullable) is None
        # and model_fields_set contains the field
        if self.currency_code is None and "currency_code" in self.model_fields_set:
            _dict['currencyCode'] = None

        # set to None if currency_type (nullable) is None
        # and model_fields_set contains the field
        if self.currency_type is None and "currency_type" in self.model_fields_set:
            _dict['currencyType'] = None

        # set to None if quantity (nullable) is None
        # and model_fields_set contains the field
        if self.quantity is None and "quantity" in self.model_fields_set:
            _dict['quantity'] = None

        # set to None if amount (nullable) is None
        # and model_fields_set contains the field
        if self.amount is None and "amount" in self.model_fields_set:
            _dict['amount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceAndAvailabilityResponseInnerDiscountsInnerQuantityDiscountsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conditionType": obj.get("conditionType"),
            "currencyCode": obj.get("currencyCode"),
            "currencyType": obj.get("currencyType"),
            "quantity": obj.get("quantity"),
            "amount": obj.get("amount")
        })
        return _obj


