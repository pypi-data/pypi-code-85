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


class HttpRule(object):
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
        'rule_type': 'str',
        'methods': 'list[str]',
        'path_regex': 'str',
        'query_parameters': 'list[RuleQueryParameter]',
        'body': 'RuleQueryBody'
    }

    attribute_map = {
        'rule_type': 'rule_type',
        'methods': 'methods',
        'path_regex': 'path_regex',
        'query_parameters': 'query_parameters',
        'body': 'body'
    }

    def __init__(self, rule_type='HttpRule', methods=None, path_regex=None, query_parameters=None, body=None, local_vars_configuration=None):  # noqa: E501
        """HttpRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._rule_type = None
        self._methods = None
        self._path_regex = None
        self._query_parameters = None
        self._body = None
        self.discriminator = None

        self.rule_type = rule_type
        if methods is not None:
            self.methods = methods
        if path_regex is not None:
            self.path_regex = path_regex
        if query_parameters is not None:
            self.query_parameters = query_parameters
        if body is not None:
            self.body = body

    @property
    def rule_type(self):
        """Gets the rule_type of this HttpRule.  # noqa: E501

        Used to distinguish between different types of rule  # noqa: E501

        :return: The rule_type of this HttpRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this HttpRule.

        Used to distinguish between different types of rule  # noqa: E501

        :param rule_type: The rule_type of this HttpRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_type`, must not be `None`")  # noqa: E501

        self._rule_type = rule_type

    @property
    def methods(self):
        """Gets the methods of this HttpRule.  # noqa: E501

        The HTTP methods to allow. If any of the listed methods are matched, then this portion of the rule matches.   # noqa: E501

        :return: The methods of this HttpRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this HttpRule.

        The HTTP methods to allow. If any of the listed methods are matched, then this portion of the rule matches.   # noqa: E501

        :param methods: The methods of this HttpRule.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["get", "put", "post", "delete", "head", "options", "connect", "trace", "patch", "copy", "lock", "mkcol", "move", "propfind", "proppatch", "unlock", "all"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(methods).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `methods` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(methods) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._methods = methods

    @property
    def path_regex(self):
        """Gets the path_regex of this HttpRule.  # noqa: E501

        regex for HTTP path. Can be templatized with jinja2 using definitions collection.  # noqa: E501

        :return: The path_regex of this HttpRule.  # noqa: E501
        :rtype: str
        """
        return self._path_regex

    @path_regex.setter
    def path_regex(self, path_regex):
        """Sets the path_regex of this HttpRule.

        regex for HTTP path. Can be templatized with jinja2 using definitions collection.  # noqa: E501

        :param path_regex: The path_regex of this HttpRule.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                path_regex is not None and len(path_regex) > 512):
            raise ValueError("Invalid value for `path_regex`, length must be less than or equal to `512`")  # noqa: E501

        self._path_regex = path_regex

    @property
    def query_parameters(self):
        """Gets the query_parameters of this HttpRule.  # noqa: E501

        A set of constraints on the parameters specified in the query string.  # noqa: E501

        :return: The query_parameters of this HttpRule.  # noqa: E501
        :rtype: list[RuleQueryParameter]
        """
        return self._query_parameters

    @query_parameters.setter
    def query_parameters(self, query_parameters):
        """Sets the query_parameters of this HttpRule.

        A set of constraints on the parameters specified in the query string.  # noqa: E501

        :param query_parameters: The query_parameters of this HttpRule.  # noqa: E501
        :type: list[RuleQueryParameter]
        """

        self._query_parameters = query_parameters

    @property
    def body(self):
        """Gets the body of this HttpRule.  # noqa: E501


        :return: The body of this HttpRule.  # noqa: E501
        :rtype: RuleQueryBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this HttpRule.


        :param body: The body of this HttpRule.  # noqa: E501
        :type: RuleQueryBody
        """

        self._body = body

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
        if not isinstance(other, HttpRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HttpRule):
            return True

        return self.to_dict() != other.to_dict()
