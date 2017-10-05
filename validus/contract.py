# -*- coding: utf-8 -*-


'''
Framework for enforcing assertions utilizing Python 3.6 features

Inspired by/stolen from the contract.py framework written by David Beazely at
his PyCon Israel talk:
  https://www.youtube.com/watch?v=js_0wjzuMfc&t=1999s
'''

from collections import ChainMap
from functools import wraps
from inspect import signature
import validators


def checked(func):
    '''
    Enable a decorator that enforces the type annotations
    in the signature of a function.

    Example::

        @checked
        def gcd(a:positive_integer,b:positive_integer):
            """
            Compute greatest common denominator
            """
            while b:
                a, b = b, a % b
            return a
    '''
    sig = signature(func)
#    ann=func.__annotations__
#     chainmap here allows module annotations (global or "typemap")
    ann = ChainMap(
        func.__annotations__,
        func.__globals__.get('__annotations__', {})
    )

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            if name in ann:
                ann[name].check(val)
        return func(*args, **kwargs)
    return wrapper


# Registry to make namespacing magic
_contracts = {'validators': type(validators), 'checked': type(checked)}


class Contract:

    @classmethod
    def __init_subclass__(cls):
        """ Register all contracts to simplify import
        """
        _contracts[cls.__name__] = cls

#   Own the "dot" (Descriptor protocol)
    def __set__(self, instance, value):
        ''' Check the value before setting it to the name
        This allows things like::

            email = email()
        '''
        self.check(value)
        instance.__dict__[self.name] = value

    # 3.6+ feature
    def __set_name__(self, cls, name):
        ''' Check the value before setting it to the name

        This allows in the class::

            class Player:
                name = nonempty_ascii()
                x = integer()
                y = integer()

        will give::

            p=Player('Guido',0,0)
            p.name=''  # Give error
            p.x=1.     # Give error
        '''
        self.name = name
        return

    @classmethod
    def check(cls, value):
        pass


class Validated(Contract):
    type = None
    assert_msg = None

    @classmethod
    def check(cls, value):
        ctype = cls.type
        istype = 'is'+ctype
        if not cls.assert_msg:
            assert_msg = f'{value} is not a valid {ctype}'
        else:
            assert_msg = eval(cls.assert_msg)  # eval for fstrings in classes
        assert istype in dir(validators), f'{ctype} is not a validus validator'
        assert eval('validators.'+istype+'("'+str(value)+'")'), assert_msg


class ascii(Validated):
    type = 'ascii'


class printascii(Validated):

    type = 'printascii'


class base64(Validated):
    type = 'base64'


class email(Validated):
    type = 'email'


class hexadecimal(Validated):
    type = 'hexadecimal'


class hexcolor(Validated):
    type = 'hexcolor'


class rgbcolor(Validated):
    type = 'rgbcolor'


# Do not want class names that match intrinsic functions so type != class name
class integer(Validated):
    type = 'int'


# Do not want class names that match intrinsic functions so type != class name
class real(Validated):
    type = 'float'


class slug(Validated):
    type = 'slug'


class uuid(Validated):
    type = 'uuid'


class uuid3(Validated):
    type = 'uuid3'


class uuid4(Validated):
    type = 'uuid4'


class uuid5(Validated):
    type = 'uuid5'


class fullwidth(Validated):
    type = 'fullwidth'


class halfwidth(Validated):
    type = 'halfwidth'


class latitude(Validated):
    type = 'latitude'


class longitude(Validated):
    type = 'longitude'


class mac(Validated):
    type = 'mac'


class md5(Validated):
    type = 'md5'


class sha1(Validated):
    type = 'sha1'


class sha256(Validated):
    type = 'sha256'


class sha512(Validated):
    type = 'sha512'


class mongoid(Validated):
    type = 'mongoid'


class iso8601(Validated):
    type = 'iso8601'


class ipv4(Validated):
    type = 'ipv4'


class ipv6(Validated):
    type = 'ipv6'


class ip(Validated):
    type = 'ip'


class port(Validated):
    type = 'port'


class dns(Validated):
    type = 'dns'


class ssn(Validated):
    type = 'ssn'


class semver(Validated):
    type = 'semver'


class bytelen(Validated):
    type = 'bytelen'


class multibyte(Validated):
    type = 'multibyte'


class filepath(Validated):
    type = 'filepath'


class datauri(Validated):
    type = 'datauri'


class json(Validated):
    type = 'json'


class time(Validated):
    type = 'time'


class url(Validated):
    type = 'url'


class crcard(Validated):
    type = 'crcard'


class isin(Validated):
    type = 'isin'


class iban(Validated):
    type = 'iban'


class imei(Validated):
    type = 'imei'


class nonempty(Validated):
    type = 'nonempty'
    assert_msg = '"Value must not be empty"'


class positive(Validated):
    type = 'positive'
    assert_msg = "f'{value} must be a number and >0'"


# For composite functions, the type member changes during multiple inheritance
# so Beazely's method of using super().check() doesn't work.  The solution is
# to just call the checks by hand.
class positive_integer(integer, positive):
    @classmethod
    def check(cls, value):
        positive.check(value)
        integer.check(value)


class positive_real(positive, real):
    @classmethod
    def check(cls, value):
        positive.check(value)
        real.check(value)


class nonempty_ascii(nonempty, ascii):
    @classmethod
    def check(cls, value):
        nonempty.check(value)
        ascii.check(value)


class ValidusBaseMeta(type):
    @classmethod
    def __prepare__(cls, *args):
        """
        Use the registry to define what is imported
        """
        return ChainMap({}, _contracts)

    def __new__(meta, name, bases, methods):
        """
        Need to throw away the registry for new
        """
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)


class ValidusBase(metaclass=ValidusBaseMeta):
    @classmethod
    def __init_subclass__(cls):
        """ Instatiate the contracts to enable
            type annotations in classes to be enforced
            on both members and method arguments.

            Example::
                class Player(ValidusBase):
                    name: nonempty_ascii
                    x: integer
                    y: integer

                    def left(self, dx: PositiveInteger):
                        x -= dx

             will give::

                    p = Player('Guido',0,0)
                    p.name = ''  # Give error
                    p.x = 1.     # Give error
                    p.left(-2)   # Give error

        """
        # Contract on members
        for name, valtype in cls.__annotations__.items():
            contract = valtype()
            contract.__set_name__(cls, name)
            setattr(cls, name, contract)

        # Contract on method arguments
        for name, val, in cls.__dict__.items():
            if callable(val):
                setattr(cls, name, checked(val))

    def __init__(self, *args):
        """ Enforce annotating all of your arguments
            in the constructor
            Also set all arguments passed in to members automatically
            (similar to attrs at attrs.org)
        """
        ann = self.__annotations__
        assert len(args) == len(ann), f'Expected all arguments to be annotated'
        # Relies on ordered dict in 3.6
        for name, val in zip(ann, args):
            setattr(self, name, val)

    def __repr__(self):
        """ Enforce annotating all of your arguments
            in the constructor.
        """
        args = ','.join(repr(getattr(self, name))
                        for name in self.__annotations__)
        return f'{type(self).__name__}({args})'


def set_validated_contracts(modulename):
    """
    Try to avoid `from contract import *`
    or `from contract import ascii, printascii, int, float, email, ...`

    Usage::

        from contract import set_validated_contracts
        set_validated_contracts(__name__)

    """
    import sys
    for valtype in _contracts:
        valcontract = getattr(sys.modules[__name__], valtype)
        setattr(sys.modules[modulename], valtype, valcontract)
