# coding:utf-8
import csv
import inspect
import json
import os
import random
import signal
import subprocess
import sys
import time
import warnings
from functools import wraps
from pprint import pprint
from shutil import copy2
from typing import List, Union

import requests
import smart_open
from pydub.utils import mediainfo
from termcolor import colored

from .logger import Logger


class FormatPrint:
    @classmethod
    def red(cls, text: str) -> str:
        return colored(text, 'red')

    @classmethod
    def green(cls, text: str) -> str:
        return colored(text, 'green')

    @classmethod
    def cyan(cls, text: str) -> str:
        return colored(text, 'cyan')


class Network:
    _headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    client = requests.Session()

    @classmethod
    def get(cls, url: str) -> requests.models.Response:
        return requests.get(url, headers=cls._headers)

    @classmethod
    def post(cls,
             url: str,
             param: dict,
             post_format='json') -> requests.models.Response:
        if post_format == 'json':
            return requests.post(url, json=param, headers=cls._headers)
        else:
            return requests.post(url, data=param, headers=cls._headers)

    @classmethod
    def proxy_check(cls, proxy: str):
        """proxy format: 12.12.12.12:9987, no type was given"""
        proxy = proxy.split('/').pop()
        res = []
        for ptype in ('proxy', 'socks5'):
            cmd = f"curl -s --connect-timeout 5 --{ptype} {proxy} ipinfo.io"
            r_str = shell(cmd, surpress_error=True)
            if r_str != '':
                res.append(ptype)

        return (True, res) if res else (False, ['INVALID'])


# =========================================================== display
def p(*s):
    for i in s:
        print(i)


def pp(d: dict):
    pprint(d)


def sleep(countdown: int) -> None:
    time.sleep(countdown)


def random_sleep(lower_bound: int, upper_bound: int) -> None:
    """Randomly sleep for few seconds. Typical usage involving a crontab task
    to prevent robot behavior detection.
    """
    time.sleep(random.randint(lower_bound, upper_bound))


# =========================================================== IO
def show_func_name():
    p(f"\n--------------- {sys._getframe(1).f_code.co_name} ---------------")


def smartopen(file_path: str):
    with smart_open.open(file_path) as f:
        return f.readlines()


def shell(cmd: str,
          print_str: bool = False,
          surpress_error: bool = False) -> str:
    ret_str = ''
    try:
        ret_str = subprocess.check_output(cmd,
                                          stderr=subprocess.DEVNULL,
                                          shell=True).decode('utf8')
    except Exception as e:
        if not surpress_error:
            print(e)
    finally:
        if print_str:
            p(ret_str)
        return ret_str


class FileIO:
    @classmethod
    def readable_size(cls, size: int) -> str:
        '''Convert file size into human readable string'''
        units = ['KB', 'MB', 'GB', 'TB', 'PB'][::-1]
        res, copy_size = [], size
        size //= 1024
        while size > 0:
            res.append("{}{}".format(size % 1024, units.pop()))
            size //= 1024
        return str(copy_size) + ' ({})'.format(' '.join(reversed(res)))

    @classmethod
    def info(cls, file_path: str) -> dict:
        mi = mediainfo(file_path)
        if 'size' in mi:
            mi['size'] = cls.readable_size(int(mi['size']))

        if 'duration' in mi:
            mi['duration'] = float(mi['duration'])
        return mi

    @staticmethod
    def read(file_name: str, delimiter: str = '') -> Union[str, list]:
        texts = open(file_name, 'r').read().__str__()
        if delimiter:
            return texts.strip().split(delimiter)
        return texts

    @staticmethod
    def write(cons: str, file_name: str) -> None:
        with open(file_name, 'w') as f:
            f.write(cons)

    @staticmethod
    def say(contents):
        pprint(contents)

    @staticmethod
    def walk(dir: str, depth: int = 1) -> list:
        res, iter = [], os.walk(dir)
        if depth < 0: depth = 1 << 64

        for i in range(depth):
            try:
                base, _, files = next(iter)
                res += ['/'.join([base, f]) for f in files]
            except StopIteration as e:
                Logger().warning('Maximum depth {} reached.'.format(i))
                break
        return res

    @staticmethod
    def exists(file_name: str) -> bool:
        return os.path.exists(file_name)

    @staticmethod
    def dirname() -> str:
        previous_frame = inspect.currentframe().f_back
        # (filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
        filename, *_ = inspect.getframeinfo(previous_frame)
        return os.path.dirname(os.path.realpath(filename))

    @staticmethod
    def basename(file_path: str) -> str:
        return os.path.basename(file_path)

    @staticmethod
    def path(file_path: str) -> str:
        return os.path.dirname(file_path)

    @staticmethod
    def rm(file_path: str) -> None:
        os.remove(file_path)

    @staticmethod
    def rename(old_name: str, new_name: str) -> None:
        os.rename(old_name, new_name)

    @staticmethod
    def copy(old_name: str, new_name: str) -> None:
        copy2(old_name, new_name)


