#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
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
The module file for junos_ospfv3
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: junos_ospfv3
short_description: OSPFv3 resource module
description:
- This module manages global OSPFv3 configuration on devices running Juniper JUNOS.
version_added: 1.2.0
author: Rohit Thakur (@rohitthakur2590)
requirements:
- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)
notes:
- This module requires the netconf system service be enabled on the device being managed.
- This module works with connection C(netconf). See L(the Junos OS Platform Options,../network/user_guide/platform_junos.html).
- Tested against JunOS v18.4R1
options:
  config:
    description: A list of OSPFv3 process configuration.
    type: list
    elements: dict
    suboptions:
      router_id:
        description:
        - The OSPFv3 router id.
        type: str
        required: true
      areas:
        description:
        - A list of OSPFv3 areas' configuration.
        type: list
        elements: dict
        suboptions:
          area_id:
            description:
            - The Area ID as an integer or IP Address.
            type: str
            required: true
          area_range:
            description:
            - Configure an address range for the area.
            type: str
          stub:
            description:
            - Settings for configuring the area as a stub.
            type: dict
            suboptions:
              default_metric:
                description:
                - Metric for the default route in this area.
                type: int
              set:
                description:
                - Configure the area as a stub.
                type: bool
          interfaces:
            description:
            - List of interfaces in this area.
            type: list
            elements: dict
            suboptions:
              authentication:
                description: Specify authentication type
                type: dict
                suboptions:
                  type:
                    description:
                    - Type of authentication to use.
                    type: dict
              bandwidth_based_metrics:
                description: Specify list of bandwidth based metrics
                type: list
                elements: dict
                suboptions:
                  bandwidth:
                    description:
                    - BW to apply metric to.
                    type: str
                    choices: [1g, 10g]
                  metric:
                    description: Specify metric
                    type: int
              name:
                description:
                - Name of the interface.
                type: str
                required: true
              priority:
                description:
                - Priority for the interface.
                type: int
              metric:
                description:
                - Metric applied to the interface.
                type: int
              flood_reduction:
                description:
                - Enable flood reduction.
                type: bool
              passive:
                description: Specify passive
                type: bool
              timers:
                description: Specify timers
                type: dict
                suboptions:
                  dead_interval:
                    description:
                    - Dead interval (seconds).
                    type: int
                  hello_interval:
                    description:
                    - Hello interval (seconds).
                    type: int
                  poll_interval:
                    description:
                    - Poll interval (seconds).
                    type: int
                  retransmit_interval:
                    description:
                    - Retransmit interval (seconds).
                    type: int
                  transit_delay:
                    description:
                    - Transit delay (seconds).
                    type: int
      external_preference:
        description:
        - Preference of external routes.
        type: int
      overload:
        description: Specify time for overload mode reset
        type: dict
        suboptions:
          timeout:
            description:
            - Time after which overload mode is reset (seconds).
            type: int
      preference:
        description:
        - Preference of internal routes.
        type: int
      prefix_export_limit:
        description:
        - Maximum number of external prefixes that can be exported.
        type: int
      reference_bandwidth:
        description:
        - Bandwidth for calculating metric defaults.
        type: str
        choices: [1g, 10g]
      rfc1583compatibility:
        description:
        - Set RFC1583 compatibility
        type: bool
      spf_options:
        description:
        - Configure options for SPF.
        type: dict
        suboptions:
          delay:
            description:
            - Time to wait before running an SPF (seconds).
            type: int
          holddown:
            description:
            - Time to hold down before running an SPF (seconds).
            type: int
          rapid_runs:
            description:
            - Number of maximum rapid SPF runs before holddown (seconds).
            type: int
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the Junos device
      by executing the command B(show protocols ospf.
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result
    type: str
  state:
    description:
    - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged
"""
EXAMPLES = """
# Using merged
#
# Before state
# ------------
#
# admin# show protocols ospf3

- name: Merge Junos OSPFv3 config
  junipernetworks.junos.junos_ospfv3:
    config:
    - router_id: 10.200.16.75
      areas:
        - area_id: 0.0.0.100
          stub:
            default_metric: 200
            set: true
          interfaces:
            - name: so-0/0/0.0
              priority: 3
              metric: 5
    state: merged

# After state
# -----------
#
# adimn# show protocols ospf3
# area 0.0.0.100 {
#     stub default-metric 200;
#     interface so-0/0/0.0 {
#         metric 5;
#         priority 3;
#     }
# }
# Using replaced
#
# Before state
# ------------
#
# adimn# show protocols ospf3
# area 0.0.0.100 {
#     stub default-metric 200;
#     interface so-0/0/0.0 {
#         metric 5;
#         priority 3;
#     }
# }
- name: Replace Junos OSPFv3 config
  junipernetworks.junos.junos_ospfv3:
   config:
     - router_id: 10.200.16.75
       areas:
         - area_id: 0.0.0.100
           interfaces:
             - name: so-0/0/0.0
   state: replaced

# After state
# -----------
#
# admin# show protocols ospf3
# area 0.0.0.100 {
#     interface so-0/0/0.0;
# }
# Using overridden
#
# Before state
# ------------
#
# admin# show protocols ospf3
# area 0.0.0.100 {
#     interface so-0/0/0.0;
# }
- name: Override Junos OSPFv3 config
  junipernetworks.junos.junos_ospfv3:
  config:
    - router_id: 10.200.16.75
      areas:
        - area_id: 0.0.0.100
          stub:
            default_metric: 200
            set: true
          interfaces:
            - name: so-0/0/0.0
              priority: 3
              metric: 5
              flood_reduction: true
              passive: true
        - area_id: 0.0.0.200
          interfaces:
            - name: ge-1/1/0.0
            - name: ge-2/2/0.0
  state: overridden

# After state
# -----------
#
# admin# show protocols ospf3
# area 0.0.0.100 {
#     stub default-metric 200;
#     interface so-0/0/0.0 {
#         passive;
#         metric 5;
#         priority 3;
#         flood-reduction;
#     }
# }
# area 0.0.0.200 {
#     interface ge-1/1/0.0;
#     interface ge-2/2/0.0;
# }
#
# Using deleted
#
# Before state
# ------------
#
# adimn# show protocols ospf3
# area 0.0.0.100 {
#     stub default-metric 200;
#     interface so-0/0/0.0 {
#         metric 5;
#         priority 3;
#     }
# }

- name: Delete Junos OSPFv3 config
  junipernetworks.junos.junos_ospfv3:
    config:
      - router_id: 10.200.16.75
        areas:
          - area_id: 0.0.0.100
            interfaces:
              - name: so-0/0/0.0
    state: deleted

# After state
# -----------
#
# admin# show protocols ospf3
# Using gathered
#
# Before state
# ------------
#
# adimn# show protocols ospf3
# area 0.0.0.100 {
#     stub default-metric 200;
#     interface so-0/0/0.0 {
#         passive;
#         metric 5;
#         priority 3;
#         flood-reduction;
#     }
# }
# area 0.0.0.200 {
#     interface ge-1/1/0.0;
#     interface ge-2/2/0.0;
# }

- name: Gather Junos OSPFv3 config
  junipernetworks.junos.junos_ospfv3:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": {
#             "areas": [
#                 {
#                     "area_id": "0.0.0.100",
#                     "interfaces": [
#                         {
#                             "flood_reduction": true,
#                             "metric": 5,
#                             "name": "so-0/0/0.0",
#                             "passive": true,
#                             "priority": 3
#                         }
#                     ],
#                     "stub": {
#                         "default_metric": 200,
#                         "set": true
#                     }
#                 },
#                 {
#                     "area_id": "0.0.0.200",
#                     "interfaces": [
#                         {
#                             "name": "ge-1/1/0.0"
#                         },
#                         {
#                             "name": "ge-2/2/0.0"
#                         }
#                     ]
#                 }
#             ],
#             "router_id": "10.200.16.75"
#         }
#
# Using rendered
#
#
- name: Render the commands for provided  configuration
  junipernetworks.junos.junos_ospfv3:
    config:
    - router_id: 10.200.16.75
      areas:
        - area_id: 0.0.0.100
          stub:
            default_metric: 200
            set: true
          interfaces:
            - name: so-0/0/0.0
              priority: 3
              metric: 5
              flood_reduction: true
              passive: true
        - area_id: 0.0.0.200
          interfaces:
            - name: ge-1/1/0.0
            - name: ge-2/2/0.0
    state: rendered

#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": "
# <nc:protocols
#     xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
#     <nc:ospf3>
#         <nc:area>
#             <nc:name>0.0.0.100</nc:name>
#             <nc:interface>
#                 <nc:name>so-0/0/0.0</nc:name>
#                 <nc:priority>3</nc:priority>
#                 <nc:flood-reduction/>
#                 <nc:metric>5</nc:metric>
#                 <nc:passive/>
#             </nc:interface>
#             <nc:stub>
#                 <nc:default-metric>200</nc:default-metric>
#             </nc:stub>
#         </nc:area>
#         <nc:area>
#             <nc:name>0.0.0.200</nc:name>
#             <nc:interface>
#                 <nc:name>ge-1/1/0.0</nc:name>
#             </nc:interface>
#             <nc:interface>
#                 <nc:name>ge-2/2/0.0</nc:name>
#             </nc:interface>
#         </nc:area>
#     </nc:ospf3>
# </nc:protocols>"
#
# Using parsed
# parsed.cfg
# ------------
# <rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:junos="http://xml.juniper.net/junos/18.4R1/junos">
# <data>
# <configuration xmlns="http://xml.juniper.net/xnm/1.1/xnm"
#      junos:commit-seconds="1601355317" junos:commit-localtime="2020-09-29 04:55:17 UTC" junos:commit-user="rohit">
#     <version>18.4R1-S2.4</version>
#     <interfaces>
#         <interface>
#             <name>ge-0/0/0</name>
#             <description>Configured by Ansi-Team</description>
#         </interface>
#         <interface>
#             <name>gr-0/0/0</name>
#             <description>Configured Manually</description>
#         </interface>
#         <interface>
#             <name>fxp0</name>
#             <unit>
#                 <name>0</name>
#                 <family>
#                     <inet>
#                         <dhcp>
#                         </dhcp>
#                     </inet>
#                 </family>
#             </unit>
#         </interface>
#     </interfaces>
#     <protocols>
#         <ospf3>
#             <area>
#                 <name>0.0.0.100</name>
#                 <stub>
#                     <default-metric>200</default-metric>
#                 </stub>
#                 <interface>
#                     <name>so-0/0/0.0</name>
#                     <passive>
#                     </passive>
#                     <metric>5</metric>
#                     <priority>3</priority>
#                     <flood-reduction/>
#                 </interface>
#             </area>
#             <area>
#                 <name>0.0.0.200</name>
#                 <interface>
#                     <name>ge-1/1/0.0</name>
#                 </interface>
#                 <interface>
#                     <name>ge-2/2/0.0</name>
#                 </interface>
#             </area>
#         </ospf3>
#     </protocols>
#     <routing-options>
#         <router-id>10.200.16.75</router-id>
#     </routing-options>
# </configuration>
# <database-status-information>
# <database-status>
# <user>rohit</user>
# <terminal>pts/0</terminal>
# <pid>38210</pid>
# <start-time junos:seconds="1601354977">2020-09-29 04:49:37 UTC</start-time>
# <idle-time junos:seconds="546">00:09:06</idle-time>
# <edit-path>[edit]</edit-path>
# </database-status>
# </database-status-information>
# </data>
# </rpc-reply>

- name: Parsed the device configuration to get output commands
  junipernetworks.junos.junos_ospfv3:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#         {
#             "areas": [
#                 {
#                     "area_id": "0.0.0.100",
#                     "interfaces": [
#                         {
#                             "flood_reduction": true,
#                             "metric": 5,
#                             "name": "so-0/0/0.0",
#                             "passive": true,
#                             "priority": 3
#                         }
#                     ],
#                     "stub": {
#                         "default_metric": 200,
#                         "set": true
#                     }
#                 },
#                 {
#                     "area_id": "0.0.0.200",
#                     "interfaces": [
#                         {
#                             "name": "ge-1/1/0.0"
#                         },
#                         {
#                             "name": "ge-2/2/0.0"
#                         }
#                     ]
#                 }
#             ],
#             "router_id": "10.200.16.75"
#         }
#     ]
#
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['<nc:protocols
    xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
    <nc:ospf3 delete=\"delete\"/>
    <nc:ospf3>
        <nc:area>
            <nc:name>0.0.0.100</nc:name>
            <nc:interface>
                <nc:name>so-0/0/0.0</nc:name>
                <nc:priority>3</nc:priority>
                <nc:flood-reduction/>
                <nc:metric>5</nc:metric>
                <nc:passive/>
            </nc:interface>
            <nc:stub>
                <nc:default-metric>200</nc:default-metric>
            </nc:stub>
        </nc:area>
        <nc:area>
            <nc:name>0.0.0.200</nc:name>
            <nc:interface>
                <nc:name>ge-1/1/0.0</nc:name>
            </nc:interface>
            <nc:interface>
                <nc:name>ge-2/2/0.0</nc:name>
            </nc:interface>
        </nc:area>
    </nc:ospf3>
</nc:protocols>",
        "
<nc:routing-options
    xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\">
    <nc:router-id delete=\"delete\"/>
    <nc:router-id>10.200.16.75</nc:router-id>
</nc:routing-options>', 'xml 2', 'xml 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.ospfv3.ospfv3 import (
    Ospfv3Args,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.ospfv3.ospfv3 import (
    Ospfv3,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    module = AnsibleModule(
        argument_spec=Ospfv3Args.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )
    result = Ospfv3(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
