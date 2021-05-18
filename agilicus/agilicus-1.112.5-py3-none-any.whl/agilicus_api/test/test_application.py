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
import datetime

import agilicus_api
from agilicus_api.models.application import Application  # noqa: E501
from agilicus_api.rest import ApiException

class TestApplication(unittest.TestCase):
    """Application unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Application
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.application.Application()  # noqa: E501
        if include_optional :
            return Application(
                created = '2015-07-07T15:49:51.230+02:00', 
                id = '123', 
                name = 'a', 
                description = '0', 
                category = '0', 
                image = '0', 
                image_username = '0', 
                image_password = '0', 
                image_credentials_type = 'basic_auth', 
                environments = [
                    agilicus_api.models.environment.Environment(
                        created = '2015-07-07T15:49:51.230+02:00', 
                        name = '0', 
                        maintenance_org_id = '0', 
                        domain_aliases = [
                            'a'
                            ], 
                        version_tag = '0', 
                        config_mount_path = '0', 
                        config_as_mount = '0', 
                        config_as_env = '0', 
                        secrets_mount_path = '0', 
                        secrets_as_mount = '0', 
                        secrets_as_env = '0', 
                        application_services = [
                            agilicus_api.models.application_service.ApplicationService(
                                id = '123', 
                                name = 'my-local-service', 
                                org_id = '0', 
                                hostname = 'db.example.com', 
                                ipv4_addresses = [
                                    '192.0.2.1'
                                    ], 
                                name_resolution = 'static', 
                                port = 56, 
                                protocol = 'tcp', 
                                assignments = [
                                    agilicus_api.models.application_service_assignment.ApplicationServiceAssignment(
                                        app_id = '0', 
                                        environment_name = '0', 
                                        org_id = '0', )
                                    ], 
                                updated = '2015-07-07T15:49:51.230+02:00', 
                                service_type = 'vpn', 
                                service_protocol_type = 'ip', 
                                tls_enabled = True, 
                                tls_verify = True, 
                                connector_id = '123', 
                                connection_uri = '0', 
                                stats = {"metadata":{"creation_time":"2020-07-07T15:40:46.010Z","collection_time":"2020-07-07T15:40:44.020Z","receipt_time":"2020-07-07T15:40:46.020Z"},"overall_status":"good"}, )
                            ], 
                        serverless_image = '0', 
                        status = agilicus_api.models.environment_status.EnvironmentStatus(
                            runtime_status = agilicus_api.models.runtime_status.RuntimeStatus(
                                overall_status = 'good', 
                                running_replicas = 2, 
                                error_message = 'CrashLoopBackoff', 
                                restarts = 5, 
                                cpu = 0.6, 
                                memory = 45.2, 
                                last_apply_time = '2002-10-02T10:00-05:00', 
                                running_image = 'cr.agilicus.com/applications/iomad:v1.13.0', 
                                running_hash = 'sha256:2fb759c1adfe40863b89a4076111af8f210e7342d2240f09b08fc445b357112e', 
                                org_id = '123', ), ), 
                        updated = '2015-07-07T15:49:51.230+02:00', 
                        application_configs = agilicus_api.models.application_config.ApplicationConfig(
                            authentication_config = agilicus_api.models.application_authentication_config.ApplicationAuthenticationConfig(
                                application_handles_authentication = False, 
                                session_secret = 'Gns5ZPCvXGjzrtB672HAxfoSQ0dmqriSgiQf6uEQSBU=', ), 
                            oidc_config = agilicus_api.models.oidc_proxy_config.OIDCProxyConfig(
                                headers = agilicus_api.models.oidc_proxy_header.OIDCProxyHeader(
                                    domain_substitution = agilicus_api.models.oidc_proxy_domain_substitution.OIDCProxyDomainSubstitution(
                                        standard_headers = agilicus_api.models.oidc_proxy_standard_header.OIDCProxyStandardHeader(
                                            location = True, 
                                            origin = True, 
                                            host = True, ), 
                                        other_headers = [
                                            agilicus_api.models.oidc_proxy_header_mapping.OIDCProxyHeaderMapping(
                                                name = 'Accept-Encoding', 
                                                value = '*', )
                                            ], ), 
                                    header_overrides = agilicus_api.models.oidc_proxy_header_override.OIDCProxyHeaderOverride(
                                        request = agilicus_api.models.oidc_proxy_header_user_config.OIDCProxyHeaderUserConfig(
                                            set = [
                                                agilicus_api.models.oidc_proxy_header_mapping.OIDCProxyHeaderMapping(
                                                    name = 'Accept-Encoding', 
                                                    value = '*', )
                                                ], 
                                            add = [
                                                agilicus_api.models.oidc_proxy_header_mapping.OIDCProxyHeaderMapping(
                                                    name = 'Accept-Encoding', 
                                                    value = '*', )
                                                ], 
                                            remove = [
                                                agilicus_api.models.oidc_proxy_header_name.OIDCProxyHeaderName(
                                                    name = '0', )
                                                ], ), 
                                        response = agilicus_api.models.oidc_proxy_header_user_config.OIDCProxyHeaderUserConfig(), ), ), 
                                domain_mapping = agilicus_api.models.oidc_proxy_domain_mapping.OIDCProxyDomainMapping(
                                    primary_external_name = 'app-1.cloud.egov.city', 
                                    primary_internal_name = 'app-1.internal', 
                                    other_mappings = [
                                        agilicus_api.models.oidc_proxy_domain_name_mapping.OIDCProxyDomainNameMapping(
                                            internal_name = 'local_test_app', 
                                            external_name = 'app-1', )
                                        ], ), 
                                auth = agilicus_api.models.oidc_auth_config.OIDCAuthConfig(
                                    auth_enabled = True, 
                                    client_id = 'admin-portal', 
                                    issuer = 'https://auth.cloud.egov.city', 
                                    logout_url = '/login/logout.cfm', 
                                    scopes = [
                                        agilicus_api.models.oidc_proxy_scope.OIDCProxyScope(
                                            name = 'urn:agilicus:app:app-1:owner', )
                                        ], 
                                    path_config = agilicus_api.models.oidc_auth_path_config.OIDCAuthPathConfig(
                                        included_paths = [{"path":"/login"}], 
                                        excluded_paths = [{"path":"/logout"}], ), ), 
                                content_manipulation = agilicus_api.models.oidc_proxy_content_manipulation.OIDCProxyContentManipulation(
                                    media_types = [
                                        agilicus_api.models.oidc_content_type.OIDCContentType(
                                            name = 'text/css', )
                                        ], ), 
                                upstream_config = agilicus_api.models.oidc_proxy_upstream_config.OIDCProxyUpstreamConfig(
                                    scheme = 'https', 
                                    hostname = 'httpbin.org', 
                                    port = 1, ), ), 
                            security = agilicus_api.models.application_security.ApplicationSecurity(
                                http = agilicus_api.models.http_security_settings.HTTPSecuritySettings(
                                    csp = agilicus_api.models.csp_settings.CSPSettings(
                                        enabled = True, 
                                        mode = 'enforce', 
                                        directives = [
                                            agilicus_api.models.csp_directive.CSPDirective(
                                                name = 'default-src', 
                                                values = [
                                                    'https:'
                                                    ], )
                                            ], ), 
                                    cors = agilicus_api.models.cors_settings.CORSSettings(
                                        enabled = True, 
                                        origin_matching = 'me', 
                                        allow_origins = [
                                            agilicus_api.models.cors_origin.CORSOrigin(
                                                exact = 'https://other-site.agilicus.cloud', )
                                            ], 
                                        allow_methods = [
                                            'POST'
                                            ], 
                                        allow_headers = [
                                            'Destination'
                                            ], 
                                        expose_headers = [
                                            'Location'
                                            ], 
                                        max_age_seconds = 3600, 
                                        allow_credentials = True, ), 
                                    hsts = agilicus_api.models.hsts_settings.HSTSSettings(
                                        enabled = True, 
                                        max_age_seconds = 63072000, 
                                        include_sub_domains = False, 
                                        preload = True, ), 
                                    xss_protection = agilicus_api.models.xss_settings.XSSSettings(
                                        enabled = True, 
                                        mode = 'block', 
                                        report_uri = 'https://my-site.agilicus.cloud/xss-reports', ), 
                                    certificate_transparency = agilicus_api.models.certificate_transparency_settings.CertificateTransparencySettings(
                                        enabled = True, 
                                        report_uri = 'https://my-site.agilicus.cloud/ct-reports', 
                                        enforce = True, 
                                        max_age_seconds = 63072000, ), ), ), ), 
                        name_slug = 'a', 
                        proxy_location = 'in_cloud', )
                    ], 
                org_id = '0', 
                contact_email = '0', 
                monitoring_config = agilicus_api.models.application_monitoring_config.ApplicationMonitoringConfig(
                    port = 1, 
                    path = '/metrics', ), 
                port = 56, 
                healthcheck_uri = '0', 
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
                assignments = [
                    agilicus_api.models.application_assignment.ApplicationAssignment(
                        id = '0', 
                        org_id = 'asd901laskbh', 
                        environment_name = 'production', 
                        application_name = 'Blogs', )
                    ], 
                owned = True, 
                maintained = True, 
                assigned = True, 
                published = 'no', 
                default_role_id = 'AcaSL40fs22l4Dr4XoAd5y', 
                default_role_name = 'owner', 
                icon_url = '0', 
                updated = '2015-07-07T15:49:51.230+02:00', 
                location = 'hosted', 
                service_account_id = '0', 
                service_account_required = True, 
                application_type = 'user_defined', 
                name_slug = 'a'
            )
        else :
            return Application(
                name = 'a',
                category = '0',
                org_id = '0',
        )

    def testApplication(self):
        """Test Application"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
