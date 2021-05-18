# ##### BEGIN GPL LICENSE BLOCK #####
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


import logging
from deepdiff import DeepDiff, Delta
import json
import io
from uuid import uuid4
import sys
import zmq
import math
import logging

try:
    import _pickle as pickle
except ImportError:
    import pickle

import traceback

from .constants import (
    ADDED, COMMITED,
    FETCHED, UP, MODIFIED, DIFF_BINARY, DIFF_JSON)
from .exception import (NetworkFrameError, DataError,
                        StateError, UnsupportedTypeError)
from .utils import get_state_str

CHUNK_SIZE = 2500000000


class DataTranslationProtocol(object):
    """
    Manage the data types implementations.

    """

    def __init__(self):
        self.supported_types = []

    def register_type(
            self,
            source_type,
            implementation,
            timer=0,
            automatic=False,
            supported_types=False,
            check_common=False):
        """
        Register a new replicated datatype implementation
        """
        self.supported_types.append((source_type,
                                     implementation,
                                     timer,
                                     automatic,
                                     check_common))

    def match_type_by_instance(self, data):
        """
        Find corresponding type to the given datablock
        """
        for stypes, implementation, time, auto, check_common in self.supported_types:
            if issubclass(type(data), stypes):
                return implementation
        logging.error(f"{type(data)} not supported for replication, \
                         check supported types in the documentation")
        raise UnsupportedTypeError(type(data))

    def match_type_by_name(self, type_name):
        for stypes, implementation, time, auto, check_common in self.supported_types:
            if type_name == implementation.__name__:
                return implementation
        logging.error(f"{type_name} not supported for replication, \
                         check supported types in the documentation")
        raise UnsupportedTypeError(type_name)

    def get_implementation_from_object(self, data):
        return self.match_type_by_instance(data)

    def get_implementation_from_net(self, type_name):
        """
        Re_construct a new replicated value from serialized data
        """
        return self.match_type_by_name(type_name)


