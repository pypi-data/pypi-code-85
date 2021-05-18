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
module: fortios_extender_controller_dataplan
short_description: FortiExtender dataplan configuration in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify extender_controller feature and dataplan category.
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
    extender_controller_dataplan:
        description:
            - FortiExtender dataplan configuration.
        default: null
        type: dict
        suboptions:
            apn:
                description:
                    - APN configuration.
                type: str
            APN:
                description:
                    - APN configuration.
                type: str
            auth_type:
                description:
                    - Authentication type.
                type: str
                choices:
                    - none
                    - pap
                    - chap
            billing_date:
                description:
                    - Billing day of the month (1 - 31).
                type: int
            capacity:
                description:
                    - Capacity in MB (0 - 102400000).
                type: int
            carrier:
                description:
                    - Carrier configuration.
                type: str
            iccid:
                description:
                    - ICCID configuration.
                type: str
            modem_id:
                description:
                    - Dataplan"s modem specifics, if any.
                type: str
                choices:
                    - modem1
                    - modem2
                    - all
            monthly_fee:
                description:
                    - Monthly fee of dataplan (0 - 100000, in local currency).
                type: int
            name:
                description:
                    - FortiExtender dataplan name
                required: true
                type: str
            overage:
                description:
                    - Enable/disable dataplan overage detection.
                type: str
                choices:
                    - disable
                    - enable
            password:
                description:
                    - Password.
                type: str
            pdn:
                description:
                    - PDN type.
                type: str
                choices:
                    - ipv4-only
                    - ipv6-only
                    - ipv4-ipv6
            PDN:
                description:
                    - PDN type.
                type: str
                choices:
                    - ipv4-only
                    - ipv6-only
                    - ipv4-ipv6
            preferred_subnet:
                description:
                    - Preferred subnet mask (8 - 32).
                type: int
            private_network:
                description:
                    - Enable/disable dataplan private network support.
                type: str
                choices:
                    - disable
                    - enable
            signal_period:
                description:
                    - Signal period (600 to 18000 seconds).
                type: int
            signal_threshold:
                description:
                    - Signal threshold. Specify the range between 50 - 100, where 50/100 means -50/-100 dBm.
                type: int
            slot:
                description:
                    - SIM slot configuration.
                type: str
                choices:
                    - sim1
                    - sim2
            type:
                description:
                    - Type preferences configuration.
                type: str
                choices:
                    - carrier
                    - slot
                    - iccid
                    - generic
            username:
                description:
                    - Username.
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
  - name: FortiExtender dataplan configuration.
    fortios_extender_controller_dataplan:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      extender_controller_dataplan:
        apn: "<your_own_value>"
        APN: "<your_own_value>"
        auth_type: "none"
        billing_date: "6"
        capacity: "7"
        carrier: "<your_own_value>"
        iccid: "<your_own_value>"
        modem_id: "modem1"
        monthly_fee: "11"
        name: "default_name_12"
        overage: "disable"
        password: "<your_own_value>"
        pdn: "ipv4-only"
        PDN: "ipv4-only"
        preferred_subnet: "17"
        private_network: "disable"
        signal_period: "19"
        signal_threshold: "20"
        slot: "sim1"
        type: "carrier"
        username: "<your_own_value>"

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


def filter_extender_controller_dataplan_data(json):
    option_list = ['apn', 'APN', 'auth_type',
                   'billing_date', 'capacity', 'carrier',
                   'iccid', 'modem_id', 'monthly_fee',
                   'name', 'overage', 'password',
                   'pdn', 'PDN', 'preferred_subnet',
                   'private_network', 'signal_period', 'signal_threshold',
                   'slot', 'type', 'username']
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


