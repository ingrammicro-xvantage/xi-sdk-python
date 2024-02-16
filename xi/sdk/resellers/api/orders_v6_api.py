# coding: utf-8

"""
    XI SDK Resellers

    For Resellers. Who are looking to Innovate with Ingram Micro's API SolutionsAutomate your eCommerce with our offering of APIs and Webhooks to create a seamless experience for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import date
from pydantic import Field, StrictBool, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from xi.sdk.resellers.models.order_detail_response import OrderDetailResponse

from xi.sdk.resellers.api_client import ApiClient, RequestSerialized
from xi.sdk.resellers.api_response import ApiResponse
from xi.sdk.resellers.rest import RESTResponseType


class OrdersV6Api:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_orderdetails_v6(
        self,
        ordernumber: Annotated[str, Field(strict=True, max_length=12, description="The Ingram Micro sales order number.")],
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction accross all the systems.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction. Example: MyCompany.")] = None,
        ingram_order_date: Annotated[Optional[date], Field(description="The date and time in UTC format that the order was created.")] = None,
        vendor_number: Annotated[Optional[StrictStr], Field(description="Vendor Number.")] = None,
        simulate_status: Annotated[Optional[StrictStr], Field(description="Order response for various order statuses. Not for use in production.")] = None,
        is_iml: Annotated[Optional[StrictBool], Field(description="True/False only for IML customers.")] = None,
        region_code: Annotated[Optional[StrictStr], Field(description="Region code for sandbox testing - Not for use in production.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> OrderDetailResponse:
        """Get Order Details v6

        Use your Ingram Micro sales order number to search for existing orders or retrieve existing order details.  The sales order number, IM-CustomerNumber, IM-CountryCode, IM-SenderID and IM-CorrelationID are required parameters.  In a case when the IM sales order number is repeated, you can refine the result by providing for additional filtering.  Use the \"simulateStatus\" query parameter to test the GET order response for various order statuses. This parameter is only available in the sandbox to help with development and testing of the GET order endpoint.

        :param ordernumber: The Ingram Micro sales order number. (required)
        :type ordernumber: str
        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction accross all the systems. (required)
        :type im_correlation_id: str
        :param im_sender_id: Unique value used to identify the sender of the transaction. Example: MyCompany.
        :type im_sender_id: str
        :param ingram_order_date: The date and time in UTC format that the order was created.
        :type ingram_order_date: date
        :param vendor_number: Vendor Number.
        :type vendor_number: str
        :param simulate_status: Order response for various order statuses. Not for use in production.
        :type simulate_status: str
        :param is_iml: True/False only for IML customers.
        :type is_iml: bool
        :param region_code: Region code for sandbox testing - Not for use in production.
        :type region_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_orderdetails_v6_serialize(
            ordernumber=ordernumber,
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            im_sender_id=im_sender_id,
            ingram_order_date=ingram_order_date,
            vendor_number=vendor_number,
            simulate_status=simulate_status,
            is_iml=is_iml,
            region_code=region_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "OrderDetailResponse",
            '204': "ErrorResponse",
            '400': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_orderdetails_v6_with_http_info(
        self,
        ordernumber: Annotated[str, Field(strict=True, max_length=12, description="The Ingram Micro sales order number.")],
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction accross all the systems.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction. Example: MyCompany.")] = None,
        ingram_order_date: Annotated[Optional[date], Field(description="The date and time in UTC format that the order was created.")] = None,
        vendor_number: Annotated[Optional[StrictStr], Field(description="Vendor Number.")] = None,
        simulate_status: Annotated[Optional[StrictStr], Field(description="Order response for various order statuses. Not for use in production.")] = None,
        is_iml: Annotated[Optional[StrictBool], Field(description="True/False only for IML customers.")] = None,
        region_code: Annotated[Optional[StrictStr], Field(description="Region code for sandbox testing - Not for use in production.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[OrderDetailResponse]:
        """Get Order Details v6

        Use your Ingram Micro sales order number to search for existing orders or retrieve existing order details.  The sales order number, IM-CustomerNumber, IM-CountryCode, IM-SenderID and IM-CorrelationID are required parameters.  In a case when the IM sales order number is repeated, you can refine the result by providing for additional filtering.  Use the \"simulateStatus\" query parameter to test the GET order response for various order statuses. This parameter is only available in the sandbox to help with development and testing of the GET order endpoint.

        :param ordernumber: The Ingram Micro sales order number. (required)
        :type ordernumber: str
        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction accross all the systems. (required)
        :type im_correlation_id: str
        :param im_sender_id: Unique value used to identify the sender of the transaction. Example: MyCompany.
        :type im_sender_id: str
        :param ingram_order_date: The date and time in UTC format that the order was created.
        :type ingram_order_date: date
        :param vendor_number: Vendor Number.
        :type vendor_number: str
        :param simulate_status: Order response for various order statuses. Not for use in production.
        :type simulate_status: str
        :param is_iml: True/False only for IML customers.
        :type is_iml: bool
        :param region_code: Region code for sandbox testing - Not for use in production.
        :type region_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_orderdetails_v6_serialize(
            ordernumber=ordernumber,
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            im_sender_id=im_sender_id,
            ingram_order_date=ingram_order_date,
            vendor_number=vendor_number,
            simulate_status=simulate_status,
            is_iml=is_iml,
            region_code=region_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "OrderDetailResponse",
            '204': "ErrorResponse",
            '400': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_orderdetails_v6_without_preload_content(
        self,
        ordernumber: Annotated[str, Field(strict=True, max_length=12, description="The Ingram Micro sales order number.")],
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction accross all the systems.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction. Example: MyCompany.")] = None,
        ingram_order_date: Annotated[Optional[date], Field(description="The date and time in UTC format that the order was created.")] = None,
        vendor_number: Annotated[Optional[StrictStr], Field(description="Vendor Number.")] = None,
        simulate_status: Annotated[Optional[StrictStr], Field(description="Order response for various order statuses. Not for use in production.")] = None,
        is_iml: Annotated[Optional[StrictBool], Field(description="True/False only for IML customers.")] = None,
        region_code: Annotated[Optional[StrictStr], Field(description="Region code for sandbox testing - Not for use in production.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get Order Details v6

        Use your Ingram Micro sales order number to search for existing orders or retrieve existing order details.  The sales order number, IM-CustomerNumber, IM-CountryCode, IM-SenderID and IM-CorrelationID are required parameters.  In a case when the IM sales order number is repeated, you can refine the result by providing for additional filtering.  Use the \"simulateStatus\" query parameter to test the GET order response for various order statuses. This parameter is only available in the sandbox to help with development and testing of the GET order endpoint.

        :param ordernumber: The Ingram Micro sales order number. (required)
        :type ordernumber: str
        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction accross all the systems. (required)
        :type im_correlation_id: str
        :param im_sender_id: Unique value used to identify the sender of the transaction. Example: MyCompany.
        :type im_sender_id: str
        :param ingram_order_date: The date and time in UTC format that the order was created.
        :type ingram_order_date: date
        :param vendor_number: Vendor Number.
        :type vendor_number: str
        :param simulate_status: Order response for various order statuses. Not for use in production.
        :type simulate_status: str
        :param is_iml: True/False only for IML customers.
        :type is_iml: bool
        :param region_code: Region code for sandbox testing - Not for use in production.
        :type region_code: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_orderdetails_v6_serialize(
            ordernumber=ordernumber,
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            im_sender_id=im_sender_id,
            ingram_order_date=ingram_order_date,
            vendor_number=vendor_number,
            simulate_status=simulate_status,
            is_iml=is_iml,
            region_code=region_code,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "OrderDetailResponse",
            '204': "ErrorResponse",
            '400': "ErrorResponse",
            '500': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_orderdetails_v6_serialize(
        self,
        ordernumber,
        im_customer_number,
        im_country_code,
        im_correlation_id,
        im_sender_id,
        ingram_order_date,
        vendor_number,
        simulate_status,
        is_iml,
        region_code,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if ordernumber is not None:
            _path_params['ordernumber'] = ordernumber
        # process the query parameters
        if ingram_order_date is not None:
            if isinstance(ingram_order_date, date):
                _query_params.append(
                    (
                        'ingramOrderDate',
                        ingram_order_date.strftime(
                            self.api_client.configuration.date_format
                        )
                    )
                )
            else:
                _query_params.append(('ingramOrderDate', ingram_order_date))
            
        if vendor_number is not None:
            
            _query_params.append(('vendorNumber', vendor_number))
            
        if simulate_status is not None:
            
            _query_params.append(('simulateStatus', simulate_status))
            
        if is_iml is not None:
            
            _query_params.append(('isIml', is_iml))
            
        if region_code is not None:
            
            _query_params.append(('regionCode', region_code))
            
        # process the header parameters
        if im_customer_number is not None:
            _header_params['IM-CustomerNumber'] = im_customer_number
        if im_country_code is not None:
            _header_params['IM-CountryCode'] = im_country_code
        if im_correlation_id is not None:
            _header_params['IM-CorrelationID'] = im_correlation_id
        if im_sender_id is not None:
            _header_params['IM-SenderID'] = im_sender_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'application'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/resellers/v6/orders/{ordernumber}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


