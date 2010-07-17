from showme.packages.decorator import decorator

#         ______                                      
# ___________  /_ ______ ___      _________ ___ _____ 
# __  ___/__  __ \_  __ \__ | /| / /__  __ `__ \_  _ \
# _(__  ) _  / / // /_/ /__ |/ |/ / _  / / / / //  __/
# /____/  /_/ /_/ \____/ ____/|__/  /_/ /_/ /_/ \___/ 

__version__ = '0.0.2'
__author__ = 'Kenneth Reitz'
__license__ = 'MIT'
__copyright__ = 'Copyright 2010 Kenneth Reitz'


import cProfile
import pprint


pp = pprint.PrettyPrinter(indent=4)


@decorator
def args(f, *args, **kwargs):
	"""Display passed arguments of given function"""
	
	# print('Arguments: \n  %s\n	%s' % (args, kwargs))
	# pprint.PrettyPrinter(kwargs)
	pp.pprint(kwargs)
	return f(*args, **kwargs)


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
	
	return f(*args, **kwargs)


@decorator
def docs(f, *args, **kwargs):
	"""Display PyDocs of given function"""
	
	return f(*args, **kwargs)


@decorator
def size(f, *args, **kwargs):
	return f(*args, **kwargs)
	

