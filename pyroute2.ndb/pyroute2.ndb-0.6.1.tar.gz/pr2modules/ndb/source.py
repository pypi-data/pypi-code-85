'''

Local RTNL
----------

Local RTNL source is a simple `IPRoute` instance. By default NDB
starts with one local RTNL source names `localhost`::

    >>> ndb = NDB()
    >>> ndb.sources.details()
    {'kind': u'local', u'nlm_generator': 1, 'target': u'localhost'}
    >>> ndb.sources['localhost']
    [running] <IPRoute {'nlm_generator': 1}>

The `localhost` RTNL source starts an additional async cache thread.
The `nlm_generator` option means that instead of collections the
`IPRoute` object returns generators, so `IPRoute` responses will not
consume memory regardless of the RTNL objects number::

    >>> ndb.sources['localhost'].nl.link('dump')
    <generator object _match at 0x7fa444961e10>

See also: :ref:`iproute`

Network namespaces
------------------

There are two ways to connect additional sources to an NDB instance.
One is to specify sources when creating an NDB object::

    ndb = NDB(sources=[{'target': 'localhost'}, {'netns': 'test01'}])

Another way is to call `ndb.sources.add()` method::

    ndb.sources.add(netns='test01')

This syntax: `{target': 'localhost'}` and `{'netns': 'test01'}` is the
short form. The full form would be::

    {'target': 'localhost', # the label for the DB
     'kind': 'local',       # use IPRoute class to start the source
     'nlm_generator': 1}    #

    {'target': 'test01',    # the label
     'kind': 'netns',       # use NetNS class
     'netns': 'test01'}     #

See also: :ref:`netns`

Remote systems
--------------

It is possible also to connect to remote systems using SSH. In order to
use this kind of sources it is required to install the
`mitogen <https://github.com/dw/mitogen>`_ module. The `remote` kind
of sources uses the `RemoteIPRoute` class. The short form::

    ndb.sources.add(hostname='worker1.example.com')


In some more extended form::

    ndb.sources.add(**{'target': 'worker1.example.com',
                       'kind': 'remote',
                       'hostname': 'worker1.example.com',
                       'username': 'jenkins',
                       'check_host_keys': False})

See also: :ref:`remote`
'''
import sys
import time
import uuid
import queue
import errno
import socket
import struct
import threading
from pr2modules.iproute.linux import IPRoute
from pr2modules.iproute.remote import RemoteIPRoute
from pr2modules.netlink.nlsocket import NetlinkMixin
from pr2modules.netlink.exceptions import NetlinkError
from pr2modules.netlink.rtnl.ifinfmsg import ifinfmsg
from .events import (ShutdownException,
                     State)
from .messages import (cmsg_event,
                       cmsg_failed,
                       cmsg_sstart)
if sys.platform.startswith('linux'):
    from pr2modules import netns
    from pr2modules.netns.manager import NetNSManager
    from pr2modules.nslink.nslink import NetNS
else:
    NetNS = None
    NetNSManager = None

SOURCE_FAIL_PAUSE = 5


class SourceProxy(object):

    def __init__(self, ndb, target):
        self.ndb = ndb
        self.events = queue.Queue()
        self.target = target

    def api(self, name, *argv, **kwarg):
        call_id = str(uuid.uuid4().hex)
        self.ndb._call_registry[call_id] = event = threading.Event()
        event.clear()
        (self
         .ndb
         .messenger
         .emit({'type': 'api',
                'target': self.target,
                'call_id': call_id,
                'name': name,
                'argv': argv,
                'kwarg': kwarg}))

        event.wait()
        response = self.ndb._call_registry.pop(call_id)
        if 'return' in response:
            return response['return']
        elif 'exception' in response:
            raise response['exception']


