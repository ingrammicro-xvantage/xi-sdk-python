# AsyncOrderCreateDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quote_number** | **str** | A unique identifier generated by Ingram Micro&#39;s CRM specific to each quote. | [optional] 
**customer_order_number** | **str** | The reseller&#39;s order number for reference in their system. | [optional] 
**endcustomer_order_number** | **str** | The end customer&#39;s order number for reference in their system. | [optional] 
**notes** | **str** | Order header level notes. | [optional] 
**bill_to_address_id** | **str** | Suffix used to identify billing address. Created during onboarding. Resellers are provided with one or more address IDs depending on how many bill to addresses they need for various flooring companies they are using for credit. | [optional] 
**special_bid_number** | **str** | The bid number is provided to the reseller by the vendor for special pricing and discounts. Line-level bid numbers take precedence over header-level bid numbers. | [optional] 
**internal_comments** | **str** | need to replace with actual description | [optional] 
**accept_back_order** | **bool** | ENUM [\&quot;true\&quot;,\&quot;false\&quot;] - accept order if this item is backordered. This field along with shipComplete field decides the value of backorderflag. The value of this field is ignored when shipComplete field is present. | [optional] 
**vend_auth_number** | **str** | Authorization number provided by vendor to Ingram&#39;s reseller. Orders will be placed on hold without this value, vendor specific mandatory field - please reach out Ingram Sales team for list of vendor for whom this is mandatory. | [optional] 
**reseller_info** | [**AsyncOrderCreateDTOResellerInfo**](AsyncOrderCreateDTOResellerInfo.md) |  | [optional] 
**end_user_info** | [**AsyncOrderCreateDTOEndUserInfo**](AsyncOrderCreateDTOEndUserInfo.md) |  | [optional] 
**ship_to_info** | [**AsyncOrderCreateDTOShipToInfo**](AsyncOrderCreateDTOShipToInfo.md) |  | [optional] 
**shipment_details** | [**AsyncOrderCreateDTOShipmentDetails**](AsyncOrderCreateDTOShipmentDetails.md) |  | [optional] 
**additional_attributes** | [**List[AsyncOrderCreateDTOAdditionalAttributesInner]**](AsyncOrderCreateDTOAdditionalAttributesInner.md) | Additional order create attributes. | [optional] 
**vmfadditional_attributes** | [**List[AsyncOrderCreateDTOVmfadditionalAttributesInner]**](AsyncOrderCreateDTOVmfadditionalAttributesInner.md) | The object containing the list of fields required at a header level by the vendor. | [optional] 
**lines** | [**List[AsyncOrderCreateDTOLinesInner]**](AsyncOrderCreateDTOLinesInner.md) | The object containing the lines that require vendor mandatory fields. | [optional] 
**warranty_info** | [**List[AsyncOrderCreateDTOWarrantyInfoInner]**](AsyncOrderCreateDTOWarrantyInfoInner.md) | Warranty Information | [optional] 

## Example

```python
from xi.sdk.resellers.models.async_order_create_dto import AsyncOrderCreateDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncOrderCreateDTO from a JSON string
async_order_create_dto_instance = AsyncOrderCreateDTO.from_json(json)
# print the JSON string representation of the object
print(AsyncOrderCreateDTO.to_json())

# convert the object into a dict
async_order_create_dto_dict = async_order_create_dto_instance.to_dict()
# create an instance of AsyncOrderCreateDTO from a dict
async_order_create_dto_from_dict = AsyncOrderCreateDTO.from_dict(async_order_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

