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
	pass

if __name__ == '__main__':
	test()
