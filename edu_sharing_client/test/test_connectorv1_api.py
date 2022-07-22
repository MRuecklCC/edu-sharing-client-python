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
from edu_sharing_client.api.connectorv1_api import CONNECTORV1Api  # noqa: E501
from edu_sharing_client import configuration, schemas, api_client

from . import ApiTestMixin


class TestCONNECTORV1Api(ApiTestMixin, unittest.TestCase):
    """CONNECTORV1Api unit test stubs"""
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = CONNECTORV1Api(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_list_connectors(self):
        """Test case for list_connectors

        List all available connectors  # noqa: E501
        """
        from edu_sharing_client.api.connectorv1_api_endpoints import list_connectors as endpoint_module
        response_status = 200
        # TODO get response content working
        pass


if __name__ == '__main__':
    unittest.main()
