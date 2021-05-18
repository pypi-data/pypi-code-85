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
from agilicus_api.models.list_services_response import ListServicesResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListServicesResponse(unittest.TestCase):
    """ListServicesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListServicesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_services_response.ListServicesResponse()  # noqa: E501
        if include_optional :
            return ListServicesResponse(
                services = [
                    agilicus_api.models.service.Service(
                        created = '2015-07-07T15:49:51.230+02:00', 
                        id = '123', 
                        name = '0', 
                        description = '0', 
                        org_id = '0', 
                        contact_email = '0', 
                        roles = [
                            agilicus_api.models.role.Role(
                                name = '0', 
                                rules = [
                                    agilicus_api.models.rule.Rule(
                                        host = '0', 
                                        name = 'rules.add', 
                                        method = 'get', 
                                        path = '/.*', 
                                        query_parameters = [
                                            agilicus_api.models.rule_query_parameter.RuleQueryParameter(
                                                name = '0', 
                                                exact_match = '0', )
                                            ], 
                                        body = agilicus_api.models.rule_query_body.RuleQueryBody(
                                            json = [
                                                agilicus_api.models.rule_query_body_json.RuleQueryBodyJSON(
                                                    name = '0', 
                                                    exact_match = '0', 
                                                    match_type = 'string', 
                                                    pointer = '/foo/0/a~1b/2', )
                                                ], ), )
                                    ], )
                            ], 
                        definitions = [
                            agilicus_api.models.definition.Definition(
                                key = '0', 
                                value = '0', )
                            ], 
                        base_url = 'api.agilicus.com/v1', 
                        updated = '2015-07-07T15:49:51.230+02:00', )
                    ]
            )
        else :
            return ListServicesResponse(
        )

    def testListServicesResponse(self):
        """Test ListServicesResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
