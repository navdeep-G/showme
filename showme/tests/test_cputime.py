#!/usr/bin/env python
# -*- coding: utf-8 -*-

import showme

@showme.cputime
def test():
	"""docstring for test"""
	for i in range(1000):
		a = i ** i
	return 1

if __name__ == '__main__':
	test()
