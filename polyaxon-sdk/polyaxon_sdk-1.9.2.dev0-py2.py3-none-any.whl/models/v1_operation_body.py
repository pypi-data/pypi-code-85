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


class V1OperationBody(object):
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
        'content': 'str',
        'is_managed': 'bool',
        'pending': 'V1RunPending',
        'name': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'meta_info': 'object'
    }

    attribute_map = {
        'content': 'content',
        'is_managed': 'is_managed',
        'pending': 'pending',
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'meta_info': 'meta_info'
    }

    def __init__(self, content=None, is_managed=None, pending=None, name=None, description=None, tags=None, meta_info=None, local_vars_configuration=None):  # noqa: E501
        """V1OperationBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content = None
        self._is_managed = None
        self._pending = None
        self._name = None
        self._description = None
        self._tags = None
        self._meta_info = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if is_managed is not None:
            self.is_managed = is_managed
        if pending is not None:
            self.pending = pending
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if meta_info is not None:
            self.meta_info = meta_info

    @property
    def content(self):
        """Gets the content of this V1OperationBody.  # noqa: E501


        :return: The content of this V1OperationBody.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this V1OperationBody.


        :param content: The content of this V1OperationBody.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def is_managed(self):
        """Gets the is_managed of this V1OperationBody.  # noqa: E501


        :return: The is_managed of this V1OperationBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_managed

    @is_managed.setter
    def is_managed(self, is_managed):
        """Sets the is_managed of this V1OperationBody.


        :param is_managed: The is_managed of this V1OperationBody.  # noqa: E501
        :type: bool
        """

        self._is_managed = is_managed

    @property
    def pending(self):
        """Gets the pending of this V1OperationBody.  # noqa: E501


        :return: The pending of this V1OperationBody.  # noqa: E501
        :rtype: V1RunPending
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this V1OperationBody.


        :param pending: The pending of this V1OperationBody.  # noqa: E501
        :type: V1RunPending
        """

        self._pending = pending

    @property
    def name(self):
        """Gets the name of this V1OperationBody.  # noqa: E501


        :return: The name of this V1OperationBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1OperationBody.


        :param name: The name of this V1OperationBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this V1OperationBody.  # noqa: E501


        :return: The description of this V1OperationBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1OperationBody.


        :param description: The description of this V1OperationBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this V1OperationBody.  # noqa: E501


        :return: The tags of this V1OperationBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this V1OperationBody.


        :param tags: The tags of this V1OperationBody.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def meta_info(self):
        """Gets the meta_info of this V1OperationBody.  # noqa: E501


        :return: The meta_info of this V1OperationBody.  # noqa: E501
        :rtype: object
        """
        return self._meta_info

    @meta_info.setter
    def meta_info(self, meta_info):
        """Sets the meta_info of this V1OperationBody.


        :param meta_info: The meta_info of this V1OperationBody.  # noqa: E501
        :type: object
        """

        self._meta_info = meta_info

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
        if not isinstance(other, V1OperationBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1OperationBody):
            return True

        return self.to_dict() != other.to_dict()
