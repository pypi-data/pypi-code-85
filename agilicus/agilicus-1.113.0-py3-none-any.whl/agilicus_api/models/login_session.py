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


class LoginSession(object):
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
        'session_id': 'str',
        'number_of_logins': 'int',
        'number_of_failed_multi_factor_challenges': 'int',
        'single_sign_on_time': 'datetime',
        'user_is_authenticated': 'bool',
        'user_is_authenticated_by_upstream': 'bool',
        'user_is_authenticated_by_cache': 'bool'
    }

    attribute_map = {
        'session_id': 'session_id',
        'number_of_logins': 'number_of_logins',
        'number_of_failed_multi_factor_challenges': 'number_of_failed_multi_factor_challenges',
        'single_sign_on_time': 'single_sign_on_time',
        'user_is_authenticated': 'user_is_authenticated',
        'user_is_authenticated_by_upstream': 'user_is_authenticated_by_upstream',
        'user_is_authenticated_by_cache': 'user_is_authenticated_by_cache'
    }

    def __init__(self, session_id=None, number_of_logins=None, number_of_failed_multi_factor_challenges=None, single_sign_on_time=None, user_is_authenticated=False, user_is_authenticated_by_upstream=False, user_is_authenticated_by_cache=False, local_vars_configuration=None):  # noqa: E501
        """LoginSession - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._session_id = None
        self._number_of_logins = None
        self._number_of_failed_multi_factor_challenges = None
        self._single_sign_on_time = None
        self._user_is_authenticated = None
        self._user_is_authenticated_by_upstream = None
        self._user_is_authenticated_by_cache = None
        self.discriminator = None

        self.session_id = session_id
        self.number_of_logins = number_of_logins
        self.number_of_failed_multi_factor_challenges = number_of_failed_multi_factor_challenges
        self.single_sign_on_time = single_sign_on_time
        self.user_is_authenticated = user_is_authenticated
        self.user_is_authenticated_by_upstream = user_is_authenticated_by_upstream
        self.user_is_authenticated_by_cache = user_is_authenticated_by_cache

    @property
    def session_id(self):
        """Gets the session_id of this LoginSession.  # noqa: E501

        The id of the session.  # noqa: E501

        :return: The session_id of this LoginSession.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this LoginSession.

        The id of the session.  # noqa: E501

        :param session_id: The session_id of this LoginSession.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and session_id is None:  # noqa: E501
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def number_of_logins(self):
        """Gets the number_of_logins of this LoginSession.  # noqa: E501

        The number of logins that have occured with this session id  # noqa: E501

        :return: The number_of_logins of this LoginSession.  # noqa: E501
        :rtype: int
        """
        return self._number_of_logins

    @number_of_logins.setter
    def number_of_logins(self, number_of_logins):
        """Sets the number_of_logins of this LoginSession.

        The number of logins that have occured with this session id  # noqa: E501

        :param number_of_logins: The number_of_logins of this LoginSession.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_logins is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_logins`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_of_logins is not None and number_of_logins < 0):  # noqa: E501
            raise ValueError("Invalid value for `number_of_logins`, must be a value greater than or equal to `0`")  # noqa: E501

        self._number_of_logins = number_of_logins

    @property
    def number_of_failed_multi_factor_challenges(self):
        """Gets the number_of_failed_multi_factor_challenges of this LoginSession.  # noqa: E501

        The number of failed multi-factor authentication challenges that have occured with this session id  # noqa: E501

        :return: The number_of_failed_multi_factor_challenges of this LoginSession.  # noqa: E501
        :rtype: int
        """
        return self._number_of_failed_multi_factor_challenges

    @number_of_failed_multi_factor_challenges.setter
    def number_of_failed_multi_factor_challenges(self, number_of_failed_multi_factor_challenges):
        """Sets the number_of_failed_multi_factor_challenges of this LoginSession.

        The number of failed multi-factor authentication challenges that have occured with this session id  # noqa: E501

        :param number_of_failed_multi_factor_challenges: The number_of_failed_multi_factor_challenges of this LoginSession.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number_of_failed_multi_factor_challenges is None:  # noqa: E501
            raise ValueError("Invalid value for `number_of_failed_multi_factor_challenges`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number_of_failed_multi_factor_challenges is not None and number_of_failed_multi_factor_challenges < 0):  # noqa: E501
            raise ValueError("Invalid value for `number_of_failed_multi_factor_challenges`, must be a value greater than or equal to `0`")  # noqa: E501

        self._number_of_failed_multi_factor_challenges = number_of_failed_multi_factor_challenges

    @property
    def single_sign_on_time(self):
        """Gets the single_sign_on_time of this LoginSession.  # noqa: E501

        The time of the user's last login with an upstream identity provider if the policy supported single sign on.  # noqa: E501

        :return: The single_sign_on_time of this LoginSession.  # noqa: E501
        :rtype: datetime
        """
        return self._single_sign_on_time

    @single_sign_on_time.setter
    def single_sign_on_time(self, single_sign_on_time):
        """Sets the single_sign_on_time of this LoginSession.

        The time of the user's last login with an upstream identity provider if the policy supported single sign on.  # noqa: E501

        :param single_sign_on_time: The single_sign_on_time of this LoginSession.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and single_sign_on_time is None:  # noqa: E501
            raise ValueError("Invalid value for `single_sign_on_time`, must not be `None`")  # noqa: E501

        self._single_sign_on_time = single_sign_on_time

    @property
    def user_is_authenticated(self):
        """Gets the user_is_authenticated of this LoginSession.  # noqa: E501

        An aggregate condition representing the user's authentication status in the session. This field is the result of user_is_authenticated_by_upstream OR'd with user_is_authenticated_by_cache   # noqa: E501

        :return: The user_is_authenticated of this LoginSession.  # noqa: E501
        :rtype: bool
        """
        return self._user_is_authenticated

    @user_is_authenticated.setter
    def user_is_authenticated(self, user_is_authenticated):
        """Sets the user_is_authenticated of this LoginSession.

        An aggregate condition representing the user's authentication status in the session. This field is the result of user_is_authenticated_by_upstream OR'd with user_is_authenticated_by_cache   # noqa: E501

        :param user_is_authenticated: The user_is_authenticated of this LoginSession.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and user_is_authenticated is None:  # noqa: E501
            raise ValueError("Invalid value for `user_is_authenticated`, must not be `None`")  # noqa: E501

        self._user_is_authenticated = user_is_authenticated

    @property
    def user_is_authenticated_by_upstream(self):
        """Gets the user_is_authenticated_by_upstream of this LoginSession.  # noqa: E501

        Indicates whether the user has been directly authenticated by an upstream identity provider  # noqa: E501

        :return: The user_is_authenticated_by_upstream of this LoginSession.  # noqa: E501
        :rtype: bool
        """
        return self._user_is_authenticated_by_upstream

    @user_is_authenticated_by_upstream.setter
    def user_is_authenticated_by_upstream(self, user_is_authenticated_by_upstream):
        """Sets the user_is_authenticated_by_upstream of this LoginSession.

        Indicates whether the user has been directly authenticated by an upstream identity provider  # noqa: E501

        :param user_is_authenticated_by_upstream: The user_is_authenticated_by_upstream of this LoginSession.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and user_is_authenticated_by_upstream is None:  # noqa: E501
            raise ValueError("Invalid value for `user_is_authenticated_by_upstream`, must not be `None`")  # noqa: E501

        self._user_is_authenticated_by_upstream = user_is_authenticated_by_upstream

    @property
    def user_is_authenticated_by_cache(self):
        """Gets the user_is_authenticated_by_cache of this LoginSession.  # noqa: E501

        Indicates whether the user has been authenticated via a cached credential  # noqa: E501

        :return: The user_is_authenticated_by_cache of this LoginSession.  # noqa: E501
        :rtype: bool
        """
        return self._user_is_authenticated_by_cache

    @user_is_authenticated_by_cache.setter
    def user_is_authenticated_by_cache(self, user_is_authenticated_by_cache):
        """Sets the user_is_authenticated_by_cache of this LoginSession.

        Indicates whether the user has been authenticated via a cached credential  # noqa: E501

        :param user_is_authenticated_by_cache: The user_is_authenticated_by_cache of this LoginSession.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and user_is_authenticated_by_cache is None:  # noqa: E501
            raise ValueError("Invalid value for `user_is_authenticated_by_cache`, must not be `None`")  # noqa: E501

        self._user_is_authenticated_by_cache = user_is_authenticated_by_cache

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
        if not isinstance(other, LoginSession):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoginSession):
            return True

        return self.to_dict() != other.to_dict()
