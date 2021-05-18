# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .operator import Operator
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Joiner(Operator):
    """
    The information about a joiner object.
    """

    #: A constant which can be used with the join_type property of a Joiner.
    #: This constant has a value of "INNER"
    JOIN_TYPE_INNER = "INNER"

    #: A constant which can be used with the join_type property of a Joiner.
    #: This constant has a value of "FULL"
    JOIN_TYPE_FULL = "FULL"

    #: A constant which can be used with the join_type property of a Joiner.
    #: This constant has a value of "LEFT"
    JOIN_TYPE_LEFT = "LEFT"

    #: A constant which can be used with the join_type property of a Joiner.
    #: This constant has a value of "RIGHT"
    JOIN_TYPE_RIGHT = "RIGHT"

    def __init__(self, **kwargs):
        """
        Initializes a new Joiner object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.Joiner.model_type` attribute
        of this class is ``JOINER_OPERATOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Joiner.
            Allowed values for this property are: "SOURCE_OPERATOR", "FILTER_OPERATOR", "JOINER_OPERATOR", "AGGREGATOR_OPERATOR", "PROJECTION_OPERATOR", "TARGET_OPERATOR", "DISTINCT_OPERATOR", "SORT_OPERATOR", "UNION_OPERATOR", "INTERSECT_OPERATOR", "MINUS_OPERATOR", "MERGE_OPERATOR", "START_OPERATOR", "END_OPERATOR", "PIPELINE_OPERATOR", "REST_OPERATOR", "TASK_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this Joiner.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Joiner.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Joiner.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this Joiner.
        :type name: str

        :param description:
            The value to assign to the description property of this Joiner.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this Joiner.
        :type object_version: int

        :param input_ports:
            The value to assign to the input_ports property of this Joiner.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this Joiner.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param object_status:
            The value to assign to the object_status property of this Joiner.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Joiner.
        :type identifier: str

        :param parameters:
            The value to assign to the parameters property of this Joiner.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this Joiner.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param join_type:
            The value to assign to the join_type property of this Joiner.
            Allowed values for this property are: "INNER", "FULL", "LEFT", "RIGHT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type join_type: str

        :param join_condition:
            The value to assign to the join_condition property of this Joiner.
        :type join_condition: oci.data_integration.models.Expression

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[OutputPort]',
            'object_status': 'int',
            'identifier': 'str',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'join_type': 'str',
            'join_condition': 'Expression'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'join_type': 'joinType',
            'join_condition': 'joinCondition'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._input_ports = None
        self._output_ports = None
        self._object_status = None
        self._identifier = None
        self._parameters = None
        self._op_config_values = None
        self._join_type = None
        self._join_condition = None
        self._model_type = 'JOINER_OPERATOR'

    @property
    def join_type(self):
        """
        Gets the join_type of this Joiner.
        joinType

        Allowed values for this property are: "INNER", "FULL", "LEFT", "RIGHT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The join_type of this Joiner.
        :rtype: str
        """
        return self._join_type

    @join_type.setter
    def join_type(self, join_type):
        """
        Sets the join_type of this Joiner.
        joinType


        :param join_type: The join_type of this Joiner.
        :type: str
        """
        allowed_values = ["INNER", "FULL", "LEFT", "RIGHT"]
        if not value_allowed_none_or_none_sentinel(join_type, allowed_values):
            join_type = 'UNKNOWN_ENUM_VALUE'
        self._join_type = join_type

    @property
    def join_condition(self):
        """
        Gets the join_condition of this Joiner.

        :return: The join_condition of this Joiner.
        :rtype: oci.data_integration.models.Expression
        """
        return self._join_condition

    @join_condition.setter
    def join_condition(self, join_condition):
        """
        Sets the join_condition of this Joiner.

        :param join_condition: The join_condition of this Joiner.
        :type: oci.data_integration.models.Expression
        """
        self._join_condition = join_condition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
