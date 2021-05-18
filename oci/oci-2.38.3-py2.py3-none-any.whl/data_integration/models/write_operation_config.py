# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_data_operation_config import AbstractDataOperationConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WriteOperationConfig(AbstractDataOperationConfig):
    """
    The information about the write operation.
    """

    #: A constant which can be used with the write_mode property of a WriteOperationConfig.
    #: This constant has a value of "OVERWRITE"
    WRITE_MODE_OVERWRITE = "OVERWRITE"

    #: A constant which can be used with the write_mode property of a WriteOperationConfig.
    #: This constant has a value of "APPEND"
    WRITE_MODE_APPEND = "APPEND"

    #: A constant which can be used with the write_mode property of a WriteOperationConfig.
    #: This constant has a value of "MERGE"
    WRITE_MODE_MERGE = "MERGE"

    #: A constant which can be used with the write_mode property of a WriteOperationConfig.
    #: This constant has a value of "IGNORE"
    WRITE_MODE_IGNORE = "IGNORE"

    def __init__(self, **kwargs):
        """
        Initializes a new WriteOperationConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.WriteOperationConfig.model_type` attribute
        of this class is ``WRITE_OPERATION_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this WriteOperationConfig.
            Allowed values for this property are: "READ_OPERATION_CONFIG", "WRITE_OPERATION_CONFIG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this WriteOperationConfig.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this WriteOperationConfig.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this WriteOperationConfig.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param operations:
            The value to assign to the operations property of this WriteOperationConfig.
        :type operations: list[oci.data_integration.models.PushDownOperation]

        :param data_format:
            The value to assign to the data_format property of this WriteOperationConfig.
        :type data_format: oci.data_integration.models.DataFormat

        :param partition_config:
            The value to assign to the partition_config property of this WriteOperationConfig.
        :type partition_config: oci.data_integration.models.PartitionConfig

        :param write_attribute:
            The value to assign to the write_attribute property of this WriteOperationConfig.
        :type write_attribute: oci.data_integration.models.AbstractWriteAttribute

        :param write_mode:
            The value to assign to the write_mode property of this WriteOperationConfig.
            Allowed values for this property are: "OVERWRITE", "APPEND", "MERGE", "IGNORE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type write_mode: str

        :param merge_key:
            The value to assign to the merge_key property of this WriteOperationConfig.
        :type merge_key: oci.data_integration.models.UniqueKey

        :param object_status:
            The value to assign to the object_status property of this WriteOperationConfig.
        :type object_status: int

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'operations': 'list[PushDownOperation]',
            'data_format': 'DataFormat',
            'partition_config': 'PartitionConfig',
            'write_attribute': 'AbstractWriteAttribute',
            'write_mode': 'str',
            'merge_key': 'UniqueKey',
            'object_status': 'int'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'operations': 'operations',
            'data_format': 'dataFormat',
            'partition_config': 'partitionConfig',
            'write_attribute': 'writeAttribute',
            'write_mode': 'writeMode',
            'merge_key': 'mergeKey',
            'object_status': 'objectStatus'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._operations = None
        self._data_format = None
        self._partition_config = None
        self._write_attribute = None
        self._write_mode = None
        self._merge_key = None
        self._object_status = None
        self._model_type = 'WRITE_OPERATION_CONFIG'

    @property
    def key(self):
        """
        Gets the key of this WriteOperationConfig.
        The object key.


        :return: The key of this WriteOperationConfig.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this WriteOperationConfig.
        The object key.


        :param key: The key of this WriteOperationConfig.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this WriteOperationConfig.
        The object's model version.


        :return: The model_version of this WriteOperationConfig.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this WriteOperationConfig.
        The object's model version.


        :param model_version: The model_version of this WriteOperationConfig.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this WriteOperationConfig.

        :return: The parent_ref of this WriteOperationConfig.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this WriteOperationConfig.

        :param parent_ref: The parent_ref of this WriteOperationConfig.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def operations(self):
        """
        Gets the operations of this WriteOperationConfig.
        An array of operations.


        :return: The operations of this WriteOperationConfig.
        :rtype: list[oci.data_integration.models.PushDownOperation]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """
        Sets the operations of this WriteOperationConfig.
        An array of operations.


        :param operations: The operations of this WriteOperationConfig.
        :type: list[oci.data_integration.models.PushDownOperation]
        """
        self._operations = operations

    @property
    def data_format(self):
        """
        Gets the data_format of this WriteOperationConfig.

        :return: The data_format of this WriteOperationConfig.
        :rtype: oci.data_integration.models.DataFormat
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """
        Sets the data_format of this WriteOperationConfig.

        :param data_format: The data_format of this WriteOperationConfig.
        :type: oci.data_integration.models.DataFormat
        """
        self._data_format = data_format

    @property
    def partition_config(self):
        """
        Gets the partition_config of this WriteOperationConfig.

        :return: The partition_config of this WriteOperationConfig.
        :rtype: oci.data_integration.models.PartitionConfig
        """
        return self._partition_config

    @partition_config.setter
    def partition_config(self, partition_config):
        """
        Sets the partition_config of this WriteOperationConfig.

        :param partition_config: The partition_config of this WriteOperationConfig.
        :type: oci.data_integration.models.PartitionConfig
        """
        self._partition_config = partition_config

    @property
    def write_attribute(self):
        """
        Gets the write_attribute of this WriteOperationConfig.

        :return: The write_attribute of this WriteOperationConfig.
        :rtype: oci.data_integration.models.AbstractWriteAttribute
        """
        return self._write_attribute

    @write_attribute.setter
    def write_attribute(self, write_attribute):
        """
        Sets the write_attribute of this WriteOperationConfig.

        :param write_attribute: The write_attribute of this WriteOperationConfig.
        :type: oci.data_integration.models.AbstractWriteAttribute
        """
        self._write_attribute = write_attribute

    @property
    def write_mode(self):
        """
        Gets the write_mode of this WriteOperationConfig.
        The mode for the write operation.

        Allowed values for this property are: "OVERWRITE", "APPEND", "MERGE", "IGNORE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The write_mode of this WriteOperationConfig.
        :rtype: str
        """
        return self._write_mode

    @write_mode.setter
    def write_mode(self, write_mode):
        """
        Sets the write_mode of this WriteOperationConfig.
        The mode for the write operation.


        :param write_mode: The write_mode of this WriteOperationConfig.
        :type: str
        """
        allowed_values = ["OVERWRITE", "APPEND", "MERGE", "IGNORE"]
        if not value_allowed_none_or_none_sentinel(write_mode, allowed_values):
            write_mode = 'UNKNOWN_ENUM_VALUE'
        self._write_mode = write_mode

    @property
    def merge_key(self):
        """
        Gets the merge_key of this WriteOperationConfig.

        :return: The merge_key of this WriteOperationConfig.
        :rtype: oci.data_integration.models.UniqueKey
        """
        return self._merge_key

    @merge_key.setter
    def merge_key(self, merge_key):
        """
        Sets the merge_key of this WriteOperationConfig.

        :param merge_key: The merge_key of this WriteOperationConfig.
        :type: oci.data_integration.models.UniqueKey
        """
        self._merge_key = merge_key

    @property
    def object_status(self):
        """
        Gets the object_status of this WriteOperationConfig.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this WriteOperationConfig.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this WriteOperationConfig.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this WriteOperationConfig.
        :type: int
        """
        self._object_status = object_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
