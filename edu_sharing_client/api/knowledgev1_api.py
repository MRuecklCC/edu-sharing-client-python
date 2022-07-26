# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    The version of the OpenAPI document: 1.1
    Generated by: https://openapi-generator.tech
"""

from edu_sharing_client.api_client import ApiClient
from edu_sharing_client.api.knowledgev1_api_endpoints.get_analyzing_job_status import GetAnalyzingJobStatus
from edu_sharing_client.api.knowledgev1_api_endpoints.run_analyzing_job import RunAnalyzingJob


class KNOWLEDGEV1Api(
    GetAnalyzingJobStatus,
    RunAnalyzingJob,
    ApiClient,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
