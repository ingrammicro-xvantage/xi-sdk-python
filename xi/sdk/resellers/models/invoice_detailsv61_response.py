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
from xi.sdk.resellers.models.invoice_detailsv61_response_bill_to_info import InvoiceDetailsv61ResponseBillToInfo
from xi.sdk.resellers.models.invoice_detailsv61_response_fx_rate_info import InvoiceDetailsv61ResponseFxRateInfo
from xi.sdk.resellers.models.invoice_detailsv61_response_lines_inner import InvoiceDetailsv61ResponseLinesInner
from xi.sdk.resellers.models.invoice_detailsv61_response_payment_terms_info import InvoiceDetailsv61ResponsePaymentTermsInfo
from xi.sdk.resellers.models.invoice_detailsv61_response_ship_to_info import InvoiceDetailsv61ResponseShipToInfo
from xi.sdk.resellers.models.invoice_detailsv61_response_summary import InvoiceDetailsv61ResponseSummary
from typing import Optional, Set
from typing_extensions import Self

class InvoiceDetailsv61Response(BaseModel):
    """
    InvoiceDetailsv61Response
    """ # noqa: E501
    invoice_number: Optional[StrictStr] = Field(default=None, description="The Invoice number for the order.", alias="invoiceNumber")
    invoice_status: Optional[StrictStr] = Field(default=None, description="Status of the invoice.", alias="invoiceStatus")
    invoice_date: Optional[StrictStr] = Field(default=None, description="Date of an Invoice.", alias="invoiceDate")
    customer_order_number: Optional[StrictStr] = Field(default=None, description="The reseller's order number for reference in their system.", alias="customerOrderNumber")
    end_customer_order_number: Optional[StrictStr] = Field(default=None, description="The end customer's order number for reference in their system.", alias="endCustomerOrderNumber")
    order_number: Optional[StrictStr] = Field(default=None, description="The end customer's order number for reference in their system.", alias="orderNumber")
    order_date: Optional[StrictStr] = Field(default=None, description="The date and time in UTC format that the order was created.", alias="orderDate")
    bill_to_id: Optional[StrictStr] = Field(default=None, description="Bill to party", alias="billToID")
    invoice_type: Optional[StrictStr] = Field(default=None, description="Type of the Invoice", alias="invoiceType")
    invoice_due_date: Optional[StrictStr] = Field(default=None, description="Date when the invoice is due.", alias="invoiceDueDate")
    customer_country_code: Optional[StrictStr] = Field(default=None, description="Customer country code.", alias="customerCountryCode")
    customer_number: Optional[StrictStr] = Field(default=None, description="Unique customer number in Ingram's system.", alias="customerNumber")
    ingram_order_number: Optional[StrictStr] = Field(default=None, description="The IngramMicro sales order number.", alias="ingramOrderNumber")
    notes: Optional[StrictStr] = Field(default=None, description="Notes for the invoice.")
    payment_terms_info: Optional[InvoiceDetailsv61ResponsePaymentTermsInfo] = Field(default=None, alias="paymentTermsInfo")
    bill_to_info: Optional[InvoiceDetailsv61ResponseBillToInfo] = Field(default=None, alias="billToInfo")
    ship_to_info: Optional[InvoiceDetailsv61ResponseShipToInfo] = Field(default=None, alias="shipToInfo")
    lines: Optional[List[InvoiceDetailsv61ResponseLinesInner]] = None
    fx_rate_info: Optional[InvoiceDetailsv61ResponseFxRateInfo] = Field(default=None, alias="fxRateInfo")
    summary: Optional[InvoiceDetailsv61ResponseSummary] = None
    __properties: ClassVar[List[str]] = ["invoiceNumber", "invoiceStatus", "invoiceDate", "customerOrderNumber", "endCustomerOrderNumber", "orderNumber", "orderDate", "billToID", "invoiceType", "invoiceDueDate", "customerCountryCode", "customerNumber", "ingramOrderNumber", "notes", "paymentTermsInfo", "billToInfo", "shipToInfo", "lines", "fxRateInfo", "summary"]

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
        """Create an instance of InvoiceDetailsv61Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of payment_terms_info
        if self.payment_terms_info:
            _dict['paymentTermsInfo'] = self.payment_terms_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bill_to_info
        if self.bill_to_info:
            _dict['billToInfo'] = self.bill_to_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to_info
        if self.ship_to_info:
            _dict['shipToInfo'] = self.ship_to_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item_lines in self.lines:
                if _item_lines:
                    _items.append(_item_lines.to_dict())
            _dict['lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of fx_rate_info
        if self.fx_rate_info:
            _dict['fxRateInfo'] = self.fx_rate_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceDetailsv61Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "invoiceNumber": obj.get("invoiceNumber"),
            "invoiceStatus": obj.get("invoiceStatus"),
            "invoiceDate": obj.get("invoiceDate"),
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "endCustomerOrderNumber": obj.get("endCustomerOrderNumber"),
            "orderNumber": obj.get("orderNumber"),
            "orderDate": obj.get("orderDate"),
            "billToID": obj.get("billToID"),
            "invoiceType": obj.get("invoiceType"),
            "invoiceDueDate": obj.get("invoiceDueDate"),
            "customerCountryCode": obj.get("customerCountryCode"),
            "customerNumber": obj.get("customerNumber"),
            "ingramOrderNumber": obj.get("ingramOrderNumber"),
            "notes": obj.get("notes"),
            "paymentTermsInfo": InvoiceDetailsv61ResponsePaymentTermsInfo.from_dict(obj["paymentTermsInfo"]) if obj.get("paymentTermsInfo") is not None else None,
            "billToInfo": InvoiceDetailsv61ResponseBillToInfo.from_dict(obj["billToInfo"]) if obj.get("billToInfo") is not None else None,
            "shipToInfo": InvoiceDetailsv61ResponseShipToInfo.from_dict(obj["shipToInfo"]) if obj.get("shipToInfo") is not None else None,
            "lines": [InvoiceDetailsv61ResponseLinesInner.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "fxRateInfo": InvoiceDetailsv61ResponseFxRateInfo.from_dict(obj["fxRateInfo"]) if obj.get("fxRateInfo") is not None else None,
            "summary": InvoiceDetailsv61ResponseSummary.from_dict(obj["summary"]) if obj.get("summary") is not None else None
        })
        return _obj


