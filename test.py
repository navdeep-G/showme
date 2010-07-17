#!/usr/bin/env python
# -*- coding: utf-8 -*-

import showme

hi = 'hi'

@showme.globals
def test():
	"""docstring for fname"""
	for i in xrange(8):
		i ** i ** i
	return 'nene'
	
test()