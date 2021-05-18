# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .available_plugin_summary import AvailablePluginSummary
from .create_instance_agent_command_details import CreateInstanceAgentCommandDetails
from .instance_agent_command import InstanceAgentCommand
from .instance_agent_command_content import InstanceAgentCommandContent
from .instance_agent_command_execution import InstanceAgentCommandExecution
from .instance_agent_command_execution_output_content import InstanceAgentCommandExecutionOutputContent
from .instance_agent_command_execution_output_via_object_storage_tuple_details import InstanceAgentCommandExecutionOutputViaObjectStorageTupleDetails
from .instance_agent_command_execution_output_via_object_storage_uri_details import InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails
from .instance_agent_command_execution_output_via_text_details import InstanceAgentCommandExecutionOutputViaTextDetails
from .instance_agent_command_execution_summary import InstanceAgentCommandExecutionSummary
from .instance_agent_command_output_details import InstanceAgentCommandOutputDetails
from .instance_agent_command_output_via_object_storage_tuple_details import InstanceAgentCommandOutputViaObjectStorageTupleDetails
from .instance_agent_command_output_via_object_storage_uri_details import InstanceAgentCommandOutputViaObjectStorageUriDetails
from .instance_agent_command_output_via_text_details import InstanceAgentCommandOutputViaTextDetails
from .instance_agent_command_source_details import InstanceAgentCommandSourceDetails
from .instance_agent_command_source_via_object_storage_tuple_details import InstanceAgentCommandSourceViaObjectStorageTupleDetails
from .instance_agent_command_source_via_object_storage_uri_details import InstanceAgentCommandSourceViaObjectStorageUriDetails
from .instance_agent_command_source_via_text_details import InstanceAgentCommandSourceViaTextDetails
from .instance_agent_command_summary import InstanceAgentCommandSummary
from .instance_agent_command_target import InstanceAgentCommandTarget
from .instance_agent_plugin import InstanceAgentPlugin
from .instance_agent_plugin_summary import InstanceAgentPluginSummary
from .plugin import Plugin

# Maps type names to classes for compute_instance_agent services.
compute_instance_agent_type_mapping = {
    "AvailablePluginSummary": AvailablePluginSummary,
    "CreateInstanceAgentCommandDetails": CreateInstanceAgentCommandDetails,
    "InstanceAgentCommand": InstanceAgentCommand,
    "InstanceAgentCommandContent": InstanceAgentCommandContent,
    "InstanceAgentCommandExecution": InstanceAgentCommandExecution,
    "InstanceAgentCommandExecutionOutputContent": InstanceAgentCommandExecutionOutputContent,
    "InstanceAgentCommandExecutionOutputViaObjectStorageTupleDetails": InstanceAgentCommandExecutionOutputViaObjectStorageTupleDetails,
    "InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails": InstanceAgentCommandExecutionOutputViaObjectStorageUriDetails,
    "InstanceAgentCommandExecutionOutputViaTextDetails": InstanceAgentCommandExecutionOutputViaTextDetails,
    "InstanceAgentCommandExecutionSummary": InstanceAgentCommandExecutionSummary,
    "InstanceAgentCommandOutputDetails": InstanceAgentCommandOutputDetails,
    "InstanceAgentCommandOutputViaObjectStorageTupleDetails": InstanceAgentCommandOutputViaObjectStorageTupleDetails,
    "InstanceAgentCommandOutputViaObjectStorageUriDetails": InstanceAgentCommandOutputViaObjectStorageUriDetails,
    "InstanceAgentCommandOutputViaTextDetails": InstanceAgentCommandOutputViaTextDetails,
    "InstanceAgentCommandSourceDetails": InstanceAgentCommandSourceDetails,
    "InstanceAgentCommandSourceViaObjectStorageTupleDetails": InstanceAgentCommandSourceViaObjectStorageTupleDetails,
    "InstanceAgentCommandSourceViaObjectStorageUriDetails": InstanceAgentCommandSourceViaObjectStorageUriDetails,
    "InstanceAgentCommandSourceViaTextDetails": InstanceAgentCommandSourceViaTextDetails,
    "InstanceAgentCommandSummary": InstanceAgentCommandSummary,
    "InstanceAgentCommandTarget": InstanceAgentCommandTarget,
    "InstanceAgentPlugin": InstanceAgentPlugin,
    "InstanceAgentPluginSummary": InstanceAgentPluginSummary,
    "Plugin": Plugin
}
