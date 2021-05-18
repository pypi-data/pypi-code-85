#
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
The arg spec for the ios_acls module
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class AclsArgs(object):
    """The arg spec for the ios_acls module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "afi": {
                    "required": True,
                    "choices": ["ipv4", "ipv6"],
                    "type": "str",
                },
                "acls": {
                    "elements": "dict",
                    "type": "list",
                    "options": {
                        "name": {"required": True, "type": "str"},
                        "acl_type": {
                            "choices": ["extended", "standard"],
                            "type": "str",
                        },
                        "aces": {
                            "elements": "dict",
                            "type": "list",
                            "options": {
                                "grant": {
                                    "choices": ["permit", "deny"],
                                    "type": "str",
                                },
                                "sequence": {"type": "int"},
                                "evaluate": {"type": "str"},
                                "source": {
                                    "type": "dict",
                                    "mutually_exclusive": [
                                        ["address", "any", "host"],
                                        ["wildcard_bits", "any", "host"],
                                    ],
                                    "options": {
                                        "address": {"type": "str"},
                                        "wildcard_bits": {"type": "str"},
                                        "any": {"type": "bool"},
                                        "host": {"type": "str"},
                                        "port_protocol": {
                                            "type": "dict",
                                            "options": {
                                                "eq": {"type": "str"},
                                                "gt": {"type": "str"},
                                                "lt": {"type": "str"},
                                                "neq": {"type": "str"},
                                                "range": {
                                                    "type": "dict",
                                                    "options": {
                                                        "start": {
                                                            "type": "int"
                                                        },
                                                        "end": {"type": "int"},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                "destination": {
                                    "type": "dict",
                                    "mutually_exclusive": [
                                        ["address", "any", "host"],
                                        ["wildcard_bits", "any", "host"],
                                    ],
                                    "options": {
                                        "address": {"type": "str"},
                                        "wildcard_bits": {"type": "str"},
                                        "any": {"type": "bool"},
                                        "host": {"type": "str"},
                                        "port_protocol": {
                                            "type": "dict",
                                            "options": {
                                                "eq": {"type": "str"},
                                                "gt": {"type": "str"},
                                                "lt": {"type": "str"},
                                                "neq": {"type": "str"},
                                                "range": {
                                                    "type": "dict",
                                                    "options": {
                                                        "start": {
                                                            "type": "int"
                                                        },
                                                        "end": {"type": "int"},
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                "protocol": {"type": "str"},
                                "protocol_options": {
                                    "type": "dict",
                                    "options": {
                                        "protocol_number": {"type": "int"},
                                        "ahp": {"type": "bool"},
                                        "eigrp": {"type": "bool"},
                                        "esp": {"type": "bool"},
                                        "gre": {"type": "bool"},
                                        "hbh": {"type": "bool"},
                                        "icmp": {
                                            "type": "dict",
                                            "options": {
                                                "administratively_prohibited": {
                                                    "type": "bool"
                                                },
                                                "alternate_address": {
                                                    "type": "bool"
                                                },
                                                "conversion_error": {
                                                    "type": "bool"
                                                },
                                                "dod_host_prohibited": {
                                                    "type": "bool"
                                                },
                                                "dod_net_prohibited": {
                                                    "type": "bool"
                                                },
                                                "echo": {"type": "bool"},
                                                "echo_reply": {"type": "bool"},
                                                "general_parameter_problem": {
                                                    "type": "bool"
                                                },
                                                "host_isolated": {
                                                    "type": "bool"
                                                },
                                                "host_precedence_unreachable": {
                                                    "type": "bool"
                                                },
                                                "host_redirect": {
                                                    "type": "bool"
                                                },
                                                "host_tos_redirect": {
                                                    "type": "bool"
                                                },
                                                "host_tos_unreachable": {
                                                    "type": "bool"
                                                },
                                                "host_unknown": {
                                                    "type": "bool"
                                                },
                                                "host_unreachable": {
                                                    "type": "bool"
                                                },
                                                "information_reply": {
                                                    "type": "bool"
                                                },
                                                "information_request": {
                                                    "type": "bool"
                                                },
                                                "mask_reply": {"type": "bool"},
                                                "mask_request": {
                                                    "type": "bool"
                                                },
                                                "mobile_redirect": {
                                                    "type": "bool"
                                                },
                                                "net_redirect": {
                                                    "type": "bool"
                                                },
                                                "net_tos_redirect": {
                                                    "type": "bool"
                                                },
                                                "net_tos_unreachable": {
                                                    "type": "bool"
                                                },
                                                "net_unreachable": {
                                                    "type": "bool"
                                                },
                                                "network_unknown": {
                                                    "type": "bool"
                                                },
                                                "no_room_for_option": {
                                                    "type": "bool"
                                                },
                                                "option_missing": {
                                                    "type": "bool"
                                                },
                                                "packet_too_big": {
                                                    "type": "bool"
                                                },
                                                "parameter_problem": {
                                                    "type": "bool"
                                                },
                                                "port_unreachable": {
                                                    "type": "bool"
                                                },
                                                "precedence_unreachable": {
                                                    "type": "bool"
                                                },
                                                "protocol_unreachable": {
                                                    "type": "bool"
                                                },
                                                "reassembly_timeout": {
                                                    "type": "bool"
                                                },
                                                "redirect": {"type": "bool"},
                                                "router_advertisement": {
                                                    "type": "bool"
                                                },
                                                "router_solicitation": {
                                                    "type": "bool"
                                                },
                                                "source_quench": {
                                                    "type": "bool"
                                                },
                                                "source_route_failed": {
                                                    "type": "bool"
                                                },
                                                "time_exceeded": {
                                                    "type": "bool"
                                                },
                                                "timestamp_reply": {
                                                    "type": "bool"
                                                },
                                                "timestamp_request": {
                                                    "type": "bool"
                                                },
                                                "traceroute": {"type": "bool"},
                                                "ttl_exceeded": {
                                                    "type": "bool"
                                                },
                                                "unreachable": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "igmp": {
                                            "type": "dict",
                                            "options": {
                                                "dvmrp": {"type": "bool"},
                                                "host_query": {"type": "bool"},
                                                "mtrace_resp": {
                                                    "type": "bool"
                                                },
                                                "mtrace_route": {
                                                    "type": "bool"
                                                },
                                                "pim": {"type": "bool"},
                                                "trace": {"type": "bool"},
                                                "v1host_report": {
                                                    "type": "bool"
                                                },
                                                "v2host_report": {
                                                    "type": "bool"
                                                },
                                                "v2leave_group": {
                                                    "type": "bool"
                                                },
                                                "v3host_report": {
                                                    "type": "bool"
                                                },
                                            },
                                        },
                                        "ip": {"type": "bool"},
                                        "ipv6": {"type": "bool"},
                                        "ipinip": {"type": "bool"},
                                        "nos": {"type": "bool"},
                                        "ospf": {"type": "bool"},
                                        "pcp": {"type": "bool"},
                                        "pim": {"type": "bool"},
                                        "sctp": {"type": "bool"},
                                        "tcp": {
                                            "options": {
                                                "ack": {"type": "bool"},
                                                "established": {
                                                    "type": "bool"
                                                },
                                                "fin": {"type": "bool"},
                                                "psh": {"type": "bool"},
                                                "rst": {"type": "bool"},
                                                "syn": {"type": "bool"},
                                                "urg": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                        "udp": {"type": "bool"},
                                    },
                                },
                                "dscp": {"type": "str"},
                                "fragments": {"type": "str"},
                                "log": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "user_cookie": {"type": "str"},
                                    },
                                },
                                "log_input": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "user_cookie": {"type": "str"},
                                    },
                                },
                                "option": {
                                    "type": "dict",
                                    "options": {
                                        "add_ext": {"type": "bool"},
                                        "any_options": {"type": "bool"},
                                        "com_security": {"type": "bool"},
                                        "dps": {"type": "bool"},
                                        "encode": {"type": "bool"},
                                        "eool": {"type": "bool"},
                                        "ext_ip": {"type": "bool"},
                                        "ext_security": {"type": "bool"},
                                        "finn": {"type": "bool"},
                                        "imitd": {"type": "bool"},
                                        "lsr": {"type": "bool"},
                                        "mtup": {"type": "bool"},
                                        "mtur": {"type": "bool"},
                                        "no_op": {"type": "bool"},
                                        "nsapa": {"type": "bool"},
                                        "record_route": {"type": "bool"},
                                        "router_alert": {"type": "bool"},
                                        "sdb": {"type": "bool"},
                                        "security": {"type": "bool"},
                                        "ssr": {"type": "bool"},
                                        "stream_id": {"type": "bool"},
                                        "timestamp": {"type": "bool"},
                                        "traceroute": {"type": "bool"},
                                        "ump": {"type": "bool"},
                                        "visa": {"type": "bool"},
                                        "zsu": {"type": "bool"},
                                    },
                                },
                                "precedence": {"type": "int"},
                                "time_range": {"type": "str"},
                                "tos": {
                                    "type": "dict",
                                    "options": {
                                        "service_value": {"type": "int"},
                                        "max_reliability": {"type": "bool"},
                                        "max_throughput": {"type": "bool"},
                                        "min_delay": {"type": "bool"},
                                        "min_monetary_cost": {"type": "bool"},
                                        "normal": {"type": "bool"},
                                    },
                                },
                                "ttl": {
                                    "type": "dict",
                                    "options": {
                                        "eq": {"type": "int"},
                                        "gt": {"type": "int"},
                                        "lt": {"type": "int"},
                                        "neq": {"type": "int"},
                                        "range": {
                                            "type": "dict",
                                            "options": {
                                                "start": {"type": "int"},
                                                "end": {"type": "int"},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            "type": "list",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }
