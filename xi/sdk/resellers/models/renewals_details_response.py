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

from datetime import date
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.renewals_details_response_additional_attributes_inner import RenewalsDetailsResponseAdditionalAttributesInner
from xi.sdk.resellers.models.renewals_details_response_end_user_info_inner import RenewalsDetailsResponseEndUserInfoInner
from xi.sdk.resellers.models.renewals_details_response_products_inner import RenewalsDetailsResponseProductsInner
from xi.sdk.resellers.models.renewals_details_response_reference_number_inner import RenewalsDetailsResponseReferenceNumberInner
from typing import Optional, Set
from typing_extensions import Self

class RenewalsDetailsResponse(BaseModel):
    """
    RenewalsDetailsResponse
    """ # noqa: E501
    renewal_id: Optional[StrictStr] = Field(default=None, description="Unique Ingram renewal ID.", alias="renewalId")
    ingram_order_number: Optional[StrictStr] = Field(default=None, description="The IngramMicro sales order number.", alias="ingramOrderNumber")
    ingram_order_date: Optional[date] = Field(default=None, description="The IngramMicro sales order date.", alias="ingramOrderDate")
    expiration_date: Optional[date] = Field(default=None, description="Renewal expiration date.", alias="expirationDate")
    ingram_purchase_order_number: Optional[StrictStr] = Field(default=None, description="Ingram purchase order number.", alias="ingramPurchaseOrderNumber")
    customer_order_number: Optional[StrictStr] = Field(default=None, description="The reseller's order number for reference in their system.", alias="customerOrderNumber")
    end_customer_order_number: Optional[StrictStr] = Field(default=None, description="The end customer's order number for reference in their system.", alias="endCustomerOrderNumber")
    renewal_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The value of the renewal.", alias="renewalValue")
    end_user: Optional[StrictStr] = Field(default=None, description="The company name for the end user/customer.", alias="endUser")
    vendor: Optional[StrictStr] = Field(default=None, description="The name of the vendor.")
    status: Optional[StrictStr] = Field(default=None, description="The status of the renewal.")
    end_user_info: Optional[List[RenewalsDetailsResponseEndUserInfoInner]] = Field(default=None, alias="endUserInfo")
    reference_number: Optional[List[RenewalsDetailsResponseReferenceNumberInner]] = Field(default=None, alias="referenceNumber")
    products: Optional[List[RenewalsDetailsResponseProductsInner]] = None
    additional_attributes: Optional[List[RenewalsDetailsResponseAdditionalAttributesInner]] = Field(default=None, alias="additionalAttributes")
    __properties: ClassVar[List[str]] = ["renewalId", "ingramOrderNumber", "ingramOrderDate", "expirationDate", "ingramPurchaseOrderNumber", "customerOrderNumber", "endCustomerOrderNumber", "renewalValue", "endUser", "vendor", "status", "endUserInfo", "referenceNumber", "products", "additionalAttributes"]

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
        """Create an instance of RenewalsDetailsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in end_user_info (list)
        _items = []
        if self.end_user_info:
            for _item in self.end_user_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['endUserInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reference_number (list)
        _items = []
        if self.reference_number:
            for _item in self.reference_number:
                if _item:
                    _items.append(_item.to_dict())
            _dict['referenceNumber'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item in self.products:
                if _item:
                    _items.append(_item.to_dict())
            _dict['products'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item in self.additional_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['additionalAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RenewalsDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "renewalId": obj.get("renewalId"),
            "ingramOrderNumber": obj.get("ingramOrderNumber"),
            "ingramOrderDate": obj.get("ingramOrderDate"),
            "expirationDate": obj.get("expirationDate"),
            "ingramPurchaseOrderNumber": obj.get("ingramPurchaseOrderNumber"),
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "endCustomerOrderNumber": obj.get("endCustomerOrderNumber"),
            "renewalValue": obj.get("renewalValue"),
            "endUser": obj.get("endUser"),
            "vendor": obj.get("vendor"),
            "status": obj.get("status"),
            "endUserInfo": [RenewalsDetailsResponseEndUserInfoInner.from_dict(_item) for _item in obj["endUserInfo"]] if obj.get("endUserInfo") is not None else None,
            "referenceNumber": [RenewalsDetailsResponseReferenceNumberInner.from_dict(_item) for _item in obj["referenceNumber"]] if obj.get("referenceNumber") is not None else None,
            "products": [RenewalsDetailsResponseProductsInner.from_dict(_item) for _item in obj["products"]] if obj.get("products") is not None else None,
            "additionalAttributes": [RenewalsDetailsResponseAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None
        })
        return _obj


