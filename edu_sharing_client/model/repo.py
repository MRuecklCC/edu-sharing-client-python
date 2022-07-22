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


class Repo(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    repositoryType = StrSchema
    renderingSupported = BoolSchema
    id = StrSchema
    title = StrSchema
    icon = StrSchema
    logo = StrSchema
    isHomeRepo = BoolSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        repositoryType: typing.Union[repositoryType, Unset] = unset,
        renderingSupported: typing.Union[renderingSupported, Unset] = unset,
        id: typing.Union[id, Unset] = unset,
        title: typing.Union[title, Unset] = unset,
        icon: typing.Union[icon, Unset] = unset,
        logo: typing.Union[logo, Unset] = unset,
        isHomeRepo: typing.Union[isHomeRepo, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'Repo':
        return super().__new__(
            cls,
            *args,
            repositoryType=repositoryType,
            renderingSupported=renderingSupported,
            id=id,
            title=title,
            icon=icon,
            logo=logo,
            isHomeRepo=isHomeRepo,
            _configuration=_configuration,
            **kwargs,
        )