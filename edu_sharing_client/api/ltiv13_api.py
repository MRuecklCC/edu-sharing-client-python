# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    The version of the OpenAPI document: 1.1
    Generated by: https://openapi-generator.tech
"""

from edu_sharing_client.api_client import ApiClient
from edu_sharing_client.api.ltiv13_api_endpoints.generate_deep_linking_response import GenerateDeepLinkingResponse
from edu_sharing_client.api.ltiv13_api_endpoints.jwks_uri import JwksUri
from edu_sharing_client.api.ltiv13_api_endpoints.login_initiations import LoginInitiations
from edu_sharing_client.api.ltiv13_api_endpoints.lti import Lti
from edu_sharing_client.api.ltiv13_api_endpoints.lti_registration_dynamic import LtiRegistrationDynamic
from edu_sharing_client.api.ltiv13_api_endpoints.lti_registration_url import LtiRegistrationUrl
from edu_sharing_client.api.ltiv13_api_endpoints.lti_target import LtiTarget
from edu_sharing_client.api.ltiv13_api_endpoints.register_by_type import RegisterByType
from edu_sharing_client.api.ltiv13_api_endpoints.register_test import RegisterTest
from edu_sharing_client.api.ltiv13_api_endpoints.remove_lti_registration_url import RemoveLtiRegistrationUrl


class LTIV13Api(
    GenerateDeepLinkingResponse,
    JwksUri,
    LoginInitiations,
    Lti,
    LtiRegistrationDynamic,
    LtiRegistrationUrl,
    LtiTarget,
    RegisterByType,
    RegisterTest,
    RemoveLtiRegistrationUrl,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
