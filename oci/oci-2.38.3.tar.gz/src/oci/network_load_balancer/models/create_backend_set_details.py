# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBackendSetDetails(object):
    """
    The configuration details for creating a backend set in a network load balancer.
    For more information about backend set configuration, see
    `Managing Backend Sets`__.

    **Caution:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Balance/Tasks/managingbackendsets.htm
    """

    #: A constant which can be used with the policy property of a CreateBackendSetDetails.
    #: This constant has a value of "TWO_TUPLE"
    POLICY_TWO_TUPLE = "TWO_TUPLE"

    #: A constant which can be used with the policy property of a CreateBackendSetDetails.
    #: This constant has a value of "THREE_TUPLE"
    POLICY_THREE_TUPLE = "THREE_TUPLE"

    #: A constant which can be used with the policy property of a CreateBackendSetDetails.
    #: This constant has a value of "FIVE_TUPLE"
    POLICY_FIVE_TUPLE = "FIVE_TUPLE"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBackendSetDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateBackendSetDetails.
        :type name: str

        :param policy:
            The value to assign to the policy property of this CreateBackendSetDetails.
            Allowed values for this property are: "TWO_TUPLE", "THREE_TUPLE", "FIVE_TUPLE"
        :type policy: str

        :param is_preserve_source:
            The value to assign to the is_preserve_source property of this CreateBackendSetDetails.
        :type is_preserve_source: bool

        :param backends:
            The value to assign to the backends property of this CreateBackendSetDetails.
        :type backends: list[oci.network_load_balancer.models.BackendDetails]

        :param health_checker:
            The value to assign to the health_checker property of this CreateBackendSetDetails.
        :type health_checker: oci.network_load_balancer.models.HealthCheckerDetails

        """
        self.swagger_types = {
            'name': 'str',
            'policy': 'str',
            'is_preserve_source': 'bool',
            'backends': 'list[BackendDetails]',
            'health_checker': 'HealthCheckerDetails'
        }

        self.attribute_map = {
            'name': 'name',
            'policy': 'policy',
            'is_preserve_source': 'isPreserveSource',
            'backends': 'backends',
            'health_checker': 'healthChecker'
        }

        self._name = None
        self._policy = None
        self._is_preserve_source = None
        self._backends = None
        self._health_checker = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateBackendSetDetails.
        A user-friendly name for the backend set that must be unique and cannot be changed.

        Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
        contain spaces. Avoid entering confidential information.

        Example: `example_backend_set`


        :return: The name of this CreateBackendSetDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateBackendSetDetails.
        A user-friendly name for the backend set that must be unique and cannot be changed.

        Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
        contain spaces. Avoid entering confidential information.

        Example: `example_backend_set`


        :param name: The name of this CreateBackendSetDetails.
        :type: str
        """
        self._name = name

    @property
    def policy(self):
        """
        **[Required]** Gets the policy of this CreateBackendSetDetails.
        The network load balancer policy for the backend set.

        Example: `FIVE_TUPLE``

        Allowed values for this property are: "TWO_TUPLE", "THREE_TUPLE", "FIVE_TUPLE"


        :return: The policy of this CreateBackendSetDetails.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this CreateBackendSetDetails.
        The network load balancer policy for the backend set.

        Example: `FIVE_TUPLE``


        :param policy: The policy of this CreateBackendSetDetails.
        :type: str
        """
        allowed_values = ["TWO_TUPLE", "THREE_TUPLE", "FIVE_TUPLE"]
        if not value_allowed_none_or_none_sentinel(policy, allowed_values):
            raise ValueError(
                "Invalid value for `policy`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._policy = policy

    @property
    def is_preserve_source(self):
        """
        Gets the is_preserve_source of this CreateBackendSetDetails.
        If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends.
        Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled.
        The value is true by default.


        :return: The is_preserve_source of this CreateBackendSetDetails.
        :rtype: bool
        """
        return self._is_preserve_source

    @is_preserve_source.setter
    def is_preserve_source(self, is_preserve_source):
        """
        Sets the is_preserve_source of this CreateBackendSetDetails.
        If this parameter is enabled, then the network load balancer preserves the source IP of the packet when it is forwarded to backends.
        Backends see the original source IP. If the isPreserveSourceDestination parameter is enabled for the network load balancer resource, then this parameter cannot be disabled.
        The value is true by default.


        :param is_preserve_source: The is_preserve_source of this CreateBackendSetDetails.
        :type: bool
        """
        self._is_preserve_source = is_preserve_source

    @property
    def backends(self):
        """
        Gets the backends of this CreateBackendSetDetails.
        An array of backends to be associated with the backend set.


        :return: The backends of this CreateBackendSetDetails.
        :rtype: list[oci.network_load_balancer.models.BackendDetails]
        """
        return self._backends

    @backends.setter
    def backends(self, backends):
        """
        Sets the backends of this CreateBackendSetDetails.
        An array of backends to be associated with the backend set.


        :param backends: The backends of this CreateBackendSetDetails.
        :type: list[oci.network_load_balancer.models.BackendDetails]
        """
        self._backends = backends

    @property
    def health_checker(self):
        """
        **[Required]** Gets the health_checker of this CreateBackendSetDetails.

        :return: The health_checker of this CreateBackendSetDetails.
        :rtype: oci.network_load_balancer.models.HealthCheckerDetails
        """
        return self._health_checker

    @health_checker.setter
    def health_checker(self, health_checker):
        """
        Sets the health_checker of this CreateBackendSetDetails.

        :param health_checker: The health_checker of this CreateBackendSetDetails.
        :type: oci.network_load_balancer.models.HealthCheckerDetails
        """
        self._health_checker = health_checker

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
