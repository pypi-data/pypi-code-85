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


class MFAChallengeQuestionLoginInfo(object):
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
        'user_preference': 'str',
        'client_id': 'str',
        'client_guid': 'str',
        'issuer_org_id': 'str',
        'issuer_guid': 'str',
        'org_id': 'str',
        'user_id': 'str',
        'user_object': 'UserSummary',
        'login_session': 'LoginSession',
        'upstream_idp': 'str',
        'ip_address': 'str',
        'amr_claim_present': 'bool',
        'last_mfa_login': 'datetime',
        'user_mfa_preferences': 'list[MFAChallengeMethod]'
    }

    attribute_map = {
        'user_preference': 'user_preference',
        'client_id': 'client_id',
        'client_guid': 'client_guid',
        'issuer_org_id': 'issuer_org_id',
        'issuer_guid': 'issuer_guid',
        'org_id': 'org_id',
        'user_id': 'user_id',
        'user_object': 'user_object',
        'login_session': 'login_session',
        'upstream_idp': 'upstream_idp',
        'ip_address': 'ip_address',
        'amr_claim_present': 'amr_claim_present',
        'last_mfa_login': 'last_mfa_login',
        'user_mfa_preferences': 'user_mfa_preferences'
    }

    def __init__(self, user_preference='organisation_policy', client_id=None, client_guid=None, issuer_org_id=None, issuer_guid=None, org_id=None, user_id=None, user_object=None, login_session=None, upstream_idp=None, ip_address=None, amr_claim_present=False, last_mfa_login=None, user_mfa_preferences=None, local_vars_configuration=None):  # noqa: E501
        """MFAChallengeQuestionLoginInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_preference = None
        self._client_id = None
        self._client_guid = None
        self._issuer_org_id = None
        self._issuer_guid = None
        self._org_id = None
        self._user_id = None
        self._user_object = None
        self._login_session = None
        self._upstream_idp = None
        self._ip_address = None
        self._amr_claim_present = None
        self._last_mfa_login = None
        self._user_mfa_preferences = None
        self.discriminator = None

        self.user_preference = user_preference
        self.client_id = client_id
        self.client_guid = client_guid
        self.issuer_org_id = issuer_org_id
        self.issuer_guid = issuer_guid
        self.org_id = org_id
        self.user_id = user_id
        if user_object is not None:
            self.user_object = user_object
        if login_session is not None:
            self.login_session = login_session
        self.upstream_idp = upstream_idp
        self.ip_address = ip_address
        self.amr_claim_present = amr_claim_present
        if last_mfa_login is not None:
            self.last_mfa_login = last_mfa_login
        if user_mfa_preferences is not None:
            self.user_mfa_preferences = user_mfa_preferences

    @property
    def user_preference(self):
        """Gets the user_preference of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The user's preference regarding multi-factor authentication  # noqa: E501

        :return: The user_preference of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_preference

    @user_preference.setter
    def user_preference(self, user_preference):
        """Sets the user_preference of this MFAChallengeQuestionLoginInfo.

        The user's preference regarding multi-factor authentication  # noqa: E501

        :param user_preference: The user_preference of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_preference is None:  # noqa: E501
            raise ValueError("Invalid value for `user_preference`, must not be `None`")  # noqa: E501
        allowed_values = ["always", "organisation_policy"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and user_preference not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `user_preference` ({0}), must be one of {1}"  # noqa: E501
                .format(user_preference, allowed_values)
            )

        self._user_preference = user_preference

    @property
    def client_id(self):
        """Gets the client_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The common name of the client initiating the request on behalf of the user  # noqa: E501

        :return: The client_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this MFAChallengeQuestionLoginInfo.

        The common name of the client initiating the request on behalf of the user  # noqa: E501

        :param client_id: The client_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                client_id is not None and len(client_id) > 100):
            raise ValueError("Invalid value for `client_id`, length must be less than or equal to `100`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_guid(self):
        """Gets the client_guid of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The guid of the client initiating the request on behalf of the user  # noqa: E501

        :return: The client_guid of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._client_guid

    @client_guid.setter
    def client_guid(self, client_guid):
        """Sets the client_guid of this MFAChallengeQuestionLoginInfo.

        The guid of the client initiating the request on behalf of the user  # noqa: E501

        :param client_guid: The client_guid of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_guid is None:  # noqa: E501
            raise ValueError("Invalid value for `client_guid`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                client_guid is not None and len(client_guid) > 40):
            raise ValueError("Invalid value for `client_guid`, length must be less than or equal to `40`")  # noqa: E501

        self._client_guid = client_guid

    @property
    def issuer_org_id(self):
        """Gets the issuer_org_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The id of the organisation for the issuer the user is logging in through  # noqa: E501

        :return: The issuer_org_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._issuer_org_id

    @issuer_org_id.setter
    def issuer_org_id(self, issuer_org_id):
        """Sets the issuer_org_id of this MFAChallengeQuestionLoginInfo.

        The id of the organisation for the issuer the user is logging in through  # noqa: E501

        :param issuer_org_id: The issuer_org_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and issuer_org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `issuer_org_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                issuer_org_id is not None and len(issuer_org_id) > 40):
            raise ValueError("Invalid value for `issuer_org_id`, length must be less than or equal to `40`")  # noqa: E501

        self._issuer_org_id = issuer_org_id

    @property
    def issuer_guid(self):
        """Gets the issuer_guid of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The guid of the issuer the user is logging into.  # noqa: E501

        :return: The issuer_guid of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._issuer_guid

    @issuer_guid.setter
    def issuer_guid(self, issuer_guid):
        """Sets the issuer_guid of this MFAChallengeQuestionLoginInfo.

        The guid of the issuer the user is logging into.  # noqa: E501

        :param issuer_guid: The issuer_guid of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and issuer_guid is None:  # noqa: E501
            raise ValueError("Invalid value for `issuer_guid`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                issuer_guid is not None and len(issuer_guid) > 40):
            raise ValueError("Invalid value for `issuer_guid`, length must be less than or equal to `40`")  # noqa: E501

        self._issuer_guid = issuer_guid

    @property
    def org_id(self):
        """Gets the org_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The id of the organisation the user is a member of  # noqa: E501

        :return: The org_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this MFAChallengeQuestionLoginInfo.

        The id of the organisation the user is a member of  # noqa: E501

        :param org_id: The org_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and org_id is None:  # noqa: E501
            raise ValueError("Invalid value for `org_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                org_id is not None and len(org_id) > 40):
            raise ValueError("Invalid value for `org_id`, length must be less than or equal to `40`")  # noqa: E501

        self._org_id = org_id

    @property
    def user_id(self):
        """Gets the user_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The id of the user requesting access  # noqa: E501

        :return: The user_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MFAChallengeQuestionLoginInfo.

        The id of the user requesting access  # noqa: E501

        :param user_id: The user_id of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) > 40):
            raise ValueError("Invalid value for `user_id`, length must be less than or equal to `40`")  # noqa: E501

        self._user_id = user_id

    @property
    def user_object(self):
        """Gets the user_object of this MFAChallengeQuestionLoginInfo.  # noqa: E501


        :return: The user_object of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: UserSummary
        """
        return self._user_object

    @user_object.setter
    def user_object(self, user_object):
        """Sets the user_object of this MFAChallengeQuestionLoginInfo.


        :param user_object: The user_object of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: UserSummary
        """

        self._user_object = user_object

    @property
    def login_session(self):
        """Gets the login_session of this MFAChallengeQuestionLoginInfo.  # noqa: E501


        :return: The login_session of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: LoginSession
        """
        return self._login_session

    @login_session.setter
    def login_session(self, login_session):
        """Sets the login_session of this MFAChallengeQuestionLoginInfo.


        :param login_session: The login_session of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: LoginSession
        """

        self._login_session = login_session

    @property
    def upstream_idp(self):
        """Gets the upstream_idp of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The upstream IDP that the user is authenticating against  # noqa: E501

        :return: The upstream_idp of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._upstream_idp

    @upstream_idp.setter
    def upstream_idp(self, upstream_idp):
        """Sets the upstream_idp of this MFAChallengeQuestionLoginInfo.

        The upstream IDP that the user is authenticating against  # noqa: E501

        :param upstream_idp: The upstream_idp of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and upstream_idp is None:  # noqa: E501
            raise ValueError("Invalid value for `upstream_idp`, must not be `None`")  # noqa: E501

        self._upstream_idp = upstream_idp

    @property
    def ip_address(self):
        """Gets the ip_address of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The source ip address of the user's request. Both IPv4 and IPv6 address are supported  # noqa: E501

        :return: The ip_address of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this MFAChallengeQuestionLoginInfo.

        The source ip address of the user's request. Both IPv4 and IPv6 address are supported  # noqa: E501

        :param ip_address: The ip_address of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ip_address is None:  # noqa: E501
            raise ValueError("Invalid value for `ip_address`, must not be `None`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def amr_claim_present(self):
        """Gets the amr_claim_present of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        Whether the amr claim is present in the response from the upstream  # noqa: E501

        :return: The amr_claim_present of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: bool
        """
        return self._amr_claim_present

    @amr_claim_present.setter
    def amr_claim_present(self, amr_claim_present):
        """Sets the amr_claim_present of this MFAChallengeQuestionLoginInfo.

        Whether the amr claim is present in the response from the upstream  # noqa: E501

        :param amr_claim_present: The amr_claim_present of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and amr_claim_present is None:  # noqa: E501
            raise ValueError("Invalid value for `amr_claim_present`, must not be `None`")  # noqa: E501

        self._amr_claim_present = amr_claim_present

    @property
    def last_mfa_login(self):
        """Gets the last_mfa_login of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The time of the user's last successful multi-factor authenticated login  # noqa: E501

        :return: The last_mfa_login of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._last_mfa_login

    @last_mfa_login.setter
    def last_mfa_login(self, last_mfa_login):
        """Sets the last_mfa_login of this MFAChallengeQuestionLoginInfo.

        The time of the user's last successful multi-factor authenticated login  # noqa: E501

        :param last_mfa_login: The last_mfa_login of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: datetime
        """

        self._last_mfa_login = last_mfa_login

    @property
    def user_mfa_preferences(self):
        """Gets the user_mfa_preferences of this MFAChallengeQuestionLoginInfo.  # noqa: E501

        The list of a user's multi-factor challenge methods  # noqa: E501

        :return: The user_mfa_preferences of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :rtype: list[MFAChallengeMethod]
        """
        return self._user_mfa_preferences

    @user_mfa_preferences.setter
    def user_mfa_preferences(self, user_mfa_preferences):
        """Sets the user_mfa_preferences of this MFAChallengeQuestionLoginInfo.

        The list of a user's multi-factor challenge methods  # noqa: E501

        :param user_mfa_preferences: The user_mfa_preferences of this MFAChallengeQuestionLoginInfo.  # noqa: E501
        :type: list[MFAChallengeMethod]
        """

        self._user_mfa_preferences = user_mfa_preferences

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
        if not isinstance(other, MFAChallengeQuestionLoginInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MFAChallengeQuestionLoginInfo):
            return True

        return self.to_dict() != other.to_dict()
