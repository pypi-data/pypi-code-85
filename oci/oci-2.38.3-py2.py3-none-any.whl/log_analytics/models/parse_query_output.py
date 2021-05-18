# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParseQueryOutput(object):
    """
    Returns a parser agnostic breakdown of a query string for client query string introspection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParseQueryOutput object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_query_string:
            The value to assign to the display_query_string property of this ParseQueryOutput.
        :type display_query_string: str

        :param internal_query_string:
            The value to assign to the internal_query_string property of this ParseQueryOutput.
        :type internal_query_string: str

        :param columns:
            The value to assign to the columns property of this ParseQueryOutput.
        :type columns: list[oci.log_analytics.models.AbstractColumn]

        :param response_time_in_ms:
            The value to assign to the response_time_in_ms property of this ParseQueryOutput.
        :type response_time_in_ms: int

        :param commands:
            The value to assign to the commands property of this ParseQueryOutput.
        :type commands: list[oci.log_analytics.models.AbstractCommandDescriptor]

        """
        self.swagger_types = {
            'display_query_string': 'str',
            'internal_query_string': 'str',
            'columns': 'list[AbstractColumn]',
            'response_time_in_ms': 'int',
            'commands': 'list[AbstractCommandDescriptor]'
        }

        self.attribute_map = {
            'display_query_string': 'displayQueryString',
            'internal_query_string': 'internalQueryString',
            'columns': 'columns',
            'response_time_in_ms': 'responseTimeInMs',
            'commands': 'commands'
        }

        self._display_query_string = None
        self._internal_query_string = None
        self._columns = None
        self._response_time_in_ms = None
        self._commands = None

    @property
    def display_query_string(self):
        """
        **[Required]** Gets the display_query_string of this ParseQueryOutput.
        Display string formatted by query builder of user specified query string.


        :return: The display_query_string of this ParseQueryOutput.
        :rtype: str
        """
        return self._display_query_string

    @display_query_string.setter
    def display_query_string(self, display_query_string):
        """
        Sets the display_query_string of this ParseQueryOutput.
        Display string formatted by query builder of user specified query string.


        :param display_query_string: The display_query_string of this ParseQueryOutput.
        :type: str
        """
        self._display_query_string = display_query_string

    @property
    def internal_query_string(self):
        """
        **[Required]** Gets the internal_query_string of this ParseQueryOutput.
        Internal string formatted by query builder of user specified query string.


        :return: The internal_query_string of this ParseQueryOutput.
        :rtype: str
        """
        return self._internal_query_string

    @internal_query_string.setter
    def internal_query_string(self, internal_query_string):
        """
        Sets the internal_query_string of this ParseQueryOutput.
        Internal string formatted by query builder of user specified query string.


        :param internal_query_string: The internal_query_string of this ParseQueryOutput.
        :type: str
        """
        self._internal_query_string = internal_query_string

    @property
    def columns(self):
        """
        Gets the columns of this ParseQueryOutput.
        List of columns returned by the specified query string as result output.


        :return: The columns of this ParseQueryOutput.
        :rtype: list[oci.log_analytics.models.AbstractColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this ParseQueryOutput.
        List of columns returned by the specified query string as result output.


        :param columns: The columns of this ParseQueryOutput.
        :type: list[oci.log_analytics.models.AbstractColumn]
        """
        self._columns = columns

    @property
    def response_time_in_ms(self):
        """
        Gets the response_time_in_ms of this ParseQueryOutput.
        Operation response time.


        :return: The response_time_in_ms of this ParseQueryOutput.
        :rtype: int
        """
        return self._response_time_in_ms

    @response_time_in_ms.setter
    def response_time_in_ms(self, response_time_in_ms):
        """
        Sets the response_time_in_ms of this ParseQueryOutput.
        Operation response time.


        :param response_time_in_ms: The response_time_in_ms of this ParseQueryOutput.
        :type: int
        """
        self._response_time_in_ms = response_time_in_ms

    @property
    def commands(self):
        """
        Gets the commands of this ParseQueryOutput.
        List of querylanguage command descriptors, describing the specfied query string.


        :return: The commands of this ParseQueryOutput.
        :rtype: list[oci.log_analytics.models.AbstractCommandDescriptor]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        """
        Sets the commands of this ParseQueryOutput.
        List of querylanguage command descriptors, describing the specfied query string.


        :param commands: The commands of this ParseQueryOutput.
        :type: list[oci.log_analytics.models.AbstractCommandDescriptor]
        """
        self._commands = commands

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
