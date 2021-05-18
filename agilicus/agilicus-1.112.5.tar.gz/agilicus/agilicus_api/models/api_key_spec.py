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


class APIKeySpec(object):
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
        'user_id': 'str',
        'org_id': 'str',
        'expiry': 'datetime',
        'session': 'str',
        'scopes': 'list[str]'
    }

    attribute_map = {
        'user_id': 'user_id',
        'org_id': 'org_id',
        'expiry': 'expiry',
        'session': 'session',
        'scopes': 'scopes'
    }

    def __init__(self, user_id=None, org_id=None, expiry=None, session=None, scopes=None, local_vars_configuration=None):  # noqa: E501
        """APIKeySpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._org_id = None
        self._expiry = None
        self._session = None
        self._scopes = None
        self.discriminator = None

        self.user_id = user_id
        self.org_id = org_id
        if expiry is not None:
            self.expiry = expiry
        if session is not None:
            self.session = session
        if scopes is not None:
            self.scopes = scopes

    @property
    def user_id(self):
        """Gets the user_id of this APIKeySpec.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The user_id of this APIKeySpec.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this APIKeySpec.

        Unique identifier  # noqa: E501

        :param user_id: The user_id of this APIKeySpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def org_id(self):
        """Gets the org_id of this APIKeySpec.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The org_id of this APIKeySpec.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this APIKeySpec.

        Unique identifier  # noqa: E501

        :param org_id: The org_id of this APIKeySpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501

        self._org_id = org_id

    @property
    def expiry(self):
        """Gets the expiry of this APIKeySpec.  # noqa: E501

        The API Key expiry time in UTC. If ommitted the key does not expire.  # noqa: E501

        :return: The expiry of this APIKeySpec.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this APIKeySpec.

        The API Key expiry time in UTC. If ommitted the key does not expire.  # noqa: E501

        :param expiry: The expiry of this APIKeySpec.  # noqa: E501
        :type: datetime
        """

        self._expiry = expiry

    @property
    def session(self):
        """Gets the session of this APIKeySpec.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The session of this APIKeySpec.  # noqa: E501
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this APIKeySpec.

        Unique identifier  # noqa: E501

        :param session: The session of this APIKeySpec.  # noqa: E501
        :type: str
        """

        self._session = session

    @property
    def scopes(self):
        """Gets the scopes of this APIKeySpec.  # noqa: E501

        The list of scopes requested for APIKey. Ex. urn:agilicus:users. An optional scope is specified with an ? at the end. Optional scopes are used when the permission is requested but not required. Ex. urn:agilicus:users?. A non-optional scope will cause creation of this API Key to fail if the user does not have that permission in this org.   # noqa: E501

        :return: The scopes of this APIKeySpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this APIKeySpec.

        The list of scopes requested for APIKey. Ex. urn:agilicus:users. An optional scope is specified with an ? at the end. Optional scopes are used when the permission is requested but not required. Ex. urn:agilicus:users?. A non-optional scope will cause creation of this API Key to fail if the user does not have that permission in this org.   # noqa: E501

        :param scopes: The scopes of this APIKeySpec.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

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
        if not isinstance(other, APIKeySpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIKeySpec):
            return True

        return self.to_dict() != other.to_dict()
