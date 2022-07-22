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


class Comment(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @classmethod
    @property
    def ref(cls) -> typing.Type['NodeRef']:
        return NodeRef

    @classmethod
    @property
    def replyTo(cls) -> typing.Type['NodeRef']:
        return NodeRef

    @classmethod
    @property
    def creator(cls) -> typing.Type['UserSimple']:
        return UserSimple
    created = Int64Schema
    comment = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        ref: typing.Union['NodeRef', Unset] = unset,
        replyTo: typing.Union['NodeRef', Unset] = unset,
        creator: typing.Union['UserSimple', Unset] = unset,
        created: typing.Union[created, Unset] = unset,
        comment: typing.Union[comment, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'Comment':
        return super().__new__(
            cls,
            *args,
            ref=ref,
            replyTo=replyTo,
            creator=creator,
            created=created,
            comment=comment,
            _configuration=_configuration,
            **kwargs,
        )

from edu_sharing_client.model.node_ref import NodeRef
from edu_sharing_client.model.user_simple import UserSimple
