#!/usr/bin/python
#
# Copyright 2018-2021 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Polyaxon SDKs and REST API specification.

    Polyaxon SDKs and REST API specification.  # noqa: E501

    The version of the OpenAPI document: 1.9.2-dev0
    Contact: contact@polyaxon.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from polyaxon_sdk.configuration import Configuration


class V1ProjectSettings(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'connections': 'list[str]',
        'preset': 'str',
        'presets': 'list[str]',
        'queue': 'str',
        'queues': 'list[str]',
        'agents': 'list[str]',
        'user_accesses': 'list[V1ProjectUserAccess]',
        'teams': 'list[str]'
    }

    attribute_map = {
        'connections': 'connections',
        'preset': 'preset',
        'presets': 'presets',
        'queue': 'queue',
        'queues': 'queues',
        'agents': 'agents',
        'user_accesses': 'user_accesses',
        'teams': 'teams'
    }

    def __init__(self, connections=None, preset=None, presets=None, queue=None, queues=None, agents=None, user_accesses=None, teams=None, local_vars_configuration=None):  # noqa: E501
        """V1ProjectSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connections = None
        self._preset = None
        self._presets = None
        self._queue = None
        self._queues = None
        self._agents = None
        self._user_accesses = None
        self._teams = None
        self.discriminator = None

        if connections is not None:
            self.connections = connections
        if preset is not None:
            self.preset = preset
        if presets is not None:
            self.presets = presets
        if queue is not None:
            self.queue = queue
        if queues is not None:
            self.queues = queues
        if agents is not None:
            self.agents = agents
        if user_accesses is not None:
            self.user_accesses = user_accesses
        if teams is not None:
            self.teams = teams

    @property
    def connections(self):
        """Gets the connections of this V1ProjectSettings.  # noqa: E501


        :return: The connections of this V1ProjectSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this V1ProjectSettings.


        :param connections: The connections of this V1ProjectSettings.  # noqa: E501
        :type: list[str]
        """

        self._connections = connections

    @property
    def preset(self):
        """Gets the preset of this V1ProjectSettings.  # noqa: E501


        :return: The preset of this V1ProjectSettings.  # noqa: E501
        :rtype: str
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this V1ProjectSettings.


        :param preset: The preset of this V1ProjectSettings.  # noqa: E501
        :type: str
        """

        self._preset = preset

    @property
    def presets(self):
        """Gets the presets of this V1ProjectSettings.  # noqa: E501


        :return: The presets of this V1ProjectSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._presets

    @presets.setter
    def presets(self, presets):
        """Sets the presets of this V1ProjectSettings.


        :param presets: The presets of this V1ProjectSettings.  # noqa: E501
        :type: list[str]
        """

        self._presets = presets

    @property
    def queue(self):
        """Gets the queue of this V1ProjectSettings.  # noqa: E501


        :return: The queue of this V1ProjectSettings.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this V1ProjectSettings.


        :param queue: The queue of this V1ProjectSettings.  # noqa: E501
        :type: str
        """

        self._queue = queue

    @property
    def queues(self):
        """Gets the queues of this V1ProjectSettings.  # noqa: E501


        :return: The queues of this V1ProjectSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """Sets the queues of this V1ProjectSettings.


        :param queues: The queues of this V1ProjectSettings.  # noqa: E501
        :type: list[str]
        """

        self._queues = queues

    @property
    def agents(self):
        """Gets the agents of this V1ProjectSettings.  # noqa: E501


        :return: The agents of this V1ProjectSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this V1ProjectSettings.


        :param agents: The agents of this V1ProjectSettings.  # noqa: E501
        :type: list[str]
        """

        self._agents = agents

    @property
    def user_accesses(self):
        """Gets the user_accesses of this V1ProjectSettings.  # noqa: E501


        :return: The user_accesses of this V1ProjectSettings.  # noqa: E501
        :rtype: list[V1ProjectUserAccess]
        """
        return self._user_accesses

    @user_accesses.setter
    def user_accesses(self, user_accesses):
        """Sets the user_accesses of this V1ProjectSettings.


        :param user_accesses: The user_accesses of this V1ProjectSettings.  # noqa: E501
        :type: list[V1ProjectUserAccess]
        """

        self._user_accesses = user_accesses

    @property
    def teams(self):
        """Gets the teams of this V1ProjectSettings.  # noqa: E501


        :return: The teams of this V1ProjectSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this V1ProjectSettings.


        :param teams: The teams of this V1ProjectSettings.  # noqa: E501
        :type: list[str]
        """

        self._teams = teams

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ProjectSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ProjectSettings):
            return True

        return self.to_dict() != other.to_dict()
