#!/usr/bin/python

# (c) 2021, NetApp, Inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = '''
module: na_ontap_disk_options
short_description: NetApp ONTAP modify storage disk options
extends_documentation_fragment:
    - netapp.ontap.netapp.na_ontap
version_added: '21.4.0'
author: NetApp Ansible Team (@carchi8py) <ng-ansibleteam@netapp.com>

description:
- Modify a nodes storage disk options
- Requires ONTAP 9.6 or greater
options:
  node:
    description:
    - The node to modify a disk option for
    required: true
    type: str

  bkg_firmware_update:
    description:
    - Whether or not background disk firmware updates should be enabled
    type: bool

  autocopy:
    description:
    - Whether or not disk auto copies should be enabled
    type: bool

  autoassign:
    description:
    - Whether or not disks should be automatically assigned to a node
    type: bool

  autoassign_policy:
    description:
    - the auto assign policy to use
    type: str
    choices: ['default', 'bay', 'shelf', 'stack']
    '''

EXAMPLES = """
    - name: Enable Disk Auto Assign
      na_ontap_disk_options:
        node: node1
        autoassign: true
        username: '{{ username }}'
        password: '{{ password }}'
        hostname: '{{ hostname }}'

    - name: Disable Disk Auto Assign
      na_ontap_disk_options:
        node: node1
        autoassign: false
        username: '{{ username }}'
        password: '{{ password }}'
        hostname: '{{ hostname }}'

"""

RETURN = """

"""

import traceback

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
import ansible_collections.netapp.ontap.plugins.module_utils.netapp as netapp_utils
from ansible_collections.netapp.ontap.plugins.module_utils.netapp_module import NetAppModule
from ansible_collections.netapp.ontap.plugins.module_utils.netapp import OntapRestAPI


class NetAppOntapDiskOptions():
    def __init__(self):

        self.argument_spec = netapp_utils.na_ontap_host_argument_spec()
        self.argument_spec.update(dict(
            node=dict(required=True, type='str'),
            bkg_firmware_update=dict(required=False, type='bool'),
            autocopy=dict(required=False, type='bool'),
            autoassign=dict(required=False, type='bool'),
            autoassign_policy=dict(required=False, type='str', choices=['default', 'bay', 'shelf', 'stack'])
        ))

        self.module = AnsibleModule(
            argument_spec=self.argument_spec,
            supports_check_mode=True
        )

        self.na_helper = NetAppModule()
        self.parameters = self.na_helper.set_parameters(self.module.params)

        self.rest_api = OntapRestAPI(self.module)
        self.use_rest = self.rest_api.is_rest()

        if not self.use_rest:
            self.module.fail_json(msg=self.rest_api.requires_ontap_version('na_ontap_disk_options', '9.6'))

    def get_disk_options(self):
        """
        Return a the current storage disk options for the node
        :return: a dict of storage disk options
        """
        return_value = None
        api = "private/cli/storage/disk/option"
        query = {
            'fields': 'node,autoassign,bkg-firmware-update,autocopy,autoassign-policy',
            'node': self.parameters['node']
        }
        message, error = self.rest_api.get(api, query)

        if error:
            self.module.fail_json(msg=error)
        if len(message.keys()) == 0:
            return None
        if 'records' in message and len(message['records']) == 0:
            return None
        if 'records' not in message:
            error = "Unexpected response in get_disk_options from %s: %s" % (api, repr(message))
            self.module.fail_json(msg=error)

        return_value = {
            'node': message['records'][0]['node'],
            'bkg_firmware_update': message['records'][0]['bkg_firmware_update'],
            'autocopy': message['records'][0]['autocopy'],
            'autoassign': message['records'][0]['autoassign'],
            'autoassign_policy': message['records'][0]['autoassign_policy']
        }
        return return_value

    def modify_disk_options(self, modify):
        """
        Modifies a nodes disk options
        :return: None
        """

        api = "private/cli/storage/disk/option"
        query = {
            'node': self.parameters['node']
        }

        dummy, error = self.rest_api.patch(api, modify, query)
        if error:
            self.module.fail_json(msg=error)

    def apply(self):

        current = self.get_disk_options()
        modify = self.na_helper.get_modified_attributes(current, self.parameters)

        if self.na_helper.changed and not self.module.check_mode:
            self.modify_disk_options(modify)

        self.module.exit_json(changed=self.na_helper.changed)


def main():
    """
    Execute action from playbook
    """
    command = NetAppOntapDiskOptions()
    command.apply()


if __name__ == '__main__':
    main()
