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
from agilicus_api.models.list_issuer_roots_response import ListIssuerRootsResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListIssuerRootsResponse(unittest.TestCase):
    """ListIssuerRootsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListIssuerRootsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_issuer_roots_response.ListIssuerRootsResponse()  # noqa: E501
        if include_optional :
            return ListIssuerRootsResponse(
                issuer_roots = [
                    agilicus_api.models.issuer.Issuer(
                        id = '123', 
                        issuer = '0', 
                        enabled = True, 
                        org_id = '0', 
                        theme_file_id = 'ASsdq23lsaSSf', 
                        upstream_redirect_uri = '0', 
                        managed_upstreams = [
                            agilicus_api.models.managed_upstream_identity_provider.ManagedUpstreamIdentityProvider(
                                name = '0', 
                                enabled = True, )
                            ], 
                        oidc_upstreams = [
                            agilicus_api.models.oidc_upstream_identity_provider.OIDCUpstreamIdentityProvider(
                                name = '0', 
                                icon = 'city-login', 
                                issuer = '0', 
                                client_id = '0', 
                                client_secret = '0', 
                                issuer_external_host = '0', 
                                username_key = '0', 
                                email_key = '0', 
                                email_verification_required = True, 
                                request_user_info = True, 
                                user_id_key = '0', 
                                auto_create_status = 'active', )
                            ], 
                        local_auth_upstreams = [
                            {"name":"upstreamname","issuer":"upstreamissuer","upstream_type":"local_auth","upstream_id":"id123"}
                            ], 
                        clients = [
                            agilicus_api.models.issuer_client.IssuerClient(
                                id = '123', 
                                issuer_id = '123', 
                                name = '0', 
                                secret = '0', 
                                application = '0', 
                                org_id = '0', 
                                restricted_organisations = ["org-1","org-2"], 
                                saml_metadata_file = '0', 
                                id_mapping = ["federated_claims.user_id"], 
                                saml_scopes = ["openid","profile","email","urn:agilicus:api:users:self","federated:id"], 
                                organisation_scope = 'here_only', 
                                redirects = [
                                    '0'
                                    ], 
                                mfa_challenge = 'user_preference', 
                                single_sign_on = 'never', 
                                attributes = [
                                    agilicus_api.models.authentication_attribute.AuthenticationAttribute(
                                        attribute_name = 'emailAddress', 
                                        internal_attribute_path = 'user.email', )
                                    ], )
                            ], 
                        upstream_group_mappings = [
                            agilicus_api.models.upstream_group_mapping.UpstreamGroupMapping(
                                metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                                spec = agilicus_api.models.upstream_group_mapping_spec.UpstreamGroupMappingSpec(
                                    upstream_issuer = 'https://login.microsoftonline.com/c945d377-ea94-4a7d-9c83-0615e7ff0022/v2.0', 
                                    org_id = 'asdfg123hjkl', 
                                    group_mappings = [
                                        agilicus_api.models.upstream_group_mapping_entry.UpstreamGroupMappingEntry(
                                            priority = 1, 
                                            upstream_group_name = 'Company Team (.*)', 
                                            upstream_name_is_a_guid = False, 
                                            agilicus_group_name = 'Agilicus {0}', 
                                            group_org_id = 'asdfg123hjkl', )
                                        ], 
                                    excluded_groups = [
                                        agilicus_api.models.upstream_group_excluded_entry.UpstreamGroupExcludedEntry(
                                            upstream_group_name = 'Admin*', 
                                            upstream_name_is_a_guid = False, )
                                        ], ), )
                            ], 
                        name_slug = 'a', 
                        saml_state_encryption_key = '0123456789', )
                    ], 
                limit = 56
            )
        else :
            return ListIssuerRootsResponse(
                limit = 56,
        )

    def testListIssuerRootsResponse(self):
        """Test ListIssuerRootsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
