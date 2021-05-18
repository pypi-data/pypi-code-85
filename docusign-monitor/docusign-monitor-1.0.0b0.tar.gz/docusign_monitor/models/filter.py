# coding: utf-8

"""
    DocuSign Monitor API - v2

    An API for an integrator to access the features of DocuSign Monitor  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Filter(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'filter_name': 'str'
    }

    attribute_map = {
        'filter_name': 'filterName'
    }

    def __init__(self, filter_name=None):  # noqa: E501
        """Filter - a model defined in Swagger"""  # noqa: E501

        self._filter_name = None
        self.discriminator = None

        if filter_name is not None:
            self.filter_name = filter_name

    @property
    def filter_name(self):
        """Gets the filter_name of this Filter.  # noqa: E501


        :return: The filter_name of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._filter_name

    @filter_name.setter
    def filter_name(self, filter_name):
        """Sets the filter_name of this Filter.


        :param filter_name: The filter_name of this Filter.  # noqa: E501
        :type: str
        """

        self._filter_name = filter_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Filter, dict):
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
        if not isinstance(other, Filter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
