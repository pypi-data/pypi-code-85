# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SummarizeHostInsightResourceUsageAggregation(object):
    """
    Resource usage summation for the current time period.
    """

    #: A constant which can be used with the resource_metric property of a SummarizeHostInsightResourceUsageAggregation.
    #: This constant has a value of "CPU"
    RESOURCE_METRIC_CPU = "CPU"

    #: A constant which can be used with the resource_metric property of a SummarizeHostInsightResourceUsageAggregation.
    #: This constant has a value of "MEMORY"
    RESOURCE_METRIC_MEMORY = "MEMORY"

    #: A constant which can be used with the resource_metric property of a SummarizeHostInsightResourceUsageAggregation.
    #: This constant has a value of "LOGICAL_MEMORY"
    RESOURCE_METRIC_LOGICAL_MEMORY = "LOGICAL_MEMORY"

    #: A constant which can be used with the usage_unit property of a SummarizeHostInsightResourceUsageAggregation.
    #: This constant has a value of "CORES"
    USAGE_UNIT_CORES = "CORES"

    #: A constant which can be used with the usage_unit property of a SummarizeHostInsightResourceUsageAggregation.
    #: This constant has a value of "GB"
    USAGE_UNIT_GB = "GB"

    #: A constant which can be used with the usage_unit property of a SummarizeHostInsightResourceUsageAggregation.
    #: This constant has a value of "MBPS"
    USAGE_UNIT_MBPS = "MBPS"

    #: A constant which can be used with the usage_unit property of a SummarizeHostInsightResourceUsageAggregation.
    #: This constant has a value of "PERCENT"
    USAGE_UNIT_PERCENT = "PERCENT"

    def __init__(self, **kwargs):
        """
        Initializes a new SummarizeHostInsightResourceUsageAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_interval_start:
            The value to assign to the time_interval_start property of this SummarizeHostInsightResourceUsageAggregation.
        :type time_interval_start: datetime

        :param time_interval_end:
            The value to assign to the time_interval_end property of this SummarizeHostInsightResourceUsageAggregation.
        :type time_interval_end: datetime

        :param resource_metric:
            The value to assign to the resource_metric property of this SummarizeHostInsightResourceUsageAggregation.
            Allowed values for this property are: "CPU", "MEMORY", "LOGICAL_MEMORY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_metric: str

        :param usage_unit:
            The value to assign to the usage_unit property of this SummarizeHostInsightResourceUsageAggregation.
            Allowed values for this property are: "CORES", "GB", "MBPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type usage_unit: str

        :param usage:
            The value to assign to the usage property of this SummarizeHostInsightResourceUsageAggregation.
        :type usage: float

        :param capacity:
            The value to assign to the capacity property of this SummarizeHostInsightResourceUsageAggregation.
        :type capacity: float

        :param usage_change_percent:
            The value to assign to the usage_change_percent property of this SummarizeHostInsightResourceUsageAggregation.
        :type usage_change_percent: float

        """
        self.swagger_types = {
            'time_interval_start': 'datetime',
            'time_interval_end': 'datetime',
            'resource_metric': 'str',
            'usage_unit': 'str',
            'usage': 'float',
            'capacity': 'float',
            'usage_change_percent': 'float'
        }

        self.attribute_map = {
            'time_interval_start': 'timeIntervalStart',
            'time_interval_end': 'timeIntervalEnd',
            'resource_metric': 'resourceMetric',
            'usage_unit': 'usageUnit',
            'usage': 'usage',
            'capacity': 'capacity',
            'usage_change_percent': 'usageChangePercent'
        }

        self._time_interval_start = None
        self._time_interval_end = None
        self._resource_metric = None
        self._usage_unit = None
        self._usage = None
        self._capacity = None
        self._usage_change_percent = None

    @property
    def time_interval_start(self):
        """
        **[Required]** Gets the time_interval_start of this SummarizeHostInsightResourceUsageAggregation.
        The start timestamp that was passed into the request.


        :return: The time_interval_start of this SummarizeHostInsightResourceUsageAggregation.
        :rtype: datetime
        """
        return self._time_interval_start

    @time_interval_start.setter
    def time_interval_start(self, time_interval_start):
        """
        Sets the time_interval_start of this SummarizeHostInsightResourceUsageAggregation.
        The start timestamp that was passed into the request.


        :param time_interval_start: The time_interval_start of this SummarizeHostInsightResourceUsageAggregation.
        :type: datetime
        """
        self._time_interval_start = time_interval_start

    @property
    def time_interval_end(self):
        """
        **[Required]** Gets the time_interval_end of this SummarizeHostInsightResourceUsageAggregation.
        The end timestamp that was passed into the request.


        :return: The time_interval_end of this SummarizeHostInsightResourceUsageAggregation.
        :rtype: datetime
        """
        return self._time_interval_end

    @time_interval_end.setter
    def time_interval_end(self, time_interval_end):
        """
        Sets the time_interval_end of this SummarizeHostInsightResourceUsageAggregation.
        The end timestamp that was passed into the request.


        :param time_interval_end: The time_interval_end of this SummarizeHostInsightResourceUsageAggregation.
        :type: datetime
        """
        self._time_interval_end = time_interval_end

    @property
    def resource_metric(self):
        """
        **[Required]** Gets the resource_metric of this SummarizeHostInsightResourceUsageAggregation.
        Defines the type of resource metric (CPU, Physical Memory, Logical Memory)

        Allowed values for this property are: "CPU", "MEMORY", "LOGICAL_MEMORY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_metric of this SummarizeHostInsightResourceUsageAggregation.
        :rtype: str
        """
        return self._resource_metric

    @resource_metric.setter
    def resource_metric(self, resource_metric):
        """
        Sets the resource_metric of this SummarizeHostInsightResourceUsageAggregation.
        Defines the type of resource metric (CPU, Physical Memory, Logical Memory)


        :param resource_metric: The resource_metric of this SummarizeHostInsightResourceUsageAggregation.
        :type: str
        """
        allowed_values = ["CPU", "MEMORY", "LOGICAL_MEMORY"]
        if not value_allowed_none_or_none_sentinel(resource_metric, allowed_values):
            resource_metric = 'UNKNOWN_ENUM_VALUE'
        self._resource_metric = resource_metric

    @property
    def usage_unit(self):
        """
        **[Required]** Gets the usage_unit of this SummarizeHostInsightResourceUsageAggregation.
        Displays usage unit (CORES, GB)

        Allowed values for this property are: "CORES", "GB", "MBPS", "PERCENT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The usage_unit of this SummarizeHostInsightResourceUsageAggregation.
        :rtype: str
        """
        return self._usage_unit

    @usage_unit.setter
    def usage_unit(self, usage_unit):
        """
        Sets the usage_unit of this SummarizeHostInsightResourceUsageAggregation.
        Displays usage unit (CORES, GB)


        :param usage_unit: The usage_unit of this SummarizeHostInsightResourceUsageAggregation.
        :type: str
        """
        allowed_values = ["CORES", "GB", "MBPS", "PERCENT"]
        if not value_allowed_none_or_none_sentinel(usage_unit, allowed_values):
            usage_unit = 'UNKNOWN_ENUM_VALUE'
        self._usage_unit = usage_unit

    @property
    def usage(self):
        """
        **[Required]** Gets the usage of this SummarizeHostInsightResourceUsageAggregation.
        Total amount used of the resource metric type (CPU, STORAGE).


        :return: The usage of this SummarizeHostInsightResourceUsageAggregation.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this SummarizeHostInsightResourceUsageAggregation.
        Total amount used of the resource metric type (CPU, STORAGE).


        :param usage: The usage of this SummarizeHostInsightResourceUsageAggregation.
        :type: float
        """
        self._usage = usage

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this SummarizeHostInsightResourceUsageAggregation.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE).


        :return: The capacity of this SummarizeHostInsightResourceUsageAggregation.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this SummarizeHostInsightResourceUsageAggregation.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE).


        :param capacity: The capacity of this SummarizeHostInsightResourceUsageAggregation.
        :type: float
        """
        self._capacity = capacity

    @property
    def usage_change_percent(self):
        """
        **[Required]** Gets the usage_change_percent of this SummarizeHostInsightResourceUsageAggregation.
        Percentage change in resource usage during the current period calculated using linear regression functions


        :return: The usage_change_percent of this SummarizeHostInsightResourceUsageAggregation.
        :rtype: float
        """
        return self._usage_change_percent

    @usage_change_percent.setter
    def usage_change_percent(self, usage_change_percent):
        """
        Sets the usage_change_percent of this SummarizeHostInsightResourceUsageAggregation.
        Percentage change in resource usage during the current period calculated using linear regression functions


        :param usage_change_percent: The usage_change_percent of this SummarizeHostInsightResourceUsageAggregation.
        :type: float
        """
        self._usage_change_percent = usage_change_percent

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
