# xi.sdk.resellers.OrdersApi

All URIs are relative to *https://api.ingrammicro.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ordercancel**](OrdersApi.md#delete_ordercancel) | **DELETE** /resellers/v6/orders/{OrderNumber} | Cancel your Order
[**get_orderdetails_v6_1**](OrdersApi.md#get_orderdetails_v6_1) | **GET** /resellers/v6.1/orders/{ordernumber} | Get Order Details v6.1
[**get_resellers_v6_ordersearch**](OrdersApi.md#get_resellers_v6_ordersearch) | **GET** /resellers/v6/orders/search | Search your Orders
[**post_createorder_v6**](OrdersApi.md#post_createorder_v6) | **POST** /resellers/v6/orders | Create your Order
[**post_createorder_v7**](OrdersApi.md#post_createorder_v7) | **POST** /resellers/v7/orders | Create your Order v7
[**put_ordermodify**](OrdersApi.md#put_ordermodify) | **PUT** /resellers/v6/orders/{orderNumber} | Modify your Order


# **delete_ordercancel**
> delete_ordercancel(order_number, im_customer_number, im_country_code, im_correlation_id, region_code=region_code, im_sender_id=im_sender_id)

Cancel your Order

This call must be submitted before the order is released to Ingram Micro’s warehouse. The order cannot be canceled once it is released to the warehouse. Order should be on customer hold to delete any order from Ingram system.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.OrdersApi(api_client)
    order_number = '20-RD128' # str | Ingram Micro sales order number.
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction accross all the systems.
    region_code = 'CS' # str | Region code for sandbox testing - Not for use in production. (optional)
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)

    try:
        # Cancel your Order
        api_instance.delete_ordercancel(order_number, im_customer_number, im_country_code, im_correlation_id, region_code=region_code, im_sender_id=im_sender_id)
    except Exception as e:
        print("Exception when calling OrdersApi->delete_ordercancel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_number** | **str**| Ingram Micro sales order number. | 
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction accross all the systems. | 
 **region_code** | **str**| Region code for sandbox testing - Not for use in production. | [optional] 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**400** | Bad Request |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**404** | Not Found |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**405** | Method Not Allowed |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**500** | Internal Server Error |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orderdetails_v6_1**
> OrderDetailB2B get_orderdetails_v6_1(ordernumber, im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, ingram_order_date=ingram_order_date, vendor_number=vendor_number, simulate_status=simulate_status, is_iml=is_iml, region_code=region_code)

Get Order Details v6.1

The Orders details API endpoint allows a customer to retrieve their Ingram Micro orders details by using the Ingram Micro sales order number as a path parameter. The sales order number, IM-CustomerNumber, IM-CountryCode, and IM-CorrelationID are required parameters.<br><br>*Service contracts, subscriptions, and license information are unavailable at the moment, this information will be available in the future. <br><br> Recent bug fixes:   - Fixed duplication of serial numbers in the API response.   - Fixed API time-out issues   - Fixed missing tracking information.   - Implemented enhanced order status.  

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_detail_b2_b import OrderDetailB2B
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.OrdersApi(api_client)
    ordernumber = '20-RD3QV' # str | The Ingram Micro sales order number.
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction accross all the systems.
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany. (optional)
    ingram_order_date = 'Wed May 13 00:00:00 UTC 2020' # date | The date and time in UTC format that the order was created. (optional)
    vendor_number = 'vendor_number_example' # str | Vendor Number. (optional)
    simulate_status = 'simulate_status_example' # str | Order response for various order statuses. Not for use in production. (optional)
    is_iml = True # bool | True/False only for IML customers. (optional)
    region_code = 'region_code_example' # str | Region code for sandbox testing - Not for use in production. (optional)

    try:
        # Get Order Details v6.1
        api_response = api_instance.get_orderdetails_v6_1(ordernumber, im_customer_number, im_country_code, im_correlation_id, im_sender_id=im_sender_id, ingram_order_date=ingram_order_date, vendor_number=vendor_number, simulate_status=simulate_status, is_iml=is_iml, region_code=region_code)
        print("The response of OrdersApi->get_orderdetails_v6_1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orderdetails_v6_1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordernumber** | **str**| The Ingram Micro sales order number. | 
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction accross all the systems. | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany. | [optional] 
 **ingram_order_date** | **date**| The date and time in UTC format that the order was created. | [optional] 
 **vendor_number** | **str**| Vendor Number. | [optional] 
 **simulate_status** | **str**| Order response for various order statuses. Not for use in production. | [optional] 
 **is_iml** | **bool**| True/False only for IML customers. | [optional] 
 **region_code** | **str**| Region code for sandbox testing - Not for use in production. | [optional] 

### Return type

[**OrderDetailB2B**](OrderDetailB2B.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resellers_v6_ordersearch**
> OrderSearchResponse get_resellers_v6_ordersearch(im_customer_number, im_country_code, im_correlation_id, ingram_order_number=ingram_order_number, order_status=order_status, order_status_in=order_status_in, ingram_order_date=ingram_order_date, ingram_order_date_bt=ingram_order_date_bt, im_sender_id=im_sender_id, customer_order_number=customer_order_number, page_size=page_size, page_number=page_number, end_customer_order_number=end_customer_order_number, invoice_date_bt=invoice_date_bt, ship_date_bt=ship_date_bt, delivery_date_bt=delivery_date_bt, ingram_part_number=ingram_part_number, vendor_part_number=vendor_part_number, serial_number=serial_number, tracking_number=tracking_number, vendor_name=vendor_name, special_bid_number=special_bid_number)

Search your Orders

The Orders Search API endpoint allows a customer to search their Ingram Micro orders by using any of the available query string parameters, customer can search their order by using single query string parameters or combining them together. This endpoint supports the pagination of results.

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_search_response import OrderSearchResponse
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.OrdersApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction accross all the systems.
    ingram_order_number = 'ingram_order_number_example' # str | The Ingram Micro order number. (optional)
    order_status = 'order_status_example' # str | Ingram Micro order status. (optional)
    order_status_in = ['order_status_in_example'] # List[str] | Ingram Micro order status(can use it for multiple entries). (optional)
    ingram_order_date = '2021-04-23' # str | Search by Order date(yyyy-MM-dd). (optional)
    ingram_order_date_bt = ['ingram_order_date_bt_example'] # List[str] | Search with the start and end date(only 2 entries allowed). (optional)
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)
    customer_order_number = 'customer_order_number_example' # str | Search using your PO/Order number. (optional)
    page_size = 56 # int | The number of records required in the call - max records 100 per page. (optional)
    page_number = 56 # int | The page number reference. (optional)
    end_customer_order_number = 'end_customer_order_number_example' # str | End customer/user purchase order number. (optional)
    invoice_date_bt = ['invoice_date_bt_example'] # List[str] | Invoice date of order, search with the start and end date(only 2 entries allowed).*Currently, this feature is not available in Australia. (optional)
    ship_date_bt = ['ship_date_bt_example'] # List[str] | Shipment date of order, search with the start and end date(only 2 entries allowed). (optional)
    delivery_date_bt = ['delivery_date_bt_example'] # List[str] | The delivery date of the order, search with the start and end date(only 2 entries allowed).*Currently, this feature is not available in Australia (optional)
    ingram_part_number = 'ingram_part_number_example' # str | Ingram Micro unique part number for the product. (optional)
    vendor_part_number = 'vendor_part_number_example' # str | Vendor’s part number for the product. (optional)
    serial_number = 'serial_number_example' # str | A serial number of the product. (optional)
    tracking_number = 'tracking_number_example' # str | The tracking number of the order.*Currently, this feature is not available in Australia (optional)
    vendor_name = 'vendor_name_example' # str | Name of the vendor. (optional)
    special_bid_number = 'special_bid_number_example' # str | The bid number provided to the reseller by the vendor for special pricing and discounts. Line-level bid numbers take precedence over header-level bid numbers.*Currently, this feature is not available in Australia (optional)

    try:
        # Search your Orders
        api_response = api_instance.get_resellers_v6_ordersearch(im_customer_number, im_country_code, im_correlation_id, ingram_order_number=ingram_order_number, order_status=order_status, order_status_in=order_status_in, ingram_order_date=ingram_order_date, ingram_order_date_bt=ingram_order_date_bt, im_sender_id=im_sender_id, customer_order_number=customer_order_number, page_size=page_size, page_number=page_number, end_customer_order_number=end_customer_order_number, invoice_date_bt=invoice_date_bt, ship_date_bt=ship_date_bt, delivery_date_bt=delivery_date_bt, ingram_part_number=ingram_part_number, vendor_part_number=vendor_part_number, serial_number=serial_number, tracking_number=tracking_number, vendor_name=vendor_name, special_bid_number=special_bid_number)
        print("The response of OrdersApi->get_resellers_v6_ordersearch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_resellers_v6_ordersearch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction accross all the systems. | 
 **ingram_order_number** | **str**| The Ingram Micro order number. | [optional] 
 **order_status** | **str**| Ingram Micro order status. | [optional] 
 **order_status_in** | [**List[str]**](str.md)| Ingram Micro order status(can use it for multiple entries). | [optional] 
 **ingram_order_date** | **str**| Search by Order date(yyyy-MM-dd). | [optional] 
 **ingram_order_date_bt** | [**List[str]**](str.md)| Search with the start and end date(only 2 entries allowed). | [optional] 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 
 **customer_order_number** | **str**| Search using your PO/Order number. | [optional] 
 **page_size** | **int**| The number of records required in the call - max records 100 per page. | [optional] 
 **page_number** | **int**| The page number reference. | [optional] 
 **end_customer_order_number** | **str**| End customer/user purchase order number. | [optional] 
 **invoice_date_bt** | [**List[str]**](str.md)| Invoice date of order, search with the start and end date(only 2 entries allowed).*Currently, this feature is not available in Australia. | [optional] 
 **ship_date_bt** | [**List[str]**](str.md)| Shipment date of order, search with the start and end date(only 2 entries allowed). | [optional] 
 **delivery_date_bt** | [**List[str]**](str.md)| The delivery date of the order, search with the start and end date(only 2 entries allowed).*Currently, this feature is not available in Australia | [optional] 
 **ingram_part_number** | **str**| Ingram Micro unique part number for the product. | [optional] 
 **vendor_part_number** | **str**| Vendor’s part number for the product. | [optional] 
 **serial_number** | **str**| A serial number of the product. | [optional] 
 **tracking_number** | **str**| The tracking number of the order.*Currently, this feature is not available in Australia | [optional] 
 **vendor_name** | **str**| Name of the vendor. | [optional] 
 **special_bid_number** | **str**| The bid number provided to the reseller by the vendor for special pricing and discounts. Line-level bid numbers take precedence over header-level bid numbers.*Currently, this feature is not available in Australia | [optional] 

### Return type

[**OrderSearchResponse**](OrderSearchResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrderSearch_Response to be returned |  -  |
**204** | No Content |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_createorder_v6**
> OrderCreateResponse post_createorder_v6(im_customer_number, im_country_code, im_correlation_id, order_create_request, im_sender_id=im_sender_id)

Create your Order

Instantly create and place orders. The POST API supports stocked SKUs as well as licensing and warranties SKUs. IM-CustomerNumber, IM-CountryCode, IM-SenderID and IM-CorrelationID are required parameters. Ingram Micro recommends that you provide the ingrampartnumber for each SKU contained in each order. NOTE: You must have net terms to use the Ingram Micro Order Create API. Ingram Micro offers trade credit when using our APIs, and repayment is based on net terms. For example, if your net terms agreement is net-30, you will have 30 days to make a full payment. Ingram Micro does not allow credit card transactions for API ordering. 

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_create_request import OrderCreateRequest
from xi.sdk.resellers.models.order_create_response import OrderCreateResponse
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.OrdersApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction accross all the systems.
    order_create_request = {"customerOrderNumber":"SWAGGER-01","notes":"This is the field for comments","lines":[{"customerLineNumber":"1","ingramPartNumber":"DF4128","quantity":1}],"additionalAttributes":[{"attributeName":"allowDuplicateCustomerOrderNumber","attributeValue":"true"}]} # OrderCreateRequest | 
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)

    try:
        # Create your Order
        api_response = api_instance.post_createorder_v6(im_customer_number, im_country_code, im_correlation_id, order_create_request, im_sender_id=im_sender_id)
        print("The response of OrdersApi->post_createorder_v6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->post_createorder_v6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction accross all the systems. | 
 **order_create_request** | [**OrderCreateRequest**](OrderCreateRequest.md)|  | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 

### Return type

[**OrderCreateResponse**](OrderCreateResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**207** | Multi-Status |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**400** | Bad Request |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**500** | Internal Server Error |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_createorder_v7**
> AsyncOrderCreateResponse post_createorder_v7(im_customer_number, im_country_code, im_correlation_id, async_order_create_dto, im_sender_id=im_sender_id)

Create your Order v7

This API will allow customers to perform both standard ordering and quote to order functionality via a single API enabling them to have a single endpoint to cater to all types of orders.  This approach will standardize the ordering flow for customers where they will get the response for all orders on to their webhooks.  It provides the much-awaited async ordering flow for Reseller API where large orders can also be placed via a single API with guaranteed delivery. 

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.async_order_create_dto import AsyncOrderCreateDTO
from xi.sdk.resellers.models.async_order_create_response import AsyncOrderCreateResponse
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.OrdersApi(api_client)
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction accross all the systems.
    async_order_create_dto = {"quoteNumber":"QUO-14551943-D2Y9L9","customerOrderNumber":"12345","enduserOrderNumber":"","billToAddressId":"XYZ","endUserInfo":{"companyName":"ABC TECH","contact":"44045678","addressLine1":"Texas","addressLine2":"4","addressLine3":"","city":"","state":"","postalCode":"","countryCode":"US","email":"abc@gmail.com","phoneNumber":"445678901"},"shipToInfo":{"addressId":"12345","companyName":"","contact":"","addressLine1":"Texas","addressLine2":"4","addressLine3":"","city":"","state":"","postalCode":"","countryCode":"US","email":"abc@gmail.com"},"additionalAttributes":[{"attributeName":"VEND_AUTH_NBR_FLG","attributeValue":"ABC1234"}],"vmfAdditionalAttributes":[{"attributeName":"","attributeValue":"","attributeDescription":""}],"lines":[{"customerLineNumber":"12","ingramPartNumber":"YN6231","quantity":"2","vmfAdditionalAttributesLines":[{"attributeName":"","attributeValue":"","attributeDescription":""}]}]} # AsyncOrderCreateDTO | 
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. (optional)

    try:
        # Create your Order v7
        api_response = api_instance.post_createorder_v7(im_customer_number, im_country_code, im_correlation_id, async_order_create_dto, im_sender_id=im_sender_id)
        print("The response of OrdersApi->post_createorder_v7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->post_createorder_v7: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction accross all the systems. | 
 **async_order_create_dto** | [**AsyncOrderCreateDTO**](AsyncOrderCreateDTO.md)|  | 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. | [optional] 

### Return type

[**AsyncOrderCreateResponse**](AsyncOrderCreateResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ordermodify**
> OrderModifyResponse put_ordermodify(order_number, im_customer_number, im_country_code, im_correlation_id, order_modify_request, action_code=action_code, region_code=region_code, im_sender_id=im_sender_id)

Modify your Order

The Order Modify API endpoint allows for changes to be made to an order after the order creation process as long as the order was created with the customer hold flag.  * Orders can be modified within 24hrs of being placed with the customer hold flag, after 24hrs they are voided if they are not released by the customer.  * Modifying orders that were placed without the customer hold flag is not possible 

### Example

* OAuth Authentication (application):

```python
import xi.sdk.resellers
from xi.sdk.resellers.models.order_modify_request import OrderModifyRequest
from xi.sdk.resellers.models.order_modify_response import OrderModifyResponse
from xi.sdk.resellers.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ingrammicro.com:443
# See configuration.py for a list of all supported configuration parameters.
configuration = xi.sdk.resellers.Configuration(
    host = "https://api.ingrammicro.com:443"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with xi.sdk.resellers.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xi.sdk.resellers.OrdersApi(api_client)
    order_number = '20-RC1RD' # str | Ingram sales order number.
    im_customer_number = '20-222222' # str | Your unique Ingram Micro customer number.
    im_country_code = 'US' # str | Two-character ISO country code.
    im_correlation_id = 'fbac82ba-cf0a-4bcf-fc03-0c5084' # str | Unique transaction number to identify each transaction across all the systems.
    order_modify_request = {"lines":[{"customerLineNumber":"002","ingramPartNumber":"2GZ200","addUpdateDeleteLine":"ADD","quantity":2}]} # OrderModifyRequest | 
    action_code = 'release' # str | Action code to be used for order release. (optional)
    region_code = 'CS' # str | Region code paramter to be used only for order release functionality.Region code is only for sandbox not for production (optional)
    im_sender_id = 'MyCompany' # str | Unique value used to identify the sender of the transaction. Example: MyCompany (optional)

    try:
        # Modify your Order
        api_response = api_instance.put_ordermodify(order_number, im_customer_number, im_country_code, im_correlation_id, order_modify_request, action_code=action_code, region_code=region_code, im_sender_id=im_sender_id)
        print("The response of OrdersApi->put_ordermodify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->put_ordermodify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_number** | **str**| Ingram sales order number. | 
 **im_customer_number** | **str**| Your unique Ingram Micro customer number. | 
 **im_country_code** | **str**| Two-character ISO country code. | 
 **im_correlation_id** | **str**| Unique transaction number to identify each transaction across all the systems. | 
 **order_modify_request** | [**OrderModifyRequest**](OrderModifyRequest.md)|  | 
 **action_code** | **str**| Action code to be used for order release. | [optional] 
 **region_code** | **str**| Region code paramter to be used only for order release functionality.Region code is only for sandbox not for production | [optional] 
 **im_sender_id** | **str**| Unique value used to identify the sender of the transaction. Example: MyCompany | [optional] 

### Return type

[**OrderModifyResponse**](OrderModifyResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**201** | Created |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**207** | Multi-Status |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**400** | Bad Request |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  * IM-CorrelationID - Unique transaction number to identify each transaction across all the systems. <br>  * IM-SenderID - Unique value used to identify the sender of the transaction. Example: MyCompany <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

