# ProductDetailResponseTechnicalSpecificationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_name** | **str** | Example : &#39;Basic&#39; | [optional] 
**attribute_name** | **str** | Example : &#39;Product Type&#39; | [optional] 
**attribute_display** | **str** | Example : &#39;Basic|Product Type|LCD Monitor&#39; | [optional] 
**attribute_value** | **str** | Example : &#39;LCD Monitor&#39; | [optional] 

## Example

```python
from xi.sdk.resellers.models.product_detail_response_technical_specifications_inner import ProductDetailResponseTechnicalSpecificationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailResponseTechnicalSpecificationsInner from a JSON string
product_detail_response_technical_specifications_inner_instance = ProductDetailResponseTechnicalSpecificationsInner.from_json(json)
# print the JSON string representation of the object
print(ProductDetailResponseTechnicalSpecificationsInner.to_json())

# convert the object into a dict
product_detail_response_technical_specifications_inner_dict = product_detail_response_technical_specifications_inner_instance.to_dict()
# create an instance of ProductDetailResponseTechnicalSpecificationsInner from a dict
product_detail_response_technical_specifications_inner_from_dict = ProductDetailResponseTechnicalSpecificationsInner.from_dict(product_detail_response_technical_specifications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


