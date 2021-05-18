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


class Catalogue(object):
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
        'id': 'str',
        'category': 'str',
        'catalogue_entries': 'list[CatalogueEntry]',
        'created': 'datetime',
        'updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'catalogue_entries': 'catalogue_entries',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, category=None, catalogue_entries=None, created=None, updated=None, local_vars_configuration=None):  # noqa: E501
        """Catalogue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._category = None
        self._catalogue_entries = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if catalogue_entries is not None:
            self.catalogue_entries = catalogue_entries
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this Catalogue.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this Catalogue.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Catalogue.

        Unique identifier  # noqa: E501

        :param id: The id of this Catalogue.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def category(self):
        """Gets the category of this Catalogue.  # noqa: E501

        The category of catalogue that this catalogue belongs to.  # noqa: E501

        :return: The category of this Catalogue.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Catalogue.

        The category of catalogue that this catalogue belongs to.  # noqa: E501

        :param category: The category of this Catalogue.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) > 100):
            raise ValueError("Invalid value for `category`, length must be less than or equal to `100`")  # noqa: E501

        self._category = category

    @property
    def catalogue_entries(self):
        """Gets the catalogue_entries of this Catalogue.  # noqa: E501

        The list of catalogue entries for the catalogue  # noqa: E501

        :return: The catalogue_entries of this Catalogue.  # noqa: E501
        :rtype: list[CatalogueEntry]
        """
        return self._catalogue_entries

    @catalogue_entries.setter
    def catalogue_entries(self, catalogue_entries):
        """Sets the catalogue_entries of this Catalogue.

        The list of catalogue entries for the catalogue  # noqa: E501

        :param catalogue_entries: The catalogue_entries of this Catalogue.  # noqa: E501
        :type: list[CatalogueEntry]
        """

        self._catalogue_entries = catalogue_entries

    @property
    def created(self):
        """Gets the created of this Catalogue.  # noqa: E501

        Creation time  # noqa: E501

        :return: The created of this Catalogue.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Catalogue.

        Creation time  # noqa: E501

        :param created: The created of this Catalogue.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this Catalogue.  # noqa: E501

        Update time  # noqa: E501

        :return: The updated of this Catalogue.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Catalogue.

        Update time  # noqa: E501

        :param updated: The updated of this Catalogue.  # noqa: E501
        :type: datetime
        """

        self._updated = updated

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
        if not isinstance(other, Catalogue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Catalogue):
            return True

        return self.to_dict() != other.to_dict()
