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
from xi.sdk.resellers.models.order_detail_b2_b_additional_attributes_inner import OrderDetailB2BAdditionalAttributesInner
from xi.sdk.resellers.models.order_detail_b2_b_bill_to_info import OrderDetailB2BBillToInfo
from xi.sdk.resellers.models.order_detail_b2_b_end_user_info import OrderDetailB2BEndUserInfo
from xi.sdk.resellers.models.order_detail_b2_b_lines_inner import OrderDetailB2BLinesInner
from xi.sdk.resellers.models.order_detail_b2_b_miscellaneous_charges_inner import OrderDetailB2BMiscellaneousChargesInner
from xi.sdk.resellers.models.order_detail_b2_b_ship_to_info import OrderDetailB2BShipToInfo
from typing import Optional, Set
from typing_extensions import Self

class OrderDetailB2B(BaseModel):
    """
    OrderDetailB2B
    """ # noqa: E501
    ingram_order_number: Optional[StrictStr] = Field(default=None, description="The IngramMicro sales order number.", alias="ingramOrderNumber")
    ingram_order_date: Optional[StrictStr] = Field(default=None, description="The IngramMicro sales order date.", alias="ingramOrderDate")
    order_type: Optional[StrictStr] = Field(default=None, description="The IngramMicro sales order type.", alias="orderType")
    customer_order_number: Optional[StrictStr] = Field(default=None, description="The reseller's order number for reference in their system.", alias="customerOrderNumber")
    end_customer_order_number: Optional[StrictStr] = Field(default=None, description="The end customer's order number for reference in their system.", alias="endCustomerOrderNumber")
    web_order_id: Optional[StrictStr] = Field(default=None, description="The web order id of the order.", alias="webOrderId")
    vendor_sales_order_number: Optional[StrictStr] = Field(default=None, description="The vendor's order number for reference in their system", alias="vendorSalesOrderNumber")
    ingram_purchase_order_number: Optional[StrictStr] = Field(default=None, description="Ingram purchase order number.", alias="ingramPurchaseOrderNumber")
    order_status: Optional[StrictStr] = Field(default=None, description="The header-level status of the order. One of- Shipped, Canceled, Backordered, Processing, On Hold, Delivered.", alias="orderStatus")
    order_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total cost for the order, includes subtotal, freight charges, and tax.", alias="orderTotal")
    order_sub_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The sub total cost for the order, not including tax and freight.", alias="orderSubTotal")
    freight_charges: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The freight charges for the order.", alias="freightCharges")
    currency_code: Optional[StrictStr] = Field(default=None, description="The country-specific three digit ISO 4217 currency code for the order.", alias="currencyCode")
    total_weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total order weight. unit -- North america - Pounds , other countries will be KG.", alias="totalWeight")
    total_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total tax on the orders placed.", alias="totalTax")
    total_fees: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total fees on the orders placed.", alias="totalFees")
    payment_terms: Optional[StrictStr] = Field(default=None, description="The payment terms of the order. (Ex- Net 30 days).", alias="paymentTerms")
    notes: Optional[StrictStr] = Field(default=None, description="The header-level notes for the order.")
    bill_to_info: Optional[OrderDetailB2BBillToInfo] = Field(default=None, alias="billToInfo")
    ship_to_info: Optional[OrderDetailB2BShipToInfo] = Field(default=None, alias="shipToInfo")
    end_user_info: Optional[OrderDetailB2BEndUserInfo] = Field(default=None, alias="endUserInfo")
    lines: Optional[List[OrderDetailB2BLinesInner]] = None
    miscellaneous_charges: Optional[List[OrderDetailB2BMiscellaneousChargesInner]] = Field(default=None, alias="miscellaneousCharges")
    additional_attributes: Optional[List[OrderDetailB2BAdditionalAttributesInner]] = Field(default=None, alias="additionalAttributes")
    __properties: ClassVar[List[str]] = ["ingramOrderNumber", "ingramOrderDate", "orderType", "customerOrderNumber", "endCustomerOrderNumber", "webOrderId", "vendorSalesOrderNumber", "ingramPurchaseOrderNumber", "orderStatus", "orderTotal", "orderSubTotal", "freightCharges", "currencyCode", "totalWeight", "totalTax", "totalFees", "paymentTerms", "notes", "billToInfo", "shipToInfo", "endUserInfo", "lines", "miscellaneousCharges", "additionalAttributes"]

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
        """Create an instance of OrderDetailB2B from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bill_to_info
        if self.bill_to_info:
            _dict['billToInfo'] = self.bill_to_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to_info
        if self.ship_to_info:
            _dict['shipToInfo'] = self.ship_to_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_user_info
        if self.end_user_info:
            _dict['endUserInfo'] = self.end_user_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item_lines in self.lines:
                if _item_lines:
                    _items.append(_item_lines.to_dict())
            _dict['lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in miscellaneous_charges (list)
        _items = []
        if self.miscellaneous_charges:
            for _item_miscellaneous_charges in self.miscellaneous_charges:
                if _item_miscellaneous_charges:
                    _items.append(_item_miscellaneous_charges.to_dict())
            _dict['miscellaneousCharges'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in additional_attributes (list)
        _items = []
        if self.additional_attributes:
            for _item_additional_attributes in self.additional_attributes:
                if _item_additional_attributes:
                    _items.append(_item_additional_attributes.to_dict())
            _dict['additionalAttributes'] = _items
        # set to None if lines (nullable) is None
        # and model_fields_set contains the field
        if self.lines is None and "lines" in self.model_fields_set:
            _dict['lines'] = None

        # set to None if miscellaneous_charges (nullable) is None
        # and model_fields_set contains the field
        if self.miscellaneous_charges is None and "miscellaneous_charges" in self.model_fields_set:
            _dict['miscellaneousCharges'] = None

        # set to None if additional_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.additional_attributes is None and "additional_attributes" in self.model_fields_set:
            _dict['additionalAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderDetailB2B from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ingramOrderNumber": obj.get("ingramOrderNumber"),
            "ingramOrderDate": obj.get("ingramOrderDate"),
            "orderType": obj.get("orderType"),
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "endCustomerOrderNumber": obj.get("endCustomerOrderNumber"),
            "webOrderId": obj.get("webOrderId"),
            "vendorSalesOrderNumber": obj.get("vendorSalesOrderNumber"),
            "ingramPurchaseOrderNumber": obj.get("ingramPurchaseOrderNumber"),
            "orderStatus": obj.get("orderStatus"),
            "orderTotal": obj.get("orderTotal"),
            "orderSubTotal": obj.get("orderSubTotal"),
            "freightCharges": obj.get("freightCharges"),
            "currencyCode": obj.get("currencyCode"),
            "totalWeight": obj.get("totalWeight"),
            "totalTax": obj.get("totalTax"),
            "totalFees": obj.get("totalFees"),
            "paymentTerms": obj.get("paymentTerms"),
            "notes": obj.get("notes"),
            "billToInfo": OrderDetailB2BBillToInfo.from_dict(obj["billToInfo"]) if obj.get("billToInfo") is not None else None,
            "shipToInfo": OrderDetailB2BShipToInfo.from_dict(obj["shipToInfo"]) if obj.get("shipToInfo") is not None else None,
            "endUserInfo": OrderDetailB2BEndUserInfo.from_dict(obj["endUserInfo"]) if obj.get("endUserInfo") is not None else None,
            "lines": [OrderDetailB2BLinesInner.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "miscellaneousCharges": [OrderDetailB2BMiscellaneousChargesInner.from_dict(_item) for _item in obj["miscellaneousCharges"]] if obj.get("miscellaneousCharges") is not None else None,
            "additionalAttributes": [OrderDetailB2BAdditionalAttributesInner.from_dict(_item) for _item in obj["additionalAttributes"]] if obj.get("additionalAttributes") is not None else None
        })
        return _obj


