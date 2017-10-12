# -*- coding: utf-8 -*-
'''
Framework for enforcing assertions utilizing Python 3.6 features

Notes::

    - Type is real for isfloat
    - Type is integer for isint
    - bytelen is not supported (Needs to be tuple)
    - time is not supported (Needs to be tuple)
    - The method of invoking the validus.is* methods requires evals and some tests
       have problems -- See tests_contracts.py for these issues.
'''

from collections import ChainMap
from functools import wraps
from inspect import signature
import validus
import sys

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
_contracts = {'validus': type(validus), 'checked': type(checked)}


class Contract:
    """ Base class for enforcing the contract.  
    This uses dunder magic similar to enable a compact representation
    """

    @classmethod
    def __init_subclass__(cls):
        """ Register all contracts to simplify import
        """
        _contracts[cls.__name__] = cls

#   Own the "dot" (Descriptor protocol)
    def __set__(self, instance, value):
        ''' Check the value before setting it to the name
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
    """ Class that validates the values and enforces the contract
    """
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
        assert istype in dir(validus), f'{ctype} is not a validus validator'
        cmd="validus."+istype+"('"+str(value)+"')"
        assert eval(cmd), assert_msg


class ascii(Validated):
    """ Class that validates and enforces ascii contract using isascii
    """
    type = 'ascii'


class printascii(Validated):
    """ Class that validates and enforces printascii contract using isprintascii
    """
    type = 'printascii'


class base64(Validated):
    """ Class that validates and enforces base64 contract using isbase64
    """
    type = 'base64'


class email(Validated):
    """ Class that validates and enforces email contract using isemail
    """
    type = 'email'


class hexadecimal(Validated):
    """ Class that validates and enforces hexadecimal contract using
    ishexadecimal
    """
    type = 'hexadecimal'


class hexcolor(Validated):
    """ Class that validates and enforces hexcolor contract using ishexcolor
    """
    type = 'hexcolor'


class rgbcolor(Validated):
    """ Class that validates and enforces rgbcolor contract using isrgbcolor
    """
    type = 'rgbcolor'


# Do not want class names that match intrinsic functions so type != class name
class integer(Validated):
    """ Class that validates and enforces integer contract using isinteger
    """
    type = 'int'


# Do not want class names that match intrinsic functions so type != class name
class real(Validated):
    """ Class that validates and enforces real contract using isreal
    """
    type = 'float'


class slug(Validated):
    """ Class that validates and enforces slug contract using isslug
    """
    type = 'slug'


class uuid(Validated):
    """ Class that validates and enforces uuid contract using isuuid
    """
    type = 'uuid'


class uuid3(Validated):
    """ Class that validates and enforces uuid3 contract using isuuid3
    """
    type = 'uuid3'


class uuid4(Validated):
    """ Class that validates and enforces uuid4 contract using isuuid4
    """
    type = 'uuid4'


class uuid5(Validated):
    """ Class that validates and enforces uuid5 contract using isuuid5
    """
    type = 'uuid5'


class fullwidth(Validated):
    """ Class that validates and enforces fullwidth contract using isfullwidth
    """
    type = 'fullwidth'


class halfwidth(Validated):
    """ Class that validates and enforces halfwidth contract using ishalfwidth
    """
    type = 'halfwidth'


class latitude(Validated):
    """ Class that validates and enforces latitude contract using islatitude
    """
    type = 'latitude'


class longitude(Validated):
    """ Class that validates and enforces longitude contract using islongitude
    """
    type = 'longitude'


class mac(Validated):
    """ Class that validates and enforces mac contract using ismac
    """
    type = 'mac'


class md5(Validated):
    """ Class that validates and enforces md5 contract using ismd5
    """
    type = 'md5'


class sha1(Validated):
    """ Class that validates and enforces sha1 contract using issha1
    """
    type = 'sha1'


class sha256(Validated):
    """ Class that validates and enforces sha256 contract using issha256
    """
    type = 'sha256'


class sha512(Validated):
    """ Class that validates and enforces sha512 contract using issha512
    """
    type = 'sha512'


class mongoid(Validated):
    """ Class that validates and enforces mongoid contract using ismongoid
    """
    type = 'mongoid'


class iso8601(Validated):
    """ Class that validates and enforces iso8601 contract using isiso8601
    """
    type = 'iso8601'


class ipv4(Validated):
    """ Class that validates and enforces ipv4 contract using isipv4
    """
    type = 'ipv4'


class ipv6(Validated):
    """ Class that validates and enforces ipv6 contract using isipv6
    """
    type = 'ipv6'


class ip(Validated):
    """ Class that validates and enforces ip contract using isip
    """
    type = 'ip'


class port(Validated):
    """ Class that validates and enforces port contract using isport
    """
    type = 'port'


class dns(Validated):
    """ Class that validates and enforces dns contract using isdns
    """
    type = 'dns'


class ssn(Validated):
    """ Class that validates and enforces ssn contract using isssn
    """
    type = 'ssn'


class semver(Validated):
    """ Class that validates and enforces semver contract using issemver
    """
    type = 'semver'


class multibyte(Validated):
    """ Class that validates and enforces multibyte contract using ismultibyte
    """
    type = 'multibyte'


class filepath(Validated):
    """ Class that validates and enforces filepath contract using isfilepath
    """
    type = 'filepath'


class datauri(Validated):
    """ Class that validates and enforces datauri contract using isdatauri
    """
    type = 'datauri'


class json(Validated):
    """ Class that validates and enforces json contract using isjson
    """
    type = 'json'


class time(Validated):
    """ Class that validates and enforces time contract using istime
    """
    type = 'time'


class url(Validated):
    """ Class that validates and enforces url contract using isurl
    """
    type = 'url'


class crcard(Validated):
    """ Class that validates and enforces crcard contract using iscrcard
    """
    type = 'crcard'


class isin(Validated):
    """ Class that validates and enforces isin contract using isisin
    """
    type = 'isin'


class iban(Validated):
    """ Class that validates and enforces iban contract using isiban
    """
    type = 'iban'


class imei(Validated):
    """ Class that validates and enforces imei contract using isimei
    """
    type = 'imei'


class nonempty(Validated):
    """ Class that validates and enforces nonempty contract using isnonempty
    """
    type = 'nonempty'
    assert_msg = '"Value must not be empty"'


class positive(Validated):
    """ Class that validates and enforces positive contract using ispositive
    """
    type = 'positive'
    assert_msg = "f'{value} must be a number and >0'"


# For composite functions, the type member changes during multiple inheritance
# so Beazely's method of using super().check() doesn't work.  The solution is
# to just call the checks by hand.
class positive_integer(integer, positive):
    """ Composite Class that validates and enforces both positive and integer
    """
    @classmethod
    def check(cls, value):
        positive.check(value)
        integer.check(value)


class positive_real(positive, real):
    """ Composite Class that validates and enforces both positive and real
    """
    @classmethod
    def check(cls, value):
        positive.check(value)
        real.check(value)


class nonempty_ascii(nonempty, ascii):
    """ Composite Class that validates and enforces both nonempty and ascii
    """
    @classmethod
    def check(cls, value):
        nonempty.check(value)
        ascii.check(value)


class ValidusBaseMeta(type):
    """ Metaclass for enabling elegant importing
    """
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
    """ Class to inherit from that gets the types automatically
    """
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
        if hasattr(cls,'__annotations__'):
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
    for valtype in _contracts:
        valcontract = getattr(sys.modules[__name__], valtype)
        setattr(sys.modules[modulename], valtype, valcontract)
