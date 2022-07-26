# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    The version of the OpenAPI document: 1.1
    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import edu_sharing_client
from edu_sharing_client.api.about_api import ABOUTApi  # noqa: E501
from edu_sharing_client import configuration, schemas, api_client

from . import ApiTestMixin


class TestABOUTApi(ApiTestMixin, unittest.TestCase):
    """ABOUTApi unit test stubs"""
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = ABOUTApi(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_about(self):
        """Test case for about

        Discover the API.  # noqa: E501
        """
        from edu_sharing_client.api.about_api_endpoints import about as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_status(self):
        """Test case for status

        status of repo services  # noqa: E501
        """
        from edu_sharing_client.api.about_api_endpoints import status as endpoint_module
        response_status = 200
        # TODO get response content working
        pass


if __name__ == '__main__':
    unittest.main()
