# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
import functools  # noqa: F401
from urllib3._collections import HTTPHeaderDict

from edu_sharing_client import api_client, exceptions
import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from edu_sharing_client.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    NoneClass,
    BoolClass,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)

from edu_sharing_client.model.error_response import ErrorResponse

# query params
NodeSchema = StrSchema
RequestRequiredQueryParams = typing.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing.TypedDict(
    'RequestOptionalQueryParams',
    {
        'node': NodeSchema,
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_node = api_client.QueryParameter(
    name="node",
    style=api_client.ParameterStyle.FORM,
    schema=NodeSchema,
    explode=True,
)
# path params
RepositorySchema = StrSchema


class EventSchema(
    _SchemaEnumMaker(
        enum_value_to_name={
            "DOWNLOAD_MATERIAL": "DOWNLOAD_MATERIAL",
            "VIEW_MATERIAL": "VIEW_MATERIAL",
            "VIEW_MATERIAL_EMBEDDED": "VIEW_MATERIAL_EMBEDDED",
            "VIEW_MATERIAL_PLAY_MEDIA": "VIEW_MATERIAL_PLAY_MEDIA",
            "LOGIN_USER_SESSION": "LOGIN_USER_SESSION",
            "LOGIN_USER_OAUTH_PASSWORD": "LOGIN_USER_OAUTH_PASSWORD",
            "LOGIN_USER_OAUTH_REFRESH_TOKEN": "LOGIN_USER_OAUTH_REFRESH_TOKEN",
            "LOGOUT_USER_TIMEOUT": "LOGOUT_USER_TIMEOUT",
            "LOGOUT_USER_REGULAR": "LOGOUT_USER_REGULAR",
        }
    ),
    StrSchema
):
    
    @classmethod
    @property
    def DOWNLOAD_MATERIAL(cls):
        return cls("DOWNLOAD_MATERIAL")
    
    @classmethod
    @property
    def VIEW_MATERIAL(cls):
        return cls("VIEW_MATERIAL")
    
    @classmethod
    @property
    def VIEW_MATERIAL_EMBEDDED(cls):
        return cls("VIEW_MATERIAL_EMBEDDED")
    
    @classmethod
    @property
    def VIEW_MATERIAL_PLAY_MEDIA(cls):
        return cls("VIEW_MATERIAL_PLAY_MEDIA")
    
    @classmethod
    @property
    def LOGIN_USER_SESSION(cls):
        return cls("LOGIN_USER_SESSION")
    
    @classmethod
    @property
    def LOGIN_USER_OAUTH_PASSWORD(cls):
        return cls("LOGIN_USER_OAUTH_PASSWORD")
    
    @classmethod
    @property
    def LOGIN_USER_OAUTH_REFRESH_TOKEN(cls):
        return cls("LOGIN_USER_OAUTH_REFRESH_TOKEN")
    
    @classmethod
    @property
    def LOGOUT_USER_TIMEOUT(cls):
        return cls("LOGOUT_USER_TIMEOUT")
    
    @classmethod
    @property
    def LOGOUT_USER_REGULAR(cls):
        return cls("LOGOUT_USER_REGULAR")
RequestRequiredPathParams = typing.TypedDict(
    'RequestRequiredPathParams',
    {
        'repository': RepositorySchema,
        'event': EventSchema,
    }
)
RequestOptionalPathParams = typing.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_repository = api_client.PathParameter(
    name="repository",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RepositorySchema,
    required=True,
)
request_path_event = api_client.PathParameter(
    name="event",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EventSchema,
    required=True,
)
_path = '/tracking/v1/tracking/{repository}/{event}'
_method = 'PUT'


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        Unset,
    ]
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor403ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor404ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '403': _response_for_403,
    '404': _response_for_404,
    '500': _response_for_500,
}
_all_accept_content_types = (
    'application/json',
)


class TrackEvent(api_client.Api):

    def track_event(
        self: api_client.Api,
        query_params: RequestQueryParams = frozendict(),
        path_params: RequestPathParams = frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        Track a user interaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs(RequestPathParams, path_params)
        used_path = _path

        _path_params = {}
        for parameter in (
            request_path_repository,
            request_path_event,
        ):
            parameter_data = path_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_node,
        ):
            parameter_data = query_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method=_method,
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response
