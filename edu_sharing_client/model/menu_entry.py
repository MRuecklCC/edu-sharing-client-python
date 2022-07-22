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


class MenuEntry(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    position = Int32Schema
    icon = StrSchema
    name = StrSchema
    url = StrSchema
    isDisabled = BoolSchema
    openInNew = BoolSchema
    isSeparate = BoolSchema
    isSeparateBottom = BoolSchema
    onlyDesktop = BoolSchema
    onlyWeb = BoolSchema
    path = StrSchema
    scope = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        position: typing.Union[position, Unset] = unset,
        icon: typing.Union[icon, Unset] = unset,
        name: typing.Union[name, Unset] = unset,
        url: typing.Union[url, Unset] = unset,
        isDisabled: typing.Union[isDisabled, Unset] = unset,
        openInNew: typing.Union[openInNew, Unset] = unset,
        isSeparate: typing.Union[isSeparate, Unset] = unset,
        isSeparateBottom: typing.Union[isSeparateBottom, Unset] = unset,
        onlyDesktop: typing.Union[onlyDesktop, Unset] = unset,
        onlyWeb: typing.Union[onlyWeb, Unset] = unset,
        path: typing.Union[path, Unset] = unset,
        scope: typing.Union[scope, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'MenuEntry':
        return super().__new__(
            cls,
            *args,
            position=position,
            icon=icon,
            name=name,
            url=url,
            isDisabled=isDisabled,
            openInNew=openInNew,
            isSeparate=isSeparate,
            isSeparateBottom=isSeparateBottom,
            onlyDesktop=onlyDesktop,
            onlyWeb=onlyWeb,
            path=path,
            scope=scope,
            _configuration=_configuration,
            **kwargs,
        )