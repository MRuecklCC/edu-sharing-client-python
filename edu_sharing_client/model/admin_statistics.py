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


class AdminStatistics(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    activeSessions = Int32Schema
    numberOfPreviews = Int32Schema
    maxMemory = Int64Schema
    allocatedMemory = Int64Schema
    previewCacheSize = Int64Schema
    
    
    class activeLocks(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Node']:
            return Node


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        activeSessions: typing.Union[activeSessions, Unset] = unset,
        numberOfPreviews: typing.Union[numberOfPreviews, Unset] = unset,
        maxMemory: typing.Union[maxMemory, Unset] = unset,
        allocatedMemory: typing.Union[allocatedMemory, Unset] = unset,
        previewCacheSize: typing.Union[previewCacheSize, Unset] = unset,
        activeLocks: typing.Union[activeLocks, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'AdminStatistics':
        return super().__new__(
            cls,
            *args,
            activeSessions=activeSessions,
            numberOfPreviews=numberOfPreviews,
            maxMemory=maxMemory,
            allocatedMemory=allocatedMemory,
            previewCacheSize=previewCacheSize,
            activeLocks=activeLocks,
            _configuration=_configuration,
            **kwargs,
        )

from edu_sharing_client.model.node import Node
