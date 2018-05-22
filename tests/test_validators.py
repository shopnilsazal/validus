#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_validators
----------------------------------

Tests for `validus` module.
"""

import unittest
import validus


class TestValidators(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isascii(self):
        self.assertTrue(validus.isascii('foobar'))
        self.assertTrue(validus.isascii('0987654321'))
        self.assertTrue(validus.isascii('1234abcDEF'))
        self.assertTrue(validus.isascii('test@example.com'))

        self.assertFalse(validus.isascii('ｆｏｏbar'))
        self.assertFalse(validus.isascii('ｘｙｚ０９８'))
        self.assertFalse(validus.isascii('１２３456'))

    def test_isprintascii(self):
        self.assertTrue(validus.isprintascii('foobar'))
        self.assertTrue(validus.isprintascii('0987654321'))
        self.assertTrue(validus.isprintascii('1234abcDEF'))
        self.assertTrue(validus.isprintascii('test@example.com'))

        self.assertFalse(validus.isprintascii('ｆｏｏbar'))
        self.assertFalse(validus.isprintascii('ｘｙｚ０９８'))
        self.assertFalse(validus.isprintascii('１２３456'))
        self.assertFalse(validus.isprintascii('\x19test\x7F'))

    def test_isbase64(self):
        self.assertTrue(validus.isbase64('TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4='))
        self.assertTrue(validus.isbase64('Vml2YW11cyBmZXJtZW50dW0gc2VtcGVyIHBvcnRhLg=='))
        self.assertTrue(validus.isbase64('U3VzcGVuZGlzc2UgbGVjdHVzIGxlbw=='))
        self.assertTrue(validus.isbase64('Zm9vYmE='))

        self.assertFalse(validus.isbase64('dataxbase64'))
        self.assertFalse(validus.isbase64('Vml2YW11cyBmZXJtZtesting123'))
        self.assertFalse(validus.isbase64('12345'))
        self.assertFalse(validus.isbase64('Zm9vYmFy===='))

    def test_isemail(self):
        self.assertTrue(validus.isemail('foo@bar.com'))
        self.assertTrue(validus.isemail('x@x.au'))
        self.assertTrue(validus.isemail('foo+bar@bar.com'))
        self.assertTrue(validus.isemail('foo@bar.中文网'))
        self.assertTrue(validus.isemail('hans.m端ller@test.com'))
        self.assertTrue(validus.isemail('test+ext@gmail.com'))
        self.assertTrue(validus.isemail('NATHAN.DAVIES@DOMAIN.CO.UK'))

        self.assertFalse(validus.isemail('invalidemail@'))
        self.assertFalse(validus.isemail('@invalid.com'))
        self.assertFalse(validus.isemail('invalid.com'))
        self.assertFalse(validus.isemail('foo@bar.coffee..coffee'))

    def test_ishexdecimal(self):
        self.assertTrue(validus.ishexadecimal('deadBEEF'))
        self.assertTrue(validus.ishexadecimal('ff0044'))

        self.assertFalse(validus.ishexadecimal('abcdefg'))
        self.assertFalse(validus.ishexadecimal('..'))

    def test_ishexcolor(self):
        self.assertTrue(validus.ishexcolor('#ff0034'))
        self.assertTrue(validus.ishexcolor('#eeeeee'))
        self.assertTrue(validus.ishexcolor('#f00'))
        self.assertTrue(validus.ishexcolor('#fff'))
        self.assertTrue(validus.ishexcolor('#000'))

        self.assertFalse(validus.ishexcolor('#ff'))
        self.assertFalse(validus.ishexcolor('fff0'))
        self.assertFalse(validus.ishexcolor('#ff12FG'))

    def test_isrgbcolor(self):
        self.assertTrue(validus.isrgbcolor('rgb(0,31,255)'))
        self.assertTrue(validus.isrgbcolor('rgb(0,100,255)'))
        self.assertTrue(validus.isrgbcolor('rgb(0,0,255)'))
        self.assertTrue(validus.isrgbcolor('rgb(155,133,255)'))
        self.assertTrue(validus.isrgbcolor('rgb(255,255,255)'))
        self.assertTrue(validus.isrgbcolor('rgb(0,0,0)'))

        self.assertFalse(validus.isrgbcolor('rgb(1,349,275)'))
        self.assertFalse(validus.isrgbcolor('rgb(01,31,255)'))
        self.assertFalse(validus.isrgbcolor('rgb(0.6,31,255)'))

    def test_isint(self):
        self.assertTrue(validus.isint('-2147483648'))
        self.assertTrue(validus.isint('2147483647'))
        self.assertTrue(validus.isint('-2147483649'))
        self.assertTrue(validus.isint('2147483648'))
        self.assertTrue(validus.isint('-9223372036854775808'))
        self.assertTrue(validus.isint('9223372036854775807'))
        self.assertTrue(validus.isint('18446744073709551615'))
        self.assertTrue(validus.isint('123'))

        self.assertFalse(validus.isint('000'))
        self.assertFalse(validus.isint('123.123'))
        self.assertFalse(validus.isint('100e10'))

    def test_ispositive(self):
        self.assertTrue(validus.ispositive('123.123'))
        self.assertTrue(validus.ispositive('123'))
        self.assertFalse(validus.ispositive('-.123'))
        self.assertFalse(validus.ispositive('-123'))

    def test_isnonempty(self):
        self.assertTrue(validus.isnonempty('123.123'))
        self.assertTrue(validus.isnonempty('foobar'))
        self.assertFalse(validus.isnonempty(''))

    def test_isfloat(self):
        self.assertTrue(validus.isfloat('123.123'))
        self.assertTrue(validus.isfloat('-123.123'))
        self.assertTrue(validus.isfloat('-0.123'))
        self.assertTrue(validus.isfloat('01.123'))
        self.assertTrue(validus.isfloat('-0.22250738585072011e-307'))

        self.assertFalse(validus.isfloat('foo'))
        self.assertFalse(validus.isfloat('+1f'))
        self.assertFalse(validus.isfloat('abacaba'))
        self.assertFalse(validus.isfloat('-.123'))

    def test_isslug(self):
        self.assertTrue(validus.isslug('123-12312-asdasda'))
        self.assertTrue(validus.isslug('123____123'))
        self.assertTrue(validus.isslug('dsadasd-dsadas'))

        self.assertFalse(validus.isslug('some.slug'))
        self.assertFalse(validus.isslug('1231321%'))
        self.assertFalse(validus.isslug('123asda&'))

    def test_isuuid(self):
        self.assertTrue(validus.isuuid('a987fbc9-4bed-3078-cf07-9141ba07c9f3'))
        self.assertTrue(validus.isuuid('A987FBC9-4BED-4078-8F07-9141BA07C9F3'))
        self.assertTrue(validus.isuuid('A987FBC9-4BED-5078-AF07-9141BA07C9F3'))

        self.assertFalse(validus.isuuid('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3'))
        self.assertFalse(validus.isuuid('A987FBC9-4BED-3078-CF07-9141BA07C9F3xxx'))
        self.assertFalse(validus.isuuid('A987FBC94BED3078CF079141BA07C9F3'))

    def test_isuuid3(self):
        self.assertTrue(validus.isuuid3('A987FBC9-4BED-3078-CF07-9141BA07C9F3'))

        self.assertFalse(validus.isuuid3('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3'))
        self.assertFalse(validus.isuuid3('A987FBC9-4BED-4078-8F07-9141BA07C9F3'))

    def test_isuuid4(self):
        self.assertTrue(validus.isuuid4('713ae7e3-cb32-45f9-adcb-7c4fa86b90c1'))
        self.assertTrue(validus.isuuid4('625e63f3-58f5-40b7-83a1-a72ad31acffb'))
        self.assertTrue(validus.isuuid4('57b73598-8764-4ad0-a76a-679bb6640eb1'))
        self.assertTrue(validus.isuuid4('9c858901-8a57-4791-81fe-4c455b099bc9'))

        self.assertFalse(validus.isuuid4('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3'))
        self.assertFalse(validus.isuuid4('A987FBC9-4BED-3078-CF07-9141BA07C9F3'))
        self.assertFalse(validus.isuuid4('A987FBC9-4BED-5078-AF07-9141BA07C9F3'))
        self.assertFalse(validus.isuuid4('AAAAAAAA-1111-1111-AAAG-111111111111'))

    def test_isuuid5(self):
        self.assertTrue(validus.isuuid5('987FBC97-4BED-5078-AF07-9141BA07C9F3'))
        self.assertTrue(validus.isuuid5('987FBC97-4BED-5078-BF07-9141BA07C9F3'))
        self.assertTrue(validus.isuuid5('987FBC97-4BED-5078-9F07-9141BA07C9F3'))
        self.assertTrue(validus.isuuid5('987FBC97-4BED-5078-8F07-9141BA07C9F3'))

        self.assertFalse(validus.isuuid5('xxxA987FBC9-4BED-3078-CF07-9141BA07C9F3'))
        self.assertFalse(validus.isuuid5('AAAAAAAA-1111-1111-AAAG-111111111111'))
        self.assertFalse(validus.isuuid5('9c858901-8a57-4791-81fe-4c455b099bc9'))
        self.assertFalse(validus.isuuid5('A987FBC9-4BED-3078-CF07-9141BA07C9F3'))

    def test_isfullwidth(self):
        self.assertTrue(validus.isfullwidth('ひらがな・カタカナ、．漢字'))
        self.assertTrue(validus.isfullwidth('３ー０　ａ＠ｃｏｍ'))
        self.assertTrue(validus.isfullwidth('Ｆｶﾀｶﾅﾞﾬ'))

        self.assertFalse(validus.isfullwidth('abc'))
        self.assertFalse(validus.isfullwidth('abc123'))
        self.assertFalse(validus.isfullwidth('!\"#$%&()<>/+=-_? ~^|.,@`{}[]'))

    def test_ishalfwidth(self):
        self.assertTrue(validus.ishalfwidth('!\"#$%&()<>/+=-_? ~^|.,@`{}[]'))
        self.assertTrue(validus.ishalfwidth('l-btn_02--active'))
        self.assertTrue(validus.ishalfwidth('abc123い'))
        self.assertTrue(validus.ishalfwidth('ｶﾀｶﾅﾞﾬ￩'))

        self.assertFalse(validus.ishalfwidth('あいうえお'))
        self.assertFalse(validus.ishalfwidth('００１１'))

    def test_islatitude(self):
        self.assertTrue(validus.islatitude('-90.000'))
        self.assertTrue(validus.islatitude('+90'))
        self.assertTrue(validus.islatitude('47.1231231'))

        self.assertFalse(validus.islatitude('+99.9'))
        self.assertFalse(validus.islatitude('108'))

    def test_islongitude(self):
        self.assertTrue(validus.islongitude('+73.234'))
        self.assertTrue(validus.islongitude('-180.000'))
        self.assertTrue(validus.islongitude('23.11111111'))

        self.assertFalse(validus.islongitude('180.1'))
        self.assertFalse(validus.islongitude('+382.3811'))

    def test_ismac(self):
        self.assertTrue(validus.ismac('3D:F2:C9:A6:B3:4F'))
        self.assertTrue(validus.ismac('FF:FF:FF:FF:FF:FF'))
        self.assertTrue(validus.ismac('01:02:03:04:05:ab'))
        self.assertTrue(validus.ismac('01:AB:03:04:05:06'))

        self.assertFalse(validus.ismac('01:02:03:04:05'))
        self.assertFalse(validus.ismac('01:02:03:04::ab'))
        self.assertFalse(validus.ismac('1:2:3:4:5:6'))
        self.assertFalse(validus.ismac('AB:CD:EF:GH:01:02'))

    def test_ismd5(self):
        self.assertTrue(validus.ismd5('d94f3f016ae679c3008de268209132f2'))
        self.assertTrue(validus.ismd5('751adbc511ccbe8edf23d486fa4581cd'))
        self.assertTrue(validus.ismd5('88dae00e614d8f24cfd5a8b3f8002e93'))
        self.assertTrue(validus.ismd5('0bf1c35032a71a14c2f719e5a14c1e96'))

        self.assertFalse(validus.ismd5('KYT0bf1c35032a71a14c2f719e5a14c1'))
        self.assertFalse(validus.ismd5('q94375dj93458w34'))
        self.assertFalse(validus.ismd5('39485729348'))
        self.assertFalse(validus.ismd5('%&FHKJFvk'))

    def test_issha1(self):
        self.assertTrue(validus.issha1('1bc6b8a58b484bdb6aa5264dc554934e3e46c405'))
        self.assertTrue(validus.issha1('d545e28504c797ee8f26d3f482ea1a2485d0b018'))
        self.assertTrue(validus.issha1('56Dae00e614d8F24dfd544483f209a2D9e21e57A'))

        self.assertFalse(validus.issha1('d545e28504c797ee8f26d3f482ea1a2485d0b018777'))
        self.assertFalse(validus.issha1('ZKYT059dbf1c356032a7b1a1d4c2f719e5a14c1'))
        self.assertFalse(validus.issha1('q94375dj93458w34'))
        self.assertFalse(validus.issha1('84375958454'))
        self.assertFalse(validus.issha1('*!FHPJFvc'))

    def test_issha256(self):
        self.assertTrue(validus.issha256('fd04c4a99b6b1f118452da33dfe9523ec164f5fecde4502b69f1ed3f24a29ff6'))
        self.assertTrue(validus.issha256('4523475627356732465783465723675623562365736592656273465926357236'))
        self.assertTrue(validus.issha256('AA090789a99b6b90789245234523C952ae856744352d32452b634F5D34a29fDD'))

        self.assertFalse(validus.issha256('fd04c4a99b6b1f118452da33dfe9523ec164f5fecde4502b6945f1ed3f24a29ff6'))
        self.assertFalse(validus.issha256('q94375dj93458w34'))
        self.assertFalse(validus.issha256('84375958454'))
        self.assertFalse(validus.issha256('\\M$""'))

    def test_issha512(self):
        self.assertTrue(validus.issha512('0b696861da778f6bd0d899ad9a581f4b9b1eb8286eaba266d2f2e2767539055bf8eb59e8884839a268141aba1ef078ce67cf94d421bd1195a3c0e817f5f7b286'))
        self.assertTrue(validus.issha512('45723405723485723475275235567576454134134684623196443436423641641242153645167451294512345912354123549123546125394125452194531293'))
        self.assertTrue(validus.issha512('AA090789a99b6b90789245234523C952ae856744352d32452b634F5D34a29fDDAA090789a99b6b90789245234523C952ae856744352d32452b634F5D34a29fDD'))

        self.assertFalse(validus.issha512('0b696861da778f6bd0d899ad9a581f4b9b1eb8286eaba266d2f2e2767539055bf8eb59e8884839a268141aba1ef078ce67cf94d421bd1195a3c0e817f5f7b286555'))
        self.assertFalse(validus.issha512('KLO4545ID55545789Hg545235F45255452Hgf76DJF56HgKJfg3456356356346534534653456sghey45656jhgjfgghdfhgdfhdfhdfhdfhghhq94375dj93458w34'))
        self.assertFalse(validus.issha512('975'))
        self.assertFalse(validus.issha512('*)^&!MNdf67657'))

    def test_ismongoid(self):
        self.assertTrue(validus.ismongoid('507f1f77bcf86cd799439011'))
        self.assertFalse(validus.ismongoid('507f1f77bcf86cd7994390'))
        self.assertFalse(validus.ismongoid('507f1f77bcf86cd79943901z'))

    def test_isiso8601(self):
        self.assertTrue(validus.isiso8601('2009-12T12:34'))
        self.assertTrue(validus.isiso8601('2009-05-19'))
        self.assertTrue(validus.isiso8601('20090519'))
        self.assertTrue(validus.isiso8601('2009-05-19 14:39:22-06:00'))
        self.assertTrue(validus.isiso8601('2009-05-19 14:39:22'))
        self.assertTrue(validus.isiso8601('2009-05-19 00:00'))
        self.assertTrue(validus.isiso8601('2009-W01-1'))

        self.assertFalse(validus.isiso8601('2009367'))
        self.assertFalse(validus.isiso8601('2010-02-18T16:23.33.600'))
        self.assertFalse(validus.isiso8601('2009-05-19 14:39:22+06a00'))
        self.assertFalse(validus.isiso8601('2009-05-1914:39'))
        self.assertFalse(validus.isiso8601('2009-05-19T14a39r'))
        self.assertFalse(validus.isiso8601('2009-M511'))
        self.assertFalse(validus.isiso8601('2007-04-05T24:50'))

    def test_isipv4(self):
        self.assertTrue(validus.isipv4('127.0.0.1'))
        self.assertTrue(validus.isipv4('0.0.0.0'))
        self.assertTrue(validus.isipv4('255.255.255.255'))
        self.assertTrue(validus.isipv4('1.2.3.4'))

        self.assertFalse(validus.isipv4('::1'))
        self.assertFalse(validus.isipv4('::ffff:127.0.0.1'))
        self.assertFalse(validus.isipv4('2001:db8:0000:1:1:1:1:1'))

    def test_isipv6(self):
        self.assertTrue(validus.isipv6('2001:db8:0000:1:1:1:1:1'))
        self.assertTrue(validus.isipv6('2001:41d0:2:a141::1'))

        self.assertFalse(validus.isipv6('127.0.0.1'))
        self.assertFalse(validus.isipv6('1.2.3.4'))

    def test_isip(self):
        self.assertTrue(validus.isip('127.0.0.1'))
        self.assertTrue(validus.isip('0.0.0.0'))
        self.assertTrue(validus.isip('255.255.255.255'))
        self.assertTrue(validus.isip('1.2.3.4'))
        self.assertTrue(validus.isip('2001:db8:0000:1:1:1:1:1'))
        self.assertTrue(validus.isip('2001:41d0:2:a141::1'))

        self.assertFalse(validus.isip('abc'))
        self.assertFalse(validus.isip('0200.200.200.200'))
        self.assertFalse(validus.isip('26.0.0.256'))
        self.assertFalse(validus.isip('256.0.0.0'))
        self.assertFalse(validus.isip('1:1:1:1:1:1:1:1:1:1:1:1:1:1:1:1'))

    def test_isport(self):
        self.assertTrue(validus.isport('1'))
        self.assertTrue(validus.isport('65535'))
        self.assertTrue(validus.isport('8080'))
        self.assertTrue(validus.isport('3000'))
        self.assertTrue(validus.isport('4000'))

        self.assertFalse(validus.isport('0'))
        self.assertFalse(validus.isport('65536'))
        self.assertFalse(validus.isport('65538'))

    def test_isdns(self):
        self.assertTrue(validus.isdns('localhost'))
        self.assertTrue(validus.isdns('ru.link.n.svpncloud.com'))
        self.assertTrue(validus.isdns('l.local.intern'))
        self.assertTrue(validus.isdns('localhost.local'))
        self.assertTrue(validus.isdns('a.bc'))

        self.assertFalse(validus.isdns('a.b..'))
        self.assertFalse(validus.isdns('-localhost'))
        self.assertFalse(validus.isdns('localhost.-localdomain'))
        self.assertFalse(validus.isdns('localhost.lÖcaldomain'))
        self.assertFalse(validus.isdns('127.0.0.1'))

    def test_isssn(self):
        self.assertTrue(validus.isssn('191 60 2869'))
        self.assertTrue(validus.isssn('191-60-2869'))

        self.assertFalse(validus.isssn('66690-76'))
        self.assertFalse(validus.isssn('00-90-8787'))

    def test_issemver(self):
        self.assertTrue(validus.issemver('v1.0.0'))
        self.assertTrue(validus.issemver('1.0.0'))
        self.assertTrue(validus.issemver('1.0.0-alpha'))
        self.assertTrue(validus.issemver('1.0.0-alpha.1'))
        self.assertTrue(validus.issemver('1.0.0-0.3.7'))
        self.assertTrue(validus.issemver('1.0.0-x.7.z.92'))
        self.assertTrue(validus.issemver('1.0.0-beta+exp.sha.5114f85'))

        self.assertFalse(validus.issemver('1.1.01'))
        self.assertFalse(validus.issemver('1.01.0'))
        self.assertFalse(validus.issemver('01.1.0'))
        self.assertFalse(validus.issemver('v1.1.01'))
        self.assertFalse(validus.issemver('v1.01.0'))
        self.assertFalse(validus.issemver('v01.1.0'))
        self.assertFalse(validus.issemver('1.0.0-00.3.7'))

    def test_isbytelen(self):
        self.assertTrue(validus.isbytelen('123456', 0, 100))
        self.assertTrue(validus.isbytelen('123456abcdefg', 0, 100))
        self.assertTrue(validus.isbytelen('1239999asdff29', 10, 30))
        self.assertTrue(validus.isbytelen('123def9999asdff09876', 10, 30))

        self.assertFalse(validus.isbytelen('1239999', 0, 1))
        self.assertFalse(validus.isbytelen('abcdef', 10, 20))
        self.assertFalse(validus.isbytelen('1234567890', 20, 30))

    def test_ismultibyte(self):
        self.assertTrue(validus.ismultibyte('ひらがな・カタカナ、．漢字'))
        self.assertTrue(validus.ismultibyte('あいうえお foobar'))
        self.assertTrue(validus.ismultibyte('ｶﾀｶﾅ'))
        self.assertTrue(validus.ismultibyte('中文'))

        self.assertFalse(validus.ismultibyte('abc'))
        self.assertFalse(validus.ismultibyte('abc123'))
        self.assertFalse(validus.ismultibyte('<>@" *.'))
        self.assertFalse(validus.ismultibyte('<>@;.-='))

    def test_isfilepath(self):
        self.assertEqual(validus.isfilepath('c:\\path\\file (x86)\\bar'), (True, 'Win'))
        self.assertEqual(validus.isfilepath('c:\\path\\file'), (True, 'Win'))
        self.assertEqual(validus.isfilepath('C:\\'), (True, 'Win'))
        self.assertEqual(validus.isfilepath('c:\\path\\file\\'), (True, 'Win'))
        self.assertEqual(validus.isfilepath('/path/file/'), (True, 'Unix'))
        self.assertEqual(validus.isfilepath('/path'), (True, 'Unix'))
        self.assertEqual(validus.isfilepath('/path/__bc/file.txt'), (True, 'Unix'))
        self.assertEqual(validus.isfilepath('/path/file:/.txt'), (True, 'Unix'))
        self.assertEqual(validus.isfilepath('/path/file:SAMPLE/'), (True, 'Unix'))
        self.assertEqual(validus.isfilepath('c:\\path\\file:exe'), (False, 'Unknown'))
        self.assertEqual(validus.isfilepath('c:/path/file/'), (False, 'Unknown'))

    def test_isdatauri(self):
        self.assertTrue(validus.isdatauri('data:image/png;base64,TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4='))
        self.assertTrue(validus.isdatauri('data:text/plain;base64,Vml2YW11cyBmZXJtZW50dW0gc2VtcGVyIHBvcnRhLg=='))
        self.assertTrue(validus.isdatauri('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC'))
        self.assertTrue(validus.isdatauri('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIBAMAAAA2IaO4AAAAFVBMVEXk5OTn5+ft7e319fX29vb5+fn///++GUmVAAAALUlEQVQIHWNICnYLZnALTgpmMGYIFWYIZTA2ZFAzTTFlSDFVMwVyQhmAwsYMAKDaBy0axX/iAAAAAElFTkSuQmCC'))
        self.assertTrue(validus.isdatauri('data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22100%22%20height%3D%22100%22%3E%3Crect%20fill%3D%22%2300B1FF%22%20width%3D%22100%22%20height%3D%22100%22%2F%3E%3C%2Fsvg%3E'))
        self.assertTrue(validus.isdatauri('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIj48cmVjdCBmaWxsPSIjMDBCMUZGIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIvPjwvc3ZnPg=='))
        self.assertTrue(validus.isdatauri('data:text/plain;base64,SGVsbG8sIFdvcmxkIQ%3D%3D'))
        self.assertTrue(validus.isdatauri('data:text/html,%3Ch1%3EHello%2C%20World!%3C%2Fh1%3E'))

        self.assertFalse(validus.isdatauri('dataxbase64'))
        self.assertFalse(validus.isdatauri('dataxbase64data:HelloWorld'))
        self.assertFalse(validus.isdatauri('data:base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC'))
        self.assertFalse(validus.isdatauri('data:text/html;charset=,%3Ch1%3EHello!%3C%2Fh1%3E'))
        self.assertFalse(validus.isdatauri('iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEUAAAD///+l2Z/dAAAAM0lEQVR4nGP4/5/h/1+G/58ZDrAz3D/McH8yw83NDDeNGe4Ug9C9zwz3gVLMDA/A6P9/AFGGFyjOXZtQAAAAAElFTkSuQmCC'))

    def test_isjson(self):
        self.assertTrue(validus.isjson('{"Name":"Alice","Body":"Hello","Time":1294706395881547000}'))
        self.assertTrue(validus.isjson('{"Key": {"Key": {"Key": 123}}}'))
        self.assertTrue(validus.isjson('{ "key": "value" }'))

        self.assertFalse(validus.isjson('{ key: "value" }'))
        self.assertFalse(validus.isjson('{ \'key\': \'value\' }'))

    def test_istime(self):
        self.assertTrue(validus.istime('30 Nov 00', '%d %b %y'))
        self.assertTrue(validus.istime('Tuesday, 21. November 2006 04:30PM', '%A, %d. %B %Y %I:%M%p'))
        self.assertTrue(validus.istime('21/11/06 16:30', '%d/%m/%y %H:%M'))

        self.assertFalse(validus.istime('21-11-06 4:30PM', '%d/%m/%y %H:%M'))
        self.assertFalse(validus.istime('Friday', '%d'))

    def test_isurl(self):
        self.assertTrue(validus.isurl('http://foo.bar#com'))
        self.assertTrue(validus.isurl('http://foobar.com'))
        self.assertTrue(validus.isurl('https://foobar.org'))
        self.assertTrue(validus.isurl('ftp://foobar.ru/'))
        self.assertTrue(validus.isurl('http://duckduckgo.com/?q=%2F'))
        self.assertTrue(validus.isurl('http://user:pass@www.foobar.com/'))
        self.assertTrue(validus.isurl('http://www.xn--froschgrn-x9a.net/'))
        self.assertTrue(validus.isurl('http://foobar.中文网/'))
        self.assertTrue(validus.isurl('http://localhost:3000/'))
        self.assertTrue(validus.isurl('rtmp://foobar.com'))

        self.assertFalse(validus.isurl('http://foobar.c_o_m'))
        self.assertFalse(validus.isurl('abc'))
        self.assertFalse(validus.isurl('abcd'))
        self.assertFalse(validus.isurl('abcde'))
        self.assertFalse(validus.isurl('abcdef'))
        self.assertFalse(validus.isurl('xyz://foobar.com'))
        self.assertFalse(validus.isurl('http://www.foo_bar.com/'))
        self.assertFalse(validus.isurl('http://foo bar.org'))
        self.assertFalse(validus.isurl('http://.foo.com'))

    def test_iscrcard(self):
        self.assertTrue(validus.iscrcard('375556917985515'))
        self.assertTrue(validus.iscrcard('36050234196908'))
        self.assertTrue(validus.iscrcard('4716461583322103'))
        self.assertTrue(validus.iscrcard('5398228707871527'))
        self.assertTrue(validus.iscrcard('4929 7226 5379 7141'))
        self.assertTrue(validus.iscrcard('4716-2210-5188-5662'))

        self.assertFalse(validus.iscrcard('5398228707871528'))
        self.assertFalse(validus.iscrcard('foo'))
        self.assertFalse(validus.iscrcard('foo539822870bar'))
        self.assertFalse(validus.iscrcard('2721465526338453'))
        self.assertFalse(validus.iscrcard('2220175103860763'))

    def test_isisin(self):
        self.assertTrue(validus.isisin('AU0000XVGZA3'))
        self.assertTrue(validus.isisin('DE000BAY0017'))
        self.assertTrue(validus.isisin('BE0003796134'))
        self.assertTrue(validus.isisin('SG1G55870362'))
        self.assertTrue(validus.isisin('GB0001411924'))
        self.assertTrue(validus.isisin('DE000WCH8881'))
        self.assertTrue(validus.isisin('PLLWBGD00016'))

        self.assertFalse(validus.isisin('DE000BAY0018'))
        self.assertFalse(validus.isisin('PLLWBGD00019'))
        self.assertFalse(validus.isisin('foo'))
        self.assertFalse(validus.isisin('5398228707871528'))

    def test_isiban(self):
        self.assertTrue(validus.isiban('DE29100500001061045672'))
        self.assertTrue(validus.isiban('GB82WEST12345698765432'))
        self.assertTrue(validus.isiban('NO9386011117947'))

        self.assertFalse(validus.isiban('GB81WEST12345698765432'))
        self.assertFalse(validus.isiban('NO9186011117947'))

    def test_isimei(self):
        self.assertTrue(validus.isimei('351451208401216'))
        self.assertTrue(validus.isimei('351451-20-840121-6'))
        self.assertTrue(validus.isimei('351451-20-840121 6'))
        self.assertTrue(validus.isimei('565464561111118'))
        self.assertTrue(validus.isimei('56 546456 111111 8'))
        self.assertTrue(validus.isimei('101010101010400'))

        self.assertFalse(validus.isimei('565464561111110'))
        self.assertFalse(validus.isimei('565464561111not'))
        self.assertFalse(validus.isimei('5654645611'))
        self.assertFalse(validus.isimei('not1m3i00001010'))
        self.assertFalse(validus.isimei('22201751038607631'))

    def test_ismimetype(self):
        self.assertTrue(validus.ismimetype('application/json'))
        self.assertTrue(validus.ismimetype('application/xhtml+xml'))
        self.assertTrue(validus.ismimetype('audio/mp4'))
        self.assertTrue(validus.ismimetype('image/bmp'))
        self.assertTrue(validus.ismimetype('font/woff2'))
        self.assertTrue(validus.ismimetype('message/http'))
        self.assertTrue(validus.ismimetype('model/vnd.gtw'))
        self.assertTrue(validus.ismimetype('multipart/form-data'))
        self.assertTrue(validus.ismimetype('multipart/form-data; boundary=something'))
        self.assertTrue(validus.ismimetype('multipart/form-data; charset=utf-8; boundary=something'))
        self.assertTrue(validus.ismimetype('multipart/form-data; boundary=something; charset=utf-8'))
        self.assertTrue(validus.ismimetype('multipart/form-data; boundary=something; charset="utf-8"'))
        self.assertTrue(validus.ismimetype('multipart/form-data; boundary="something"; charset=utf-8'))
        self.assertTrue(validus.ismimetype('multipart/form-data; boundary="something"; charset="utf-8"'))
        self.assertTrue(validus.ismimetype('text/css'))
        self.assertTrue(validus.ismimetype('text/plain; charset=utf8'))
        self.assertTrue(validus.ismimetype('Text/HTML;Charset="utf-8"'))
        self.assertTrue(validus.ismimetype('text/html;charset=UTF-8'))
        self.assertTrue(validus.ismimetype('Text/html;charset=UTF-8'))
        self.assertTrue(validus.ismimetype('text/html; charset=us-ascii'))
        self.assertTrue(validus.ismimetype('text/html; charset=us-ascii (Plain text)'))
        self.assertTrue(validus.ismimetype('text/html; charset="us-ascii"'))
        self.assertTrue(validus.ismimetype('video/mp4'))

        self.assertFalse(validus.ismimetype(''))
        self.assertFalse(validus.ismimetype(' '))
        self.assertFalse(validus.ismimetype('/'))
        self.assertFalse(validus.ismimetype('f/b'))
        self.assertFalse(validus.ismimetype('application'))
        self.assertFalse(validus.ismimetype('application\\json'))
        self.assertFalse(validus.ismimetype('application/json/text'))
        self.assertFalse(validus.ismimetype('application/json; charset=utf-8'))
        self.assertFalse(validus.ismimetype('audio/mp4; charset=utf-8'))
        self.assertFalse(validus.ismimetype('image/bmp; charset=utf-8'))
        self.assertFalse(validus.ismimetype('font/woff2; charset=utf-8'))
        self.assertFalse(validus.ismimetype('message/http; charset=utf-8'))
        self.assertFalse(validus.ismimetype('model/vnd.gtw; charset=utf-8'))
        self.assertFalse(validus.ismimetype('video/mp4; charset=utf-8'))

    def test_isisrc(self):
        self.assertTrue(validus.isisrc('USAT29900609'))
        self.assertTrue(validus.isisrc('GBAYE6800011'))
        self.assertTrue(validus.isisrc('USRC15705223'))
        self.assertTrue(validus.isisrc('USCA29500702'))

        self.assertFalse(validus.isisrc('USAT2990060'))
        self.assertFalse(validus.isisrc('SRC15705223'))
        self.assertFalse(validus.isisrc('US-CA29500702'))
        self.assertFalse(validus.isisrc('USARC15705223'))

