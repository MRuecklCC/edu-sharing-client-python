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


class PersonDeleteResult(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    authorityName = StrSchema
    deletedName = StrSchema
    
    
    class homeFolder(
        DictSchema
    ):
    
        @classmethod
        @property
        def _additional_properties(cls) -> typing.Type['Counts']:
            return Counts
    
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, ],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'homeFolder':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    
    
    class sharedFolders(
        DictSchema
    ):
    
        @classmethod
        @property
        def _additional_properties(cls) -> typing.Type['Counts']:
            return Counts
    
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, ],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'sharedFolders':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )

    @classmethod
    @property
    def collections(cls) -> typing.Type['CollectionCounts']:
        return CollectionCounts
    comments = Int32Schema
    ratings = Int32Schema
    collectionFeedback = Int32Schema
    stream = Int32Schema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        authorityName: typing.Union[authorityName, Unset] = unset,
        deletedName: typing.Union[deletedName, Unset] = unset,
        homeFolder: typing.Union[homeFolder, Unset] = unset,
        sharedFolders: typing.Union[sharedFolders, Unset] = unset,
        collections: typing.Union['CollectionCounts', Unset] = unset,
        comments: typing.Union[comments, Unset] = unset,
        ratings: typing.Union[ratings, Unset] = unset,
        collectionFeedback: typing.Union[collectionFeedback, Unset] = unset,
        stream: typing.Union[stream, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'PersonDeleteResult':
        return super().__new__(
            cls,
            *args,
            authorityName=authorityName,
            deletedName=deletedName,
            homeFolder=homeFolder,
            sharedFolders=sharedFolders,
            collections=collections,
            comments=comments,
            ratings=ratings,
            collectionFeedback=collectionFeedback,
            stream=stream,
            _configuration=_configuration,
            **kwargs,
        )

from edu_sharing_client.model.collection_counts import CollectionCounts
from edu_sharing_client.model.counts import Counts
