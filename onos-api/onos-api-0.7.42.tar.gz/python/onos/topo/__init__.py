# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: onos/topo/config.proto, onos/topo/ran.proto, onos/topo/topo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterator, Dict, List, Optional

import betterproto
import grpclib


class RanEntityKinds(betterproto.Enum):
    E2NODE = 0
    E2CELL = 1


class RanRelationKinds(betterproto.Enum):
    CONTROLS = 0
    CONTAINS = 1
    NEIGHBORS = 2


class EventType(betterproto.Enum):
    NONE = 0
    ADDED = 1
    UPDATED = 2
    REMOVED = 3


class Protocol(betterproto.Enum):
    UNKNOWN_PROTOCOL = 0
    GNMI = 1
    P4RUNTIME = 2
    GNOI = 3
    E2AP = 4


class ConnectivityState(betterproto.Enum):
    UNKNOWN_CONNECTIVITY_STATE = 0
    REACHABLE = 1
    UNREACHABLE = 2


class ChannelState(betterproto.Enum):
    UNKNOWN_CHANNEL_STATE = 0
    CONNECTED = 1
    DISCONNECTED = 2


class ServiceState(betterproto.Enum):
    UNKNOWN_SERVICE_STATE = 0
    AVAILABLE = 1
    UNAVAILABLE = 2
    CONNECTING = 3


class ObjectType(betterproto.Enum):
    UNSPECIFIED = 0
    ENTITY = 1
    RELATION = 2
    KIND = 3


