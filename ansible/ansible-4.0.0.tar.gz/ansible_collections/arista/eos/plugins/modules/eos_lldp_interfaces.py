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
The module file for eos_lldp_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: eos_lldp_interfaces
short_description: LLDP interfaces resource module
description:
- This module manages Link Layer Discovery Protocol (LLDP) attributes of interfaces
  on Arista EOS devices.
version_added: 1.0.0
author: Nathaniel Case (@Qalthos)
notes:
- Tested against Arista EOS 4.20.10M
- This module works with connection C(network_cli). See the L(EOS Platform Options,../network/user_guide/platform_eos.html).
options:
  config:
    description: A dictionary of LLDP interfaces options.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Full name of the interface (i.e. Ethernet1).
        type: str
      receive:
        description:
        - Enable/disable LLDP RX on an interface.
        type: bool
      transmit:
        description:
        - Enable/disable LLDP TX on an interface.
        type: bool
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the EOS device by
      executing the command B(show running-config | section ^interface).
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
    - overridden
    - deleted
    - parsed
    - gathered
    - rendered
    default: merged

"""
EXAMPLES = """
# Using merged
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    no lldp receive
# interface Ethernet2
#    no lldp transmit

- name: Merge provided configuration with running configuration
  arista.eos.eos_lldp_interfaces:
    config:
    - name: Ethernet1
      transmit: false
    - name: Ethernet2
      transmit: false
    state: merged

#
# ------------
# After state
# ------------
#
# veos#show run | section ^interface
# interface Ethernet1
#    no lldp transmit
#    no lldp receive
# interface Ethernet2
#    no lldp transmit


# Using replaced
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    no lldp receive
# interface Ethernet2
#    no lldp transmit

- name: Replace existing LLDP configuration of specified interfaces with provided
    configuration
  arista.eos.eos_lldp_interfaces:
    config:
    - name: Ethernet1
      transmit: false
    state: replaced

#
# ------------
# After state
# ------------
#
# veos#show run | section ^interface
# interface Ethernet1
#    no lldp transmit
# interface Ethernet2
#    no lldp transmit


# Using overridden
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    no lldp receive
# interface Ethernet2
#    no lldp transmit

- name: Override the LLDP configuration of all the interfaces with provided configuration
  arista.eos.eos_lldp_interfaces:
    config:
    - name: Ethernet1
      transmit: false
    state: overridden

#
# ------------
# After state
# ------------
#
# veos#show run | section ^interface
# interface Ethernet1
#    no lldp transmit
# interface Ethernet2


# Using deleted
#
#
# ------------
# Before state
# ------------
#
#
# veos#show run | section ^interface
# interface Ethernet1
#    no lldp receive
# interface Ethernet2
#    no lldp transmit

- name: Delete LLDP configuration of specified interfaces (or all interfaces if none
    are specified)
  arista.eos.eos_lldp_interfaces:
    state: deleted

#
# ------------
# After state
# ------------
#
# veos#show run | section ^interface
# interface Ethernet1
# interface Ethernet2

# using rendered:

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_lldp_interfaces:
    config:
    - name: Ethernet1
      transmit: false
    - name: Ethernet2
      transmit: false
    state: rendered

#
# ------------
# Output
# ------------
#
# interface Ethernet1
#    no lldp transmit
# interface Ethernet2
#    no lldp transmit

# Using parsed
# parsed.cfg

# interface Ethernet1
#    no lldp transmit
# interface Ethernet2
#    no lldp transmit


- name: Use parsed to convert native configs to structured data
  arista.eos.lldp_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# ------------
# Output
# ------------

#   parsed:
#     - name: Ethernet1
#       transmit: False
#     - name: Ethernet2
#       transmit: False

# Using gathered:

# native config:
# interface Ethernet1
#    no lldp transmit
# interface Ethernet2
#    no lldp transmit

- name: Gather lldp interfaces facts from the device
  arista.eos.lldp_interfaces:
    state: gathered

# ------------
# Output
# ------------

#   gathered:
#     - name: Ethernet1
#       transmit: False
#     - name: Ethernet2
#       transmit: False

"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['interface Ethernet1', 'no lldp transmit']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.arista.eos.plugins.module_utils.network.eos.argspec.lldp_interfaces.lldp_interfaces import (
    Lldp_interfacesArgs,
)
from ansible_collections.arista.eos.plugins.module_utils.network.eos.config.lldp_interfaces.lldp_interfaces import (
    Lldp_interfaces,
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
        argument_spec=Lldp_interfacesArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = Lldp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
