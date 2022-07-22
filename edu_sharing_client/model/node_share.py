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


class NodeShare(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    password = BoolSchema
    token = StrSchema
    email = StrSchema
    expiryDate = Int64Schema
    invitedAt = Int64Schema
    downloadCount = Int32Schema
    url = StrSchema
    shareId = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        password: typing.Union[password, Unset] = unset,
        token: typing.Union[token, Unset] = unset,
        email: typing.Union[email, Unset] = unset,
        expiryDate: typing.Union[expiryDate, Unset] = unset,
        invitedAt: typing.Union[invitedAt, Unset] = unset,
        downloadCount: typing.Union[downloadCount, Unset] = unset,
        url: typing.Union[url, Unset] = unset,
        shareId: typing.Union[shareId, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'NodeShare':
        return super().__new__(
            cls,
            *args,
            password=password,
            token=token,
            email=email,
            expiryDate=expiryDate,
            invitedAt=invitedAt,
            downloadCount=downloadCount,
            url=url,
            shareId=shareId,
            _configuration=_configuration,
            **kwargs,
        )
