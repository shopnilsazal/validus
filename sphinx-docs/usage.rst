=====
Usage
=====

Basic Validation
================

Each validator in ``validus`` is a simple function that takes the value to
validate and possibly some additional key-value arguments. Each function returns
``True`` when validation succeeds and ``False`` when validation fails.

Basic Usage
-----------

    >>> import validus
    >>> validus.isemail('me@mine.com')
    True
    >>> validus.isemail('@invalid.com')
    False


isascii
-------

.. module:: validus

.. autofunction:: isascii


isprintascii
------------

.. module:: validus

.. autofunction:: isprintascii


isbase64
--------

.. module:: validus

.. autofunction:: isbase64


isemail
-------

.. module:: validus

.. autofunction:: isemail


ishexadecimal
-------------

.. module:: validus

.. autofunction:: ishexadecimal


ishexcolor
----------

.. module:: validus

.. autofunction:: ishexcolor


isrgbcolor
----------

.. module:: validus

.. autofunction:: isrgbcolor


isint
-----

.. module:: validus

.. autofunction:: isint


isfloat
-------

.. module:: validus

.. autofunction:: isfloat


isslug
------

.. module:: validus

.. autofunction:: isslug


isuuid
------

.. module:: validus

.. autofunction:: isuuid


isuuid3
-------

.. module:: validus

.. autofunction:: isuuid3


isuuid4
-------

.. module:: validus

.. autofunction:: isuuid4


isuuid5
-------

.. module:: validus

.. autofunction:: isuuid5


isfullwidth
-----------

.. module:: validus

.. autofunction:: isfullwidth


ishalfwidth
-----------

.. module:: validus

.. autofunction:: ishalfwidth


islatitude
----------

.. module:: validus

.. autofunction:: islatitude


islongitude
-----------

.. module:: validus

.. autofunction:: islongitude


ismac
-----

.. module:: validus

.. autofunction:: ismac


ismd5
-----

.. module:: validus

.. autofunction:: ismd5


ismongoid
---------

.. module:: validus

.. autofunction:: ismongoid


isiso8601
---------

.. module:: validus

.. autofunction:: isiso8601


isipv4
------

.. module:: validus

.. autofunction:: isipv4


isipv6
------

.. module:: validus

.. autofunction:: isipv6


isip
----

.. module:: validus

.. autofunction:: isip


isport
------

.. module:: validus

.. autofunction:: isport


isdns
-----

.. module:: validus

.. autofunction:: isdns


isssn
-----

.. module:: validus

.. autofunction:: isssn


issemver
--------

.. module:: validus

.. autofunction:: issemver


isbytelen
---------

.. module:: validus

.. autofunction:: isbytelen


ismultibyte
-----------

.. module:: validus

.. autofunction:: ismultibyte


isfilepath
----------

.. module:: validus

.. autofunction:: isfilepath


isdatauri
---------

.. module:: validus

.. autofunction:: isdatauri


isjson
------

.. module:: validus

.. autofunction:: isjson


istime
------

.. module:: validus

.. autofunction:: istime


isurl
-----

.. module:: validus

.. autofunction:: isurl


iscrcard
--------

.. module:: validus

.. autofunction:: iscrcard


isisin
------

.. module:: validus

.. autofunction:: isisin


isiban
------

.. module:: validus

.. autofunction:: isiban


isphone
-------

.. module:: validus

.. autofunction:: isphone


isisbn
------

.. module:: validus

.. autofunction:: isisbn


isisbn10
--------

.. module:: validus

.. autofunction:: isisbn10


isisbn13
--------

.. module:: validus

.. autofunction:: isisbn13

