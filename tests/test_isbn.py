#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_isbn
----------------------------------

Tests for `validus` module.
"""

import unittest
import validus


class TestIsbn(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isisbn(self):
        self.assertTrue(validus.isisbn('3836221195'))
        self.assertTrue(validus.isisbn('978-3-8362-2119-1'))
        self.assertTrue(validus.isisbn('3 423 21412 0'))
        self.assertTrue(validus.isisbn('0-00-726970-6'))
        self.assertTrue(validus.isisbn('978-4-87311-368-5'))
        self.assertFalse(validus.isisbn('3423214121'))
        self.assertFalse(validus.isisbn('foo'))
        self.assertFalse(validus.isisbn('1234abc56789'))
        self.assertFalse(validus.isisbn('978-3-8362-2119-0'))
        self.assertFalse(validus.isisbn('3-423-21412-1'))

    def test_isisbn10(self):
        self.assertTrue(validus.isisbn10('3 401 01319 X'))
        self.assertTrue(validus.isisbn10('1-61729-085-8'))
        self.assertTrue(validus.isisbn10('3-401-01319-X'))
        self.assertFalse(validus.isisbn10('123456789a'))
        self.assertFalse(validus.isisbn10('abc123def5'))
        self.assertFalse(validus.isisbn10('3-423-21412-1'))
        self.assertFalse(validus.isisbn10('9783836221191'))
        self.assertFalse(validus.isisbn10('3 423 21412 1'))

    def test_isisbn13(self):
        self.assertTrue(validus.isisbn13('978-4-87311-368-5'))
        self.assertTrue(validus.isisbn13('978-3-8362-2119-1'))
        self.assertTrue(validus.isisbn13('978 3401013190'))
        self.assertTrue(validus.isisbn13('978 4 87311 368 5'))
        self.assertTrue(validus.isisbn13('978 3 8362 2119 1'))
        self.assertFalse(validus.isisbn13('3-8362-2119-5'))
        self.assertFalse(validus.isisbn13('01234567890ab'))
        self.assertFalse(validus.isisbn13('foobar'))
        self.assertFalse(validus.isisbn13('01234567890ab'))
        self.assertFalse(validus.isisbn13('3836221195'))

