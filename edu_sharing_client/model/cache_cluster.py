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


class CacheCluster(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class instances(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['CacheMember']:
            return CacheMember
    
    
    class cacheInfos(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['CacheInfo']:
            return CacheInfo
    localMember = StrSchema
    freeMemory = Int64Schema
    totalMemory = Int64Schema
    maxMemory = Int64Schema
    availableProcessors = Int32Schema
    timeStamp = DateTimeSchema
    groupName = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        instances: typing.Union[instances, Unset] = unset,
        cacheInfos: typing.Union[cacheInfos, Unset] = unset,
        localMember: typing.Union[localMember, Unset] = unset,
        freeMemory: typing.Union[freeMemory, Unset] = unset,
        totalMemory: typing.Union[totalMemory, Unset] = unset,
        maxMemory: typing.Union[maxMemory, Unset] = unset,
        availableProcessors: typing.Union[availableProcessors, Unset] = unset,
        timeStamp: typing.Union[timeStamp, Unset] = unset,
        groupName: typing.Union[groupName, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'CacheCluster':
        return super().__new__(
            cls,
            *args,
            instances=instances,
            cacheInfos=cacheInfos,
            localMember=localMember,
            freeMemory=freeMemory,
            totalMemory=totalMemory,
            maxMemory=maxMemory,
            availableProcessors=availableProcessors,
            timeStamp=timeStamp,
            groupName=groupName,
            _configuration=_configuration,
            **kwargs,
        )

from edu_sharing_client.model.cache_info import CacheInfo
from edu_sharing_client.model.cache_member import CacheMember
