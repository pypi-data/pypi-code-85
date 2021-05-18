# coding: utf-8

"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.05.18
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class AgentConnectorProxyRequestStats(object):
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
        'last_request_start_time': 'datetime',
        'bytes_received': 'int',
        'bytes_sent': 'int',
        'requests': 'AgentConnectorProxyRequestStatsDetails'
    }

    attribute_map = {
        'last_request_start_time': 'last_request_start_time',
        'bytes_received': 'bytes_received',
        'bytes_sent': 'bytes_sent',
        'requests': 'requests'
    }

    def __init__(self, last_request_start_time=None, bytes_received=None, bytes_sent=None, requests=None, local_vars_configuration=None):  # noqa: E501
        """AgentConnectorProxyRequestStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_request_start_time = None
        self._bytes_received = None
        self._bytes_sent = None
        self._requests = None
        self.discriminator = None

        if last_request_start_time is not None:
            self.last_request_start_time = last_request_start_time
        self.bytes_received = bytes_received
        self.bytes_sent = bytes_sent
        self.requests = requests

    @property
    def last_request_start_time(self):
        """Gets the last_request_start_time of this AgentConnectorProxyRequestStats.  # noqa: E501

        When the last request handled by this proxy was started. Note that the request may still be in flight.   # noqa: E501

        :return: The last_request_start_time of this AgentConnectorProxyRequestStats.  # noqa: E501
        :rtype: datetime
        """
        return self._last_request_start_time

    @last_request_start_time.setter
    def last_request_start_time(self, last_request_start_time):
        """Sets the last_request_start_time of this AgentConnectorProxyRequestStats.

        When the last request handled by this proxy was started. Note that the request may still be in flight.   # noqa: E501

        :param last_request_start_time: The last_request_start_time of this AgentConnectorProxyRequestStats.  # noqa: E501
        :type: datetime
        """

        self._last_request_start_time = last_request_start_time

    @property
    def bytes_received(self):
        """Gets the bytes_received of this AgentConnectorProxyRequestStats.  # noqa: E501

        The number of bytes, including headers, received by the proxy.  # noqa: E501

        :return: The bytes_received of this AgentConnectorProxyRequestStats.  # noqa: E501
        :rtype: int
        """
        return self._bytes_received

    @bytes_received.setter
    def bytes_received(self, bytes_received):
        """Sets the bytes_received of this AgentConnectorProxyRequestStats.

        The number of bytes, including headers, received by the proxy.  # noqa: E501

        :param bytes_received: The bytes_received of this AgentConnectorProxyRequestStats.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bytes_received is None:  # noqa: E501
            raise ValueError("Invalid value for `bytes_received`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bytes_received is not None and bytes_received < 0):  # noqa: E501
            raise ValueError("Invalid value for `bytes_received`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bytes_received = bytes_received

    @property
    def bytes_sent(self):
        """Gets the bytes_sent of this AgentConnectorProxyRequestStats.  # noqa: E501

        The number of bytes, including headers, sent by the proxy.  # noqa: E501

        :return: The bytes_sent of this AgentConnectorProxyRequestStats.  # noqa: E501
        :rtype: int
        """
        return self._bytes_sent

    @bytes_sent.setter
    def bytes_sent(self, bytes_sent):
        """Sets the bytes_sent of this AgentConnectorProxyRequestStats.

        The number of bytes, including headers, sent by the proxy.  # noqa: E501

        :param bytes_sent: The bytes_sent of this AgentConnectorProxyRequestStats.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and bytes_sent is None:  # noqa: E501
            raise ValueError("Invalid value for `bytes_sent`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                bytes_sent is not None and bytes_sent < 0):  # noqa: E501
            raise ValueError("Invalid value for `bytes_sent`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bytes_sent = bytes_sent

    @property
    def requests(self):
        """Gets the requests of this AgentConnectorProxyRequestStats.  # noqa: E501


        :return: The requests of this AgentConnectorProxyRequestStats.  # noqa: E501
        :rtype: AgentConnectorProxyRequestStatsDetails
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this AgentConnectorProxyRequestStats.


        :param requests: The requests of this AgentConnectorProxyRequestStats.  # noqa: E501
        :type: AgentConnectorProxyRequestStatsDetails
        """
        if self.local_vars_configuration.client_side_validation and requests is None:  # noqa: E501
            raise ValueError("Invalid value for `requests`, must not be `None`")  # noqa: E501

        self._requests = requests

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
        if not isinstance(other, AgentConnectorProxyRequestStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentConnectorProxyRequestStats):
            return True

        return self.to_dict() != other.to_dict()
