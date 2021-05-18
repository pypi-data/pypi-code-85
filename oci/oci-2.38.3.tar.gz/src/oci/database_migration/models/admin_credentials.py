# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AdminCredentials(object):
    """
    Database Administrator Credentials details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AdminCredentials object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param username:
            The value to assign to the username property of this AdminCredentials.
        :type username: str

        """
        self.swagger_types = {
            'username': 'str'
        }

        self.attribute_map = {
            'username': 'username'
        }

        self._username = None

    @property
    def username(self):
        """
        **[Required]** Gets the username of this AdminCredentials.
        Administrator username


        :return: The username of this AdminCredentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this AdminCredentials.
        Administrator username


        :param username: The username of this AdminCredentials.
        :type: str
        """
        self._username = username

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