class JsonIO:
    @staticmethod
    def read(file_name: str) -> dict:
        res = {}
        with open(file_name, 'r') as f:
            res = json.loads(f.read())
        return res

    @staticmethod
    def write(d: dict, file_name: str):
        json.dump(d, open(file_name, 'w'), ensure_ascii=False, indent=2)

    @staticmethod
    def eval(file_name: str) -> dict:
        '''Helpful parsing single quoted dict'''
        return eval(FileIO.read(file_name))


class CSVIO:
    '''CSV manager'''
    @classmethod
    def read(cls, filename: str, delimiter: str = ',') -> List[List]:
        ''' read a CSV file and export it to a list '''
        texts = []
        with open(filename, newline='') as f:
            for row in csv.reader(f, delimiter=delimiter):
                texts.append(row)
        return texts

    @classmethod
    def iterator(cls, filename: str, delimiter: str = ',') -> csv.reader:
        return csv.reader(open(filename, 'r').readlines(),
                          delimiter=delimiter,
                          quoting=csv.QUOTE_MINIMAL)

    @classmethod
    def write(cls,
              texts: List,
              filename: str,
              delimiter: str = ',',
              column: int = 0) -> None:
        with open(filename, mode='w') as f:
            wt = csv.writer(f,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
            for row in texts:
                if column > 0:
                    n_row = row[:column - 1]
                    n_row.append(' '.join(row[column - 1:]))
                    n_row = [e.strip() for e in n_row]
                    wt.writerow(n_row)
                else:
                    wt.writerow(row)


# =========================================================== Decorators
def set_timeout(countdown: int, callback=print):
    def decorator(func):
        def handle(signum, frame):
            raise RuntimeError

        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handle)
                signal.alarm(countdown)  # set countdown
                r = func(*args, **kwargs)
                signal.alarm(0)  # close alarm
                return r
            except RuntimeError as e:
                print(e)
                callback()

        return wrapper

    return decorator


def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


def logged(logger_func, name=None, message=None):
    """
    Add logging to a function. name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    import logging

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger_func(logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


def retry(total_tries=3, initial_wait=0.5, backoff_factor=2):
    """calling the decorated function applying an exponential backoff.
    Args:
        total_tries: Total tries
        initial_wait: Time to first retry
        backoff_factor: Backoff multiplier (e.g. value of 2 will double the delay each retry).
    """
    logger = Logger()

    def retry_decorator(f):
        @wraps(f)
        def func_with_retries(*args, **kwargs):
            _tries, _delay = total_tries + 1, initial_wait
            while _tries > 0:
                try:
                    logger.info(
                        f'{f.__name__} {total_tries + 1 - _tries} try:')
                    return f(*args, **kwargs)
                except Exception as e:
                    _tries -= 1
                    print_args = args if args else 'no args'
                    if _tries == 0:
                        msg = "Fuction [{}] failed after {} tries. Args: [{}], kwargs [{}]".format(
                            f.__name__, total_tries, print_args, kwargs)
                        logger.info(msg)
                        raise
                    msg = "Function [{}] exception [{}]. Retrying in {} seconds. Args: [{}], kwargs: [{}]".format(
                        f.__name__, e, _delay, print_args, kwargs)
                    logger.info(msg)
                    time.sleep(_delay)
                    _delay *= backoff_factor

        return func_with_retries

    return retry_decorator


# -------------------------------------- End of decorators


def wrap_mod(mod, deprecated):
    """Return a wrapped object that warns about deprecated accesses"""
    deprecated = set(deprecated)

    class Wrapper(object):
        def __getattr__(self, attr):
            if attr in deprecated:
                warnings.warn(f"Alias {attr} is deprecated")
            return getattr(mod, attr)

        def __setattr__(self, attr, value):
            if attr in deprecated:
                warnings.warn("Property %s is deprecated" % attr)
            return setattr(mod, attr, value)

    return Wrapper()
