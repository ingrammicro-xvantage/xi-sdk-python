# coding: utf-8

"""
    XI Sdk Resellers

    For resellers seeking to innovate with Ingram Micro's API solutions, automate your eCommerce experience with our array of API's and webhooks to craft a seamless journey for your customers.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from xi.sdk.resellers.models.renewals_details_response import RenewalsDetailsResponse
from xi.sdk.resellers.models.renewals_search_request import RenewalsSearchRequest
from xi.sdk.resellers.models.renewals_search_response import RenewalsSearchResponse

from xi.sdk.resellers.api_client import ApiClient, RequestSerialized
from xi.sdk.resellers.api_response import ApiResponse
from xi.sdk.resellers.rest import RESTResponseType


class RenewalsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_resellers_v6_renewalsdetails(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction across all the systems.")],
        renewal_id: Annotated[StrictStr, Field(description="Unique Ingram renewal ID.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction. Example: MyCompany")] = None,
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
    ) -> RenewalsDetailsResponse:
        """Renewals Details

        The Renewal Details API endpoint will retrieve all the details related to the renewal. The customer is required to pass renewalId as a path parameter while sending a request.

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction across all the systems. (required)
        :type im_correlation_id: str
        :param renewal_id: Unique Ingram renewal ID. (required)
        :type renewal_id: str
        :param im_sender_id: Unique value used to identify the sender of the transaction. Example: MyCompany
        :type im_sender_id: str
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

        _param = self._get_resellers_v6_renewalsdetails_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            renewal_id=renewal_id,
            im_sender_id=im_sender_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RenewalsDetailsResponse",
            '400': "PostRenewalssearch400Response",
            '500': "PostCreateorderV7500Response",
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
    def get_resellers_v6_renewalsdetails_with_http_info(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction across all the systems.")],
        renewal_id: Annotated[StrictStr, Field(description="Unique Ingram renewal ID.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction. Example: MyCompany")] = None,
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
    ) -> ApiResponse[RenewalsDetailsResponse]:
        """Renewals Details

        The Renewal Details API endpoint will retrieve all the details related to the renewal. The customer is required to pass renewalId as a path parameter while sending a request.

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction across all the systems. (required)
        :type im_correlation_id: str
        :param renewal_id: Unique Ingram renewal ID. (required)
        :type renewal_id: str
        :param im_sender_id: Unique value used to identify the sender of the transaction. Example: MyCompany
        :type im_sender_id: str
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

        _param = self._get_resellers_v6_renewalsdetails_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            renewal_id=renewal_id,
            im_sender_id=im_sender_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RenewalsDetailsResponse",
            '400': "PostRenewalssearch400Response",
            '500': "PostCreateorderV7500Response",
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
    def get_resellers_v6_renewalsdetails_without_preload_content(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction across all the systems.")],
        renewal_id: Annotated[StrictStr, Field(description="Unique Ingram renewal ID.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction. Example: MyCompany")] = None,
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
        """Renewals Details

        The Renewal Details API endpoint will retrieve all the details related to the renewal. The customer is required to pass renewalId as a path parameter while sending a request.

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction across all the systems. (required)
        :type im_correlation_id: str
        :param renewal_id: Unique Ingram renewal ID. (required)
        :type renewal_id: str
        :param im_sender_id: Unique value used to identify the sender of the transaction. Example: MyCompany
        :type im_sender_id: str
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

        _param = self._get_resellers_v6_renewalsdetails_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            renewal_id=renewal_id,
            im_sender_id=im_sender_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RenewalsDetailsResponse",
            '400': "PostRenewalssearch400Response",
            '500': "PostCreateorderV7500Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_resellers_v6_renewalsdetails_serialize(
        self,
        im_customer_number,
        im_country_code,
        im_correlation_id,
        renewal_id,
        im_sender_id,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if renewal_id is not None:
            _path_params['renewalId'] = renewal_id
        # process the query parameters
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
        if 'Accept' not in _header_params:
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
            resource_path='/resellers/v6/renewals/{renewalId}',
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




    @validate_call
    def post_renewalssearch(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction across all the systems.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction. Example: MyCompany")] = None,
        customer_order_number: Annotated[Optional[StrictStr], Field(description="The reseller's unique PO/Order number.")] = None,
        ingram_purchase_order_number: Annotated[Optional[StrictStr], Field(description="Sales order number.")] = None,
        serial_number: Annotated[Optional[StrictStr], Field(description="A serial number of the product.")] = None,
        page: Annotated[Optional[StrictStr], Field(description="Number of page.")] = None,
        size: Annotated[Optional[StrictStr], Field(description="The submitted pagesize, default is 25.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Refers to the column selected to apply the sorting criteria.")] = None,
        renewals_search_request: Optional[RenewalsSearchRequest] = None,
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
    ) -> RenewalsSearchResponse:
        """Renewals Search

        The Renewal Search API, by default, will retrieve all the renewals that are associated with the customer’s account. The customer will be able to search for renewals via basic search or advanced search. Basic search is available thru the query string parameters, whereas the advanced search is available thru the request body schema. 

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction across all the systems. (required)
        :type im_correlation_id: str
        :param im_sender_id: Unique value used to identify the sender of the transaction. Example: MyCompany
        :type im_sender_id: str
        :param customer_order_number: The reseller's unique PO/Order number.
        :type customer_order_number: str
        :param ingram_purchase_order_number: Sales order number.
        :type ingram_purchase_order_number: str
        :param serial_number: A serial number of the product.
        :type serial_number: str
        :param page: Number of page.
        :type page: str
        :param size: The submitted pagesize, default is 25.
        :type size: str
        :param sort: Refers to the column selected to apply the sorting criteria.
        :type sort: str
        :param renewals_search_request:
        :type renewals_search_request: RenewalsSearchRequest
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

        _param = self._post_renewalssearch_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            im_sender_id=im_sender_id,
            customer_order_number=customer_order_number,
            ingram_purchase_order_number=ingram_purchase_order_number,
            serial_number=serial_number,
            page=page,
            size=size,
            sort=sort,
            renewals_search_request=renewals_search_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RenewalsSearchResponse",
            '400': "PostRenewalssearch400Response",
            '500': "PostCreateorderV7500Response",
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
    def post_renewalssearch_with_http_info(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction across all the systems.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction. Example: MyCompany")] = None,
        customer_order_number: Annotated[Optional[StrictStr], Field(description="The reseller's unique PO/Order number.")] = None,
        ingram_purchase_order_number: Annotated[Optional[StrictStr], Field(description="Sales order number.")] = None,
        serial_number: Annotated[Optional[StrictStr], Field(description="A serial number of the product.")] = None,
        page: Annotated[Optional[StrictStr], Field(description="Number of page.")] = None,
        size: Annotated[Optional[StrictStr], Field(description="The submitted pagesize, default is 25.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Refers to the column selected to apply the sorting criteria.")] = None,
        renewals_search_request: Optional[RenewalsSearchRequest] = None,
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
    ) -> ApiResponse[RenewalsSearchResponse]:
        """Renewals Search

        The Renewal Search API, by default, will retrieve all the renewals that are associated with the customer’s account. The customer will be able to search for renewals via basic search or advanced search. Basic search is available thru the query string parameters, whereas the advanced search is available thru the request body schema. 

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction across all the systems. (required)
        :type im_correlation_id: str
        :param im_sender_id: Unique value used to identify the sender of the transaction. Example: MyCompany
        :type im_sender_id: str
        :param customer_order_number: The reseller's unique PO/Order number.
        :type customer_order_number: str
        :param ingram_purchase_order_number: Sales order number.
        :type ingram_purchase_order_number: str
        :param serial_number: A serial number of the product.
        :type serial_number: str
        :param page: Number of page.
        :type page: str
        :param size: The submitted pagesize, default is 25.
        :type size: str
        :param sort: Refers to the column selected to apply the sorting criteria.
        :type sort: str
        :param renewals_search_request:
        :type renewals_search_request: RenewalsSearchRequest
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

        _param = self._post_renewalssearch_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            im_sender_id=im_sender_id,
            customer_order_number=customer_order_number,
            ingram_purchase_order_number=ingram_purchase_order_number,
            serial_number=serial_number,
            page=page,
            size=size,
            sort=sort,
            renewals_search_request=renewals_search_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RenewalsSearchResponse",
            '400': "PostRenewalssearch400Response",
            '500': "PostCreateorderV7500Response",
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
    def post_renewalssearch_without_preload_content(
        self,
        im_customer_number: Annotated[str, Field(strict=True, max_length=10, description="Your unique Ingram Micro customer number.")],
        im_country_code: Annotated[str, Field(min_length=2, strict=True, max_length=2, description="Two-character ISO country code.")],
        im_correlation_id: Annotated[str, Field(strict=True, max_length=32, description="Unique transaction number to identify each transaction across all the systems.")],
        im_sender_id: Annotated[Optional[Annotated[str, Field(strict=True, max_length=32)]], Field(description="Unique value used to identify the sender of the transaction. Example: MyCompany")] = None,
        customer_order_number: Annotated[Optional[StrictStr], Field(description="The reseller's unique PO/Order number.")] = None,
        ingram_purchase_order_number: Annotated[Optional[StrictStr], Field(description="Sales order number.")] = None,
        serial_number: Annotated[Optional[StrictStr], Field(description="A serial number of the product.")] = None,
        page: Annotated[Optional[StrictStr], Field(description="Number of page.")] = None,
        size: Annotated[Optional[StrictStr], Field(description="The submitted pagesize, default is 25.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Refers to the column selected to apply the sorting criteria.")] = None,
        renewals_search_request: Optional[RenewalsSearchRequest] = None,
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
        """Renewals Search

        The Renewal Search API, by default, will retrieve all the renewals that are associated with the customer’s account. The customer will be able to search for renewals via basic search or advanced search. Basic search is available thru the query string parameters, whereas the advanced search is available thru the request body schema. 

        :param im_customer_number: Your unique Ingram Micro customer number. (required)
        :type im_customer_number: str
        :param im_country_code: Two-character ISO country code. (required)
        :type im_country_code: str
        :param im_correlation_id: Unique transaction number to identify each transaction across all the systems. (required)
        :type im_correlation_id: str
        :param im_sender_id: Unique value used to identify the sender of the transaction. Example: MyCompany
        :type im_sender_id: str
        :param customer_order_number: The reseller's unique PO/Order number.
        :type customer_order_number: str
        :param ingram_purchase_order_number: Sales order number.
        :type ingram_purchase_order_number: str
        :param serial_number: A serial number of the product.
        :type serial_number: str
        :param page: Number of page.
        :type page: str
        :param size: The submitted pagesize, default is 25.
        :type size: str
        :param sort: Refers to the column selected to apply the sorting criteria.
        :type sort: str
        :param renewals_search_request:
        :type renewals_search_request: RenewalsSearchRequest
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

        _param = self._post_renewalssearch_serialize(
            im_customer_number=im_customer_number,
            im_country_code=im_country_code,
            im_correlation_id=im_correlation_id,
            im_sender_id=im_sender_id,
            customer_order_number=customer_order_number,
            ingram_purchase_order_number=ingram_purchase_order_number,
            serial_number=serial_number,
            page=page,
            size=size,
            sort=sort,
            renewals_search_request=renewals_search_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "RenewalsSearchResponse",
            '400': "PostRenewalssearch400Response",
            '500': "PostCreateorderV7500Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _post_renewalssearch_serialize(
        self,
        im_customer_number,
        im_country_code,
        im_correlation_id,
        im_sender_id,
        customer_order_number,
        ingram_purchase_order_number,
        serial_number,
        page,
        size,
        sort,
        renewals_search_request,
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
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if customer_order_number is not None:
            
            _query_params.append(('customerOrderNumber', customer_order_number))
            
        if ingram_purchase_order_number is not None:
            
            _query_params.append(('ingramPurchaseOrderNumber', ingram_purchase_order_number))
            
        if serial_number is not None:
            
            _query_params.append(('serialNumber', serial_number))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if size is not None:
            
            _query_params.append(('size', size))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
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
        if renewals_search_request is not None:
            _body_params = renewals_search_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'application'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/resellers/v6/renewals/search',
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


