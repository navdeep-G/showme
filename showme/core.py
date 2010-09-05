#		  ______									  
# ___________  /_ ______ ___	  _________ ___ _____ 
# __  ___/__  __ \_	 __ \__ | /| / /__	__ `__ \_  _ \
# _(__	) _	 / / // /_/ /__ |/ |/ / _  / / / / //  __/
# /____/  /_/ /_/ \____/ ____/|__/	/_/ /_/ /_/ \___/ 

from showme.packages.decorator import decorator

import cProfile
import inspect
import pprint


__version__ = '0.0.3'
__author__ = 'Kenneth Reitz'
__license__ = 'MIT'
__copyright__ = 'Copyright 2010 Kenneth Reitz'


pp = pprint.PrettyPrinter(indent=4)


@decorator
def time(f, *args, **kwargs):
	"""Display CPU Time statistics of given function"""

	t = cProfile.Profile()
	r = t.runcall(f, *args, **kwargs)
	t.print_stats()
	
	return r
	

@decorator
def globals(f, *args, **kwargs):
	"""Display global variables"""
	
	print('Globals:')
	print globals()
	return f(*args, **kwargs)


@decorator
def locals(f, *args, **kwargs):
	"""Display local variables"""
	# print locals()
	return f(*args, **kwargs)


@decorator
def docs(f, *args, **kwargs):
	"""Display PyDocs of given function"""
	print inspect.getdoc(f)
	return f(*args, **kwargs)


@decorator
def trace(f, *args, **kwargs):
	"""Print scope, call, and argument information."""

	_scope = inspect.getmodule(f).__name__

	# guess that function is a method of it's class
	if f.func_name in dir(args[0].__class__):
		_scope +=  '.' + args[0].__class__.__name__
		_scope +=  '.' + f.__name__
	else:
		_scope +=  '.' + f.__name__
		

	print("calling %s() with \nargs: %s \nkwargs: %s" % (_scope, args, kwargs))

	return f(*args, **kwargs)



