from __future__ import absolute_import, division, print_function

from circle import api_requestor, util
from circle.circle_object import CircleObject


def nested_resource_class_methods(
    resource, nested_object, path=None, operations=None, resource_plural=None
):
    assert issubclass(nested_object, CircleObject), (
        "nested_object, %s, must inherit from CircleObject" % nested_object
    )
    if resource_plural is None:
        resource_plural = "%ss" % resource
    if path is None:
        path = "%s" % resource
    if operations is None:
        raise ValueError("operations list required")

    def wrapper(cls):
        def nested_resource_url(cls, id, nested_id=None):
            url = "%s/%s/%s" % (
                cls.class_url(),
                id,
                path,
            )
            if nested_id is not None:
                url += "/%s" % nested_id
            return url

        resource_url_method = "%ss_url" % resource
        setattr(cls, resource_url_method, classmethod(nested_resource_url))

        def nested_resource_request(
            cls,
            method,
            url,
            api_key=None,
            **params,
        ):
            requestor = api_requestor.APIRequestor(
                api_key,
            )
            # TODO: Come back to this
            # headers = util.populate_headers(idempotency_key)
            idempotency_key = params.get("idempotencyKey", None)
            if idempotency_key:
                params.update({"idempotencyKey": idempotency_key})
            response, api_key = requestor.request(method, url, params)
            return util.convert_to_circle_object(
                response, api_key, klass_name=nested_object.OBJECT_NAME
            )

        resource_request_method = "%ss_request" % resource
        setattr(cls, resource_request_method, classmethod(nested_resource_request))

        for operation in operations:
            if operation == "create":

                def create_nested_resource(cls, id, **params):
                    url = getattr(cls, resource_url_method)(id)
                    return getattr(cls, resource_request_method)("post", url, **params)

                create_method = "create_%s" % resource
                setattr(cls, create_method, classmethod(create_nested_resource))

            elif operation == "retrieve":

                def retrieve_nested_resource(
                    cls,
                    id,
                    nested_id=None,  # Nested ID is not required for all retrievals. E.g. retrieving wire instructions has no nested ID.
                    **params,
                ):
                    url = getattr(cls, resource_url_method)(id, nested_id)
                    return getattr(cls, resource_request_method)("get", url, **params)

                retrieve_method = "retrieve_%s" % resource
                setattr(cls, retrieve_method, classmethod(retrieve_nested_resource))

            elif operation == "update":

                def modify_nested_resource(cls, id, nested_id, **params):
                    url = getattr(cls, resource_url_method)(id, nested_id)
                    return getattr(cls, resource_request_method)("post", url, **params)

                modify_method = "modify_%s" % resource
                setattr(cls, modify_method, classmethod(modify_nested_resource))

            elif operation == "delete":

                def delete_nested_resource(cls, id, nested_id, **params):
                    url = getattr(cls, resource_url_method)(id, nested_id)
                    return getattr(cls, resource_request_method)(
                        "delete", url, **params
                    )

                delete_method = "delete_%s" % resource
                setattr(cls, delete_method, classmethod(delete_nested_resource))

            elif operation == "list":

                def list_nested_resources(cls, id, **params):
                    url = getattr(cls, resource_url_method)(id)
                    return getattr(cls, resource_request_method)("get", url, **params)

                list_method = "list_%s" % resource_plural
                setattr(cls, list_method, classmethod(list_nested_resources))

            else:
                raise ValueError("Unknown operation: %s" % operation)

        return cls

    return wrapper
