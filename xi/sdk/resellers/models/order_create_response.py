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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from xi.sdk.resellers.models.order_create_response_end_user_info import OrderCreateResponseEndUserInfo
from xi.sdk.resellers.models.order_create_response_orders_inner import OrderCreateResponseOrdersInner
from xi.sdk.resellers.models.order_create_response_ship_to_info import OrderCreateResponseShipToInfo
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateResponse(BaseModel):
    """
    OrderCreateResponse
    """ # noqa: E501
    customer_order_number: Optional[StrictStr] = Field(default=None, description="The reseller's unique PO/Order number.", alias="customerOrderNumber")
    end_customer_order_number: Optional[StrictStr] = Field(default=None, description="The end user/customer's Purchase Order number.", alias="endCustomerOrderNumber")
    bill_to_address_id: Optional[StrictStr] = Field(default=None, description="Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit", alias="billToAddressId")
    special_bid_number: Optional[StrictStr] = Field(default=None, description="The bid number provided to the reseller by the vendor for special pricing and discounts. Line-level bid numbers take precedence over header-level bid numbers.", alias="specialBidNumber")
    order_split: Optional[StrictBool] = Field(default=None, description="true for multiple orders", alias="orderSplit")
    processed_partially: Optional[StrictBool] = Field(default=None, description="true for partial order succesfully placed", alias="processedPartially")
    purchase_order_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total of all the orders including taxes and fees.", alias="purchaseOrderTotal")
    ship_to_info: Optional[OrderCreateResponseShipToInfo] = Field(default=None, alias="shipToInfo")
    end_user_info: Optional[OrderCreateResponseEndUserInfo] = Field(default=None, alias="endUserInfo")
    orders: Optional[List[OrderCreateResponseOrdersInner]] = Field(default=None, description="Order-level details.")
    __properties: ClassVar[List[str]] = ["customerOrderNumber", "endCustomerOrderNumber", "billToAddressId", "specialBidNumber", "orderSplit", "processedPartially", "purchaseOrderTotal", "shipToInfo", "endUserInfo", "orders"]

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
        """Create an instance of OrderCreateResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ship_to_info
        if self.ship_to_info:
            _dict['shipToInfo'] = self.ship_to_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_user_info
        if self.end_user_info:
            _dict['endUserInfo'] = self.end_user_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in orders (list)
        _items = []
        if self.orders:
            for _item in self.orders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['orders'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderCreateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "endCustomerOrderNumber": obj.get("endCustomerOrderNumber"),
            "billToAddressId": obj.get("billToAddressId"),
            "specialBidNumber": obj.get("specialBidNumber"),
            "orderSplit": obj.get("orderSplit"),
            "processedPartially": obj.get("processedPartially"),
            "purchaseOrderTotal": obj.get("purchaseOrderTotal"),
            "shipToInfo": OrderCreateResponseShipToInfo.from_dict(obj["shipToInfo"]) if obj.get("shipToInfo") is not None else None,
            "endUserInfo": OrderCreateResponseEndUserInfo.from_dict(obj["endUserInfo"]) if obj.get("endUserInfo") is not None else None,
            "orders": [OrderCreateResponseOrdersInner.from_dict(_item) for _item in obj["orders"]] if obj.get("orders") is not None else None
        })
        return _obj


