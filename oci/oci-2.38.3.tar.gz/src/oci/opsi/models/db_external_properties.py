# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_configuration_metric_group import DatabaseConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DBExternalProperties(DatabaseConfigurationMetricGroup):
    """
    Configuration parameters defined for external databases.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DBExternalProperties object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.DBExternalProperties.metric_name` attribute
        of this class is ``DB_EXTERNAL_PROPERTIES`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this DBExternalProperties.
            Allowed values for this property are: "DB_EXTERNAL_PROPERTIES", "DB_EXTERNAL_INSTANCE", "DB_OS_CONFIG_INSTANCE"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this DBExternalProperties.
        :type time_collected: datetime

        :param name:
            The value to assign to the name property of this DBExternalProperties.
        :type name: str

        :param log_mode:
            The value to assign to the log_mode property of this DBExternalProperties.
        :type log_mode: str

        :param cdb:
            The value to assign to the cdb property of this DBExternalProperties.
        :type cdb: str

        :param open_mode:
            The value to assign to the open_mode property of this DBExternalProperties.
        :type open_mode: str

        :param database_role:
            The value to assign to the database_role property of this DBExternalProperties.
        :type database_role: str

        :param guard_status:
            The value to assign to the guard_status property of this DBExternalProperties.
        :type guard_status: str

        :param platform_name:
            The value to assign to the platform_name property of this DBExternalProperties.
        :type platform_name: str

        :param control_file_type:
            The value to assign to the control_file_type property of this DBExternalProperties.
        :type control_file_type: str

        :param switchover_status:
            The value to assign to the switchover_status property of this DBExternalProperties.
        :type switchover_status: str

        :param created:
            The value to assign to the created property of this DBExternalProperties.
        :type created: datetime

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'name': 'str',
            'log_mode': 'str',
            'cdb': 'str',
            'open_mode': 'str',
            'database_role': 'str',
            'guard_status': 'str',
            'platform_name': 'str',
            'control_file_type': 'str',
            'switchover_status': 'str',
            'created': 'datetime'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'name': 'name',
            'log_mode': 'logMode',
            'cdb': 'cdb',
            'open_mode': 'openMode',
            'database_role': 'databaseRole',
            'guard_status': 'guardStatus',
            'platform_name': 'platformName',
            'control_file_type': 'controlFileType',
            'switchover_status': 'switchoverStatus',
            'created': 'created'
        }

        self._metric_name = None
        self._time_collected = None
        self._name = None
        self._log_mode = None
        self._cdb = None
        self._open_mode = None
        self._database_role = None
        self._guard_status = None
        self._platform_name = None
        self._control_file_type = None
        self._switchover_status = None
        self._created = None
        self._metric_name = 'DB_EXTERNAL_PROPERTIES'

    @property
    def name(self):
        """
        Gets the name of this DBExternalProperties.
        Name of the database.


        :return: The name of this DBExternalProperties.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DBExternalProperties.
        Name of the database.


        :param name: The name of this DBExternalProperties.
        :type: str
        """
        self._name = name

    @property
    def log_mode(self):
        """
        Gets the log_mode of this DBExternalProperties.
        Archive log mode.


        :return: The log_mode of this DBExternalProperties.
        :rtype: str
        """
        return self._log_mode

    @log_mode.setter
    def log_mode(self, log_mode):
        """
        Sets the log_mode of this DBExternalProperties.
        Archive log mode.


        :param log_mode: The log_mode of this DBExternalProperties.
        :type: str
        """
        self._log_mode = log_mode

    @property
    def cdb(self):
        """
        Gets the cdb of this DBExternalProperties.
        Indicates if it is a CDB or not. This would be 'yes' or 'no'.


        :return: The cdb of this DBExternalProperties.
        :rtype: str
        """
        return self._cdb

    @cdb.setter
    def cdb(self, cdb):
        """
        Sets the cdb of this DBExternalProperties.
        Indicates if it is a CDB or not. This would be 'yes' or 'no'.


        :param cdb: The cdb of this DBExternalProperties.
        :type: str
        """
        self._cdb = cdb

    @property
    def open_mode(self):
        """
        Gets the open_mode of this DBExternalProperties.
        Open mode information.


        :return: The open_mode of this DBExternalProperties.
        :rtype: str
        """
        return self._open_mode

    @open_mode.setter
    def open_mode(self, open_mode):
        """
        Sets the open_mode of this DBExternalProperties.
        Open mode information.


        :param open_mode: The open_mode of this DBExternalProperties.
        :type: str
        """
        self._open_mode = open_mode

    @property
    def database_role(self):
        """
        Gets the database_role of this DBExternalProperties.
        Current role of the database.


        :return: The database_role of this DBExternalProperties.
        :rtype: str
        """
        return self._database_role

    @database_role.setter
    def database_role(self, database_role):
        """
        Sets the database_role of this DBExternalProperties.
        Current role of the database.


        :param database_role: The database_role of this DBExternalProperties.
        :type: str
        """
        self._database_role = database_role

    @property
    def guard_status(self):
        """
        Gets the guard_status of this DBExternalProperties.
        Data protection policy.


        :return: The guard_status of this DBExternalProperties.
        :rtype: str
        """
        return self._guard_status

    @guard_status.setter
    def guard_status(self, guard_status):
        """
        Sets the guard_status of this DBExternalProperties.
        Data protection policy.


        :param guard_status: The guard_status of this DBExternalProperties.
        :type: str
        """
        self._guard_status = guard_status

    @property
    def platform_name(self):
        """
        Gets the platform_name of this DBExternalProperties.
        Platform name of the database, OS with architecture.


        :return: The platform_name of this DBExternalProperties.
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """
        Sets the platform_name of this DBExternalProperties.
        Platform name of the database, OS with architecture.


        :param platform_name: The platform_name of this DBExternalProperties.
        :type: str
        """
        self._platform_name = platform_name

    @property
    def control_file_type(self):
        """
        Gets the control_file_type of this DBExternalProperties.
        Type of control file.


        :return: The control_file_type of this DBExternalProperties.
        :rtype: str
        """
        return self._control_file_type

    @control_file_type.setter
    def control_file_type(self, control_file_type):
        """
        Sets the control_file_type of this DBExternalProperties.
        Type of control file.


        :param control_file_type: The control_file_type of this DBExternalProperties.
        :type: str
        """
        self._control_file_type = control_file_type

    @property
    def switchover_status(self):
        """
        Gets the switchover_status of this DBExternalProperties.
        Indicates whether switchover is allowed.


        :return: The switchover_status of this DBExternalProperties.
        :rtype: str
        """
        return self._switchover_status

    @switchover_status.setter
    def switchover_status(self, switchover_status):
        """
        Sets the switchover_status of this DBExternalProperties.
        Indicates whether switchover is allowed.


        :param switchover_status: The switchover_status of this DBExternalProperties.
        :type: str
        """
        self._switchover_status = switchover_status

    @property
    def created(self):
        """
        Gets the created of this DBExternalProperties.
        Creation time.


        :return: The created of this DBExternalProperties.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this DBExternalProperties.
        Creation time.


        :param created: The created of this DBExternalProperties.
        :type: datetime
        """
        self._created = created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
