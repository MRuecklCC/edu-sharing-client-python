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
from edu_sharing_client.api.registerv1_api import REGISTERV1Api  # noqa: E501
from edu_sharing_client import configuration, schemas, api_client

from . import ApiTestMixin


class TestREGISTERV1Api(ApiTestMixin, unittest.TestCase):
    """REGISTERV1Api unit test stubs"""
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = REGISTERV1Api(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    def test_activate(self):
        """Test case for activate

        Activate a new user (by using a supplied key)  # noqa: E501
        """
        from edu_sharing_client.api.registerv1_api_endpoints import activate as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_mail_exists(self):
        """Test case for mail_exists

        Check if the given mail is already successfully registered  # noqa: E501
        """
        from edu_sharing_client.api.registerv1_api_endpoints import mail_exists as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_recover_password(self):
        """Test case for recover_password

        Send a mail to recover/reset password  # noqa: E501
        """
        from edu_sharing_client.api.registerv1_api_endpoints import recover_password as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_register(self):
        """Test case for register

        Register a new user  # noqa: E501
        """
        from edu_sharing_client.api.registerv1_api_endpoints import register as endpoint_module
        response_status = 200
        # TODO get response content working

    def test_resend_mail(self):
        """Test case for resend_mail

        Resend a registration mail for a given mail address  # noqa: E501
        """
        from edu_sharing_client.api.registerv1_api_endpoints import resend_mail as endpoint_module
        response_status = 200
        # TODO get response content working
        pass

    def test_reset_password(self):
        """Test case for reset_password

        Send a mail to recover/reset password  # noqa: E501
        """
        from edu_sharing_client.api.registerv1_api_endpoints import reset_password as endpoint_module
        response_status = 200
        # TODO get response content working
        pass


if __name__ == '__main__':
    unittest.main()
