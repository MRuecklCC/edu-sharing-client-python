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
from edu_sharing_client.api.statisticv1_api import STATISTICV1Api  # noqa: E501
from edu_sharing_client import configuration, schemas, api_client

from . import ApiTestMixin


class TestSTATISTICV1Api(ApiTestMixin, unittest.TestCase):
    """STATISTICV1Api unit test stubs"""
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = STATISTICV1Api(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_get(self):
        """Test case for get

        Get statistics of repository.  # noqa: E501
        """
        from edu_sharing_client.api.statisticv1_api_endpoints import get as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_get_global_statistics(self):
        """Test case for get_global_statistics

        Get stats.  # noqa: E501
        """
        from edu_sharing_client.api.statisticv1_api_endpoints import get_global_statistics as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_node_data(self):
        """Test case for get_node_data

        get the range of nodes which had tracked actions since a given timestamp  # noqa: E501
        """
        from edu_sharing_client.api.statisticv1_api_endpoints import get_node_data as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_nodes_altered_in_range(self):
        """Test case for get_nodes_altered_in_range

        get the range of nodes which had tracked actions since a given timestamp  # noqa: E501
        """
        from edu_sharing_client.api.statisticv1_api_endpoints import get_nodes_altered_in_range as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_statistics_node(self):
        """Test case for get_statistics_node

        get statistics for node actions  # noqa: E501
        """
        from edu_sharing_client.api.statisticv1_api_endpoints import get_statistics_node as endpoint_module
        response_status = 200
        # TODO get response content working

    def test_get_statistics_user(self):
        """Test case for get_statistics_user

        get statistics for user actions (login, logout)  # noqa: E501
        """
        from edu_sharing_client.api.statisticv1_api_endpoints import get_statistics_user as endpoint_module
        response_status = 200
        # TODO get response content working


if __name__ == '__main__':
    unittest.main()
