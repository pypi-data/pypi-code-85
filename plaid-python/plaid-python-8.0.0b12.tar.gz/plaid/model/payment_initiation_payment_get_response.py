"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from plaid.model.external_payment_refund_details import ExternalPaymentRefundDetails
    from plaid.model.external_payment_schedule_get import ExternalPaymentScheduleGet
    from plaid.model.nullable_recipient_bacs import NullableRecipientBACS
    from plaid.model.payment_amount import PaymentAmount
    from plaid.model.payment_initiation_payment import PaymentInitiationPayment
    from plaid.model.payment_initiation_recipient_get_response_all_of import PaymentInitiationRecipientGetResponseAllOf
    globals()['ExternalPaymentRefundDetails'] = ExternalPaymentRefundDetails
    globals()['ExternalPaymentScheduleGet'] = ExternalPaymentScheduleGet
    globals()['NullableRecipientBACS'] = NullableRecipientBACS
    globals()['PaymentAmount'] = PaymentAmount
    globals()['PaymentInitiationPayment'] = PaymentInitiationPayment
    globals()['PaymentInitiationRecipientGetResponseAllOf'] = PaymentInitiationRecipientGetResponseAllOf


class PaymentInitiationPaymentGetResponse(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('status',): {
            'INPUT_NEEDED': "PAYMENT_STATUS_INPUT_NEEDED",
            'PROCESSING': "PAYMENT_STATUS_PROCESSING",
            'INITIATED': "PAYMENT_STATUS_INITIATED",
            'COMPLETED': "PAYMENT_STATUS_COMPLETED",
            'INSUFFICIENT_FUNDS': "PAYMENT_STATUS_INSUFFICIENT_FUNDS",
            'FAILED': "PAYMENT_STATUS_FAILED",
            'BLOCKED': "PAYMENT_STATUS_BLOCKED",
            'UNKNOWN': "PAYMENT_STATUS_UNKNOWN",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'payment_id': (str,),  # noqa: E501
            'amount': (PaymentAmount,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'recipient_id': (str,),  # noqa: E501
            'reference': (str,),  # noqa: E501
            'last_status_update': (datetime,),  # noqa: E501
            'bacs': (NullableRecipientBACS,),  # noqa: E501
            'iban': (str, none_type,),  # noqa: E501
            'request_id': (str,),  # noqa: E501
            'adjusted_reference': (str, none_type,),  # noqa: E501
            'schedule': (ExternalPaymentScheduleGet,),  # noqa: E501
            'refund_details': (ExternalPaymentRefundDetails,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'payment_id': 'payment_id',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'status': 'status',  # noqa: E501
        'recipient_id': 'recipient_id',  # noqa: E501
        'reference': 'reference',  # noqa: E501
        'last_status_update': 'last_status_update',  # noqa: E501
        'bacs': 'bacs',  # noqa: E501
        'iban': 'iban',  # noqa: E501
        'request_id': 'request_id',  # noqa: E501
        'adjusted_reference': 'adjusted_reference',  # noqa: E501
        'schedule': 'schedule',  # noqa: E501
        'refund_details': 'refund_details',  # noqa: E501
    }

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, payment_id, amount, status, recipient_id, reference, last_status_update, bacs, iban, request_id, *args, **kwargs):  # noqa: E501
        """PaymentInitiationPaymentGetResponse - a model defined in OpenAPI

        Args:
            payment_id (str): The ID of the payment. Like all Plaid identifiers, the `payment_id` is case sensitive.
            amount (PaymentAmount):
            status (str): The status of the payment.  `PAYMENT_STATUS_INPUT_NEEDED`: This is the initial state of all payments. It indicates that the payment is waiting on user input to continue processing. A payment may re-enter this state later on if further input is needed.  `PAYMENT_STATUS_PROCESSING`: The payment is currently being processed. The payment will automatically exit this state when processing is complete.  `PAYMENT_STATUS_INITIATED`: The payment has been successfully initiated and is considered complete.  `PAYMENT_STATUS_COMPLETED`: Indicates that the standing order has been successfully established. This state is only used for standing orders.  `PAYMENT_STATUS_INSUFFICIENT_FUNDS`: The payment has failed due to insufficient funds.  `PAYMENT_STATUS_FAILED`: The payment has failed to be initiated. This error is retryable once the root cause is resolved.  `PAYMENT_STATUS_BLOCKED`: The payment has been blocked. This is a retryable error.  `PAYMENT_STATUS_UNKNOWN`: The payment status is unknown.
            recipient_id (str): The ID of the recipient
            reference (str): A reference for the payment.
            last_status_update (datetime): The date and time of the last time the `status` was updated, in IS0 8601 format
            bacs (NullableRecipientBACS):
            iban (str, none_type):
            request_id (str): A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            adjusted_reference (str, none_type): The value of the reference sent to the bank after adjustment to pass bank validation rules.. [optional]  # noqa: E501
            schedule (ExternalPaymentScheduleGet): [optional]  # noqa: E501
            refund_details (ExternalPaymentRefundDetails): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        required_args = {
            'payment_id': payment_id,
            'amount': amount,
            'status': status,
            'recipient_id': recipient_id,
            'reference': reference,
            'last_status_update': last_status_update,
            'bacs': bacs,
            'iban': iban,
            'request_id': request_id,
        }
        model_args = {}
        model_args.update(required_args)
        model_args.update(kwargs)
        composed_info = validate_get_composed_info(
            constant_args, model_args, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        unused_args = composed_info[3]

        for var_name, var_value in required_args.items():
            setattr(self, var_name, var_value)
        for var_name, var_value in kwargs.items():
            if var_name in unused_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        not self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              PaymentInitiationPayment,
              PaymentInitiationRecipientGetResponseAllOf,
          ],
          'oneOf': [
          ],
        }
