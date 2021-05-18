#!/usr/bin/python
# -*- coding: utf-8 -*-
# © Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
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
The module file for sonic_tacacs_server
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_tacacs_server
version_added: 1.0.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies.
- Supports C(check_mode).
author: Niraimadaiselvam M (@niraimadaiselvamm)
short_description: Configures tacacs server settings on Enterprise SONiC
description:
  - This module provides configuration management of tacacs server parameters on devices running Enterprise SONiC.
options:
  config:
    description:
      - Specifies the tacacs server related configuration.
    type: dict
    suboptions:
      auth_type:
        description:
          - Specifies the authentication type of the tacacs server.
        type: str
        choices:
          - pap
          - chap
          - mschap
          - login
        default: pap
      key:
        description:
          - Specifies the key of the tacacs server.
        type: str
      timeout:
        description:
          - Specifies the timeout of the tacacs server.
        type: int
      source_interface:
        description:
          - Specifies the source interface of the tacacs server.
        type: str
      servers:
        description:
          - Specifies the servers list of the tacacs server.
        type: dict
        suboptions:
          host:
            description:
              - Specifies the host details of the tacacs servers list.
            type: list
            elements: dict
            suboptions:
              name:
                description:
                  - Specifies the name of the tacacs server host.
                type: str
              auth_type:
                description:
                  - Specifies the authentication type of the tacacs server host.
                type: str
                choices:
                  - pap
                  - chap
                  - mschap
                  - login
                default: pap
              key:
                description:
                  - Specifies the key of the tacacs server host.
                type: str
              priority:
                description:
                  - Specifies the priority of the tacacs server host.
                type: int
                default: 1
              port:
                description:
                  - Specifies the port of the tacacs server host.
                type: int
                default: 49
              timeout:
                description:
                  - Specifies the timeout of the tacacs server host.
                type: int
                default: 5
              vrf:
                description:
                  - Specifies the vrf of the tacacs server host.
                type: str
                default: default
  state:
    description:
      - Specifies the operation to be performed on the tacacs server configured on the device.
      - In case of merged, the input mode configuration will be merged with the existing tacacs server configuration on the device.
      - In case of deleted the existing tacacs server mode configuration will be removed from the device.
    default: merged
    choices: ['merged', 'deleted']
    type: str
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#
# do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#source-interface  : Ethernet12
#timeout    : 10
#auth-type  : login
#key        : login
#------------------------------------------------------------------------------------------------
#HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
#------------------------------------------------------------------------------------------------
#1.2.3.4              pap             *****      50         2          10         mgmt
#localhost            pap                        49         1          5          default
#

- name: Merge tacacs configurations
  dellemc.enterprise_sonic.sonic_tacacs_server:
    config:
      auth_type: login
      key: login
      source_interface: Ethernet 12
      timeout: 10
      servers:
        host:
          - name: 1.2.3.4
    state: deleted

# After state:
# ------------
#
#do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#timeout    : 5
#auth-type  : pap
#------------------------------------------------------------------------------------------------
#HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
#------------------------------------------------------------------------------------------------
#localhost            pap                        49         1          5          default


# Using deleted
#
# Before state:
# -------------
#
# do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#source-interface  : Ethernet12
#timeout    : 10
#auth-type  : login
#key        : login
#------------------------------------------------------------------------------------------------
#HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
#------------------------------------------------------------------------------------------------
#1.2.3.4              pap             *****      50         2          10         mgmt
#localhost            pap                        49         1          5          default
#

- name: Merge tacacs configurations
  dellemc.enterprise_sonic.sonic_tacacs_server:
    config:
    state: deleted

# After state:
# ------------
#
#do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#timeout    : 5
#auth-type  : pap


# Using merged
#
# Before state:
# -------------
#
#sonic(config)# do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#
- name: Merge tacacs configurations
  dellemc.enterprise_sonic.sonic_tacacs_server:
    config:
      auth_type: pap
      key: pap
      source_interface: Ethernet 12
      timeout: 10
      servers:
        host:
          - name: 1.2.3.4
            auth_type: pap
            key: 1234
    state: merged

# After state:
# ------------
#
#sonic(config)# do show tacacs-server
#---------------------------------------------------------
#TACACS Global Configuration
#---------------------------------------------------------
#source-interface  : Ethernet12
#timeout    : 10
#auth-type  : pap
#key        : pap
#------------------------------------------------------------------------------------------------
#HOST                 AUTH-TYPE       KEY        PORT       PRIORITY   TIMEOUT    VRF
#------------------------------------------------------------------------------------------------
#1.2.3.4              pap             1234       49         1          5          default


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.tacacs_server.tacacs_server import Tacacs_serverArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.tacacs_server.tacacs_server import Tacacs_server


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Tacacs_serverArgs.argument_spec,
                           supports_check_mode=True)

    result = Tacacs_server(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
