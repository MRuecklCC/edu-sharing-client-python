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


class Mds(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'name',
        'widgets',
        'views',
        'groups',
        'lists',
        'sorts',
    ))
    name = StrSchema

    @classmethod
    @property
    def create(cls) -> typing.Type['Create']:
        return Create
    
    
    class widgets(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['MdsWidget']:
            return MdsWidget
    
    
    class views(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['MdsView']:
            return MdsView
    
    
    class groups(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['MdsGroup']:
            return MdsGroup
    
    
    class lists(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['MdsList']:
            return MdsList
    
    
    class sorts(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['MdsSort']:
            return MdsSort


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        name: name,
        widgets: widgets,
        views: views,
        groups: groups,
        lists: lists,
        sorts: sorts,
        create: typing.Union['Create', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'Mds':
        return super().__new__(
            cls,
            *args,
            name=name,
            widgets=widgets,
            views=views,
            groups=groups,
            lists=lists,
            sorts=sorts,
            create=create,
            _configuration=_configuration,
            **kwargs,
        )

from edu_sharing_client.model.create import Create
from edu_sharing_client.model.mds_group import MdsGroup
from edu_sharing_client.model.mds_list import MdsList
from edu_sharing_client.model.mds_sort import MdsSort
from edu_sharing_client.model.mds_view import MdsView
from edu_sharing_client.model.mds_widget import MdsWidget
