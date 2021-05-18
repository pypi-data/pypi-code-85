# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMultipartUploadDetails(object):
    """
    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized,
    talk to an administrator. If you are an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the storage_tier property of a CreateMultipartUploadDetails.
    #: This constant has a value of "Standard"
    STORAGE_TIER_STANDARD = "Standard"

    #: A constant which can be used with the storage_tier property of a CreateMultipartUploadDetails.
    #: This constant has a value of "InfrequentAccess"
    STORAGE_TIER_INFREQUENT_ACCESS = "InfrequentAccess"

    #: A constant which can be used with the storage_tier property of a CreateMultipartUploadDetails.
    #: This constant has a value of "Archive"
    STORAGE_TIER_ARCHIVE = "Archive"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMultipartUploadDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param object:
            The value to assign to the object property of this CreateMultipartUploadDetails.
        :type object: str

        :param content_type:
            The value to assign to the content_type property of this CreateMultipartUploadDetails.
        :type content_type: str

        :param content_language:
            The value to assign to the content_language property of this CreateMultipartUploadDetails.
        :type content_language: str

        :param content_encoding:
            The value to assign to the content_encoding property of this CreateMultipartUploadDetails.
        :type content_encoding: str

        :param content_disposition:
            The value to assign to the content_disposition property of this CreateMultipartUploadDetails.
        :type content_disposition: str

        :param cache_control:
            The value to assign to the cache_control property of this CreateMultipartUploadDetails.
        :type cache_control: str

        :param storage_tier:
            The value to assign to the storage_tier property of this CreateMultipartUploadDetails.
            Allowed values for this property are: "Standard", "InfrequentAccess", "Archive"
        :type storage_tier: str

        :param metadata:
            The value to assign to the metadata property of this CreateMultipartUploadDetails.
        :type metadata: dict(str, str)

        """
        self.swagger_types = {
            'object': 'str',
            'content_type': 'str',
            'content_language': 'str',
            'content_encoding': 'str',
            'content_disposition': 'str',
            'cache_control': 'str',
            'storage_tier': 'str',
            'metadata': 'dict(str, str)'
        }

        self.attribute_map = {
            'object': 'object',
            'content_type': 'contentType',
            'content_language': 'contentLanguage',
            'content_encoding': 'contentEncoding',
            'content_disposition': 'contentDisposition',
            'cache_control': 'cacheControl',
            'storage_tier': 'storageTier',
            'metadata': 'metadata'
        }

        self._object = None
        self._content_type = None
        self._content_language = None
        self._content_encoding = None
        self._content_disposition = None
        self._cache_control = None
        self._storage_tier = None
        self._metadata = None

    @property
    def object(self):
        """
        **[Required]** Gets the object of this CreateMultipartUploadDetails.
        The name of the object to which this multi-part upload is targeted. Avoid entering confidential information.
        Example: test/object1.log


        :return: The object of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CreateMultipartUploadDetails.
        The name of the object to which this multi-part upload is targeted. Avoid entering confidential information.
        Example: test/object1.log


        :param object: The object of this CreateMultipartUploadDetails.
        :type: str
        """
        self._object = object

    @property
    def content_type(self):
        """
        Gets the content_type of this CreateMultipartUploadDetails.
        The optional Content-Type header that defines the standard MIME type format of the object to upload.
        Specifying values for this header has no effect on Object Storage behavior. Programs that read the object
        determine what to do based on the value provided. For example, you could use this header to identify and
        perform special operations on text only objects.


        :return: The content_type of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this CreateMultipartUploadDetails.
        The optional Content-Type header that defines the standard MIME type format of the object to upload.
        Specifying values for this header has no effect on Object Storage behavior. Programs that read the object
        determine what to do based on the value provided. For example, you could use this header to identify and
        perform special operations on text only objects.


        :param content_type: The content_type of this CreateMultipartUploadDetails.
        :type: str
        """
        self._content_type = content_type

    @property
    def content_language(self):
        """
        Gets the content_language of this CreateMultipartUploadDetails.
        The optional Content-Language header that defines the content language of the object to upload. Specifying
        values for this header has no effect on Object Storage behavior. Programs that read the object determine what
        to do based on the value provided. For example, you could use this header to identify and differentiate objects
        based on a particular language.


        :return: The content_language of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._content_language

    @content_language.setter
    def content_language(self, content_language):
        """
        Sets the content_language of this CreateMultipartUploadDetails.
        The optional Content-Language header that defines the content language of the object to upload. Specifying
        values for this header has no effect on Object Storage behavior. Programs that read the object determine what
        to do based on the value provided. For example, you could use this header to identify and differentiate objects
        based on a particular language.


        :param content_language: The content_language of this CreateMultipartUploadDetails.
        :type: str
        """
        self._content_language = content_language

    @property
    def content_encoding(self):
        """
        Gets the content_encoding of this CreateMultipartUploadDetails.
        The optional Content-Encoding header that defines the content encodings that were applied to the object to
        upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the
        object determine what to do based on the value provided. For example, you could use this header to determine
        what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of
        the object.


        :return: The content_encoding of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._content_encoding

    @content_encoding.setter
    def content_encoding(self, content_encoding):
        """
        Sets the content_encoding of this CreateMultipartUploadDetails.
        The optional Content-Encoding header that defines the content encodings that were applied to the object to
        upload. Specifying values for this header has no effect on Object Storage behavior. Programs that read the
        object determine what to do based on the value provided. For example, you could use this header to determine
        what decoding mechanisms need to be applied to obtain the media-type specified by the Content-Type header of
        the object.


        :param content_encoding: The content_encoding of this CreateMultipartUploadDetails.
        :type: str
        """
        self._content_encoding = content_encoding

    @property
    def content_disposition(self):
        """
        Gets the content_disposition of this CreateMultipartUploadDetails.
        The optional Content-Disposition header that defines presentational information for the object to be
        returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object
        Storage behavior. Programs that read the object determine what to do based on the value provided.
        For example, you could use this header to let users download objects with custom filenames in a browser.


        :return: The content_disposition of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._content_disposition

    @content_disposition.setter
    def content_disposition(self, content_disposition):
        """
        Sets the content_disposition of this CreateMultipartUploadDetails.
        The optional Content-Disposition header that defines presentational information for the object to be
        returned in GetObject and HeadObject responses. Specifying values for this header has no effect on Object
        Storage behavior. Programs that read the object determine what to do based on the value provided.
        For example, you could use this header to let users download objects with custom filenames in a browser.


        :param content_disposition: The content_disposition of this CreateMultipartUploadDetails.
        :type: str
        """
        self._content_disposition = content_disposition

    @property
    def cache_control(self):
        """
        Gets the cache_control of this CreateMultipartUploadDetails.
        The optional Cache-Control header that defines the caching behavior value to be returned in GetObject and
        HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs
        that read the object determine what to do based on the value provided.
        For example, you could use this header to identify objects that require caching restrictions.


        :return: The cache_control of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._cache_control

    @cache_control.setter
    def cache_control(self, cache_control):
        """
        Sets the cache_control of this CreateMultipartUploadDetails.
        The optional Cache-Control header that defines the caching behavior value to be returned in GetObject and
        HeadObject responses. Specifying values for this header has no effect on Object Storage behavior. Programs
        that read the object determine what to do based on the value provided.
        For example, you could use this header to identify objects that require caching restrictions.


        :param cache_control: The cache_control of this CreateMultipartUploadDetails.
        :type: str
        """
        self._cache_control = cache_control

    @property
    def storage_tier(self):
        """
        Gets the storage_tier of this CreateMultipartUploadDetails.
        The storage tier that the object should be stored in. If not specified, the object will be stored in
        the same storage tier as the bucket.

        Allowed values for this property are: "Standard", "InfrequentAccess", "Archive"


        :return: The storage_tier of this CreateMultipartUploadDetails.
        :rtype: str
        """
        return self._storage_tier

    @storage_tier.setter
    def storage_tier(self, storage_tier):
        """
        Sets the storage_tier of this CreateMultipartUploadDetails.
        The storage tier that the object should be stored in. If not specified, the object will be stored in
        the same storage tier as the bucket.


        :param storage_tier: The storage_tier of this CreateMultipartUploadDetails.
        :type: str
        """
        allowed_values = ["Standard", "InfrequentAccess", "Archive"]
        if not value_allowed_none_or_none_sentinel(storage_tier, allowed_values):
            raise ValueError(
                "Invalid value for `storage_tier`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._storage_tier = storage_tier

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateMultipartUploadDetails.
        Arbitrary string keys and values for the user-defined metadata for the object.
        Keys must be in \"opc-meta-*\" format. Avoid entering confidential information.


        :return: The metadata of this CreateMultipartUploadDetails.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateMultipartUploadDetails.
        Arbitrary string keys and values for the user-defined metadata for the object.
        Keys must be in \"opc-meta-*\" format. Avoid entering confidential information.


        :param metadata: The metadata of this CreateMultipartUploadDetails.
        :type: dict(str, str)
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
