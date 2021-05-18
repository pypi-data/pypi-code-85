from __future__ import annotations

import asyncio
import base64
import contextlib
import copy
import json
import numbers
import os
import pathlib
import platform
import sys
import threading
import time
import uuid
import warnings
import weakref
from contextlib import contextmanager
from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
    Generator,
    Generic,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
    cast,
    overload,
)

import aiohttp
import dask
import dask.distributed
import distributed
import rich
import toolz
import yaml
from distributed.comm import parse_address
from distributed.utils import Log, Logs, LoopRunner, sync, thread_state
from rich.console import Console
from rich.table import Table
from tornado.ioloop import IOLoop
from typing_extensions import Literal, Protocol

from .compatibility import COILED_VERSION, DISTRIBUTED_VERSION, PY_VERSION
from .utils import (
    GatewaySecurity,
    Spinner,
    experimental,
    handle_api_exception,
    handle_credentials,
    parse_identifier,
    rich_console,
)

console = Console()


def get_uuid():
    return str(uuid.uuid4())[:10]


def delete_docstring(func):
    delete_doc = """ Delete a {kind}

Parameters
---------
name
    Name of {kind} to delete.
"""
    func_name = func.__name__
    kind = " ".join(
        func_name.split("_")[1:]
    )  # delete_software_environments -> software environments
    func.__doc__ = delete_doc.format(kind=kind)
    return func


def list_docstring(func):

    list_doc = """ List {kind}s

Parameters
---------
account
    Name of the Coiled account to list {kind}s.
    If not provided, will use the ``coiled.account`` configuration
    value.

Returns
-------
:
    Dictionary with information about each {kind} in the
    specified account. Keys in the dictionary are names of {kind}s,
    while the values contain information about the corresponding {kind}.
"""
    func_name = func.__name__
    kind = " ".join(func_name.split("_")[1:])
    kind = kind[:-1]  # drop trailing "s"
    func.__doc__ = list_doc.format(kind=kind)
    return func


# This lock helps avoid a race condition between cluster creation in the
# in process backend, which temporarily modify coiled's dask config values,
# and the creation of new Cloud objects, with load those same config values.
# This works, but is not ideal.
_cluster_creation_lock = threading.RLock()


# Generic TypeVar for return value from sync/async function.
_T = TypeVar("_T")


# A generic that can only be True/False, allowing us to type async/sync
# versions of coiled objects.
Async = Literal[True]
Sync = Literal[False]
IsAsynchronous = TypeVar("IsAsynchronous", Async, Sync, covariant=True)


# Short of writing type stubs for distributed or typing the underlying package,
# this is a useful cast.
class _SyncProtocol(Protocol):
    def __call__(
        self,
        loop: IOLoop,
        func: Callable[..., Awaitable[_T]],
        *args: Any,
        callback_timeout: numbers.Number,
        **kwargs: Any,
    ) -> _T:
        ...


sync = cast(_SyncProtocol, sync)


