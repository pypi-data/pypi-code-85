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

class SoftwareInstallationStepsChecks(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'details': 'str',
        'name': 'str',
        'overridable': 'bool',
        'status': 'str'
    }

    attribute_map = {
        'details': 'details',
        'name': 'name',
        'overridable': 'overridable',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(
        self,
        details=None,  # type: str
        name=None,  # type: str
        overridable=None,  # type: bool
        status=None,  # type: str
    ):
        """
        Keyword args:
            details (str): Detailed result of the check used to diagnose check failures.
            name (str): Name of the upgrade check.
            overridable (bool): Whether the check failure can be overridden.
            status (str): Status of the check. Valid values are `running`, `failed`, `passed`, and `overridden`. A status of `running` indicates that the check has not finished. A status of `failed` indicates that the check has failed. A status of `passed` indicates that the check has passed. A status of `overridden` indicates that the check has failed, but the failure has been overridden.
        """
        if details is not None:
            self.details = details
        if name is not None:
            self.name = name
        if overridable is not None:
            self.overridable = overridable
        if status is not None:
            self.status = status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SoftwareInstallationStepsChecks`".format(key))
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
        if issubclass(SoftwareInstallationStepsChecks, dict):
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
        if not isinstance(other, SoftwareInstallationStepsChecks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
