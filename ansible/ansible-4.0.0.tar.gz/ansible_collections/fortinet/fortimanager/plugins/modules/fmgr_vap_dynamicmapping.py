#!/usr/bin/python
from __future__ import absolute_import, division, print_function
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
module: fmgr_vap_dynamicmapping
short_description: no description
description:
    - This module is able to configure a FortiManager device.
    - Examples include all parameters and values which need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Frank Shen (@fshen01)
    - Hongbin Lu (@fgtdev-hblu)
notes:
    - Running in workspace locking mode is supported in this FortiManager module, the top
      level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
    - To create or update an object, use state present directive.
    - To delete an object, use state absent directive.
    - Normally, running one module can fail when a non-zero rc is returned. you can also override
      the conditions to fail or succeed with parameters rc_failed and rc_succeeded

options:
    bypass_validation:
        description: only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters
        required: false
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock for FortiManager running in workspace mode, the value can be global and others including root
        required: false
        type: str
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
        required: false
        type: int
        default: 300
    state:
        description: the directive to create, update or delete an object
        type: str
        required: true
        choices:
          - present
          - absent
    rc_succeeded:
        description: the rc codes list with which the conditions to succeed will be overriden
        type: list
        required: false
    rc_failed:
        description: the rc codes list with which the conditions to fail will be overriden
        type: list
        required: false
    adom:
        description: the parameter (adom) in requested url
        type: str
        required: true
    vap:
        description: the parameter (vap) in requested url
        type: str
        required: true
    vap_dynamicmapping:
        description: the top level parameters set
        required: false
        type: dict
        suboptions:
            _centmgmt:
                type: str
                default: 'disable'
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            _dhcp_svr_id:
                type: str
                description: no description
            _intf_allowaccess:
                description: no description
                type: list
                choices:
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - fgfm
                 - auto-ipsec
                 - radius-acct
                 - probe-response
                 - capwap
            _intf_device-identification:
                type: str
                default: 'disable'
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            _intf_device-netscan:
                type: str
                default: 'disable'
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            _intf_dhcp-relay-ip:
                description: no description
                type: str
            _intf_dhcp-relay-service:
                type: str
                default: 'disable'
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            _intf_dhcp-relay-type:
                type: str
                default: 'regular'
                description: no description
                choices:
                    - 'regular'
                    - 'ipsec'
            _intf_dhcp6-relay-ip:
                type: str
                description: no description
            _intf_dhcp6-relay-service:
                type: str
                default: 'disable'
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            _intf_dhcp6-relay-type:
                type: str
                default: 'regular'
                description: no description
                choices:
                    - 'regular'
            _intf_ip:
                type: str
                description: no description
            _intf_ip6-address:
                type: str
                description: no description
            _intf_ip6-allowaccess:
                description: no description
                type: list
                choices:
                 - https
                 - ping
                 - ssh
                 - snmp
                 - http
                 - telnet
                 - any
                 - fgfm
                 - capwap
            _intf_listen-forticlient-connection:
                type: str
                default: 'disable'
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            _scope:
                description: no description
                type: list
                suboptions:
                    name:
                        type: str
                        description: no description
                    vdom:
                        type: str
                        description: no description
            acct-interim-interval:
                type: int
                description: no description
            address-group:
                type: str
                description: no description
            alias:
                type: str
                description: no description
            atf-weight:
                type: int
                description: no description
            auth:
                type: str
                description: no description
                choices:
                    - 'PSK'
                    - 'psk'
                    - 'RADIUS'
                    - 'radius'
                    - 'usergroup'
            broadcast-ssid:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            broadcast-suppression:
                description: no description
                type: list
                choices:
                 - dhcp
                 - arp
                 - dhcp2
                 - arp2
                 - netbios-ns
                 - netbios-ds
                 - arp3
                 - dhcp-up
                 - dhcp-down
                 - arp-known
                 - arp-unknown
                 - arp-reply
                 - ipv6
                 - dhcp-starvation
                 - arp-poison
                 - all-other-mc
                 - all-other-bc
                 - arp-proxy
                 - dhcp-ucast
            captive-portal-ac-name:
                type: str
                description: no description
            captive-portal-macauth-radius-secret:
                description: no description
                type: str
            captive-portal-macauth-radius-server:
                type: str
                description: no description
            captive-portal-radius-secret:
                description: no description
                type: str
            captive-portal-radius-server:
                type: str
                description: no description
            captive-portal-session-timeout-interval:
                type: int
                description: no description
            client-count:
                type: int
                description: no description
            dhcp-lease-time:
                type: int
                description: no description
            dhcp-option82-circuit-id-insertion:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'style-1'
                    - 'style-2'
            dhcp-option82-insertion:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            dhcp-option82-remote-id-insertion:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'style-1'
            dynamic-vlan:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            eap-reauth:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            eap-reauth-intv:
                type: int
                description: no description
            eapol-key-retries:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            encrypt:
                type: str
                description: no description
                choices:
                    - 'TKIP'
                    - 'AES'
                    - 'TKIP-AES'
            external-fast-roaming:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            external-logout:
                type: str
                description: no description
            external-web:
                type: str
                description: no description
            fast-bss-transition:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            fast-roaming:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            ft-mobility-domain:
                type: int
                description: no description
            ft-over-ds:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            ft-r0-key-lifetime:
                type: int
                description: no description
            gtk-rekey:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            gtk-rekey-intv:
                type: int
                description: no description
            hotspot20-profile:
                type: str
                description: no description
            intra-vap-privacy:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            ip:
                type: str
                description: no description
            key:
                description: no description
                type: str
            keyindex:
                type: int
                description: no description
            ldpc:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'tx'
                    - 'rx'
                    - 'rxtx'
            local-authentication:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            local-bridging:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            local-lan:
                type: str
                description: no description
                choices:
                    - 'deny'
                    - 'allow'
            local-standalone:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            local-standalone-nat:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            local-switching:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            mac-auth-bypass:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            mac-filter:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            mac-filter-policy-other:
                type: str
                description: no description
                choices:
                    - 'deny'
                    - 'allow'
            max-clients:
                type: int
                description: no description
            max-clients-ap:
                type: int
                description: no description
            me-disable-thresh:
                type: int
                description: no description
            mesh-backhaul:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            mpsk:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            mpsk-concurrent-clients:
                type: int
                description: no description
            multicast-enhance:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            multicast-rate:
                type: str
                description: no description
                choices:
                    - '0'
                    - '6000'
                    - '12000'
                    - '24000'
            okc:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            owe-groups:
                description: no description
                type: list
                choices:
                 - 19
                 - 20
                 - 21
            owe-transition:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            owe-transition-ssid:
                type: str
                description: no description
            passphrase:
                description: no description
                type: str
            pmf:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
                    - 'optional'
            pmf-assoc-comeback-timeout:
                type: int
                description: no description
            pmf-sa-query-retry-timeout:
                type: int
                description: no description
            portal-message-override-group:
                type: str
                description: no description
            portal-type:
                type: str
                description: no description
                choices:
                    - 'auth'
                    - 'auth+disclaimer'
                    - 'disclaimer'
                    - 'email-collect'
                    - 'cmcc'
                    - 'cmcc-macauth'
                    - 'auth-mac'
            probe-resp-suppression:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            probe-resp-threshold:
                type: str
                description: no description
            ptk-rekey:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            ptk-rekey-intv:
                type: int
                description: no description
            qos-profile:
                type: str
                description: no description
            quarantine:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            radio-2g-threshold:
                type: str
                description: no description
            radio-5g-threshold:
                type: str
                description: no description
            radio-sensitivity:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            radius-mac-auth:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            radius-mac-auth-server:
                type: str
                description: no description
            radius-mac-auth-usergroups:
                description: no description
                type: str
            radius-server:
                type: str
                description: no description
            rates-11a:
                description: no description
                type: list
                choices:
                 - 1
                 - 1-basic
                 - 2
                 - 2-basic
                 - 5.5
                 - 5.5-basic
                 - 6
                 - 6-basic
                 - 9
                 - 9-basic
                 - 12
                 - 12-basic
                 - 18
                 - 18-basic
                 - 24
                 - 24-basic
                 - 36
                 - 36-basic
                 - 48
                 - 48-basic
                 - 54
                 - 54-basic
                 - 11
                 - 11-basic
            rates-11ac-ss12:
                description: no description
                type: list
                choices:
                 - mcs0/1
                 - mcs1/1
                 - mcs2/1
                 - mcs3/1
                 - mcs4/1
                 - mcs5/1
                 - mcs6/1
                 - mcs7/1
                 - mcs8/1
                 - mcs9/1
                 - mcs0/2
                 - mcs1/2
                 - mcs2/2
                 - mcs3/2
                 - mcs4/2
                 - mcs5/2
                 - mcs6/2
                 - mcs7/2
                 - mcs8/2
                 - mcs9/2
                 - mcs10/1
                 - mcs11/1
                 - mcs10/2
                 - mcs11/2
            rates-11ac-ss34:
                description: no description
                type: list
                choices:
                 - mcs0/3
                 - mcs1/3
                 - mcs2/3
                 - mcs3/3
                 - mcs4/3
                 - mcs5/3
                 - mcs6/3
                 - mcs7/3
                 - mcs8/3
                 - mcs9/3
                 - mcs0/4
                 - mcs1/4
                 - mcs2/4
                 - mcs3/4
                 - mcs4/4
                 - mcs5/4
                 - mcs6/4
                 - mcs7/4
                 - mcs8/4
                 - mcs9/4
                 - mcs10/3
                 - mcs11/3
                 - mcs10/4
                 - mcs11/4
            rates-11bg:
                description: no description
                type: list
                choices:
                 - 1
                 - 1-basic
                 - 2
                 - 2-basic
                 - 5.5
                 - 5.5-basic
                 - 6
                 - 6-basic
                 - 9
                 - 9-basic
                 - 12
                 - 12-basic
                 - 18
                 - 18-basic
                 - 24
                 - 24-basic
                 - 36
                 - 36-basic
                 - 48
                 - 48-basic
                 - 54
                 - 54-basic
                 - 11
                 - 11-basic
            rates-11n-ss12:
                description: no description
                type: list
                choices:
                 - mcs0/1
                 - mcs1/1
                 - mcs2/1
                 - mcs3/1
                 - mcs4/1
                 - mcs5/1
                 - mcs6/1
                 - mcs7/1
                 - mcs8/2
                 - mcs9/2
                 - mcs10/2
                 - mcs11/2
                 - mcs12/2
                 - mcs13/2
                 - mcs14/2
                 - mcs15/2
            rates-11n-ss34:
                description: no description
                type: list
                choices:
                 - mcs16/3
                 - mcs17/3
                 - mcs18/3
                 - mcs19/3
                 - mcs20/3
                 - mcs21/3
                 - mcs22/3
                 - mcs23/3
                 - mcs24/4
                 - mcs25/4
                 - mcs26/4
                 - mcs27/4
                 - mcs28/4
                 - mcs29/4
                 - mcs30/4
                 - mcs31/4
            sae-groups:
                description: no description
                type: list
                choices:
                 - 1
                 - 2
                 - 5
                 - 14
                 - 15
                 - 16
                 - 17
                 - 18
                 - 19
                 - 20
                 - 21
                 - 27
                 - 28
                 - 29
                 - 30
                 - 31
            sae-password:
                description: no description
                type: str
            schedule:
                type: str
                description: no description
            security:
                type: str
                description: no description
                choices:
                    - 'None'
                    - 'WEP64'
                    - 'wep64'
                    - 'WEP128'
                    - 'wep128'
                    - 'WPA_PSK'
                    - 'WPA_RADIUS'
                    - 'WPA'
                    - 'WPA2'
                    - 'WPA2_AUTO'
                    - 'open'
                    - 'wpa-personal'
                    - 'wpa-enterprise'
                    - 'captive-portal'
                    - 'wpa-only-personal'
                    - 'wpa-only-enterprise'
                    - 'wpa2-only-personal'
                    - 'wpa2-only-enterprise'
                    - 'wpa-personal+captive-portal'
                    - 'wpa-only-personal+captive-portal'
                    - 'wpa2-only-personal+captive-portal'
                    - 'osen'
                    - 'wpa3-enterprise'
                    - 'sae'
                    - 'sae-transition'
                    - 'owe'
                    - 'wpa3-sae'
                    - 'wpa3-sae-transition'
            security-exempt-list:
                type: str
                description: no description
            security-obsolete-option:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            security-redirect-url:
                type: str
                description: no description
            selected-usergroups:
                type: str
                description: no description
            split-tunneling:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            ssid:
                type: str
                description: no description
            tkip-counter-measure:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            usergroup:
                type: str
                description: no description
            utm-profile:
                type: str
                description: no description
            vdom:
                type: str
                description: no description
            vlan-auto:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'
            vlan-pooling:
                type: str
                description: no description
                choices:
                    - 'wtp-group'
                    - 'round-robin'
                    - 'hash'
                    - 'disable'
            vlanid:
                type: int
                description: no description
            voice-enterprise:
                type: str
                description: no description
                choices:
                    - 'disable'
                    - 'enable'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:
    - name: no description
      fmgr_vap_dynamicmapping:
         bypass_validation: False
         workspace_locking_adom: <value in [global, custom adom including root]>
         workspace_locking_timeout: 300
         rc_succeeded: [0, -2, -3, ...]
         rc_failed: [-2, -3, ...]
         adom: <your own value>
         vap: <your own value>
         state: <value in [present, absent]>
         vap_dynamicmapping:
            _centmgmt: <value in [disable, enable]>
            _dhcp_svr_id: <value of string>
            _intf_allowaccess:
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - fgfm
              - auto-ipsec
              - radius-acct
              - probe-response
              - capwap
            _intf_device-identification: <value in [disable, enable]>
            _intf_device-netscan: <value in [disable, enable]>
            _intf_dhcp-relay-ip: <value of string>
            _intf_dhcp-relay-service: <value in [disable, enable]>
            _intf_dhcp-relay-type: <value in [regular, ipsec]>
            _intf_dhcp6-relay-ip: <value of string>
            _intf_dhcp6-relay-service: <value in [disable, enable]>
            _intf_dhcp6-relay-type: <value in [regular]>
            _intf_ip: <value of string>
            _intf_ip6-address: <value of string>
            _intf_ip6-allowaccess:
              - https
              - ping
              - ssh
              - snmp
              - http
              - telnet
              - any
              - fgfm
              - capwap
            _intf_listen-forticlient-connection: <value in [disable, enable]>
            _scope:
              -
                  name: <value of string>
                  vdom: <value of string>
            acct-interim-interval: <value of integer>
            address-group: <value of string>
            alias: <value of string>
            atf-weight: <value of integer>
            auth: <value in [PSK, psk, RADIUS, ...]>
            broadcast-ssid: <value in [disable, enable]>
            broadcast-suppression:
              - dhcp
              - arp
              - dhcp2
              - arp2
              - netbios-ns
              - netbios-ds
              - arp3
              - dhcp-up
              - dhcp-down
              - arp-known
              - arp-unknown
              - arp-reply
              - ipv6
              - dhcp-starvation
              - arp-poison
              - all-other-mc
              - all-other-bc
              - arp-proxy
              - dhcp-ucast
            captive-portal-ac-name: <value of string>
            captive-portal-macauth-radius-secret: <value of string>
            captive-portal-macauth-radius-server: <value of string>
            captive-portal-radius-secret: <value of string>
            captive-portal-radius-server: <value of string>
            captive-portal-session-timeout-interval: <value of integer>
            client-count: <value of integer>
            dhcp-lease-time: <value of integer>
            dhcp-option82-circuit-id-insertion: <value in [disable, style-1, style-2]>
            dhcp-option82-insertion: <value in [disable, enable]>
            dhcp-option82-remote-id-insertion: <value in [disable, style-1]>
            dynamic-vlan: <value in [disable, enable]>
            eap-reauth: <value in [disable, enable]>
            eap-reauth-intv: <value of integer>
            eapol-key-retries: <value in [disable, enable]>
            encrypt: <value in [TKIP, AES, TKIP-AES]>
            external-fast-roaming: <value in [disable, enable]>
            external-logout: <value of string>
            external-web: <value of string>
            fast-bss-transition: <value in [disable, enable]>
            fast-roaming: <value in [disable, enable]>
            ft-mobility-domain: <value of integer>
            ft-over-ds: <value in [disable, enable]>
            ft-r0-key-lifetime: <value of integer>
            gtk-rekey: <value in [disable, enable]>
            gtk-rekey-intv: <value of integer>
            hotspot20-profile: <value of string>
            intra-vap-privacy: <value in [disable, enable]>
            ip: <value of string>
            key: <value of string>
            keyindex: <value of integer>
            ldpc: <value in [disable, tx, rx, ...]>
            local-authentication: <value in [disable, enable]>
            local-bridging: <value in [disable, enable]>
            local-lan: <value in [deny, allow]>
            local-standalone: <value in [disable, enable]>
            local-standalone-nat: <value in [disable, enable]>
            local-switching: <value in [disable, enable]>
            mac-auth-bypass: <value in [disable, enable]>
            mac-filter: <value in [disable, enable]>
            mac-filter-policy-other: <value in [deny, allow]>
            max-clients: <value of integer>
            max-clients-ap: <value of integer>
            me-disable-thresh: <value of integer>
            mesh-backhaul: <value in [disable, enable]>
            mpsk: <value in [disable, enable]>
            mpsk-concurrent-clients: <value of integer>
            multicast-enhance: <value in [disable, enable]>
            multicast-rate: <value in [0, 6000, 12000, ...]>
            okc: <value in [disable, enable]>
            owe-groups:
              - 19
              - 20
              - 21
            owe-transition: <value in [disable, enable]>
            owe-transition-ssid: <value of string>
            passphrase: <value of string>
            pmf: <value in [disable, enable, optional]>
            pmf-assoc-comeback-timeout: <value of integer>
            pmf-sa-query-retry-timeout: <value of integer>
            portal-message-override-group: <value of string>
            portal-type: <value in [auth, auth+disclaimer, disclaimer, ...]>
            probe-resp-suppression: <value in [disable, enable]>
            probe-resp-threshold: <value of string>
            ptk-rekey: <value in [disable, enable]>
            ptk-rekey-intv: <value of integer>
            qos-profile: <value of string>
            quarantine: <value in [disable, enable]>
            radio-2g-threshold: <value of string>
            radio-5g-threshold: <value of string>
            radio-sensitivity: <value in [disable, enable]>
            radius-mac-auth: <value in [disable, enable]>
            radius-mac-auth-server: <value of string>
            radius-mac-auth-usergroups: <value of string>
            radius-server: <value of string>
            rates-11a:
              - 1
              - 1-basic
              - 2
              - 2-basic
              - 5.5
              - 5.5-basic
              - 6
              - 6-basic
              - 9
              - 9-basic
              - 12
              - 12-basic
              - 18
              - 18-basic
              - 24
              - 24-basic
              - 36
              - 36-basic
              - 48
              - 48-basic
              - 54
              - 54-basic
              - 11
              - 11-basic
            rates-11ac-ss12:
              - mcs0/1
              - mcs1/1
              - mcs2/1
              - mcs3/1
              - mcs4/1
              - mcs5/1
              - mcs6/1
              - mcs7/1
              - mcs8/1
              - mcs9/1
              - mcs0/2
              - mcs1/2
              - mcs2/2
              - mcs3/2
              - mcs4/2
              - mcs5/2
              - mcs6/2
              - mcs7/2
              - mcs8/2
              - mcs9/2
              - mcs10/1
              - mcs11/1
              - mcs10/2
              - mcs11/2
            rates-11ac-ss34:
              - mcs0/3
              - mcs1/3
              - mcs2/3
              - mcs3/3
              - mcs4/3
              - mcs5/3
              - mcs6/3
              - mcs7/3
              - mcs8/3
              - mcs9/3
              - mcs0/4
              - mcs1/4
              - mcs2/4
              - mcs3/4
              - mcs4/4
              - mcs5/4
              - mcs6/4
              - mcs7/4
              - mcs8/4
              - mcs9/4
              - mcs10/3
              - mcs11/3
              - mcs10/4
              - mcs11/4
            rates-11bg:
              - 1
              - 1-basic
              - 2
              - 2-basic
              - 5.5
              - 5.5-basic
              - 6
              - 6-basic
              - 9
              - 9-basic
              - 12
              - 12-basic
              - 18
              - 18-basic
              - 24
              - 24-basic
              - 36
              - 36-basic
              - 48
              - 48-basic
              - 54
              - 54-basic
              - 11
              - 11-basic
            rates-11n-ss12:
              - mcs0/1
              - mcs1/1
              - mcs2/1
              - mcs3/1
              - mcs4/1
              - mcs5/1
              - mcs6/1
              - mcs7/1
              - mcs8/2
              - mcs9/2
              - mcs10/2
              - mcs11/2
              - mcs12/2
              - mcs13/2
              - mcs14/2
              - mcs15/2
            rates-11n-ss34:
              - mcs16/3
              - mcs17/3
              - mcs18/3
              - mcs19/3
              - mcs20/3
              - mcs21/3
              - mcs22/3
              - mcs23/3
              - mcs24/4
              - mcs25/4
              - mcs26/4
              - mcs27/4
              - mcs28/4
              - mcs29/4
              - mcs30/4
              - mcs31/4
            sae-groups:
              - 1
              - 2
              - 5
              - 14
              - 15
              - 16
              - 17
              - 18
              - 19
              - 20
              - 21
              - 27
              - 28
              - 29
              - 30
              - 31
            sae-password: <value of string>
            schedule: <value of string>
            security: <value in [None, WEP64, wep64, ...]>
            security-exempt-list: <value of string>
            security-obsolete-option: <value in [disable, enable]>
            security-redirect-url: <value of string>
            selected-usergroups: <value of string>
            split-tunneling: <value in [disable, enable]>
            ssid: <value of string>
            tkip-counter-measure: <value in [disable, enable]>
            usergroup: <value of string>
            utm-profile: <value of string>
            vdom: <value of string>
            vlan-auto: <value in [disable, enable]>
            vlan-pooling: <value in [wtp-group, round-robin, hash, ...]>
            vlanid: <value of integer>
            voice-enterprise: <value in [disable, enable]>

