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
from edu_sharing_client.api.collectionv1_api import COLLECTIONV1Api  # noqa: E501
from edu_sharing_client import configuration, schemas, api_client

from . import ApiTestMixin


class TestCOLLECTIONV1Api(ApiTestMixin, unittest.TestCase):
    """COLLECTIONV1Api unit test stubs"""
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = COLLECTIONV1Api(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_add_feedback_to_collection(self):
        """Test case for add_feedback_to_collection

        Post feedback to collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import add_feedback_to_collection as endpoint_module
        response_status = 200
        # TODO get response content working

    def test_add_to_collection(self):
        """Test case for add_to_collection

        Add a node to a collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import add_to_collection as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_change_icon_of_collection(self):
        """Test case for change_icon_of_collection

        Writes Preview Image of a collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import change_icon_of_collection as endpoint_module
        response_status = 200
        # TODO get response content working

    def test_create_collection(self):
        """Test case for create_collection

        Create a new collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import create_collection as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_delete_collection(self):
        """Test case for delete_collection

        Delete a collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import delete_collection as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_delete_from_collection(self):
        """Test case for delete_from_collection

        Delete a node from a collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import delete_from_collection as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_collection(self):
        """Test case for get_collection

        Get a collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import get_collection as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_collections_containing_proposals(self):
        """Test case for get_collections_containing_proposals

        Get all collections containing proposals with a given state (via search index)  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import get_collections_containing_proposals as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_collections_proposals(self):
        """Test case for get_collections_proposals

        Get proposed objects for collection (requires edit permissions on collection).  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import get_collections_proposals as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_collections_references(self):
        """Test case for get_collections_references

        Get references objects for collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import get_collections_references as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_collections_subcollections(self):
        """Test case for get_collections_subcollections

        Get child collections for collection (or root).  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import get_collections_subcollections as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_feedback_of_collection(self):
        """Test case for get_feedback_of_collection

        Get feedback of collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import get_feedback_of_collection as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_remove_icon_of_collection(self):
        """Test case for remove_icon_of_collection

        Deletes Preview Image of a collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import remove_icon_of_collection as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_search_collections(self):
        """Test case for search_collections

        Search collections.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import search_collections as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_set_collection_order(self):
        """Test case for set_collection_order

        Set order of nodes in a collection. In order to work as expected, provide a list of all nodes in this collection  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import set_collection_order as endpoint_module
        response_status = 200
        # TODO get response content working

    def test_set_pinned_collections(self):
        """Test case for set_pinned_collections

        Set pinned collections.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import set_pinned_collections as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_update_collection(self):
        """Test case for update_collection

        Update a collection.  # noqa: E501
        """
        from edu_sharing_client.api.collectionv1_api_endpoints import update_collection as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'




if __name__ == '__main__':
    unittest.main()
