# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyPriorityAnswerData(object):
    """
    SteeringPolicyPriorityAnswerData model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyPriorityAnswerData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param answer_condition:
            The value to assign to the answer_condition property of this SteeringPolicyPriorityAnswerData.
        :type answer_condition: str

        :param value:
            The value to assign to the value property of this SteeringPolicyPriorityAnswerData.
        :type value: int

        """
        self.swagger_types = {
            'answer_condition': 'str',
            'value': 'int'
        }

        self.attribute_map = {
            'answer_condition': 'answerCondition',
            'value': 'value'
        }

        self._answer_condition = None
        self._value = None

    @property
    def answer_condition(self):
        """
        Gets the answer_condition of this SteeringPolicyPriorityAnswerData.
        An expression that is used to select a set of answers that match a condition. For example, answers with matching pool properties.


        :return: The answer_condition of this SteeringPolicyPriorityAnswerData.
        :rtype: str
        """
        return self._answer_condition

    @answer_condition.setter
    def answer_condition(self, answer_condition):
        """
        Sets the answer_condition of this SteeringPolicyPriorityAnswerData.
        An expression that is used to select a set of answers that match a condition. For example, answers with matching pool properties.


        :param answer_condition: The answer_condition of this SteeringPolicyPriorityAnswerData.
        :type: str
        """
        self._answer_condition = answer_condition

    @property
    def value(self):
        """
        **[Required]** Gets the value of this SteeringPolicyPriorityAnswerData.
        The rank assigned to the set of answers that match the expression in `answerCondition`.
        Answers with the lowest values move to the beginning of the list without changing the
        relative order of those with the same value. Answers can be given a value between `0` and `255`.


        :return: The value of this SteeringPolicyPriorityAnswerData.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SteeringPolicyPriorityAnswerData.
        The rank assigned to the set of answers that match the expression in `answerCondition`.
        Answers with the lowest values move to the beginning of the list without changing the
        relative order of those with the same value. Answers can be given a value between `0` and `255`.


        :param value: The value of this SteeringPolicyPriorityAnswerData.
        :type: int
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
