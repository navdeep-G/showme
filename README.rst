ShowMe -- Quick and easy debugging for Python
=============================================

(Beware, this is still in doc-driven development)

Usage
-----

Print passed-in arguments and function calls. ::

	@showme.trace
	def complex_function(a, b, c, **kwargs):…
	
	>>> complex_function('alpha', 'beta', False, debug=True)
	calling haystack.submodule.complex_function() with 
	   args: ({'a': 'alpha', 'b': 'beta', 'c': False},)
	   kwargs: {'debug': True}

	
Print function execution time. ::

	@showme.time
	def complex_function(a, b, c):…


Print global variables available at runtime. ::
	
	@showme.globals
	def complex_function(a, b, c):…


Print local variables available at runtime. ::
	
	@showme.locals
	def complex_function(a, b, c):…



Pretty print function documentation. ::
	
	@showme.docs
	def complex_function(a, b, c):…
	
