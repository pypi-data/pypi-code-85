# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_1 import models

class RemoteProtectionGroupSnapshot(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'created': 'int',
        'destroyed': 'bool',
        'is_local': 'bool',
        'remote': 'FixedReference',
        'source': 'FixedReferenceNoId',
        'suffix': 'str',
        'time_remaining': 'int'
    }

    attribute_map = {
        'name': 'name',
        'created': 'created',
        'destroyed': 'destroyed',
        'is_local': 'is_local',
        'remote': 'remote',
        'source': 'source',
        'suffix': 'suffix',
        'time_remaining': 'time_remaining'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        created=None,  # type: int
        destroyed=None,  # type: bool
        is_local=None,  # type: bool
        remote=None,  # type: models.FixedReference
        source=None,  # type: models.FixedReferenceNoId
        suffix=None,  # type: str
        time_remaining=None,  # type: int
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified.
            created (int): Creation time of the snapshot on the original source of the snapshot. Measured in milliseconds since the UNIX epoch.
            destroyed (bool): Destroyed and pending eradication? If not specified, defaults to false.
            is_local (bool): Whether or not this remote protection group snapshot is replicated from the current array.
            remote (FixedReference): The offload target where the remote protection group snapshot is located.
            source (FixedReferenceNoId): The original protection group from which this snapshot was taken.
            suffix (str): The suffix that is appended to the `source_name` value to generate the full remote protection group snapshot name in the form `PGROUP.SUFFIX`. If the suffix is not specified, the system constructs the snapshot name in the form `PGROUP.NNN`, where `PGROUP` is the protection group name, and `NNN` is a monotonically increasing number.
            time_remaining (int): Milliseconds remaining until eradication, if the snapshot has been destroyed.
        """
        if name is not None:
            self.name = name
        if created is not None:
            self.created = created
        if destroyed is not None:
            self.destroyed = destroyed
        if is_local is not None:
            self.is_local = is_local
        if remote is not None:
            self.remote = remote
        if source is not None:
            self.source = source
        if suffix is not None:
            self.suffix = suffix
        if time_remaining is not None:
            self.time_remaining = time_remaining

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `RemoteProtectionGroupSnapshot`".format(key))
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
        if issubclass(RemoteProtectionGroupSnapshot, dict):
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
        if not isinstance(other, RemoteProtectionGroupSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
