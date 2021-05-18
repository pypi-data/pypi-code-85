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
    from plaid.model.location import Location
    from plaid.model.payment_meta import PaymentMeta
    from plaid.model.transaction_code import TransactionCode
    globals()['Location'] = Location
    globals()['PaymentMeta'] = PaymentMeta
    globals()['TransactionCode'] = TransactionCode


class Transaction(ModelNormal):
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
        ('transaction_type',): {
            'DIGITAL': "digital",
            'PLACE': "place",
            'SPECIAL': "special",
            'UNRESOLVED': "unresolved",
        },
        ('payment_channel',): {
            'ONLINE': "online",
            'IN_STORE': "in store",
            'OTHER': "other",
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
            'transaction_id': (str,),  # noqa: E501
            'pending': (bool,),  # noqa: E501
            'date': (str,),  # noqa: E501
            'amount': (float,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'transaction_type': (str,),  # noqa: E501
            'account_owner': (str, none_type,),  # noqa: E501
            'pending_transaction_id': (str, none_type,),  # noqa: E501
            'payment_channel': (str,),  # noqa: E501
            'payment_meta': (PaymentMeta,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'merchant_name': (str, none_type,),  # noqa: E501
            'location': (Location,),  # noqa: E501
            'authorized_date': (str, none_type,),  # noqa: E501
            'authorized_datetime': (str, none_type,),  # noqa: E501
            'datetime': (str, none_type,),  # noqa: E501
            'category_id': (str,),  # noqa: E501
            'category': ([str], none_type,),  # noqa: E501
            'unofficial_currency_code': (str, none_type,),  # noqa: E501
            'iso_currency_code': (str, none_type,),  # noqa: E501
            'transaction_code': (TransactionCode,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'transaction_id': 'transaction_id',  # noqa: E501
        'pending': 'pending',  # noqa: E501
        'date': 'date',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'account_id': 'account_id',  # noqa: E501
        'transaction_type': 'transaction_type',  # noqa: E501
        'account_owner': 'account_owner',  # noqa: E501
        'pending_transaction_id': 'pending_transaction_id',  # noqa: E501
        'payment_channel': 'payment_channel',  # noqa: E501
        'payment_meta': 'payment_meta',  # noqa: E501
        'name': 'name',  # noqa: E501
        'merchant_name': 'merchant_name',  # noqa: E501
        'location': 'location',  # noqa: E501
        'authorized_date': 'authorized_date',  # noqa: E501
        'authorized_datetime': 'authorized_datetime',  # noqa: E501
        'datetime': 'datetime',  # noqa: E501
        'category_id': 'category_id',  # noqa: E501
        'category': 'category',  # noqa: E501
        'unofficial_currency_code': 'unofficial_currency_code',  # noqa: E501
        'iso_currency_code': 'iso_currency_code',  # noqa: E501
        'transaction_code': 'transaction_code',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, transaction_id, pending, date, amount, account_id, *args, **kwargs):  # noqa: E501
        """Transaction - a model defined in OpenAPI

        Args:
            transaction_id (str): The unique ID of the transaction. Like all Plaid identifiers, the `transaction_id` is case sensitive.
            pending (bool): When `true`, identifies the transaction as pending or unsettled. Pending transaction details (name, type, amount, category ID) may change before they are settled.
            date (str): For pending transactions, the date that the transaction occurred; for posted transactions, the date that the transaction posted. Both dates are returned in an ISO 8601 format ( `YYYY-MM-DD` ).
            amount (float): The settled value of the transaction, denominated in the account's currency, as stated in `iso_currency_code` or `unofficial_currency_code`. Positive values when money moves out of the account; negative values when money moves in. For example, debit card purchases are positive; credit card payments, direct deposits, and refunds are negative.
            account_id (str): The ID of the account in which this transaction occurred.

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
            transaction_type (str): Please use the `payment_channel` field, `transaction_type` will be deprecated in the future.  `digital:` transactions that took place online.  `place:` transactions that were made at a physical location.  `special:` transactions that relate to banks, e.g. fees or deposits.  `unresolved:` transactions that do not fit into the other three types. . [optional]  # noqa: E501
            account_owner (str, none_type): The name of the account owner. This field is not typically populated and only relevant when dealing with sub-accounts.. [optional]  # noqa: E501
            pending_transaction_id (str, none_type): The ID of a posted transaction's associated pending transaction, where applicable.. [optional]  # noqa: E501
            payment_channel (str): The channel used to make a payment. `online:` transactions that took place online.  `in store:` transactions that were made at a physical location.  `other:` transactions that relate to banks, e.g. fees or deposits.  This field replaces the `transaction_type` field. . [optional]  # noqa: E501
            payment_meta (PaymentMeta): [optional]  # noqa: E501
            name (str): The merchant name or transaction description.  If the `transactions` object was returned by a Transactions endpoint such as `/transactions/get`, this field will always appear. If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.. [optional]  # noqa: E501
            merchant_name (str, none_type): The merchant name, as extracted by Plaid from the `name` field.. [optional]  # noqa: E501
            location (Location): [optional]  # noqa: E501
            authorized_date (str, none_type): The date that the transaction was authorized. Dates are returned in an ISO 8601 format ( `YYYY-MM-DD` ).. [optional]  # noqa: E501
            authorized_datetime (str, none_type): Date and time when a transaction was authorized in ISO 8601 format ( `YYYY-MM-DDTHH:mm:ssZ` ).  This field is only populated for UK institutions. For institutions in other countries, will be `null`.. [optional]  # noqa: E501
            datetime (str, none_type): Date and time when a transaction was posted in ISO 8601 format ( `YYYY-MM-DDTHH:mm:ssZ` ).  This field is only populated for UK institutions. For institutions in other countries, will be `null`.. [optional]  # noqa: E501
            category_id (str): The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview).  If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.. [optional]  # noqa: E501
            category ([str], none_type): A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/#category-overview).  If the `transactions` object was returned by an Assets endpoint such as `/asset_report/get/` or `/asset_report/pdf/get`, this field will only appear in an Asset Report with Insights.. [optional]  # noqa: E501
            unofficial_currency_code (str, none_type): The unofficial currency code associated with the transaction. Always `null` if `iso_currency_code` is non-`null`. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries.  See the [currency code schema](/docs/api/accounts#currency-code-schema) for a full listing of supported `iso_currency_code`s.. [optional]  # noqa: E501
            iso_currency_code (str, none_type): The ISO-4217 currency code of the transaction. Always `null` if `unofficial_currency_code` is non-null.. [optional]  # noqa: E501
            transaction_code (TransactionCode): [optional]  # noqa: E501
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

        self.transaction_id = transaction_id
        self.pending = pending
        self.date = date
        self.amount = amount
        self.account_id = account_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
