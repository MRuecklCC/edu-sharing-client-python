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
from edu_sharing_client.api.nodev1_api import NODEV1Api  # noqa: E501
from edu_sharing_client import configuration, schemas, api_client

from . import ApiTestMixin


class TestNODEV1Api(ApiTestMixin, unittest.TestCase):
    """NODEV1Api unit test stubs"""
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = NODEV1Api(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_add_aspects(self):
        """Test case for add_aspects

        Add aspect to node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import add_aspects as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_add_workflow_history(self):
        """Test case for add_workflow_history

        Add workflow.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import add_workflow_history as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_change_content(self):
        """Test case for change_content

        Change content of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import change_content as endpoint_module
        response_status = 200
        # TODO get response content working

    def test_change_content_as_text(self):
        """Test case for change_content_as_text

        Change content of node as text.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import change_content_as_text as endpoint_module
        response_status = 200
        # TODO get response content working

    def test_change_metadata(self):
        """Test case for change_metadata

        Change metadata of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import change_metadata as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_change_metadata_with_versioning(self):
        """Test case for change_metadata_with_versioning

        Change metadata of node (new version).  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import change_metadata_with_versioning as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_change_preview(self):
        """Test case for change_preview

        Change preview of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import change_preview as endpoint_module
        response_status = 200
        # TODO get response content working

    def test_change_template_metadata(self):
        """Test case for change_template_metadata

        Set the metadata template for this folder.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import change_template_metadata as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_create_child(self):
        """Test case for create_child

        Create a new child.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import create_child as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_create_child_by_copying(self):
        """Test case for create_child_by_copying

        Create a new child by copying.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import create_child_by_copying as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_create_child_by_moving(self):
        """Test case for create_child_by_moving

        Create a new child by moving.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import create_child_by_moving as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_create_fork_of_node(self):
        """Test case for create_fork_of_node

        Create a copy of a node by creating a forked version (variant).  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import create_fork_of_node as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_create_share(self):
        """Test case for create_share

        Create a share for a node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import create_share as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_delete(self):
        """Test case for delete

        Delete node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import delete as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_delete_preview(self):
        """Test case for delete_preview

        Delete preview of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import delete_preview as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_assocs(self):
        """Test case for get_assocs

        Get related nodes.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_assocs as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_children(self):
        """Test case for get_children

        Get children of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_children as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_metadata(self):
        """Test case for get_metadata

        Get metadata of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_metadata as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_nodes(self):
        """Test case for get_nodes

        Searching nodes.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_nodes as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_notify_list(self):
        """Test case for get_notify_list

        Get notifys (sharing history) of the node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_notify_list as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_parents(self):
        """Test case for get_parents

        Get parents of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_parents as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_permission(self):
        """Test case for get_permission

        Get all permission of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_permission as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_published_copies(self):
        """Test case for get_published_copies

        Publish  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_published_copies as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_shares(self):
        """Test case for get_shares

        Get shares of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_shares as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_template_metadata(self):
        """Test case for get_template_metadata

        Get the metadata template + status for this folder.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_template_metadata as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_text_content(self):
        """Test case for get_text_content

        Get the text content of a document.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_text_content as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_version_metadata(self):
        """Test case for get_version_metadata

        Get metadata of node version.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_version_metadata as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_versions(self):
        """Test case for get_versions

        Get all versions of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_versions as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_get_workflow_history(self):
        """Test case for get_workflow_history

        Get workflow history.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import get_workflow_history as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_has_permission(self):
        """Test case for has_permission

        Which permissions has user/group for node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import has_permission as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_import_node(self):
        """Test case for import_node

        Import node  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import import_node as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_islocked(self):
        """Test case for islocked

        locked status of a node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import islocked as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_prepare_usage(self):
        """Test case for prepare_usage

        create remote object and get properties.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import prepare_usage as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_publish_copy(self):
        """Test case for publish_copy

        Publish  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import publish_copy as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_remove_share(self):
        """Test case for remove_share

        Remove share of a node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import remove_share as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_report_node(self):
        """Test case for report_node

        Report the node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import report_node as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_revert_version(self):
        """Test case for revert_version

        Revert to node version.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import revert_version as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_set_owner(self):
        """Test case for set_owner

        Set owner of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import set_owner as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_set_permission(self):
        """Test case for set_permission

        Set local permissions of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import set_permission as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_set_property(self):
        """Test case for set_property

        Set single property of node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import set_property as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_store_x_api_data(self):
        """Test case for store_x_api_data

        Store xApi-Conform data for a given node  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import store_x_api_data as endpoint_module
        response_status = 200
        # TODO get response content working
        content_type = 'application/json'



    def test_unlock(self):
        """Test case for unlock

        unlock node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import unlock as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_update_share(self):
        """Test case for update_share

        update share of a node.  # noqa: E501
        """
        from edu_sharing_client.api.nodev1_api_endpoints import update_share as endpoint_module
        response_status = 200
        # TODO get response content working
        pass


if __name__ == '__main__':
    unittest.main()