class Cloud(Generic[IsAsynchronous]):
    """Connect to Coiled

    Parameters
    ----------
    user
        Username for Coiled account. If not specified, will check the
        ``coiled.user`` configuration value.
    token
        Token for Coiled account. If not specified, will check the
        ``coiled.token`` configuration value.
    server
        Server to connect to. If not specified, will check the
        ``coiled.server`` configuration value.
    account
        The coiled account to use. If not specified,
        will check the ``coiled.account`` configuration value.
    region
        Name of the AWS region to use (e.g. "us-east-2").
        If not specified, will check the ``coiled.aws.region``
        configuration value.
    asynchronous
        Set to True if using this Cloud within ``async``/``await`` functions or
        within Tornado ``gen.coroutines``. Otherwise this should remain
        ``False`` for normal use. Default is ``False``.
    loop
        If given, this event loop will be re-used, otherwise an appropriate one
        will be looked up or created.
    default_cluster_timeout
        Default timeout in seconds to wait for cluster startup before raising ``TimeoutError``.
        Pass ``None`` to wait forever, otherwise the default is 20 minutes.
    """

    _recent_sync: list[weakref.ReferenceType[Cloud[Sync]]] = list()
    _recent_async: list[weakref.ReferenceType[Cloud[Async]]] = list()

    @overload
    def __init__(
        self: Cloud[Sync],
        user: str = None,
        token: str = None,
        server: str = None,
        account: str = None,
        region: str = None,
        asynchronous: Sync = False,
        loop: IOLoop = None,
        default_cluster_timeout: int = 20 * 60,
    ):
        ...

    @overload
    def __init__(
        self: Cloud[Async],
        user: str = None,
        token: str = None,
        server: str = None,
        account: str = None,
        region: str = None,
        asynchronous: Async = True,
        loop: IOLoop = None,
        default_cluster_timeout: int = 20 * 60,
    ):
        ...

    @overload
    def __init__(
        self,
        user: str = None,
        token: str = None,
        server: str = None,
        account: str = None,
        region: str = None,
        asynchronous: bool = False,
        loop: IOLoop = None,
        default_cluster_timeout: int = 20 * 60,
    ):
        ...

    def __init__(
        self,
        user: str = None,
        token: str = None,
        server: str = None,
        account: str = None,
        region: str = None,
        asynchronous: bool = False,
        loop: IOLoop = None,
        default_cluster_timeout: int = 20 * 60,
    ):
        with _cluster_creation_lock:
            self.user = user or dask.config.get("coiled.user")
            self.token = token or dask.config.get("coiled.token")
            self.server = server or dask.config.get("coiled.server")
            if "://" not in self.server:
                self.server = "http://" + self.server
            self.server = self.server.rstrip("/")
            self._default_account = account or dask.config.get("coiled.account")
            self._default_backend_options = (
                dask.config.get("coiled.backend-options", None) or {}
            )
        self.session: Optional[aiohttp.ClientSession] = None
        self.status = "init"
        self.cluster_id: Optional[int] = None
        self._asynchronous = asynchronous
        self._loop_runner = LoopRunner(loop=loop, asynchronous=asynchronous)
        self._loop_runner.start()
        self.default_cluster_timeout = default_cluster_timeout

        if asynchronous:
            Cloud._recent_async.append(weakref.ref(cast(Cloud[Async], self)))
        else:
            Cloud._recent_sync.append(weakref.ref(cast(Cloud[Sync], self)))

        if not self.asynchronous:
            self._sync(self._start)

    def __repr__(self):
        return f"<Cloud: {self.user}@{self.server} - {self.status}>"

    def _repr_html_(self):
        text = (
            '<h3 style="text-align: left;">Cloud</h3>\n'
            '<ul style="text-align: left; list-style: none; margin: 0; padding: 0;">\n'
            f"  <li><b>User: </b>{self.user}</li>\n"
            f"  <li><b>Server: </b>{self.server}</li>\n"
            f"  <li><b>Account: </b>{self.default_account}</li>\n"
        )

        return text

    @property
    def loop(self):
        return self._loop_runner.loop

    @overload
    @classmethod
    def current(cls, asynchronous: Sync) -> Cloud[Sync]:
        ...

    @overload
    @classmethod
    def current(cls, asynchronous: Async) -> Cloud[Async]:
        ...

    @overload
    @classmethod
    def current(cls, asynchronous: bool) -> Cloud:
        ...

    @classmethod
    def current(cls, asynchronous: bool) -> Cloud:
        recent: list[weakref.ReferenceType[Cloud]]
        if asynchronous:
            recent = cls._recent_async
        else:
            recent = cls._recent_sync
        try:
            cloud = recent[-1]()
            while cloud is None or cloud.status != "running":
                recent.pop()
                cloud = recent[-1]()
        except IndexError:
            try:
                if asynchronous:
                    return Cloud(asynchronous=True)
                else:
                    return Cloud(asynchronous=False)
            except Exception:
                raise ValueError("Please first connect with coiled.Cloud(...)")
        else:
            return cloud

    @property
    def closed(self) -> bool:
        if self.session:
            return self.session.closed
        # If we haven't opened, we must be closed?
        return True

    async def _do_request(self, operation_uuid: str, *args, **kwargs):
        """
        This wraps the session.request call and injects a per-call UUID.

        Most of the time we check that this is in a "running" state before making
        requests. However, we can disable that by passing in ensure_running=False
        """
        ensure_running = bool(kwargs.pop("ensure_running", True))
        session = self._ensure_session(ensure_running)
        headers = kwargs["headers"] if "headers" in kwargs else {}
        # get frame of caller
        st = sys._getframe(1)
        func = st.f_code.co_name
        # any point in sendin these?
        # path = st.f_code.co_filename
        # lineno = st.f_lineno
        headers["coiled-operation-id"] = operation_uuid
        headers["coiled-operation-func"] = func
        kwargs["headers"] = headers
        response = await session.request(*args, **kwargs)
        return response

    def _ensure_session(self, ensure_running=True) -> aiohttp.ClientSession:
        if self.session and (not ensure_running or self.status == "running"):
            return self.session
        else:
            raise RuntimeError("Cloud is not running, did you forget to await it?")

    async def _start(self) -> Cloud:
        op_uuid = get_uuid()
        if self.status != "init":
            return self
        # Check that server and token are valid
        self.user, self.token, self.server = await handle_credentials(
            server=self.server, token=self.token, save=False
        )
        self.session = aiohttp.ClientSession(
            headers={
                "Authorization": "Token " + self.token,
                "Client-Version": COILED_VERSION,
                "x-session-id": get_uuid(),
            }
        )
        # do normal queries
        response = await self._do_request(
            op_uuid, "GET", self.server + "/api/v1/users/me/", ensure_running=False
        )
        if response.status == 426:
            # Upgrade required
            await handle_api_exception(response, exception_cls=ImportError)
        if response.status >= 400:
            await handle_api_exception(response)

        data = await response.json()
        self.accounts = {
            d["account"]["slug"]: toolz.merge(
                d["account"],
                {"admin": d["is_admin"]},
            )
            for d in data["membership_set"]
        }
        if self._default_account:
            self._verify_account(self._default_account)

        self.status = "running"

        return self

    @property
    def default_account(self):
        if self._default_account:
            return self._default_account
        elif len(self.accounts) == 1:
            return toolz.first(self.accounts)
        elif self.user in self.accounts:
            return self.user
        elif self.user.lower() in self.accounts:
            return self.user.lower()
        else:
            raise ValueError(
                "Please provide an account among the following options",
                list(self.accounts),
            )

    async def _close(self) -> None:
        if self.session:
            await self.session.close()
        self.status = "closed"

    @overload
    def close(self: Cloud[Sync]) -> None:
        ...

    @overload
    def close(self: Cloud[Async]) -> Awaitable[None]:
        ...

    def close(self) -> Optional[Awaitable[None]]:
        """Close connection to Coiled"""
        result = self._sync(self._close)
        self._loop_runner.stop()
        return result

    def __await__(self: Cloud[Async]):
        return self._start().__await__()

    async def __aenter__(self: Cloud[Async]) -> Cloud[Async]:
        return await self._start()

    async def __aexit__(self: Cloud[Async], typ, value, tb) -> None:
        await self._close()

    def __enter__(self: Cloud[Sync]) -> Cloud[Sync]:
        return self

    def __exit__(self: Cloud[Sync], typ, value, tb) -> None:
        self.close()

    @property
    def asynchronous(self) -> bool:
        """ Are we running in the event loop? """
        return self._asynchronous and self.loop is IOLoop.current()

    @overload
    def _sync(
        self: Cloud[Sync],
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: Union[Sync, Literal[None]] = None,
        callback_timeout=None,
        **kwargs,
    ) -> _T:
        ...

    @overload
    def _sync(
        self: Cloud[Async],
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: Union[bool, Literal[None]] = None,
        callback_timeout=None,
        **kwargs,
    ) -> Awaitable[_T]:
        ...

    def _sync(
        self,
        func: Callable[..., Awaitable[_T]],
        *args,
        asynchronous: bool = None,
        callback_timeout=None,
        **kwargs,
    ) -> Union[_T, Awaitable[_T]]:
        callback_timeout = dask.utils.parse_timedelta(callback_timeout, "s")
        if (
            asynchronous
            or self.asynchronous
            or getattr(thread_state, "asynchronous", False)
        ):
            future = func(*args, **kwargs)
            if callback_timeout is not None:
                future = asyncio.wait_for(future, callback_timeout)
            return future
        else:
            return sync(
                self.loop, func, *args, callback_timeout=callback_timeout, **kwargs
            )

    async def _list_clusters(self, account: str = None):
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid, "GET", self.server + f"/api/v1/{account}/clusters/"
        )
        if response.status >= 400:
            await handle_api_exception(response)

        data = await response.json()
        return {
            d["name"]: format_cluster_output(d, self.server)
            for d in data["results"]
            if d["status"] in ("pending", "running")
        }

    @overload
    def list_clusters(self: Cloud[Sync], account: str = None) -> dict:
        ...

    @overload
    def list_clusters(self: Cloud[Async], account: str = None) -> Awaitable[dict]:
        ...

    @list_docstring
    def list_clusters(self, account: str = None) -> Union[dict, Awaitable[dict]]:
        return self._sync(self._list_clusters, account)

    @overload
    def create_cluster(
        self: Cloud[Sync],
        name: str = None,
        *,
        configuration: str = None,
        software: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: Union[str, int] = None,
        worker_class: str = None,
        worker_options: dict = None,
        scheduler_cpu: int = None,
        scheduler_memory: Union[str, int] = None,
        scheduler_class: str = None,
        scheduler_options: dict = None,
        account: str = None,
        workers: int = 0,
        log_output=sys.stdout,
        backend_options: Optional[Dict] = None,
    ) -> int:
        ...

    @overload
    def create_cluster(
        self: Cloud[Async],
        name: str = None,
        *,
        configuration: str = None,
        software: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: Union[str, int] = None,
        worker_class: str = None,
        worker_options: dict = None,
        scheduler_cpu: int = None,
        scheduler_memory: Union[str, int] = None,
        scheduler_class: str = None,
        scheduler_options: dict = None,
        account: str = None,
        workers: int = 0,
        log_output=sys.stdout,
        backend_options: Optional[Dict] = None,
    ) -> Awaitable[int]:
        ...

    def create_cluster(
        self,
        name: str = None,
        *,
        configuration: str = None,
        software: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: Union[str, int] = None,
        worker_class: str = None,
        worker_options: dict = None,
        scheduler_cpu: int = None,
        scheduler_memory: Union[str, int] = None,
        scheduler_class: str = None,
        scheduler_options: dict = None,
        account: str = None,
        workers: int = 0,
        log_output=sys.stdout,
        backend_options: Optional[Dict] = None,
    ) -> Union[int, Awaitable[int]]:
        return self._sync(
            self._create_cluster,
            name=name,
            configuration=configuration,
            software=software,
            worker_cpu=worker_cpu,
            worker_gpu=worker_gpu,
            worker_memory=worker_memory,
            worker_class=worker_class,
            worker_options=worker_options,
            scheduler_cpu=scheduler_cpu,
            scheduler_memory=scheduler_memory,
            scheduler_class=scheduler_class,
            scheduler_options=scheduler_options,
            account=account,
            workers=workers,
            backend_options=backend_options,
        )

    async def _create_cluster(
        self,
        name: str,
        *,
        configuration: str = None,
        software: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: Union[str, int] = None,
        worker_class: str = None,
        worker_options: dict = None,
        scheduler_cpu: int = None,
        scheduler_memory: Union[str, int] = None,
        scheduler_class: str = None,
        scheduler_options: dict = None,
        account: str = None,
        workers: int = 0,
        log_output=sys.stdout,
        backend_options: Optional[Dict] = None,
    ) -> int:

        account, name = self._normalize_name(name, context_account=account)
        session = self._ensure_session()
        self._verify_account(account)
        backend_options = {**self._default_backend_options, **(backend_options or {})}
        data = {
            "name": name,
            "server": self.server,
            "configuration": configuration,
            "software": software,
            "worker_cpu": worker_cpu,
            "worker_gpu": worker_gpu,
            "worker_memory": max(dask.utils.parse_bytes(worker_memory) // 2 ** 30, 1)
            if worker_memory
            else None,
            "worker_class": worker_class,
            "worker_options": worker_options,
            "scheduler_cpu": scheduler_cpu,
            "scheduler_memory": max(
                dask.utils.parse_bytes(scheduler_memory) // 2 ** 30, 1
            )
            if scheduler_memory
            else None,
            "scheduler_class": scheduler_class,
            "scheduler_options": scheduler_options,
            "workers": workers,
            "options": backend_options,
        }
        ws_server = self.server.replace("http", "ws", 1)
        ws_endpoint = f"{ws_server}/ws/api/v1/{account}/clusters/"
        try:
            ws = await session.ws_connect(ws_endpoint)
        except aiohttp.WSServerHandshakeError:
            raise ValueError(
                "Unable to connect to server, do you have permissions to "
                f'create clusters in the "{account}" account?'
            )
        await ws.send_json(data)

        error_details = await self._websocket_stream(ws, log_output, use_spinner=False)
        if error_details:
            raise ValueError(f"Unable to create cluster: {error_details}")

        return await self._get_cluster_by_name(name=name, account=account)

    async def _delete_cluster(self, cluster_id: int, account: str = None) -> None:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid,
            "DELETE",
            self.server + f"/api/v1/{account}/cluster/{cluster_id}/",
        )
        if response.status >= 400:
            await handle_api_exception(response)
        else:
            rich.print("[green]Cluster deleted successfully.")

    @overload
    def delete_cluster(self: Cloud[Sync], cluster_id: int, account: str = None) -> None:
        ...

    @overload
    def delete_cluster(
        self: Cloud[Async], cluster_id: int, account: str = None
    ) -> Awaitable[None]:
        ...

    @delete_docstring
    def delete_cluster(
        self, cluster_id: int, account: str = None
    ) -> Optional[Awaitable[None]]:
        return self._sync(self._delete_cluster, cluster_id, account)

    @overload
    def get_cluster_by_name(
        self: Cloud[Sync],
        name: str,
        account: str = None,
    ) -> int:
        ...

    @overload
    def get_cluster_by_name(
        self: Cloud[Async],
        name: str,
        account: str = None,
    ) -> Awaitable[int]:
        ...

    def get_cluster_by_name(
        self,
        name: str,
        account: str = None,
    ) -> Union[int, Awaitable[int]]:
        return self._sync(
            self._get_cluster_by_name,
            name=name,
            account=account,
        )

    async def _get_cluster_by_name(
        self,
        name: str,
        account: str = None,
    ) -> int:
        """Fetch the latest cluster (pending/running) and store it under cluster_id"""
        op_uuid = get_uuid()
        account, name = self._normalize_name(name, context_account=account)

        params = {"exclude_statuses": "stopping,stopped"}
        path = self.server + f"/api/v1/{account}/clusters/{name}/"
        response = await self._do_request(
            op_uuid,
            "GET",
            path,
            params=params,
        )

        if response.status >= 400:
            await handle_api_exception(response)

        cluster = await response.json()
        if cluster["id"] is None:
            raise Exception(f"Could not find cluster '{account}/{name}'")

        self.cluster_id = cast(int, cluster["id"])
        return self.cluster_id

    async def _cluster_status(
        self, cluster_id: int, account: str = None, exclude_stopped: bool = True
    ) -> dict:
        op_uuid = get_uuid()
        account = account or self.default_account
        params = {}
        if exclude_stopped:
            params = {"exclude_statuses": "stopping,stopped"}
        response = await self._do_request(
            op_uuid,
            "GET",
            self.server + "/api/v1/{}/cluster/{}/".format(account, cluster_id),
            params=params,
        )
        if response.status >= 400:
            await handle_api_exception(response)
        data = await response.json()
        return data

    async def _security(
        self, cluster_id: int, account: str = None
    ) -> Tuple[dask.distributed.Security, dict]:
        while True:
            data = await self._cluster_status(
                cluster_id=cluster_id, account=account, exclude_stopped=False
            )
            if data["status"] in ["stopped", "stopping"]:
                # cluster is stopped, probably very shortly after starting
                raise ValueError(
                    "Cluster status is unexpectedly STOPPED: it was either unable to start up or died very quickly."
                )
            if data["status"] != "pending" and data["public_address"]:
                break
            else:
                await asyncio.sleep(1.0)
        result = format_security_output(data, cluster_id, self.server)
        security = GatewaySecurity(
            result.get("tls_key"),
            result.get("tls_cert"),
            extra_conn_args=result.get("extra_conn_args"),
        )

        return security, result

    @overload
    def security(
        self: Cloud[Sync], cluster_id: int, account: str = None
    ) -> Tuple[dask.distributed.Security, dict]:
        ...

    @overload
    def security(
        self: Cloud[Async], cluster_id: int, account: str = None
    ) -> Awaitable[Tuple[dask.distributed.Security, dict]]:
        ...

    def security(
        self, cluster_id: int, account: str = None
    ) -> Union[
        Tuple[dask.distributed.Security, dict],
        Awaitable[Tuple[dask.distribued.Security, dict]],
    ]:
        return self._sync(self._security, cluster_id, account)

    async def _scale(self, cluster_id: int, n: int, account: str = None) -> None:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid,
            "PATCH",
            f"{self.server}/api/v1/{account}/cluster/{cluster_id}/scale/",
            data={"worker_count_requested": n},
        )
        if response.status >= 400:
            await handle_api_exception(response)

        with contextlib.suppress(aiohttp.ContentTypeError, json.JSONDecodeError):
            result = await response.json()
            if result:
                warning_style = "[bold][yellow]Warning:[/yellow][/bold] "
                try:
                    message = (
                        f"{result['message']}\n"
                        f"code: {result['code']}\n"
                        f"exception: {result['exception']}"
                    )
                    console.print(f"{warning_style} {message}")
                except KeyError:
                    console.print(f"{warning_style} {result}")
            return

    @overload
    def scale(self: Cloud[Sync], cluster_id: int, n: int, account: str = None) -> None:
        ...

    @overload
    def scale(
        self: Cloud[Async], cluster_id: int, n: int, account: str = None
    ) -> Awaitable[None]:
        ...

    def scale(
        self, cluster_id: int, n: int, account: str = None
    ) -> Optional[Awaitable[None]]:
        """Scale cluster to ``n`` workers

        Parameters
        ----------
        cluster_id
            Unique cluster identifier.
        n
            Number of workers to scale cluster size to.
        account
            Name of Coiled account which the cluster belongs to.
            If not provided, will default to ``Cloud.default_account``.

        """
        return self._sync(self._scale, cluster_id, n, account)

    def _verify_account(self, account: str):
        """Perform sanity checks on account values

        In particular, this raises and informative error message if the
        account is not found, and provides a list of possible options.
        """
        account = account or self.default_account
        if account not in self.accounts:
            raise PermissionError(
                "Account not found: '{}'\n"
                "Possible accounts: {}".format(account, sorted(self.accounts))
            )

    @overload
    def create_software_environment(
        self: Cloud[Sync],
        name: str = None,
        *,
        account: Optional[str] = None,
        conda: Union[list, dict, str] = None,
        pip: Union[list, str] = None,
        container: str = None,
        post_build: Union[list, str] = None,
        conda_env_name: str = None,
        backend_options: Optional[Dict] = None,
        log_output=sys.stdout,
        private: bool = False,
        force_rebuild: bool = False,
    ) -> None:
        ...

    @overload
    def create_software_environment(
        self: Cloud[Async],
        name: str = None,
        *,
        account: Optional[str] = None,
        conda: Union[list, dict, str] = None,
        pip: Union[list, str] = None,
        container: str = None,
        post_build: Union[list, str] = None,
        conda_env_name: str = None,
        backend_options: Optional[Dict] = None,
        log_output=sys.stdout,
        private: bool = False,
        force_rebuild: bool = False,
    ) -> Awaitable[None]:
        ...

    def create_software_environment(
        self,
        name: str = None,
        *,
        account: Optional[str] = None,
        conda: Union[list, dict, str] = None,
        pip: Union[list, str] = None,
        container: str = None,
        post_build: Union[list, str] = None,
        conda_env_name: str = None,
        backend_options: Optional[Dict] = None,
        log_output=sys.stdout,
        private: bool = False,
        force_rebuild: bool = False,
    ) -> Optional[Awaitable[None]]:
        return self._sync(
            self._create_software_environment,
            name=name,
            account=account,
            conda=conda,
            pip=pip,
            container=container,
            post_build=post_build,
            log_output=log_output,
            conda_env_name=conda_env_name,
            backend_options=backend_options,
            private=private,
            force_rebuild=force_rebuild,
        )

    async def _create_software_environment(
        self,
        name=None,
        *,
        account: Optional[str] = None,
        conda=None,
        pip=None,
        container=None,
        post_build=None,
        conda_env_name: str = None,
        log_output=sys.stdout,
        backend_options: Optional[Dict] = None,
        private: bool = False,
        force_rebuild: bool = False,
    ) -> None:
        """
        :param name:
        :param conda:
        :param pip:
        :param container:
        :param post_build:
        :param conda_env_name:
        :param log_output:
        :param backend_options: Dict or None
          backend_options["container_registry"]
        :param private:
        :param force_rebuild:
        :return:
        """
        session = self._ensure_session()
        if conda is None and container is None and pip is not None:
            v = ".".join(map(str, sys.version_info[:2]))
            conda = {"dependencies": [f"python={v}", {"pip": []}]}
        elif isinstance(conda, list):
            conda = {"dependencies": conda}
        elif isinstance(conda, (str, pathlib.Path)):
            # Local conda environment YAML file
            with open(conda, mode="r") as f:
                conda = yaml.safe_load(f)

        if isinstance(pip, (str, pathlib.Path)):
            # Local pip requirements file
            with open(pip, mode="r") as f:
                pip = f.read().splitlines()

        if isinstance(post_build, (str, pathlib.Path)):
            # Post-build script
            with open(post_build, mode="r") as f:
                post_build = f.read().splitlines()

        # Conda supports specifying pip packages via their CLI, but not when
        # using conda.api.Solver. So we move any pip packages to the pip portion
        # of this software environment
        if conda is not None:
            for idx, dep in enumerate(conda["dependencies"]):
                if isinstance(dep, dict) and list(dep.keys()) == ["pip"]:
                    # Copy conda to avoid mutating input from users
                    conda = copy.deepcopy(conda)
                    pip_packages = conda["dependencies"].pop(idx)["pip"]
                    if pip is not None:
                        pip = pip + pip_packages
                    else:
                        pip = pip_packages

        # Remove duplicates and ensure consistent package ordering which helps with
        # downstream tokenization of package spec
        if pip is not None:
            pip = sorted(set(pip))
        if conda is not None:
            conda["dependencies"] = sorted(set(conda["dependencies"]))

        if name is None and conda is not None and "name" in conda:
            name = conda["name"]
        if name is None:
            raise ValueError("Must provide a name when creating a software environment")

        account, name = self._normalize_name(str(name), context_account=account)

        # Connect to the websocket, send the data and get some logs
        # TODO add other types as well
        data = {
            "container": container,
            "conda": conda,
            "conda_env_name": conda_env_name,
            "pip": pip,
            "post_build": post_build,
            "options": {**self._default_backend_options, **(backend_options or {})},
            "private": private,
            "force_rebuild": force_rebuild,
        }

        ws_server = self.server.replace("http", "ws", 1)
        ws_endpoint = (
            f"{ws_server}/ws/api/v1/{account}/software_environments/{name.lower()}/"
        )

        try:
            ws = await session.ws_connect(ws_endpoint)
        except aiohttp.WSServerHandshakeError:
            raise ValueError(
                "Unable to connect to server, do you have permissions to "
                f'create environments in the "{account}" account?'
            )
        await ws.send_json(data)

        print("Updating software environment...")
        error_details = await self._websocket_stream(ws, log_output, use_spinner=False)
        if error_details:
            raise ValueError(f"Unable to update Environment: {error_details}")

    async def _list_software_environments(self, account: Optional[str] = None) -> dict:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid, "GET", self.server + f"/api/v1/{account}/software_environments/"
        )
        if response.status >= 400:
            await handle_api_exception(response)
            return {}
        else:
            results = (await response.json())["results"]

            results = {
                f"{format_account_output(r['account'])}/{r['name']}": format_software_environment_output(
                    r
                )
                for r in results
            }

            return results

    @overload
    def list_software_environments(
        self: Cloud[Sync], account: Optional[str] = None
    ) -> dict:
        ...

    @overload
    def list_software_environments(
        self: Cloud[Async], account: Optional[str] = None
    ) -> Awaitable[dict]:
        ...

    @list_docstring
    def list_software_environments(
        self, account: Optional[str] = None
    ) -> Union[dict, Awaitable[dict]]:
        return self._sync(self._list_software_environments, account=account)

    def _normalize_name(
        self, name: str, context_account: Optional[str] = None
    ) -> Tuple[str, str]:
        account, name, _ = parse_identifier(name)
        account = account or context_account or self.default_account
        return account, name

    @overload
    def delete_software_environment(
        self: Cloud[Sync], name: str, account: Optional[str] = None
    ) -> None:
        ...

    @overload
    def delete_software_environment(
        self: Cloud[Async], name: str, account: Optional[str] = None
    ) -> Awaitable[None]:
        ...

    @delete_docstring
    def delete_software_environment(
        self, name: str, account: Optional[str] = None
    ) -> Optional[Awaitable[None]]:
        return self._sync(self._delete_software_environment, name, account)

    async def _delete_software_environment(
        self, name: str, account: Optional[str] = None
    ) -> None:
        op_uuid = get_uuid()
        context_account = account
        account, name, tag = parse_identifier(name)
        account = account or context_account or self.default_account
        if tag:
            name = ":".join([name, tag])
        response = await self._do_request(
            op_uuid,
            "DELETE",
            self.server + f"/api/v1/{account}/software_environments/{name}/",
        )
        if response.status >= 400:
            await handle_api_exception(response)
        else:
            rich.print("[green]Software environment deleted successfully.")

    @overload
    def create_cluster_configuration(
        self: Cloud[Sync],
        name: str,
        software: str,
        *,
        account: Optional[str] = None,
        worker_cpu: int = 1,
        worker_gpu: int = 0,
        worker_memory: str = "4 GiB",
        worker_class: str = "dask.distributed.Nanny",
        worker_options: dict = None,
        scheduler_cpu: int = 1,
        scheduler_memory: str = "4 GiB",
        scheduler_class: str = "dask.distributed.Scheduler",
        scheduler_options: dict = None,
        private: bool = False,
    ) -> None:
        ...

    @overload
    def create_cluster_configuration(
        self: Cloud[Async],
        name: str,
        software: str,
        *,
        account: Optional[str] = None,
        worker_cpu: int = 1,
        worker_gpu: int = 0,
        worker_memory: str = "4 GiB",
        worker_class: str = "dask.distributed.Nanny",
        worker_options: dict = None,
        scheduler_cpu: int = 1,
        scheduler_memory: str = "4 GiB",
        scheduler_class: str = "dask.distributed.Scheduler",
        scheduler_options: dict = None,
        private: bool = False,
    ) -> Awaitable[None]:
        ...

    def create_cluster_configuration(
        self,
        name: str,
        software: str,
        *,
        account: Optional[str] = None,
        worker_cpu: int = 1,
        worker_gpu: int = 0,
        worker_memory: str = "4 GiB",
        worker_class: str = "dask.distributed.Nanny",
        worker_options: dict = None,
        scheduler_cpu: int = 1,
        scheduler_memory: str = "4 GiB",
        scheduler_class: str = "dask.distributed.Scheduler",
        scheduler_options: dict = None,
        private: bool = False,
    ) -> Optional[Awaitable[None]]:
        return self._sync(
            self._create_cluster_configuration,
            name=name,
            software=software,
            account=account,
            worker_cpu=worker_cpu,
            worker_gpu=worker_gpu,
            worker_memory=worker_memory,
            worker_class=worker_class,
            worker_options=worker_options,
            scheduler_cpu=scheduler_cpu,
            scheduler_memory=scheduler_memory,
            scheduler_class=scheduler_class,
            scheduler_options=scheduler_options,
            private=private,
        )

    async def _create_cluster_configuration(
        self,
        name: str,
        software: str,
        *,
        account: Optional[str] = None,
        worker_cpu: int,
        worker_gpu: int,
        worker_memory: str,
        worker_class: str,
        worker_options: dict,
        scheduler_cpu: int,
        scheduler_memory: str,
        scheduler_class: str,
        scheduler_options: dict,
        private: bool,
    ) -> None:
        op_uuid = get_uuid()
        account, name = self._normalize_name(name, context_account=account)
        data = {
            "software_environment": software,
            "worker_cpu": worker_cpu,
            "worker_gpu": worker_gpu,
            "worker_memory": max(
                # TODO we should be throwing an error instead of choosing
                # 1 if they give use something below 1.
                dask.utils.parse_bytes(worker_memory) // 2 ** 30,
                1,
            ),
            "worker_class": worker_class,
            "worker_options": worker_options or {},
            "scheduler_cpu": scheduler_cpu,
            "scheduler_memory": max(
                dask.utils.parse_bytes(scheduler_memory) // 2 ** 30, 1
            ),
            "scheduler_class": scheduler_class,
            "scheduler_options": scheduler_options or {},
            # TODO environments
            "private": private,
        }
        # Check if we already have a config
        response = await self._do_request(
            op_uuid,
            "GET",
            self.server + f"/api/v1/{account}/cluster_configurations/{name}/",
        )
        if response.status == 404:
            rich.print(f"Attempting to create cluster configuration '{name}'...")
            data.update({"name": name})
            response = await self._do_request(
                op_uuid,
                "POST",
                self.server + f"/api/v1/{account}/cluster_configurations/",
                json=data,
            )
        else:
            rich.print(
                f"Found cluster configuration '{name}', updating this configuration..."
            )
            response = await self._do_request(
                op_uuid,
                "PATCH",
                self.server + f"/api/v1/{account}/cluster_configurations/{name}/",
                json=data,
            )

        if response.status >= 400:
            await handle_api_exception(response)

    @overload
    def list_cluster_configurations(self: Cloud[Sync], account=None) -> dict:
        ...

    @overload
    def list_cluster_configurations(
        self: Cloud[Async], account=None
    ) -> Awaitable[dict]:
        ...

    @list_docstring
    def list_cluster_configurations(self, account=None) -> Union[dict, Awaitable[dict]]:
        return self._sync(self._list_cluster_configurations, account=account)

    async def _list_cluster_configurations(self, account=None) -> dict:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid,
            "GET",
            self.server + f"/api/v1/{account}/cluster_configurations/",
        )
        if response.status >= 400:
            await handle_api_exception(response)  # will always raise
        results = (await response.json())["results"]
        results = {
            f"{format_account_output(r['account'])}/{r['name']}": format_cluster_configuration_output(
                r
            )
            for r in results
        }
        return results

    @overload
    def list_job_configurations(self: Cloud[Sync], account=None) -> dict:
        ...

    @overload
    def list_job_configurations(self: Cloud[Async], account=None) -> Awaitable[dict]:
        ...

    @list_docstring
    def list_job_configurations(self, account=None) -> Union[dict, Awaitable[dict]]:
        return self._sync(self._list_job_configurations, account=account)

    async def _list_job_configurations(self, account=None) -> dict:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid,
            "GET",
            self.server + f"/api/v1/{account}/process-configurations/",
            params={"only_listable": "True"},
        )
        if response.status >= 400:
            await handle_api_exception(response)  #  will always raise
        results = (await response.json())["results"]
        results = {r["name"]: format_job_configuration_output(r) for r in results}
        return results

    @overload
    def delete_job_configuration(
        self: Cloud[Sync], name: str, account: Optional[str] = None
    ) -> None:
        ...

    @overload
    def delete_job_configuration(
        self: Cloud[Async], name: str, account: Optional[str] = None
    ) -> Awaitable[None]:
        ...

    @delete_docstring
    def delete_job_configuration(
        self, name: str, account: Optional[str] = None
    ) -> Optional[Awaitable[None]]:
        return self._sync(self._delete_job_configuration, name, account)

    async def _delete_job_configuration(
        self, name: str, account: Optional[str] = None
    ) -> None:
        op_uuid = get_uuid()
        account, name = self._normalize_name(name, context_account=account)
        response = await self._do_request(
            op_uuid,
            "DELETE",
            self.server + f"/api/v1/{account}/process-configurations/{name}/",
        )
        if response.status >= 400:
            await handle_api_exception(response)
        else:
            rich.print(f"[green]Deleted '{name}' successfully.")

    @overload
    def list_jobs(self: Cloud[Sync], account: Optional[str] = None) -> dict:
        ...

    @overload
    def list_jobs(self: Cloud[Async], account: Optional[str] = None) -> Awaitable[dict]:
        ...

    @list_docstring
    def list_jobs(self, account: Optional[str] = None) -> Union[dict, Awaitable[dict]]:
        return self._sync(self._list_jobs, account=account)

    async def _list_jobs(self, account: Optional[str] = None) -> dict:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid, "GET", self.server + f"/api/v1/{account}/jobs/"
        )
        if response.status >= 400:
            await handle_api_exception(response)  # will always raise
        results = (await response.json())["results"]
        results = {
            r["name"]: format_job_output(r)
            for r in results
            if r["status"] in ("pending", "running")
        }
        return results

    @overload
    def get_job_by_name(
        self: Cloud[Sync],
        name: str,
        account: str = None,
        backend_options: Optional[Dict] = None,
    ) -> Optional[int]:
        ...

    @overload
    def get_job_by_name(
        self: Cloud[Async],
        name: str,
        account: str = None,
        backend_options: Optional[Dict] = None,
    ) -> Awaitable[Optional[int]]:
        ...

    def get_job_by_name(
        self, name: str, account: str = None, backend_options: Optional[Dict] = None
    ) -> Union[Optional[int], Awaitable[Optional[int]]]:
        return self._sync(
            self._get_job_by_name,
            name=name,
            account=account,
            backend_options=backend_options,
        )

    async def _get_job_by_name(
        self,
        name: str,
        account: str = None,
        backend_options: Optional[Dict] = None,
    ) -> Optional[int]:
        """Fetch the latest running job"""
        op_uuid = get_uuid()
        account, name = self._normalize_name(name, context_account=account)
        response = await self._do_request(
            op_uuid,
            "GET",
            self.server + f"/api/v1/{account}/jobs/{name}/",
            params={"exclude_statuses": "pending,stopped"},
        )

        if response.status >= 400:
            await handle_api_exception(response)

        job = await response.json()
        return job["id"]

    @overload
    def delete_cluster_configuration(
        self: Cloud[Sync], name: str, account: Optional[str] = None
    ) -> None:
        ...

    @overload
    def delete_cluster_configuration(
        self: Cloud[Async], name: str, account: Optional[str] = None
    ) -> Awaitable[None]:
        ...

    @delete_docstring
    def delete_cluster_configuration(
        self, name: str, account: Optional[str] = None
    ) -> Optional[Awaitable[None]]:
        return self._sync(self._delete_cluster_configuration, name, account)

    async def _delete_cluster_configuration(
        self, name: str, account: Optional[str] = None
    ):
        op_uuid = get_uuid()
        account, name = self._normalize_name(name, context_account=account)

        response = await self._do_request(
            op_uuid,
            "DELETE",
            self.server + f"/api/v1/{account}/cluster_configurations/{name}/",
        )
        if response.status >= 400:
            await handle_api_exception(response)
        else:
            rich.print("[green]Cluster configuration deleted successfully.")

    @overload
    def create_job_configuration(
        self: Cloud[Sync],
        name: str,
        command: List[str],
        software: str,
        *,
        account: Optional[str] = None,
        cpu: int = 1,
        gpu: int = 0,
        memory: str = "4 GiB",
        ports: List = None,
        files: Union[str, List[str]] = None,
        description: Optional[str] = None,
    ) -> None:
        ...

    @overload
    def create_job_configuration(
        self: Cloud[Async],
        name: str,
        command: List[str],
        software: str,
        *,
        account: Optional[str] = None,
        cpu: int = 1,
        gpu: int = 0,
        memory: str = "4 GiB",
        ports: List = None,
        files: Union[str, List[str]] = None,
        description: Optional[str] = None,
    ) -> Awaitable[None]:
        ...

    def create_job_configuration(
        self,
        name: str,
        command: List[str],
        software: str,
        *,
        account: Optional[str] = None,
        cpu: int = 1,
        gpu: int = 0,
        memory: str = "4 GiB",
        ports: List = None,
        files: Union[str, List[str]] = None,
        description: Optional[str] = None,
    ) -> Optional[Awaitable[None]]:
        return self._sync(
            self._create_job_configuration,
            name=name,
            command=command,
            software=software,
            account=account,
            cpu=cpu,
            gpu=gpu,
            memory=memory,
            ports=ports,
            files=files,
            description=description,
        )

    async def _create_job_configuration(
        self,
        name: str,
        command: List[str],
        software: str,
        *,
        account: Optional[str] = None,
        cpu: int = 1,
        gpu: int = 0,
        memory: str = "4 GiB",
        ports: List = None,
        files: Union[str, List[str]] = None,
        description: Optional[str] = None,
    ) -> None:
        op_uuid = get_uuid()
        account, name = self._normalize_name(name, context_account=account)

        if isinstance(files, str):
            files = [files]

        file_mapping = {}
        if files is not None:
            for path in files:
                with open(path, "rb") as f:
                    file_mapping[os.path.basename(path)] = base64.b64encode(
                        f.read()
                    ).decode("utf8")

        data = {
            "software_environment": software,
            "cpu": cpu,
            "gpu": gpu,
            "memory": max(
                # TODO we should be throwing an error instead of choosing
                # 1 if they give use something below 1.
                dask.utils.parse_bytes(memory) // 2 ** 30,
                1,
            ),
            "command": command,
            "ports": ports or [],
            "listable": True,
            "files": file_mapping,
            "description": description,
            # TODO environments
        }
        # Check if we already have a config
        response = await self._do_request(
            op_uuid,
            "GET",
            self.server + f"/api/v1/{account}/process-configurations/{name}/",
        )
        if response.status == 404:
            data.update({"name": name})
            response = await self._do_request(
                op_uuid,
                "POST",
                self.server + f"/api/v1/{account}/process-configurations/",
                json=data,
            )
        else:
            response = await self._do_request(
                op_uuid,
                "PATCH",
                self.server + f"/api/v1/{account}/process-configurations/{name}/",
                json=data,
            )

        if response.status >= 400:
            await handle_api_exception(response)

    @overload
    def start_job(
        self: Cloud[Sync],
        configuration: str = None,
        account: str = None,
        backend_options: Optional[Dict] = None,
        log_output=sys.stdout,
    ) -> str:
        ...

    @overload
    def start_job(
        self: Cloud[Async],
        configuration: str = None,
        account: str = None,
        backend_options: Optional[Dict] = None,
        log_output=sys.stdout,
    ) -> Awaitable[str]:
        ...

    def start_job(
        self,
        configuration: str = None,
        account: str = None,
        backend_options: Optional[Dict] = None,
        log_output=sys.stdout,
    ) -> Union[str, Awaitable[str]]:

        return self._sync(
            self._start_job,
            configuration=configuration,
            account=account,
            backend_options=backend_options,
            log_output=log_output,
        )

    async def _start_job(
        self,
        configuration: str,
        account: str = None,
        backend_options: Optional[Dict] = None,
        log_output=sys.stdout,
    ) -> str:
        account, name = self._normalize_name(configuration, context_account=account)
        session = self._ensure_session()
        self._verify_account(account)
        name = self.user + "-" + name + "-" + str(uuid.uuid4())[:10]
        data = {
            "name": name,
            # TODO why do we need to send the server's url
            # to itself?
            "server": self.server,
            "job": configuration,
            "options": {**self._default_backend_options, **(backend_options or {})},
        }
        ws_server = self.server.replace("http", "ws", 1)
        ws_endpoint = f"{ws_server}/ws/api/v1/{account}/jobs/"
        try:
            ws = await session.ws_connect(ws_endpoint)
        except aiohttp.WSServerHandshakeError:
            raise ValueError(
                "Unable to connect to server, do you have permissions to "
                f'start jobs in the "{account}" account?'
            )
        await ws.send_json(data)
        print("Starting job. This might take a few minutes ...", end="")
        error_details = await self._websocket_stream(ws, log_output)
        if error_details:
            raise ValueError(f"Unable to start_job: {error_details}")

        return name

    @overload
    def stop_job(self: Cloud[Sync], name: str, account: Optional[str] = None) -> None:
        ...

    @overload
    def stop_job(
        self: Cloud[Async], name: str, account: Optional[str] = None
    ) -> Awaitable[None]:
        ...

    def stop_job(
        self, name: str, account: Optional[str] = None
    ) -> Optional[Awaitable[None]]:
        return self._sync(
            self._stop_job,
            name=name,
            account=account,
        )

    async def _stop_job(self, name: str, account: Optional[str] = None) -> None:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid,
            "DELETE",
            self.server + f"/api/v1/{account}/jobs/{name}/",
        )
        if response.status >= 400:
            await handle_api_exception(response)

    async def _websocket_stream(self, ws, log_output, use_spinner=True):
        error_details = None
        with Spinner() if use_spinner else contextlib.suppress():
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    data = msg.json()
                    # TODO: Change this hack since it belongs only to jobs
                    if "type" in data:
                        if data["type"] == "job_status_changed":
                            await ws.close()
                            return
                    elif "message" in data:
                        message = data["message"]
                        if data.get("raise", False):
                            error_details = message
                        print(f"{message}", file=log_output)
                elif msg.type == aiohttp.WSMsgType.CLOSE:
                    await ws.close()

                elif msg.type == aiohttp.WSMsgType.ERROR:
                    # TODO find out what would be in one of these messages
                    error_details = str(msg.extra)
                    break
                else:
                    raise ValueError(f"Unexpected websocket message: {str(msg)}")
        return error_details

    @overload
    def cluster_logs(
        self: Cloud[Sync],
        cluster_id: int,
        account: str = None,
        scheduler: bool = True,
        workers: bool = True,
    ) -> Logs:
        ...

    @overload
    def cluster_logs(
        self: Cloud[Async],
        cluster_id: int,
        account: str = None,
        scheduler: bool = True,
        workers: bool = True,
    ) -> Awaitable[Logs]:
        ...

    def cluster_logs(
        self,
        cluster_id: int,
        account: str = None,
        scheduler: bool = True,
        workers: bool = True,
    ) -> Union[Logs, Awaitable[Logs]]:
        return self._sync(self._cluster_logs, cluster_id, account, scheduler, workers)

    async def _cluster_logs(
        self,
        cluster_id: int,
        account: str = None,
        scheduler: bool = True,
        workers: bool = True,
    ) -> Logs:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid,
            "GET",
            self.server + "/api/v1/{}/cluster/{}/logs/".format(account, cluster_id),
        )
        if response.status >= 400:
            await handle_api_exception(response)

        data = await response.json()
        # munge the response to match the signature of Cluster's parent class
        out = {}
        if scheduler:
            out["Scheduler"] = Log(data["scheduler"]["logs"])
        if workers:
            for w in data["workers"]:
                out[w["name"]] = Log(w["logs"])

        return Logs(out)

    @overload
    def job_logs(
        self: Cloud[Sync],
        job_id: int,
        account: str = None,
    ) -> Logs:
        ...

    @overload
    def job_logs(
        self: Cloud[Async],
        job_id: int,
        account: str = None,
    ) -> Awaitable[Logs]:
        ...

    def job_logs(
        self,
        job_id: int,
        account: str = None,
    ) -> Union[Logs, Awaitable[Logs]]:
        return self._sync(self._job_logs, job_id, account=account)

    async def _job_logs(
        self,
        job_id: int,
        account: str = None,
    ) -> Logs:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid,
            "GET",
            self.server + "/api/v1/{}/jobs/{}/logs/".format(account, job_id),
        )
        if response.status >= 400:
            await handle_api_exception(response)

        data = await response.json()

        return Logs({"Process": Log(data["process"]["logs"])})

    async def get_aws_credentials(self, account: str = None):
        """Return the logged in user's AWS credentials"""
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid, "GET", self.server + f"/api/v1/{account}/backend_options/"
        )
        if response.status >= 400:
            await handle_api_exception(response)

        backend_options = await response.json()
        if backend_options["backend"] != "ecs":
            return {}

        credentials = backend_options.get("options", {}).get("credentials", {})
        return credentials

    @overload
    def get_software_info(
        self: Cloud[Sync], name: str, account: Optional[str] = None
    ) -> dict:
        ...

    @overload
    def get_software_info(
        self: Cloud[Async], name: str, account: Optional[str] = None
    ) -> Awaitable[dict]:
        ...

    def get_software_info(
        self, name: str, account: Optional[str] = None
    ) -> Union[dict, Awaitable[dict]]:
        return self._sync(self._get_software_info, name=name, account=account)

    async def _get_software_info(
        self, name: str, account: Optional[str] = None
    ) -> dict:
        """Retrieve solved spec for a Coiled software environment

        Parameters
        ----------
        name
            Software environment name

        Returns
        -------
        results
            Coiled software environment information
        """
        op_uuid = get_uuid()
        account, name = self._normalize_name(name, context_account=account)

        response = await self._do_request(
            op_uuid,
            "GET",
            self.server + f"/api/v1/{account}/software_environments/{name}/",
        )
        if response.status >= 400:
            text = await response.text()
            if "Not found" in text:
                raise ValueError(
                    f"Could not find a '{account}/{name}' Coiled software environment"
                )
            else:
                await handle_api_exception(response)

        results = await response.json()
        return results

    @overload
    def cluster_cost_estimate(
        self: Cloud[Sync],
        *,
        account: str = None,
        n_workers: int = 4,
        configuration: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: Union[str, int] = None,
        scheduler_cpu: int = None,
        scheduler_memory: Union[str, int] = None,
        backend_options: Optional[Dict] = None,
    ) -> str:
        ...

    @overload
    def cluster_cost_estimate(
        self: Cloud[Async],
        *,
        account: str = None,
        n_workers: int = 4,
        configuration: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: Union[str, int] = None,
        scheduler_cpu: int = None,
        scheduler_memory: Union[str, int] = None,
        backend_options: Optional[Dict] = None,
    ) -> Awaitable[str]:
        ...

    def cluster_cost_estimate(
        self,
        *,
        account: str = None,
        n_workers: int = 4,
        configuration: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: Union[str, int] = None,
        scheduler_cpu: int = None,
        scheduler_memory: Union[str, int] = None,
        backend_options: Optional[Dict] = None,
    ) -> Union[str, Awaitable[str]]:
        return self._sync(
            self._cluster_cost_estimate,
            account=account,
            n_workers=n_workers,
            configuration=configuration,
            worker_cpu=worker_cpu,
            worker_gpu=worker_gpu,
            worker_memory=worker_memory,
            scheduler_cpu=scheduler_cpu,
            scheduler_memory=scheduler_memory,
            backend_options=backend_options,
        )

    async def _cluster_cost_estimate(
        self,
        *,
        account: str = None,
        n_workers: int = None,
        configuration: str = None,
        worker_cpu: int = None,
        worker_gpu: int = None,
        worker_memory: Union[str, int] = None,
        scheduler_cpu: int = None,
        scheduler_memory: Union[str, int] = None,
        backend_options: Optional[Dict] = None,
    ) -> str:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid,
            "POST",
            self.server + f"/api/v1/{account}/cluster/cost-estimate/",
            json={
                "n_workers": n_workers,
                "configuration": configuration,
                "worker_cpu": worker_cpu,
                "worker_memory": max(
                    dask.utils.parse_bytes(worker_memory) // 2 ** 30, 1
                )
                if worker_memory
                else None,
                "worker_gpu": worker_gpu,
                "scheduler_cpu": scheduler_cpu,
                "scheduler_memory": max(
                    dask.utils.parse_bytes(scheduler_memory) // 2 ** 30, 1
                )
                if scheduler_memory
                else None,
                "options": {**self._default_backend_options, **(backend_options or {})},
            },
        )

        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()
        return f"${result['cost']}/hr"

    @overload
    def list_core_usage(
        self: Cloud[Sync], json: Literal[False], account: str = None
    ) -> None:
        ...

    @overload
    def list_core_usage(
        self: Cloud[Async], json: Literal[False], account: str = None
    ) -> Awaitable[None]:
        ...

    @overload
    def list_core_usage(
        self: Cloud[Sync], json: Literal[True], account: str = None
    ) -> dict:
        ...

    @overload
    def list_core_usage(
        self: Cloud[Async], json: Literal[True], account: str = None
    ) -> Awaitable[dict]:
        ...

    @overload
    def list_core_usage(
        self: Cloud[Async], json: bool, account: str = None
    ) -> Awaitable[Optional[dict]]:
        ...

    @overload
    def list_core_usage(
        self: Cloud[Sync], json: bool, account: str = None
    ) -> Optional[dict]:
        ...

    def list_core_usage(
        self, json: bool = False, account: str = None
    ) -> Union[Awaitable[Optional[dict]], Optional[dict]]:
        return self._sync(self._list_core_usage, json=json, account=account)

    async def _list_core_usage(
        self, json: bool = False, account: str = None
    ) -> Optional[dict]:
        op_uuid = get_uuid()
        account = account or self.default_account

        response = await self._do_request(
            op_uuid, "GET", f"{self.server}/api/v1/{account}/usage/cores/"
        )

        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()

        if json:
            return result

        cores_table = Table(title="Core usage")
        cores_table.add_column("Account Limit", justify="center")
        cores_table.add_column("User Total", justify="center")
        cores_table.add_column("Account Total", justify="center")
        cores_table.add_column("Cores used by Clusters", justify="center")
        cores_table.add_column("Cores used by Jobs", justify="center")

        cores_table.add_row(
            str(result["account_limit"]),
            str(result["user_total"]),
            str(result["account_total"]),
            str(result["clusters_total"]),
            str(result["jobs_total"]),
        )

        console = Console()
        console.print(cores_table)
        return None

    async def _list_local_versions(self, json: bool = False) -> Union[dict, None]:
        versions_table = Table(title="Versions")
        versions_table.add_column("Operating System", justify="center")
        versions_table.add_column("Python Version", justify="center")
        versions_table.add_column("Pip Version", justify="center"),
        versions_table.add_column("Conda Version", justify="center")
        versions_table.add_column("Coiled Version", justify="center")
        versions_table.add_column("Dask Version", justify="center")
        versions_table.add_column("Distributed Version", justify="center")

        try:
            import conda

            conda_version = conda.__version__
        except ModuleNotFoundError:
            conda_version = "None"

        try:
            import pip

            pip_version = pip.__version__
        except ModuleNotFoundError:
            pip_version = "None"

        versions_table.add_row(
            platform.platform(),
            str(PY_VERSION),
            pip_version,
            conda_version,
            str(COILED_VERSION),
            dask.__version__,
            distributed.__version__,
        )

        if json:
            return {
                "operating_system": platform.platform(),
                "python_version": PY_VERSION,
                "pip_version": pip_version,
                "conda_version": conda_version,
                "coiled_version": COILED_VERSION,
                "dask_version": dask.__version__,
                "distributed_version": distributed.__version__,
            }

        console.print(versions_table)
        return None

    @overload
    def list_local_versions(self: Cloud[Sync], json: Literal[False]) -> None:
        ...

    @overload
    def list_local_versions(
        self: Cloud[Async], json: Literal[False]
    ) -> Awaitable[None]:
        ...

    @overload
    def list_local_versions(self: Cloud[Sync], json: Literal[True]) -> dict:
        ...

    @overload
    def list_local_versions(self: Cloud[Async], json: Literal[True]) -> Awaitable[dict]:
        ...

    @overload
    def list_local_versions(self: Cloud[Sync], json: bool) -> Optional[dict]:
        ...

    @overload
    def list_local_versions(
        self: Cloud[Async], json: bool
    ) -> Awaitable[Optional[dict]]:
        ...

    def list_local_versions(
        self, json: bool = False
    ) -> Union[Awaitable[Optional[dict]], Optional[dict]]:
        return self._sync(self._list_local_versions, json=json)

    @overload
    def get_notifications(
        self: Cloud[Sync],
        json: Literal[True],
        account: str = None,
        limit: int = 100,
    ) -> List[dict]:
        ...

    @overload
    def get_notifications(
        self: Cloud[Async],
        json: Literal[True],
        account: str = None,
        limit: int = 100,
    ) -> Awaitable[List[dict]]:
        ...

    @overload
    def get_notifications(
        self: Cloud[Sync],
        json: bool,
        account: str = None,
        limit: int = 100,
    ) -> Optional[List[dict]]:
        ...

    @overload
    def get_notifications(
        self: Cloud[Async],
        json: bool,
        account: str = None,
        limit: int = 100,
    ) -> Awaitable[Optional[List[dict]]]:
        ...

    def get_notifications(
        self,
        json: bool = False,
        account: str = None,
        limit: int = 100,
    ) -> Union[Awaitable[Optional[List[dict]]], Optional[List[dict]]]:
        return self._sync(
            self._get_notifications, json=json, account=account, limit=limit
        )

    async def _get_notifications(
        self,
        json: bool = False,
        account: str = None,
        limit: int = 100,
    ) -> Optional[List[dict]]:
        op_uuid = get_uuid()
        account = account or self.default_account

        response = await self._do_request(
            op_uuid,
            "GET",
            f"{self.server}/api/v1/{account}/notifications/",
            params={"limit": limit},
        )

        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()
        notifications: List[dict] = result["notifications"]

        if json:
            return notifications

        cores_table = Table(title="Notifications")
        cores_table.add_column("time", justify="center")
        cores_table.add_column("id", justify="center")
        cores_table.add_column("level", justify="center")
        cores_table.add_column("event_type", justify="center")
        cores_table.add_column("msg", justify="center")
        cores_table.add_column("data", justify="center")

        for notification in notifications:
            try:
                local_time = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime(notification["timestamp"])
                )
            except KeyError:
                local_time = "???"
            cores_table.add_row(
                str(local_time),
                str(notification.get("id", "")),
                str(notification.get("level", "")),
                str(notification.get("event_type", "")),
                str(notification["msg"]),
                str(notification.get("data", "")),
            )

        console = Console()
        console.print(cores_table)
        return None

    async def _noop_wait(self, duration: int):
        op_uuid = get_uuid()
        response = await self._do_request(
            op_uuid, "GET", self.server + f"/api/v1/_noop_wait/{int(duration)}"
        )

        result = await response.json()
        return result

    async def _upload_performance_report(
        self,
        content: str,
        account: str = None,
        filename: str = None,
        private: bool = False,
    ) -> Dict:
        op_uuid = get_uuid()
        account = account or self.default_account

        data = aiohttp.MultipartWriter("form-data")
        part = data.append(open(content, "rb"))
        part.headers[
            aiohttp.hdrs.CONTENT_DISPOSITION
        ] = f'form-data; name="file"; filename="{filename}"; filename*="other_{filename}"'

        upload_type = "private" if private else "public"
        response = await self._do_request(
            op_uuid,
            "POST",
            f"{self.server}/api/v1/{account}/performance_reports/{upload_type}/",
            data=data,
        )

        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()
        return result

    @overload
    def upload_performance_report(
        self: Cloud[Sync],
        content: str,
        account: str = None,
        filename: str = None,
        private: bool = False,
    ) -> Dict:
        ...

    @overload
    def upload_performance_report(
        self: Cloud[Async],
        content: str,
        account: str = None,
        filename: str = None,
        private: bool = False,
    ) -> Awaitable[Dict]:
        ...

    def upload_performance_report(
        self,
        content: str,
        account: str = None,
        filename: str = None,
        private: bool = False,
    ) -> Union[Dict, Awaitable[Dict]]:
        return self._sync(
            self._upload_performance_report,
            content,
            filename=filename,
            account=account,
            private=private,
        )

    async def _list_performance_reports(
        self,
        account: str = None,
    ) -> List[Dict]:
        op_uuid = get_uuid()
        account = account or self.default_account
        response = await self._do_request(
            op_uuid,
            "GET",
            f"{self.server}/api/v1/{account}/performance_reports/all/",
        )
        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()
        return result

    @overload
    def list_performance_reports(
        self: Cloud[Async],
        account: str = None,
    ) -> Awaitable[List[Dict]]:
        ...

    @overload
    def list_performance_reports(
        self: Cloud[Sync],
        account: str = None,
    ) -> List[Dict]:
        ...

    def list_performance_reports(
        self,
        account: str = None,
    ) -> Union[List[Dict], Awaitable[List[Dict]]]:
        return self._sync(
            self._list_performance_reports,
            account=account,
        )

    @overload
    def list_user_information(self: Cloud[Sync]) -> dict:
        ...

    @overload
    def list_user_information(self: Cloud[Async]) -> Awaitable[dict]:
        ...

    def list_user_information(self) -> Union[Awaitable[dict], dict]:
        return self._sync(self._list_user_information)

    async def _list_user_information(
        self,
    ) -> dict:
        op_uuid = get_uuid()
        response = await self._do_request(
            op_uuid, "GET", self.server + "/api/v1/users/me/"
        )
        if response.status >= 400:
            await handle_api_exception(response)
        result = await response.json()

        return result

    async def _health_check(self) -> dict:
        op_uuid = get_uuid()
        response = await self._do_request(
            op_uuid, "GET", self.server + "/api/v1/health"
        )
        if response.status >= 400:
            await handle_api_exception(response)

        result = await response.json()
        return result

    @overload
    def health_check(self: Cloud[Sync]) -> dict:
        ...

    @overload
    def health_check(self: Cloud[Async]) -> Awaitable[dict]:
        ...

    def health_check(self) -> Union[Awaitable[dict], dict]:
        return self._sync(self._health_check)


