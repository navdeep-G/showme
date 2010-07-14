#!/usr/bin/env python
# encoding: utf-8

import os
import sys
import show


from distutils.core import setup

def publish():
	"""Publish to PyPi"""
	os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
	publish()
	sys.exit()

setup(name='show',
	  version=show.core.__version__,
	  description='Quick Debugging for Python',
	  long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
	  author='Kenneth Reitz',
	  author_email='me@kennethreitz.com',
	  url='http://github.com/kennethreitz/show',
	  packages=['show'],
	  license='MIT',
	  classifiers = ( 
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.5",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		)
	 )
