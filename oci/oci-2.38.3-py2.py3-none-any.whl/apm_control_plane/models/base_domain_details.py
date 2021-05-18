# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BaseDomainDetails(object):
    """
    Basic details for an APM Domain.
    """

    #: A constant which can be used with the lifecycle_state property of a BaseDomainDetails.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a BaseDomainDetails.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a BaseDomainDetails.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a BaseDomainDetails.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a BaseDomainDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new BaseDomainDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BaseDomainDetails.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this BaseDomainDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this BaseDomainDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this BaseDomainDetails.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BaseDomainDetails.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"
        :type lifecycle_state: str

        :param is_free_tier:
            The value to assign to the is_free_tier property of this BaseDomainDetails.
        :type is_free_tier: bool

        :param time_created:
            The value to assign to the time_created property of this BaseDomainDetails.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this BaseDomainDetails.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BaseDomainDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BaseDomainDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'is_free_tier': 'bool',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'is_free_tier': 'isFreeTier',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._is_free_tier = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BaseDomainDetails.
        Unique identifier that is immutable on creation.


        :return: The id of this BaseDomainDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BaseDomainDetails.
        Unique identifier that is immutable on creation.


        :param id: The id of this BaseDomainDetails.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this BaseDomainDetails.
        APM Domain display name, can be updated.


        :return: The display_name of this BaseDomainDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BaseDomainDetails.
        APM Domain display name, can be updated.


        :param display_name: The display_name of this BaseDomainDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this BaseDomainDetails.
        Description of the APM Domain.


        :return: The description of this BaseDomainDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BaseDomainDetails.
        Description of the APM Domain.


        :param description: The description of this BaseDomainDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this BaseDomainDetails.
        The OCID of the compartment corresponding to the APM Domain.


        :return: The compartment_id of this BaseDomainDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BaseDomainDetails.
        The OCID of the compartment corresponding to the APM Domain.


        :param compartment_id: The compartment_id of this BaseDomainDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this BaseDomainDetails.
        The current lifecycle state of the APM Domain.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"


        :return: The lifecycle_state of this BaseDomainDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BaseDomainDetails.
        The current lifecycle state of the APM Domain.


        :param lifecycle_state: The lifecycle_state of this BaseDomainDetails.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def is_free_tier(self):
        """
        Gets the is_free_tier of this BaseDomainDetails.
        Indicates if this is an Always Free resource.


        :return: The is_free_tier of this BaseDomainDetails.
        :rtype: bool
        """
        return self._is_free_tier

    @is_free_tier.setter
    def is_free_tier(self, is_free_tier):
        """
        Sets the is_free_tier of this BaseDomainDetails.
        Indicates if this is an Always Free resource.


        :param is_free_tier: The is_free_tier of this BaseDomainDetails.
        :type: bool
        """
        self._is_free_tier = is_free_tier

    @property
    def time_created(self):
        """
        Gets the time_created of this BaseDomainDetails.
        The time the the APM Domain was created. An RFC3339 formatted datetime string


        :return: The time_created of this BaseDomainDetails.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BaseDomainDetails.
        The time the the APM Domain was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this BaseDomainDetails.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this BaseDomainDetails.
        The time the APM Domain was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this BaseDomainDetails.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this BaseDomainDetails.
        The time the APM Domain was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this BaseDomainDetails.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BaseDomainDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this BaseDomainDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BaseDomainDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this BaseDomainDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BaseDomainDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this BaseDomainDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BaseDomainDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this BaseDomainDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
