# coding: utf-8

"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.05.18
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import agilicus_api
from agilicus_api.models.list_auth_audits_response import ListAuthAuditsResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListAuthAuditsResponse(unittest.TestCase):
    """ListAuthAuditsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListAuthAuditsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_auth_audits_response.ListAuthAuditsResponse()  # noqa: E501
        if include_optional :
            return ListAuthAuditsResponse(
                auth_audits = [
                    agilicus_api.models.auth_audits.AuthAudits(
                        user_id = 'jjkkGmwB9oTJWDjIglTU', 
                        upstream_user_id = 'asvl2-1a1s-asdlk-3sl1', 
                        org_id = '2jkMGmwB9o7JW3jIglNZ', 
                        org_name = '2jkMGmwB9o7JW3jIglNZ', 
                        time = '2002-10-02T10:00-05:00', 
                        event = 'Timeout', 
                        source_ip = '192.0.2.1', 
                        token_id = 'XMYdZy7yAiudMDxQqgDwkY', 
                        trace_id = '00b893c9ec7c0089c3da65e7c9e2263a', 
                        session = '00b893c9ec7c0089c3da65e7c9e2263a', 
                        issuer = 'https://auth.cloud.egov.city', 
                        client_id = 'my-client-id-ABCD', 
                        application_name = 'app-1', 
                        login_org_id = 'Io7MGmwB9o7JW3jIg23B', 
                        login_org_name = 'Io7MGmwB9o7JW3jIg23B', 
                        upstream_idp = 'google', 
                        stage = 'Login', 
                        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) Chrome/83.0.4103.97 Safari/537.36', )
                    ], 
                limit = 56
            )
        else :
            return ListAuthAuditsResponse(
                limit = 56,
        )

    def testListAuthAuditsResponse(self):
        """Test ListAuthAuditsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
