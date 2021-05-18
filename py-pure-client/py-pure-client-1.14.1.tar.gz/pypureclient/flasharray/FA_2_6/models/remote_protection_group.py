# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_6 import models

class RemoteProtectionGroup(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'destroyed': 'bool',
        'is_local': 'bool',
        'remote': 'FixedReference',
        'source': 'FixedReference',
        'target_retention': 'RetentionPolicy',
        'time_remaining': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'destroyed': 'destroyed',
        'is_local': 'is_local',
        'remote': 'remote',
        'source': 'source',
        'target_retention': 'target_retention',
        'time_remaining': 'time_remaining'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        destroyed=None,  # type: bool
        is_local=None,  # type: bool
        remote=None,  # type: models.FixedReference
        source=None,  # type: models.FixedReference
        target_retention=None,  # type: models.RetentionPolicy
        time_remaining=None,  # type: int
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A locally unique, system-generated name. The name cannot be modified.
            destroyed (bool): Returns a value of `true` if the remote protection group has been destroyed and is pending eradication. The `time_remaining` value displays the amount of time left until the destroyed remote protection group is permanently eradicated. Before the `time_remaining` period has elapsed, the destroyed remote protection group can be recovered by setting `destroyed=false`. Once the `time_remaining` period has elapsed, the remote protection group is permanently eradicated and can no longer be recovered.
            is_local (bool): If set to `true`, the location reference is to the local array. If set to `false`, the location reference is to a remote location, such as a remote array or offload target.
            remote (FixedReference): The offload target that the remote protection group is on.
            source (FixedReference): The array where the remote protection group is replicated from.
            target_retention (RetentionPolicy): The retention policy for the remote protection group.
            time_remaining (int): Milliseconds remaining until eradication, if remote protection group has been destroyed.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if destroyed is not None:
            self.destroyed = destroyed
        if is_local is not None:
            self.is_local = is_local
        if remote is not None:
            self.remote = remote
        if source is not None:
            self.source = source
        if target_retention is not None:
            self.target_retention = target_retention
        if time_remaining is not None:
            self.time_remaining = time_remaining

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `RemoteProtectionGroup`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
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
        if issubclass(RemoteProtectionGroup, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RemoteProtectionGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