# Utility functions for formatting list_* endpoint responses to be more user-friendly


def format_security_output(data, cluster_id, server):
    d = data.copy()
    scheme, _ = parse_address(d["public_address"])
    if scheme.startswith("ws"):
        address = f"{server.replace('http', 'ws')}/cluster/{cluster_id}/"
        d["public_address"] = address
        d["dashboard_address"] = f"{server}/dashboard/{cluster_id}/status"
        d.pop("tls_key")
        d.pop("tls_cert")
    else:
        d.pop("extra_conn_args")
    return d


def format_account_output(d):
    return d["slug"]


def format_software_environment_output(d):
    exclude_list = [
        "id",
        "name",
        "content_hash",
        "builds",
    ]
    d = {k: v for k, v in d.items() if k not in exclude_list}
    d["account"] = format_account_output(d["account"])
    return d


def format_cluster_configuration_output(d):
    d = d.copy()
    d.pop("id")
    d.pop("name")
    d["account"] = format_account_output(d["account"])
    for process in ["scheduler", "worker"]:
        d[process].pop("id")
        d[process].pop("name")
        d[process].pop("account")
        d[process]["software"] = d[process]["software_environment"]
        d[process].pop("software_environment")
    return d


def format_cluster_output(d, server):
    d = d.copy()
    for key in ["auth_token", "private_address", "name", "last_seen"]:
        d.pop(key)
    d["account"] = format_account_output(d["account"])
    # Rename "public_address" to "address"
    address = d.pop("public_address")
    scheme, _ = parse_address(address)
    if scheme.startswith("ws"):
        address = f"{server.replace('http', 'ws')}/cluster/{d['id']}/"
    d["address"] = address
    # Use proxied dashboard address if we're in a hosted notebook
    # or proxying through websockets
    if dask.config.get("coiled.dashboard.proxy", False) or scheme.startswith("ws"):
        d["dashboard_address"] = f"{server}/dashboard/{d['id']}/status"
    return d


