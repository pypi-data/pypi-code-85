import os
from functools import wraps

import numpy as np

from . import lib


class UnsupportedGEOSOperation(ImportError):
    pass


class requires_geos:
    def __init__(self, version):
        if version.count(".") != 2:
            raise ValueError("Version must be <major>.<minor>.<patch> format")
        self.version = tuple(int(x) for x in version.split("."))

    def __call__(self, func):
        is_compatible = lib.geos_version >= self.version
        is_doc_build = os.environ.get("SPHINX_DOC_BUILD") == "1"  # set in docs/conf.py
        if is_compatible and not is_doc_build:
            return func  # return directly, do not change the docstring

        msg = "'{}' requires at least GEOS {}.{}.{}.".format(
            func.__name__, *self.version
        )
        if is_compatible:

            @wraps(func)
            def wrapped(*args, **kwargs):
                return func(*args, **kwargs)

        else:

            @wraps(func)
            def wrapped(*args, **kwargs):
                raise UnsupportedGEOSOperation(msg)

        if wrapped.__doc__:
            wrapped.__doc__ = wrapped.__doc__.replace(
                "\n\n", "\n\n    .. note:: {}\n\n".format(msg), 1
            )

        return wrapped


def multithreading_enabled(func):
    """Prepare multithreading by setting the writable flags of object type
    ndarrays to False.

    NB: multithreading also requires the GIL to be released, which is done in
    the C extension (ufuncs.c)."""

    @wraps(func)
    def wrapped(*args, **kwargs):
        array_args = [
            arg for arg in args if isinstance(arg, np.ndarray) and arg.dtype == object
        ] + [
            arg
            for name, arg in kwargs.items()
            if name not in {"where", "out"}
            and isinstance(arg, np.ndarray)
            and arg.dtype == object
        ]
        old_flags = [arr.flags.writeable for arr in array_args]
        try:
            for arr in array_args:
                arr.flags.writeable = False
            return func(*args, **kwargs)
        finally:
            for arr, old_flag in zip(array_args, old_flags):
                arr.flags.writeable = old_flag

    return wrapped
