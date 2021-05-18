#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for eos_lldp_global
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: eos_lldp_global
short_description: LLDP resource module
description:
- This module manages Global Link Layer Discovery Protocol (LLDP) settings on Arista
  EOS devices.
version_added: 1.0.0
author: Nathaniel Case (@Qalthos)
notes:
- Tested against Arista EOS 4.20.10M
- This module works with connection C(network_cli). See the L(EOS Platform Options,../network/user_guide/platform_eos.html).
options:
  config:
    description: The provided global LLDP configuration.
    type: dict
    suboptions:
      holdtime:
        description:
        - Specifies the holdtime (in sec) to be sent in packets.
        type: int
      reinit:
        description:
        - Specifies the delay (in sec) for LLDP initialization on any interface.
        type: int
      timer:
        description:
        - Specifies the rate at which LLDP packets are sent (in sec).
        type: int
      tlv_select:
        description:
        - Specifies the LLDP TLVs to enable or disable.
        type: dict
        suboptions:
          link_aggregation:
            description:
            - Enable or disable link aggregation TLV.
            type: bool
          management_address:
            description:
            - Enable or disable management address TLV.
            type: bool
          max_frame_size:
            description:
            - Enable or disable maximum frame size TLV.
            type: bool
          port_description:
            description:
            - Enable or disable port description TLV.
            type: bool
          system_capabilities:
            description:
            - Enable or disable system capabilities TLV.
            type: bool
          system_description:
            description:
            - Enable or disable system description TLV.
            type: bool
          system_name:
            description:
            - Enable or disable system name TLV.
            type: bool
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the EOS device by
      executing the command B(show running-config | section lldp).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
    - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - deleted
    - rendered
    - gathered
    - parsed
    default: merged

"""
EXAMPLES = """
# Using merged
#
# ------------
# Before State
# ------------
#
# veos# show run | section lldp
# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select system-description

- name: Merge provided LLDP configuration with the existing configuration
  arista.eos.eos_lldp_global:
    config:
      holdtime: 100
      tlv_select:
        management_address: false
        port_description: false
        system_description: true
    state: merged

# -----------
# After state
# -----------
#
# veos# show run | section lldp
# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select port-description


# Using replaced
#
# ------------
# Before State
# ------------
#
# veos# show run | section lldp
# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select system-description

- name: Replace existing LLDP device configuration with provided configuration
  arista.eos.eos_lldp_global:
    config:
      holdtime: 100
      tlv_select:
        management_address: false
        port_description: false
        system_description: true
    state: replaced

# -----------
# After state
# -----------
#
# veos# show run | section lldp
# lldp holdtime 100
# no lldp tlv-select management-address
# no lldp tlv-select port-description


# Using deleted
#
# ------------
# Before State
# ------------
#
# veos# show run | section lldp
# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select system-description

- name: Delete existing LLDP configurations from the device
  arista.eos.eos_lldp_global:
    state: deleted

# -----------
# After state
# -----------
#
# veos# show run | section ^lldp

# Using rendered:

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_lldp_global:
    config:
      holdtime: 100
      tlv_select:
        management_address: false
        port_description: false
        system_description: true
    state: rendered

# -----------
# Output
# -----------
#
# rendered:
#   - "lldp holdtime 100"
#   - "no lldp tlv-select management-address"
#   - "no lldp tlv-select port-description"

# Using parsed

# parsed.cfg

# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select system-description

- name: Use parsed to convert native configs to structured data
  arista.eos.lldp_global:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# -----------
# Output
# -----------

#    parsed:
#      holdtime: 100
#      timer 3000
#      reinit 5
#      tlv_select:
#        management_address: False
#        port_description: False
#        system_description: True

# Using gathered:
# native config:
# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select system-description


- name: Gather lldp_global facts from the device
  arista.eos.lldp_global:
    state: gathered

# -----------
# Output
# -----------

#    gathered:
#      holdtime: 100
#      timer 3000
#      reinit 5
#      tlv_select:
#        management_address: False
#        port_description: False
#        system_description: True

"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['lldp holdtime 100', 'no lldp timer', 'lldp tlv-select system-description']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.lldp_global.lldp_global import (
    Lldp_globalArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.lldp_global.lldp_global import (
    Lldp_global,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """

    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]
    module = AnsibleModule(
        argument_spec=Lldp_globalArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = Lldp_global(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
