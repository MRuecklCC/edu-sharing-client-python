# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    The version of the OpenAPI document: 1.1
    Generated by: https://openapi-generator.tech
"""

from edu_sharing_client.api_client import ApiClient
from edu_sharing_client.api.sharingv1_api_endpoints.get_children1 import GetChildren1
from edu_sharing_client.api.sharingv1_api_endpoints.get_info import GetInfo


class SHARINGV1Api(
    GetChildren1,
    GetInfo,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
