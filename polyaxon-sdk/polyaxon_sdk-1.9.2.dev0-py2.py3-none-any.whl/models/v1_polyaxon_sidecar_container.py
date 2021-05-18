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


class V1PolyaxonSidecarContainer(object):
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
        'image': 'str',
        'image_tag': 'str',
        'image_pull_policy': 'str',
        'sleep_interval': 'int',
        'sync_interval': 'int',
        'monitor_logs': 'bool',
        'resources': 'object'
    }

    attribute_map = {
        'image': 'image',
        'image_tag': 'imageTag',
        'image_pull_policy': 'imagePullPolicy',
        'sleep_interval': 'sleepInterval',
        'sync_interval': 'syncInterval',
        'monitor_logs': 'monitorLogs',
        'resources': 'resources'
    }

    def __init__(self, image=None, image_tag=None, image_pull_policy=None, sleep_interval=None, sync_interval=None, monitor_logs=None, resources=None, local_vars_configuration=None):  # noqa: E501
        """V1PolyaxonSidecarContainer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._image = None
        self._image_tag = None
        self._image_pull_policy = None
        self._sleep_interval = None
        self._sync_interval = None
        self._monitor_logs = None
        self._resources = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if image_tag is not None:
            self.image_tag = image_tag
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if sleep_interval is not None:
            self.sleep_interval = sleep_interval
        if sync_interval is not None:
            self.sync_interval = sync_interval
        if monitor_logs is not None:
            self.monitor_logs = monitor_logs
        if resources is not None:
            self.resources = resources

    @property
    def image(self):
        """Gets the image of this V1PolyaxonSidecarContainer.  # noqa: E501


        :return: The image of this V1PolyaxonSidecarContainer.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this V1PolyaxonSidecarContainer.


        :param image: The image of this V1PolyaxonSidecarContainer.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def image_tag(self):
        """Gets the image_tag of this V1PolyaxonSidecarContainer.  # noqa: E501


        :return: The image_tag of this V1PolyaxonSidecarContainer.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this V1PolyaxonSidecarContainer.


        :param image_tag: The image_tag of this V1PolyaxonSidecarContainer.  # noqa: E501
        :type: str
        """

        self._image_tag = image_tag

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this V1PolyaxonSidecarContainer.  # noqa: E501


        :return: The image_pull_policy of this V1PolyaxonSidecarContainer.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this V1PolyaxonSidecarContainer.


        :param image_pull_policy: The image_pull_policy of this V1PolyaxonSidecarContainer.  # noqa: E501
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def sleep_interval(self):
        """Gets the sleep_interval of this V1PolyaxonSidecarContainer.  # noqa: E501


        :return: The sleep_interval of this V1PolyaxonSidecarContainer.  # noqa: E501
        :rtype: int
        """
        return self._sleep_interval

    @sleep_interval.setter
    def sleep_interval(self, sleep_interval):
        """Sets the sleep_interval of this V1PolyaxonSidecarContainer.


        :param sleep_interval: The sleep_interval of this V1PolyaxonSidecarContainer.  # noqa: E501
        :type: int
        """

        self._sleep_interval = sleep_interval

    @property
    def sync_interval(self):
        """Gets the sync_interval of this V1PolyaxonSidecarContainer.  # noqa: E501


        :return: The sync_interval of this V1PolyaxonSidecarContainer.  # noqa: E501
        :rtype: int
        """
        return self._sync_interval

    @sync_interval.setter
    def sync_interval(self, sync_interval):
        """Sets the sync_interval of this V1PolyaxonSidecarContainer.


        :param sync_interval: The sync_interval of this V1PolyaxonSidecarContainer.  # noqa: E501
        :type: int
        """

        self._sync_interval = sync_interval

    @property
    def monitor_logs(self):
        """Gets the monitor_logs of this V1PolyaxonSidecarContainer.  # noqa: E501


        :return: The monitor_logs of this V1PolyaxonSidecarContainer.  # noqa: E501
        :rtype: bool
        """
        return self._monitor_logs

    @monitor_logs.setter
    def monitor_logs(self, monitor_logs):
        """Sets the monitor_logs of this V1PolyaxonSidecarContainer.


        :param monitor_logs: The monitor_logs of this V1PolyaxonSidecarContainer.  # noqa: E501
        :type: bool
        """

        self._monitor_logs = monitor_logs

    @property
    def resources(self):
        """Gets the resources of this V1PolyaxonSidecarContainer.  # noqa: E501


        :return: The resources of this V1PolyaxonSidecarContainer.  # noqa: E501
        :rtype: object
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this V1PolyaxonSidecarContainer.


        :param resources: The resources of this V1PolyaxonSidecarContainer.  # noqa: E501
        :type: object
        """

        self._resources = resources

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
        if not isinstance(other, V1PolyaxonSidecarContainer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PolyaxonSidecarContainer):
            return True

        return self.to_dict() != other.to_dict()
