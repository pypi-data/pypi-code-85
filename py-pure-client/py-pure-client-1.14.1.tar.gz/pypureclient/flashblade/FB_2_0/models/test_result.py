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

class TestResult(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'component_address': 'str',
        'component_name': 'str',
        'description': 'str',
        'destination': 'str',
        'enabled': 'bool',
        'resource': 'FixedReference',
        'result_details': 'str',
        'success': 'bool',
        'test_type': 'str'
    }

    attribute_map = {
        'component_address': 'component_address',
        'component_name': 'component_name',
        'description': 'description',
        'destination': 'destination',
        'enabled': 'enabled',
        'resource': 'resource',
        'result_details': 'result_details',
        'success': 'success',
        'test_type': 'test_type'
    }

    required_args = {
    }

    def __init__(
        self,
        component_address=None,  # type: str
        component_name=None,  # type: str
        description=None,  # type: str
        destination=None,  # type: str
        enabled=None,  # type: bool
        resource=None,  # type: models.FixedReference
        result_details=None,  # type: str
        success=None,  # type: bool
        test_type=None,  # type: str
    ):
        """
        Keyword args:
            component_address (str): Address of the component running the test.
            component_name (str): Name of the component running the test.
            description (str): What the test is doing.
            destination (str): The URI of the target server being tested.
            enabled (bool): Is the service enabled or not?
            resource (FixedReference): A reference to the object being tested.
            result_details (str): Additional information about the test result.
            success (bool): Returns a value of `true` if the specified test succeeded. Returns a value of `false` if the specified test failed.
            test_type (str): Displays the type of test being performed. The returned values are determined by the `resource` being tested and its configuration.
        """
        if component_address is not None:
            self.component_address = component_address
        if component_name is not None:
            self.component_name = component_name
        if description is not None:
            self.description = description
        if destination is not None:
            self.destination = destination
        if enabled is not None:
            self.enabled = enabled
        if resource is not None:
            self.resource = resource
        if result_details is not None:
            self.result_details = result_details
        if success is not None:
            self.success = success
        if test_type is not None:
            self.test_type = test_type

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `TestResult`".format(key))
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
        if issubclass(TestResult, dict):
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
        if not isinstance(other, TestResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
