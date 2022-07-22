# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    The version of the OpenAPI document: 1.1
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

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


class DynamicRegistrationToken(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    token = StrSchema
    url = StrSchema
    registeredAppId = StrSchema
    tsCreated = Int64Schema
    tsExpiry = Int64Schema
    valid = BoolSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        token: typing.Union[token, Unset] = unset,
        url: typing.Union[url, Unset] = unset,
        registeredAppId: typing.Union[registeredAppId, Unset] = unset,
        tsCreated: typing.Union[tsCreated, Unset] = unset,
        tsExpiry: typing.Union[tsExpiry, Unset] = unset,
        valid: typing.Union[valid, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'DynamicRegistrationToken':
        return super().__new__(
            cls,
            *args,
            token=token,
            url=url,
            registeredAppId=registeredAppId,
            tsCreated=tsCreated,
            tsExpiry=tsExpiry,
            valid=valid,
            _configuration=_configuration,
            **kwargs,
        )