def format_job_configuration_output(d):
    d = d.copy()
    d["software"] = d["software_environment"]
    # d["software"] = "/".join(
    #     [
    #         d["software_environment"]["account"]["slug"],
    #         d["software_environment"]["name"],
    #     ]
    # )
    if d["files"] is not None:
        d["files"] = list(d["files"].keys())
    for key in ["id", "software_environment", "name", "listable"]:
        d.pop(key)

    d["account"] = format_account_output(d["account"])

    return d


def format_job_output(d):
    d = d.copy()
    d["configuration"] = "/".join(
        [d["process"]["account"]["slug"], d["process"]["name"]]
    )
    for key in ["process", "name"]:
        d.pop(key)

    d["account"] = format_account_output(d["account"])

    return d


# Public API


def create_software_environment(
    name: str = None,
    *,
    account: Optional[str] = None,
    conda: Union[list, dict, str] = None,
    pip: Union[list, str] = None,
    container: str = None,
    log_output=sys.stdout,
    post_build: Union[list, str] = None,
    conda_env_name: str = None,
    backend_options: Optional[Dict] = None,
    private: bool = False,
    force_rebuild: bool = False,
) -> None:
    """Create a software environment

    Parameters
    ---------
    name
        Name of software environment. Name can't contain uppercase letters.
    account
        The account in which to create the software environment, if not given in the name.
    conda
        Specification for packages to install into the software environment using conda.
        Can be a list of packages, a dictionary, or a path to a conda environment YAML file.
    pip
        Packages to install into the software environment using pip.
        Can be a list of packages or a path to a pip requirements file.
    container
        Docker image to use for the software environment. Must be the name of a docker image
        on Docker hub. Defaults to ``coiled/default``.
    post_build
        List of commands or path to a local executable script to run after pip and conda packages
        have been installed.
    log_output
        Stream to output logs to. Defaults to ``sys.stdout``.
    conda_env_name
        Name of conda environment to install packages into. Note that this should *only* be used
        when specifying a non-default value for ``container`` *and* when the non-default Docker
        image used expects commands to run in a conda environment not named "coiled".
        Defaults to "coiled".
    backend_options
        Dictionary of backend specific options (e.g. ``{'region': 'us-east-2'}``). Any options
        specified with this keyword argument will take precedence over those stored in the
        ``coiled.backend-options`` cofiguration value.
    private
        Whether this software environment is private or public. Defaults to ``False``
    force_rebuild
        By default, if an existing software environment with the same name and dependencies already
        exists, a rebuild is aborted. If this is set to True, those checks are skipped and the
        environment will be rebuilt. Defaults to ``False``
    """
    with Cloud() as cloud:
        return cloud.create_software_environment(
            name=name,
            account=account,
            conda=conda,
            pip=pip,
            container=container,
            post_build=post_build,
            log_output=log_output,
            conda_env_name=conda_env_name,
            backend_options=backend_options,
            private=private,
            force_rebuild=force_rebuild,
        )