class ReplicatedDatablock(object):
    """
    Datablock definition that handle object replication logic.
    PUSH: send the object over the wire
    STORE: register the object on the given replication graph
    LOAD: apply loaded changes by reference on the local copy
    DUMP: get local changes

    """

    __slots__ = [
        'uuid',             # uuid used as key      (string)
        'data',             # dcc data ref          (DCC type)
        'instance',         # raw data              (json)
        'str_type',         # data type name        (string)
        'dependencies',     # dependencies array    (string)
        'owner',            # Data owner            (string)
        'buffer',           # Serialized local buffer (bytes)
        'state',            # Node state            (int)
        'sender',           # Node sender origin (client uuid)
        'delta'
        ]

    is_root = False

    def __init__(
            self,
            owner=None,
            instance=None,
            str_type=None,
            uuid=None,
            data=None,
            bytes=None,
            sender=None,
            dependencies=[]):

        self.uuid = uuid if uuid else str(uuid4())
        self.owner = owner
        self.str_type = str_type if str_type else type(self).__name__
        self.buffer = None
        self.data = {}
        self.instance = None


        if instance:
            self.state = ADDED
            self.instance = instance
        elif data:
            self.data = data
            if type(self) == ReplicatedDatablock:
                self.state = UP
            else:
                self.state = FETCHED
        elif bytes:
            # Server side
            if type(self) == ReplicatedDatablock:
                self.state = UP
                self.str_type = str_type
            else:
                self.state = FETCHED
        self.delta = bytes
        self.dependencies = dependencies
        self.sender = sender
    
    def patch(self, patch):
        self.data = self.data + patch

    def push(self, socket, identity=None, check_data=True, force=False):
        """ Push the node over the given socket as a multipart frame

            :raise NetworkFrameError:
            :raise DataError:
        """

        if self.state == COMMITED or force:
            owner = self.owner.encode()
            key = self.uuid.encode()
            rep_type = self.str_type.encode()
            dependencies = pickle.dumps(self.dependencies, protocol=4)

            # Server to specific Client case
            if identity:
                serialized_data = self.delta
                socket.send(identity, zmq.SNDMORE)
            else: 
                serialized_data = self.buffer.dumps() 

            if not serialized_data or \
                    not dependencies or \
                    not rep_type or \
                    not owner or \
                    not socket.IDENTITY:

                raise NetworkFrameError(f"Trying to push incomplete data: {repr(self)}")

            # First step : send nodes metadata
            socket.send_multipart([key,
                                   owner,
                                   rep_type,
                                   dependencies,
                                   serialized_data])
            self.buffer = None
            self.state = UP
        else:
            logging.debug(f"Nothing to push {self.uuid}")

    @classmethod
    def fetch(cls, socket, factory=None):
        """
        Here we reeceive data from the wire:
            - read data from the socket
            - reconstruct an instance
        """

        frame = socket.recv_multipart(0)

        # identity, uuid, owner, str_type, ck_number, dependencies
        # Load node metadata

        if len(frame) == 6:
            identity = frame.pop(0)

        if len(frame) != 5:
            logging.info(frame[1])
            logging.error(f"Incomplete frame received ({len(frame)})")
            raise NetworkFrameError("Error fetching data")

        uuid = frame[0].decode()
        owner = frame[1].decode()
        str_type = frame[2].decode()
        dependencies = pickle.loads(frame[3])
        serialized_data = frame[4]
        dependencies = dependencies if dependencies else None


        instance = None

        # Server side replication
        if factory is None:
            instance = ReplicatedDatablock(owner=owner,
                                           uuid=uuid,
                                           dependencies=dependencies,
                                           sender=identity,
                                           str_type=str_type,
                                           bytes=serialized_data)

        # Client side replication
        else:
            implementation = factory.get_implementation_from_net(str_type)

            instance = implementation(owner=owner,
                                      uuid=uuid,
                                      dependencies=dependencies,
                                      bytes=serialized_data)

        return instance

    def is_valid(self):
        raise NotImplementedError()

    def _construct(self, data=None):
        """Construct a new instance of the target object,
        assign our instance to this instance
        """
        raise NotImplementedError()

    def remove_instance(self):
        raise NotImplementedError()

    def resolve(self):
        pass

    def _deserialize(self, data):
        """
        BUFFER -> JSON
        """
        return pickle.loads(data)

    def _serialize(self):
        """
        JSON -> BUFFER
        """
        return pickle.dumps(self.data, protocol=4)

    def _dump(self, instance=None):
        """
        DCC -> JSON
        """
        assert(instance)

        return json.dumps(instance)

    def _load(self, data=None, target=None):
        """
        JSON -> DCC
        """
        raise NotImplementedError()

    def check(self, bytes):
        try:
            self._deserialize(bytes)
        except Exception:
            raise DataError(f"Failed to deserialize {self.uuid} data")

    def diff(self, diff_params={}, delta_params={}):
        """Compare stored data to the actual one.

        return True if the versions doesn't match
        """
        new_version = self._dump(instance=self.instance)

        return Delta(DeepDiff(self.data, new_version, cache_size=5000, **diff_params), **delta_params)

    def resolve_deps(self):
        """Return a list of dependencies
        """
        return []

    def add_dependency(self, dependency):
        if not self.dependencies:
            self.dependencies = []
        if dependency not in self.dependencies:
            self.dependencies.append(dependency)

    def __repr__(self):
        return f"- uuid: {self.uuid} \n \
                 - owner: {self.owner} \n \
                 - state: {get_state_str(self.state)} \n \
                 - type: {self.str_type} \n \
                 - data: {self.data if hasattr(self, 'data') else 'Empty'} \n \
                 - deps: {self.dependencies}"


