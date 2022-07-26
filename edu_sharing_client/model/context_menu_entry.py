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


class ContextMenuEntry(
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
    mode = StrSchema
    
    
    class scopes(
        ListSchema
    ):
        
        
        class _items(
            _SchemaEnumMaker(
                enum_value_to_name={
                    "Render": "RENDER",
                    "Search": "SEARCH",
                    "CollectionsReferences": "COLLECTIONSREFERENCES",
                    "CollectionsCollection": "COLLECTIONSCOLLECTION",
                    "WorkspaceList": "WORKSPACELIST",
                    "WorkspaceTree": "WORKSPACETREE",
                    "Oer": "OER",
                    "CreateMenu": "CREATEMENU",
                }
            ),
            StrSchema
        ):
            
            @classmethod
            @property
            def RENDER(cls):
                return cls("Render")
            
            @classmethod
            @property
            def SEARCH(cls):
                return cls("Search")
            
            @classmethod
            @property
            def COLLECTIONSREFERENCES(cls):
                return cls("CollectionsReferences")
            
            @classmethod
            @property
            def COLLECTIONSCOLLECTION(cls):
                return cls("CollectionsCollection")
            
            @classmethod
            @property
            def WORKSPACELIST(cls):
                return cls("WorkspaceList")
            
            @classmethod
            @property
            def WORKSPACETREE(cls):
                return cls("WorkspaceTree")
            
            @classmethod
            @property
            def OER(cls):
                return cls("Oer")
            
            @classmethod
            @property
            def CREATEMENU(cls):
                return cls("CreateMenu")
    ajax = BoolSchema
    group = StrSchema
    permission = StrSchema
    toolpermission = StrSchema
    isDirectory = BoolSchema
    showAsAction = BoolSchema
    multiple = BoolSchema
    
    
    class changeStrategy(
        _SchemaEnumMaker(
            enum_value_to_name={
                "update": "UPDATE",
                "remove": "REMOVE",
            }
        ),
        StrSchema
    ):
        
        @classmethod
        @property
        def UPDATE(cls):
            return cls("update")
        
        @classmethod
        @property
        def REMOVE(cls):
            return cls("remove")


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
        mode: typing.Union[mode, Unset] = unset,
        scopes: typing.Union[scopes, Unset] = unset,
        ajax: typing.Union[ajax, Unset] = unset,
        group: typing.Union[group, Unset] = unset,
        permission: typing.Union[permission, Unset] = unset,
        toolpermission: typing.Union[toolpermission, Unset] = unset,
        isDirectory: typing.Union[isDirectory, Unset] = unset,
        showAsAction: typing.Union[showAsAction, Unset] = unset,
        multiple: typing.Union[multiple, Unset] = unset,
        changeStrategy: typing.Union[changeStrategy, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'ContextMenuEntry':
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
            mode=mode,
            scopes=scopes,
            ajax=ajax,
            group=group,
            permission=permission,
            toolpermission=toolpermission,
            isDirectory=isDirectory,
            showAsAction=showAsAction,
            multiple=multiple,
            changeStrategy=changeStrategy,
            _configuration=_configuration,
            **kwargs,
        )
