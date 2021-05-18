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


class APIKeyIntrospectResponse(object):
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
        'sub_org_results': 'list[Token]',
        'primary_token': 'Token',
        'raw_token': 'str'
    }

    attribute_map = {
        'sub_org_results': 'sub_org_results',
        'primary_token': 'primary_token',
        'raw_token': 'raw_token'
    }

    def __init__(self, sub_org_results=None, primary_token=None, raw_token=None, local_vars_configuration=None):  # noqa: E501
        """APIKeyIntrospectResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sub_org_results = None
        self._primary_token = None
        self._raw_token = None
        self.discriminator = None

        self.sub_org_results = sub_org_results
        self.primary_token = primary_token
        if raw_token is not None:
            self.raw_token = raw_token

    @property
    def sub_org_results(self):
        """Gets the sub_org_results of this APIKeyIntrospectResponse.  # noqa: E501

        List of sub org's tokens. Empty if the introspection did not allow for multiple orgs.   # noqa: E501

        :return: The sub_org_results of this APIKeyIntrospectResponse.  # noqa: E501
        :rtype: list[Token]
        """
        return self._sub_org_results

    @sub_org_results.setter
    def sub_org_results(self, sub_org_results):
        """Sets the sub_org_results of this APIKeyIntrospectResponse.

        List of sub org's tokens. Empty if the introspection did not allow for multiple orgs.   # noqa: E501

        :param sub_org_results: The sub_org_results of this APIKeyIntrospectResponse.  # noqa: E501
        :type: list[Token]
        """
        if self.local_vars_configuration.client_side_validation and sub_org_results is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_org_results`, must not be `None`")  # noqa: E501

        self._sub_org_results = sub_org_results

    @property
    def primary_token(self):
        """Gets the primary_token of this APIKeyIntrospectResponse.  # noqa: E501


        :return: The primary_token of this APIKeyIntrospectResponse.  # noqa: E501
        :rtype: Token
        """
        return self._primary_token

    @primary_token.setter
    def primary_token(self, primary_token):
        """Sets the primary_token of this APIKeyIntrospectResponse.


        :param primary_token: The primary_token of this APIKeyIntrospectResponse.  # noqa: E501
        :type: Token
        """
        if self.local_vars_configuration.client_side_validation and primary_token is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_token`, must not be `None`")  # noqa: E501

        self._primary_token = primary_token

    @property
    def raw_token(self):
        """Gets the raw_token of this APIKeyIntrospectResponse.  # noqa: E501

        The raw token backing this API Key. This will be passed onwards to upstream endpoints.   # noqa: E501

        :return: The raw_token of this APIKeyIntrospectResponse.  # noqa: E501
        :rtype: str
        """
        return self._raw_token

    @raw_token.setter
    def raw_token(self, raw_token):
        """Sets the raw_token of this APIKeyIntrospectResponse.

        The raw token backing this API Key. This will be passed onwards to upstream endpoints.   # noqa: E501

        :param raw_token: The raw_token of this APIKeyIntrospectResponse.  # noqa: E501
        :type: str
        """

        self._raw_token = raw_token

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
        if not isinstance(other, APIKeyIntrospectResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIKeyIntrospectResponse):
            return True

        return self.to_dict() != other.to_dict()
