# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    The version of the OpenAPI document: 1.1
    Generated by: https://openapi-generator.tech
"""

from edu_sharing_client.api_client import ApiClient
from edu_sharing_client.api.organizationv1_api_endpoints.create_organizations import CreateOrganizations
from edu_sharing_client.api.organizationv1_api_endpoints.delete_organizations import DeleteOrganizations
from edu_sharing_client.api.organizationv1_api_endpoints.get_organization import GetOrganization
from edu_sharing_client.api.organizationv1_api_endpoints.get_organizations import GetOrganizations
from edu_sharing_client.api.organizationv1_api_endpoints.remove_from_organization import RemoveFromOrganization


class ORGANIZATIONV1Api(
    CreateOrganizations,
    DeleteOrganizations,
    GetOrganization,
    GetOrganizations,
    RemoveFromOrganization,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
