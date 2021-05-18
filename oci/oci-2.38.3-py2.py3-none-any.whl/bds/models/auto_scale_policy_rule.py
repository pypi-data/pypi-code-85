# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutoScalePolicyRule(object):
    """
    A rule that defines a specific autoscaling action to take and the metric that triggers that action.
    """

    #: A constant which can be used with the action property of a AutoScalePolicyRule.
    #: This constant has a value of "CHANGE_SHAPE_SCALE_UP"
    ACTION_CHANGE_SHAPE_SCALE_UP = "CHANGE_SHAPE_SCALE_UP"

    #: A constant which can be used with the action property of a AutoScalePolicyRule.
    #: This constant has a value of "CHANGE_SHAPE_SCALE_DOWN"
    ACTION_CHANGE_SHAPE_SCALE_DOWN = "CHANGE_SHAPE_SCALE_DOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new AutoScalePolicyRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this AutoScalePolicyRule.
            Allowed values for this property are: "CHANGE_SHAPE_SCALE_UP", "CHANGE_SHAPE_SCALE_DOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param metric:
            The value to assign to the metric property of this AutoScalePolicyRule.
        :type metric: oci.bds.models.AutoScalePolicyMetricRule

        """
        self.swagger_types = {
            'action': 'str',
            'metric': 'AutoScalePolicyMetricRule'
        }

        self.attribute_map = {
            'action': 'action',
            'metric': 'metric'
        }

        self._action = None
        self._metric = None

    @property
    def action(self):
        """
        **[Required]** Gets the action of this AutoScalePolicyRule.
        The valid value are - CHANGE_SHAPE_SCALE_UP or CHANGE_SHAPE_SCALE_DOWN

        Allowed values for this property are: "CHANGE_SHAPE_SCALE_UP", "CHANGE_SHAPE_SCALE_DOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this AutoScalePolicyRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this AutoScalePolicyRule.
        The valid value are - CHANGE_SHAPE_SCALE_UP or CHANGE_SHAPE_SCALE_DOWN


        :param action: The action of this AutoScalePolicyRule.
        :type: str
        """
        allowed_values = ["CHANGE_SHAPE_SCALE_UP", "CHANGE_SHAPE_SCALE_DOWN"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def metric(self):
        """
        **[Required]** Gets the metric of this AutoScalePolicyRule.

        :return: The metric of this AutoScalePolicyRule.
        :rtype: oci.bds.models.AutoScalePolicyMetricRule
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this AutoScalePolicyRule.

        :param metric: The metric of this AutoScalePolicyRule.
        :type: oci.bds.models.AutoScalePolicyMetricRule
        """
        self._metric = metric

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
