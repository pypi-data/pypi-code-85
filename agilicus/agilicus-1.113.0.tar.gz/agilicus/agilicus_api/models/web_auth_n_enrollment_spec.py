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


class WebAuthNEnrollmentSpec(object):
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
        'relying_party_id': 'str',
        'attestation_format': 'str',
        'attestation_conveyance': 'str',
        'user_verification': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'relying_party_id': 'relying_party_id',
        'attestation_format': 'attestation_format',
        'attestation_conveyance': 'attestation_conveyance',
        'user_verification': 'user_verification'
    }

    def __init__(self, user_id=None, relying_party_id=None, attestation_format=None, attestation_conveyance=None, user_verification='discouraged', local_vars_configuration=None):  # noqa: E501
        """WebAuthNEnrollmentSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._relying_party_id = None
        self._attestation_format = None
        self._attestation_conveyance = None
        self._user_verification = None
        self.discriminator = None

        self.user_id = user_id
        self.relying_party_id = relying_party_id
        if attestation_format is not None:
            self.attestation_format = attestation_format
        if attestation_conveyance is not None:
            self.attestation_conveyance = attestation_conveyance
        if user_verification is not None:
            self.user_verification = user_verification

    @property
    def user_id(self):
        """Gets the user_id of this WebAuthNEnrollmentSpec.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The user_id of this WebAuthNEnrollmentSpec.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this WebAuthNEnrollmentSpec.

        Unique identifier  # noqa: E501

        :param user_id: The user_id of this WebAuthNEnrollmentSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def relying_party_id(self):
        """Gets the relying_party_id of this WebAuthNEnrollmentSpec.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The relying_party_id of this WebAuthNEnrollmentSpec.  # noqa: E501
        :rtype: str
        """
        return self._relying_party_id

    @relying_party_id.setter
    def relying_party_id(self, relying_party_id):
        """Sets the relying_party_id of this WebAuthNEnrollmentSpec.

        Unique identifier  # noqa: E501

        :param relying_party_id: The relying_party_id of this WebAuthNEnrollmentSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and relying_party_id is None:  # noqa: E501
            raise ValueError("Invalid value for `relying_party_id`, must not be `None`")  # noqa: E501

        self._relying_party_id = relying_party_id

    @property
    def attestation_format(self):
        """Gets the attestation_format of this WebAuthNEnrollmentSpec.  # noqa: E501

        The format of the attestation statement for this challenge.  # noqa: E501

        :return: The attestation_format of this WebAuthNEnrollmentSpec.  # noqa: E501
        :rtype: str
        """
        return self._attestation_format

    @attestation_format.setter
    def attestation_format(self, attestation_format):
        """Sets the attestation_format of this WebAuthNEnrollmentSpec.

        The format of the attestation statement for this challenge.  # noqa: E501

        :param attestation_format: The attestation_format of this WebAuthNEnrollmentSpec.  # noqa: E501
        :type: str
        """

        self._attestation_format = attestation_format

    @property
    def attestation_conveyance(self):
        """Gets the attestation_conveyance of this WebAuthNEnrollmentSpec.  # noqa: E501

        The relying parties attestation conveyance preference.  # noqa: E501

        :return: The attestation_conveyance of this WebAuthNEnrollmentSpec.  # noqa: E501
        :rtype: str
        """
        return self._attestation_conveyance

    @attestation_conveyance.setter
    def attestation_conveyance(self, attestation_conveyance):
        """Sets the attestation_conveyance of this WebAuthNEnrollmentSpec.

        The relying parties attestation conveyance preference.  # noqa: E501

        :param attestation_conveyance: The attestation_conveyance of this WebAuthNEnrollmentSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["direct", "indirect", "none"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and attestation_conveyance not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `attestation_conveyance` ({0}), must be one of {1}"  # noqa: E501
                .format(attestation_conveyance, allowed_values)
            )

        self._attestation_conveyance = attestation_conveyance

    @property
    def user_verification(self):
        """Gets the user_verification of this WebAuthNEnrollmentSpec.  # noqa: E501

        A WebAuthn Relying Party may require user verification for some of its operations but not for others, and may use this type to express its needs.   # noqa: E501

        :return: The user_verification of this WebAuthNEnrollmentSpec.  # noqa: E501
        :rtype: str
        """
        return self._user_verification

    @user_verification.setter
    def user_verification(self, user_verification):
        """Sets the user_verification of this WebAuthNEnrollmentSpec.

        A WebAuthn Relying Party may require user verification for some of its operations but not for others, and may use this type to express its needs.   # noqa: E501

        :param user_verification: The user_verification of this WebAuthNEnrollmentSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["required", "preferred", "discouraged"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and user_verification not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `user_verification` ({0}), must be one of {1}"  # noqa: E501
                .format(user_verification, allowed_values)
            )

        self._user_verification = user_verification

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
        if not isinstance(other, WebAuthNEnrollmentSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebAuthNEnrollmentSpec):
            return True

        return self.to_dict() != other.to_dict()
