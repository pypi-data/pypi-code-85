#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_webfilter_urlfilter
short_description: Configure URL filter lists.
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Frank Shen (@fshen01)
    - Hongbin Lu (@fgtdev-hblu)
notes:
    - Running in workspace locking mode is supported in this FortiManager module, the top
      level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
    - To create or update an object, use state present directive.
    - To delete an object, use state absent directive.
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded

options:
    bypass_validation:
        description: only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters
        required: false
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock for FortiManager running in workspace mode, the value can be global and others including root
        required: false
        type: str
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
        required: false
        type: int
        default: 300
    state:
        description: the directive to create, update or delete an object
        type: str
        required: true
        choices:
          - present
          - absent
    rc_succeeded:
        description: the rc codes list with which the conditions to succeed will be overriden
        type: list
        required: false
    rc_failed:
        description: the rc codes list with which the conditions to fail will be overriden
        type: list
        required: false
    adom:
        description: the parameter (adom) in requested url
        type: str
        required: true
    webfilter_urlfilter:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            comment:
                type: str
                description: 'Optional comments.'
            entries:
                description: no description
                type: list
                suboptions:
                    action:
                        type: str
                        description: 'Action to take for URL filter matches.'
                        choices:
                            - 'exempt'
                            - 'block'
                            - 'allow'
                            - 'monitor'
                            - 'pass'
                    dns-address-family:
                        type: str
                        description: 'Resolve IPv4 address, IPv6 address, or both from DNS server.'
                        choices:
                            - 'ipv4'
                            - 'ipv6'
                            - 'both'
                    exempt:
                        description: no description
                        type: list
                        choices:
                         - av
                         - web-content
                         - activex-java-cookie
                         - dlp
                         - fortiguard
                         - all
                         - filepattern
                         - pass
                         - range-block
                    id:
                        type: int
                        description: 'Id.'
                    referrer-host:
                        type: str
                        description: 'Referrer host name.'
                    status:
                        type: str
                        description: 'Enable/disable this URL filter.'
                        choices:
                            - 'disable'
                            - 'enable'
                    type:
                        type: str
                        description: 'Filter type (simple, regex, or wildcard).'
                        choices:
                            - 'simple'
                            - 'regex'
                            - 'wildcard'
                    url:
                        type: str
                        description: 'URL to be filtered.'
                    web-proxy-profile:
                        type: str
                        description: 'Web proxy profile.'
            id:
                type: int
                description: 'ID.'
            ip-addr-block:
                type: str
                description: 'Enable/disable blocking URLs when the hostname appears as an IP address.'
                choices:
                    - 'disable'
                    - 'enable'
            name:
                type: str
                description: 'Name of URL filter list.'
            one-arm-ips-urlfilter:
                type: str
                description: 'Enable/disable DNS resolver for one-arm IPS URL filter operation.'
                choices:
                    - 'disable'
                    - 'enable'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: Configure URL filter lists.
      fmgr_webfilter_urlfilter:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         state: <value in [present, absent]>
         webfilter_urlfilter:
            comment: <value of string>
            entries:
              -
                  action: <value in [exempt, block, allow, ...]>
                  dns-address-family: <value in [ipv4, ipv6, both]>
                  exempt:
                    - av
                    - web-content
                    - activex-java-cookie
                    - dlp
                    - fortiguard
                    - all
                    - filepattern
                    - pass
                    - range-block
                  id: <value of integer>
                  referrer-host: <value of string>
                  status: <value in [disable, enable]>
                  type: <value in [simple, regex, wildcard]>
                  url: <value of string>
                  web-proxy-profile: <value of string>
            id: <value of integer>
            ip-addr-block: <value in [disable, enable]>
            name: <value of string>
            one-arm-ips-urlfilter: <value in [disable, enable]>

'''

RETURN = '''
request_url:
    description: The full url requested
    returned: always
    type: str
    sample: /sys/login/user
response_code:
    description: The status of api request
    returned: always
    type: int
    sample: 0
response_message:
    description: The descriptive message of the api response
    type: str
    returned: always
    sample: OK.

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import NAPIManager
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_parameter_bypass


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/webfilter/urlfilter',
        '/pm/config/global/obj/webfilter/urlfilter'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/webfilter/urlfilter/{urlfilter}',
        '/pm/config/global/obj/webfilter/urlfilter/{urlfilter}'
    ]

    url_params = ['adom']
    module_primary_key = 'id'
    module_arg_spec = {
        'bypass_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'rc_succeeded': {
            'required': False,
            'type': 'list'
        },
        'rc_failed': {
            'required': False,
            'type': 'list'
        },
        'state': {
            'type': 'str',
            'required': True,
            'choices': [
                'present',
                'absent'
            ]
        },
        'adom': {
            'required': True,
            'type': 'str'
        },
        'webfilter_urlfilter': {
            'required': False,
            'type': 'dict',
            'options': {
                'comment': {
                    'required': False,
                    'type': 'str'
                },
                'entries': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'action': {
                            'required': False,
                            'choices': [
                                'exempt',
                                'block',
                                'allow',
                                'monitor',
                                'pass'
                            ],
                            'type': 'str'
                        },
                        'dns-address-family': {
                            'required': False,
                            'choices': [
                                'ipv4',
                                'ipv6',
                                'both'
                            ],
                            'type': 'str'
                        },
                        'exempt': {
                            'required': False,
                            'type': 'list',
                            'choices': [
                                'av',
                                'web-content',
                                'activex-java-cookie',
                                'dlp',
                                'fortiguard',
                                'all',
                                'filepattern',
                                'pass',
                                'range-block'
                            ]
                        },
                        'id': {
                            'required': False,
                            'type': 'int'
                        },
                        'referrer-host': {
                            'required': False,
                            'type': 'str'
                        },
                        'status': {
                            'required': False,
                            'choices': [
                                'disable',
                                'enable'
                            ],
                            'type': 'str'
                        },
                        'type': {
                            'required': False,
                            'choices': [
                                'simple',
                                'regex',
                                'wildcard'
                            ],
                            'type': 'str'
                        },
                        'url': {
                            'required': False,
                            'type': 'str'
                        },
                        'web-proxy-profile': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'id': {
                    'required': True,
                    'type': 'int'
                },
                'ip-addr-block': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'name': {
                    'required': False,
                    'type': 'str'
                },
                'one-arm-ips-urlfilter': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'webfilter_urlfilter'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.validate_parameters(params_validation_blob)
        fmgr.process_curd()
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
