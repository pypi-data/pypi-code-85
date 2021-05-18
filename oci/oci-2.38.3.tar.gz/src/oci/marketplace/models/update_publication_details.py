# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePublicationDetails(object):
    """
    The updated details of the resource
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePublicationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdatePublicationDetails.
        :type name: str

        :param short_description:
            The value to assign to the short_description property of this UpdatePublicationDetails.
        :type short_description: str

        :param long_description:
            The value to assign to the long_description property of this UpdatePublicationDetails.
        :type long_description: str

        :param support_contacts:
            The value to assign to the support_contacts property of this UpdatePublicationDetails.
        :type support_contacts: list[oci.marketplace.models.SupportContact]

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdatePublicationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdatePublicationDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'name': 'str',
            'short_description': 'str',
            'long_description': 'str',
            'support_contacts': 'list[SupportContact]',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'name': 'name',
            'short_description': 'shortDescription',
            'long_description': 'longDescription',
            'support_contacts': 'supportContacts',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._name = None
        self._short_description = None
        self._long_description = None
        self._support_contacts = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def name(self):
        """
        Gets the name of this UpdatePublicationDetails.
        The name of the listing.


        :return: The name of this UpdatePublicationDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdatePublicationDetails.
        The name of the listing.


        :param name: The name of this UpdatePublicationDetails.
        :type: str
        """
        self._name = name

    @property
    def short_description(self):
        """
        Gets the short_description of this UpdatePublicationDetails.
        short description of the catalog listing


        :return: The short_description of this UpdatePublicationDetails.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """
        Sets the short_description of this UpdatePublicationDetails.
        short description of the catalog listing


        :param short_description: The short_description of this UpdatePublicationDetails.
        :type: str
        """
        self._short_description = short_description

    @property
    def long_description(self):
        """
        Gets the long_description of this UpdatePublicationDetails.
        short description of the catalog listing


        :return: The long_description of this UpdatePublicationDetails.
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """
        Sets the long_description of this UpdatePublicationDetails.
        short description of the catalog listing


        :param long_description: The long_description of this UpdatePublicationDetails.
        :type: str
        """
        self._long_description = long_description

    @property
    def support_contacts(self):
        """
        Gets the support_contacts of this UpdatePublicationDetails.
        Contact information to use to get support from the publisher for the listing.


        :return: The support_contacts of this UpdatePublicationDetails.
        :rtype: list[oci.marketplace.models.SupportContact]
        """
        return self._support_contacts

    @support_contacts.setter
    def support_contacts(self, support_contacts):
        """
        Sets the support_contacts of this UpdatePublicationDetails.
        Contact information to use to get support from the publisher for the listing.


        :param support_contacts: The support_contacts of this UpdatePublicationDetails.
        :type: list[oci.marketplace.models.SupportContact]
        """
        self._support_contacts = support_contacts

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdatePublicationDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdatePublicationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdatePublicationDetails.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdatePublicationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdatePublicationDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdatePublicationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdatePublicationDetails.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdatePublicationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
