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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.freight_response_freight_estimate_response_distribution_inner import FreightResponseFreightEstimateResponseDistributionInner
from xi.sdk.resellers.models.freight_response_freight_estimate_response_lines_inner import FreightResponseFreightEstimateResponseLinesInner
from typing import Optional, Set
from typing_extensions import Self

class FreightResponseFreightEstimateResponse(BaseModel):
    """
    FreightResponseFreightEstimateResponse
    """ # noqa: E501
    currency_code: Optional[StrictStr] = Field(default=None, description="The country-specific three-character ISO 4217 currency code used for the order.", alias="currencyCode")
    total_freight_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total freight amount.", alias="totalFreightAmount")
    total_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total tax amount.", alias="totalTaxAmount")
    total_fees: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total fees.", alias="totalFees")
    total_net_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total net amount.", alias="totalNetAmount")
    gross_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Gross amount.", alias="grossAmount")
    distribution: Optional[List[FreightResponseFreightEstimateResponseDistributionInner]] = None
    lines: Optional[List[FreightResponseFreightEstimateResponseLinesInner]] = None
    __properties: ClassVar[List[str]] = ["currencyCode", "totalFreightAmount", "totalTaxAmount", "totalFees", "totalNetAmount", "grossAmount", "distribution", "lines"]

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
        """Create an instance of FreightResponseFreightEstimateResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in distribution (list)
        _items = []
        if self.distribution:
            for _item_distribution in self.distribution:
                if _item_distribution:
                    _items.append(_item_distribution.to_dict())
            _dict['distribution'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item_lines in self.lines:
                if _item_lines:
                    _items.append(_item_lines.to_dict())
            _dict['lines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FreightResponseFreightEstimateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "currencyCode": obj.get("currencyCode"),
            "totalFreightAmount": obj.get("totalFreightAmount"),
            "totalTaxAmount": obj.get("totalTaxAmount"),
            "totalFees": obj.get("totalFees"),
            "totalNetAmount": obj.get("totalNetAmount"),
            "grossAmount": obj.get("grossAmount"),
            "distribution": [FreightResponseFreightEstimateResponseDistributionInner.from_dict(_item) for _item in obj["distribution"]] if obj.get("distribution") is not None else None,
            "lines": [FreightResponseFreightEstimateResponseLinesInner.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None
        })
        return _obj


