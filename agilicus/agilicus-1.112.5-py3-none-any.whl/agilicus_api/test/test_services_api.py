# coding: utf-8

"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.05.14
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import agilicus_api
from agilicus_api.api.services_api import ServicesApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestServicesApi(unittest.TestCase):
    """ServicesApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.services_api.ServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_service(self):
        """Test case for create_service

        Create a Service  # noqa: E501
        """
        pass

    def test_delete_service(self):
        """Test case for delete_service

        Remove a Service  # noqa: E501
        """
        pass

    def test_get_service(self):
        """Test case for get_service

        Get a single Service  # noqa: E501
        """
        pass

    def test_list_services(self):
        """Test case for list_services

        Get a subset of the Services  # noqa: E501
        """
        pass

    def test_replace_service(self):
        """Test case for replace_service

        Create or update a Service.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
