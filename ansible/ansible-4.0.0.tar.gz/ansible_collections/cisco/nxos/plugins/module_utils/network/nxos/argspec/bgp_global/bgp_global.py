# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# cli_rm_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the module docstring and re-run
# cli_rm_builder.
#
#############################################

"""
The arg spec for the nxos_bgp_global module
"""


class Bgp_globalArgs(object):  # pylint: disable=R0903
    """The arg spec for the nxos_bgp_global module
    """

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {
            "type": "dict",
            "options": {
                "as_number": {"type": "str"},
                "affinity_group": {
                    "type": "dict",
                    "options": {"group_id": {"type": "int"}},
                },
                "bestpath": {
                    "type": "dict",
                    "options": {
                        "always_compare_med": {"type": "bool"},
                        "as_path": {
                            "type": "dict",
                            "options": {
                                "ignore": {"type": "bool"},
                                "multipath_relax": {"type": "bool"},
                            },
                        },
                        "compare_neighborid": {"type": "bool"},
                        "compare_routerid": {"type": "bool"},
                        "cost_community_ignore": {"type": "bool"},
                        "igp_metric_ignore": {"type": "bool"},
                        "med": {
                            "type": "dict",
                            "options": {
                                "confed": {"type": "bool"},
                                "missing_as_worst": {"type": "bool"},
                                "non_deterministic": {"type": "bool"},
                            },
                        },
                    },
                },
                "cluster_id": {"type": "str"},
                "confederation": {
                    "type": "dict",
                    "options": {
                        "identifier": {"type": "str"},
                        "peers": {"type": "list", "elements": "str"},
                    },
                },
                "disable_policy_batching": {
                    "type": "dict",
                    "options": {
                        "set": {"type": "bool"},
                        "ipv4": {
                            "type": "dict",
                            "options": {"prefix_list": {"type": "str"}},
                        },
                        "ipv6": {
                            "type": "dict",
                            "options": {"prefix_list": {"type": "str"}},
                        },
                        "nexthop": {"type": "bool"},
                    },
                },
                "dynamic_med_interval": {"type": "int"},
                "enforce_first_as": {"type": "bool"},
                "enhanced_error": {"type": "bool"},
                "fabric_soo": {"type": "str"},
                "fast_external_fallover": {"type": "bool"},
                "flush_routes": {"type": "bool"},
                "graceful_restart": {
                    "type": "dict",
                    "options": {
                        "set": {"type": "bool"},
                        "restart_time": {"type": "int"},
                        "stalepath_time": {"type": "int"},
                        "helper": {"type": "bool"},
                    },
                },
                "graceful_shutdown": {
                    "type": "dict",
                    "options": {
                        "activate": {
                            "type": "dict",
                            "options": {
                                "set": {"type": "bool"},
                                "route_map": {"type": "str"},
                            },
                        },
                        "aware": {"type": "bool"},
                    },
                },
                "isolate": {
                    "type": "dict",
                    "options": {
                        "set": {"type": "bool"},
                        "include_local": {"type": "bool"},
                    },
                },
                "log_neighbor_changes": {"type": "bool"},
                "maxas_limit": {"type": "int"},
                "neighbors": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "neighbor_address": {"type": "str", "required": True},
                        "bfd": {
                            "type": "dict",
                            "options": {
                                "set": {"type": "bool"},
                                "singlehop": {"type": "bool"},
                                "multihop": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "interval": {
                                            "type": "dict",
                                            "options": {
                                                "tx_interval": {"type": "int"},
                                                "min_rx_interval": {
                                                    "type": "int"
                                                },
                                                "multiplier": {"type": "int"},
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        "neighbor_affinity_group": {
                            "type": "dict",
                            "options": {"group_id": {"type": "int"}},
                        },
                        "bmp_activate_server": {"type": "int"},
                        "capability": {
                            "type": "dict",
                            "options": {
                                "suppress_4_byte_as": {"type": "bool"}
                            },
                        },
                        "description": {"type": "str"},
                        "disable_connected_check": {"type": "bool"},
                        "dont_capability_negotiate": {"type": "bool"},
                        "dscp": {"type": "str"},
                        "dynamic_capability": {"type": "bool"},
                        "ebgp_multihop": {"type": "int"},
                        "graceful_shutdown": {
                            "type": "dict",
                            "options": {
                                "activate": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "route_map": {"type": "str"},
                                    },
                                }
                            },
                        },
                        "inherit": {
                            "type": "dict",
                            "options": {
                                "peer": {"type": "str"},
                                "peer_session": {"type": "str"},
                            },
                        },
                        "local_as": {"type": "str"},
                        "log_neighbor_changes": {
                            "type": "dict",
                            "options": {
                                "set": {"type": "bool"},
                                "disable": {"type": "bool"},
                            },
                        },
                        "low_memory": {
                            "type": "dict",
                            "options": {"exempt": {"type": "bool"}},
                        },
                        "password": {
                            "type": "dict",
                            "no_log": False,
                            "options": {
                                "encryption": {"type": "int"},
                                "key": {"type": "str", "no_log": True},
                            },
                        },
                        "path_attribute": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "action": {
                                    "type": "str",
                                    "choices": [
                                        "discard",
                                        "treat-as-withdraw",
                                    ],
                                },
                                "type": {"type": "int"},
                                "range": {
                                    "type": "dict",
                                    "options": {
                                        "start": {"type": "int"},
                                        "end": {"type": "int"},
                                    },
                                },
                            },
                        },
                        "peer_type": {
                            "type": "str",
                            "choices": [
                                "fabric-border-leaf",
                                "fabric-external",
                            ],
                        },
                        "remote_as": {"type": "str"},
                        "remove_private_as": {
                            "type": "dict",
                            "options": {
                                "set": {"type": "bool"},
                                "replace_as": {"type": "bool"},
                                "all": {"type": "bool"},
                            },
                        },
                        "shutdown": {"type": "bool"},
                        "timers": {
                            "type": "dict",
                            "options": {
                                "keepalive": {"type": "int"},
                                "holdtime": {"type": "int"},
                            },
                        },
                        "transport": {
                            "type": "dict",
                            "options": {
                                "connection_mode": {
                                    "type": "dict",
                                    "options": {"passive": {"type": "bool"}},
                                }
                            },
                        },
                        "ttl_security": {
                            "type": "dict",
                            "options": {"hops": {"type": "int"}},
                        },
                        "update_source": {"type": "str"},
                    },
                },
                "neighbor_down": {
                    "type": "dict",
                    "options": {"fib_accelerate": {"type": "bool"}},
                },
                "nexthop": {
                    "type": "dict",
                    "options": {
                        "suppress_default_resolution": {"type": "bool"}
                    },
                },
                "rd": {
                    "type": "dict",
                    "options": {
                        "dual": {"type": "bool"},
                        "id": {"type": "int"},
                    },
                },
                "reconnect_interval": {"type": "int"},
                "router_id": {"type": "str"},
                "shutdown": {"type": "bool"},
                "suppress_fib_pending": {"type": "bool"},
                "timers": {
                    "type": "dict",
                    "options": {
                        "bestpath_limit": {
                            "type": "dict",
                            "options": {
                                "timeout": {"type": "int"},
                                "always": {"type": "bool"},
                            },
                        },
                        "bgp": {
                            "type": "dict",
                            "options": {
                                "keepalive": {"type": "int"},
                                "holdtime": {"type": "int"},
                            },
                        },
                        "prefix_peer_timeout": {"type": "int"},
                        "prefix_peer_wait": {"type": "int"},
                    },
                },
                "vrfs": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "vrf": {"type": "str"},
                        "allocate_index": {"type": "int"},
                        "bestpath": {
                            "type": "dict",
                            "options": {
                                "always_compare_med": {"type": "bool"},
                                "as_path": {
                                    "type": "dict",
                                    "options": {
                                        "ignore": {"type": "bool"},
                                        "multipath_relax": {"type": "bool"},
                                    },
                                },
                                "compare_neighborid": {"type": "bool"},
                                "compare_routerid": {"type": "bool"},
                                "cost_community_ignore": {"type": "bool"},
                                "igp_metric_ignore": {"type": "bool"},
                                "med": {
                                    "type": "dict",
                                    "options": {
                                        "confed": {"type": "bool"},
                                        "missing_as_worst": {"type": "bool"},
                                        "non_deterministic": {"type": "bool"},
                                    },
                                },
                            },
                        },
                        "cluster_id": {"type": "str"},
                        "confederation": {
                            "type": "dict",
                            "options": {
                                "identifier": {"type": "str"},
                                "peers": {"type": "list", "elements": "str"},
                            },
                        },
                        "graceful_restart": {
                            "type": "dict",
                            "options": {
                                "set": {"type": "bool"},
                                "restart_time": {"type": "int"},
                                "stalepath_time": {"type": "int"},
                                "helper": {"type": "bool"},
                            },
                        },
                        "local_as": {"type": "str"},
                        "log_neighbor_changes": {"type": "bool"},
                        "maxas_limit": {"type": "int"},
                        "neighbors": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "neighbor_address": {
                                    "type": "str",
                                    "required": True,
                                },
                                "bfd": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "singlehop": {"type": "bool"},
                                        "multihop": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "interval": {
                                                    "type": "dict",
                                                    "options": {
                                                        "tx_interval": {
                                                            "type": "int"
                                                        },
                                                        "min_rx_interval": {
                                                            "type": "int"
                                                        },
                                                        "multiplier": {
                                                            "type": "int"
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                "neighbor_affinity_group": {
                                    "type": "dict",
                                    "options": {"group_id": {"type": "int"}},
                                },
                                "bmp_activate_server": {"type": "int"},
                                "capability": {
                                    "type": "dict",
                                    "options": {
                                        "suppress_4_byte_as": {"type": "bool"}
                                    },
                                },
                                "description": {"type": "str"},
                                "disable_connected_check": {"type": "bool"},
                                "dont_capability_negotiate": {"type": "bool"},
                                "dscp": {"type": "str"},
                                "dynamic_capability": {"type": "bool"},
                                "ebgp_multihop": {"type": "int"},
                                "graceful_shutdown": {
                                    "type": "dict",
                                    "options": {
                                        "activate": {
                                            "type": "dict",
                                            "options": {
                                                "set": {"type": "bool"},
                                                "route_map": {"type": "str"},
                                            },
                                        }
                                    },
                                },
                                "inherit": {
                                    "type": "dict",
                                    "options": {
                                        "peer": {"type": "str"},
                                        "peer_session": {"type": "str"},
                                    },
                                },
                                "local_as": {"type": "str"},
                                "log_neighbor_changes": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "disable": {"type": "bool"},
                                    },
                                },
                                "low_memory": {
                                    "type": "dict",
                                    "options": {"exempt": {"type": "bool"}},
                                },
                                "password": {
                                    "type": "dict",
                                    "no_log": False,
                                    "options": {
                                        "encryption": {"type": "int"},
                                        "key": {"type": "str", "no_log": True},
                                    },
                                },
                                "path_attribute": {
                                    "type": "list",
                                    "elements": "dict",
                                    "options": {
                                        "action": {
                                            "type": "str",
                                            "choices": [
                                                "discard",
                                                "treat-as-withdraw",
                                            ],
                                        },
                                        "type": {"type": "int"},
                                        "range": {
                                            "type": "dict",
                                            "options": {
                                                "start": {"type": "int"},
                                                "end": {"type": "int"},
                                            },
                                        },
                                    },
                                },
                                "peer_type": {
                                    "type": "str",
                                    "choices": [
                                        "fabric-border-leaf",
                                        "fabric-external",
                                    ],
                                },
                                "remote_as": {"type": "str"},
                                "remove_private_as": {
                                    "type": "dict",
                                    "options": {
                                        "set": {"type": "bool"},
                                        "replace_as": {"type": "bool"},
                                        "all": {"type": "bool"},
                                    },
                                },
                                "shutdown": {"type": "bool"},
                                "timers": {
                                    "type": "dict",
                                    "options": {
                                        "keepalive": {"type": "int"},
                                        "holdtime": {"type": "int"},
                                    },
                                },
                                "transport": {
                                    "type": "dict",
                                    "options": {
                                        "connection_mode": {
                                            "type": "dict",
                                            "options": {
                                                "passive": {"type": "bool"}
                                            },
                                        }
                                    },
                                },
                                "ttl_security": {
                                    "type": "dict",
                                    "options": {"hops": {"type": "int"}},
                                },
                                "update_source": {"type": "str"},
                            },
                        },
                        "neighbor_down": {
                            "type": "dict",
                            "options": {"fib_accelerate": {"type": "bool"}},
                        },
                        "reconnect_interval": {"type": "int"},
                        "router_id": {"type": "str"},
                        "timers": {
                            "type": "dict",
                            "options": {
                                "bestpath_limit": {
                                    "type": "dict",
                                    "options": {
                                        "timeout": {"type": "int"},
                                        "always": {"type": "bool"},
                                    },
                                },
                                "bgp": {
                                    "type": "dict",
                                    "options": {
                                        "keepalive": {"type": "int"},
                                        "holdtime": {"type": "int"},
                                    },
                                },
                                "prefix_peer_timeout": {"type": "int"},
                                "prefix_peer_wait": {"type": "int"},
                            },
                        },
                    },
                },
            },
        },
        "state": {
            "type": "str",
            "choices": [
                "merged",
                "replaced",
                "deleted",
                "purged",
                "parsed",
                "gathered",
                "rendered",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301
