#		  ______
# ___________  /_ ______ ___	  _________ ___ _____
# __  ___/__  __ \_	 __ \__ | /| / /__	__ `__ \_  _ \
# _(__	) _	 / / // /_/ /__ |/ |/ / _  / / / / //  __/
# /____/  /_/ /_/ \____/ ____/|__/	/_/ /_/ /_/ \___/

from colorama import *
from decorator import decorator

import cProfile
import inspect

from time import time as now


__version__ = '1.0.1'
__author__ = 'Navdeep Gill'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019 Navdeep Gill'

__all__ = ('cputime',  'docs', 'time', 'trace')


# CLI Color
init(autoreset=True)


@decorator
def cputime(f, *args, **kwargs):
    """Display CPU Time statistics of given function."""

    print(('CPU time for %s%s%s:' % (Fore.CYAN, _get_scope(f, args), Fore.RESET)))

    t = cProfile.Profile()
    r = t.runcall(f, *args, **kwargs)
    t.print_stats()

    return r


@decorator
def docs(f, *args, **kwargs):
    """Display Docstrings of given function."""

    print(('Documentation for %s%s%s:' % (Fore.CYAN, _get_scope(f, args), Fore.RESET)))
    print((inspect.getdoc(f)))

    return f(*args, **kwargs)


@decorator
def time(f, *args, **kwargs):
    """Display Runtime statistics of given function."""

    print(('Execution speed of %s%s%s:' % (Fore.CYAN, _get_scope(f, args), Fore.RESET)))
    _t0 = now()
    _r = f(*args, **kwargs)
    _t1 = now()

    total_time = _t1 - _t0
    print(('%s seconds' % (total_time)))

    return _r


@decorator
def trace(f, *args, **kwargs):
    """Display epic argument and context call information of given function."""

    _scope = _get_scope(f, args)

    print(("Calling %s%s%s with: \n   %sargs%s: %s \n   %skwargs%s: %s" % (
        Fore.CYAN, _scope, Fore.RESET, Fore.BLUE, Fore.RESET,
        args, Fore.BLUE, Fore.RESET, kwargs)))

    return f(*args, **kwargs)


def _get_scope(f, args):
    """Get scope nameo of given function."""

    _scope = inspect.getmodule(f).__name__
    # guess that function is a method of it's class
    try:
        if f.__name__ in dir(args[0].__class__):
            _scope += '.' + args[0].__class__.__name__
            _scope += '.' + f.__name__
        else:
            _scope += '.' + f.__name__
    except IndexError:
        _scope += '.' + f.__name__

    return _scope
