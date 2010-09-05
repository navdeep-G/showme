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

    @showme.cputime
    def complex_function(a, b, c):…
    
    >>> complex_function()
         3 function calls in 0.013 CPU seconds
		
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.013    0.013    0.013    0.013 test_time.py:6(test)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {range}


Print local variables available at runtime. ::
	
	@showme.locals
	def complex_function(a, b, c):…



Pretty print function documentation. ::
	
	@showme.docs
	def complex_function():
		"""Example Documentation for complex_function"""
		pass
		
	>>> complex_function()
	Example Documentation for complex_function
	
