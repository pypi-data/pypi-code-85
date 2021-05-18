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


class CORSSettings(object):
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
        'enabled': 'bool',
        'origin_matching': 'str',
        'allow_origins': 'list[CORSOrigin]',
        'allow_methods': 'list[str]',
        'allow_headers': 'list[str]',
        'expose_headers': 'list[str]',
        'max_age_seconds': 'int',
        'allow_credentials': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'origin_matching': 'origin_matching',
        'allow_origins': 'allow_origins',
        'allow_methods': 'allow_methods',
        'allow_headers': 'allow_headers',
        'expose_headers': 'expose_headers',
        'max_age_seconds': 'max_age_seconds',
        'allow_credentials': 'allow_credentials'
    }

    def __init__(self, enabled=None, origin_matching=None, allow_origins=None, allow_methods=None, allow_headers=None, expose_headers=None, max_age_seconds=None, allow_credentials=None, local_vars_configuration=None):  # noqa: E501
        """CORSSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enabled = None
        self._origin_matching = None
        self._allow_origins = None
        self._allow_methods = None
        self._allow_headers = None
        self._expose_headers = None
        self._max_age_seconds = None
        self._allow_credentials = None
        self.discriminator = None

        self.enabled = enabled
        self.origin_matching = origin_matching
        self.allow_origins = allow_origins
        self.allow_methods = allow_methods
        self.allow_headers = allow_headers
        self.expose_headers = expose_headers
        self.max_age_seconds = max_age_seconds
        self.allow_credentials = allow_credentials

    @property
    def enabled(self):
        """Gets the enabled of this CORSSettings.  # noqa: E501

        Whether or not to apply the CORS policy. If the policy is disabled, then any CORS headers applied by the application will be passed through unchanged.   # noqa: E501

        :return: The enabled of this CORSSettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CORSSettings.

        Whether or not to apply the CORS policy. If the policy is disabled, then any CORS headers applied by the application will be passed through unchanged.   # noqa: E501

        :param enabled: The enabled of this CORSSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def origin_matching(self):
        """Gets the origin_matching of this CORSSettings.  # noqa: E501

        How to match the origin. Note that in all cases the 'allow_origins' list will be consulted.  - `me`: match the hosts on which this application can be reached.  - `wildcard`: match any host.  - `list`: match only those hosts provided in the `allow_origins` list.   # noqa: E501

        :return: The origin_matching of this CORSSettings.  # noqa: E501
        :rtype: str
        """
        return self._origin_matching

    @origin_matching.setter
    def origin_matching(self, origin_matching):
        """Sets the origin_matching of this CORSSettings.

        How to match the origin. Note that in all cases the 'allow_origins' list will be consulted.  - `me`: match the hosts on which this application can be reached.  - `wildcard`: match any host.  - `list`: match only those hosts provided in the `allow_origins` list.   # noqa: E501

        :param origin_matching: The origin_matching of this CORSSettings.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and origin_matching is None:  # noqa: E501
            raise ValueError("Invalid value for `origin_matching`, must not be `None`")  # noqa: E501
        allowed_values = ["me", "wildcard", "list"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and origin_matching not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `origin_matching` ({0}), must be one of {1}"  # noqa: E501
                .format(origin_matching, allowed_values)
            )

        self._origin_matching = origin_matching

    @property
    def allow_origins(self):
        """Gets the allow_origins of this CORSSettings.  # noqa: E501

        Lists the origins allowed to access the resources of this application. Any matching origin will have its value echoed back in the `Access-Control-Allow-Origin` header.   # noqa: E501

        :return: The allow_origins of this CORSSettings.  # noqa: E501
        :rtype: list[CORSOrigin]
        """
        return self._allow_origins

    @allow_origins.setter
    def allow_origins(self, allow_origins):
        """Sets the allow_origins of this CORSSettings.

        Lists the origins allowed to access the resources of this application. Any matching origin will have its value echoed back in the `Access-Control-Allow-Origin` header.   # noqa: E501

        :param allow_origins: The allow_origins of this CORSSettings.  # noqa: E501
        :type: list[CORSOrigin]
        """
        if self.local_vars_configuration.client_side_validation and allow_origins is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_origins`, must not be `None`")  # noqa: E501

        self._allow_origins = allow_origins

    @property
    def allow_methods(self):
        """Gets the allow_methods of this CORSSettings.  # noqa: E501

        The methods for which to allow access to resources. These correspond to the `Access-Conrol-Allow-Methods` header, into which they are joined by commas. If this value is null, then the methods are wildcarded. Set a value to '*' to wildcard.   # noqa: E501

        :return: The allow_methods of this CORSSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._allow_methods

    @allow_methods.setter
    def allow_methods(self, allow_methods):
        """Sets the allow_methods of this CORSSettings.

        The methods for which to allow access to resources. These correspond to the `Access-Conrol-Allow-Methods` header, into which they are joined by commas. If this value is null, then the methods are wildcarded. Set a value to '*' to wildcard.   # noqa: E501

        :param allow_methods: The allow_methods of this CORSSettings.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and allow_methods is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_methods`, must not be `None`")  # noqa: E501

        self._allow_methods = allow_methods

    @property
    def allow_headers(self):
        """Gets the allow_headers of this CORSSettings.  # noqa: E501

        The headers which may be sent in a request to resources from this application. These correspond to the `Access-Conrol-Allow-Headers` header, into which they are joined by commas. If this value is null, then the headers are wildcarded. Set a value to '*' to wildcard.   # noqa: E501

        :return: The allow_headers of this CORSSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._allow_headers

    @allow_headers.setter
    def allow_headers(self, allow_headers):
        """Sets the allow_headers of this CORSSettings.

        The headers which may be sent in a request to resources from this application. These correspond to the `Access-Conrol-Allow-Headers` header, into which they are joined by commas. If this value is null, then the headers are wildcarded. Set a value to '*' to wildcard.   # noqa: E501

        :param allow_headers: The allow_headers of this CORSSettings.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and allow_headers is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_headers`, must not be `None`")  # noqa: E501

        self._allow_headers = allow_headers

    @property
    def expose_headers(self):
        """Gets the expose_headers of this CORSSettings.  # noqa: E501

        The response headers which the javascript running in the browser may access for resources from this application. These correspond to the `Access-Conrol-Expose-Headers` header, into which they are joined by commas. If this value is null, then the headers are wildcarded. Set a value to '*' to wildcard.   # noqa: E501

        :return: The expose_headers of this CORSSettings.  # noqa: E501
        :rtype: list[str]
        """
        return self._expose_headers

    @expose_headers.setter
    def expose_headers(self, expose_headers):
        """Sets the expose_headers of this CORSSettings.

        The response headers which the javascript running in the browser may access for resources from this application. These correspond to the `Access-Conrol-Expose-Headers` header, into which they are joined by commas. If this value is null, then the headers are wildcarded. Set a value to '*' to wildcard.   # noqa: E501

        :param expose_headers: The expose_headers of this CORSSettings.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and expose_headers is None:  # noqa: E501
            raise ValueError("Invalid value for `expose_headers`, must not be `None`")  # noqa: E501

        self._expose_headers = expose_headers

    @property
    def max_age_seconds(self):
        """Gets the max_age_seconds of this CORSSettings.  # noqa: E501

        This sets the `Access-Control-Max-Age` which controls the maximum number of seconds for which the results of the CORS preflight check may be cached. -1 disables caching.   # noqa: E501

        :return: The max_age_seconds of this CORSSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_age_seconds

    @max_age_seconds.setter
    def max_age_seconds(self, max_age_seconds):
        """Sets the max_age_seconds of this CORSSettings.

        This sets the `Access-Control-Max-Age` which controls the maximum number of seconds for which the results of the CORS preflight check may be cached. -1 disables caching.   # noqa: E501

        :param max_age_seconds: The max_age_seconds of this CORSSettings.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_age_seconds is None:  # noqa: E501
            raise ValueError("Invalid value for `max_age_seconds`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_age_seconds is not None and max_age_seconds < -1):  # noqa: E501
            raise ValueError("Invalid value for `max_age_seconds`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._max_age_seconds = max_age_seconds

    @property
    def allow_credentials(self):
        """Gets the allow_credentials of this CORSSettings.  # noqa: E501

        Whether credentials may be sent in requests. This corresponds to the `Access-Control-Allow-Credentials` header.   # noqa: E501

        :return: The allow_credentials of this CORSSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_credentials

    @allow_credentials.setter
    def allow_credentials(self, allow_credentials):
        """Sets the allow_credentials of this CORSSettings.

        Whether credentials may be sent in requests. This corresponds to the `Access-Control-Allow-Credentials` header.   # noqa: E501

        :param allow_credentials: The allow_credentials of this CORSSettings.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_credentials is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_credentials`, must not be `None`")  # noqa: E501

        self._allow_credentials = allow_credentials

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
        if not isinstance(other, CORSSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CORSSettings):
            return True

        return self.to_dict() != other.to_dict()
