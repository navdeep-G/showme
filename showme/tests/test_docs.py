#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

>>> test()
sample docstring for test

"""

import doctest
import showme


@showme.docs
def test():
	"""sample docstring for test"""
	for i in range(1000):
		a = i ** i

if __name__ == '__main__':
	import doctest
	doctest.testmod()
