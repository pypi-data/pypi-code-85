# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BulkMoveResourcesDetails(object):
    """
    BulkMoveResourcesDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BulkMoveResourcesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resources:
            The value to assign to the resources property of this BulkMoveResourcesDetails.
        :type resources: list[oci.identity.models.BulkActionResource]

        :param target_compartment_id:
            The value to assign to the target_compartment_id property of this BulkMoveResourcesDetails.
        :type target_compartment_id: str

        """
        self.swagger_types = {
            'resources': 'list[BulkActionResource]',
            'target_compartment_id': 'str'
        }

        self.attribute_map = {
            'resources': 'resources',
            'target_compartment_id': 'targetCompartmentId'
        }

        self._resources = None
        self._target_compartment_id = None

    @property
    def resources(self):
        """
        **[Required]** Gets the resources of this BulkMoveResourcesDetails.
        The resources to be moved.


        :return: The resources of this BulkMoveResourcesDetails.
        :rtype: list[oci.identity.models.BulkActionResource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this BulkMoveResourcesDetails.
        The resources to be moved.


        :param resources: The resources of this BulkMoveResourcesDetails.
        :type: list[oci.identity.models.BulkActionResource]
        """
        self._resources = resources

    @property
    def target_compartment_id(self):
        """
        **[Required]** Gets the target_compartment_id of this BulkMoveResourcesDetails.
        The `OCID`__ of the destination compartment
        into which to move the resources.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The target_compartment_id of this BulkMoveResourcesDetails.
        :rtype: str
        """
        return self._target_compartment_id

    @target_compartment_id.setter
    def target_compartment_id(self, target_compartment_id):
        """
        Sets the target_compartment_id of this BulkMoveResourcesDetails.
        The `OCID`__ of the destination compartment
        into which to move the resources.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param target_compartment_id: The target_compartment_id of this BulkMoveResourcesDetails.
        :type: str
        """
        self._target_compartment_id = target_compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
