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
from xi.sdk.resellers.models.price_and_availability_request_products_inner_additional_attributes_inner import PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner
from xi.sdk.resellers.models.price_and_availability_request_products_inner_plan_id import PriceAndAvailabilityRequestProductsInnerPlanID
from xi.sdk.resellers.models.price_and_availability_request_products_inner_quantity_requested import PriceAndAvailabilityRequestProductsInnerQuantityRequested
from typing import Optional, Set
from typing_extensions import Self

class PriceAndAvailabilityRequestProductsInner(BaseModel):
    """
    PriceAndAvailabilityRequestProductsInner
    """ # noqa: E501
    ingram_part_number: Optional[StrictStr] = Field(default=None, description="Ingram Micro unique part number for the product.", alias="ingramPartNumber")
    vendor_part_number: Optional[StrictStr] = Field(default=None, description="Vendor’s part number for the product.", alias="vendorPartNumber")
    customer_part_number: Optional[StrictStr] = Field(default=None, description="Reseller/end-user’s part number for the product.", alias="customerPartNumber")
    upc: Optional[StrictStr] = Field(default=None, description="The UPC code for the product. Consists of 12 numeric digits that are uniquely assigned to each trade item.")
    quantity_requested: Optional[PriceAndAvailabilityRequestProductsInnerQuantityRequested] = Field(default=None, alias="quantityRequested")
    plan_id: Optional[PriceAndAvailabilityRequestProductsInnerPlanID] = Field(default=None, alias="planID")
    additional_attributes: Optional[List[PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner]] = Field(default=None, alias="additionalAttributes")
    __properties: ClassVar[List[str]] = ["ingramPartNumber", "vendorPartNumber", "customerPartNumber", "upc", "quantityRequested", "planID", "additionalAttributes"]

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
        """Create an instance of PriceAndAvailabilityRequestProductsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of quantity_requested
        if self.quantity_requested:
            _dict['quantityRequested'] = self.quantity_requested.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan_id
        if self.plan_id:
            _dict['planID'] = self.plan_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item_additional_attributes in self.additional_attributes:
                if _item_additional_attributes:
                    _items.append(_item_additional_attributes.to_dict())
            _dict['additionalAttributes'] = _items
        # set to None if ingram_part_number (nullable) is None
        # and model_fields_set contains the field
        if self.ingram_part_number is None and "ingram_part_number" in self.model_fields_set:
            _dict['ingramPartNumber'] = None

        # set to None if vendor_part_number (nullable) is None
        # and model_fields_set contains the field
        if self.vendor_part_number is None and "vendor_part_number" in self.model_fields_set:
            _dict['vendorPartNumber'] = None

        # set to None if customer_part_number (nullable) is None
        # and model_fields_set contains the field
        if self.customer_part_number is None and "customer_part_number" in self.model_fields_set:
            _dict['customerPartNumber'] = None

        # set to None if upc (nullable) is None
        # and model_fields_set contains the field
        if self.upc is None and "upc" in self.model_fields_set:
            _dict['upc'] = None

        # set to None if quantity_requested (nullable) is None
        # and model_fields_set contains the field
        if self.quantity_requested is None and "quantity_requested" in self.model_fields_set:
            _dict['quantityRequested'] = None

        # set to None if plan_id (nullable) is None
        # and model_fields_set contains the field
        if self.plan_id is None and "plan_id" in self.model_fields_set:
            _dict['planID'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceAndAvailabilityRequestProductsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "vendorPartNumber": obj.get("vendorPartNumber"),
            "customerPartNumber": obj.get("customerPartNumber"),
            "upc": obj.get("upc"),
            "quantityRequested": PriceAndAvailabilityRequestProductsInnerQuantityRequested.from_dict(obj["quantityRequested"]) if obj.get("quantityRequested") is not None else None,
            "planID": PriceAndAvailabilityRequestProductsInnerPlanID.from_dict(obj["planID"]) if obj.get("planID") is not None else None,
            "additionalAttributes": [PriceAndAvailabilityRequestProductsInnerAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None
        })
        return _obj