@list_docstring
def list_software_environments(account=None):
    with Cloud(account=account) as cloud:
        return cloud.list_software_environments(account=account)


@delete_docstring
def delete_software_environment(name):
    with Cloud() as cloud:
        return cloud.delete_software_environment(name=name)


def get_software_info(name: str, account: Optional[str] = None) -> dict:
    """Retrieve solved spec for a Coiled software environment

    Parameters
    ----------
    name
        Software environment name

    Returns
    -------
    results
        Coiled software environment information
    """
    with Cloud() as cloud:
        return cloud.get_software_info(name=name, account=account)


def create_cluster_configuration(
    name: str,
    software: str,
    *,
    account: str = None,
    worker_cpu: int = 1,
    worker_gpu: int = 0,
    worker_memory: str = "4 GiB",
    worker_class: str = "dask.distributed.Nanny",
    worker_options: dict = None,
    scheduler_cpu: int = 1,
    scheduler_memory: str = "4 GiB",
    scheduler_class: str = "dask.distributed.Scheduler",
    scheduler_options: dict = None,
    private: bool = False,
) -> None:
    """Create a cluster configuration

    Parameters
    ----------
    name
        Name of cluster configuration.
        Optionally prefixed with an account name like "myaccount/myname"
    software
        Identifier of the software environment to use, in the format (<account>/)<name>. If the software environment
        is owned by the same account as that passed into "account", the (<account>/) prefix is optional.

        For example, suppose your account is "wondercorp", but your friends at "friendlycorp" have an environment
        named "xgboost" that you want to use; you can specify this with "friendlycorp/xgboost". If you simply
        entered "xgboost", this is shorthand for "wondercorp/xgboost".

        The "name" portion of (<account>/)<name> can only contain ASCII letters, hyphens and underscores.
    account
        The account in which to create the cluster configuration, if not given in the name.
    worker_cpu
        Number of CPUs allocated for each worker. Defaults to 1.
    worker_gpu
        Number of GPUs allocated for each worker. Defaults to 0 (no GPU support). Note that this will _always_
        allocate GPU-enabled workers, so is expensive.
    worker_memory
        Amount of memory to allocate for each worker. Defaults to 4 GiB.
    worker_class
        Worker class to use. Defaults to "dask.distributed.Nanny".
    worker_options
        Mapping with keyword arguments to pass to ``worker_class``. Defaults to ``{}``.
    scheduler_cpu
        Number of CPUs allocated for the scheduler. Defaults to 1.
    scheduler_memory
        Amount of memory to allocate for the scheduler. Defaults to 4 GiB.
    scheduler_class
        Scheduler class to use. Defaults to "dask.distributed.Scheduler".
    scheduler_options
        Mapping with keyword arguments to pass to ``scheduler_class``. Defaults to ``{}``.
    private
        Whether this cluster configuration is private or public. Defaults to ``False``

    See Also
    --------
    dask.utils.parse_bytes
    """
    with Cloud() as cloud:
        return cloud.create_cluster_configuration(
            name=name,
            software=software,
            account=account,
            worker_cpu=worker_cpu,
            worker_gpu=worker_gpu,
            worker_memory=worker_memory,
            worker_class=worker_class,
            worker_options=worker_options,
            scheduler_cpu=scheduler_cpu,
            scheduler_memory=scheduler_memory,
            scheduler_class=scheduler_class,
            scheduler_options=scheduler_options,
            private=private,
        )


