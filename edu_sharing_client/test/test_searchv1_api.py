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
from edu_sharing_client.api.searchv1_api import SEARCHV1Api  # noqa: E501
from edu_sharing_client import configuration, schemas, api_client

from . import ApiTestMixin


class TestSEARCHV1Api(ApiTestMixin, unittest.TestCase):
    """SEARCHV1Api unit test stubs"""
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = SEARCHV1Api(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_get_metdata(self):
        """Test case for get_metdata

        get nodes with metadata and collections  # noqa: E501
        """
        from edu_sharing_client.api.searchv1_api_endpoints import get_metdata as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_relevant_nodes(self):
        """Test case for get_relevant_nodes

        Get relevant nodes for the current user  # noqa: E501
        """
        from edu_sharing_client.api.searchv1_api_endpoints import get_relevant_nodes as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_load_save_search(self):
        """Test case for load_save_search

        Load a saved search query.  # noqa: E501
        """
        from edu_sharing_client.api.searchv1_api_endpoints import load_save_search as endpoint_module
        response_status = 200
        # TODO get response content working

    def test_save_search(self):
        """Test case for save_search

        Save a search query.  # noqa: E501
        """
        from edu_sharing_client.api.searchv1_api_endpoints import save_search as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_search(self):
        """Test case for search

        Perform queries based on metadata sets.  # noqa: E501
        """
        from edu_sharing_client.api.searchv1_api_endpoints import search as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_search_by_property(self):
        """Test case for search_by_property

        Search for custom properties with custom values  # noqa: E501
        """
        from edu_sharing_client.api.searchv1_api_endpoints import search_by_property as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_search_contributor(self):
        """Test case for search_contributor

        Search for contributors  # noqa: E501
        """
        from edu_sharing_client.api.searchv1_api_endpoints import search_contributor as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_search_facets(self):
        """Test case for search_facets

        Search in facets.  # noqa: E501
        """
        from edu_sharing_client.api.searchv1_api_endpoints import search_facets as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_search_fingerprint(self):
        """Test case for search_fingerprint

        Perform queries based on metadata sets.  # noqa: E501
        """
        from edu_sharing_client.api.searchv1_api_endpoints import search_fingerprint as endpoint_module
        response_status = 200
        # TODO get response content working
        pass


if __name__ == '__main__':
    unittest.main()