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


class AgentConnectorConnectionInfo(object):
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
        'connection_uri': 'str',
        'connection_location': 'str',
        'connection_path': 'str',
        'connection_org_id': 'str',
        'connection_app_name': 'str',
        'is_an_auth_service': 'bool',
        'end_to_end_tls': 'bool',
        'max_number_connections': 'int',
        'ip_services': 'list[ApplicationService]',
        'file_share_services': 'list[FileShareService]',
        'application_config': 'ApplicationConfig'
    }

    attribute_map = {
        'connection_uri': 'connection_uri',
        'connection_location': 'connection_location',
        'connection_path': 'connection_path',
        'connection_org_id': 'connection_org_id',
        'connection_app_name': 'connection_app_name',
        'is_an_auth_service': 'is_an_auth_service',
        'end_to_end_tls': 'end_to_end_tls',
        'max_number_connections': 'max_number_connections',
        'ip_services': 'ip_services',
        'file_share_services': 'file_share_services',
        'application_config': 'application_config'
    }

    def __init__(self, connection_uri=None, connection_location=None, connection_path=None, connection_org_id=None, connection_app_name=None, is_an_auth_service=False, end_to_end_tls=None, max_number_connections=16, ip_services=None, file_share_services=None, application_config=None, local_vars_configuration=None):  # noqa: E501
        """AgentConnectorConnectionInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connection_uri = None
        self._connection_location = None
        self._connection_path = None
        self._connection_org_id = None
        self._connection_app_name = None
        self._is_an_auth_service = None
        self._end_to_end_tls = None
        self._max_number_connections = None
        self._ip_services = None
        self._file_share_services = None
        self._application_config = None
        self.discriminator = None

        if connection_uri is not None:
            self.connection_uri = connection_uri
        if connection_location is not None:
            self.connection_location = connection_location
        if connection_path is not None:
            self.connection_path = connection_path
        if connection_org_id is not None:
            self.connection_org_id = connection_org_id
        if connection_app_name is not None:
            self.connection_app_name = connection_app_name
        if is_an_auth_service is not None:
            self.is_an_auth_service = is_an_auth_service
        if end_to_end_tls is not None:
            self.end_to_end_tls = end_to_end_tls
        if max_number_connections is not None:
            self.max_number_connections = max_number_connections
        if ip_services is not None:
            self.ip_services = ip_services
        if file_share_services is not None:
            self.file_share_services = file_share_services
        if application_config is not None:
            self.application_config = application_config

    @property
    def connection_uri(self):
        """Gets the connection_uri of this AgentConnectorConnectionInfo.  # noqa: E501

        The URI used to establish a connection to the connector.  # noqa: E501

        :return: The connection_uri of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._connection_uri

    @connection_uri.setter
    def connection_uri(self, connection_uri):
        """Sets the connection_uri of this AgentConnectorConnectionInfo.

        The URI used to establish a connection to the connector.  # noqa: E501

        :param connection_uri: The connection_uri of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: str
        """

        self._connection_uri = connection_uri

    @property
    def connection_location(self):
        """Gets the connection_location of this AgentConnectorConnectionInfo.  # noqa: E501

        The location (e.g. fully qualified domain name) of the connection. While this matches the location in the `connection_uri`, it is provided separately for convenience.   # noqa: E501

        :return: The connection_location of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._connection_location

    @connection_location.setter
    def connection_location(self, connection_location):
        """Sets the connection_location of this AgentConnectorConnectionInfo.

        The location (e.g. fully qualified domain name) of the connection. While this matches the location in the `connection_uri`, it is provided separately for convenience.   # noqa: E501

        :param connection_location: The connection_location of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: str
        """

        self._connection_location = connection_location

    @property
    def connection_path(self):
        """Gets the connection_path of this AgentConnectorConnectionInfo.  # noqa: E501

        The path of the connection. While this matches the path in the `connection_uri`, it is provided separately for convenience.   # noqa: E501

        :return: The connection_path of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._connection_path

    @connection_path.setter
    def connection_path(self, connection_path):
        """Sets the connection_path of this AgentConnectorConnectionInfo.

        The path of the connection. While this matches the path in the `connection_uri`, it is provided separately for convenience.   # noqa: E501

        :param connection_path: The connection_path of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: str
        """

        self._connection_path = connection_path

    @property
    def connection_org_id(self):
        """Gets the connection_org_id of this AgentConnectorConnectionInfo.  # noqa: E501

        The identifier for the organisation hosting the server side of this connection.   # noqa: E501

        :return: The connection_org_id of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._connection_org_id

    @connection_org_id.setter
    def connection_org_id(self, connection_org_id):
        """Sets the connection_org_id of this AgentConnectorConnectionInfo.

        The identifier for the organisation hosting the server side of this connection.   # noqa: E501

        :param connection_org_id: The connection_org_id of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                connection_org_id is not None and len(connection_org_id) > 40):
            raise ValueError("Invalid value for `connection_org_id`, length must be less than or equal to `40`")  # noqa: E501

        self._connection_org_id = connection_org_id

    @property
    def connection_app_name(self):
        """Gets the connection_app_name of this AgentConnectorConnectionInfo.  # noqa: E501

        The name of the Application (if any) hosting the server side of this connection. Note that not all servers will be hosted by an Application, in which case this will be empty.   # noqa: E501

        :return: The connection_app_name of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._connection_app_name

    @connection_app_name.setter
    def connection_app_name(self, connection_app_name):
        """Sets the connection_app_name of this AgentConnectorConnectionInfo.

        The name of the Application (if any) hosting the server side of this connection. Note that not all servers will be hosted by an Application, in which case this will be empty.   # noqa: E501

        :param connection_app_name: The connection_app_name of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                connection_app_name is not None and len(connection_app_name) > 63):
            raise ValueError("Invalid value for `connection_app_name`, length must be less than or equal to `63`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connection_app_name is not None and len(connection_app_name) < 1):
            raise ValueError("Invalid value for `connection_app_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connection_app_name is not None and not re.search(r'^[a-zA-Z0-9-:]+$', connection_app_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `connection_app_name`, must be a follow pattern or equal to `/^[a-zA-Z0-9-:]+$/`")  # noqa: E501

        self._connection_app_name = connection_app_name

    @property
    def is_an_auth_service(self):
        """Gets the is_an_auth_service of this AgentConnectorConnectionInfo.  # noqa: E501

        Indicates that the connection is exposing an authentication service   # noqa: E501

        :return: The is_an_auth_service of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_an_auth_service

    @is_an_auth_service.setter
    def is_an_auth_service(self, is_an_auth_service):
        """Sets the is_an_auth_service of this AgentConnectorConnectionInfo.

        Indicates that the connection is exposing an authentication service   # noqa: E501

        :param is_an_auth_service: The is_an_auth_service of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: bool
        """

        self._is_an_auth_service = is_an_auth_service

    @property
    def end_to_end_tls(self):
        """Gets the end_to_end_tls of this AgentConnectorConnectionInfo.  # noqa: E501

        Controls if the connection is end to end TLS.   # noqa: E501

        :return: The end_to_end_tls of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._end_to_end_tls

    @end_to_end_tls.setter
    def end_to_end_tls(self, end_to_end_tls):
        """Sets the end_to_end_tls of this AgentConnectorConnectionInfo.

        Controls if the connection is end to end TLS.   # noqa: E501

        :param end_to_end_tls: The end_to_end_tls of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: bool
        """

        self._end_to_end_tls = end_to_end_tls

    @property
    def max_number_connections(self):
        """Gets the max_number_connections of this AgentConnectorConnectionInfo.  # noqa: E501

        The maximum number of connections to maintain to the cluster when stable. Note that this value may be exceeded during times of reconfiguration. A value of zero means that the connection is effectively unused by this Secure Agent.   # noqa: E501

        :return: The max_number_connections of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_number_connections

    @max_number_connections.setter
    def max_number_connections(self, max_number_connections):
        """Sets the max_number_connections of this AgentConnectorConnectionInfo.

        The maximum number of connections to maintain to the cluster when stable. Note that this value may be exceeded during times of reconfiguration. A value of zero means that the connection is effectively unused by this Secure Agent.   # noqa: E501

        :param max_number_connections: The max_number_connections of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_number_connections is not None and max_number_connections > 64):  # noqa: E501
            raise ValueError("Invalid value for `max_number_connections`, must be a value less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_number_connections is not None and max_number_connections < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_number_connections`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_number_connections = max_number_connections

    @property
    def ip_services(self):
        """Gets the ip_services of this AgentConnectorConnectionInfo.  # noqa: E501

        The list of ip services associated with this connection  # noqa: E501

        :return: The ip_services of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: list[ApplicationService]
        """
        return self._ip_services

    @ip_services.setter
    def ip_services(self, ip_services):
        """Sets the ip_services of this AgentConnectorConnectionInfo.

        The list of ip services associated with this connection  # noqa: E501

        :param ip_services: The ip_services of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: list[ApplicationService]
        """

        self._ip_services = ip_services

    @property
    def file_share_services(self):
        """Gets the file_share_services of this AgentConnectorConnectionInfo.  # noqa: E501

        The list of fileshare services associated with this connection  # noqa: E501

        :return: The file_share_services of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: list[FileShareService]
        """
        return self._file_share_services

    @file_share_services.setter
    def file_share_services(self, file_share_services):
        """Sets the file_share_services of this AgentConnectorConnectionInfo.

        The list of fileshare services associated with this connection  # noqa: E501

        :param file_share_services: The file_share_services of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: list[FileShareService]
        """

        self._file_share_services = file_share_services

    @property
    def application_config(self):
        """Gets the application_config of this AgentConnectorConnectionInfo.  # noqa: E501


        :return: The application_config of this AgentConnectorConnectionInfo.  # noqa: E501
        :rtype: ApplicationConfig
        """
        return self._application_config

    @application_config.setter
    def application_config(self, application_config):
        """Sets the application_config of this AgentConnectorConnectionInfo.


        :param application_config: The application_config of this AgentConnectorConnectionInfo.  # noqa: E501
        :type: ApplicationConfig
        """

        self._application_config = application_config

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
        if not isinstance(other, AgentConnectorConnectionInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentConnectorConnectionInfo):
            return True

        return self.to_dict() != other.to_dict()
