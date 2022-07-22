# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    The version of the OpenAPI document: 1.1
    Generated by: https://openapi-generator.tech
"""

from edu_sharing_client.api_client import ApiClient
from edu_sharing_client.api.networkv1_api_endpoints.add_service import AddService
from edu_sharing_client.api.networkv1_api_endpoints.get_repositories import GetRepositories
from edu_sharing_client.api.networkv1_api_endpoints.get_service import GetService
from edu_sharing_client.api.networkv1_api_endpoints.get_services import GetServices
from edu_sharing_client.api.networkv1_api_endpoints.update_service import UpdateService


class NETWORKV1Api(
    AddService,
    GetRepositories,
    GetService,
    GetServices,
    UpdateService,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass