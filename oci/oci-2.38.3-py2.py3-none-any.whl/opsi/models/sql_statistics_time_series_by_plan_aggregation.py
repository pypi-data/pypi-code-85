# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlStatisticsTimeSeriesByPlanAggregation(object):
    """
    SQL performance statistics for a given plan
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlStatisticsTimeSeriesByPlanAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param plan_hash:
            The value to assign to the plan_hash property of this SqlStatisticsTimeSeriesByPlanAggregation.
        :type plan_hash: int

        :param statistics:
            The value to assign to the statistics property of this SqlStatisticsTimeSeriesByPlanAggregation.
        :type statistics: list[oci.opsi.models.SqlStatisticsTimeSeries]

        """
        self.swagger_types = {
            'plan_hash': 'int',
            'statistics': 'list[SqlStatisticsTimeSeries]'
        }

        self.attribute_map = {
            'plan_hash': 'planHash',
            'statistics': 'statistics'
        }

        self._plan_hash = None
        self._statistics = None

    @property
    def plan_hash(self):
        """
        **[Required]** Gets the plan_hash of this SqlStatisticsTimeSeriesByPlanAggregation.
        Plan hash value for the SQL Execution Plan


        :return: The plan_hash of this SqlStatisticsTimeSeriesByPlanAggregation.
        :rtype: int
        """
        return self._plan_hash

    @plan_hash.setter
    def plan_hash(self, plan_hash):
        """
        Sets the plan_hash of this SqlStatisticsTimeSeriesByPlanAggregation.
        Plan hash value for the SQL Execution Plan


        :param plan_hash: The plan_hash of this SqlStatisticsTimeSeriesByPlanAggregation.
        :type: int
        """
        self._plan_hash = plan_hash

    @property
    def statistics(self):
        """
        **[Required]** Gets the statistics of this SqlStatisticsTimeSeriesByPlanAggregation.
        SQL performance statistics for a given plan


        :return: The statistics of this SqlStatisticsTimeSeriesByPlanAggregation.
        :rtype: list[oci.opsi.models.SqlStatisticsTimeSeries]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """
        Sets the statistics of this SqlStatisticsTimeSeriesByPlanAggregation.
        SQL performance statistics for a given plan


        :param statistics: The statistics of this SqlStatisticsTimeSeriesByPlanAggregation.
        :type: list[oci.opsi.models.SqlStatisticsTimeSeries]
        """
        self._statistics = statistics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
