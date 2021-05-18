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


class FileSummary(object):
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
        'name': 'str',
        'tag': 'str',
        'label': 'str',
        'size': 'int',
        'visibility': 'FileVisibility',
        'public_url': 'str',
        'storage_path': 'str',
        'last_accessed': 'datetime',
        'created': 'datetime',
        'updated': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'tag': 'tag',
        'label': 'label',
        'size': 'size',
        'visibility': 'visibility',
        'public_url': 'public_url',
        'storage_path': 'storage_path',
        'last_accessed': 'last_accessed',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, name=None, tag=None, label=None, size=None, visibility=None, public_url=None, storage_path=None, last_accessed=None, created=None, updated=None, local_vars_configuration=None):  # noqa: E501
        """FileSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._tag = None
        self._label = None
        self._size = None
        self._visibility = None
        self._public_url = None
        self._storage_path = None
        self._last_accessed = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if tag is not None:
            self.tag = tag
        if label is not None:
            self.label = label
        if size is not None:
            self.size = size
        if visibility is not None:
            self.visibility = visibility
        if public_url is not None:
            self.public_url = public_url
        if storage_path is not None:
            self.storage_path = storage_path
        if last_accessed is not None:
            self.last_accessed = last_accessed
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        """Gets the id of this FileSummary.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The id of this FileSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileSummary.

        Unique identifier  # noqa: E501

        :param id: The id of this FileSummary.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FileSummary.  # noqa: E501

        Name of file  # noqa: E501

        :return: The name of this FileSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileSummary.

        Name of file  # noqa: E501

        :param name: The name of this FileSummary.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def tag(self):
        """Gets the tag of this FileSummary.  # noqa: E501

        A file tag  # noqa: E501

        :return: The tag of this FileSummary.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this FileSummary.

        A file tag  # noqa: E501

        :param tag: The tag of this FileSummary.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def label(self):
        """Gets the label of this FileSummary.  # noqa: E501

        A file label  # noqa: E501

        :return: The label of this FileSummary.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this FileSummary.

        A file label  # noqa: E501

        :param label: The label of this FileSummary.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def size(self):
        """Gets the size of this FileSummary.  # noqa: E501

        Size in bytes of the file  # noqa: E501

        :return: The size of this FileSummary.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileSummary.

        Size in bytes of the file  # noqa: E501

        :param size: The size of this FileSummary.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def visibility(self):
        """Gets the visibility of this FileSummary.  # noqa: E501


        :return: The visibility of this FileSummary.  # noqa: E501
        :rtype: FileVisibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this FileSummary.


        :param visibility: The visibility of this FileSummary.  # noqa: E501
        :type: FileVisibility
        """

        self._visibility = visibility

    @property
    def public_url(self):
        """Gets the public_url of this FileSummary.  # noqa: E501

        The location of the file on the internet. If present, this file can be downloaded by requesting this URI. If the file is publically visible, then no credentials need be provided.   # noqa: E501

        :return: The public_url of this FileSummary.  # noqa: E501
        :rtype: str
        """
        return self._public_url

    @public_url.setter
    def public_url(self, public_url):
        """Sets the public_url of this FileSummary.

        The location of the file on the internet. If present, this file can be downloaded by requesting this URI. If the file is publically visible, then no credentials need be provided.   # noqa: E501

        :param public_url: The public_url of this FileSummary.  # noqa: E501
        :type: str
        """

        self._public_url = public_url

    @property
    def storage_path(self):
        """Gets the storage_path of this FileSummary.  # noqa: E501

        Where the file is stored in the backend storage.  # noqa: E501

        :return: The storage_path of this FileSummary.  # noqa: E501
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """Sets the storage_path of this FileSummary.

        Where the file is stored in the backend storage.  # noqa: E501

        :param storage_path: The storage_path of this FileSummary.  # noqa: E501
        :type: str
        """

        self._storage_path = storage_path

    @property
    def last_accessed(self):
        """Gets the last_accessed of this FileSummary.  # noqa: E501

        Time object was last accessed  # noqa: E501

        :return: The last_accessed of this FileSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._last_accessed

    @last_accessed.setter
    def last_accessed(self, last_accessed):
        """Sets the last_accessed of this FileSummary.

        Time object was last accessed  # noqa: E501

        :param last_accessed: The last_accessed of this FileSummary.  # noqa: E501
        :type: datetime
        """

        self._last_accessed = last_accessed

    @property
    def created(self):
        """Gets the created of this FileSummary.  # noqa: E501

        Creation time  # noqa: E501

        :return: The created of this FileSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this FileSummary.

        Creation time  # noqa: E501

        :param created: The created of this FileSummary.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this FileSummary.  # noqa: E501

        Update time  # noqa: E501

        :return: The updated of this FileSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this FileSummary.

        Update time  # noqa: E501

        :param updated: The updated of this FileSummary.  # noqa: E501
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
        if not isinstance(other, FileSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileSummary):
            return True

        return self.to_dict() != other.to_dict()