'''

RETURN = '''
request_url:
    description: The full url requested
    returned: always
    type: str
    sample: /sys/login/user
response_code:
    description: The status of api request
    returned: always
    type: int
    sample: 0
response_message:
    description: The descriptive message of the api response
    type: str
    returned: always
    sample: OK.

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import NAPIManager
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_galaxy_version
from ansible_collections.fortinet.fortimanager.plugins.module_utils.napi import check_parameter_bypass


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/dynamic_mapping',
        '/pm/config/global/obj/wireless-controller/vap/{vap}/dynamic_mapping'
    ]

    perobject_jrpc_urls = [
        '/pm/config/adom/{adom}/obj/wireless-controller/vap/{vap}/dynamic_mapping/{dynamic_mapping}',
        '/pm/config/global/obj/wireless-controller/vap/{vap}/dynamic_mapping/{dynamic_mapping}'
    ]

    url_params = ['adom', 'vap']
    module_primary_key = 'complex:{{module}}["_scope"][0]["name"]+"/"+{{module}}["_scope"][0]["vdom"]'
    module_arg_spec = {
        'bypass_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'rc_succeeded': {
            'required': False,
            'type': 'list'
        },
        'rc_failed': {
            'required': False,
            'type': 'list'
        },
        'state': {
            'type': 'str',
            'required': True,
            'choices': [
                'present',
                'absent'
            ]
        },
        'adom': {
            'required': True,
            'type': 'str'
        },
        'vap': {
            'required': True,
            'type': 'str'
        },
        'vap_dynamicmapping': {
            'required': False,
            'type': 'dict',
            'options': {
                '_centmgmt': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                '_dhcp_svr_id': {
                    'required': False,
                    'type': 'str'
                },
                '_intf_allowaccess': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'https',
                        'ping',
                        'ssh',
                        'snmp',
                        'http',
                        'telnet',
                        'fgfm',
                        'auto-ipsec',
                        'radius-acct',
                        'probe-response',
                        'capwap'
                    ]
                },
                '_intf_device-identification': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                '_intf_device-netscan': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                '_intf_dhcp-relay-ip': {
                    'required': False,
                    'type': 'str'
                },
                '_intf_dhcp-relay-service': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                '_intf_dhcp-relay-type': {
                    'required': False,
                    'choices': [
                        'regular',
                        'ipsec'
                    ],
                    'type': 'str'
                },
                '_intf_dhcp6-relay-ip': {
                    'required': False,
                    'type': 'str'
                },
                '_intf_dhcp6-relay-service': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                '_intf_dhcp6-relay-type': {
                    'required': False,
                    'choices': [
                        'regular'
                    ],
                    'type': 'str'
                },
                '_intf_ip': {
                    'required': False,
                    'type': 'str'
                },
                '_intf_ip6-address': {
                    'required': False,
                    'type': 'str'
                },
                '_intf_ip6-allowaccess': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'https',
                        'ping',
                        'ssh',
                        'snmp',
                        'http',
                        'telnet',
                        'any',
                        'fgfm',
                        'capwap'
                    ]
                },
                '_intf_listen-forticlient-connection': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                '_scope': {
                    'required': False,
                    'type': 'list',
                    'options': {
                        'name': {
                            'required': False,
                            'type': 'str'
                        },
                        'vdom': {
                            'required': False,
                            'type': 'str'
                        }
                    }
                },
                'acct-interim-interval': {
                    'required': False,
                    'type': 'int'
                },
                'address-group': {
                    'required': False,
                    'type': 'str'
                },
                'alias': {
                    'required': False,
                    'type': 'str'
                },
                'atf-weight': {
                    'required': False,
                    'type': 'int'
                },
                'auth': {
                    'required': False,
                    'choices': [
                        'PSK',
                        'psk',
                        'RADIUS',
                        'radius',
                        'usergroup'
                    ],
                    'type': 'str'
                },
                'broadcast-ssid': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'broadcast-suppression': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'dhcp',
                        'arp',
                        'dhcp2',
                        'arp2',
                        'netbios-ns',
                        'netbios-ds',
                        'arp3',
                        'dhcp-up',
                        'dhcp-down',
                        'arp-known',
                        'arp-unknown',
                        'arp-reply',
                        'ipv6',
                        'dhcp-starvation',
                        'arp-poison',
                        'all-other-mc',
                        'all-other-bc',
                        'arp-proxy',
                        'dhcp-ucast'
                    ]
                },
                'captive-portal-ac-name': {
                    'required': False,
                    'type': 'str'
                },
                'captive-portal-macauth-radius-secret': {
                    'required': False,
                    'type': 'str'
                },
                'captive-portal-macauth-radius-server': {
                    'required': False,
                    'type': 'str'
                },
                'captive-portal-radius-secret': {
                    'required': False,
                    'type': 'str'
                },
                'captive-portal-radius-server': {
                    'required': False,
                    'type': 'str'
                },
                'captive-portal-session-timeout-interval': {
                    'required': False,
                    'type': 'int'
                },
                'client-count': {
                    'required': False,
                    'type': 'int'
                },
                'dhcp-lease-time': {
                    'required': False,
                    'type': 'int'
                },
                'dhcp-option82-circuit-id-insertion': {
                    'required': False,
                    'choices': [
                        'disable',
                        'style-1',
                        'style-2'
                    ],
                    'type': 'str'
                },
                'dhcp-option82-insertion': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'dhcp-option82-remote-id-insertion': {
                    'required': False,
                    'choices': [
                        'disable',
                        'style-1'
                    ],
                    'type': 'str'
                },
                'dynamic-vlan': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'eap-reauth': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'eap-reauth-intv': {
                    'required': False,
                    'type': 'int'
                },
                'eapol-key-retries': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'encrypt': {
                    'required': False,
                    'choices': [
                        'TKIP',
                        'AES',
                        'TKIP-AES'
                    ],
                    'type': 'str'
                },
                'external-fast-roaming': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'external-logout': {
                    'required': False,
                    'type': 'str'
                },
                'external-web': {
                    'required': False,
                    'type': 'str'
                },
                'fast-bss-transition': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'fast-roaming': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ft-mobility-domain': {
                    'required': False,
                    'type': 'int'
                },
                'ft-over-ds': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ft-r0-key-lifetime': {
                    'required': False,
                    'type': 'int'
                },
                'gtk-rekey': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'gtk-rekey-intv': {
                    'required': False,
                    'type': 'int'
                },
                'hotspot20-profile': {
                    'required': False,
                    'type': 'str'
                },
                'intra-vap-privacy': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ip': {
                    'required': False,
                    'type': 'str'
                },
                'key': {
                    'required': False,
                    'type': 'str'
                },
                'keyindex': {
                    'required': False,
                    'type': 'int'
                },
                'ldpc': {
                    'required': False,
                    'choices': [
                        'disable',
                        'tx',
                        'rx',
                        'rxtx'
                    ],
                    'type': 'str'
                },
                'local-authentication': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'local-bridging': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'local-lan': {
                    'required': False,
                    'choices': [
                        'deny',
                        'allow'
                    ],
                    'type': 'str'
                },
                'local-standalone': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'local-standalone-nat': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'local-switching': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'mac-auth-bypass': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'mac-filter': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'mac-filter-policy-other': {
                    'required': False,
                    'choices': [
                        'deny',
                        'allow'
                    ],
                    'type': 'str'
                },
                'max-clients': {
                    'required': False,
                    'type': 'int'
                },
                'max-clients-ap': {
                    'required': False,
                    'type': 'int'
                },
                'me-disable-thresh': {
                    'required': False,
                    'type': 'int'
                },
                'mesh-backhaul': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'mpsk': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'mpsk-concurrent-clients': {
                    'required': False,
                    'type': 'int'
                },
                'multicast-enhance': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'multicast-rate': {
                    'required': False,
                    'choices': [
                        '0',
                        '6000',
                        '12000',
                        '24000'
                    ],
                    'type': 'str'
                },
                'okc': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'owe-groups': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        '19',
                        '20',
                        '21'
                    ]
                },
                'owe-transition': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'owe-transition-ssid': {
                    'required': False,
                    'type': 'str'
                },
                'passphrase': {
                    'required': False,
                    'type': 'str'
                },
                'pmf': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable',
                        'optional'
                    ],
                    'type': 'str'
                },
                'pmf-assoc-comeback-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'pmf-sa-query-retry-timeout': {
                    'required': False,
                    'type': 'int'
                },
                'portal-message-override-group': {
                    'required': False,
                    'type': 'str'
                },
                'portal-type': {
                    'required': False,
                    'choices': [
                        'auth',
                        'auth+disclaimer',
                        'disclaimer',
                        'email-collect',
                        'cmcc',
                        'cmcc-macauth',
                        'auth-mac'
                    ],
                    'type': 'str'
                },
                'probe-resp-suppression': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'probe-resp-threshold': {
                    'required': False,
                    'type': 'str'
                },
                'ptk-rekey': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ptk-rekey-intv': {
                    'required': False,
                    'type': 'int'
                },
                'qos-profile': {
                    'required': False,
                    'type': 'str'
                },
                'quarantine': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'radio-2g-threshold': {
                    'required': False,
                    'type': 'str'
                },
                'radio-5g-threshold': {
                    'required': False,
                    'type': 'str'
                },
                'radio-sensitivity': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'radius-mac-auth': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'radius-mac-auth-server': {
                    'required': False,
                    'type': 'str'
                },
                'radius-mac-auth-usergroups': {
                    'required': False,
                    'type': 'str'
                },
                'radius-server': {
                    'required': False,
                    'type': 'str'
                },
                'rates-11a': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        '1',
                        '1-basic',
                        '2',
                        '2-basic',
                        '5.5',
                        '5.5-basic',
                        '6',
                        '6-basic',
                        '9',
                        '9-basic',
                        '12',
                        '12-basic',
                        '18',
                        '18-basic',
                        '24',
                        '24-basic',
                        '36',
                        '36-basic',
                        '48',
                        '48-basic',
                        '54',
                        '54-basic',
                        '11',
                        '11-basic'
                    ]
                },
                'rates-11ac-ss12': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'mcs0/1',
                        'mcs1/1',
                        'mcs2/1',
                        'mcs3/1',
                        'mcs4/1',
                        'mcs5/1',
                        'mcs6/1',
                        'mcs7/1',
                        'mcs8/1',
                        'mcs9/1',
                        'mcs0/2',
                        'mcs1/2',
                        'mcs2/2',
                        'mcs3/2',
                        'mcs4/2',
                        'mcs5/2',
                        'mcs6/2',
                        'mcs7/2',
                        'mcs8/2',
                        'mcs9/2',
                        'mcs10/1',
                        'mcs11/1',
                        'mcs10/2',
                        'mcs11/2'
                    ]
                },
                'rates-11ac-ss34': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'mcs0/3',
                        'mcs1/3',
                        'mcs2/3',
                        'mcs3/3',
                        'mcs4/3',
                        'mcs5/3',
                        'mcs6/3',
                        'mcs7/3',
                        'mcs8/3',
                        'mcs9/3',
                        'mcs0/4',
                        'mcs1/4',
                        'mcs2/4',
                        'mcs3/4',
                        'mcs4/4',
                        'mcs5/4',
                        'mcs6/4',
                        'mcs7/4',
                        'mcs8/4',
                        'mcs9/4',
                        'mcs10/3',
                        'mcs11/3',
                        'mcs10/4',
                        'mcs11/4'
                    ]
                },
                'rates-11bg': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        '1',
                        '1-basic',
                        '2',
                        '2-basic',
                        '5.5',
                        '5.5-basic',
                        '6',
                        '6-basic',
                        '9',
                        '9-basic',
                        '12',
                        '12-basic',
                        '18',
                        '18-basic',
                        '24',
                        '24-basic',
                        '36',
                        '36-basic',
                        '48',
                        '48-basic',
                        '54',
                        '54-basic',
                        '11',
                        '11-basic'
                    ]
                },
                'rates-11n-ss12': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'mcs0/1',
                        'mcs1/1',
                        'mcs2/1',
                        'mcs3/1',
                        'mcs4/1',
                        'mcs5/1',
                        'mcs6/1',
                        'mcs7/1',
                        'mcs8/2',
                        'mcs9/2',
                        'mcs10/2',
                        'mcs11/2',
                        'mcs12/2',
                        'mcs13/2',
                        'mcs14/2',
                        'mcs15/2'
                    ]
                },
                'rates-11n-ss34': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        'mcs16/3',
                        'mcs17/3',
                        'mcs18/3',
                        'mcs19/3',
                        'mcs20/3',
                        'mcs21/3',
                        'mcs22/3',
                        'mcs23/3',
                        'mcs24/4',
                        'mcs25/4',
                        'mcs26/4',
                        'mcs27/4',
                        'mcs28/4',
                        'mcs29/4',
                        'mcs30/4',
                        'mcs31/4'
                    ]
                },
                'sae-groups': {
                    'required': False,
                    'type': 'list',
                    'choices': [
                        '1',
                        '2',
                        '5',
                        '14',
                        '15',
                        '16',
                        '17',
                        '18',
                        '19',
                        '20',
                        '21',
                        '27',
                        '28',
                        '29',
                        '30',
                        '31'
                    ]
                },
                'sae-password': {
                    'required': False,
                    'type': 'str'
                },
                'schedule': {
                    'required': False,
                    'type': 'str'
                },
                'security': {
                    'required': False,
                    'choices': [
                        'None',
                        'WEP64',
                        'wep64',
                        'WEP128',
                        'wep128',
                        'WPA_PSK',
                        'WPA_RADIUS',
                        'WPA',
                        'WPA2',
                        'WPA2_AUTO',
                        'open',
                        'wpa-personal',
                        'wpa-enterprise',
                        'captive-portal',
                        'wpa-only-personal',
                        'wpa-only-enterprise',
                        'wpa2-only-personal',
                        'wpa2-only-enterprise',
                        'wpa-personal+captive-portal',
                        'wpa-only-personal+captive-portal',
                        'wpa2-only-personal+captive-portal',
                        'osen',
                        'wpa3-enterprise',
                        'sae',
                        'sae-transition',
                        'owe',
                        'wpa3-sae',
                        'wpa3-sae-transition'
                    ],
                    'type': 'str'
                },
                'security-exempt-list': {
                    'required': False,
                    'type': 'str'
                },
                'security-obsolete-option': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'security-redirect-url': {
                    'required': False,
                    'type': 'str'
                },
                'selected-usergroups': {
                    'required': False,
                    'type': 'str'
                },
                'split-tunneling': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'ssid': {
                    'required': False,
                    'type': 'str'
                },
                'tkip-counter-measure': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'usergroup': {
                    'required': False,
                    'type': 'str'
                },
                'utm-profile': {
                    'required': False,
                    'type': 'str'
                },
                'vdom': {
                    'required': False,
                    'type': 'str'
                },
                'vlan-auto': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                },
                'vlan-pooling': {
                    'required': False,
                    'choices': [
                        'wtp-group',
                        'round-robin',
                        'hash',
                        'disable'
                    ],
                    'type': 'str'
                },
                'vlanid': {
                    'required': False,
                    'type': 'int'
                },
                'voice-enterprise': {
                    'required': False,
                    'choices': [
                        'disable',
                        'enable'
                    ],
                    'type': 'str'
                }
            }

        }
    }

    params_validation_blob = []
    check_galaxy_version(module_arg_spec)
    module = AnsibleModule(argument_spec=check_parameter_bypass(module_arg_spec, 'vap_dynamicmapping'),
                           supports_check_mode=False)

    fmgr = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        fmgr = NAPIManager(jrpc_urls, perobject_jrpc_urls, module_primary_key, url_params, module, connection, top_level_schema_name='data')
        fmgr.validate_parameters(params_validation_blob)
        fmgr.process_curd()
    else:
        module.fail_json(msg='MUST RUN IN HTTPAPI MODE')
    module.exit_json(meta=module.params)


if __name__ == '__main__':
    main()
