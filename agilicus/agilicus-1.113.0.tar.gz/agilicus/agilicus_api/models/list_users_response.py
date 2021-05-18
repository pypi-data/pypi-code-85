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


class ListUsersResponse(object):
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
        'users': 'list[User]',
        'limit': 'int',
        'previous_page_email': 'str',
        'next_page_email': 'str'
    }

    attribute_map = {
        'users': 'users',
        'limit': 'limit',
        'previous_page_email': 'previous_page_email',
        'next_page_email': 'next_page_email'
    }

    def __init__(self, users=None, limit=None, previous_page_email=None, next_page_email=None, local_vars_configuration=None):  # noqa: E501
        """ListUsersResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._users = None
        self._limit = None
        self._previous_page_email = None
        self._next_page_email = None
        self.discriminator = None

        if users is not None:
            self.users = users
        self.limit = limit
        if previous_page_email is not None:
            self.previous_page_email = previous_page_email
        if next_page_email is not None:
            self.next_page_email = next_page_email

    @property
    def users(self):
        """Gets the users of this ListUsersResponse.  # noqa: E501

        List of User objects  # noqa: E501

        :return: The users of this ListUsersResponse.  # noqa: E501
        :rtype: list[User]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ListUsersResponse.

        List of User objects  # noqa: E501

        :param users: The users of this ListUsersResponse.  # noqa: E501
        :type: list[User]
        """

        self._users = users

    @property
    def limit(self):
        """Gets the limit of this ListUsersResponse.  # noqa: E501

        Limit on the number of rows in the response  # noqa: E501

        :return: The limit of this ListUsersResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUsersResponse.

        Limit on the number of rows in the response  # noqa: E501

        :param limit: The limit of this ListUsersResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def previous_page_email(self):
        """Gets the previous_page_email of this ListUsersResponse.  # noqa: E501

        The first email on the current page. Can be used with \"backwards\" as the search_direction_query parameter to retrieve the previous page's entries. Is an empty string if the current page is the first page.   # noqa: E501

        :return: The previous_page_email of this ListUsersResponse.  # noqa: E501
        :rtype: str
        """
        return self._previous_page_email

    @previous_page_email.setter
    def previous_page_email(self, previous_page_email):
        """Sets the previous_page_email of this ListUsersResponse.

        The first email on the current page. Can be used with \"backwards\" as the search_direction_query parameter to retrieve the previous page's entries. Is an empty string if the current page is the first page.   # noqa: E501

        :param previous_page_email: The previous_page_email of this ListUsersResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                previous_page_email is not None and len(previous_page_email) > 100):
            raise ValueError("Invalid value for `previous_page_email`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                previous_page_email is not None and len(previous_page_email) < 0):
            raise ValueError("Invalid value for `previous_page_email`, length must be greater than or equal to `0`")  # noqa: E501

        self._previous_page_email = previous_page_email

    @property
    def next_page_email(self):
        """Gets the next_page_email of this ListUsersResponse.  # noqa: E501

        The first email on the next page. Can be used with \"forwards\" as the search_direction_query parameter to retrieve the next page's entries. Is an empty string if the current page is the last page.   # noqa: E501

        :return: The next_page_email of this ListUsersResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_email

    @next_page_email.setter
    def next_page_email(self, next_page_email):
        """Sets the next_page_email of this ListUsersResponse.

        The first email on the next page. Can be used with \"forwards\" as the search_direction_query parameter to retrieve the next page's entries. Is an empty string if the current page is the last page.   # noqa: E501

        :param next_page_email: The next_page_email of this ListUsersResponse.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                next_page_email is not None and len(next_page_email) > 100):
            raise ValueError("Invalid value for `next_page_email`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                next_page_email is not None and len(next_page_email) < 0):
            raise ValueError("Invalid value for `next_page_email`, length must be greater than or equal to `0`")  # noqa: E501

        self._next_page_email = next_page_email

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
        if not isinstance(other, ListUsersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListUsersResponse):
            return True

        return self.to_dict() != other.to_dict()
