#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_contracts
----------------------------------

Tests for `validus` contracts module.
"""

import unittest
from validus.contract import ValidusBase
from validus.contract import set_validated_contracts
set_validated_contracts(__name__)


class TestContracts(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ascii(self):
        @checked
        def checkedmethod(a: ascii):
            return True

        self.assertTrue(checkedmethod('foobar'))
        self.assertTrue(checkedmethod('0987654321'))
        self.assertTrue(checkedmethod('1234abcDEF'))
        self.assertTrue(checkedmethod('test@example.com'))

        self.assertRaises(AssertionError, checkedmethod, 'ｆｏｏbar')
        self.assertRaises(AssertionError, checkedmethod, 'ｘｙｚ０９８')
        self.assertRaises(AssertionError, checkedmethod, '１２３456')

        class CheckedClass(ValidusBase):
            a: ascii

        self.assertIsNotNone(CheckedClass('foobar'))
        self.assertIsNotNone(CheckedClass('0987654321'))
        self.assertIsNotNone(CheckedClass('1234abcDEF'))
        self.assertIsNotNone(CheckedClass('test@example.com'))

        self.assertRaises(AssertionError, CheckedClass, 'ｆｏｏbar')
        self.assertRaises(AssertionError, CheckedClass, 'ｘｙｚ０９８')
        self.assertRaises(AssertionError, CheckedClass, '１２３456')

    def test_printascii(self):
        @checked
        def checkedmethod(a: printascii):
            return True

        self.assertTrue(checkedmethod('foobar'))
        self.assertTrue(checkedmethod('0987654321'))
        self.assertTrue(checkedmethod('1234abcDEF'))
        self.assertTrue(checkedmethod('test@example.com'))

        self.assertRaises(AssertionError, checkedmethod, 'ｆｏｏbar')
        self.assertRaises(AssertionError, checkedmethod, 'ｘｙｚ０９８')
        self.assertRaises(AssertionError, checkedmethod, '１２３456')
        self.assertRaises(AssertionError, checkedmethod, '\x19test\x7F')

        class CheckedClass(ValidusBase):
            a: printascii

        self.assertTrue(CheckedClass('foobar'))
        self.assertTrue(CheckedClass('0987654321'))
        self.assertTrue(CheckedClass('1234abcDEF'))
        self.assertTrue(CheckedClass('test@example.com'))

        self.assertRaises(AssertionError, CheckedClass, 'ｆｏｏbar')
        self.assertRaises(AssertionError, CheckedClass, 'ｘｙｚ０９８')
        self.assertRaises(AssertionError, CheckedClass, '１２３456')
        self.assertRaises(AssertionError, CheckedClass, '\x19test\x7F')

    def test_base64(self):
        @checked
        def checkedmethod(a: base64):
            return True

        self.assertTrue(checkedmethod('TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4='))
        self.assertTrue(checkedmethod('Vml2YW11cyBmZXJtZW50dW0gc2VtcGVyIHBvcnRhLg=='))
        self.assertTrue(checkedmethod('U3VzcGVuZGlzc2UgbGVjdHVzIGxlbw=='))
        self.assertTrue(checkedmethod('Zm9vYmE='))

        self.assertRaises(AssertionError, checkedmethod, 'dataxbase64')
        self.assertRaises(AssertionError, checkedmethod, 'Vml2YW11cyBmZXJtZtesting123')
        self.assertRaises(AssertionError, checkedmethod, '12345')
        self.assertRaises(AssertionError, checkedmethod, 'Zm9vYmFy====')

        class CheckedClass(ValidusBase):
            a: base64

        self.assertTrue(CheckedClass('TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4='))
        self.assertTrue(CheckedClass('Vml2YW11cyBmZXJtZW50dW0gc2VtcGVyIHBvcnRhLg=='))
        self.assertTrue(CheckedClass('U3VzcGVuZGlzc2UgbGVjdHVzIGxlbw=='))
        self.assertTrue(CheckedClass('Zm9vYmE='))

        self.assertRaises(AssertionError, CheckedClass, 'dataxbase64')
        self.assertRaises(AssertionError, CheckedClass, 'Vml2YW11cyBmZXJtZtesting123')
        self.assertRaises(AssertionError, CheckedClass, '12345')
        self.assertRaises(AssertionError, CheckedClass, 'Zm9vYmFy====')

    def test_email(self):
        @checked
        def checkedmethod(a: email):
            return True

        self.assertTrue(checkedmethod('foo@bar.com'))
        self.assertTrue(checkedmethod('x@x.au'))
        self.assertTrue(checkedmethod('foo+bar@bar.com'))
        self.assertTrue(checkedmethod('foo@bar.中文网'))
        self.assertTrue(checkedmethod('hans.m端ller@test.com'))
        self.assertTrue(checkedmethod('test+ext@gmail.com'))
        self.assertTrue(checkedmethod('NATHAN.DAVIES@DOMAIN.CO.UK'))

        self.assertRaises(AssertionError, checkedmethod, 'invalidemail@')
        self.assertRaises(AssertionError, checkedmethod, '@invalid.com')
        self.assertRaises(AssertionError, checkedmethod, 'invalid.com')
        self.assertRaises(AssertionError, checkedmethod, 'foo@bar.coffee..coffee')

        class CheckedClass(ValidusBase):
            a: email

        self.assertTrue(CheckedClass('foo@bar.com'))
        self.assertTrue(CheckedClass('x@x.au'))
        self.assertTrue(CheckedClass('foo+bar@bar.com'))
        self.assertTrue(CheckedClass('foo@bar.中文网'))
        self.assertTrue(CheckedClass('hans.m端ller@test.com'))
        self.assertTrue(CheckedClass('test+ext@gmail.com'))
        self.assertTrue(CheckedClass('NATHAN.DAVIES@DOMAIN.CO.UK'))

        self.assertRaises(AssertionError, CheckedClass, 'invalidemail@')
        self.assertRaises(AssertionError, CheckedClass, '@invalid.com')
        self.assertRaises(AssertionError, CheckedClass, 'invalid.com')
        self.assertRaises(AssertionError, CheckedClass, 'foo@bar.coffee..coffee')

    def test_hexadecimal(self):
        @checked
        def checkedmethod(a: hexadecimal):
            return True

        self.assertTrue(checkedmethod('deadBEEF'))
        self.assertTrue(checkedmethod('ff0044'))

        self.assertRaises(AssertionError, checkedmethod, 'abcdefg')
        self.assertRaises(AssertionError, checkedmethod, '..')

        class CheckedClass(ValidusBase):
            a: hexadecimal

        self.assertTrue(CheckedClass('deadBEEF'))
        self.assertTrue(CheckedClass('ff0044'))

        self.assertRaises(AssertionError, CheckedClass, 'abcdefg')
        self.assertRaises(AssertionError, CheckedClass, '..')

    def test_hexcolor(self):
        @checked
        def checkedmethod(a: hexcolor):
            return True

        self.assertTrue(checkedmethod('#ff0034'))
        self.assertTrue(checkedmethod('#eeeeee'))
        self.assertTrue(checkedmethod('#f00'))
        self.assertTrue(checkedmethod('#fff'))
        self.assertTrue(checkedmethod('#000'))

        self.assertRaises(AssertionError, checkedmethod, '#ff')
        self.assertRaises(AssertionError, checkedmethod, 'fff0')
        self.assertRaises(AssertionError, checkedmethod, '#ff12FG')

        class CheckedClass(ValidusBase):
            a: hexcolor

        self.assertTrue(CheckedClass('#ff0034'))
        self.assertTrue(CheckedClass('#eeeeee'))
        self.assertTrue(CheckedClass('#f00'))
        self.assertTrue(CheckedClass('#fff'))
        self.assertTrue(CheckedClass('#000'))

        self.assertRaises(AssertionError, CheckedClass, '#ff')
        self.assertRaises(AssertionError, CheckedClass, 'fff0')
        self.assertRaises(AssertionError, CheckedClass, '#ff12FG')

    def test_rgbcolor(self):
        @checked
        def checkedmethod(a: rgbcolor):
            return True

        self.assertTrue(checkedmethod('rgb(0,31,255)'))
        self.assertTrue(checkedmethod('rgb(0,100,255)'))
        self.assertTrue(checkedmethod('rgb(0,0,255)'))
        self.assertTrue(checkedmethod('rgb(155,133,255)'))
        self.assertTrue(checkedmethod('rgb(255,255,255)'))
        self.assertTrue(checkedmethod('rgb(0,0,0)'))

        self.assertRaises(AssertionError, checkedmethod, 'rgb(1,349,275)')
        self.assertRaises(AssertionError, checkedmethod, 'rgb(01,31,255)')
        self.assertRaises(AssertionError, checkedmethod, 'rgb(0.6,31,255)')

        class CheckedClass(ValidusBase):
            a: rgbcolor

        self.assertTrue(CheckedClass('rgb(0,31,255)'))
        self.assertTrue(CheckedClass('rgb(0,100,255)'))
        self.assertTrue(CheckedClass('rgb(0,0,255)'))
        self.assertTrue(CheckedClass('rgb(155,133,255)'))
        self.assertTrue(CheckedClass('rgb(255,255,255)'))
        self.assertTrue(CheckedClass('rgb(0,0,0)'))

        self.assertRaises(AssertionError, CheckedClass, 'rgb(1,349,275)')
        self.assertRaises(AssertionError, CheckedClass, 'rgb(01,31,255)')
        self.assertRaises(AssertionError, CheckedClass, 'rgb(0.6,31,255)')

    def test_integer(self):
        @checked
        def checkedmethod(a: integer):
            return True

        self.assertTrue(checkedmethod('-2147483648'))
        self.assertTrue(checkedmethod('2147483647'))
        self.assertTrue(checkedmethod('-2147483649'))
        self.assertTrue(checkedmethod('2147483648'))
        self.assertTrue(checkedmethod('-9223372036854775808'))
        self.assertTrue(checkedmethod('9223372036854775807'))
        self.assertTrue(checkedmethod('18446744073709551615'))
        self.assertTrue(checkedmethod('123'))

        self.assertRaises(AssertionError, checkedmethod, '000')
        self.assertRaises(AssertionError, checkedmethod, '123.123')
        self.assertRaises(AssertionError, checkedmethod, '100e10')

        class CheckedClass(ValidusBase):
            a: integer

        self.assertTrue(CheckedClass('-2147483648'))
        self.assertTrue(CheckedClass('2147483647'))
        self.assertTrue(CheckedClass('-2147483649'))
        self.assertTrue(CheckedClass('2147483648'))
        self.assertTrue(CheckedClass('-9223372036854775808'))
        self.assertTrue(CheckedClass('9223372036854775807'))
        self.assertTrue(CheckedClass('18446744073709551615'))
        self.assertTrue(CheckedClass('123'))

        self.assertRaises(AssertionError, CheckedClass, '000')
        self.assertRaises(AssertionError, CheckedClass, '123.123')
        self.assertRaises(AssertionError, CheckedClass, '100e10')

    def test_real(self):
        @checked
        def checkedmethod(a: real):
            return True

        self.assertTrue(checkedmethod('123.123'))
        self.assertTrue(checkedmethod('-123.123'))
        self.assertTrue(checkedmethod('-0.123'))
        self.assertTrue(checkedmethod('01.123'))
        self.assertTrue(checkedmethod('-0.22250738585072011e-307'))

        self.assertRaises(AssertionError, checkedmethod, 'foo')
        self.assertRaises(AssertionError, checkedmethod, '+1f')
        self.assertRaises(AssertionError, checkedmethod, 'abacaba')
        self.assertRaises(AssertionError, checkedmethod, '-.123')

        class CheckedClass(ValidusBase):
            a: real

        self.assertTrue(CheckedClass('123.123'))
        self.assertTrue(CheckedClass('-123.123'))
        self.assertTrue(CheckedClass('-0.123'))
        self.assertTrue(CheckedClass('01.123'))
        self.assertTrue(CheckedClass('-0.22250738585072011e-307'))

        self.assertRaises(AssertionError, CheckedClass, 'foo')
        self.assertRaises(AssertionError, CheckedClass, '+1f')
        self.assertRaises(AssertionError, CheckedClass, 'abacaba')
        self.assertRaises(AssertionError, CheckedClass, '-.123')

    def test_slug(self):
        @checked
        def checkedmethod(a: slug):
            return True

        self.assertTrue(checkedmethod('123-12312-asdasda'))
        self.assertTrue(checkedmethod('123____123'))
        self.assertTrue(checkedmethod('dsadasd-dsadas'))

        self.assertRaises(AssertionError, checkedmethod, 'some.slug')
        self.assertRaises(AssertionError, checkedmethod, '1231321%')
        self.assertRaises(AssertionError, checkedmethod, '123asda&')

        class CheckedClass(ValidusBase):
            a: slug

        self.assertTrue(CheckedClass('123-12312-asdasda'))
        self.assertTrue(CheckedClass('123____123'))
        self.assertTrue(CheckedClass('dsadasd-dsadas'))

        self.assertRaises(AssertionError, CheckedClass, 'some.slug')
        self.assertRaises(AssertionError, CheckedClass, '1231321%')
        self.assertRaises(AssertionError, CheckedClass, '123asda&')

    def test_uuid(self):
        @checked
        def checkedmethod(a: uuid):
            return True

        self.assertTrue(checkedmethod('a987fbc9-4bed-3078-cf07-9141ba07c9f3'))
        self.assertTrue(checkedmethod('A987FBC9-4BED-4078-8F07-9141BA07C9F3'))
        self.assertTrue(checkedmethod('A987FBC9-4BED-5078-AF07-9141BA07C9F3'))

        self.assertRaises(AssertionError, checkedmethod, 'xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3')
        self.assertRaises(AssertionError, checkedmethod, 'A987FBC9-4BED-3078-CF07-9141BA07C9F3xxx')
        self.assertRaises(AssertionError, checkedmethod, 'A987FBC94BED3078CF079141BA07C9F3')

        class CheckedClass(ValidusBase):
            a: uuid

        self.assertTrue(CheckedClass('a987fbc9-4bed-3078-cf07-9141ba07c9f3'))
        self.assertTrue(CheckedClass('A987FBC9-4BED-4078-8F07-9141BA07C9F3'))
        self.assertTrue(CheckedClass('A987FBC9-4BED-5078-AF07-9141BA07C9F3'))

        self.assertRaises(AssertionError, CheckedClass, 'xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3')
        self.assertRaises(AssertionError, CheckedClass, 'A987FBC9-4BED-3078-CF07-9141BA07C9F3xxx')
        self.assertRaises(AssertionError, CheckedClass, 'A987FBC94BED3078CF079141BA07C9F3')

    def test_uuid3(self):
        @checked
        def checkedmethod(a: uuid3):
            return True

        self.assertTrue(checkedmethod('A987FBC9-4BED-3078-CF07-9141BA07C9F3'))

        self.assertRaises(AssertionError, checkedmethod, 'xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3')
        self.assertRaises(AssertionError, checkedmethod, 'A987FBC9-4BED-4078-8F07-9141BA07C9F3')

        class CheckedClass(ValidusBase):
            a: uuid3

        self.assertTrue(CheckedClass('A987FBC9-4BED-3078-CF07-9141BA07C9F3'))

        self.assertRaises(AssertionError, CheckedClass, 'xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3')
        self.assertRaises(AssertionError, CheckedClass, 'A987FBC9-4BED-4078-8F07-9141BA07C9F3')

    def test_uuid4(self):
        @checked
        def checkedmethod(a: uuid4):
            return True

        self.assertTrue(checkedmethod('713ae7e3-cb32-45f9-adcb-7c4fa86b90c1'))
        self.assertTrue(checkedmethod('625e63f3-58f5-40b7-83a1-a72ad31acffb'))
        self.assertTrue(checkedmethod('57b73598-8764-4ad0-a76a-679bb6640eb1'))
        self.assertTrue(checkedmethod('9c858901-8a57-4791-81fe-4c455b099bc9'))

        self.assertRaises(AssertionError, checkedmethod, 'xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3')
        self.assertRaises(AssertionError, checkedmethod, 'A987FBC9-4BED-3078-CF07-9141BA07C9F3')
        self.assertRaises(AssertionError, checkedmethod, 'A987FBC9-4BED-5078-AF07-9141BA07C9F3')
        self.assertRaises(AssertionError, checkedmethod, 'AAAAAAAA-1111-1111-AAAG-111111111111')

        class CheckedClass(ValidusBase):
            a: uuid4

        self.assertTrue(CheckedClass('713ae7e3-cb32-45f9-adcb-7c4fa86b90c1'))
        self.assertTrue(CheckedClass('625e63f3-58f5-40b7-83a1-a72ad31acffb'))
        self.assertTrue(CheckedClass('57b73598-8764-4ad0-a76a-679bb6640eb1'))
        self.assertTrue(CheckedClass('9c858901-8a57-4791-81fe-4c455b099bc9'))

        self.assertRaises(AssertionError, CheckedClass, 'xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3')
        self.assertRaises(AssertionError, CheckedClass, 'A987FBC9-4BED-3078-CF07-9141BA07C9F3')
        self.assertRaises(AssertionError, CheckedClass, 'A987FBC9-4BED-5078-AF07-9141BA07C9F3')
        self.assertRaises(AssertionError, CheckedClass, 'AAAAAAAA-1111-1111-AAAG-111111111111')

    def test_uuid5(self):
        @checked
        def checkedmethod(a: uuid5):
            return True

        self.assertTrue(checkedmethod('987FBC97-4BED-5078-AF07-9141BA07C9F3'))
        self.assertTrue(checkedmethod('987FBC97-4BED-5078-BF07-9141BA07C9F3'))
        self.assertTrue(checkedmethod('987FBC97-4BED-5078-9F07-9141BA07C9F3'))
        self.assertTrue(checkedmethod('987FBC97-4BED-5078-8F07-9141BA07C9F3'))

        self.assertRaises(AssertionError, checkedmethod, 'xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3')
        self.assertRaises(AssertionError, checkedmethod, 'AAAAAAAA-1111-1111-AAAG-111111111111')
        self.assertRaises(AssertionError, checkedmethod, '9c858901-8a57-4791-81fe-4c455b099bc9')
        self.assertRaises(AssertionError, checkedmethod, 'A987FBC9-4BED-3078-CF07-9141BA07C9F3')

        class CheckedClass(ValidusBase):
            a: uuid5

        self.assertTrue(CheckedClass('987FBC97-4BED-5078-AF07-9141BA07C9F3'))
        self.assertTrue(CheckedClass('987FBC97-4BED-5078-BF07-9141BA07C9F3'))
        self.assertTrue(CheckedClass('987FBC97-4BED-5078-9F07-9141BA07C9F3'))
        self.assertTrue(CheckedClass('987FBC97-4BED-5078-8F07-9141BA07C9F3'))

        self.assertRaises(AssertionError, CheckedClass, 'xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3')
        self.assertRaises(AssertionError, CheckedClass, 'AAAAAAAA-1111-1111-AAAG-111111111111')
        self.assertRaises(AssertionError, CheckedClass, '9c858901-8a57-4791-81fe-4c455b099bc9')
        self.assertRaises(AssertionError, CheckedClass, 'A987FBC9-4BED-3078-CF07-9141BA07C9F3')

    def test_fullwidth(self):
        @checked
        def checkedmethod(a: fullwidth):
            return True

        self.assertTrue(checkedmethod('ひらがな・カタカナ、．漢字'))
        self.assertTrue(checkedmethod('３ー０　ａ＠ｃｏｍ'))
        self.assertTrue(checkedmethod('Ｆｶﾀｶﾅﾞﾬ'))

        self.assertRaises(AssertionError, checkedmethod, 'abc')
        self.assertRaises(AssertionError, checkedmethod, 'abc123')

        class CheckedClass(ValidusBase):
            a: fullwidth

        self.assertTrue(CheckedClass('ひらがな・カタカナ、．漢字'))
        self.assertTrue(CheckedClass('３ー０　ａ＠ｃｏｍ'))
        self.assertTrue(CheckedClass('Ｆｶﾀｶﾅﾞﾬ'))

        self.assertRaises(AssertionError, CheckedClass, 'abc')
        self.assertRaises(AssertionError, CheckedClass, 'abc123')

    def test_halfwidth(self):
        @checked
        def checkedmethod(a: halfwidth):
            return True

        self.assertTrue(checkedmethod('l-btn_02--active'))
        self.assertTrue(checkedmethod('abc123い'))
        self.assertTrue(checkedmethod('ｶﾀｶﾅﾞﾬ￩'))

        self.assertRaises(AssertionError, checkedmethod, 'あいうえお')
        self.assertRaises(AssertionError, checkedmethod, '００１１')

        class CheckedClass(ValidusBase):
            a: halfwidth

        self.assertTrue(CheckedClass('l-btn_02--active'))
        self.assertTrue(CheckedClass('abc123い'))
        self.assertTrue(CheckedClass('ｶﾀｶﾅﾞﾬ￩'))

        self.assertRaises(AssertionError, CheckedClass, 'あいうえお')
        self.assertRaises(AssertionError, CheckedClass, '００１１')

    def test_latitude(self):
        @checked
        def checkedmethod(a: latitude):
            return True

        self.assertTrue(checkedmethod('-90.000'))
        self.assertTrue(checkedmethod('+90'))
        self.assertTrue(checkedmethod('47.1231231'))

        self.assertRaises(AssertionError, checkedmethod, '+99.9')
        self.assertRaises(AssertionError, checkedmethod, '108')

        class CheckedClass(ValidusBase):
            a: latitude

        self.assertTrue(CheckedClass('-90.000'))
        self.assertTrue(CheckedClass('+90'))
        self.assertTrue(CheckedClass('47.1231231'))

        self.assertRaises(AssertionError, CheckedClass, '+99.9')
        self.assertRaises(AssertionError, CheckedClass, '108')

    def test_longitude(self):
        @checked
        def checkedmethod(a: longitude):
            return True

        self.assertTrue(checkedmethod('+73.234'))
        self.assertTrue(checkedmethod('-180.000'))
        self.assertTrue(checkedmethod('23.11111111'))

        self.assertRaises(AssertionError, checkedmethod, '180.1')
        self.assertRaises(AssertionError, checkedmethod, '+382.3811')

        class CheckedClass(ValidusBase):
            a: longitude

        self.assertTrue(CheckedClass('+73.234'))
        self.assertTrue(CheckedClass('-180.000'))
        self.assertTrue(CheckedClass('23.11111111'))

        self.assertRaises(AssertionError, CheckedClass, '180.1')
        self.assertRaises(AssertionError, CheckedClass, '+382.3811')

    def test_mac(self):
        @checked
        def checkedmethod(a: mac):
            return True

        self.assertTrue(checkedmethod('3D:F2:C9:A6:B3:4F'))
        self.assertTrue(checkedmethod('FF:FF:FF:FF:FF:FF'))
        self.assertTrue(checkedmethod('01:02:03:04:05:ab'))
        self.assertTrue(checkedmethod('01:AB:03:04:05:06'))

        self.assertRaises(AssertionError, checkedmethod, '01:02:03:04:05')
        self.assertRaises(AssertionError, checkedmethod, '01:02:03:04::ab')
        self.assertRaises(AssertionError, checkedmethod, '1:2:3:4:5:6')
        self.assertRaises(AssertionError, checkedmethod, 'AB:CD:EF:GH:01:02')

        class CheckedClass(ValidusBase):
            a: mac

        self.assertTrue(CheckedClass('3D:F2:C9:A6:B3:4F'))
        self.assertTrue(CheckedClass('FF:FF:FF:FF:FF:FF'))
        self.assertTrue(CheckedClass('01:02:03:04:05:ab'))
        self.assertTrue(CheckedClass('01:AB:03:04:05:06'))

        self.assertRaises(AssertionError, CheckedClass, '01:02:03:04:05')
        self.assertRaises(AssertionError, CheckedClass, '01:02:03:04::ab')
        self.assertRaises(AssertionError, CheckedClass, '1:2:3:4:5:6')
        self.assertRaises(AssertionError, CheckedClass, 'AB:CD:EF:GH:01:02')

    def test_md5(self):
        @checked
        def checkedmethod(a: md5):
            return True

        self.assertTrue(checkedmethod('d94f3f016ae679c3008de268209132f2'))
        self.assertTrue(checkedmethod('751adbc511ccbe8edf23d486fa4581cd'))
        self.assertTrue(checkedmethod('88dae00e614d8f24cfd5a8b3f8002e93'))
        self.assertTrue(checkedmethod('0bf1c35032a71a14c2f719e5a14c1e96'))

        self.assertRaises(AssertionError, checkedmethod, 'KYT0bf1c35032a71a14c2f719e5a14c1')
        self.assertRaises(AssertionError, checkedmethod, 'q94375dj93458w34')
        self.assertRaises(AssertionError, checkedmethod, '39485729348')
        self.assertRaises(AssertionError, checkedmethod, '%&FHKJFvk')

        class CheckedClass(ValidusBase):
            a: md5

        self.assertTrue(CheckedClass('d94f3f016ae679c3008de268209132f2'))
        self.assertTrue(CheckedClass('751adbc511ccbe8edf23d486fa4581cd'))
        self.assertTrue(CheckedClass('88dae00e614d8f24cfd5a8b3f8002e93'))
        self.assertTrue(CheckedClass('0bf1c35032a71a14c2f719e5a14c1e96'))

        self.assertRaises(AssertionError, CheckedClass, 'KYT0bf1c35032a71a14c2f719e5a14c1')
        self.assertRaises(AssertionError, CheckedClass, 'q94375dj93458w34')
        self.assertRaises(AssertionError, CheckedClass, '39485729348')
        self.assertRaises(AssertionError, CheckedClass, '%&FHKJFvk')

    def test_sha1(self):
        @checked
        def checkedmethod(a: sha1):
            return True

        self.assertTrue(checkedmethod('1bc6b8a58b484bdb6aa5264dc554934e3e46c405'))
        self.assertTrue(checkedmethod('d545e28504c797ee8f26d3f482ea1a2485d0b018'))
        self.assertTrue(checkedmethod('56Dae00e614d8F24dfd544483f209a2D9e21e57A'))

        self.assertRaises(AssertionError, checkedmethod, 'd545e28504c797ee8f26d3f482ea1a2485d0b018777')
        self.assertRaises(AssertionError, checkedmethod, 'ZKYT059dbf1c356032a7b1a1d4c2f719e5a14c1')
        self.assertRaises(AssertionError, checkedmethod, 'q94375dj93458w34')
        self.assertRaises(AssertionError, checkedmethod, '84375958454')
        self.assertRaises(AssertionError, checkedmethod, '*!FHPJFvc')

        class CheckedClass(ValidusBase):
            a: sha1

        self.assertTrue(CheckedClass('1bc6b8a58b484bdb6aa5264dc554934e3e46c405'))
        self.assertTrue(CheckedClass('d545e28504c797ee8f26d3f482ea1a2485d0b018'))
        self.assertTrue(CheckedClass('56Dae00e614d8F24dfd544483f209a2D9e21e57A'))

        self.assertRaises(AssertionError, CheckedClass, 'd545e28504c797ee8f26d3f482ea1a2485d0b018777')
        self.assertRaises(AssertionError, CheckedClass, 'ZKYT059dbf1c356032a7b1a1d4c2f719e5a14c1')
        self.assertRaises(AssertionError, CheckedClass, 'q94375dj93458w34')
        self.assertRaises(AssertionError, CheckedClass, '84375958454')
        self.assertRaises(AssertionError, CheckedClass, '*!FHPJFvc')

    def test_sha256(self):
        @checked
        def checkedmethod(a: sha256):
            return True

        self.assertTrue(checkedmethod('fd04c4a99b6b1f118452da33dfe9523ec164f5fecde4502b69f1ed3f24a29ff6'))
        self.assertTrue(checkedmethod('4523475627356732465783465723675623562365736592656273465926357236'))
        self.assertTrue(checkedmethod('AA090789a99b6b90789245234523C952ae856744352d32452b634F5D34a29fDD'))

        self.assertRaises(AssertionError, checkedmethod, 'fd04c4a99b6b1f118452da33dfe9523ec164f5fecde4502b6945f1ed3f24a29ff6')
        self.assertRaises(AssertionError, checkedmethod, 'q94375dj93458w34')
        self.assertRaises(AssertionError, checkedmethod, '84375958454')
        self.assertRaises(AssertionError, checkedmethod, '\\M$""')

        class CheckedClass(ValidusBase):
            a: sha256

        self.assertTrue(CheckedClass('fd04c4a99b6b1f118452da33dfe9523ec164f5fecde4502b69f1ed3f24a29ff6'))
        self.assertTrue(CheckedClass('4523475627356732465783465723675623562365736592656273465926357236'))
        self.assertTrue(CheckedClass('AA090789a99b6b90789245234523C952ae856744352d32452b634F5D34a29fDD'))

        self.assertRaises(AssertionError, CheckedClass, 'fd04c4a99b6b1f118452da33dfe9523ec164f5fecde4502b6945f1ed3f24a29ff6')
        self.assertRaises(AssertionError, CheckedClass, 'q94375dj93458w34')
        self.assertRaises(AssertionError, CheckedClass, '84375958454')
        self.assertRaises(AssertionError, CheckedClass, '\\M$""')

    def test_sha512(self):
        @checked
        def checkedmethod(a: sha512):
            return True

        self.assertTrue(checkedmethod('0b696861da778f6bd0d899ad9a581f4b9b1eb8286eaba266d2f2e2767539055bf8eb59e8884839a268141aba1ef078ce67cf94d421bd1195a3c0e817f5f7b286'))
        self.assertTrue(checkedmethod('45723405723485723475275235567576454134134684623196443436423641641242153645167451294512345912354123549123546125394125452194531293'))
        self.assertTrue(checkedmethod('AA090789a99b6b90789245234523C952ae856744352d32452b634F5D34a29fDDAA090789a99b6b90789245234523C952ae856744352d32452b634F5D34a29fDD'))

        self.assertRaises(AssertionError, checkedmethod, '0b696861da778f6bd0d899ad9a581f4b9b1eb8286eaba266d2f2e2767539055bf8eb59e8884839a268141aba1ef078ce67cf94d421bd1195a3c0e817f5f7b286555')
        self.assertRaises(AssertionError, checkedmethod, 'KLO4545ID55545789Hg545235F45255452Hgf76DJF56HgKJfg3456356356346534534653456sghey45656jhgjfgghdfhgdfhdfhdfhdfhghhq94375dj93458w34')
        self.assertRaises(AssertionError, checkedmethod, '975')
        self.assertRaises(AssertionError, checkedmethod, '*)^&!MNdf67657')

        class CheckedClass(ValidusBase):
            a: sha512

        self.assertTrue(CheckedClass('0b696861da778f6bd0d899ad9a581f4b9b1eb8286eaba266d2f2e2767539055bf8eb59e8884839a268141aba1ef078ce67cf94d421bd1195a3c0e817f5f7b286'))
        self.assertTrue(CheckedClass('45723405723485723475275235567576454134134684623196443436423641641242153645167451294512345912354123549123546125394125452194531293'))
        self.assertTrue(CheckedClass('AA090789a99b6b90789245234523C952ae856744352d32452b634F5D34a29fDDAA090789a99b6b90789245234523C952ae856744352d32452b634F5D34a29fDD'))

        self.assertRaises(AssertionError, CheckedClass, '0b696861da778f6bd0d899ad9a581f4b9b1eb8286eaba266d2f2e2767539055bf8eb59e8884839a268141aba1ef078ce67cf94d421bd1195a3c0e817f5f7b286555')
        self.assertRaises(AssertionError, CheckedClass, 'KLO4545ID55545789Hg545235F45255452Hgf76DJF56HgKJfg3456356356346534534653456sghey45656jhgjfgghdfhgdfhdfhdfhdfhghhq94375dj93458w34')
        self.assertRaises(AssertionError, CheckedClass, '975')
        self.assertRaises(AssertionError, CheckedClass, '*)^&!MNdf67657')

    def test_mongoid(self):
        @checked
        def checkedmethod(a: mongoid):
            return True

        self.assertTrue(checkedmethod('507f1f77bcf86cd799439011'))
        self.assertRaises(AssertionError, checkedmethod, '507f1f77bcf86cd7994390')
        self.assertRaises(AssertionError, checkedmethod, '507f1f77bcf86cd79943901z')

        class CheckedClass(ValidusBase):
            a: mongoid

        self.assertTrue(CheckedClass('507f1f77bcf86cd799439011'))
        self.assertRaises(AssertionError, CheckedClass, '507f1f77bcf86cd7994390')
        self.assertRaises(AssertionError, CheckedClass, '507f1f77bcf86cd79943901z')

    def test_iso8601(self):
        @checked
        def checkedmethod(a: iso8601):
            return True

        self.assertTrue(checkedmethod('2009-12T12:34'))
        self.assertTrue(checkedmethod('2009-05-19'))
        self.assertTrue(checkedmethod('20090519'))
        self.assertTrue(checkedmethod('2009-05-19 14:39:22-06:00'))
        self.assertTrue(checkedmethod('2009-05-19 14:39:22'))
        self.assertTrue(checkedmethod('2009-05-19 00:00'))
        self.assertTrue(checkedmethod('2009-W01-1'))

        self.assertRaises(AssertionError, checkedmethod, '2009367')
        self.assertRaises(AssertionError, checkedmethod, '2010-02-18T16:23.33.600')
        self.assertRaises(AssertionError, checkedmethod, '2009-05-19 14:39:22+06a00')
        self.assertRaises(AssertionError, checkedmethod, '2009-05-1914:39')
        self.assertRaises(AssertionError, checkedmethod, '2009-05-19T14a39r')
        self.assertRaises(AssertionError, checkedmethod, '2009-M511')
        self.assertRaises(AssertionError, checkedmethod, '2007-04-05T24:50')

        class CheckedClass(ValidusBase):
            a: iso8601

        self.assertTrue(CheckedClass('2009-12T12:34'))
        self.assertTrue(CheckedClass('2009-05-19'))
        self.assertTrue(CheckedClass('20090519'))
        self.assertTrue(CheckedClass('2009-05-19 14:39:22-06:00'))
        self.assertTrue(CheckedClass('2009-05-19 14:39:22'))
        self.assertTrue(CheckedClass('2009-05-19 00:00'))
        self.assertTrue(CheckedClass('2009-W01-1'))

        self.assertRaises(AssertionError, CheckedClass, '2009367')
        self.assertRaises(AssertionError, CheckedClass, '2010-02-18T16:23.33.600')
        self.assertRaises(AssertionError, CheckedClass, '2009-05-19 14:39:22+06a00')
        self.assertRaises(AssertionError, CheckedClass, '2009-05-1914:39')
        self.assertRaises(AssertionError, CheckedClass, '2009-05-19T14a39r')
        self.assertRaises(AssertionError, CheckedClass, '2009-M511')
        self.assertRaises(AssertionError, CheckedClass, '2007-04-05T24:50')

    def test_ipv4(self):
        @checked
        def checkedmethod(a: ipv4):
            return True

        self.assertTrue(checkedmethod('127.0.0.1'))
        self.assertTrue(checkedmethod('0.0.0.0'))
        self.assertTrue(checkedmethod('255.255.255.255'))
        self.assertTrue(checkedmethod('1.2.3.4'))

        self.assertRaises(AssertionError, checkedmethod, '::1')
        self.assertRaises(AssertionError, checkedmethod, '::ffff:127.0.0.1')
        self.assertRaises(AssertionError, checkedmethod, '2001:db8:0000:1:1:1:1:1')

        class CheckedClass(ValidusBase):
            a: ipv4

        self.assertTrue(CheckedClass('127.0.0.1'))
        self.assertTrue(CheckedClass('0.0.0.0'))
        self.assertTrue(CheckedClass('255.255.255.255'))
        self.assertTrue(CheckedClass('1.2.3.4'))

        self.assertRaises(AssertionError, CheckedClass, '::1')
        self.assertRaises(AssertionError, CheckedClass, '::ffff:127.0.0.1')
        self.assertRaises(AssertionError, CheckedClass, '2001:db8:0000:1:1:1:1:1')

    def test_ipv6(self):
        @checked
        def checkedmethod(a: ipv6):
            return True

        self.assertTrue(checkedmethod('2001:db8:0000:1:1:1:1:1'))
        self.assertTrue(checkedmethod('2001:41d0:2:a141::1'))

        self.assertRaises(AssertionError, checkedmethod, '127.0.0.1')
        self.assertRaises(AssertionError, checkedmethod, '1.2.3.4')

        class CheckedClass(ValidusBase):
            a: ipv6

        self.assertTrue(CheckedClass('2001:db8:0000:1:1:1:1:1'))
        self.assertTrue(CheckedClass('2001:41d0:2:a141::1'))

        self.assertRaises(AssertionError, CheckedClass, '127.0.0.1')
        self.assertRaises(AssertionError, CheckedClass, '1.2.3.4')

    def test_ip(self):
        @checked
        def checkedmethod(a: ip):
            return True

        self.assertTrue(checkedmethod('127.0.0.1'))
        self.assertTrue(checkedmethod('0.0.0.0'))
        self.assertTrue(checkedmethod('255.255.255.255'))
        self.assertTrue(checkedmethod('1.2.3.4'))
        self.assertTrue(checkedmethod('2001:db8:0000:1:1:1:1:1'))
        self.assertTrue(checkedmethod('2001:41d0:2:a141::1'))

        self.assertRaises(AssertionError, checkedmethod, 'abc')
        self.assertRaises(AssertionError, checkedmethod, '0200.200.200.200')
        self.assertRaises(AssertionError, checkedmethod, '26.0.0.256')
        self.assertRaises(AssertionError, checkedmethod, '256.0.0.0')
        self.assertRaises(AssertionError, checkedmethod, '1:1:1:1:1:1:1:1:1:1:1:1:1:1:1:1')

        class CheckedClass(ValidusBase):
            a: ip

        self.assertTrue(CheckedClass('127.0.0.1'))
        self.assertTrue(CheckedClass('0.0.0.0'))
        self.assertTrue(CheckedClass('255.255.255.255'))
        self.assertTrue(CheckedClass('1.2.3.4'))
        self.assertTrue(CheckedClass('2001:db8:0000:1:1:1:1:1'))
        self.assertTrue(CheckedClass('2001:41d0:2:a141::1'))

        self.assertRaises(AssertionError, CheckedClass, 'abc')
        self.assertRaises(AssertionError, CheckedClass, '0200.200.200.200')
        self.assertRaises(AssertionError, CheckedClass, '26.0.0.256')
        self.assertRaises(AssertionError, CheckedClass, '256.0.0.0')
        self.assertRaises(AssertionError, CheckedClass, '1:1:1:1:1:1:1:1:1:1:1:1:1:1:1:1')

    def test_port(self):
        @checked
        def checkedmethod(a: port):
            return True

        self.assertTrue(checkedmethod('1'))
        self.assertTrue(checkedmethod('65535'))
        self.assertTrue(checkedmethod('8080'))
        self.assertTrue(checkedmethod('3000'))
        self.assertTrue(checkedmethod('4000'))

        self.assertRaises(AssertionError, checkedmethod, '0')
        self.assertRaises(AssertionError, checkedmethod, '65536')
        self.assertRaises(AssertionError, checkedmethod, '65538')

        class CheckedClass(ValidusBase):
            a: port

        self.assertTrue(CheckedClass('1'))
        self.assertTrue(CheckedClass('65535'))
        self.assertTrue(CheckedClass('8080'))
        self.assertTrue(CheckedClass('3000'))
        self.assertTrue(CheckedClass('4000'))

        self.assertRaises(AssertionError, CheckedClass, '0')
        self.assertRaises(AssertionError, CheckedClass, '65536')
        self.assertRaises(AssertionError, CheckedClass, '65538')

    def test_dns(self):
        @checked
        def checkedmethod(a: dns):
            return True

        self.assertTrue(checkedmethod('localhost'))
        self.assertTrue(checkedmethod('ru.link.n.svpncloud.com'))
        self.assertTrue(checkedmethod('l.local.intern'))
        self.assertTrue(checkedmethod('localhost.local'))
        self.assertTrue(checkedmethod('a.bc'))

        self.assertRaises(AssertionError, checkedmethod, 'a.b..')
        self.assertRaises(AssertionError, checkedmethod, '-localhost')
        self.assertRaises(AssertionError, checkedmethod, 'localhost.-localdomain')
        self.assertRaises(AssertionError, checkedmethod, 'localhost.lÖcaldomain')
        self.assertRaises(AssertionError, checkedmethod, '127.0.0.1')

        class CheckedClass(ValidusBase):
            a: dns

        self.assertTrue(CheckedClass('localhost'))
        self.assertTrue(CheckedClass('ru.link.n.svpncloud.com'))
        self.assertTrue(CheckedClass('l.local.intern'))
        self.assertTrue(CheckedClass('localhost.local'))
        self.assertTrue(CheckedClass('a.bc'))

        self.assertRaises(AssertionError, CheckedClass, 'a.b..')
        self.assertRaises(AssertionError, CheckedClass, '-localhost')
        self.assertRaises(AssertionError, CheckedClass, 'localhost.-localdomain')
        self.assertRaises(AssertionError, CheckedClass, 'localhost.lÖcaldomain')
        self.assertRaises(AssertionError, CheckedClass, '127.0.0.1')

    def test_ssn(self):
        @checked
        def checkedmethod(a: ssn):
            return True

        self.assertTrue(checkedmethod('191 60 2869'))
        self.assertTrue(checkedmethod('191-60-2869'))

        self.assertRaises(AssertionError, checkedmethod, '66690-76')
        self.assertRaises(AssertionError, checkedmethod, '00-90-8787')

        class CheckedClass(ValidusBase):
            a: ssn

        self.assertTrue(CheckedClass('191 60 2869'))
        self.assertTrue(CheckedClass('191-60-2869'))

        self.assertRaises(AssertionError, CheckedClass, '66690-76')
        self.assertRaises(AssertionError, CheckedClass, '00-90-8787')

    def test_semver(self):
        @checked
        def checkedmethod(a: semver):
            return True

        self.assertTrue(checkedmethod('v1.0.0'))
        self.assertTrue(checkedmethod('1.0.0'))
        self.assertTrue(checkedmethod('1.0.0-alpha'))
        self.assertTrue(checkedmethod('1.0.0-alpha.1'))
        self.assertTrue(checkedmethod('1.0.0-0.3.7'))
        self.assertTrue(checkedmethod('1.0.0-x.7.z.92'))
        self.assertTrue(checkedmethod('1.0.0-beta+exp.sha.5114f85'))

        self.assertRaises(AssertionError, checkedmethod, '1.1.01')
        self.assertRaises(AssertionError, checkedmethod, '1.01.0')
        self.assertRaises(AssertionError, checkedmethod, '01.1.0')
        self.assertRaises(AssertionError, checkedmethod, 'v1.1.01')
        self.assertRaises(AssertionError, checkedmethod, 'v1.01.0')
        self.assertRaises(AssertionError, checkedmethod, 'v01.1.0')
        self.assertRaises(AssertionError, checkedmethod, '1.0.0-00.3.7')

        class CheckedClass(ValidusBase):
            a: semver

        self.assertTrue(CheckedClass('v1.0.0'))
        self.assertTrue(CheckedClass('1.0.0'))
        self.assertTrue(CheckedClass('1.0.0-alpha'))
        self.assertTrue(CheckedClass('1.0.0-alpha.1'))
        self.assertTrue(CheckedClass('1.0.0-0.3.7'))
        self.assertTrue(CheckedClass('1.0.0-x.7.z.92'))
        self.assertTrue(CheckedClass('1.0.0-beta+exp.sha.5114f85'))

        self.assertRaises(AssertionError, CheckedClass, '1.1.01')
        self.assertRaises(AssertionError, CheckedClass, '1.01.0')
        self.assertRaises(AssertionError, CheckedClass, '01.1.0')
        self.assertRaises(AssertionError, CheckedClass, 'v1.1.01')
        self.assertRaises(AssertionError, CheckedClass, 'v1.01.0')
        self.assertRaises(AssertionError, CheckedClass, 'v01.1.0')
        self.assertRaises(AssertionError, CheckedClass, '1.0.0-00.3.7')

    def test_multibyte(self):
        @checked
        def checkedmethod(a: multibyte):
            return True

        self.assertTrue(checkedmethod('ひらがな・カタカナ、．漢字'))
        self.assertTrue(checkedmethod('あいうえお foobar'))
        self.assertTrue(checkedmethod('ｶﾀｶﾅ'))
        self.assertTrue(checkedmethod('中文'))

        self.assertRaises(AssertionError, checkedmethod, 'abc')
        self.assertRaises(AssertionError, checkedmethod, 'abc123')
        self.assertRaises(AssertionError, checkedmethod, '<>@" *.')
        self.assertRaises(AssertionError, checkedmethod, '<>@;.-=')

        class CheckedClass(ValidusBase):
            a: multibyte

        self.assertTrue(CheckedClass('ひらがな・カタカナ、．漢字'))
        self.assertTrue(CheckedClass('あいうえお foobar'))
        self.assertTrue(CheckedClass('ｶﾀｶﾅ'))
        self.assertTrue(CheckedClass('中文'))

        self.assertRaises(AssertionError, CheckedClass, 'abc')
        self.assertRaises(AssertionError, CheckedClass, 'abc123')
        self.assertRaises(AssertionError, CheckedClass, '<>@" *.')
        self.assertRaises(AssertionError, CheckedClass, '<>@;.-=')

    def test_filepath(self):
        @checked
        def checkedmethod(a: filepath):
            return True

        self.assertTrue(checkedmethod('c:\\path\\file (x86)\\bar'))
        self.assertTrue(checkedmethod('c:\\path\\file'))
        #self.assertTrue(checkedmethod('C:\\'))
        #self.assertTrue(checkedmethod('c:\\path\\file\\'))
        self.assertTrue(checkedmethod('/path/file/'))
        self.assertTrue(checkedmethod('/path'))
        self.assertTrue(checkedmethod('/path/__bc/file.txt'))
        self.assertTrue(checkedmethod('/path/file:/.txt'))
        self.assertTrue(checkedmethod('/path/file:SAMPLE/'))
        self.assertTrue(checkedmethod('c:\\path\\file:exe'))
        self.assertTrue(checkedmethod('c:/path/file/'))

        class CheckedClass(ValidusBase):
            a: filepath

        self.assertTrue(CheckedClass('c:\\path\\file (x86)\\bar'))
        self.assertTrue(CheckedClass('c:\\path\\file'))
        #self.assertTrue(CheckedClass('C:\\'))
        #self.assertTrue(CheckedClass('c:\\path\\file\\'))
        self.assertTrue(CheckedClass('/path/file/'))
        self.assertTrue(CheckedClass('/path'))
        self.assertTrue(CheckedClass('/path/__bc/file.txt'))
        self.assertTrue(CheckedClass('/path/file:/.txt'))
        self.assertTrue(CheckedClass('/path/file:SAMPLE/'))
        self.assertTrue(CheckedClass('c:\\path\\file:exe'))
        self.assertTrue(CheckedClass('c:/path/file/'))

    def test_datauri(self):
        @checked
        def checkedmethod(a: datauri):
            return True

        self.assertTrue(checkedmethod('data:image/png;base64,TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4='))
        self.assertTrue(checkedmethod('data:text/plain;base64,Vml2YW11cyBmZXJtZW50dW0gc2VtcGVyIHBvcnRhLg=='))
        self.assertTrue(checkedmethod('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC'))
        self.assertTrue(checkedmethod('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIBAMAAAA2IaO4AAAAFVBMVEXk5OTn5+ft7e319fX29vb5+fn///++GUmVAAAALUlEQVQIHWNICnYLZnALTgpmMGYIFWYIZTA2ZFAzTTFlSDFVMwVyQhmAwsYMAKDaBy0axX/iAAAAAElFTkSuQmCC'))
        self.assertTrue(checkedmethod('data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22100%22%20height%3D%22100%22%3E%3Crect%20fill%3D%22%2300B1FF%22%20width%3D%22100%22%20height%3D%22100%22%2F%3E%3C%2Fsvg%3E'))
        self.assertTrue(checkedmethod('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIj48cmVjdCBmaWxsPSIjMDBCMUZGIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIvPjwvc3ZnPg=='))
        self.assertTrue(checkedmethod('data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D'))
        self.assertTrue(checkedmethod('data:text/html,%3Ch1%3EHello%2C%20World!%3C%2Fh1%3E'))

        self.assertRaises(AssertionError, checkedmethod, 'dataxbase64')
        self.assertRaises(AssertionError, checkedmethod, 'dataxbase64data:HelloWorld')
        self.assertRaises(AssertionError, checkedmethod, 'data:base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC')
        self.assertRaises(AssertionError, checkedmethod, 'data:text/html;charset=,%3Ch1%3EHello!%3C%2Fh1%3E')
        self.assertRaises(AssertionError, checkedmethod, 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC')

        class CheckedClass(ValidusBase):
            a: datauri

        self.assertTrue(CheckedClass('data:image/png;base64,TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4='))
        self.assertTrue(CheckedClass('data:text/plain;base64,Vml2YW11cyBmZXJtZW50dW0gc2VtcGVyIHBvcnRhLg=='))
        self.assertTrue(CheckedClass('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC'))
        self.assertTrue(CheckedClass('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIBAMAAAA2IaO4AAAAFVBMVEXk5OTn5+ft7e319fX29vb5+fn///++GUmVAAAALUlEQVQIHWNICnYLZnALTgpmMGYIFWYIZTA2ZFAzTTFlSDFVMwVyQhmAwsYMAKDaBy0axX/iAAAAAElFTkSuQmCC'))
        self.assertTrue(CheckedClass('data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22100%22%20height%3D%22100%22%3E%3Crect%20fill%3D%22%2300B1FF%22%20width%3D%22100%22%20height%3D%22100%22%2F%3E%3C%2Fsvg%3E'))
        self.assertTrue(CheckedClass('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIj48cmVjdCBmaWxsPSIjMDBCMUZGIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIvPjwvc3ZnPg=='))
        self.assertTrue(CheckedClass('data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D'))
        self.assertTrue(CheckedClass('data:text/html,%3Ch1%3EHello%2C%20World!%3C%2Fh1%3E'))

        self.assertRaises(AssertionError, CheckedClass, 'dataxbase64')
        self.assertRaises(AssertionError, CheckedClass, 'dataxbase64data:HelloWorld')
        self.assertRaises(AssertionError, CheckedClass, 'data:base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC')
        self.assertRaises(AssertionError, CheckedClass, 'data:text/html;charset=,%3Ch1%3EHello!%3C%2Fh1%3E')
        self.assertRaises(AssertionError, CheckedClass, 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC')

    def test_json(self):
        @checked
        def checkedmethod(a: json):
            return True

        self.assertTrue(checkedmethod('{"Name":"Alice","Body":"Hello","Time":1294706395881547000}'))
        self.assertTrue(checkedmethod('{"Key": {"Key": {"Key": 123}}}'))
        self.assertTrue(checkedmethod('{ "key": "value" }'))

        self.assertRaises(AssertionError, checkedmethod, '{ key: "value" }')
        #self.assertRaises(AssertionError, checkedmethod, '{ \'key\': \'value\' }')

        class CheckedClass(ValidusBase):
            a: json

        self.assertTrue(CheckedClass('{"Name":"Alice","Body":"Hello","Time":1294706395881547000}'))
        self.assertTrue(CheckedClass('{"Key": {"Key": {"Key": 123}}}'))
        self.assertTrue(CheckedClass('{ "key": "value" }'))

        self.assertRaises(AssertionError, CheckedClass, '{ key: "value" }')
        #self.assertRaises(AssertionError, CheckedClass, '{ \'key\': \'value\' }')

    def test_url(self):
        @checked
        def checkedmethod(a: url):
            return True

        self.assertTrue(checkedmethod('http://foo.bar#com'))
        self.assertTrue(checkedmethod('http://foobar.com'))
        self.assertTrue(checkedmethod('https://foobar.org'))
        self.assertTrue(checkedmethod('ftp://foobar.ru/'))
        self.assertTrue(checkedmethod('http://duckduckgo.com/?q=%2F'))
        self.assertTrue(checkedmethod('http://user:pass@www.foobar.com/'))
        self.assertTrue(checkedmethod('http://www.xn--froschgrn-x9a.net/'))
        self.assertTrue(checkedmethod('http://foobar.中文网/'))
        self.assertTrue(checkedmethod('http://localhost:3000/'))
        self.assertTrue(checkedmethod('irc://#channel@network'))

        self.assertRaises(AssertionError, checkedmethod, 'http://foobar.c_o_m')
        self.assertRaises(AssertionError, checkedmethod, 'xyz://foobar.com')
        self.assertRaises(AssertionError, checkedmethod, 'rtmp://foobar.com')
        self.assertRaises(AssertionError, checkedmethod, 'http://www.foo---bar.com/')
        self.assertRaises(AssertionError, checkedmethod, 'http://www.foo_bar.com/')
        self.assertRaises(AssertionError, checkedmethod, 'http://foo bar.org')
        self.assertRaises(AssertionError, checkedmethod, 'http://.foo.com')

        class CheckedClass(ValidusBase):
            a: url

        self.assertTrue(CheckedClass('http://foo.bar#com'))
        self.assertTrue(CheckedClass('http://foobar.com'))
        self.assertTrue(CheckedClass('https://foobar.org'))
        self.assertTrue(CheckedClass('ftp://foobar.ru/'))
        self.assertTrue(CheckedClass('http://duckduckgo.com/?q=%2F'))
        self.assertTrue(CheckedClass('http://user:pass@www.foobar.com/'))
        self.assertTrue(CheckedClass('http://www.xn--froschgrn-x9a.net/'))
        self.assertTrue(CheckedClass('http://foobar.中文网/'))
        self.assertTrue(CheckedClass('http://localhost:3000/'))
        self.assertTrue(CheckedClass('irc://#channel@network'))

        self.assertRaises(AssertionError, CheckedClass, 'http://foobar.c_o_m')
        self.assertRaises(AssertionError, CheckedClass, 'xyz://foobar.com')
        self.assertRaises(AssertionError, CheckedClass, 'rtmp://foobar.com')
        self.assertRaises(AssertionError, CheckedClass, 'http://www.foo---bar.com/')
        self.assertRaises(AssertionError, CheckedClass, 'http://www.foo_bar.com/')
        self.assertRaises(AssertionError, CheckedClass, 'http://foo bar.org')
        self.assertRaises(AssertionError, CheckedClass, 'http://.foo.com')

    def test_crcard(self):
        @checked
        def checkedmethod(a: crcard):
            return True

        self.assertTrue(checkedmethod('375556917985515'))
        self.assertTrue(checkedmethod('36050234196908'))
        self.assertTrue(checkedmethod('4716461583322103'))
        self.assertTrue(checkedmethod('5398228707871527'))
        self.assertTrue(checkedmethod('4929 7226 5379 7141'))
        self.assertTrue(checkedmethod('4716-2210-5188-5662'))

        self.assertRaises(AssertionError, checkedmethod, '5398228707871528')
        self.assertRaises(AssertionError, checkedmethod, 'foo')
        self.assertRaises(AssertionError, checkedmethod, 'foo539822870bar')
        self.assertRaises(AssertionError, checkedmethod, '2721465526338453')
        self.assertRaises(AssertionError, checkedmethod, '2220175103860763')

        class CheckedClass(ValidusBase):
            a: crcard

        self.assertTrue(CheckedClass('375556917985515'))
        self.assertTrue(CheckedClass('36050234196908'))
        self.assertTrue(CheckedClass('4716461583322103'))
        self.assertTrue(CheckedClass('5398228707871527'))
        self.assertTrue(CheckedClass('4929 7226 5379 7141'))
        self.assertTrue(CheckedClass('4716-2210-5188-5662'))

        self.assertRaises(AssertionError, CheckedClass, '5398228707871528')
        self.assertRaises(AssertionError, CheckedClass, 'foo')
        self.assertRaises(AssertionError, CheckedClass, 'foo539822870bar')
        self.assertRaises(AssertionError, CheckedClass, '2721465526338453')
        self.assertRaises(AssertionError, CheckedClass, '2220175103860763')

    def test_isin(self):
        @checked
        def checkedmethod(a: isin):
            return True

        self.assertTrue(checkedmethod('AU0000XVGZA3'))
        self.assertTrue(checkedmethod('DE000BAY0017'))
        self.assertTrue(checkedmethod('BE0003796134'))
        self.assertTrue(checkedmethod('SG1G55870362'))
        self.assertTrue(checkedmethod('GB0001411924'))
        self.assertTrue(checkedmethod('DE000WCH8881'))
        self.assertTrue(checkedmethod('PLLWBGD00016'))

        self.assertRaises(AssertionError, checkedmethod, 'DE000BAY0018')
        self.assertRaises(AssertionError, checkedmethod, 'PLLWBGD00019')
        self.assertRaises(AssertionError, checkedmethod, 'foo')
        self.assertRaises(AssertionError, checkedmethod, '5398228707871528')

        class CheckedClass(ValidusBase):
            a: isin

        self.assertTrue(CheckedClass('AU0000XVGZA3'))
        self.assertTrue(CheckedClass('DE000BAY0017'))
        self.assertTrue(CheckedClass('BE0003796134'))
        self.assertTrue(CheckedClass('SG1G55870362'))
        self.assertTrue(CheckedClass('GB0001411924'))
        self.assertTrue(CheckedClass('DE000WCH8881'))
        self.assertTrue(CheckedClass('PLLWBGD00016'))

        self.assertRaises(AssertionError, CheckedClass, 'DE000BAY0018')
        self.assertRaises(AssertionError, CheckedClass, 'PLLWBGD00019')
        self.assertRaises(AssertionError, CheckedClass, 'foo')
        self.assertRaises(AssertionError, CheckedClass, '5398228707871528')

    def test_iban(self):
        @checked
        def checkedmethod(a: iban):
            return True

        self.assertTrue(checkedmethod('DE29100500001061045672'))
        self.assertTrue(checkedmethod('GB82WEST12345698765432'))
        self.assertTrue(checkedmethod('NO9386011117947'))

        self.assertRaises(AssertionError, checkedmethod, 'GB81WEST12345698765432')
        self.assertRaises(AssertionError, checkedmethod, 'NO9186011117947')

        class CheckedClass(ValidusBase):
            a: iban

        self.assertTrue(CheckedClass('DE29100500001061045672'))
        self.assertTrue(CheckedClass('GB82WEST12345698765432'))
        self.assertTrue(CheckedClass('NO9386011117947'))

        self.assertRaises(AssertionError, CheckedClass, 'GB81WEST12345698765432')
        self.assertRaises(AssertionError, CheckedClass, 'NO9186011117947')

    def test_imei(self):
        @checked
        def checkedmethod(a: imei):
            return True

        self.assertTrue(checkedmethod('351451208401216'))
        self.assertTrue(checkedmethod('351451-20-840121-6'))
        self.assertTrue(checkedmethod('351451-20-840121 6'))
        self.assertTrue(checkedmethod('565464561111118'))
        self.assertTrue(checkedmethod('56 546456 111111 8'))
        self.assertTrue(checkedmethod('101010101010400'))

        self.assertRaises(AssertionError, checkedmethod, '565464561111110')
        self.assertRaises(AssertionError, checkedmethod, '565464561111not')
        self.assertRaises(AssertionError, checkedmethod, '5654645611')
        self.assertRaises(AssertionError, checkedmethod, 'not1m3i00001010')

        class CheckedClass(ValidusBase):
            a: imei

        self.assertTrue(CheckedClass('351451208401216'))
        self.assertTrue(CheckedClass('351451-20-840121-6'))
        self.assertTrue(CheckedClass('351451-20-840121 6'))
        self.assertTrue(CheckedClass('565464561111118'))
        self.assertTrue(CheckedClass('56 546456 111111 8'))
        self.assertTrue(CheckedClass('101010101010400'))

        self.assertRaises(AssertionError, CheckedClass, '565464561111110')
        self.assertRaises(AssertionError, CheckedClass, '565464561111not')
        self.assertRaises(AssertionError, CheckedClass, '5654645611')
        self.assertRaises(AssertionError, CheckedClass, 'not1m3i00001010')
        self.assertRaises(AssertionError, CheckedClass, '22201751038607631')