@list_docstring
def list_cluster_configurations(account=None):
    with Cloud() as cloud:
        return cloud.list_cluster_configurations(account=account)


@delete_docstring
def delete_cluster_configuration(name):
    with Cloud() as cloud:
        return cloud.delete_cluster_configuration(name=name)


def create_cluster(
    name: str = None,
    *,
    configuration: str,
    software: str = None,
    worker_cpu: int = None,
    worker_gpu: int = None,
    worker_memory: str = None,
    worker_class: str = None,
    worker_options: dict = None,
    scheduler_cpu: int = None,
    scheduler_memory: str = None,
    scheduler_class: str = None,
    scheduler_options: dict = None,
    account: str = None,
    workers: int = 0,
    backend_options: Optional[Dict] = None,
    log_output=sys.stdout,
) -> int:
    """Create a cluster
    Parameters
    ---------
    name
        Name of cluster.
    configuration
        Identifier of the cluster configuration to use, in the format (<account>/)<name>. If the configuration
        is owned by the same account as that passed into "account", the (<account>/) prefix is optional.
        For example, suppose your account is "wondercorp", but your friends at "friendlycorp" have a configuration
        named "xgboost" that you want to use; you can specify this with "friendlycorp/xgboost". If you simply
        entered "xgboost", this is shorthand for "wondercorp/xgboost".
    software
        Identifier of the software environment to use, in the format (<account>/)<name>. If the software environment
        is owned by the same account as that passed into "account", the (<account>/) prefix is optional.

        For example, suppose your account is "wondercorp", but your friends at "friendlycorp" have an environment
        named "xgboost" that you want to use; you can specify this with "friendlycorp/xgboost". If you simply
        entered "xgboost", this is shorthand for "wondercorp/xgboost".

        The "name" portion of (<account>/)<name> can only contain ASCII letters, hyphens and underscores.
    worker_cpu
        Number of CPUs allocated for each worker. Defaults to 2.
    worker_gpu
        Number of GPUs allocated for each worker. Defaults to 0 (no GPU support). Note that this will _always_
        allocate GPU-enabled workers, so is expensive.
    worker_memory
        Amount of memory to allocate for each worker. Defaults to 8 GiB.
    worker_class
        Worker class to use. Defaults to "dask.distributed.Nanny".
    worker_options
        Mapping with keyword arguments to pass to ``worker_class``. Defaults to ``{}``.
    scheduler_cpu
        Number of CPUs allocated for the scheduler. Defaults to 1.
    scheduler_memory
        Amount of memory to allocate for the scheduler. Defaults to 4 GiB.
    scheduler_class
        Scheduler class to use. Defaults to "dask.distributed.Scheduler".
    scheduler_options
        Mapping with keyword arguments to pass to ``scheduler_class``. Defaults to ``{}``.
    account
        Name of the Coiled account to create the cluster in.
        If not provided, will default to ``Cloud.default_account``.
    workers
        Number of workers we to launch.
    backend_options
        Dictionary of backend specific options (e.g. ``{'region': 'us-east-2'}``). Any options
        specified with this keyword argument will take precedence over those stored in the
        ``coiled.backend-options`` cofiguration value.
    See Also
    --------
    coiled.Cluster
    """
    # TODO cleanup repetition of explaining a configuration identifier (see docstring for
    # creating software_environments)
    warnings.warn(
        "Please use coiled.Cluster() for creating clusters instead of coiled.create_cluster()."
        "coiled.Cluster() offers more control over the cluster you create and is the recommended approach."
    )
    with Cloud(account=account) as cloud:
        return cloud.create_cluster(
            name=name,
            configuration=configuration,
            software=software,
            worker_cpu=worker_cpu,
            worker_gpu=worker_gpu,
            worker_memory=worker_memory,
            worker_class=worker_class,
            worker_options=worker_options,
            scheduler_cpu=scheduler_cpu,
            scheduler_memory=scheduler_memory,
            scheduler_class=scheduler_class,
            scheduler_options=scheduler_options,
            account=account,
            workers=workers,
            backend_options=backend_options,
            log_output=log_output,
        )


