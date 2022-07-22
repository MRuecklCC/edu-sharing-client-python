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


class StatisticsKeyGroup(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    key = StrSchema
    displayName = StrSchema
    count = Int32Schema
    
    
    class subGroups(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['StatisticsSubGroup']:
            return StatisticsSubGroup


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        key: typing.Union[key, Unset] = unset,
        displayName: typing.Union[displayName, Unset] = unset,
        count: typing.Union[count, Unset] = unset,
        subGroups: typing.Union[subGroups, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'StatisticsKeyGroup':
        return super().__new__(
            cls,
            *args,
            key=key,
            displayName=displayName,
            count=count,
            subGroups=subGroups,
            _configuration=_configuration,
            **kwargs,
        )

from edu_sharing_client.model.statistics_sub_group import StatisticsSubGroup
