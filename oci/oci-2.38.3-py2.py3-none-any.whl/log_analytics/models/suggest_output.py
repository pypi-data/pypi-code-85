# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SuggestOutput(object):
    """
    Typeahead results
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SuggestOutput object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param position:
            The value to assign to the position property of this SuggestOutput.
        :type position: int

        :param commands:
            The value to assign to the commands property of this SuggestOutput.
        :type commands: list[str]

        :param fields:
            The value to assign to the fields property of this SuggestOutput.
        :type fields: list[str]

        :param field_values:
            The value to assign to the field_values property of this SuggestOutput.
        :type field_values: list[str]

        :param terms:
            The value to assign to the terms property of this SuggestOutput.
        :type terms: list[str]

        :param options:
            The value to assign to the options property of this SuggestOutput.
        :type options: list[str]

        :param examples:
            The value to assign to the examples property of this SuggestOutput.
        :type examples: list[str]

        """
        self.swagger_types = {
            'position': 'int',
            'commands': 'list[str]',
            'fields': 'list[str]',
            'field_values': 'list[str]',
            'terms': 'list[str]',
            'options': 'list[str]',
            'examples': 'list[str]'
        }

        self.attribute_map = {
            'position': 'position',
            'commands': 'commands',
            'fields': 'fields',
            'field_values': 'fieldValues',
            'terms': 'terms',
            'options': 'options',
            'examples': 'examples'
        }

        self._position = None
        self._commands = None
        self._fields = None
        self._field_values = None
        self._terms = None
        self._options = None
        self._examples = None

    @property
    def position(self):
        """
        **[Required]** Gets the position of this SuggestOutput.
        Character position suggestion should be placed in queryString provided as input.


        :return: The position of this SuggestOutput.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this SuggestOutput.
        Character position suggestion should be placed in queryString provided as input.


        :param position: The position of this SuggestOutput.
        :type: int
        """
        self._position = position

    @property
    def commands(self):
        """
        Gets the commands of this SuggestOutput.
        Context specific list of querylanguage commands if input is seeking command suggestions.


        :return: The commands of this SuggestOutput.
        :rtype: list[str]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        """
        Sets the commands of this SuggestOutput.
        Context specific list of querylanguage commands if input is seeking command suggestions.


        :param commands: The commands of this SuggestOutput.
        :type: list[str]
        """
        self._commands = commands

    @property
    def fields(self):
        """
        Gets the fields of this SuggestOutput.
        Context specific list of querylanguage fields / columns if input is seeking field / column suggestions.


        :return: The fields of this SuggestOutput.
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this SuggestOutput.
        Context specific list of querylanguage fields / columns if input is seeking field / column suggestions.


        :param fields: The fields of this SuggestOutput.
        :type: list[str]
        """
        self._fields = fields

    @property
    def field_values(self):
        """
        Gets the field_values of this SuggestOutput.
        Context specific list of field values if input is seeking field value suggestions.


        :return: The field_values of this SuggestOutput.
        :rtype: list[str]
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this SuggestOutput.
        Context specific list of field values if input is seeking field value suggestions.


        :param field_values: The field_values of this SuggestOutput.
        :type: list[str]
        """
        self._field_values = field_values

    @property
    def terms(self):
        """
        Gets the terms of this SuggestOutput.
        Context specific list of terms / phrases if input is seeking terms / phrase suggestions.


        :return: The terms of this SuggestOutput.
        :rtype: list[str]
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """
        Sets the terms of this SuggestOutput.
        Context specific list of terms / phrases if input is seeking terms / phrase suggestions.


        :param terms: The terms of this SuggestOutput.
        :type: list[str]
        """
        self._terms = terms

    @property
    def options(self):
        """
        Gets the options of this SuggestOutput.
        Context specific list of querylanguage command options if input is seeking command option suggestions.


        :return: The options of this SuggestOutput.
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this SuggestOutput.
        Context specific list of querylanguage command options if input is seeking command option suggestions.


        :param options: The options of this SuggestOutput.
        :type: list[str]
        """
        self._options = options

    @property
    def examples(self):
        """
        Gets the examples of this SuggestOutput.
        Context specific list of querylanguage querystring examples if input is seeking queryString example suggestions.


        :return: The examples of this SuggestOutput.
        :rtype: list[str]
        """
        return self._examples

    @examples.setter
    def examples(self, examples):
        """
        Sets the examples of this SuggestOutput.
        Context specific list of querylanguage querystring examples if input is seeking queryString example suggestions.


        :param examples: The examples of this SuggestOutput.
        :type: list[str]
        """
        self._examples = examples

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
