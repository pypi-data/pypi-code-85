#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Mikhail Yohman (@FragmentedPacket) <mikhail.yohman@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: netbox_provider
short_description: Create, update or delete providers within Netbox
description:
  - Creates, updates or removes providers from Netbox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Mikhail Yohman (@FragmentedPacket)
requirements:
  - pynetbox
version_added: '0.1.0'
options:
  netbox_url:
    description:
      - URL of the Netbox instance resolvable by Ansible control host
    required: true
    type: str
  netbox_token:
    description:
      - The token created within Netbox to authorize API access
    required: true
    type: str
  data:
    type: dict
    description:
      - Defines the provider configuration
    suboptions:
      name:
        description:
          - The name of the provider
        required: false
        type: str
      asn:
        description:
          - The provider ASN
        required: false
        type: int
      account:
        description:
          - The account number of the provider
        required: false
        type: str
      portal_url:
        description:
          - The URL of the provider
        required: false
        type: str
      noc_contact:
        description:
          - The NOC contact of the provider
        required: false
        type: str
      admin_contact:
        description:
          - The admin contact of the provider
        required: false
        type: str
      comments:
        description:
          - Comments related to the provider
        required: false
        type: str
      tags:
        description:
          - Any tags that the device may need to be associated with
        required: false
        type: list
      custom_fields:
        description:
          - must exist in Netbox
        required: false
        type: dict
    required: true
  state:
    description:
      - Use C(present) or C(absent) for adding or removing.
    choices: [ absent, present ]
    default: present
    type: str
  query_params:
    description:
      - This can be used to override the specified values in ALLOWED_QUERY_PARAMS that is defined
      - in plugins/module_utils/netbox_utils.py and provides control to users on what may make
      - an object unique in their environment.
    required: false
    type: list
    elements: str
  validate_certs:
    description:
      - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    default: true
    type: raw
"""

EXAMPLES = r"""
- name: "Test Netbox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create provider within Netbox with only required information
      netbox_provider:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Provider
        state: present

    - name: Update provider with other fields
      netbox_provider:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Provider
          asn: 65001
          account: 200129104
          portal_url: http://provider.net
          noc_contact: noc@provider.net
          admin_contact: admin@provider.net
          comments: "BAD PROVIDER"
        state: present

    - name: Delete provider within netbox
      netbox_provider:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Provider
        state: absent
"""

RETURN = r"""
provider:
  description: Serialized object as created or already existent within Netbox
  returned: success (when I(state=present))
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxAnsibleModule,
    NETBOX_ARG_SPEC,
)
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_circuits import (
    NetboxCircuitsModule,
    NB_PROVIDERS,
)
from copy import deepcopy


def main():
    """
    Main entry point for module execution
    """
    argument_spec = deepcopy(NETBOX_ARG_SPEC)
    argument_spec.update(
        dict(
            data=dict(
                type="dict",
                required=True,
                options=dict(
                    name=dict(required=False, type="str"),
                    asn=dict(required=False, type="int"),
                    account=dict(required=False, type="str"),
                    portal_url=dict(required=False, type="str"),
                    noc_contact=dict(required=False, type="str"),
                    admin_contact=dict(required=False, type="str"),
                    comments=dict(required=False, type="str"),
                    tags=dict(required=False, type="list"),
                    custom_fields=dict(required=False, type="dict"),
                ),
            ),
        ),
    )

    required_if = [("state", "present", ["name"]), ("state", "absent", ["name"])]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_provider = NetboxCircuitsModule(module, NB_PROVIDERS)
    netbox_provider.run()


if __name__ == "__main__":  # pragma: no cover
    main()
