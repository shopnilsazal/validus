=======
Validus
=======


.. image:: https://img.shields.io/pypi/v/validus.svg
        :target: https://pypi.python.org/pypi/validus

.. image:: https://img.shields.io/travis/shopnilsazal/validus.svg
        :target: https://travis-ci.org/shopnilsazal/validus


A dead simple Python data validation library.


Requirements
------------

- Python 3.3+


Installation
------------

.. code-block:: bash

    pip install validus


Usage
-----

.. code-block:: python

    >>> import validus

    >>> validus.isemail('someone@example.com')
    True


List of Functions
-----------------

.. code-block:: python

    isascii()
    isprintascii()
    isbase64()
    isemail()
    ishexadecimal()
    isint()
    isfloat()
    isslug()
    isuuid()
    isuuid3()
    isuuid4()
    isuuid5()
    isfullwidth()
    ishalfwidth()
    islatitude()
    islongitude()
    ismac()
    ismd5()
    issha1()
    issha256()
    issha512()
    ismongoid()
    isiso8601()
    isbytelen()
    isipv4()
    isipv6()
    isip()
    isport()
    isdns()
    isssn()
    issemver()
    ismultibyte()
    isfilepath()
    isdatauri()
    isjson()
    istime()
    isepoch()
    isurl()
    iscrcard()
    isisin()
    isiban()
    ishexcolor()
    isrgbcolor()
    isphone()
    isisbn()
    isisbn10()
    isisbn13()
    isimei()



Resources
---------

- `Documentation <http://shopnilsazal.github.io/validus/>`_
- `Issue Tracker <http://github.com/shopnilsazal/validus/issues>`_
- `Code <http://github.com/shopnilsazal/validus/>`_



Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