@list_docstring
def list_clusters(account=None):
    with Cloud() as cloud:
        return cloud.list_clusters(account=account)


@delete_docstring
def delete_cluster(name: str, account: str = None):
    with Cloud() as cloud:
        cluster_id = cloud.get_cluster_by_name(name=name, account=account)
        if cluster_id is not None:
            return cloud.delete_cluster(cluster_id=cluster_id, account=account)


def cluster_logs(name: str, account: str = None) -> Logs:
    """Retrieve logs from a Coiled cluster.

    Parameters
    ----------
    name
        Cluster name

    account
        The account in which the cluster is running

    Returns
    -------
    logs
        The logs from the cluster.
    """
    with Cloud() as cloud:
        cluster_id = cloud.get_cluster_by_name(name=name, account=account)
        if cluster_id is not None:
            return cloud.cluster_logs(cluster_id=cluster_id, account=account)


@experimental
def create_job_configuration(
    name: str,
    command: List[str],
    software: str,
    *,
    account: str = None,
    cpu: int = 1,
    gpu: int = 0,
    memory: str = "4 GiB",
    ports: List = None,
    files: Union[str, List[str]] = None,
    description: Optional[str] = None,
) -> None:
    """Create a job configuration

    Parameters
    ----------
    name
        Name of the job configuration
        Optionally prefixed with an account name like "myaccount/myname"
    command:
        Command to run this job. Defaults to None.
    software
        Identifier of the software environment to use, in the format (<account>/)<name>. If the software environment
        is owned by the same account as that passed into "account", the (<account>/) prefix is optional.

        For example, suppose your account is "wondercorp", but your friends at "friendlycorp" have an environment
        named "xgboost" that you want to use; you can specify this with "friendlycorp/xgboost". If you simply
        entered "xgboost", this is shorthand for "wondercorp/xgboost".
    account
        The coiled account in which to create the configuration.
    cpu
        Number of CPUs allocated for this job. Defaults to 1.
    gpu
        Number of GPUs allocated for this job. Defaults to 0.
    memory
        Ammount of memory allocated for this job. Defaults to 4 GiB.
    ports
        List of ports to expose. Defaults to None.
    files
        List of local files to upload.
    description
        Description for the job.
    """
    with Cloud() as cloud:
        return cloud.create_job_configuration(
            name=name,
            command=command,
            software=software,
            account=account,
            cpu=cpu,
            gpu=gpu,
            memory=memory,
            ports=ports,
            files=files,
            description=description,
        )


