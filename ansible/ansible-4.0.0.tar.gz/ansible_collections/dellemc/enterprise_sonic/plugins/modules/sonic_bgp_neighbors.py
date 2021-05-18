#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
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
The module file for sonic_bgp_neighbors
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_bgp_neighbors
version_added: 1.0.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies.
- Supports C(check_mode).
short_description: Configures BGP neighbors on devices running Enterprise SONiC
description:
  - This module provides configuration management of global BGP_NEIGHBORS parameters on devices running Enterprise SONiC.
  - bgp_as and vrf_name must be created on the device in advance.
author: Abirami N (@abirami-n)
options:
  config:
    description: Specifies the BGP neighbors related configuration.
    type: list
    elements: dict
    suboptions:
      bgp_as:
        description:
          - Specifies the BGP autonomous system (AS) number which is already configured on the device.
        type: str
        required: True
      vrf_name:
        description:
          - Specifies the VRF name which is already configured on the device.
        default: default
        type: str
      peer_group:
        description: Specifies the list of peer groups.
        type: list
        elements: dict
        suboptions:
          name:
            description: Name of the peer group.
            type: str
            required: True
          remote_as:
            description:
              - Remote AS of the BGP peer group to configure.
              - peer_as and peer_type are mutually exclusive.
            type: dict
            suboptions:
              peer_as:
                description:
                  - Specifies remote AS number.
                  - The range is from 1 to 4294967295.
                type: int
              peer_type:
                description:
                  - Specifies the type of BGP peer.
                type: str
                choices:
                  - internal
                  - external
          bfd:
            description:
              - Enables or disables BFD.
            type: bool
          advertisement_interval:
            description:
              - Specifies the minimum interval between sending BGP routing updates.
              - The range is from 0 to 600.
            type: int
          timers:
            description:
              - Specifies BGP peer group timer related configurations.
            type: dict
            suboptions:
              keepalive:
                description:
                  - Frequency with which the device sends keepalive messages to its peer, in seconds.
                  - The range is from 0 to 65535.
                type: int
              holdtime:
                description:
                  - Interval after not receiving a keepalive message that Enterprise SONiC declares a peer dead, in seconds.
                  - The range is from 0 to 65535.
                type: int
          capability:
            description:
              - Specifies capability attributes to this peer group.
            type: dict
            suboptions:
              dynamic:
                description:
                  - Enables or disables dynamic capability to this peer group.
                type: bool
              extended_nexthop:
                description:
                  - Enables or disables advertise extended next-hop capability to the peer.
                type: bool
          address_family:
            description:
              - Holds of list of address families associated to the peergroup.
            type: dict
            suboptions:
              afis:
                description:
                  - List of address families with afi, safi, activate and allowas-in parameters.
                  - afi and safi are required together.
                type: list
                elements: dict
                suboptions:
                  afi:
                    description:
                      - Holds afi mode.
                    type: str
                    choices:
                      - ipv4
                      - ipv6
                      - l2vpn
                  safi:
                    description:
                      - Holds safi mode.
                    type: str
                    choices:
                      - unicast
                      - evpn
                  activate:
                    description:
                      - Enable or disable activate.
                    type: bool
                  allowas_in:
                    description:
                      - Holds AS value.
                      - The origin and value are mutually exclusive.
                    type: dict
                    suboptions:
                      origin:
                        description:
                          - Set AS as the origin.
                        type: bool
                      value:
                        description:
                          - Holds AS number in the range 1-10.
                        type: int
      neighbors:
        description: Specifies BGP neighbor-related configurations.
        type: list
        elements: dict
        suboptions:
          neighbor:
            description:
              - Neighbor router address.
            type: str
            required: True
          remote_as:
            description:
              - Remote AS of the BGP neighbor to configure.
              - peer_as and peer_type are mutually exclusive.
            type: dict
            suboptions:
              peer_as:
                description:
                  - Specifies remote AS number.
                  - The range is from 1 to 4294967295.
                type: int
              peer_type:
                description:
                  - Specifies the type of BGP peer.
                type: str
                choices:
                  - internal
                  - external
          bfd:
            description:
              - Enables or disables BFD.
            type: bool
          advertisement_interval:
            description:
              - Specifies the minimum interval between sending BGP routing updates.
              - The range is from 0 to 600.
            type: int
          peer_group:
            description:
              - The name of the peer group that the neighbor is a member of.
            type: str
          timers:
            description:
              - Specifies BGP neighbor timer-related configurations.
            type: dict
            suboptions:
              keepalive:
                description:
                  - Frequency with which the device sends keepalive messages to its peer, in seconds.
                  - The range is from 0 to 65535.
                type: int
              holdtime:
                description:
                  - Interval after not receiving a keepalive message that SONiC declares a peer dead, in seconds.
                  - The range is from 0 to 65535.
                type: int
          capability:
            description:
              - Specifies capability attributes to this neighbor.
            type: dict
            suboptions:
              dynamic:
                description:
                  - Enables or disables dynamic capability to this neighbor.
                type: bool
              extended_nexthop:
                description:
                  - Enables or disables advertise extended next-hop capability to the peer.
                type: bool
  state:
    description:
      - Specifies the operation to be performed on the BGP process that is configured on the device.
      - In case of merged, the input configuration is merged with the existing BGP configuration on the device.
      - In case of deleted, the existing BGP configuration is removed from the device.
    default: merged
    type: str
    choices:
      - merged
      - deleted
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# neighbor interface Eth1/3
#!
#router bgp 11
# network import-check
# timers 60 180
# !
# neighbor 192.168.1.4
# !
# peer-group SP1
#  bfd
#  capability dynamic
# !
# peer-group SP2
# !
#
- name: Deletes all BGP neighbors
  dellemc.enterprise_sonic.sonic_bgp_neighbors:
    config:
    state: deleted