def extender_controller_dataplan(data, fos):
    vdom = data['vdom']

    state = data['state']

    extender_controller_dataplan_data = data['extender_controller_dataplan']
    filtered_data = underscore_to_hyphen(filter_extender_controller_dataplan_data(extender_controller_dataplan_data))

    if state == "present" or state is True:
        return fos.set('extender-controller',
                       'dataplan',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('extender-controller',
                          'dataplan',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_extender_controller(data, fos):

    if data['extender_controller_dataplan']:
        resp = extender_controller_dataplan(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('extender_controller_dataplan'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


versioned_schema = {
    "type": "list",
    "children": {
        "slot": {
            "type": "string",
            "options": [
                {
                    "value": "sim1",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                },
                {
                    "value": "sim2",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                }
            ],
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "username": {
            "type": "string",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "capacity": {
            "type": "integer",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "name": {
            "type": "string",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "monthly_fee": {
            "type": "integer",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "type": {
            "type": "string",
            "options": [
                {
                    "value": "carrier",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                },
                {
                    "value": "slot",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                },
                {
                    "value": "iccid",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                },
                {
                    "value": "generic",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                }
            ],
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "pdn": {
            "type": "string",
            "options": [
                {
                    "value": "ipv4-only",
                    "revisions": {
                        "v6.4.4": True
                    }
                },
                {
                    "value": "ipv6-only",
                    "revisions": {
                        "v6.4.4": True
                    }
                },
                {
                    "value": "ipv4-ipv6",
                    "revisions": {
                        "v6.4.4": True
                    }
                }
            ],
            "revisions": {
                "v6.4.4": True
            }
        },
        "signal_threshold": {
            "type": "integer",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "auth_type": {
            "type": "string",
            "options": [
                {
                    "value": "none",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                },
                {
                    "value": "pap",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                },
                {
                    "value": "chap",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                }
            ],
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "overage": {
            "type": "string",
            "options": [
                {
                    "value": "disable",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                },
                {
                    "value": "enable",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                }
            ],
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "PDN": {
            "type": "string",
            "options": [
                {
                    "value": "ipv4-only",
                    "revisions": {
                        "v6.4.0": True
                    }
                },
                {
                    "value": "ipv6-only",
                    "revisions": {
                        "v6.4.0": True
                    }
                },
                {
                    "value": "ipv4-ipv6",
                    "revisions": {
                        "v6.4.0": True
                    }
                }
            ],
            "revisions": {
                "v6.4.4": False,
                "v6.4.0": True
            }
        },
        "carrier": {
            "type": "string",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "apn": {
            "type": "string",
            "revisions": {
                "v6.4.4": True
            }
        },
        "signal_period": {
            "type": "integer",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "APN": {
            "type": "string",
            "revisions": {
                "v6.4.4": False,
                "v6.4.0": True
            }
        },
        "iccid": {
            "type": "string",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "private_network": {
            "type": "string",
            "options": [
                {
                    "value": "disable",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                },
                {
                    "value": "enable",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                }
            ],
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "password": {
            "type": "string",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "billing_date": {
            "type": "integer",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "preferred_subnet": {
            "type": "integer",
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        },
        "modem_id": {
            "type": "string",
            "options": [
                {
                    "value": "modem1",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                },
                {
                    "value": "modem2",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                },
                {
                    "value": "all",
                    "revisions": {
                        "v6.4.4": True,
                        "v6.4.0": True
                    }
                }
            ],
            "revisions": {
                "v6.4.4": True,
                "v6.4.0": True
            }
        }
    },
    "revisions": {
        "v6.4.4": True,
        "v6.4.0": True
    }
}


def main():
    module_spec = schema_to_module_spec(versioned_schema)
    mkeyname = 'name'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "enable_log": {"required": False, "type": bool},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "extender_controller_dataplan": {
            "required": False, "type": "dict", "default": None,
            "options": {
            }
        }
    }
    for attribute_name in module_spec['options']:
        fields["extender_controller_dataplan"]['options'][attribute_name] = module_spec['options'][attribute_name]
        if mkeyname and mkeyname == attribute_name:
            fields["extender_controller_dataplan"]['options'][attribute_name]['required'] = True

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
        versions_check_result = check_schema_versioning(fos, versioned_schema, "extender_controller_dataplan")

        is_error, has_changed, result = fortios_extender_controller(module.params, fos)

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
