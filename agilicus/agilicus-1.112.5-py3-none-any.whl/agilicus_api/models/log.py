# coding: utf-8

"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.05.14
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class Log(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'log': 'str',
        'stream': 'str',
        'timestamp': 'str',
        'app': 'str',
        'org_id': 'str',
        'sub_org_id': 'str',
        'env': 'str'
    }

    attribute_map = {
        'log': 'log',
        'stream': 'stream',
        'timestamp': 'timestamp',
        'app': 'app',
        'org_id': 'org_id',
        'sub_org_id': 'sub_org_id',
        'env': 'env'
    }

    def __init__(self, log=None, stream=None, timestamp=None, app=None, org_id=None, sub_org_id=None, env=None, local_vars_configuration=None):  # noqa: E501
        """Log - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._log = None
        self._stream = None
        self._timestamp = None
        self._app = None
        self._org_id = None
        self._sub_org_id = None
        self._env = None
        self.discriminator = None

        if log is not None:
            self.log = log
        if stream is not None:
            self.stream = stream
        if timestamp is not None:
            self.timestamp = timestamp
        if app is not None:
            self.app = app
        if org_id is not None:
            self.org_id = org_id
        if sub_org_id is not None:
            self.sub_org_id = sub_org_id
        if env is not None:
            self.env = env

    @property
    def log(self):
        """Gets the log of this Log.  # noqa: E501

        log  # noqa: E501

        :return: The log of this Log.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this Log.

        log  # noqa: E501

        :param log: The log of this Log.  # noqa: E501
        :type: str
        """

        self._log = log

    @property
    def stream(self):
        """Gets the stream of this Log.  # noqa: E501

        log stream  # noqa: E501

        :return: The stream of this Log.  # noqa: E501
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this Log.

        log stream  # noqa: E501

        :param stream: The stream of this Log.  # noqa: E501
        :type: str
        """

        self._stream = stream

    @property
    def timestamp(self):
        """Gets the timestamp of this Log.  # noqa: E501

        timestamp of log  # noqa: E501

        :return: The timestamp of this Log.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Log.

        timestamp of log  # noqa: E501

        :param timestamp: The timestamp of this Log.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def app(self):
        """Gets the app of this Log.  # noqa: E501

        name of application associated with log  # noqa: E501

        :return: The app of this Log.  # noqa: E501
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this Log.

        name of application associated with log  # noqa: E501

        :param app: The app of this Log.  # noqa: E501
        :type: str
        """

        self._app = app

    @property
    def org_id(self):
        """Gets the org_id of this Log.  # noqa: E501

        unique shortuuid for the  organisation  # noqa: E501

        :return: The org_id of this Log.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Log.

        unique shortuuid for the  organisation  # noqa: E501

        :param org_id: The org_id of this Log.  # noqa: E501
        :type: str
        """

        self._org_id = org_id

    @property
    def sub_org_id(self):
        """Gets the sub_org_id of this Log.  # noqa: E501

        unique shortuuid for the sub-organisation  # noqa: E501

        :return: The sub_org_id of this Log.  # noqa: E501
        :rtype: str
        """
        return self._sub_org_id

    @sub_org_id.setter
    def sub_org_id(self, sub_org_id):
        """Sets the sub_org_id of this Log.

        unique shortuuid for the sub-organisation  # noqa: E501

        :param sub_org_id: The sub_org_id of this Log.  # noqa: E501
        :type: str
        """

        self._sub_org_id = sub_org_id

    @property
    def env(self):
        """Gets the env of this Log.  # noqa: E501

        environment that app is running in  # noqa: E501

        :return: The env of this Log.  # noqa: E501
        :rtype: str
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this Log.

        environment that app is running in  # noqa: E501

        :param env: The env of this Log.  # noqa: E501
        :type: str
        """

        self._env = env

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Log):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Log):
            return True

        return self.to_dict() != other.to_dict()
