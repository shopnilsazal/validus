# -*- coding: utf-8 -*-

import sys

if sys.version_info[1] < 6:
    __all__=['test_isbn.py','test_phones.py','test_validators.py']
else:
    __all__=['test_contracts.py','test_isbn.py','test_phones.py','test_validators.py']


