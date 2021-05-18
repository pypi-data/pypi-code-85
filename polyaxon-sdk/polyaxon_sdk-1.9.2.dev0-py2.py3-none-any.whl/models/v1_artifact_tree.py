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


class V1ArtifactTree(object):
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
        'files': 'dict(str, str)',
        'dirs': 'list[str]',
        'is_done': 'bool'
    }

    attribute_map = {
        'files': 'files',
        'dirs': 'dirs',
        'is_done': 'is_done'
    }

    def __init__(self, files=None, dirs=None, is_done=None, local_vars_configuration=None):  # noqa: E501
        """V1ArtifactTree - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._files = None
        self._dirs = None
        self._is_done = None
        self.discriminator = None

        if files is not None:
            self.files = files
        if dirs is not None:
            self.dirs = dirs
        if is_done is not None:
            self.is_done = is_done

    @property
    def files(self):
        """Gets the files of this V1ArtifactTree.  # noqa: E501


        :return: The files of this V1ArtifactTree.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this V1ArtifactTree.


        :param files: The files of this V1ArtifactTree.  # noqa: E501
        :type: dict(str, str)
        """

        self._files = files

    @property
    def dirs(self):
        """Gets the dirs of this V1ArtifactTree.  # noqa: E501


        :return: The dirs of this V1ArtifactTree.  # noqa: E501
        :rtype: list[str]
        """
        return self._dirs

    @dirs.setter
    def dirs(self, dirs):
        """Sets the dirs of this V1ArtifactTree.


        :param dirs: The dirs of this V1ArtifactTree.  # noqa: E501
        :type: list[str]
        """

        self._dirs = dirs

    @property
    def is_done(self):
        """Gets the is_done of this V1ArtifactTree.  # noqa: E501


        :return: The is_done of this V1ArtifactTree.  # noqa: E501
        :rtype: bool
        """
        return self._is_done

    @is_done.setter
    def is_done(self, is_done):
        """Sets the is_done of this V1ArtifactTree.


        :param is_done: The is_done of this V1ArtifactTree.  # noqa: E501
        :type: bool
        """

        self._is_done = is_done

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
        if not isinstance(other, V1ArtifactTree):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ArtifactTree):
            return True

        return self.to_dict() != other.to_dict()