class ReplicatedCommandFactory(object):
    """
    Manage the data types implementations.

    """

    def __init__(self):
        self.supported_types = []

        self.register_type(RepDeleteCommand, RepDeleteCommand)
        self.register_type(RepRightCommand, RepRightCommand)
        self.register_type(RepConfigCommand, RepConfigCommand)
        self.register_type(RepSnapshotCommand, RepSnapshotCommand)
        self.register_type(RepServerSnapshotCommand, RepServerSnapshotCommand)
        self.register_type(RepAuthCommand, RepAuthCommand)
        self.register_type(RepDisconnectCommand, RepDisconnectCommand)
        self.register_type(RepKickCommand, RepKickCommand)
        self.register_type(RepUpdateClientsState, RepUpdateClientsState)
        self.register_type(RepUpdateUserMetadata, RepUpdateUserMetadata)

    def register_type(
            self,
            source_type,
            implementation):
        """
        Register a new replicated datatype implementation
        """
        self.supported_types.append(
            (source_type, implementation))

    def match_type_by_name(self, type_name):
        for stypes, implementation in self.supported_types:
            if type_name == implementation.__name__:
                return implementation
        logging.error(f"{type_name} not supported for replication")

    def get_implementation_from_object(self, data):
        return self.match_type_by_instance(data)

    def get_implementation_from_net(self, type_name):
        """
        Re_construct a new replicated value from serialized data
        """
        return self.match_type_by_name(type_name)


class ReplicatedCommand():
    def __init__(
            self,
            owner=None,
            data=None):
        assert(owner)

        self.owner = owner
        self.data = data
        self.str_type = type(self).__name__

    def push(self, socket):
        """
        Here send data over the wire:
            - _serialize the data
            - send them as a multipart frame thought the given socket
        """
        data = pickle.dumps(self.data, protocol=4)
        owner = self.owner.encode()
        type = self.str_type.encode()

        socket.send_multipart([owner, type, data])

    @classmethod
    def fetch(cls, socket, factory=None):
        """
        Here we reeceive data from the wire:
            - read data from the socket
            - reconstruct an instance
        """

        owner, str_type, data = socket.recv_multipart(0)

        str_type = str_type.decode()
        owner = owner.decode()
        data = pickle.loads(data)

        implementation = factory.get_implementation_from_net(str_type)

        instance = implementation(owner=owner, data=data)
        return instance

    @classmethod
    def server_fetch(cls, socket, factory=None):
        """
        Here we reeceive data from the wire:
            - read data from the socket
            - reconstruct an instance
        """
        instance = None
        frame = socket.recv_multipart(0)

        if len(frame) != 4:
            logging.error(
                f"Malformed command frame received (len: {len(frame)}/4)")
            raise NetworkFrameError("Error fetching command")
        else:
            str_type = frame[2].decode()
            owner = frame[1].decode()
            data = pickle.loads(frame[3])

            implementation = factory.get_implementation_from_net(str_type)

            instance = implementation(owner=owner, data=data)
            instance.sender = frame[0]

        return instance

    def execute(self, graph):
        raise NotImplementedError()


class RepDeleteCommand(ReplicatedCommand):
    def execute(self, graph):
        assert(self.data)

        if graph and self.data in graph.keys():
            # Clean all reference to this node
            for key, value in graph.items():
                if value.dependencies and self.data in value.dependencies:
                    value.dependencies.remove(self.data)
            # Remove the node itself
            del graph[self.data]


class RepRightCommand(ReplicatedCommand):
    def execute(self, graph):
        assert(self.data)

        if graph and self.data['uuid'] in graph.keys():
            graph[self.data['uuid']].owner = self.data['owner']


class RepConfigCommand(ReplicatedCommand):
    pass


class RepSnapshotCommand(ReplicatedCommand):
    pass


class RepServerSnapshotCommand(ReplicatedCommand):
    pass


class RepAuthCommand(ReplicatedCommand):
    pass


class RepDisconnectCommand(ReplicatedCommand):
    pass


class RepKickCommand(ReplicatedCommand):
    pass


class RepUpdateClientsState(ReplicatedCommand):
    pass


class RepUpdateUserMetadata(ReplicatedCommand):
    pass
