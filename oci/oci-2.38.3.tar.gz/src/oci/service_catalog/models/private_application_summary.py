# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateApplicationSummary(object):
    """
    Brief data about an application or a solution, which lives inside the tenancy and may be included into service catalogs.
    """

    #: A constant which can be used with the package_type property of a PrivateApplicationSummary.
    #: This constant has a value of "STACK"
    PACKAGE_TYPE_STACK = "STACK"

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateApplicationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PrivateApplicationSummary.
        :type lifecycle_state: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PrivateApplicationSummary.
        :type compartment_id: str

        :param id:
            The value to assign to the id property of this PrivateApplicationSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this PrivateApplicationSummary.
        :type display_name: str

        :param short_description:
            The value to assign to the short_description property of this PrivateApplicationSummary.
        :type short_description: str

        :param logo:
            The value to assign to the logo property of this PrivateApplicationSummary.
        :type logo: oci.service_catalog.models.UploadData

        :param package_type:
            The value to assign to the package_type property of this PrivateApplicationSummary.
            Allowed values for this property are: "STACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type package_type: str

        :param time_created:
            The value to assign to the time_created property of this PrivateApplicationSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'lifecycle_state': 'str',
            'compartment_id': 'str',
            'id': 'str',
            'display_name': 'str',
            'short_description': 'str',
            'logo': 'UploadData',
            'package_type': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState',
            'compartment_id': 'compartmentId',
            'id': 'id',
            'display_name': 'displayName',
            'short_description': 'shortDescription',
            'logo': 'logo',
            'package_type': 'packageType',
            'time_created': 'timeCreated'
        }

        self._lifecycle_state = None
        self._compartment_id = None
        self._id = None
        self._display_name = None
        self._short_description = None
        self._logo = None
        self._package_type = None
        self._time_created = None

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PrivateApplicationSummary.
        The lifecycle state of the private application.


        :return: The lifecycle_state of this PrivateApplicationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PrivateApplicationSummary.
        The lifecycle state of the private application.


        :param lifecycle_state: The lifecycle_state of this PrivateApplicationSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PrivateApplicationSummary.
        The `OCID`__ of the compartment where the private application resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this PrivateApplicationSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PrivateApplicationSummary.
        The `OCID`__ of the compartment where the private application resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this PrivateApplicationSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PrivateApplicationSummary.
        The `OCID`__ of the private application.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this PrivateApplicationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrivateApplicationSummary.
        The `OCID`__ of the private application.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this PrivateApplicationSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PrivateApplicationSummary.
        The name of the private application.


        :return: The display_name of this PrivateApplicationSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PrivateApplicationSummary.
        The name of the private application.


        :param display_name: The display_name of this PrivateApplicationSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def short_description(self):
        """
        Gets the short_description of this PrivateApplicationSummary.
        A short description of the private application.


        :return: The short_description of this PrivateApplicationSummary.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this PrivateApplicationSummary.
        A short description of the private application.


        :param short_description: The short_description of this PrivateApplicationSummary.
        :type: str
        """
        self._short_description = short_description

    @property
    def logo(self):
        """
        Gets the logo of this PrivateApplicationSummary.

        :return: The logo of this PrivateApplicationSummary.
        :rtype: oci.service_catalog.models.UploadData
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """
        Sets the logo of this PrivateApplicationSummary.

        :param logo: The logo of this PrivateApplicationSummary.
        :type: oci.service_catalog.models.UploadData
        """
        self._logo = logo

    @property
    def package_type(self):
        """
        **[Required]** Gets the package_type of this PrivateApplicationSummary.
        Type of the packages, which are hosted by the private application.

        Allowed values for this property are: "STACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The package_type of this PrivateApplicationSummary.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this PrivateApplicationSummary.
        Type of the packages, which are hosted by the private application.


        :param package_type: The package_type of this PrivateApplicationSummary.
        :type: str
        """
        allowed_values = ["STACK"]
        if not value_allowed_none_or_none_sentinel(package_type, allowed_values):
            package_type = 'UNKNOWN_ENUM_VALUE'
        self._package_type = package_type

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PrivateApplicationSummary.
        The date and time the private application was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-05-27T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this PrivateApplicationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PrivateApplicationSummary.
        The date and time the private application was created, expressed in `RFC 3339`__
        timestamp format.

        Example: `2021-05-27T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this PrivateApplicationSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
