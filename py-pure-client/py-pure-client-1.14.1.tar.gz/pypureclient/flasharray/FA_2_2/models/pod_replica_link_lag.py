# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_2 import models

class PodReplicaLinkLag(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'direction': 'str',
        'lag': 'ReplicaLinkLag',
        'local_pod': 'FixedReference',
        'recovery_point': 'int',
        'remote_pod': 'FixedReference',
        'remotes': 'list[FixedReference]',
        'status': 'str',
        'time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'direction': 'direction',
        'lag': 'lag',
        'local_pod': 'local_pod',
        'recovery_point': 'recovery_point',
        'remote_pod': 'remote_pod',
        'remotes': 'remotes',
        'status': 'status',
        'time': 'time'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        direction=None,  # type: str
        lag=None,  # type: models.ReplicaLinkLag
        local_pod=None,  # type: models.FixedReference
        recovery_point=None,  # type: int
        remote_pod=None,  # type: models.FixedReference
        remotes=None,  # type: List[models.FixedReference]
        status=None,  # type: str
        time=None,  # type: int
    ):
        """
        Keyword args:
            id (str): A non-modifiable, globally unique ID chosen by the system.
            direction (str): The direction of replication. Valid values include `inbound` and `outbound`.
            lag (ReplicaLinkLag): Duration in milliseconds that indicates how far behind the replication target is from the source.
            local_pod (FixedReference): Reference to a local pod.
            recovery_point (int): Time when the last piece of data was replicated, in milliseconds since the UNIX epoch, and the recovery point if the pod is promoted. If the pod is baselining then the value is `null`.
            remote_pod (FixedReference): Reference to a remote pod.
            remotes (list[FixedReference]): Reference to a remote array.
            status (str): Status of the replica-link. Valid values include `replicating`, `baselining`, `paused`, `quiescing`, `quiesced`, `idle`, and `unhealthy`.
            time (int): Sample time in milliseconds since the UNIX epoch.
        """
        if id is not None:
            self.id = id
        if direction is not None:
            self.direction = direction
        if lag is not None:
            self.lag = lag
        if local_pod is not None:
            self.local_pod = local_pod
        if recovery_point is not None:
            self.recovery_point = recovery_point
        if remote_pod is not None:
            self.remote_pod = remote_pod
        if remotes is not None:
            self.remotes = remotes
        if status is not None:
            self.status = status
        if time is not None:
            self.time = time

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodReplicaLinkLag`".format(key))
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
        if issubclass(PodReplicaLinkLag, dict):
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
        if not isinstance(other, PodReplicaLinkLag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
