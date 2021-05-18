#!/usr/bin/python
# Copyright (c) 2016 Hewlett-Packard Enterprise
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = '''
---
module: recordset
short_description: Manage OpenStack DNS recordsets
author: OpenStack Ansible SIG
description:
    - Manage OpenStack DNS recordsets. Recordsets can be created, deleted or
      updated. Only the I(records), I(description), and I(ttl) values
      can be updated.
options:
   zone:
     description:
        - Zone managing the recordset
     required: true
     type: str
   name:
     description:
        - Name of the recordset. It must be ended with name of dns zone.
     required: true
     type: str
   recordset_type:
     description:
        - Recordset type
        - Required when I(state=present).
     choices: ['a', 'aaaa', 'mx', 'cname', 'txt', 'ns', 'srv', 'ptr', 'caa']
     type: str
   records:
     description:
        - List of recordset definitions.
        - Required when I(state=present).
     type: list
     elements: str
   description:
     description:
        - Description of the recordset
     type: str
   ttl:
     description:
        -  TTL (Time To Live) value in seconds
     type: int
   state:
     description:
       - Should the resource be present or absent.
     choices: [present, absent]
     default: present
     type: str
requirements:
    - "python >= 3.6"
    - "openstacksdk"

extends_documentation_fragment:
- openstack.cloud.openstack
'''

EXAMPLES = '''
# Create a recordset named "www.example.net."
- openstack.cloud.recordset:
    cloud: mycloud
    state: present
    zone: example.net.
    name: www.example.net.
    recordset_type: "a"
    records: ['10.1.1.1']
    description: test recordset
    ttl: 3600

# Update the TTL on existing "www.example.net." recordset
- openstack.cloud.recordset:
    cloud: mycloud
    state: present
    zone: example.net.
    name: www.example.net.
    recordset_type: "a"
    records: ['10.1.1.1']
    ttl: 7200

# Delete recordset named "www.example.net."
- openstack.cloud.recordset:
    cloud: mycloud
    state: absent
    zone: example.net.
    name: www.example.net.
'''

RETURN = '''
recordset:
    description: Dictionary describing the recordset.
    returned: On success when I(state) is 'present'.
    type: complex
    contains:
        id:
            description: Unique recordset ID
            type: str
            sample: "c1c530a3-3619-46f3-b0f6-236927b2618c"
        name:
            description: Recordset name
            type: str
            sample: "www.example.net."
        zone_id:
            description: Zone id
            type: str
            sample: 9508e177-41d8-434e-962c-6fe6ca880af7
        type:
            description: Recordset type
            type: str
            sample: "A"
        description:
            description: Recordset description
            type: str
            sample: "Test description"
        ttl:
            description: Zone TTL value
            type: int
            sample: 3600
        records:
            description: Recordset records
            type: list
            sample: ['10.0.0.1']
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.openstack.cloud.plugins.module_utils.openstack import (openstack_full_argument_spec,
                                                                                openstack_module_kwargs,
                                                                                openstack_cloud_from_module)


def _system_state_change(state, records, description, ttl, recordset):
    if state == 'present':
        if recordset is None:
            return True
        if records is not None and recordset['records'] != records:
            return True
        if description is not None and recordset['description'] != description:
            return True
        if ttl is not None and recordset['ttl'] != ttl:
            return True
    if state == 'absent' and recordset:
        return True
    return False


def main():
    argument_spec = openstack_full_argument_spec(
        zone=dict(required=True),
        name=dict(required=True),
        recordset_type=dict(required=False, choices=['a', 'aaaa', 'mx', 'cname', 'txt', 'ns', 'srv', 'ptr', 'caa']),
        records=dict(required=False, type='list', elements='str'),
        description=dict(required=False, default=None),
        ttl=dict(required=False, type='int'),
        state=dict(default='present', choices=['absent', 'present']),
    )

    module_kwargs = openstack_module_kwargs()
    module = AnsibleModule(argument_spec,
                           required_if=[
                               ('state', 'present',
                                ['recordset_type', 'records'])],
                           supports_check_mode=True,
                           **module_kwargs)

    module.module_min_sdk_version = '0.28.0'
    zone = module.params.get('zone')
    name = module.params.get('name')
    state = module.params.get('state')

    sdk, cloud = openstack_cloud_from_module(module)
    recordsets = cloud.search_recordsets(zone, name_or_id=name)

    if recordsets:
        recordset = recordsets[0]
        try:
            recordset_id = recordset['id']
        except KeyError as e:
            module.fail_json(msg=str(e))
    else:
        # recordsets is filtered by type and should never be more than 1 return
        recordset = None

    if state == 'present':
        recordset_type = module.params.get('recordset_type').upper()
        records = module.params.get('records')
        description = module.params.get('description')
        ttl = module.params.get('ttl')

        kwargs = {}
        if description:
            kwargs['description'] = description
        kwargs['records'] = records

        if module.check_mode:
            module.exit_json(changed=_system_state_change(state,
                                                          records, description,
                                                          ttl, recordset))

        if recordset is None:
            if ttl:
                kwargs['ttl'] = ttl
            else:
                kwargs['ttl'] = 300

            recordset = cloud.create_recordset(
                zone=zone, name=name, recordset_type=recordset_type,
                **kwargs)
            changed = True
        else:

            if ttl:
                kwargs['ttl'] = ttl

            pre_update_recordset = recordset
            changed = _system_state_change(state, records,
                                           description, ttl,
                                           pre_update_recordset)
            if changed:
                recordset = cloud.update_recordset(
                    zone=zone, name_or_id=recordset_id, **kwargs)

        module.exit_json(changed=changed, recordset=recordset)

    elif state == 'absent':
        if module.check_mode:
            module.exit_json(changed=_system_state_change(state,
                                                          None, None,
                                                          None, recordset))

        if recordset is None:
            changed = False
        else:
            cloud.delete_recordset(zone, recordset_id)
            changed = True
        module.exit_json(changed=changed)


if __name__ == '__main__':
    main()
