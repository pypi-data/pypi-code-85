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
module: fortios_system_vdom_exception
short_description: Global configuration objects that can be configured independently for all VDOMs or for the defined VDOM scope in Fortinet's FortiOS and
   FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system feature and vdom_exception category.
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
    system_vdom_exception:
        description:
            - Global configuration objects that can be configured independently for all VDOMs or for the defined VDOM scope.
        default: null
        type: dict
        suboptions:
            id:
                description:
                    - Index <1-4096>.
                required: true
                type: int
            object:
                description:
                    - Name of the configuration object that can be configured independently for all VDOMs.
                type: str
                choices:
                    - log.fortianalyzer.setting
                    - log.fortianalyzer.override-setting
                    - log.fortianalyzer2.setting
                    - log.fortianalyzer2.override-setting
                    - log.fortianalyzer3.setting
                    - log.fortianalyzer3.override-setting
                    - system.central-management
                    - system.csf
                    - user.radius
                    - log.fortianalyzer-cloud.setting
                    - log.fortianalyzer-cloud.override-setting
                    - log.syslogd.setting
                    - log.syslogd.override-setting
                    - log.syslogd2.setting
                    - log.syslogd2.override-setting
                    - log.syslogd3.setting
                    - log.syslogd3.override-setting
                    - log.syslogd4.setting
                    - log.syslogd4.override-setting
            oid:
                description:
                    - Object ID.
                type: int
            scope:
                description:
                    - Determine whether the configuration object can be configured separately for all VDOMs or if some VDOMs share the same configuration.
                type: str
                choices:
                    - all
                    - inclusive
                    - exclusive
            vdom:
                description:
                    - Names of the VDOMs.
                type: list
                suboptions:
                    name:
                        description:
                            - VDOM name. Source system.vdom.name.
                        required: true
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
  - name: Global configuration objects that can be configured independently for all VDOMs or for the defined VDOM scope.
    fortios_system_vdom_exception:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_vdom_exception:
        id:  "3"
        object: "log.fortianalyzer.setting"
        oid: "5"
        scope: "all"
        vdom:
         -
            name: "default_name_8 (source system.vdom.name)"

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


def filter_system_vdom_exception_data(json):
    option_list = ['id', 'object', 'oid',
                   'scope', 'vdom']
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


def system_vdom_exception(data, fos):
    vdom = data['vdom']

    state = data['state']

    system_vdom_exception_data = data['system_vdom_exception']
    filtered_data = underscore_to_hyphen(filter_system_vdom_exception_data(system_vdom_exception_data))

    if state == "present" or state is True:
        return fos.set('system',
                       'vdom-exception',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('system',
                          'vdom-exception',
                          mkey=filtered_data['id'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos):

    if data['system_vdom_exception']:
        resp = system_vdom_exception(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('system_vdom_exception'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


versioned_schema = {
    "type": "list",
    "children": {
        "vdom": {
            "type": "list",
            "children": {
                "name": {
                    "type": "string",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": True,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                }
            },
            "revisions": {
                "v6.0.0": True,
                "v6.0.5": True,
                "v6.4.4": True,
                "v6.4.0": True,
                "v6.4.1": True,
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.2.5": True,
                "v6.2.7": True,
                "v6.0.11": True
            }
        },
        "scope": {
            "type": "string",
            "options": [
                {
                    "value": "all",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": True,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "inclusive",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": True,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "exclusive",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": True,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                }
            ],
            "revisions": {
                "v6.0.0": True,
                "v6.0.5": True,
                "v6.4.4": True,
                "v6.4.0": True,
                "v6.4.1": True,
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.2.5": True,
                "v6.2.7": True,
                "v6.0.11": True
            }
        },
        "oid": {
            "type": "integer",
            "revisions": {
                "v6.0.0": True,
                "v6.0.5": True,
                "v6.4.4": False,
                "v6.4.0": False,
                "v6.4.1": False,
                "v6.2.0": False,
                "v6.2.3": True,
                "v6.2.5": False,
                "v6.2.7": False,
                "v6.0.11": True
            }
        },
        "id": {
            "type": "integer",
            "revisions": {
                "v6.0.0": True,
                "v6.0.5": True,
                "v6.4.4": True,
                "v6.4.0": True,
                "v6.4.1": True,
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.2.5": True,
                "v6.2.7": True,
                "v6.0.11": True
            }
        },
        "object": {
            "type": "string",
            "options": [
                {
                    "value": "log.fortianalyzer.setting",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": True,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "log.fortianalyzer.override-setting",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": True,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "log.fortianalyzer2.setting",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": False,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "log.fortianalyzer2.override-setting",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": False,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "log.fortianalyzer3.setting",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": False,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "log.fortianalyzer3.override-setting",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": False,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "system.central-management",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": False,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "system.csf",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": False,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "user.radius",
                    "revisions": {
                        "v6.0.0": True,
                        "v6.0.5": False,
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True,
                        "v6.0.11": True
                    }
                },
                {
                    "value": "log.fortianalyzer-cloud.setting",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True
                    }
                },
                {
                    "value": "log.fortianalyzer-cloud.override-setting",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True,
                        "v6.2.0": True,
                        "v6.2.3": True,
                        "v6.2.5": True,
                        "v6.2.7": True
                    }
                },
                {
                    "value": "log.syslogd.setting",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "log.syslogd.override-setting",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "log.syslogd2.setting",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "log.syslogd2.override-setting",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "log.syslogd3.setting",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "log.syslogd3.override-setting",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "log.syslogd4.setting",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                },
                {
                    "value": "log.syslogd4.override-setting",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True,
                        "v6.4.1": True
                    }
                }
            ],
            "revisions": {
                "v6.0.0": True,
                "v6.0.5": True,
                "v6.4.4": True,
                "v6.4.0": True,
                "v6.4.1": True,
                "v6.2.0": True,
                "v6.2.3": True,
                "v6.2.5": True,
                "v6.2.7": True,
                "v6.0.11": True
            }
        }
    },
    "revisions": {
        "v6.0.0": True,
        "v6.0.5": True,
        "v6.4.4": True,
        "v6.4.0": True,
        "v6.4.1": True,
        "v6.2.0": True,
        "v6.2.3": True,
        "v6.2.5": True,
        "v6.2.7": True,
        "v6.0.11": True
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
        "system_vdom_exception": {
            "required": False, "type": "dict", "default": None,
            "options": {
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["system_vdom_exception"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["system_vdom_exception"]['options'][attribute_name]['required'] = True

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
        versions_check_result = check_schema_versioning(fos, versioned_schema, "system_vdom_exception")

        is_error, has_changed, result = fortios_system(module.params, fos)

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
