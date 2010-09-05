#!/usr/bin/env python
# encoding: utf-8

import os
import sys

from distutils.core import setup

def publish():
	"""Publish to PyPi"""
	os.system("python setup.py sdist upload")
	
if sys.argv[-1] == 'publish':
	publish()
	sys.exit()


setup(
	name='showme',
	version='1.0.0',
	description='Painless Debugging and Inspection for Python',
	long_description=open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
	author='Kenneth Reitz',
	author_email='me@kennethreitz.com',
	url='http://github.com/kennethreitz/showme',
	packages=['showme'],
	install_requires=[
		'colorama>=0.1.18', 
		'decorator>=3.2.0'
	],
	license='MIT',
	classifiers = ( 
	  'Development Status :: 5 - Production/Stable',
	  'Environment :: Console',
	  'Intended Audience :: Developers',
	  'License :: OSI Approved :: MIT License',
	  'Programming Language :: Python',
	  'Programming Language :: Python :: 2.5',
	  'Programming Language :: Python :: 2.6',
	  'Programming Language :: Python :: 2.7',
	  'Operating System :: MacOS :: MacOS X',
	  'Operating System :: Unix',
	  'Operating System :: POSIX',
	  'Topic :: Software Development',
	  'Topic :: Software Development :: Libraries',
	  'Topic :: Software Development :: Libraries :: Python Modules',
	  )
)
	
