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


class StreamEntry(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id = StrSchema
    description = StrSchema
    
    
    class nodes(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Node']:
            return Node
    
    
    class properties(
        DictSchema
    ):
        _additional_properties = DictSchema
    
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, ],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'properties':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    priority = Int32Schema

    @classmethod
    @property
    def author(cls) -> typing.Type['UserSimple']:
        return UserSimple
    created = Int64Schema
    modified = Int64Schema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        id: typing.Union[id, Unset] = unset,
        description: typing.Union[description, Unset] = unset,
        nodes: typing.Union[nodes, Unset] = unset,
        properties: typing.Union[properties, Unset] = unset,
        priority: typing.Union[priority, Unset] = unset,
        author: typing.Union['UserSimple', Unset] = unset,
        created: typing.Union[created, Unset] = unset,
        modified: typing.Union[modified, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'StreamEntry':
        return super().__new__(
            cls,
            *args,
            id=id,
            description=description,
            nodes=nodes,
            properties=properties,
            priority=priority,
            author=author,
            created=created,
            modified=modified,
            _configuration=_configuration,
            **kwargs,
        )

from edu_sharing_client.model.node import Node
from edu_sharing_client.model.user_simple import UserSimple
