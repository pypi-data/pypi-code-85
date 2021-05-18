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


class ConnectorStats(object):
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
        'metadata': 'ConnectorStatsMetadata',
        'overall_status': 'str',
        'forwarder_stats': 'ServiceForwarderStatsGroup',
        'app_service_stats': 'ApplicationServiceStatsGroup',
        'share_service_stats': 'FileShareServiceStatsGroup',
        'diagnostic_stats': 'ConnectorDiagnosticStats'
    }

    attribute_map = {
        'metadata': 'metadata',
        'overall_status': 'overall_status',
        'forwarder_stats': 'forwarder_stats',
        'app_service_stats': 'app_service_stats',
        'share_service_stats': 'share_service_stats',
        'diagnostic_stats': 'diagnostic_stats'
    }

    def __init__(self, metadata=None, overall_status=None, forwarder_stats=None, app_service_stats=None, share_service_stats=None, diagnostic_stats=None, local_vars_configuration=None):  # noqa: E501
        """ConnectorStats - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metadata = None
        self._overall_status = None
        self._forwarder_stats = None
        self._app_service_stats = None
        self._share_service_stats = None
        self._diagnostic_stats = None
        self.discriminator = None

        self.metadata = metadata
        self.overall_status = overall_status
        if forwarder_stats is not None:
            self.forwarder_stats = forwarder_stats
        if app_service_stats is not None:
            self.app_service_stats = app_service_stats
        if share_service_stats is not None:
            self.share_service_stats = share_service_stats
        if diagnostic_stats is not None:
            self.diagnostic_stats = diagnostic_stats

    @property
    def metadata(self):
        """Gets the metadata of this ConnectorStats.  # noqa: E501


        :return: The metadata of this ConnectorStats.  # noqa: E501
        :rtype: ConnectorStatsMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ConnectorStats.


        :param metadata: The metadata of this ConnectorStats.  # noqa: E501
        :type: ConnectorStatsMetadata
        """
        if self.local_vars_configuration.client_side_validation and metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def overall_status(self):
        """Gets the overall_status of this ConnectorStats.  # noqa: E501

        The summary status of the Connector. - A `good` status means that no action is neccessary on this Connector - A `warn` status means that there is an issue that should be dealt with   Examples include connections restarting frequently. - A `down` status indicates that there is a service accessibility problem   that should be dealt with as soon as possible. This could mean that there is a   problem with the Connector's configuration, or the platform. - A `stale` status indicates that although there may not be anything wrong,   we haven't been able to update the status recently. This may indicate   a communications issue between Agilicus and the Connector.   # noqa: E501

        :return: The overall_status of this ConnectorStats.  # noqa: E501
        :rtype: str
        """
        return self._overall_status

    @overall_status.setter
    def overall_status(self, overall_status):
        """Sets the overall_status of this ConnectorStats.

        The summary status of the Connector. - A `good` status means that no action is neccessary on this Connector - A `warn` status means that there is an issue that should be dealt with   Examples include connections restarting frequently. - A `down` status indicates that there is a service accessibility problem   that should be dealt with as soon as possible. This could mean that there is a   problem with the Connector's configuration, or the platform. - A `stale` status indicates that although there may not be anything wrong,   we haven't been able to update the status recently. This may indicate   a communications issue between Agilicus and the Connector.   # noqa: E501

        :param overall_status: The overall_status of this ConnectorStats.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and overall_status is None:  # noqa: E501
            raise ValueError("Invalid value for `overall_status`, must not be `None`")  # noqa: E501
        allowed_values = ["good", "warn", "down", "stale"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and overall_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `overall_status` ({0}), must be one of {1}"  # noqa: E501
                .format(overall_status, allowed_values)
            )

        self._overall_status = overall_status

    @property
    def forwarder_stats(self):
        """Gets the forwarder_stats of this ConnectorStats.  # noqa: E501


        :return: The forwarder_stats of this ConnectorStats.  # noqa: E501
        :rtype: ServiceForwarderStatsGroup
        """
        return self._forwarder_stats

    @forwarder_stats.setter
    def forwarder_stats(self, forwarder_stats):
        """Sets the forwarder_stats of this ConnectorStats.


        :param forwarder_stats: The forwarder_stats of this ConnectorStats.  # noqa: E501
        :type: ServiceForwarderStatsGroup
        """

        self._forwarder_stats = forwarder_stats

    @property
    def app_service_stats(self):
        """Gets the app_service_stats of this ConnectorStats.  # noqa: E501


        :return: The app_service_stats of this ConnectorStats.  # noqa: E501
        :rtype: ApplicationServiceStatsGroup
        """
        return self._app_service_stats

    @app_service_stats.setter
    def app_service_stats(self, app_service_stats):
        """Sets the app_service_stats of this ConnectorStats.


        :param app_service_stats: The app_service_stats of this ConnectorStats.  # noqa: E501
        :type: ApplicationServiceStatsGroup
        """

        self._app_service_stats = app_service_stats

    @property
    def share_service_stats(self):
        """Gets the share_service_stats of this ConnectorStats.  # noqa: E501


        :return: The share_service_stats of this ConnectorStats.  # noqa: E501
        :rtype: FileShareServiceStatsGroup
        """
        return self._share_service_stats

    @share_service_stats.setter
    def share_service_stats(self, share_service_stats):
        """Sets the share_service_stats of this ConnectorStats.


        :param share_service_stats: The share_service_stats of this ConnectorStats.  # noqa: E501
        :type: FileShareServiceStatsGroup
        """

        self._share_service_stats = share_service_stats

    @property
    def diagnostic_stats(self):
        """Gets the diagnostic_stats of this ConnectorStats.  # noqa: E501


        :return: The diagnostic_stats of this ConnectorStats.  # noqa: E501
        :rtype: ConnectorDiagnosticStats
        """
        return self._diagnostic_stats

    @diagnostic_stats.setter
    def diagnostic_stats(self, diagnostic_stats):
        """Sets the diagnostic_stats of this ConnectorStats.


        :param diagnostic_stats: The diagnostic_stats of this ConnectorStats.  # noqa: E501
        :type: ConnectorDiagnosticStats
        """

        self._diagnostic_stats = diagnostic_stats

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
        if not isinstance(other, ConnectorStats):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConnectorStats):
            return True

        return self.to_dict() != other.to_dict()
