===========================
Contract Usage (Python 3.6)
===========================

**Introduction: Design by Contract**

One programming paradigm is `Design by Contract <https://en.wikipedia.org/wiki/Design_by_contract>`_ .
The basic idea is that one should be explicit in the interface statements, *the
contract*, and that this should be enforced.  The enforcement of the contract
requires *validation*.   Traditionally, Python did not even allow types to be
described in the arguments; but as of Python 3.6, variable type annotations were
implemented.   However, these annotations were *hints*; that is, they did not
actually do anything, and thus by default cannot be used to enforce the
contract (at least, without using `mypy`).

Recently David Beazley gave a
`nice presentation <https://www.youtube.com/watch?v=js_0wjzuMfc>`_
on how this design can be elegantly implemented using Python 3.6 features to
enforce validation with the new type annotations.  This design pattern is
implemented in validus (`contract.py`) and can be used for any validus type.

This is useful as is,  but the real power is modifying this as a base class for
your own needs, as you may/will want to customize actions for each validation.
Making validation a core of your program is valuable, and this is an elegant
technique for implementing it in python.


Illustration using a simple function
====================================

We use Beazley's example of calculating the greatest common denominator, a
computation that only makes sense for positive integers.  Using validus in the
basic usage method to make sure that arguments are valid could be 
(see :download:`example <./gcd0.py>`):

.. literalinclude:: gcd0.py
    :linenos:
    :lines: 2,5-15

Running this example gives::

      (py36) bash-3.2$ python gcd0.py
      The greatest common denominator of 27 and 36 is:
      9
      The greatest common denominator of 2.7 and 3.6 is:
      AssertionError: gcd requires a positive number for a


The coding to enforce the example is a bit verbose.  Using type annotations, a
bit more compact method would be to use the decorator from `contract.py`
(see :download:`example <./gcd1.py>`):

.. literalinclude:: gcd1.py
    :linenos:
    :lines: 2,3,6-15

Running this example gives the same output as above.
The command on line 2 is to define all of the types that validus provides
validation methods for; i.e., for every `isfoo` validus method, there is a `foo`
type that can be validated.  `contract.py` also defines a composite type,
`positive_integer` using multiple inheritance.


Illustration using a simple class
=================================

A more elegant example is Beazley's simple game class. We show several different
methods of enforcing the contract.  

In this first design pattern, we use the traditional method of using validus to
enforce the contract:
(see :download:`example <./game1.py>`):

.. literalinclude:: game0.py
    :linenos:
    :language: python
    :lines: 2,6-23

Running this example, gives::

      Instantiating class with name=Guido, x=0, y=0
      Move to the left with dx=1
      Move to the left with dx=-1
      AssertionError: -1 must be a number and >0

In this second design pattern, we use a more compact description for both
the members of the class and arguments passed to methods
(see :download:`example <./game1.py>`):

.. literalinclude:: game1.py
    :linenos:
    :language: python
    :lines: 2,6-15

The result of this example is the same as above.
The lack of a constructor here is due to some `getattr/setattr` magic that is
similar to the `attrs` python package.  Finally, `contract.py` enables the
ability to specify the type globally within a module
(see :download:`example <./game2.py>`):

.. literalinclude:: game2.py
    :linenos:
    :language: python
    :lines: 1-3,6-15

Again, the output of this example is the same as the previous examples.

Contract module documentation
=============================

.. module:: contract

Decorator
---------

.. autofunction:: checked

Classes
---------

.. autoclass:: Contract

.. autoclass:: Validated

Validus contract types
-----------------------------

.. autoclass:: ascii

.. autoclass:: printascii

.. autoclass:: base64

.. autoclass:: email

.. autoclass:: hexadecimal

.. autoclass:: hexcolor

.. autoclass:: rgbcolor

.. autoclass:: integer
   
.. autoclass:: real
   
.. autoclass:: slug
   
.. autoclass:: uuid
   
.. autoclass:: uuid3
   
.. autoclass:: uuid4
   
.. autoclass:: uuid5
   
.. autoclass:: fullwidth
   
.. autoclass:: halfwidth
   
.. autoclass:: latitude
   
.. autoclass:: longitude
   
.. autoclass:: mac
   
.. autoclass:: md5
   
.. autoclass:: sha1
   
.. autoclass:: sha256
   
.. autoclass:: sha512
   
.. autoclass:: mongoid
   
.. autoclass:: iso8601
   
.. autoclass:: ipv4
   
.. autoclass:: ipv6
   
.. autoclass:: ip
   
.. autoclass:: port
   
.. autoclass:: dns
   
.. autoclass:: ssn
   
.. autoclass:: semver
   
.. autoclass:: bytelen
   
.. autoclass:: multibyte
   
.. autoclass:: filepath
   
.. autoclass:: datauri
   
.. autoclass:: json
   
.. autoclass:: time
   
.. autoclass:: url
   
.. autoclass:: crcard
   
.. autoclass:: isin
   
.. autoclass:: iban
   
.. autoclass:: imei
   
.. autoclass:: nonempty
   
.. autoclass:: positive
   
.. autoclass:: positive_integer
   
.. autoclass:: positive_real
   
.. autoclass:: nonempty_ascii
   

Import classes and methods
-----------------------------

.. autoclass:: ValidusBaseMeta
   
.. autoclass:: ValidusBase

.. autofunction:: set_validated_contracts