@experimental
def start_job(
    configuration: str,
    account: str = None,
    backend_options: Optional[Dict] = None,
    log_output=sys.stdout,
):
    """Start a job

    Parameters
    ----------
    configuration
        Name of the job configuration to create the job from.
    account
        Name of Coiled account to use. If not provided, will
        default to the user account for the ``cloud`` object being used.
    backend_options
        Dictionary of backend specific options (e.g. ``{'region': 'us-east-2'}``). Any options
        specified with this keyword argument will take precedence over those stored in the
        ``coiled.backend-options`` cofiguration value
    log_output
        Stream to output logs to. Defaults to ``sys.stdout``.
    """
    with Cloud(account=account) as cloud:
        return cloud.start_job(
            configuration=configuration,
            account=account,
            backend_options=backend_options,
            log_output=log_output,
        )


@experimental
def stop_job(name: str):
    """Stop a running job

    Parameters
    ----------
    name
        Name of job to stop.

        You can get a list of running jobs and their names by using the
        command ``coiled.list_jobs()``
    """
    with Cloud() as cloud:
        return cloud.stop_job(name=name)


@experimental
@list_docstring
def list_job_configurations(account=None):
    with Cloud(account=account) as cloud:
        return cloud.list_job_configurations(account=account)


@experimental
@delete_docstring
def delete_job_configuration(name):
    with Cloud() as cloud:
        return cloud.delete_job_configuration(name=name)


@experimental
@list_docstring
def list_jobs(account=None):
    with Cloud(account=account) as cloud:
        return cloud.list_jobs(account=account)


@experimental
def job_logs(name: str, account: str = None) -> Logs:
    """Retrieve logs from a Coiled job.

    Parameters
    ----------
    name
        Job name

    account
        The account in which the job is run

    Returns
    -------
    logs
        Coiled job logs
    """
    with Cloud() as cloud:
        job_id = cloud.get_job_by_name(name=name, account=account)
        if job_id is not None:
            return cloud.job_logs(job_id=job_id, account=account)


@experimental
def create_notebook(
    name,
    *,
    container="coiled/notebook:latest",
    conda=None,
    pip=None,
    post_build=None,
    cpu: int = 1,
    gpu: int = 0,
    memory: str = "4 GiB",
    files=None,
    command=("/bin/bash", "start.sh", "jupyter", "lab"),
    ports=(8888,),
    description=None,
):
    """Create a notebook

    This allows you to create a hosted notebook which is runnable on https://cloud.coiled.io.

    Parameters
    ---------
    name
        Name of the notebook.
    container
        Docker image to use for the notebook's software environment.
        Defaults to ``coiled/notebook:latest``. Note that when using a non-default
        container, you should check whether the default ``command`` is compatible
        with the container being used and, if not, update the ``command`` such that
        it launches a Jupyter session within the container.
    conda
        Specification for packages to install into the notebook's software environment using conda.
        Can be a list of packages, a dictionary, or a path to a conda environment YAML file.
    pip
        Packages to install into the notebook's software environment using pip.
        Can be a list of packages or a path to a pip requirements file.
    post_build
        List of commands or path to a local executable script to run after pip and conda packages
        have been installed.
    cpu
        Number of CPUs allocated for the notebook session. Defaults to 1.
    gpu
        Number of GPUs allocated for the notebook session. Defaults to 0 (no GPU support).
    memory
        Amount of memory to allocated for the notebook session. Defaults to 4 GiB.
    files
        List of local files to upload.
    command
        Command to run. If not specified, defaults to running JupyterLab.
    ports
        List of ports to expose. If not specified, defaults to ``(8888,)``
    description
        Description for notebook.
    """

    with Cloud() as cloud:

        # Create software environment for notebook
        name_software = name + "-notebook"
        cloud.create_software_environment(
            name=name_software,
            container=container,
            conda=conda,
            pip=pip,
            post_build=post_build,
        )

        # Create job configuration for notebook
        cloud.create_job_configuration(
            name=name,
            software=name_software,
            cpu=cpu,
            gpu=gpu,
            memory=memory,
            command=command,
            files=files,
            ports=ports,
            description=description,
        )


def cluster_cost_estimate(
    n_workers: int = 4,
    configuration: str = None,
    worker_cpu: int = None,
    worker_gpu: int = None,
    worker_memory: Union[str, int] = None,
    scheduler_cpu: int = None,
    scheduler_memory: Union[str, int] = None,
    backend_options: Optional[Dict] = None,
) -> str:
    """Estimate the cluster hourly cost

    Parameters
    ----------
    n_workers
        Number of workers in this cluster. Defaults to 4.
    configuration
        Name of cluster configuration to create cluster from.
        If not specified, defaults to ``coiled/default`` for the
        current Python version.
    worker_cpu
        Number of CPUs allocated for each worker. Defaults to 1.
    worker_gpu
        Number of GPUs allocated for each worker. Defaults to 0 (no GPU support). Note that this will _always_
        allocate GPU-enabled workers, so is expensive.
    worker_memory
        Amount of memory to allocate for each worker. Defaults to 4 GiB.
    scheduler_cpu
        Number of CPUs allocated for the scheduler. Defaults to 1.
    scheduler_memory
        Amount of memory to allocate for the scheduler. Defaults to 4 GiB.
    backend_options
        Dictionary of backend specific options (e.g. ``{'region': 'us-east-2'}``). Any options
        specified with this keyword argument will take precedence over those stored in the
        ``coiled.backend-options`` cofiguration value.

    See Also
    --------
    dask.utils.parse_bytes
    """
    if configuration is None:
        v = "".join(map(str, sys.version_info[:2]))
        configuration = f"coiled/default-py{v}"
    with Cloud() as cloud:
        return cloud.cluster_cost_estimate(
            n_workers=n_workers,
            configuration=configuration,
            worker_cpu=worker_cpu,
            worker_gpu=worker_gpu,
            worker_memory=worker_memory,
            scheduler_cpu=scheduler_cpu,
            scheduler_memory=scheduler_memory,
            backend_options=backend_options,
        )


@overload
def list_core_usage(json: Literal[True], account: str = None) -> dict:
    ...


@overload
def list_core_usage(json: Literal[False] = False, account: str = None) -> None:
    ...


def list_core_usage(json: bool = False, account: str = None) -> Union[dict, None]:
    """Get a list of used cores.

    Returns a table that shows the limit of cores that the user can use
    and a breakdown of the core usage split up between account, user, clusters
    and jobs.

    Parameters
    ----------
    account
        Name of the Coiled account to list core usage. If not provided,
        will use the coiled.account configuration value.
    json
        If set to ``True``, it will return this list in json format instead of
        a table.
    """
    with Cloud() as cloud:
        return cloud.list_core_usage(json=json, account=account)


def get_notifications(
    json: bool = False,
    account: str = None,
    limit: int = 100,
) -> Union[List[dict], None]:
    """Get a list of all recent notification."""
    with Cloud() as cloud:
        return cloud.get_notifications(json=json, account=account, limit=limit)


@overload
def list_local_versions(json: Literal[False] = False) -> None:
    ...


@overload
def list_local_versions(json: Literal[True]) -> dict:
    ...


def list_local_versions(json: bool = False) -> Optional[dict]:
    """Get information about local versions.

    Returns the versions of Python, Coiled, Dask and Distributed that
    are installed locally. This information could be useful when
    troubleshooting issues.

    Parameters
    ----------
    json
        If set to ``True``, it will return this list in json format instead of a
        table.
    """
    with Cloud() as cloud:
        return cloud.list_local_versions(json=json)


def diagnostics(account: str = None) -> dict:
    """Run a diagnose check aimed to help support with any issues.

    This command will call others to dump information that could help
    in troubleshooting issues. This command will return a json that will
    make it easier for you to share with the Coiled support team if needed.

    Parameters
    ----------
    account
        Name of the Coiled account to list core usage. If not provided,
        will use the coiled.account configuration value.
    """
    console = rich_console()
    with console.status("Gathering diagnostics..."):
        with Cloud() as cloud:
            data = {}

            health_check = cloud.health_check()
            status = health_check.get("status", "Issues found")

            data["health_check"] = health_check
            console.print(f"Performing health check.... Status: {status}")
            time.sleep(0.5)

            console.print("Gathering information about local environment...")
            local_versions = cloud.list_local_versions(json=True)
            data["local_versions"] = local_versions
            time.sleep(0.5)

            configuration = dask.config.config
            configuration["coiled"]["token"] = "hidden"
            data["coiled_configuration"] = configuration
            time.sleep(0.5)

            console.print("Getting user information...")
            user_info = cloud.list_user_information()
            data["user_information"] = user_info
            time.sleep(0.5)

            usage = cloud.list_core_usage(json=True, account=account)
            data["core_usage"] = usage
            time.sleep(0.5)

            return data


def list_user_information() -> dict:
    """List information about your user.

    This command will give you more information about your account,
    which teams you are part of and any limits that your account might
    have.
    """
    with Cloud() as cloud:
        cloud.list_user_information()
        return cloud.list_user_information()


@experimental
@contextmanager
def performance_report(
    filename="dask-report.html", private=False, account=None
) -> Generator[Dict, None, None]:
    """Generates a static performance report and saves it to Coiled Cloud

    This context manager lightly wraps Dask's performance_report. It generates a static performance
    report and uploads it to Coiled Cloud. It returns a dict that includes the url of the report as well as
    other useful information. Note each user is limited to 5 hosted reports with each a maximum file size of 10mb.

    Parameters
    ----------
    filename
        The file name of the performance report file.

    private
        If set to ``True``, the uploaded performance report is only accessible via signed url with 60 minute lifetime.

    account
        Associated the account which user wishes to upload to. If not specified, current / default
        account will be utilized.

    """
    # stacklevel= is newer kwarg after version check below
    report_kwargs = {"stacklevel": 3} if DISTRIBUTED_VERSION >= "2021.05.0" else {}

    with dask.distributed.performance_report(filename=filename, **report_kwargs):
        pass

    statinfo = os.stat(filename)
    if statinfo.st_size >= 1048576 * 10:
        raise ValueError("Report file size greater than 10mb limit")

    # At this point Dask has generated a local file with the performance report contents
    with Cloud() as cloud:
        result = cloud.upload_performance_report(
            filename, filename=filename, private=private, account=account
        )
        yield result


@experimental
def list_performance_reports(account=None) -> List[Dict]:
    """List performance reports stored on Coiled Cloud

    Returns a list of dicts that contain information about Coiled Cloud hosted performance reports

    Parameters
    ----------

    account
        Associated account for which the user wishes to get reports from. If not specified, current / default
        account will be utilized.

    """
    with Cloud() as cloud:
        result = cloud.list_performance_reports(account=account)
        return result
