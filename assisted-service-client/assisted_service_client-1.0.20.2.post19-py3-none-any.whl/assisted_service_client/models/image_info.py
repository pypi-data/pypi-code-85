# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ImageInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ssh_public_key': 'str',
        'size_bytes': 'int',
        'download_url': 'str',
        'generator_version': 'str',
        'created_at': 'datetime',
        'expires_at': 'datetime',
        'static_network_config': 'str',
        'type': 'ImageType'
    }

    attribute_map = {
        'ssh_public_key': 'ssh_public_key',
        'size_bytes': 'size_bytes',
        'download_url': 'download_url',
        'generator_version': 'generator_version',
        'created_at': 'created_at',
        'expires_at': 'expires_at',
        'static_network_config': 'static_network_config',
        'type': 'type'
    }

    def __init__(self, ssh_public_key=None, size_bytes=None, download_url=None, generator_version=None, created_at=None, expires_at=None, static_network_config=None, type=None):  # noqa: E501
        """ImageInfo - a model defined in Swagger"""  # noqa: E501

        self._ssh_public_key = None
        self._size_bytes = None
        self._download_url = None
        self._generator_version = None
        self._created_at = None
        self._expires_at = None
        self._static_network_config = None
        self._type = None
        self.discriminator = None

        if ssh_public_key is not None:
            self.ssh_public_key = ssh_public_key
        if size_bytes is not None:
            self.size_bytes = size_bytes
        if download_url is not None:
            self.download_url = download_url
        if generator_version is not None:
            self.generator_version = generator_version
        if created_at is not None:
            self.created_at = created_at
        if expires_at is not None:
            self.expires_at = expires_at
        if static_network_config is not None:
            self.static_network_config = static_network_config
        if type is not None:
            self.type = type

    @property
    def ssh_public_key(self):
        """Gets the ssh_public_key of this ImageInfo.  # noqa: E501

        SSH public key for debugging the installation.  # noqa: E501

        :return: The ssh_public_key of this ImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key):
        """Sets the ssh_public_key of this ImageInfo.

        SSH public key for debugging the installation.  # noqa: E501

        :param ssh_public_key: The ssh_public_key of this ImageInfo.  # noqa: E501
        :type: str
        """

        self._ssh_public_key = ssh_public_key

    @property
    def size_bytes(self):
        """Gets the size_bytes of this ImageInfo.  # noqa: E501


        :return: The size_bytes of this ImageInfo.  # noqa: E501
        :rtype: int
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this ImageInfo.


        :param size_bytes: The size_bytes of this ImageInfo.  # noqa: E501
        :type: int
        """
        if size_bytes is not None and size_bytes < 0:  # noqa: E501
            raise ValueError("Invalid value for `size_bytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size_bytes = size_bytes

    @property
    def download_url(self):
        """Gets the download_url of this ImageInfo.  # noqa: E501


        :return: The download_url of this ImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this ImageInfo.


        :param download_url: The download_url of this ImageInfo.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    @property
    def generator_version(self):
        """Gets the generator_version of this ImageInfo.  # noqa: E501

        Image generator version.  # noqa: E501

        :return: The generator_version of this ImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._generator_version

    @generator_version.setter
    def generator_version(self, generator_version):
        """Sets the generator_version of this ImageInfo.

        Image generator version.  # noqa: E501

        :param generator_version: The generator_version of this ImageInfo.  # noqa: E501
        :type: str
        """

        self._generator_version = generator_version

    @property
    def created_at(self):
        """Gets the created_at of this ImageInfo.  # noqa: E501


        :return: The created_at of this ImageInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ImageInfo.


        :param created_at: The created_at of this ImageInfo.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def expires_at(self):
        """Gets the expires_at of this ImageInfo.  # noqa: E501


        :return: The expires_at of this ImageInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this ImageInfo.


        :param expires_at: The expires_at of this ImageInfo.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def static_network_config(self):
        """Gets the static_network_config of this ImageInfo.  # noqa: E501

        static network configuration string in the format expected by discovery ignition generation  # noqa: E501

        :return: The static_network_config of this ImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._static_network_config

    @static_network_config.setter
    def static_network_config(self, static_network_config):
        """Sets the static_network_config of this ImageInfo.

        static network configuration string in the format expected by discovery ignition generation  # noqa: E501

        :param static_network_config: The static_network_config of this ImageInfo.  # noqa: E501
        :type: str
        """

        self._static_network_config = static_network_config

    @property
    def type(self):
        """Gets the type of this ImageInfo.  # noqa: E501


        :return: The type of this ImageInfo.  # noqa: E501
        :rtype: ImageType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImageInfo.


        :param type: The type of this ImageInfo.  # noqa: E501
        :type: ImageType
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ImageInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
