from typing import List, Dict, Callable
import inspect
import json

from .task_handler import TaskHandler
from .task_runner import TaskRunner
from .wait_handler import WaitHandler
from .blocked_handler import BlockedHandler
from .cluster_heartbeat import ClusterHeartbeat
from .wrapper.redis_client import RedisClient
from .common.settings import unique_hostnames, force_register
from .models.mongo.registered_task import RegisteredTask
from .models.mongo.node_tasks import NodeTasks
from .models.mongo.task import Task
from .wrapper.mongodb_client import MongoDBClient


class TaskQueue():
    def __init__(
        self,
        node_name: str,
        worker_count: int,
        amqp_host: str,
        task_queue: str,
        wait_queue: str,
        incoming_blocked_queue: str,
        wait_blocked_queue: str,
        amqp_username: str,
        amqp_password: str,
        redis_client: RedisClient,
        mongodb_client: MongoDBClient
    ):
        self.node_name = node_name
        self.worker_count = worker_count

        self.redis_client = redis_client
        self.mongodb_client = mongodb_client

        self.amqp_host = amqp_host

        self.task_queue = task_queue
        self.wait_queue = wait_queue
        self.incoming_blocked_queue = incoming_blocked_queue
        self.wait_blocked_queue = wait_blocked_queue

        self._start_handlers(amqp_username, amqp_password)

    def _start_handlers(self, amqp_username: str, amqp_password: str):
        """
        Init all handlers
        -> wait handler
        -> incoming blocked handler
        -> wait blocked handler
        -> task handler
        -> cluster heartbeat
        """
        self._init_wait_handler(amqp_username, amqp_password)
        self._init_incoming_blocked_handler(amqp_username, amqp_password)
        self._init_wait_blocked_handler(amqp_username, amqp_password)
        self._init_task_handler(amqp_username, amqp_password)
        self.init_cluster_heartbeat()

    def task(self, name: str = ''):
        """
        Decorator to simply register a new task
        """
        def wrapper(func):
            temp_name = name
            if len(temp_name) <= 0:
                # get the function name as string
                temp_name = func.__name__
            # register the function
            # using the function name
            self.task_handler.add_task(temp_name, func)
        return wrapper

    def add_task(self, func, name: str = ''):
        """
        Method to add tasks, which cannot be added using the decorator
        """
        outer_wrapper = self.task(name)
        outer_wrapper(func)

    def _task_arguments(self, function_signature):
        """
        Get arguments from task function signature
        """
        return [
            obj for obj in list(function_signature.parameters)
            if obj != 'self'
        ]

    def _task_argument_types(self, function_signature):
        """
        Get argument types from task function signature
        """
        return [
            function_signature.parameters[d].annotation.__name__
            if hasattr(function_signature.parameters[d].annotation, '__name__')
            else str(function_signature.parameters[d].annotation)
            for d in function_signature.parameters
        ]

    def _registered_task(self, task_name: str, callback: Callable[..., Task]):
        """
        Inspect given callback and return a RegisteredTask object
        needed for _node_tasks to assemble the full list of registered tasks
        """
        function_signature = inspect.signature(callback)
        argument_names = self._task_arguments(function_signature)
        argument_types = self._task_argument_types(function_signature)
        return RegisteredTask(
            name=task_name,
            arguments=dict(zip(argument_names, argument_types))
        )

    def _node_tasks(self):
        """
        Get all registered tasks on this node
        """
        task_runners: Dict[str, TaskRunner] = \
            self.task_handler.registered_tasks
        all_registered_tasks: List[RegisteredTask] = []
        for task_name in task_runners:
            registered_task = self._registered_task(
                task_name, task_runners[task_name].callback)
            all_registered_tasks.append(registered_task)
        return NodeTasks(
            node_name=self.node_name,
            tasks=all_registered_tasks
        )

    def _register_tasks(self):
        """
        Registers all internally registered tasks in the redis database
        in the form:
            node_name/task_name
        """
        node_tasks = self._node_tasks()
        already_registered_node = \
            self.mongodb_client.db().registered_tasks.find_one(
                {
                    'node_name': self.node_name
                }
            )
        if already_registered_node is not None:
            if unique_hostnames:  # setting
                raise Exception(
                    'Existing node name found in redis list, exiting.\n'
                    'If this is intentional, set unique_hostnames to False'
                )
            if force_register:
                self.mongodb_client.db().registered_tasks.delete_many(
                    {
                        'node_name': self.node_name
                    }
                )
        self.mongodb_client.db().registered_tasks.insert_one(
            dict(json.loads(node_tasks.to_json()))
        )

    def _init_wait_handler(self, amqp_username: str, amqp_password: str):
        """
        Start the wait handler queue listener
        """
        self.wait_thread = WaitHandler(
            node_name=self.node_name,
            amqp_host=self.amqp_host,
            amqp_username=amqp_username,
            amqp_password=amqp_password,
            redis_client=self.redis_client,
            queue_name=self.task_queue,
            wait_queue_name=self.wait_queue,
            blocked_queue_name=self.wait_blocked_queue
        )

    def _init_incoming_blocked_handler(
        self,
        amqp_username: str,
        amqp_password: str
    ):
        """
        Init the blocked queue for all blocked tasks,
        which are blocked before even getting to the actual processing
        --> Blacklist/Blocklist
        --> Node is set to not respond to any task
        --> Node is in standby mode
        """
        self.incoming_blocked_handler = BlockedHandler(
            node_name=self.node_name,
            amqp_host=self.amqp_host,
            amqp_username=amqp_username,
            amqp_password=amqp_password,
            redis_client=self.redis_client,
            task_queue_name=self.task_queue,
            blocked_queue_name=self.incoming_blocked_queue
        )

    def _init_wait_blocked_handler(
        self,
        amqp_username: str,
        amqp_password: str
    ):
        """
        Init the blocked queue listener for all waiting tasks (failed, etc.)
        """
        self.wait_blocked_handler = BlockedHandler(
            node_name=self.node_name,
            amqp_host=self.amqp_host,
            amqp_username=amqp_username,
            amqp_password=amqp_password,
            redis_client=self.redis_client,
            task_queue_name=self.wait_queue,
            blocked_queue_name=self.wait_blocked_queue
        )

    def _init_task_handler(self, amqp_username: str, amqp_password: str):
        """
        Init the actual task queue listener
        """
        self.task_handler = TaskHandler(
            node_name=self.node_name,
            amqp_host=self.amqp_host,
            amqp_username=amqp_username,
            amqp_password=amqp_password,
            redis_client=self.redis_client,
            queue_name=self.task_queue,
            wait_queue_name=self.wait_queue,
            blocked_queue_name=self.incoming_blocked_queue,
            mongodb_client=self.mongodb_client
        )

    def init_cluster_heartbeat(self):
        """
        Init the ClusterHeartbeat
        """
        self.cluster_heartbeat: ClusterHeartbeat = ClusterHeartbeat(
            self.node_name,
            self.redis_client
        )

    def _listen_handlers(self):
        """
        Start all handlers to listen
        """
        self.wait_thread.listen()
        self.incoming_blocked_handler.listen()
        self.wait_blocked_handler.listen()

    def listen(self):
        """
        Start listening on all queues
        """
        self._register_tasks()
        print(self.worker_count)
        self.task_handler.scale(self.worker_count)
        self.cluster_heartbeat.start_heartbeat()
        print('listening')
        self._listen_handlers()
        self.task_handler.listen()