@dataclass(eq=False, repr=False)
class Asset(betterproto.Message):
    """Basic asset information"""

    name: str = betterproto.string_field(1)
    manufacturer: str = betterproto.string_field(2)
    model: str = betterproto.string_field(3)
    serial: str = betterproto.string_field(4)
    asset: str = betterproto.string_field(5)
    sw_version: str = betterproto.string_field(6)
    role: str = betterproto.string_field(8)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Configurable(betterproto.Message):
    """Configurable device aspect"""

    type: str = betterproto.string_field(1)
    address: str = betterproto.string_field(2)
    target: str = betterproto.string_field(3)
    version: str = betterproto.string_field(4)
    timeout: int = betterproto.uint64_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class MastershipState(betterproto.Message):
    """Aspect for tracking device mastership"""

    term: int = betterproto.uint64_field(1)
    node_id: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class TlsOptions(betterproto.Message):
    """TLS connectivity aspect"""

    insecure: bool = betterproto.bool_field(1)
    plain: bool = betterproto.bool_field(2)
    key: str = betterproto.string_field(3)
    ca_cert: str = betterproto.string_field(4)
    cert: str = betterproto.string_field(5)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class AdHoc(betterproto.Message):
    """Aspect for ad-hoc properties"""

    properties: Dict[str, str] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Location(betterproto.Message):
    """Basic asset information"""

    lat: float = betterproto.double_field(1)
    lng: float = betterproto.double_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Coverage(betterproto.Message):
    """Configurable device aspect"""

    height: int = betterproto.int32_field(1)
    arc_width: int = betterproto.int32_field(2)
    azimuth: int = betterproto.int32_field(3)
    tilt: int = betterproto.int32_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class E2Node(betterproto.Message):
    """Aspect for tracking device mastership"""

    service_models: Dict[str, "ServiceModelInfo"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class E2Cell(betterproto.Message):
    """TLS connectivity aspect"""

    cid: str = betterproto.string_field(1)
    antenna_count: int = betterproto.uint32_field(2)
    earfcn: int = betterproto.uint32_field(3)
    cell_type: str = betterproto.string_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ServiceModelInfo(betterproto.Message):
    """Aspect for ad-hoc properties"""

    oid: str = betterproto.string_field(1)
    name: str = betterproto.string_field(2)
    ran_functions: List[
        "betterproto_lib_google_protobuf.Any"
    ] = betterproto.message_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class RcRanFunction(betterproto.Message):
    id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class KpmRanFunction(betterproto.Message):
    id: str = betterproto.string_field(1)
    measurements: List["KpmMeasurement"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class KpmMeasurement(betterproto.Message):
    id: str = betterproto.string_field(1)
    name: str = betterproto.string_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Event(betterproto.Message):
    """Basic asset information"""

    type: "EventType" = betterproto.enum_field(1)
    object: "Object" = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CreateRequest(betterproto.Message):
    """Configurable device aspect"""

    object: "Object" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class CreateResponse(betterproto.Message):
    """Aspect for tracking device mastership"""

    object: "Object" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetRequest(betterproto.Message):
    """TLS connectivity aspect"""

    id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class GetResponse(betterproto.Message):
    """Aspect for ad-hoc properties"""

    object: "Object" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class UpdateRequest(betterproto.Message):
    object: "Object" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class UpdateResponse(betterproto.Message):
    object: "Object" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DeleteRequest(betterproto.Message):
    id: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DeleteResponse(betterproto.Message):
    pass

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Filter(betterproto.Message):
    equal: "EqualFilter" = betterproto.message_field(1, group="filter")
    not_: "NotFilter" = betterproto.message_field(2, group="filter")
    in_: "InFilter" = betterproto.message_field(3, group="filter")
    key: str = betterproto.string_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class EqualFilter(betterproto.Message):
    value: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class InFilter(betterproto.Message):
    values: List[str] = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class NotFilter(betterproto.Message):
    inner: "Filter" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Filters(betterproto.Message):
    kind_filters: List["Filter"] = betterproto.message_field(1)
    label_filters: List["Filter"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListRequest(betterproto.Message):
    filters: "Filters" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ListResponse(betterproto.Message):
    objects: List["Object"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchRequest(betterproto.Message):
    filters: "Filters" = betterproto.message_field(1)
    noreplay: bool = betterproto.bool_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class WatchResponse(betterproto.Message):
    event: "Event" = betterproto.message_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Object(betterproto.Message):
    id: str = betterproto.string_field(1)
    revision: int = betterproto.uint64_field(2)
    type: "ObjectType" = betterproto.enum_field(3)
    entity: "Entity" = betterproto.message_field(4, group="obj")
    relation: "Relation" = betterproto.message_field(5, group="obj")
    kind: "Kind" = betterproto.message_field(6, group="obj")
    aspects: Dict[str, "betterproto_lib_google_protobuf.Any"] = betterproto.map_field(
        7, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    labels: Dict[str, str] = betterproto.map_field(
        8, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Entity(betterproto.Message):
    kind_id: str = betterproto.string_field(1)
    protocols: List["ProtocolState"] = betterproto.message_field(2)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Relation(betterproto.Message):
    kind_id: str = betterproto.string_field(1)
    src_entity_id: str = betterproto.string_field(2)
    tgt_entity_id: str = betterproto.string_field(3)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class Kind(betterproto.Message):
    name: str = betterproto.string_field(1)

    def __post_init__(self) -> None:
        super().__post_init__()


@dataclass(eq=False, repr=False)
class ProtocolState(betterproto.Message):
    protocol: "Protocol" = betterproto.enum_field(1)
    connectivity_state: "ConnectivityState" = betterproto.enum_field(2)
    channel_state: "ChannelState" = betterproto.enum_field(3)
    service_state: "ServiceState" = betterproto.enum_field(4)

    def __post_init__(self) -> None:
        super().__post_init__()


class TopoStub(betterproto.ServiceStub):
    async def create(self, *, object: "Object" = None) -> "CreateResponse":

        request = CreateRequest()
        if object is not None:
            request.object = object

        return await self._unary_unary(
            "/onos.topo.Topo/Create", request, CreateResponse
        )

    async def get(self, *, id: str = "") -> "GetResponse":

        request = GetRequest()
        request.id = id

        return await self._unary_unary("/onos.topo.Topo/Get", request, GetResponse)

    async def update(self, *, object: "Object" = None) -> "UpdateResponse":

        request = UpdateRequest()
        if object is not None:
            request.object = object

        return await self._unary_unary(
            "/onos.topo.Topo/Update", request, UpdateResponse
        )

    async def delete(self, *, id: str = "") -> "DeleteResponse":

        request = DeleteRequest()
        request.id = id

        return await self._unary_unary(
            "/onos.topo.Topo/Delete", request, DeleteResponse
        )

    async def list(self, *, filters: "Filters" = None) -> "ListResponse":

        request = ListRequest()
        if filters is not None:
            request.filters = filters

        return await self._unary_unary("/onos.topo.Topo/List", request, ListResponse)

    async def watch(
        self, *, filters: "Filters" = None, noreplay: bool = False
    ) -> AsyncIterator["WatchResponse"]:

        request = WatchRequest()
        if filters is not None:
            request.filters = filters
        request.noreplay = noreplay

        async for response in self._unary_stream(
            "/onos.topo.Topo/Watch",
            request,
            WatchResponse,
        ):
            yield response


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
