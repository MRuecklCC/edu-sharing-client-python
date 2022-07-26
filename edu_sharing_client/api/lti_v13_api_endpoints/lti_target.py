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

# path params
NodeIdSchema = StrSchema
RequestRequiredPathParams = typing.TypedDict(
    'RequestRequiredPathParams',
    {
        'nodeId': NodeIdSchema,
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


request_path_node_id = api_client.PathParameter(
    name="nodeId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=NodeIdSchema,
    required=True,
)
# body param


class SchemaForRequestBodyApplicationXWwwFormUrlencoded(
    DictSchema
):
    _required_property_names = set((
        'id_token',
        'state',
    ))
    id_token = StrSchema
    state = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        id_token: id_token,
        state: state,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'SchemaForRequestBodyApplicationXWwwFormUrlencoded':
        return super().__new__(
            cls,
            *args,
            id_token=id_token,
            state=state,
            _configuration=_configuration,
            **kwargs,
        )


request_body_body = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
)
_path = '/lti/v13/lti13/{nodeId}'
_method = 'POST'
SchemaFor200ResponseBodyTextHtml = StrSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyTextHtml,
    ]
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'text/html': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextHtml),
    },
)
SchemaFor400ResponseBodyTextHtml = StrSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyTextHtml,
    ]
    headers: Unset = unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'text/html': api_client.MediaType(
            schema=SchemaFor400ResponseBodyTextHtml),
    },
)
SchemaFor401ResponseBodyTextHtml = StrSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyTextHtml,
    ]
    headers: Unset = unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'text/html': api_client.MediaType(
            schema=SchemaFor401ResponseBodyTextHtml),
    },
)
SchemaFor403ResponseBodyTextHtml = StrSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor403ResponseBodyTextHtml,
    ]
    headers: Unset = unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    content={
        'text/html': api_client.MediaType(
            schema=SchemaFor403ResponseBodyTextHtml),
    },
)
SchemaFor404ResponseBodyTextHtml = StrSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor404ResponseBodyTextHtml,
    ]
    headers: Unset = unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    content={
        'text/html': api_client.MediaType(
            schema=SchemaFor404ResponseBodyTextHtml),
    },
)
SchemaFor500ResponseBodyTextHtml = StrSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyTextHtml,
    ]
    headers: Unset = unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'text/html': api_client.MediaType(
            schema=SchemaFor500ResponseBodyTextHtml),
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
    'text/html',
)


class LtiTarget(api_client.Api):

    def lti_target(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] = unset,
        path_params: RequestPathParams = frozendict(),
        content_type: str = 'application/x-www-form-urlencoded',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        lti tool resource link target.
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs(RequestPathParams, path_params)
        used_path = _path

        _path_params = {}
        for parameter in (
            request_path_node_id,
        ):
            parameter_data = path_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not unset:
            serialized_data = request_body_body.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method=_method,
            headers=_headers,
            fields=_fields,
            body=_body,
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
