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


class Node(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'ref',
        'name',
        'createdAt',
        'createdBy',
        'access',
        'downloadUrl',
        'collection',
        'owner',
    ))

    @classmethod
    @property
    def nodeLTIDeepLink(cls) -> typing.Type['NodeLTIDeepLink']:
        return NodeLTIDeepLink

    @classmethod
    @property
    def remote(cls) -> typing.Type['Remote']:
        return Remote

    @classmethod
    @property
    def content(cls) -> typing.Type['Content']:
        return Content

    @classmethod
    @property
    def license(cls) -> typing.Type['License']:
        return License
    isDirectory = BoolSchema
    commentCount = Int32Schema

    @classmethod
    @property
    def rating(cls) -> typing.Type['RatingDetails']:
        return RatingDetails
    
    
    class usedInCollections(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Node']:
            return Node
    
    
    class relations(
        DictSchema
    ):
    
        @classmethod
        @property
        def _additional_properties(cls) -> typing.Type['Node']:
            return Node
    
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, ],
            _configuration: typing.Optional[Configuration] = None,
            **kwargs: typing.Type[Schema],
        ) -> 'relations':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    
    
    class contributors(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Contributor']:
            return Contributor

    @classmethod
    @property
    def ref(cls) -> typing.Type['NodeRef']:
        return NodeRef

    @classmethod
    @property
    def parent(cls) -> typing.Type['NodeRef']:
        return NodeRef
    type = StrSchema
    
    
    class aspects(
        ListSchema
    ):
        _items = StrSchema
    name = StrSchema
    title = StrSchema
    metadataset = StrSchema
    repositoryType = StrSchema
    createdAt = DateTimeSchema

    @classmethod
    @property
    def createdBy(cls) -> typing.Type['Person']:
        return Person
    modifiedAt = DateTimeSchema

    @classmethod
    @property
    def modifiedBy(cls) -> typing.Type['Person']:
        return Person
    
    
    class access(
        ListSchema
    ):
        _items = StrSchema
    downloadUrl = StrSchema
    
    
    class properties(
        DictSchema
    ):
        
        
        class _additional_properties(
            ListSchema
        ):
            _items = StrSchema
    
    
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
    mimetype = StrSchema
    mediatype = StrSchema
    size = StrSchema

    @classmethod
    @property
    def preview(cls) -> typing.Type['Preview']:
        return Preview
    iconURL = StrSchema

    @classmethod
    @property
    def collection(cls) -> typing.Type['Collection']:
        return Collection

    @classmethod
    @property
    def owner(cls) -> typing.Type['Person']:
        return Person
    isPublic = BoolSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        ref: ref,
        name: name,
        createdAt: createdAt,
        createdBy: createdBy,
        access: access,
        downloadUrl: downloadUrl,
        collection: collection,
        owner: owner,
        nodeLTIDeepLink: typing.Union['NodeLTIDeepLink', Unset] = unset,
        remote: typing.Union['Remote', Unset] = unset,
        content: typing.Union['Content', Unset] = unset,
        license: typing.Union['License', Unset] = unset,
        isDirectory: typing.Union[isDirectory, Unset] = unset,
        commentCount: typing.Union[commentCount, Unset] = unset,
        rating: typing.Union['RatingDetails', Unset] = unset,
        usedInCollections: typing.Union[usedInCollections, Unset] = unset,
        relations: typing.Union[relations, Unset] = unset,
        contributors: typing.Union[contributors, Unset] = unset,
        parent: typing.Union['NodeRef', Unset] = unset,
        type: typing.Union[type, Unset] = unset,
        aspects: typing.Union[aspects, Unset] = unset,
        title: typing.Union[title, Unset] = unset,
        metadataset: typing.Union[metadataset, Unset] = unset,
        repositoryType: typing.Union[repositoryType, Unset] = unset,
        modifiedAt: typing.Union[modifiedAt, Unset] = unset,
        modifiedBy: typing.Union['Person', Unset] = unset,
        properties: typing.Union[properties, Unset] = unset,
        mimetype: typing.Union[mimetype, Unset] = unset,
        mediatype: typing.Union[mediatype, Unset] = unset,
        size: typing.Union[size, Unset] = unset,
        preview: typing.Union['Preview', Unset] = unset,
        iconURL: typing.Union[iconURL, Unset] = unset,
        isPublic: typing.Union[isPublic, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'Node':
        return super().__new__(
            cls,
            *args,
            ref=ref,
            name=name,
            createdAt=createdAt,
            createdBy=createdBy,
            access=access,
            downloadUrl=downloadUrl,
            collection=collection,
            owner=owner,
            nodeLTIDeepLink=nodeLTIDeepLink,
            remote=remote,
            content=content,
            license=license,
            isDirectory=isDirectory,
            commentCount=commentCount,
            rating=rating,
            usedInCollections=usedInCollections,
            relations=relations,
            contributors=contributors,
            parent=parent,
            type=type,
            aspects=aspects,
            title=title,
            metadataset=metadataset,
            repositoryType=repositoryType,
            modifiedAt=modifiedAt,
            modifiedBy=modifiedBy,
            properties=properties,
            mimetype=mimetype,
            mediatype=mediatype,
            size=size,
            preview=preview,
            iconURL=iconURL,
            isPublic=isPublic,
            _configuration=_configuration,
            **kwargs,
        )

from edu_sharing_client.model.collection import Collection
from edu_sharing_client.model.content import Content
from edu_sharing_client.model.contributor import Contributor
from edu_sharing_client.model.license import License
from edu_sharing_client.model.node_lti_deep_link import NodeLTIDeepLink
from edu_sharing_client.model.node_ref import NodeRef
from edu_sharing_client.model.person import Person
from edu_sharing_client.model.preview import Preview
from edu_sharing_client.model.rating_details import RatingDetails
from edu_sharing_client.model.remote import Remote
