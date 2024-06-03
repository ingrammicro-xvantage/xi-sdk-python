# OrderCreateRequestAdditionalAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | allowPartialOrder: Allow orders with failed lines. (SAP) Depends on backorder settings.    DpasRating: DX rating by Department of Defense is the highest rating by the highest offices and meant to be top priority. DO any other gov offices at the federal level to priotize.    DpasProgramId: Identifies the actual agency that signed off on the DPAS priority.    allowDuplicateCustomerOrderNumber: Allow orders with duplicate customer PO numbers. Enables resellers to have the same PO number for multiple orders.     channelCode: Determine storage location for Markeplace(SAP) for different orderTypes.    customerPOType: Used for pricing, similar to orderType. Possible SAP values- ZXML and ZWEB.    storageLocation: Determine the location of the product stock in SAP for Marketplaces.    soldTo: To be used in cases when Sold-To is different than Customer ID.    orderType: Order Type[SAP]- ZOR and ZLCN.    endUserSearchTerm: Search ID for a end user contact is used in SAP to determine the contact name.    Z101: Used for end customer details such as name, address, phone, etc. This information flows to SAP and is used by warehouse.    euDepId: DEP ID would be the &#39;End User DEP/ABM Organization ID&#39; up to 32 characters and is assigned by Apple.    depOrderNbr: depordernbr is &#39;End User PO to reseller&#39; Can appear in message lines or dedicated end user po#.    govtProgramType: Program type, “PA” for government orders, “ED” for education order.    govtEndUserType: Type of end user of the program. F &#x3D; Federal, S &#x3D; State, E &#x3D; Local, K &#x3D; K-12 school, and H &#x3D; Higher Education    govtSolicitationNumber: Education order’s contract number    govtPublicPrivateCode: Determines TAX / NO TAX.   &#39;P&#39; PUBLIC SECTOR,   &#39;R&#39; PRIVATE SECTOR.  Value needs only to be provided for EDUCATION order.    govtEndUserData: Name of the End user of the program. For example, STATE OF OHIO, CHICAGO SCHOOLDISTRICT etc.    govtEndUserPostalCode: 9 CHAR FIELD / Zip Code of the End user of the order.    dynamicMessageLine1: Custom Dynamic Message line 1.    allowOrderOnCustomerHold: Boolean value flag which allows a customer to create an order with the hold status. | [optional] 
**attribute_value** | **str** | attributefield data | [optional] 

## Example

```python
from xi.sdk.resellers.models.order_create_request_additional_attributes_inner import OrderCreateRequestAdditionalAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestAdditionalAttributesInner from a JSON string
order_create_request_additional_attributes_inner_instance = OrderCreateRequestAdditionalAttributesInner.from_json(json)
# print the JSON string representation of the object
print(OrderCreateRequestAdditionalAttributesInner.to_json())

# convert the object into a dict
order_create_request_additional_attributes_inner_dict = order_create_request_additional_attributes_inner_instance.to_dict()
# create an instance of OrderCreateRequestAdditionalAttributesInner from a dict
order_create_request_additional_attributes_inner_from_dict = OrderCreateRequestAdditionalAttributesInner.from_dict(order_create_request_additional_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


