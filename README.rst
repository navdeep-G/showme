ShowMe -- Quick and easy debugging for Python
=============================================

ShowMe is a simple set of extremely useful function decorators for Python.
It allows you to view trace information, execution time, cputime, and function
documentation.


Installation
------------

To use **showme**, simply:

``pip install showme``

or, if you must:

``easy_install showme``


Usage
-----

Print passed-in arguments and function calls. ::

    @showme.trace
    def complex_function(a, b, c, **kwargs):
        ...


    >>> complex_function('alpha', 'beta', False, debug=True)
    calling haystack.submodule.complex_function with
       args: ({'a': 'alpha', 'b': 'beta', 'c': False},)
       kwargs: {'debug': True}


Print function execution time. ::

    @showme.time
    def some_function(a):
        ...

    >>> some_function()
    Execution speed of __main__.some_function:
    0.000688076019287 seconds

Print function cpu-execution time. ::

    @showme.cputime
    def complex_function(a, b, c):
        ...

    >>> complex_function()
    CPU time for __main__.complex_function:
         3 function calls in 0.013 CPU seconds

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.013    0.013    0.013    0.013 test_time.py:6(test)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {range}


.. Print local variables available at runtime. ::
..
..  @showme.locals
..  def complex_function(a, b, c):
..      ...


Pretty print function documentation. ::

    @showme.docs
    def complex_function():
        """Example Documentation for complex_function."""
        ...

    >>> complex_function()
    Documentation for __main__.complex_function:
    Example Documentation for complex_function.


Releasing pip package update
----------------------------

To udate the Python pip package, one can first satisfy the following requirements:

```bash
pip install --upgrade pip setuptools wheel
pip install twine
```

Followed by updating the package with:

```bash
python3 setup.py sdist bdist_wheel
python -m twine upload dist/\*
```

Developer pip install
---------------------

```bash
mkdir -p ~/bin
cp snn_rebuild.sh ~/bin/snnrb
chmod +x ~/bin/snnrb
```

Then you can rebuild and locally re-install all 5 repositories with the command:

```bash
snnrb
```

If you want to quickly test if your changes work, you can go into the root dir
of this project and run:

```bash
pip install -e .
```

that installs the latest changes into the pip package locally (into your conda
environment).

<!-- Un-wrapped URL's (Badges and Hyperlinks) -->