class Source(dict):
    '''
    The RNTL source. The source that is used to init the object
    must comply to IPRoute API, must support the async_cache. If
    the source starts additional threads, they must be joined
    in the source.close()
    '''
    table_alias = 'src'
    dump = None
    dump_header = None
    summary = None
    summary_header = None
    view = None
    table = 'sources'
    vmap = {'local': IPRoute,
            'netns': NetNS,
            'remote': RemoteIPRoute,
            'nsmanager': NetNSManager}

    def __init__(self, ndb, **spec):
        self.th = None
        self.nl = None
        self.ndb = ndb
        self.evq = self.ndb._event_queue
        # the target id -- just in case
        self.target = spec['target']
        self.kind = spec.pop('kind', 'local')
        self.persistent = spec.pop('persistent', True)
        self.event = spec.pop('event')
        # RTNL API
        self.nl_prime = self.vmap[self.kind]
        self.nl_kwarg = spec
        #
        if self.ndb.messenger is not None:
            self.ndb.messenger.targets.add(self.target)
        #
        self.shutdown = threading.Event()
        self.started = threading.Event()
        self.lock = threading.RLock()
        self.shutdown_lock = threading.RLock()
        self.started.clear()
        self.log = ndb.log.channel('sources.%s' % self.target)
        self.state = State(log=self.log)
        self.state.set('init')
        self.ndb.schema.execute('''
                                INSERT INTO sources (f_target, f_kind)
                                VALUES (%s, %s)
                                ''' % (self.ndb.schema.plch,
                                       self.ndb.schema.plch),
                                (self.target, self.kind))
        for key, value in spec.items():
            vtype = 'int' if isinstance(value, int) else 'str'
            self.ndb.schema.execute('''
                                    INSERT INTO sources_options
                                    (f_target, f_name, f_type, f_value)
                                    VALUES (%s, %s, %s, %s)
                                    ''' % (self.ndb.schema.plch,
                                           self.ndb.schema.plch,
                                           self.ndb.schema.plch,
                                           self.ndb.schema.plch),
                                    (self.target, key, vtype, value))

        self.load_sql()

    @classmethod
    def defaults(cls, spec):
        ret = dict(spec)
        defaults = {}
        if 'hostname' in spec:
            defaults['kind'] = 'remote'
            defaults['protocol'] = 'ssh'
            defaults['target'] = spec['hostname']
        if 'netns' in spec:
            defaults['kind'] = 'netns'
            defaults['target'] = spec['netns']
            ret['netns'] = netns._get_netnspath(spec['netns'])
        for key in defaults:
            if key not in ret:
                ret[key] = defaults[key]
        return ret

    def __repr__(self):
        if isinstance(self.nl_prime, NetlinkMixin):
            name = self.nl_prime.__class__.__name__
        elif isinstance(self.nl_prime, type):
            name = self.nl_prime.__name__

        return '[%s] <%s %s>' % (self.state.get(), name, self.nl_kwarg)

    @classmethod
    def nla2name(cls, name):
        return name

    @classmethod
    def name2nla(cls, name):
        return name

    @classmethod
    def summary(cls, view):
        yield ('state', 'name', 'spec')
        for key in view.keys():
            yield (view[key].state.get(), key, '%s' % (view[key].nl_kwarg, ))

    def api(self, name, *argv, **kwarg):
        for _ in range(100):  # FIXME make a constant
            with self.lock:
                try:
                    return getattr(self.nl, name)(*argv, **kwarg)
                except (NetlinkError,
                        AttributeError,
                        ValueError,
                        KeyError,
                        TypeError,
                        socket.error,
                        struct.error):
                    raise
                except Exception as e:
                    # probably the source is restarting
                    self.log.debug('source api error: %s' % e)
                    time.sleep(1)
        raise RuntimeError('api call failed')

    def fake_zero_if(self):
        url = 'https://github.com/svinota/pyroute2/issues/737'
        zero_if = ifinfmsg()
        zero_if['index'] = 0
        zero_if['state'] = 'up'
        zero_if['flags'] = 1
        zero_if['header']['flags'] = 2
        zero_if['header']['type'] = 16
        zero_if['header']['target'] = self.target
        zero_if['event'] = 'RTM_NEWLINK'
        zero_if['attrs'] = [('IFLA_IFNAME', url),
                            ('IFLA_ADDRESS', '00:00:00:00:00:00')]
        zero_if.encode()
        self.evq.put([zero_if, ])

    def receiver(self):
        #
        # The source thread routine -- get events from the
        # channel and forward them into the common event queue
        #
        # The routine exists on an event with error code == 104
        #
        stop = False
        while not stop:
            with self.lock:
                if self.shutdown.is_set():
                    break

                if self.nl is not None:
                    try:
                        self.nl.close(code=0)
                    except Exception as e:
                        self.log.warning('source restart: %s' % e)
                try:
                    self.state.set('connecting')
                    if isinstance(self.nl_prime, type):
                        spec = {}
                        spec.update(self.nl_kwarg)
                        if self.kind in ('nsmanager', ):
                            spec['libc'] = self.ndb.libc
                        self.nl = self.nl_prime(**spec)
                    else:
                        raise TypeError('source channel not supported')
                    self.state.set('loading')
                    #
                    self.nl.bind(async_cache=True, clone_socket=True)
                    #
                    # Initial load -- enqueue the data
                    #
                    self.ndb.schema.allow_read(False)
                    try:
                        self.ndb.schema.flush(self.target)
                        if self.kind in ('local', 'netns', 'remote'):
                            self.fake_zero_if()
                        self.evq.put(self.nl.dump())
                    finally:
                        self.ndb.schema.allow_read(True)
                    self.started.set()
                    self.shutdown.clear()
                    self.state.set('running')
                    if self.event is not None:
                        self.evq.put((cmsg_event(self.target, self.event), ))
                    else:
                        self.evq.put((cmsg_sstart(self.target), ))
                except Exception as e:
                    self.started.set()
                    self.state.set('failed')
                    self.log.error('source error: %s %s' % (type(e), e))
                    try:
                        self.evq.put((cmsg_failed(self.target), ))
                    except ShutdownException:
                        stop = True
                        break
                    if self.persistent:
                        self.log.debug('sleeping before restart')
                        self.shutdown.wait(SOURCE_FAIL_PAUSE)
                        if self.shutdown.is_set():
                            self.log.debug('source shutdown')
                            stop = True
                            break
                    else:
                        self.event.set()
                        return
                    continue

            while not stop:
                try:
                    msg = tuple(self.nl.get())
                except Exception as e:
                    self.log.error('source error: %s %s' % (type(e), e))
                    msg = None
                    if not self.persistent:
                        stop = True
                    break

                code = 0
                if msg and msg[0]['header']['error']:
                    code = msg[0]['header']['error'].code

                if msg is None or code == errno.ECONNRESET:
                    stop = True
                    break

                self.ndb.schema._allow_write.wait()
                try:
                    self.evq.put(msg)
                except ShutdownException:
                    stop = True
                    break

        # thus we make sure that all the events from
        # this source are consumed by the main loop
        # in __dbm__() routine
        try:
            self.sync()
            self.log.debug('flush DB for the target')
            self.ndb.schema.flush(self.target)
        except ShutdownException:
            self.log.debug('shutdown handled by the main thread')
            pass
        self.state.set('stopped')

    def sync(self):
        self.log.debug('sync')
        sync = threading.Event()
        self.evq.put((cmsg_event(self.target, sync), ))
        sync.wait()

    def start(self):

        #
        # Start source thread
        with self.lock:
            self.log.debug('starting the source')
            if (self.th is not None) and self.th.is_alive():
                raise RuntimeError('source is running')

            self.th = (threading
                       .Thread(target=self.receiver,
                               name='NDB event source: %s' % (self.target)))
            self.th.start()
            return self

    def close(self, code=errno.ECONNRESET, sync=True):
        with self.shutdown_lock:
            if self.shutdown.is_set():
                self.log.debug('already stopped')
                return
            self.log.debug('source shutdown')
            self.shutdown.set()
            if self.nl is not None:
                try:
                    self.nl.close(code=code)
                except Exception as e:
                    self.log.error('source close: %s' % e)
        if sync:
            if self.th is not None:
                self.th.join()
                self.th = None
            else:
                self.log.debug('receiver thread missing')

    def restart(self, reason='unknown'):
        with self.lock:
            with self.shutdown_lock:
                self.log.debug('restarting the source, reason <%s>' % (reason))
                self.started.clear()
                self.ndb.schema.allow_read(False)
                try:
                    self.close()
                    if self.th:
                        self.th.join()
                    self.shutdown.clear()
                    self.start()
                finally:
                    self.ndb.schema.allow_read(True)
        self.started.wait()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def load_sql(self):
        #
        spec = self.ndb.schema.fetchone('''
                                        SELECT * FROM sources
                                        WHERE f_target = %s
                                        ''' % self.ndb.schema.plch,
                                        (self.target, ))
        self['target'], self['kind'] = spec
        for spec in self.ndb.schema.fetch('''
                                          SELECT * FROM sources_options
                                          WHERE f_target = %s
                                          ''' % self.ndb.schema.plch,
                                          (self.target, )):
            f_target, f_name, f_type, f_value = spec
            self[f_name] = int(f_value) if f_type == 'int' else f_value
