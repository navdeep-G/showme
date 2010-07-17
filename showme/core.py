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

import pprint
pp = pprint.PrettyPrinter(indent=4)

@decorator
def args(f, *args, **kwargs):
	# print('Arguments: \n  %s\n	%s' % (args, kwargs))
	# pprint.PrettyPrinter(kwargs)
	pp.pprint(kwargs)
	return f(*args, **kwargs)
