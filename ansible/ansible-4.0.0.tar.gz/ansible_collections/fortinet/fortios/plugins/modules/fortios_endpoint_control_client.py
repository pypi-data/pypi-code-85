#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
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
module: fortios_endpoint_control_client
short_description: Configure endpoint control client lists in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify endpoint_control feature and client category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.0.0
version_added: "2.10"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

requirements:
    - ansible>=2.9.0
options:
    access_token:
        description:
            - Token-based authentication.
              Generated from GUI of Fortigate.
        type: str
        required: false
    enable_log:
        description:
            - Enable/Disable logging for task.
        type: bool
        required: false
        default: false
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root

    state:
        description:
            - Indicates whether to create or remove the object.
        type: str
        required: true
        choices:
            - present
            - absent
    endpoint_control_client:
        description:
            - Configure endpoint control client lists.
        default: null
        type: dict
        suboptions:
            ad_groups:
                description:
                    - Endpoint client AD logon groups.
                type: str
            ftcl_uid:
                description:
                    - Endpoint FortiClient UID.
                type: str
            id:
                description:
                    - Endpoint client ID.
                required: true
                type: int
            info:
                description:
                    - Endpoint client information.
                type: str
            src_ip:
                description:
                    - Endpoint client IP address.
                type: str
            src_mac:
                description:
                    - Endpoint client MAC address.
                type: str
'''

EXAMPLES = '''
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure endpoint control client lists.
    fortios_endpoint_control_client:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      endpoint_control_client:
        ad_groups: "<your_own_value>"
        ftcl_uid: "<your_own_value>"
        id:  "5"
        info: "<your_own_value>"
        src_ip: "<your_own_value>"
        src_mac: "<your_own_value>"

'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import FortiOSHandler
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_legacy_fortiosapi
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import schema_to_module_spec
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_schema_versioning
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG


def filter_endpoint_control_client_data(json):
    option_list = ['ad_groups', 'ftcl_uid', 'id',
                   'info', 'src_ip', 'src_mac']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for i, elem in enumerate(data):
            data[i] = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data


def endpoint_control_client(data, fos):
    vdom = data['vdom']

    state = data['state']

    endpoint_control_client_data = data['endpoint_control_client']
    filtered_data = underscore_to_hyphen(filter_endpoint_control_client_data(endpoint_control_client_data))

    if state == "present" or state is True:
        return fos.set('endpoint-control',
                       'client',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('endpoint-control',
                          'client',
                          mkey=filtered_data['id'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_endpoint_control(data, fos):

    if data['endpoint_control_client']:
        resp = endpoint_control_client(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('endpoint_control_client'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


versioned_schema = {
    "type": "list",
    "children": {
        "info": {
            "type": "string",
            "revisions": {
                "v6.0.11": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.0.5": True
            }
        },
        "ad_groups": {
            "type": "string",
            "revisions": {
                "v6.0.11": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.0.5": True
            }
        },
        "id": {
            "type": "integer",
            "revisions": {
                "v6.0.11": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.0.5": True
            }
        },
        "src_ip": {
            "type": "string",
            "revisions": {
                "v6.0.11": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.0.5": True
            }
        },
        "ftcl_uid": {
            "type": "string",
            "revisions": {
                "v6.0.11": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.0.5": True
            }
        },
        "src_mac": {
            "type": "string",
            "revisions": {
                "v6.0.11": True,
                "v6.0.0": True,
                "v6.2.3": True,
                "v6.0.5": True
            }
        }
    },
    "revisions": {
        "v6.0.11": True,
        "v6.0.0": True,
        "v6.2.3": True,
        "v6.0.5": True
    }
}


def main():
    module_spec = schema_to_module_spec(versioned_schema)
    mkeyname = 'id'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "enable_log": {"required": False, "type": bool},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "endpoint_control_client": {
            "required": False, "type": "dict", "default": None,
            "options": {
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["endpoint_control_client"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["endpoint_control_client"]['options'][attribute_name]['required'] = True

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        if 'enable_log' in module.params:
            connection.set_option('enable_log', module.params['enable_log'])
        else:
            connection.set_option('enable_log', False)
        fos = FortiOSHandler(connection, module, mkeyname)
        versions_check_result = check_schema_versioning(fos, versioned_schema, "endpoint_control_client")

        is_error, has_changed, result = fortios_endpoint_control(module.params, fos)

    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result['matched'] is False:
        module.warn("Ansible has detected version mismatch between FortOS system and your playbook, see more details by specifying option -vvv")

    if not is_error:
        if versions_check_result and versions_check_result['matched'] is False:
            module.exit_json(changed=has_changed, version_check_warning=versions_check_result, meta=result)
        else:
            module.exit_json(changed=has_changed, meta=result)
    else:
        if versions_check_result and versions_check_result['matched'] is False:
            module.fail_json(msg="Error in repo", version_check_warning=versions_check_result, meta=result)
        else:
            module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
