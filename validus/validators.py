# -*- coding: utf-8 -*-

from .utils import validate_str
import re
import ipaddress
import json
import time

patterns = {
    'ascii': r"^[\x00-\x7F]+$",
    'base64': r"^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{4})$",
    'email': r"""^(((([a-zA-Z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-zA-Z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-zA-Z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-zA-Z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-zA-Z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-zA-Z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-zA-Z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-zA-Z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-zA-Z]|\d|-|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-zA-Z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$""",
    'credit_card': r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$",
    'float': r"^(?:[-+]?(?:[0-9]+))?(?:\.[0-9]*)?(?:[eE][\+\-]?(?:[0-9]+))?$",
    'int': r"^(?:[-+]?(?:0|[1-9][0-9]*))$",
    'iso8601': r'^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$',
    'iban': r'^[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}$',
    'isin': r'^[A-Z]{2}[0-9A-Z]{9}[0-9]$',
    'uuid3': r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-3[0-9a-fA-F]{3}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    'uuid4': r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    'uuid5': r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-5[0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    'uuid': r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    'md5': r'^[a-fA-F0-9]{32}$',
    'mac': r'^([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])$',
    'printable_ascii': r"^[\x20-\x7E]+$",
    'multi_byte': r"[^\x00-\x7F]",
    'full_width': r"[^\u0020-\u007E\uFF61-\uFF9F\uFFA0-\uFFDC\uFFE8-\uFFEE0-9a-zA-Z]",
    'half_width': r"[\u0020-\u007E\uFF61-\uFF9F\uFFA0-\uFFDC\uFFE8-\uFFEE0-9a-zA-Z]",
    'hexadecimal': r"^[0-9a-fA-F]+$",
    'hex_color': r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$",
    'rgb_color': r"^rgb\(\s*(0|[1-9]\d?|1\d\d?|2[0-4]\d|25[0-5])\s*,\s*(0|[1-9]\d?|1\d\d?|2[0-4]\d|25[0-5])\s*,\s*(0|[1-9]\d?|1\d\d?|2[0-4]\d|25[0-5])\s*\)$",
    'data_uri': r"\s*data:([a-zA-Z]+\/[a-zA-Z0-9\-\+]+(;[a-zA-Z\-]+=[a-zA-Z0-9\-]+)?)?(;base64)?,[a-zA-Z0-9!\$&',\(\)\*\+,;=\-\._~:@\/\?%\s]*\s*$",
    'latitude': r'^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)$',
    'longitude': r'^[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$',
    'dns': r'^([a-zA-Z0-9_]{1}[a-zA-Z0-9_-]{0,62}){1}(\.[a-zA-Z0-9_]{1}[a-zA-Z0-9_-]{0,62})*[\._]?$',
    'url': r'^((ftp|tcp|irc|udp|wss?|https?):\/\/)?(\S+(:\S*)?@)?((([1-9]\d?|1\d\d|2[01]\d|22[0-3])(\.(1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.([0-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\])|(([a-zA-Z0-9]([a-zA-Z0-9-_]+)?[a-zA-Z0-9]([-\.][a-zA-Z0-9]+)*)|(((www\.)|([a-zA-Z0-9]([-\.][-\._a-zA-Z0-9]+)*))?))?(([a-zA-Z\u00a1-\uffff0-9]+-?-?)*[a-zA-Z\u00a1-\uffff0-9]+)(?:\.([a-zA-Z\u00a1-\uffff]{1,}))?))\.?(:(\d{1,5}))?((\/|\?|#)[^\s]*)?$',
    'ssn': r'^\d{3}[- ]?\d{2}[- ]?\d{4}$',
    'slug': r'^[-a-zA-Z0-9_]+$',
    'semver': r'^v?(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(-(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*)?(\+[0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*)?$',
    'win_path': r'^[a-zA-Z]:\\(?:[^\\/:*?"<>|\r\n]+\\)*[^\\/:*?"<>|\r\n]*$',
    'unix_path': r'^(/[^/\x00]*)+/?$'

}


@validate_str
def isascii(value):
    """
    Return whether or not given value contains ASCII chars only. Empty string is valid.
    If the value contains ASCII chars only, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isascii('1234abcDEF')
        True

        >>> isascii('ｆｏｏbar')
        False

    :param value: string to validate ASCII chars
    """
    return value == '' or bool(re.match(patterns['ascii'], value))


@validate_str
def isprintascii(value):
    """
    Return whether or not given value contains printable ASCII chars only. Empty string is valid.
    If the value contains printable ASCII chars only, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isprintascii('1234abcDEF')
        True

        >>> isprintascii('ｆｏｏbar')
        False

    :param value: string to validate printable ASCII chars
    """
    return value == '' or bool(re.match(patterns['printable_ascii'], value))


@validate_str
def isbase64(value):
    """
    Return whether or not given value is base64 encoded.
    If the value is base64 encoded, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isbase64('U3VzcGVuZGlzc2UgbGVjdHVzIGxlbw==')
        True

        >>> isbase64('Vml2YW11cyBmZXJtZtesting123')
        False

    :param value: string to validate base64 encoding
    """
    return bool(re.match(patterns['base64'], value))


@validate_str
def isemail(value):
    """
    Return whether or not given value is an email.
    If the value is an email, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isemail('foo@bar.com')
        True

        >>> isemail('invalidemail@')
        False

    :param value: string to validate email
    """
    return bool(re.match(patterns['email'], value))


@validate_str
def ishexadecimal(value):
    """
    Return whether or not given value is a hexadecimal number.
    If the value is a hexadecimal number, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> ishexadecimal('deadBEEF')
        True

        >>> ishexadecimal('abcdefg')
        False

    :param value: string to validate hexadecimal number
    """
    return bool(re.match(patterns['hexadecimal'], value))


@validate_str
def ishexcolor(value):
    """
    Return whether or not given value is a hexadecimal color.
    If the value is a hexadecimal color, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> ishexcolor('#ff0034')
        True

        >>> ishexcolor('#ff12FG')
        False

    :param value: string to validate hexadecimal color
    """
    return bool(re.match(patterns['hex_color'], value))


@validate_str
def isrgbcolor(value):
    """
    Return whether or not given value is a rgb color.
    If the value is a rgb color, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isrgbcolor('rgb(0,31,255)')
        True

        >>> isrgbcolor('rgb(1,349,275)')
        False

    :param value: string to validate rgb color
    """
    return bool(re.match(patterns['rgb_color'], value))


@validate_str
def isint(value):
    """
    Return whether or not given value is an integer.
    If the value is an integer, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isint('-2147483648')
        True

        >>> isint('123.123')
        False

    :param value: string to validate integer
    """
    return value != '' and bool(re.match(patterns['int'], value))


@validate_str
def isfloat(value):
    """
    Return whether or not given value is a float.
    If the value is a float, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isfloat('01.123')
        True

        >>> isfloat('+1f')
        False

    :param value: string to validate float
    """
    return value != '' and bool(re.match(patterns['float'], value))


@validate_str
def isslug(value):
    """
    Validate whether or not given value is valid slug.
    Valid slug can contain only alphanumeric characters, hyphens and
    underscores. If the value is a slug, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isslug('my-slug-2134')
        True

        >>> isslug('my.slug')
        False

    :param value: value to validate
    """
    return bool(re.match(patterns['slug'], value))


@validate_str
def isuuid(value):
    """
    Return whether or not given value is a UUID (version 3, 4 or 5).
    If the value is a UUID (version 3, 4 or 5), this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isuuid('a987fbc9-4bed-3078-cf07-9141ba07c9f3')
        True

        >>> isuuid('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3')
        False

    :param value: string to validate UUID (version 3, 4 or 5)
    """
    return bool(re.match(patterns['uuid'], value))


@validate_str
def isuuid3(value):
    """
    Return whether or not given value is a UUID version 3.
    If the value is a UUID version 3, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isuuid3('A987FBC9-4BED-3078-CF07-9141BA07C9F3')
        True

        >>> isuuid3('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3')
        False

    :param value: string to validate UUID version 3
    """
    return bool(re.match(patterns['uuid3'], value))


@validate_str
def isuuid4(value):
    """
    Return whether or not given value is a UUID version 4.
    If the value is a UUID version 4, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isuuid4('713ae7e3-cb32-45f9-adcb-7c4fa86b90c1')
        True

        >>> isuuid4('A987FBC9-4BED-3078-CF07-9141BA07C9F3')
        False

    :param value: string to validate UUID version 4
    """
    return bool(re.match(patterns['uuid4'], value))


@validate_str
def isuuid5(value):
    """
    Return whether or not given value is a UUID version 5.
    If the value is a UUID version 5, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isuuid5('987FBC97-4BED-5078-AF07-9141BA07C9F3')
        True

        >>> isuuid5('9c858901-8a57-4791-81fe-4c455b099bc9')
        False

    :param value: string to validate UUID version 5
    """
    return bool(re.match(patterns['uuid5'], value))


@validate_str
def isfullwidth(value):
    """
    Return whether or not given value contains any full-width chars.
    If the value contains any full-width chars, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isfullwidth('３ー０　ａ＠ｃｏｍ')
        True

        >>> isfullwidth('abc123')
        False

    :param value: string to validate full-width chars
    """
    return bool(re.match(patterns['full_width'], value))


@validate_str
def ishalfwidth(value):
    """
    Return whether or not given value contains any half-width chars.
    If the value contains any half-width chars, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> ishalfwidth('l-btn_02--active')
        True

        >>> ishalfwidth('００１１')
        False

    :param value: string to validate half-width chars
    """
    return bool(re.match(patterns['half_width'], value))


@validate_str
def islatitude(value):
    """
    Return whether or not given value is valid latitude.
    If the value is valid latitude, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> islatitude('-90.000')
        True

        >>> islatitude('+99.9')
        False

    :param value: string to validate latitude
    """
    return bool(re.match(patterns['latitude'], value))


@validate_str
def islongitude(value):
    """
    Return whether or not given value is valid longitude.
    If the value is valid longitude, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> islongitude('+73.234')
        True

        >>> islongitude('180.1')
        False

    :param value: string to validate longitude
    """
    return bool(re.match(patterns['longitude'], value))


@validate_str
def ismac(value):
    """
    Return whether or not given value is valid MAC address.
    If the value is valid MAC address, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> ismac('3D:F2:C9:A6:B3:4F')
        True

        >>> ismac('01:02:03:04:05')
        False

    :param value: string to validate MAC address
    """
    return bool(re.match(patterns['mac'], value))


@validate_str
def ismd5(value):
    """
    Return whether or not given value is MD5 encoded.
    If the value is MD5 encoded, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> ismd5('d94f3f016ae679c3008de268209132f2')
        True

        >>> ismd5('KYT0bf1c35032a71a14c2f719e5a14c1')
        False

    :param value: string to validate MD5 encoding
    """
    return bool(re.match(patterns['md5'], value))


@validate_str
def ismongoid(value):
    """
    Return whether or not given value is a valid hex-encoded representation of a MongoDB ObjectId.
    If the value is a MongoDB ObjectId, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> ismongoid('507f1f77bcf86cd799439011')
        True

        >>> ismongoid('507f1f77bcf86cd7994390')
        False

    :param value: string to validate MongoDB ObjectId
    """
    return ishexadecimal(value) and len(value) == 24


@validate_str
def isiso8601(value):
    """
    Return whether or not given value is ISO 8601 date.
    If the value is ISO 8601 date, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isiso8601('2009-12T12:34')
        True

        >>> isiso8601('2009367')
        False

    :param value: string to validate ISO 8601 date
    """
    return bool(re.match(patterns['iso8601'], value))


@validate_str
def isipv4(value):
    """
    Return whether or not given value is an IP version 4.
    If the value is an IP version 4, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isipv4('127.0.0.1')
        True

        >>> isipv4('::1')
        False

    :param value: string to validate IP version 4
    """
    try:
        ip_addr = ipaddress.IPv4Address(value)
    except ipaddress.AddressValueError:
        return False
    return ip_addr.version == 4


@validate_str
def isipv6(value):
    """
    Return whether or not given value is an IP version 6.
    If the value is an IP version 6, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isipv6('2001:41d0:2:a141::1')
        True

        >>> isipv6('127.0.0.1')
        False

    :param value: string to validate IP version 6
    """
    try:
        ip_addr = ipaddress.IPv6Address(value)
    except ipaddress.AddressValueError:
        return False
    return ip_addr.version == 6


@validate_str
def isip(value):
    """
    Return whether or not given value is an IP version 4 or 6.
    If the value is an IP version 4 or 6, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isip('127.0.0.1')
        True

        >>> isip('0200.200.200.200')
        False

    :param value: string to validate IP version 4 or 6
    """
    return isipv4(value) or isipv6(value)


@validate_str
def isport(value):
    """
    Return whether or not given value represents a valid port.
    If the value represents a valid port, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isport('8080')
        True

        >>> isport('65536')
        False

    :param value: string to validate port
    """
    try:
        port = int(value)
    except ValueError:
        return False
    if 0 < port < 65536:
        return True
    else:
        return False


@validate_str
def isdns(value):
    """
    Return whether or not given value represents a valid DNS name.
    If the value represents a valid DNS name, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isdns('localhost')
        True

        >>> isdns('a.b..')
        False

    :param value: string to validate DNS name
    """
    if value == '' or len(value.replace('.', '')) > 255:
        return False
    return (not isip(value)) and bool(re.match(patterns['dns'], value))


@validate_str
def isssn(value):
    """
    Return whether or not given value is a U.S. Social Security Number.
    If the value is a U.S. Social Security Number, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isssn('191 60 2869')
        True

        >>> isssn('66690-76')
        False

    :param value: string to validate U.S. Social Security Number
    """
    if value == '' or len(value) != 11:
        return False
    return bool(re.match(patterns['ssn'], value))


@validate_str
def issemver(value):
    """
    Return whether or not given value is valid semantic version.
    If the value is valid semantic version, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> issemver('v1.0.0')
        True

        >>> issemver('1.1.01')
        False

    :param value: string to validate semantic version
    """
    return bool(re.match(patterns['semver'], value))


@validate_str
def isbytelen(value, minimum, maximum):
    """
    Return whether or not given value's length (in bytes) falls in a range.
    If the value's length (in bytes) falls in a range, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isbytelen('123456', 0, 100)
        True

        >>> isbytelen('1239999', 0, 1)
        False

    :param value: string to validate length (in bytes) falls in a range
    :param minimum: minimum value of the range in integer
    :param maximum: maximum value of the range in integer
    """
    return minimum <= len(value) <= maximum


@validate_str
def ismultibyte(value):
    """
    Return whether or not given value contains one or more multibyte chars.
    If the value contains one or more multibyte chars, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> ismultibyte('あいうえお foobar')
        True

        >>> ismultibyte('abc')
        False

    :param value: string to validate one or more multibyte chars
    """
    return bool(re.match(patterns['multi_byte'], value))


@validate_str
def isfilepath(value):
    """
    Return whether or not given value is Win or Unix file path and returns it's type.
    If the value is Win or Unix file path, this function returns ``True, Type``, otherwise ``False, Type``.

    Examples::

        >>> isfilepath('c:\\path\\file (x86)\\bar')
        True, 'Win'

        >>> isfilepath('/path')
        True, 'Unix'

        >>> isfilepath('c:/path/file/')
        False, 'Unknown'

    :param value: string to validate file path
    """
    if re.match(patterns['win_path'], value):
        # check windows path limit see:
        # http://msdn.microsoft.com/en-us/library/aa365247(VS.85).aspx#maxpath
        if len(value[3:]) > 32767:
            return False, 'Win'
        return True, 'Win'
    elif re.match(patterns['unix_path'], value):
        return True, 'Unix'
    return False, 'Unknown'


@validate_str
def isdatauri(value):
    """
    Return whether or not given value is base64 encoded data URI such as an image.
    If the value is base64 encoded data URI, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isdatauri('data:text/plain;base64,Vml2YW11cyBmZXJtZW50dW0gc2VtcGVyIHBvcnRhLg==')
        True

        >>> isdatauri('dataxbase64data:HelloWorld')
        False

    :param value: string to validate base64 encoded data URI
    """
    return bool(re.match(patterns['data_uri'], value))


@validate_str
def isjson(value):
    """
    Return whether or not given value is valid JSON.
    If the value is valid JSON, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isjson('{"Key": {"Key": {"Key": 123}}}')
        True

        >>> isjson('{ key: "value" }')
        False

    :param value: string to validate JSON
    """
    try:
        decoded_json = json.loads(value)
    except ValueError:
        return False
    return True


@validate_str
def istime(value, fmt):
    """
    Return whether or not given value is valid time according to given format.
    If the value is valid time, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> istime('30 Nov 00', '%d %b %y')
        True

        >>> istime('Friday', '%d')
        False

    :param value: string to validate time
    :param fmt: format of time
    """
    try:
        time_obj = time.strptime(value, fmt)
    except ValueError:
        return False
    return True


@validate_str
def isurl(value):
    """
    Return whether or not given value is an URL.
    If the value is an URL, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isurl('http://foo.bar#com')
        True

        >>> isurl('http://foobar.c_o_m')
        False

    :param value: string to validate URL
    """
    if value == '' or len(value) >= 2083 or len(value) <= 3:
        return False
    return bool(re.match(patterns['url'], value))


@validate_str
def iscrcard(value):
    """
    Return whether or not given value is a credit card.
    If the value is a credit card, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> iscrcard('375556917985515')
        True

        >>> iscrcard('5398228707871528')
        False

    :param value: string to validate credit card
    """
    sanitized = re.sub(r'[^0-9]+', '', value)
    if not re.match(patterns['credit_card'], sanitized):
        return False

    summation = 0
    should_double = False
    for i in reversed(range(len(sanitized))):
        digit = int(sanitized[i:i+1])
        if should_double:
            digit *= 2
            if digit >= 10:
                summation += (digit % 10) + 1
            else:
                summation += digit
        else:
            summation += digit
        should_double = not should_double
    if summation % 10 == 0:
        return True
    return False


@validate_str
def isisin(value):
    """
    Return whether or not given value is valid International Securities Identification Number.
    If the value is a valid ISIN, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isisin('AU0000XVGZA3')
        True

        >>> isisin('DE000BAY0018')
        False

    :param value: string to validate ISIN
    """
    if not re.match(patterns['isin'], value):
        return False

    checksum_str = re.sub(r'[A-Z]', lambda ch: str(int(ch.group(0), 36)), value)
    summation = 0
    should_double = True
    for i in checksum_str[-2::-1]:
        digit = int(i)
        if should_double:
            digit *= 2
            if digit >= 10:
                summation += (digit + 1)
            else:
                summation += digit
        else:
            summation += digit
        should_double = not should_double

    return int(value[-1]) == (10000 - summation) % 10


@validate_str
def isiban(value):
    """
    Return whether or not given value is a valid IBAN code.
    If the value is a valid IBAN, this function returns ``True``, otherwise ``False``.

    Examples::

        >>> isiban('DE29100500001061045672')
        True

        >>> isiban('NO9186011117947')
        False

    :param value: string to validate IBAN code
    """
    cleaned_value = value.replace(' ', '').replace('\t', '')
    iban = cleaned_value[4:] + cleaned_value[:4]
    if not re.match(patterns['iban'], cleaned_value):
        return False
    digits = int(''.join(str(int(ch, 36)) for ch in iban))  # BASE 36: 0..9,A..Z -> 0..35
    return digits % 97 == 1

