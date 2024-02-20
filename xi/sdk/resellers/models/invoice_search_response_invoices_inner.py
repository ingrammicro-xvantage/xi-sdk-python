# coding: utf-8

"""
    XI Sdk Resellers

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
from typing import Optional, Set
from typing_extensions import Self

class InvoiceSearchResponseInvoicesInner(BaseModel):
    """
    InvoiceSearchResponseInvoicesInner
    """ # noqa: E501
    payment_terms_due_date: Optional[StrictStr] = Field(default=None, description="Payment Terms Due date.", alias="paymentTermsDueDate")
    erp_order_number: Optional[StrictStr] = Field(default=None, description="Order number", alias="erpOrderNumber")
    invoice_number: Optional[StrictStr] = Field(default=None, description="Invoice no.", alias="invoiceNumber")
    invoice_status: Optional[StrictStr] = Field(default=None, description="Invoice Status.", alias="invoiceStatus")
    invoice_date: Optional[StrictStr] = Field(default=None, description="Invoice Date.", alias="invoiceDate")
    invoice_due_date: Optional[StrictStr] = Field(default=None, description="Invoice Due Date.", alias="invoiceDueDate")
    invoiced_amount_due: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Invoice Amount.", alias="invoicedAmountDue")
    customer_order_number: Optional[StrictStr] = Field(default=None, description="Customer Order No.", alias="customerOrderNumber")
    end_customer_order_number: Optional[StrictStr] = Field(default=None, description="End Customer Order number.", alias="endCustomerOrderNumber")
    order_create_date: Optional[StrictStr] = Field(default=None, description="Order Create Date.", alias="orderCreateDate")
    invoice_amount_incl_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Invoice Amount Inclusive of Taxes", alias="invoiceAmountInclTax")
    forgntotalamount: Optional[Union[StrictFloat, StrictInt]] = None
    gst_invoice_number: Optional[StrictStr] = Field(default=None, alias="gstInvoiceNumber")
    isfeccenabled: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["paymentTermsDueDate", "erpOrderNumber", "invoiceNumber", "invoiceStatus", "invoiceDate", "invoiceDueDate", "invoicedAmountDue", "customerOrderNumber", "endCustomerOrderNumber", "orderCreateDate", "invoiceAmountInclTax", "forgntotalamount", "gstInvoiceNumber", "isfeccenabled"]

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
        """Create an instance of InvoiceSearchResponseInvoicesInner from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceSearchResponseInvoicesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "paymentTermsDueDate": obj.get("paymentTermsDueDate"),
            "erpOrderNumber": obj.get("erpOrderNumber"),
            "invoiceNumber": obj.get("invoiceNumber"),
            "invoiceStatus": obj.get("invoiceStatus"),
            "invoiceDate": obj.get("invoiceDate"),
            "invoiceDueDate": obj.get("invoiceDueDate"),
            "invoicedAmountDue": obj.get("invoicedAmountDue"),
            "customerOrderNumber": obj.get("customerOrderNumber"),
            "endCustomerOrderNumber": obj.get("endCustomerOrderNumber"),
            "orderCreateDate": obj.get("orderCreateDate"),
            "invoiceAmountInclTax": obj.get("invoiceAmountInclTax"),
            "forgntotalamount": obj.get("forgntotalamount"),
            "gstInvoiceNumber": obj.get("gstInvoiceNumber"),
            "isfeccenabled": obj.get("isfeccenabled")
        })
        return _obj


