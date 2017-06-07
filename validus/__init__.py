# -*- coding: utf-8 -*-

__author__ = """Rafiqul Hasan"""
__email__ = 'shopnilsazal@gmail.com'
__version__ = '0.1.0'


from .phones import isphone
from .isbn import isisbn, isisbn10, isisbn13
from .validators import isascii, isprintascii, isbase64, isemail, ishexadecimal
from .validators import isint, isfloat, isslug, isuuid, isuuid3, isuuid4, isuuid5
from .validators import isfullwidth, ishalfwidth, islatitude, islongitude
from .validators import ismac, ismd5, ismongoid, isiso8601, isbytelen
from .validators import isipv4, isipv6, isip, isport, isdns, isssn, issemver
from .validators import ismultibyte, isfilepath, isdatauri, isjson, istime, isurl
from .validators import iscrcard, isisin, isiban, ishexcolor, isrgbcolor

