# coding: utf-8

"""
    FlashBlade REST API Client

    A lightweight client for FlashBlade REST API 2.0, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_0 import models

class ApiClient(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'access_token_ttl_in_ms': 'int',
        'enabled': 'bool',
        'issuer': 'str',
        'key_id': 'str',
        'max_role': 'FixedReference',
        'public_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'access_token_ttl_in_ms': 'access_token_ttl_in_ms',
        'enabled': 'enabled',
        'issuer': 'issuer',
        'key_id': 'key_id',
        'max_role': 'max_role',
        'public_key': 'public_key'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        id=None,  # type: str
        access_token_ttl_in_ms=None,  # type: int
        enabled=None,  # type: bool
        issuer=None,  # type: str
        key_id=None,  # type: str
        max_role=None,  # type: models.FixedReference
        public_key=None,  # type: str
    ):
        """
        Keyword args:
            name (str): Name of the object (e.g., a file system or snapshot).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            access_token_ttl_in_ms (int): The TTL (Time To Live) duration for which the exchanged access token is valid. Measured in milliseconds.
            enabled (bool): If `true`, the API client is permitted to exchange ID Tokens for access tokens. API clients are disabled by default.
            issuer (str): The name of the identity provider that will be issuing ID Tokens for this API client. This string represents the JWT `iss` (issuer) claim in ID Tokens issued for this API client.
            key_id (str): The unique identifier for the associated public key of this API client. This string must match the JWT `kid` (key ID) claim in ID Tokens issued for this API client.
            max_role (FixedReference): The maximum role allowed for ID Tokens issued by this API client. The bearer of an access token will be authorized to perform actions within the intersection of this `max_role` and the role of the array user specified as the JWT `sub` (subject) claim. The `max_role` field is a reference to a `role`. Valid `role`s are `readonly`, `ops_admin`, `array_admin`, and `storage_admin`. Users with the `readonly` (Read Only) role can perform operations that convey the state of the array. Read Only users cannot alter the state of the array. Users with the `ops_admin` (Ops Admin) role can perform the same operations as Read Only users plus enable and disable remote assistance sessions. Ops Admin users cannot alter the state of the array. Users with the `storage_admin` (Storage Admin) role can perform the same operations as Read Only users plus storage related operations, such as administering file systems, snapshots, and buckets. Storage Admin users cannot perform operations that deal with global and system configurations. Users with the `array_admin` (Array Admin) role can perform the same operations as Storage Admin users plus array-wide changes dealing with global and system configurations. In other words, Array Admin users can perform all operations.
            public_key (str): The API client's PEM formatted (Base64 encoded) RSA public key.
        """
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if access_token_ttl_in_ms is not None:
            self.access_token_ttl_in_ms = access_token_ttl_in_ms
        if enabled is not None:
            self.enabled = enabled
        if issuer is not None:
            self.issuer = issuer
        if key_id is not None:
            self.key_id = key_id
        if max_role is not None:
            self.max_role = max_role
        if public_key is not None:
            self.public_key = public_key

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ApiClient`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
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
        if issubclass(ApiClient, dict):
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
        if not isinstance(other, ApiClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
