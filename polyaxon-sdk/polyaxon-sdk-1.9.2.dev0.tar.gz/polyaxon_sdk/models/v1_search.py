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


class V1Search(object):
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
        'uuid': 'str',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'live_state': 'int',
        'spec': 'V1SearchSpec',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'uuid': 'uuid',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'live_state': 'live_state',
        'spec': 'spec',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, uuid=None, name=None, description=None, tags=None, live_state=None, spec=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """V1Search - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uuid = None
        self._name = None
        self._description = None
        self._tags = None
        self._live_state = None
        self._spec = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if live_state is not None:
            self.live_state = live_state
        if spec is not None:
            self.spec = spec
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def uuid(self):
        """Gets the uuid of this V1Search.  # noqa: E501


        :return: The uuid of this V1Search.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this V1Search.


        :param uuid: The uuid of this V1Search.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this V1Search.  # noqa: E501


        :return: The name of this V1Search.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1Search.


        :param name: The name of this V1Search.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this V1Search.  # noqa: E501


        :return: The description of this V1Search.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1Search.


        :param description: The description of this V1Search.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this V1Search.  # noqa: E501


        :return: The tags of this V1Search.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1Search.


        :param tags: The tags of this V1Search.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def live_state(self):
        """Gets the live_state of this V1Search.  # noqa: E501


        :return: The live_state of this V1Search.  # noqa: E501
        :rtype: int
        """
        return self._live_state

    @live_state.setter
    def live_state(self, live_state):
        """Sets the live_state of this V1Search.


        :param live_state: The live_state of this V1Search.  # noqa: E501
        :type: int
        """

        self._live_state = live_state

    @property
    def spec(self):
        """Gets the spec of this V1Search.  # noqa: E501


        :return: The spec of this V1Search.  # noqa: E501
        :rtype: V1SearchSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this V1Search.


        :param spec: The spec of this V1Search.  # noqa: E501
        :type: V1SearchSpec
        """

        self._spec = spec

    @property
    def created_at(self):
        """Gets the created_at of this V1Search.  # noqa: E501


        :return: The created_at of this V1Search.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V1Search.


        :param created_at: The created_at of this V1Search.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this V1Search.  # noqa: E501


        :return: The updated_at of this V1Search.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this V1Search.


        :param updated_at: The updated_at of this V1Search.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, V1Search):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Search):
            return True

        return self.to_dict() != other.to_dict()