#
# After state:
# -------------
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
#!
#router bgp 11
# network import-check
# timers 60 180
# !
#
# Using merged
#
# Before state:
# ------------
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
#!
#router bgp 11
# network import-check
# timers 60 180
# !

- name: "Adds sonic_bgp_neighbors"
  dellemc.enterprise_sonic.sonic_bgp_neighbors:
    config:
     - bgp_as: 51
       vrf_name: VrfReg1
       peer_group:
         - name: SPINE
           bfd: true
           capability:
             dynamic: true
             extended_nexthop: true
           remote_as:
             peer_as: 4
           address_family:
             afis:
               - afi: ipv4
                 safi: unicast
                 activate: true
                 allowas_in:
                   origin: true
               - afi: ipv6
                 safi: unicast
                 activate: true
                 allowas_in:
                   value: 5
       neighbors:
         - neighbor: Eth1/3
           remote_as:
             peer_as: 10
           peer_group: SPINE
           advertisement_interval: 15
           timers:
             keepalive: 30
             holdtime: 15
           bfd: true
           capability:
             dynamic: true
             extended_nexthop: true
         - neighbor: 192.168.1.4
    state: merged
#
# After state:
# ------------
#!
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE
#  remote-as 4
#  bfd
#  capability dynamic
#  capability extended-nexthop
#  address-family ipv4 unicast
#   activate
#   allowas-in origin
#   send-community both
# !
#  address-family ipv6 unicast
#   activate
#   allowas-in 5
#   send-community both
# !
# neighbor interface Eth1/3
#  peer-group SPINE
#  remote-as 10
#  timers 15 30
#  advertisement-interval 15
#  bfd
#  capability extended-nexthop
#  capability dynamic
# !
# neighbor 192.168.1.4
#!
#router bgp 11
# network import-check
# timers 60 180
#
# Using deleted
#
# Before state:
# ------------
#!
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE
#  bfd
#  remote-as 4
# !
# neighbor interface Eth1/3
#  peer-group SPINE
#  remote-as 10
#  timers 15 30
#  advertisement-interval 15
#  bfd
#  capability extended-nexthop
#  capability dynamic
# !
# neighbor 192.168.1.4
#!
#router bgp 11
# network import-check
# timers 60 18
# !
# peer-group SP
# !
# neighbor interface Eth1/3
#
- name: "Deletes sonic_bgp_neighbors and peer-groups specific to vrfname"
  dellemc.enterprise_sonic.sonic_bgp_neighbors:
    config:
     - bgp_as: 51
       vrf_name: VrfReg1
    state: deleted

# After state:
# ------------
#!
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
#router bgp 11
# network import-check
# timers 60 18
# !
# peer-group SP
# !
# neighbor interface Eth1/3
#
# Using deleted
#
# Before state:
# -------------
#
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE
#  bfd
#  remote-as 4
# !
# neighbor interface Eth1/3
#  peer-group SPINE
#  remote-as 10
#  timers 15 30
#  advertisement-interval 15
#  bfd
#  capability extended-nexthop
#  capability dynamic
# !
# neighbor 192.168.1.4
# !

- name: "Deletes specific sonic_bgp_neighbors"
  dellemc.enterprise_sonic.sonic_bgp_neighbors:
    config:
     - bgp_as: 51
       vrf_name: VrfReg1
       peer_group:
         - name: SPINE
           bfd: true
           remote_as:
             peer_as: 4
       neighbors:
         - neighbor: Eth1/3
           remote_as:
             peer_as: 10
           peer_group: SPINE
           advertisement_interval: 15
           timers:
             keepalive: 30
             holdtime: 15
           bfd: true
           capability:
             dynamic: true
             extended_nexthop: true
         - neighbor: 192.168.1.4
    state: deleted
#
# After state:
# -------------
#
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE
# !
# neighbor interface Eth1/3
# !

"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned is always in the same format
    of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned is always in the same format
    of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.bgp_neighbors.bgp_neighbors import Bgp_neighborsArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.bgp_neighbors.bgp_neighbors import Bgp_neighbors


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=Bgp_neighborsArgs.argument_spec,
                           supports_check_mode=True)

    result = Bgp_neighbors(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
