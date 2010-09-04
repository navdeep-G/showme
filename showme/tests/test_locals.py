#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

>>> test()


"""

import doctest
import showme


@showme.locals
def test():
	"""sample docstring for test"""
	a = 'hi'
	b = 'bye'

if __name__ == '__main__':
	import doctest
	doctest.testmod()
