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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderModifyRequestLinesInner(BaseModel):
    """
    OrderModifyRequestLinesInner
    """ # noqa: E501
    ingram_part_number: Optional[Annotated[str, Field(strict=True, max_length=18)]] = Field(default=None, description="The unique IngramMicro part number.", alias="ingramPartNumber")
    ingram_line_number: Optional[Annotated[str, Field(strict=True, max_length=6)]] = Field(default=None, description="The IngramMicro line number.", alias="ingramLineNumber")
    customer_line_number: Optional[Annotated[str, Field(strict=True, max_length=6)]] = Field(default=None, description="The reseller's line number for reference in their system.", alias="customerLineNumber")
    add_update_delete_line: Optional[StrictStr] = Field(default=None, description="The line number that was added, updated, or deleted.", alias="addUpdateDeleteLine")
    quantity: Optional[StrictInt] = Field(default=None, description="The quantity of the line item.")
    notes: Optional[Annotated[str, Field(strict=True, max_length=132)]] = Field(default=None, description="The line-level notes.")
    __properties: ClassVar[List[str]] = ["ingramPartNumber", "ingramLineNumber", "customerLineNumber", "addUpdateDeleteLine", "quantity", "notes"]

    @field_validator('add_update_delete_line')
    def add_update_delete_line_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('UPDATE', 'DELETE', 'ADD'):
            raise ValueError("must be one of enum values ('UPDATE', 'DELETE', 'ADD')")
        return value

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
        """Create an instance of OrderModifyRequestLinesInner from a JSON string"""
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
        """Create an instance of OrderModifyRequestLinesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ingramPartNumber": obj.get("ingramPartNumber"),
            "ingramLineNumber": obj.get("ingramLineNumber"),
            "customerLineNumber": obj.get("customerLineNumber"),
            "addUpdateDeleteLine": obj.get("addUpdateDeleteLine"),
            "quantity": obj.get("quantity"),
            "notes": obj.get("notes")
        })
        return _obj

