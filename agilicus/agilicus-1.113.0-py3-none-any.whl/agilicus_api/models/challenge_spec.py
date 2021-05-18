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


class ChallengeSpec(object):
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
        'challenge_type': 'str',
        'challenge_types': 'list[str]',
        'user_id': 'str',
        'send_now': 'bool',
        'timeout_seconds': 'int',
        'response_uri': 'str',
        'origin': 'str',
        'challenge_endpoints': 'list[ChallengeEndpoint]'
    }

    attribute_map = {
        'challenge_type': 'challenge_type',
        'challenge_types': 'challenge_types',
        'user_id': 'user_id',
        'send_now': 'send_now',
        'timeout_seconds': 'timeout_seconds',
        'response_uri': 'response_uri',
        'origin': 'origin',
        'challenge_endpoints': 'challenge_endpoints'
    }

    def __init__(self, challenge_type=None, challenge_types=None, user_id=None, send_now=False, timeout_seconds=600, response_uri=None, origin=None, challenge_endpoints=None, local_vars_configuration=None):  # noqa: E501
        """ChallengeSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._challenge_type = None
        self._challenge_types = None
        self._user_id = None
        self._send_now = None
        self._timeout_seconds = None
        self._response_uri = None
        self._origin = None
        self._challenge_endpoints = None
        self.discriminator = None

        if challenge_type is not None:
            self.challenge_type = challenge_type
        if challenge_types is not None:
            self.challenge_types = challenge_types
        self.user_id = user_id
        if send_now is not None:
            self.send_now = send_now
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds
        if response_uri is not None:
            self.response_uri = response_uri
        if origin is not None:
            self.origin = origin
        if challenge_endpoints is not None:
            self.challenge_endpoints = challenge_endpoints

    @property
    def challenge_type(self):
        """Gets the challenge_type of this ChallengeSpec.  # noqa: E501

        The type of challenge to issue. This controls how the user is informed of the challenge, as well as how the challenge can be satisfied. The follow types are supported:   - sms:  a `sms` challenge informs the user via text message of the challenge. The challenge can     be answered via the link provided in the text message. The user can deny the challenge via this     mechanism as well.   - web_push: a `web_push` challenge informs the user of the challenge on every device they have   registered via the web push (rfc8030) mechanism. If the user accepts via the link provided in   the web push, the challenge will be satisfied. The user can deny the challenge via this   mechanism as well.   - totp: a time-based one-time password challenge allows the user to enter the code from their registered   - webauthn: a challenge issued for a specific device the user has possession of. Either a yubikey, or a phone that has a Trusted Platform Module.   device and application. enum: [sms, web_push, totp, webauthn] example: web_push   # noqa: E501

        :return: The challenge_type of this ChallengeSpec.  # noqa: E501
        :rtype: str
        """
        return self._challenge_type

    @challenge_type.setter
    def challenge_type(self, challenge_type):
        """Sets the challenge_type of this ChallengeSpec.

        The type of challenge to issue. This controls how the user is informed of the challenge, as well as how the challenge can be satisfied. The follow types are supported:   - sms:  a `sms` challenge informs the user via text message of the challenge. The challenge can     be answered via the link provided in the text message. The user can deny the challenge via this     mechanism as well.   - web_push: a `web_push` challenge informs the user of the challenge on every device they have   registered via the web push (rfc8030) mechanism. If the user accepts via the link provided in   the web push, the challenge will be satisfied. The user can deny the challenge via this   mechanism as well.   - totp: a time-based one-time password challenge allows the user to enter the code from their registered   - webauthn: a challenge issued for a specific device the user has possession of. Either a yubikey, or a phone that has a Trusted Platform Module.   device and application. enum: [sms, web_push, totp, webauthn] example: web_push   # noqa: E501

        :param challenge_type: The challenge_type of this ChallengeSpec.  # noqa: E501
        :type: str
        """

        self._challenge_type = challenge_type

    @property
    def challenge_types(self):
        """Gets the challenge_types of this ChallengeSpec.  # noqa: E501

        List of acceptable challenge types for this challenge request. The subsequent challenge answer must be one of these types.  # noqa: E501

        :return: The challenge_types of this ChallengeSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._challenge_types

    @challenge_types.setter
    def challenge_types(self, challenge_types):
        """Sets the challenge_types of this ChallengeSpec.

        List of acceptable challenge types for this challenge request. The subsequent challenge answer must be one of these types.  # noqa: E501

        :param challenge_types: The challenge_types of this ChallengeSpec.  # noqa: E501
        :type: list[str]
        """

        self._challenge_types = challenge_types

    @property
    def user_id(self):
        """Gets the user_id of this ChallengeSpec.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The user_id of this ChallengeSpec.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ChallengeSpec.

        Unique identifier  # noqa: E501

        :param user_id: The user_id of this ChallengeSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def send_now(self):
        """Gets the send_now of this ChallengeSpec.  # noqa: E501

        Whether to send the challenge now. If the challenge hasn't yet been set, setting this to true will send the challenge. If the challenge has been sent, changing this has no effect.   # noqa: E501

        :return: The send_now of this ChallengeSpec.  # noqa: E501
        :rtype: bool
        """
        return self._send_now

    @send_now.setter
    def send_now(self, send_now):
        """Sets the send_now of this ChallengeSpec.

        Whether to send the challenge now. If the challenge hasn't yet been set, setting this to true will send the challenge. If the challenge has been sent, changing this has no effect.   # noqa: E501

        :param send_now: The send_now of this ChallengeSpec.  # noqa: E501
        :type: bool
        """

        self._send_now = send_now

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this ChallengeSpec.  # noqa: E501

        For how long the system will accept answers for the challenge. After this time, if the challenge is not in the `challenge_passed` state, it will transition into the `timed_out` state.   # noqa: E501

        :return: The timeout_seconds of this ChallengeSpec.  # noqa: E501
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this ChallengeSpec.

        For how long the system will accept answers for the challenge. After this time, if the challenge is not in the `challenge_passed` state, it will transition into the `timed_out` state.   # noqa: E501

        :param timeout_seconds: The timeout_seconds of this ChallengeSpec.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                timeout_seconds is not None and timeout_seconds > 3600):  # noqa: E501
            raise ValueError("Invalid value for `timeout_seconds`, must be a value less than or equal to `3600`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                timeout_seconds is not None and timeout_seconds < 1):  # noqa: E501
            raise ValueError("Invalid value for `timeout_seconds`, must be a value greater than or equal to `1`")  # noqa: E501

        self._timeout_seconds = timeout_seconds

    @property
    def response_uri(self):
        """Gets the response_uri of this ChallengeSpec.  # noqa: E501

        The base URI which the user should retrieve in order to answer the challenge. It is expected that this will be an HTTP endpoint serving `text/html` content. The final URI that the user should retrieve will be this value, extended with three form parameters that may be used to invoke the `answer` endpoint.   - challenge_answer: A string which is the answer code.   - challenge_uid: the id of the user being challenged.   - challenge_id: the id of the challenge. In the example, this would turn into something like: `https://auth.egov.city/mfa-answer?challenge_answer=supersecret&challenge_uid=1234&challenge_id=5678`   # noqa: E501

        :return: The response_uri of this ChallengeSpec.  # noqa: E501
        :rtype: str
        """
        return self._response_uri

    @response_uri.setter
    def response_uri(self, response_uri):
        """Sets the response_uri of this ChallengeSpec.

        The base URI which the user should retrieve in order to answer the challenge. It is expected that this will be an HTTP endpoint serving `text/html` content. The final URI that the user should retrieve will be this value, extended with three form parameters that may be used to invoke the `answer` endpoint.   - challenge_answer: A string which is the answer code.   - challenge_uid: the id of the user being challenged.   - challenge_id: the id of the challenge. In the example, this would turn into something like: `https://auth.egov.city/mfa-answer?challenge_answer=supersecret&challenge_uid=1234&challenge_id=5678`   # noqa: E501

        :param response_uri: The response_uri of this ChallengeSpec.  # noqa: E501
        :type: str
        """

        self._response_uri = response_uri

    @property
    def origin(self):
        """Gets the origin of this ChallengeSpec.  # noqa: E501

        The origin that is initiating the challenge.  # noqa: E501

        :return: The origin of this ChallengeSpec.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this ChallengeSpec.

        The origin that is initiating the challenge.  # noqa: E501

        :param origin: The origin of this ChallengeSpec.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def challenge_endpoints(self):
        """Gets the challenge_endpoints of this ChallengeSpec.  # noqa: E501

        List of endpoint ids to challenge for this challenge request. At least one entry is required here when the challenge type includes webauthn.  # noqa: E501

        :return: The challenge_endpoints of this ChallengeSpec.  # noqa: E501
        :rtype: list[ChallengeEndpoint]
        """
        return self._challenge_endpoints

    @challenge_endpoints.setter
    def challenge_endpoints(self, challenge_endpoints):
        """Sets the challenge_endpoints of this ChallengeSpec.

        List of endpoint ids to challenge for this challenge request. At least one entry is required here when the challenge type includes webauthn.  # noqa: E501

        :param challenge_endpoints: The challenge_endpoints of this ChallengeSpec.  # noqa: E501
        :type: list[ChallengeEndpoint]
        """

        self._challenge_endpoints = challenge_endpoints

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
        if not isinstance(other, ChallengeSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChallengeSpec):
            return True

        return self.to_dict() != other.to_dict()
