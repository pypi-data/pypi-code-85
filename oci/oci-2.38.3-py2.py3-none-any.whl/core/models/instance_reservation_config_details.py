# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceReservationConfigDetails(object):
    """
    A template that contains the settings to use when defining the instance reservation configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceReservationConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param instance_shape:
            The value to assign to the instance_shape property of this InstanceReservationConfigDetails.
        :type instance_shape: str

        :param instance_shape_config:
            The value to assign to the instance_shape_config property of this InstanceReservationConfigDetails.
        :type instance_shape_config: oci.core.models.InstanceReservationShapeConfigDetails

        :param fault_domain:
            The value to assign to the fault_domain property of this InstanceReservationConfigDetails.
        :type fault_domain: str

        :param reserved_count:
            The value to assign to the reserved_count property of this InstanceReservationConfigDetails.
        :type reserved_count: int

        """
        self.swagger_types = {
            'instance_shape': 'str',
            'instance_shape_config': 'InstanceReservationShapeConfigDetails',
            'fault_domain': 'str',
            'reserved_count': 'int'
        }

        self.attribute_map = {
            'instance_shape': 'instanceShape',
            'instance_shape_config': 'instanceShapeConfig',
            'fault_domain': 'faultDomain',
            'reserved_count': 'reservedCount'
        }

        self._instance_shape = None
        self._instance_shape_config = None
        self._fault_domain = None
        self._reserved_count = None

    @property
    def instance_shape(self):
        """
        **[Required]** Gets the instance_shape of this InstanceReservationConfigDetails.
        The shape requested when launching instances using reserved capacity.
        The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.
        You can list all available shapes by calling :class:`ListComputeCapacityReservationInstanceShapes`.


        :return: The instance_shape of this InstanceReservationConfigDetails.
        :rtype: str
        """
        return self._instance_shape

    @instance_shape.setter
    def instance_shape(self, instance_shape):
        """
        Sets the instance_shape of this InstanceReservationConfigDetails.
        The shape requested when launching instances using reserved capacity.
        The shape determines the number of CPUs, amount of memory,
        and other resources allocated to the instance.
        You can list all available shapes by calling :class:`ListComputeCapacityReservationInstanceShapes`.


        :param instance_shape: The instance_shape of this InstanceReservationConfigDetails.
        :type: str
        """
        self._instance_shape = instance_shape

    @property
    def instance_shape_config(self):
        """
        Gets the instance_shape_config of this InstanceReservationConfigDetails.

        :return: The instance_shape_config of this InstanceReservationConfigDetails.
        :rtype: oci.core.models.InstanceReservationShapeConfigDetails
        """
        return self._instance_shape_config

    @instance_shape_config.setter
    def instance_shape_config(self, instance_shape_config):
        """
        Sets the instance_shape_config of this InstanceReservationConfigDetails.

        :param instance_shape_config: The instance_shape_config of this InstanceReservationConfigDetails.
        :type: oci.core.models.InstanceReservationShapeConfigDetails
        """
        self._instance_shape_config = instance_shape_config

    @property
    def fault_domain(self):
        """
        Gets the fault_domain of this InstanceReservationConfigDetails.
        The fault domain to use for instances created using this reservation configuration.
        For more information, see `Fault Domains`__.
        If you do not specify the fault domain, the capacity is available for an instance
        that does not specify a fault domain. To change the fault domain for a reservation,
        delete the reservation and create a new one in the preferred fault domain.

        To retrieve a list of fault domains, use the `ListFaultDomains` operation in
        the `Identity and Access Management Service API`__.

        Example: `FAULT-DOMAIN-1`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault
        __ https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/


        :return: The fault_domain of this InstanceReservationConfigDetails.
        :rtype: str
        """
        return self._fault_domain

    @fault_domain.setter
    def fault_domain(self, fault_domain):
        """
        Sets the fault_domain of this InstanceReservationConfigDetails.
        The fault domain to use for instances created using this reservation configuration.
        For more information, see `Fault Domains`__.
        If you do not specify the fault domain, the capacity is available for an instance
        that does not specify a fault domain. To change the fault domain for a reservation,
        delete the reservation and create a new one in the preferred fault domain.

        To retrieve a list of fault domains, use the `ListFaultDomains` operation in
        the `Identity and Access Management Service API`__.

        Example: `FAULT-DOMAIN-1`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm#fault
        __ https://docs.cloud.oracle.com/iaas/api/#/en/identity/20160918/


        :param fault_domain: The fault_domain of this InstanceReservationConfigDetails.
        :type: str
        """
        self._fault_domain = fault_domain

    @property
    def reserved_count(self):
        """
        **[Required]** Gets the reserved_count of this InstanceReservationConfigDetails.
        The amount of capacity to reserve in this reservation configuration.


        :return: The reserved_count of this InstanceReservationConfigDetails.
        :rtype: int
        """
        return self._reserved_count

    @reserved_count.setter
    def reserved_count(self, reserved_count):
        """
        Sets the reserved_count of this InstanceReservationConfigDetails.
        The amount of capacity to reserve in this reservation configuration.


        :param reserved_count: The reserved_count of this InstanceReservationConfigDetails.
        :type: int
        """
        self._reserved_count = reserved_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
