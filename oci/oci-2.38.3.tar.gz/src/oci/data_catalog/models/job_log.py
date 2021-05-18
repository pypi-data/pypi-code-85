# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobLog(object):
    """
    Job log details. A job log is an audit log record inserted during the lifecycle of a job execution instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobLog object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this JobLog.
        :type key: str

        :param job_execution_key:
            The value to assign to the job_execution_key property of this JobLog.
        :type job_execution_key: str

        :param created_by_id:
            The value to assign to the created_by_id property of this JobLog.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this JobLog.
        :type updated_by_id: str

        :param time_updated:
            The value to assign to the time_updated property of this JobLog.
        :type time_updated: datetime

        :param time_created:
            The value to assign to the time_created property of this JobLog.
        :type time_created: datetime

        :param severity:
            The value to assign to the severity property of this JobLog.
        :type severity: str

        :param log_message:
            The value to assign to the log_message property of this JobLog.
        :type log_message: str

        :param uri:
            The value to assign to the uri property of this JobLog.
        :type uri: str

        """
        self.swagger_types = {
            'key': 'str',
            'job_execution_key': 'str',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'time_updated': 'datetime',
            'time_created': 'datetime',
            'severity': 'str',
            'log_message': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'job_execution_key': 'jobExecutionKey',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'time_updated': 'timeUpdated',
            'time_created': 'timeCreated',
            'severity': 'severity',
            'log_message': 'logMessage',
            'uri': 'uri'
        }

        self._key = None
        self._job_execution_key = None
        self._created_by_id = None
        self._updated_by_id = None
        self._time_updated = None
        self._time_created = None
        self._severity = None
        self._log_message = None
        self._uri = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this JobLog.
        Unique key of the job log that is immutable.


        :return: The key of this JobLog.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this JobLog.
        Unique key of the job log that is immutable.


        :param key: The key of this JobLog.
        :type: str
        """
        self._key = key

    @property
    def job_execution_key(self):
        """
        Gets the job_execution_key of this JobLog.
        The unique key of the parent job execution for which the log resource was created.


        :return: The job_execution_key of this JobLog.
        :rtype: str
        """
        return self._job_execution_key

    @job_execution_key.setter
    def job_execution_key(self, job_execution_key):
        """
        Sets the job_execution_key of this JobLog.
        The unique key of the parent job execution for which the log resource was created.


        :param job_execution_key: The job_execution_key of this JobLog.
        :type: str
        """
        self._job_execution_key = job_execution_key

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this JobLog.
        OCID of the user who created the log record for this job. Usually the executor of the job instance.


        :return: The created_by_id of this JobLog.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this JobLog.
        OCID of the user who created the log record for this job. Usually the executor of the job instance.


        :param created_by_id: The created_by_id of this JobLog.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this JobLog.
        OCID of the user who created the log record for this job. Usually the executor of the job instance.


        :return: The updated_by_id of this JobLog.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this JobLog.
        OCID of the user who created the log record for this job. Usually the executor of the job instance.


        :param updated_by_id: The updated_by_id of this JobLog.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def time_updated(self):
        """
        Gets the time_updated of this JobLog.
        Job log update time. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this JobLog.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this JobLog.
        Job log update time. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this JobLog.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def time_created(self):
        """
        Gets the time_created of this JobLog.
        The date and time the job log was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this JobLog.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobLog.
        The date and time the job log was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this JobLog.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def severity(self):
        """
        Gets the severity of this JobLog.
        Severity level for this log.


        :return: The severity of this JobLog.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this JobLog.
        Severity level for this log.


        :param severity: The severity of this JobLog.
        :type: str
        """
        self._severity = severity

    @property
    def log_message(self):
        """
        Gets the log_message of this JobLog.
        Message for this job log.


        :return: The log_message of this JobLog.
        :rtype: str
        """
        return self._log_message

    @log_message.setter
    def log_message(self, log_message):
        """
        Sets the log_message of this JobLog.
        Message for this job log.


        :param log_message: The log_message of this JobLog.
        :type: str
        """
        self._log_message = log_message

    @property
    def uri(self):
        """
        Gets the uri of this JobLog.
        URI to the job log instance in the API.


        :return: The uri of this JobLog.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this JobLog.
        URI to the job log instance in the API.


        :param uri: The uri of this JobLog.
        :type: str
        """
        self._uri = uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
