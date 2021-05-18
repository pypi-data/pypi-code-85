# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DNS(object):
    """
    The DNS resolution results.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DNS object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param domain_lookup_duration:
            The value to assign to the domain_lookup_duration property of this DNS.
        :type domain_lookup_duration: float

        :param addresses:
            The value to assign to the addresses property of this DNS.
        :type addresses: list[str]

        """
        self.swagger_types = {
            'domain_lookup_duration': 'float',
            'addresses': 'list[str]'
        }

        self.attribute_map = {
            'domain_lookup_duration': 'domainLookupDuration',
            'addresses': 'addresses'
        }

        self._domain_lookup_duration = None
        self._addresses = None

    @property
    def domain_lookup_duration(self):
        """
        Gets the domain_lookup_duration of this DNS.
        Total DNS resolution duration, in milliseconds. Calculated using `domainLookupEnd`
        minus `domainLookupStart`.


        :return: The domain_lookup_duration of this DNS.
        :rtype: float
        """
        return self._domain_lookup_duration

    @domain_lookup_duration.setter
    def domain_lookup_duration(self, domain_lookup_duration):
        """
        Sets the domain_lookup_duration of this DNS.
        Total DNS resolution duration, in milliseconds. Calculated using `domainLookupEnd`
        minus `domainLookupStart`.


        :param domain_lookup_duration: The domain_lookup_duration of this DNS.
        :type: float
        """
        self._domain_lookup_duration = domain_lookup_duration

    @property
    def addresses(self):
        """
        Gets the addresses of this DNS.
        The addresses returned by DNS resolution.


        :return: The addresses of this DNS.
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this DNS.
        The addresses returned by DNS resolution.


        :param addresses: The addresses of this DNS.
        :type: list[str]
        """
        self._addresses = addresses

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
