# coding: utf-8

"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.05.14
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class ResourceStatsMetadata(object):
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
        'creation_time': 'datetime',
        'collection_time': 'datetime',
        'receipt_time': 'datetime'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'collection_time': 'collection_time',
        'receipt_time': 'receipt_time'
    }

    def __init__(self, creation_time=None, collection_time=None, receipt_time=None, local_vars_configuration=None):  # noqa: E501
        """ResourceStatsMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._creation_time = None
        self._collection_time = None
        self._receipt_time = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        self.collection_time = collection_time
        if receipt_time is not None:
            self.receipt_time = receipt_time

    @property
    def creation_time(self):
        """Gets the creation_time of this ResourceStatsMetadata.  # noqa: E501

        When the statistics were first created  # noqa: E501

        :return: The creation_time of this ResourceStatsMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this ResourceStatsMetadata.

        When the statistics were first created  # noqa: E501

        :param creation_time: The creation_time of this ResourceStatsMetadata.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def collection_time(self):
        """Gets the collection_time of this ResourceStatsMetadata.  # noqa: E501

        When the statistics were collected  # noqa: E501

        :return: The collection_time of this ResourceStatsMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this ResourceStatsMetadata.

        When the statistics were collected  # noqa: E501

        :param collection_time: The collection_time of this ResourceStatsMetadata.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and collection_time is None:  # noqa: E501
            raise ValueError("Invalid value for `collection_time`, must not be `None`")  # noqa: E501

        self._collection_time = collection_time

    @property
    def receipt_time(self):
        """Gets the receipt_time of this ResourceStatsMetadata.  # noqa: E501

        When the statistics were received for storage  # noqa: E501

        :return: The receipt_time of this ResourceStatsMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._receipt_time

    @receipt_time.setter
    def receipt_time(self, receipt_time):
        """Sets the receipt_time of this ResourceStatsMetadata.

        When the statistics were received for storage  # noqa: E501

        :param receipt_time: The receipt_time of this ResourceStatsMetadata.  # noqa: E501
        :type: datetime
        """

        self._receipt_time = receipt_time

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
        if not isinstance(other, ResourceStatsMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResourceStatsMetadata):
            return True

        return self.to_dict() != other.to_dict()
