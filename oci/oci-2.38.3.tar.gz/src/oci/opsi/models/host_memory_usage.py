# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_performance_metric_group import HostPerformanceMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostMemoryUsage(HostPerformanceMetricGroup):
    """
    Memory usage metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostMemoryUsage object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostMemoryUsage.metric_name` attribute
        of this class is ``HOST_MEMORY_USAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostMemoryUsage.
            Allowed values for this property are: "HOST_CPU_USAGE", "HOST_MEMORY_USAGE", "HOST_NETWORK_ACTIVITY_SUMMARY"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostMemoryUsage.
        :type time_collected: datetime

        :param memory_used_in_gb:
            The value to assign to the memory_used_in_gb property of this HostMemoryUsage.
        :type memory_used_in_gb: float

        :param memory_utilization_in_percent:
            The value to assign to the memory_utilization_in_percent property of this HostMemoryUsage.
        :type memory_utilization_in_percent: float

        :param memory_load_in_gb:
            The value to assign to the memory_load_in_gb property of this HostMemoryUsage.
        :type memory_load_in_gb: float

        :param real_memory_in_kb:
            The value to assign to the real_memory_in_kb property of this HostMemoryUsage.
        :type real_memory_in_kb: float

        :param free_memory_in_kb:
            The value to assign to the free_memory_in_kb property of this HostMemoryUsage.
        :type free_memory_in_kb: float

        :param logical_memory_used_in_gb:
            The value to assign to the logical_memory_used_in_gb property of this HostMemoryUsage.
        :type logical_memory_used_in_gb: float

        :param logical_memory_utilization_in_percent:
            The value to assign to the logical_memory_utilization_in_percent property of this HostMemoryUsage.
        :type logical_memory_utilization_in_percent: float

        :param free_logical_memory_in_kb:
            The value to assign to the free_logical_memory_in_kb property of this HostMemoryUsage.
        :type free_logical_memory_in_kb: float

        :param major_page_faults:
            The value to assign to the major_page_faults property of this HostMemoryUsage.
        :type major_page_faults: int

        :param swap_free_in_kb:
            The value to assign to the swap_free_in_kb property of this HostMemoryUsage.
        :type swap_free_in_kb: float

        :param anon_huge_pages_in_kb:
            The value to assign to the anon_huge_pages_in_kb property of this HostMemoryUsage.
        :type anon_huge_pages_in_kb: float

        :param huge_pages_free:
            The value to assign to the huge_pages_free property of this HostMemoryUsage.
        :type huge_pages_free: int

        :param huge_pages_reserved:
            The value to assign to the huge_pages_reserved property of this HostMemoryUsage.
        :type huge_pages_reserved: int

        :param huge_pages_surplus:
            The value to assign to the huge_pages_surplus property of this HostMemoryUsage.
        :type huge_pages_surplus: int

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'memory_used_in_gb': 'float',
            'memory_utilization_in_percent': 'float',
            'memory_load_in_gb': 'float',
            'real_memory_in_kb': 'float',
            'free_memory_in_kb': 'float',
            'logical_memory_used_in_gb': 'float',
            'logical_memory_utilization_in_percent': 'float',
            'free_logical_memory_in_kb': 'float',
            'major_page_faults': 'int',
            'swap_free_in_kb': 'float',
            'anon_huge_pages_in_kb': 'float',
            'huge_pages_free': 'int',
            'huge_pages_reserved': 'int',
            'huge_pages_surplus': 'int'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'memory_used_in_gb': 'memoryUsedInGB',
            'memory_utilization_in_percent': 'memoryUtilizationInPercent',
            'memory_load_in_gb': 'memoryLoadInGB',
            'real_memory_in_kb': 'realMemoryInKB',
            'free_memory_in_kb': 'freeMemoryInKB',
            'logical_memory_used_in_gb': 'logicalMemoryUsedInGB',
            'logical_memory_utilization_in_percent': 'logicalMemoryUtilizationInPercent',
            'free_logical_memory_in_kb': 'freeLogicalMemoryInKB',
            'major_page_faults': 'majorPageFaults',
            'swap_free_in_kb': 'swapFreeInKB',
            'anon_huge_pages_in_kb': 'anonHugePagesInKB',
            'huge_pages_free': 'hugePagesFree',
            'huge_pages_reserved': 'hugePagesReserved',
            'huge_pages_surplus': 'hugePagesSurplus'
        }

        self._metric_name = None
        self._time_collected = None
        self._memory_used_in_gb = None
        self._memory_utilization_in_percent = None
        self._memory_load_in_gb = None
        self._real_memory_in_kb = None
        self._free_memory_in_kb = None
        self._logical_memory_used_in_gb = None
        self._logical_memory_utilization_in_percent = None
        self._free_logical_memory_in_kb = None
        self._major_page_faults = None
        self._swap_free_in_kb = None
        self._anon_huge_pages_in_kb = None
        self._huge_pages_free = None
        self._huge_pages_reserved = None
        self._huge_pages_surplus = None
        self._metric_name = 'HOST_MEMORY_USAGE'

    @property
    def memory_used_in_gb(self):
        """
        Gets the memory_used_in_gb of this HostMemoryUsage.
        Amount of physical memory used in gigabytes


        :return: The memory_used_in_gb of this HostMemoryUsage.
        :rtype: float
        """
        return self._memory_used_in_gb

    @memory_used_in_gb.setter
    def memory_used_in_gb(self, memory_used_in_gb):
        """
        Sets the memory_used_in_gb of this HostMemoryUsage.
        Amount of physical memory used in gigabytes


        :param memory_used_in_gb: The memory_used_in_gb of this HostMemoryUsage.
        :type: float
        """
        self._memory_used_in_gb = memory_used_in_gb

    @property
    def memory_utilization_in_percent(self):
        """
        Gets the memory_utilization_in_percent of this HostMemoryUsage.
        Amount of physical memory used in percentage


        :return: The memory_utilization_in_percent of this HostMemoryUsage.
        :rtype: float
        """
        return self._memory_utilization_in_percent

    @memory_utilization_in_percent.setter
    def memory_utilization_in_percent(self, memory_utilization_in_percent):
        """
        Sets the memory_utilization_in_percent of this HostMemoryUsage.
        Amount of physical memory used in percentage


        :param memory_utilization_in_percent: The memory_utilization_in_percent of this HostMemoryUsage.
        :type: float
        """
        self._memory_utilization_in_percent = memory_utilization_in_percent

    @property
    def memory_load_in_gb(self):
        """
        Gets the memory_load_in_gb of this HostMemoryUsage.
        Load on memory in gigabytes


        :return: The memory_load_in_gb of this HostMemoryUsage.
        :rtype: float
        """
        return self._memory_load_in_gb

    @memory_load_in_gb.setter
    def memory_load_in_gb(self, memory_load_in_gb):
        """
        Sets the memory_load_in_gb of this HostMemoryUsage.
        Load on memory in gigabytes


        :param memory_load_in_gb: The memory_load_in_gb of this HostMemoryUsage.
        :type: float
        """
        self._memory_load_in_gb = memory_load_in_gb

    @property
    def real_memory_in_kb(self):
        """
        Gets the real_memory_in_kb of this HostMemoryUsage.
        Amount of usable physical memory in kilobytes


        :return: The real_memory_in_kb of this HostMemoryUsage.
        :rtype: float
        """
        return self._real_memory_in_kb

    @real_memory_in_kb.setter
    def real_memory_in_kb(self, real_memory_in_kb):
        """
        Sets the real_memory_in_kb of this HostMemoryUsage.
        Amount of usable physical memory in kilobytes


        :param real_memory_in_kb: The real_memory_in_kb of this HostMemoryUsage.
        :type: float
        """
        self._real_memory_in_kb = real_memory_in_kb

    @property
    def free_memory_in_kb(self):
        """
        Gets the free_memory_in_kb of this HostMemoryUsage.
        Amount of available physical memory in kilobytes


        :return: The free_memory_in_kb of this HostMemoryUsage.
        :rtype: float
        """
        return self._free_memory_in_kb

    @free_memory_in_kb.setter
    def free_memory_in_kb(self, free_memory_in_kb):
        """
        Sets the free_memory_in_kb of this HostMemoryUsage.
        Amount of available physical memory in kilobytes


        :param free_memory_in_kb: The free_memory_in_kb of this HostMemoryUsage.
        :type: float
        """
        self._free_memory_in_kb = free_memory_in_kb

    @property
    def logical_memory_used_in_gb(self):
        """
        Gets the logical_memory_used_in_gb of this HostMemoryUsage.
        Memory used excluding buffers and cache in gigabytes


        :return: The logical_memory_used_in_gb of this HostMemoryUsage.
        :rtype: float
        """
        return self._logical_memory_used_in_gb

    @logical_memory_used_in_gb.setter
    def logical_memory_used_in_gb(self, logical_memory_used_in_gb):
        """
        Sets the logical_memory_used_in_gb of this HostMemoryUsage.
        Memory used excluding buffers and cache in gigabytes


        :param logical_memory_used_in_gb: The logical_memory_used_in_gb of this HostMemoryUsage.
        :type: float
        """
        self._logical_memory_used_in_gb = logical_memory_used_in_gb

    @property
    def logical_memory_utilization_in_percent(self):
        """
        Gets the logical_memory_utilization_in_percent of this HostMemoryUsage.
        Amount of logical memory used in percentage


        :return: The logical_memory_utilization_in_percent of this HostMemoryUsage.
        :rtype: float
        """
        return self._logical_memory_utilization_in_percent

    @logical_memory_utilization_in_percent.setter
    def logical_memory_utilization_in_percent(self, logical_memory_utilization_in_percent):
        """
        Sets the logical_memory_utilization_in_percent of this HostMemoryUsage.
        Amount of logical memory used in percentage


        :param logical_memory_utilization_in_percent: The logical_memory_utilization_in_percent of this HostMemoryUsage.
        :type: float
        """
        self._logical_memory_utilization_in_percent = logical_memory_utilization_in_percent

    @property
    def free_logical_memory_in_kb(self):
        """
        Gets the free_logical_memory_in_kb of this HostMemoryUsage.
        Amount of avaiable virtual memory in kilobytes


        :return: The free_logical_memory_in_kb of this HostMemoryUsage.
        :rtype: float
        """
        return self._free_logical_memory_in_kb

    @free_logical_memory_in_kb.setter
    def free_logical_memory_in_kb(self, free_logical_memory_in_kb):
        """
        Sets the free_logical_memory_in_kb of this HostMemoryUsage.
        Amount of avaiable virtual memory in kilobytes


        :param free_logical_memory_in_kb: The free_logical_memory_in_kb of this HostMemoryUsage.
        :type: float
        """
        self._free_logical_memory_in_kb = free_logical_memory_in_kb

    @property
    def major_page_faults(self):
        """
        Gets the major_page_faults of this HostMemoryUsage.
        Number of major page faults


        :return: The major_page_faults of this HostMemoryUsage.
        :rtype: int
        """
        return self._major_page_faults

    @major_page_faults.setter
    def major_page_faults(self, major_page_faults):
        """
        Sets the major_page_faults of this HostMemoryUsage.
        Number of major page faults


        :param major_page_faults: The major_page_faults of this HostMemoryUsage.
        :type: int
        """
        self._major_page_faults = major_page_faults

    @property
    def swap_free_in_kb(self):
        """
        Gets the swap_free_in_kb of this HostMemoryUsage.
        Amount of available swap space in kilobytes


        :return: The swap_free_in_kb of this HostMemoryUsage.
        :rtype: float
        """
        return self._swap_free_in_kb

    @swap_free_in_kb.setter
    def swap_free_in_kb(self, swap_free_in_kb):
        """
        Sets the swap_free_in_kb of this HostMemoryUsage.
        Amount of available swap space in kilobytes


        :param swap_free_in_kb: The swap_free_in_kb of this HostMemoryUsage.
        :type: float
        """
        self._swap_free_in_kb = swap_free_in_kb

    @property
    def anon_huge_pages_in_kb(self):
        """
        Gets the anon_huge_pages_in_kb of this HostMemoryUsage.
        Amount of memory used for anon huge pages in kilobytes


        :return: The anon_huge_pages_in_kb of this HostMemoryUsage.
        :rtype: float
        """
        return self._anon_huge_pages_in_kb

    @anon_huge_pages_in_kb.setter
    def anon_huge_pages_in_kb(self, anon_huge_pages_in_kb):
        """
        Sets the anon_huge_pages_in_kb of this HostMemoryUsage.
        Amount of memory used for anon huge pages in kilobytes


        :param anon_huge_pages_in_kb: The anon_huge_pages_in_kb of this HostMemoryUsage.
        :type: float
        """
        self._anon_huge_pages_in_kb = anon_huge_pages_in_kb

    @property
    def huge_pages_free(self):
        """
        Gets the huge_pages_free of this HostMemoryUsage.
        Number of available huge pages


        :return: The huge_pages_free of this HostMemoryUsage.
        :rtype: int
        """
        return self._huge_pages_free

    @huge_pages_free.setter
    def huge_pages_free(self, huge_pages_free):
        """
        Sets the huge_pages_free of this HostMemoryUsage.
        Number of available huge pages


        :param huge_pages_free: The huge_pages_free of this HostMemoryUsage.
        :type: int
        """
        self._huge_pages_free = huge_pages_free

    @property
    def huge_pages_reserved(self):
        """
        Gets the huge_pages_reserved of this HostMemoryUsage.
        Number of reserved huge pages


        :return: The huge_pages_reserved of this HostMemoryUsage.
        :rtype: int
        """
        return self._huge_pages_reserved

    @huge_pages_reserved.setter
    def huge_pages_reserved(self, huge_pages_reserved):
        """
        Sets the huge_pages_reserved of this HostMemoryUsage.
        Number of reserved huge pages


        :param huge_pages_reserved: The huge_pages_reserved of this HostMemoryUsage.
        :type: int
        """
        self._huge_pages_reserved = huge_pages_reserved

    @property
    def huge_pages_surplus(self):
        """
        Gets the huge_pages_surplus of this HostMemoryUsage.
        Number of surplus huge pages


        :return: The huge_pages_surplus of this HostMemoryUsage.
        :rtype: int
        """
        return self._huge_pages_surplus

    @huge_pages_surplus.setter
    def huge_pages_surplus(self, huge_pages_surplus):
        """
        Sets the huge_pages_surplus of this HostMemoryUsage.
        Number of surplus huge pages


        :param huge_pages_surplus: The huge_pages_surplus of this HostMemoryUsage.
        :type: int
        """
        self._huge_pages_surplus = huge_pages_surplus

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
