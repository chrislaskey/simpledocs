# -*- coding: utf8 -*-

# nosetests --with-coverage --cover-package=<package> \
# --nocapture ./tests

import os
from lib.environment import Environment
base_dir = '{0}/../../'.format(__file__)
abs_base_dir = os.path.abspath(base_dir)
Environment().add_virtualenv_site_packages_to_path(abs_base_dir)

from nose.tools import *
from lib.requestparser import RequestParser

class TestRequestParser:

    def setup(self):
        "Set up test fixtures"

    def teardown(self):
        "Tear down test fixtures"

    def test_empty_url_raises_exception(self):
        url = ''

        request = RequestStub().create(url)
        assert_raises(Exception, RequestParser.parse, request)

    def test_invalid_url_raises_exception(self):
        url = 'www.example.com/test/uri.html?one=two'

        request = RequestStub().create(url)
        assert_raises(Exception, RequestParser.parse, request)

    def test_valid_url(self):
        url = 'http://www.example.com/test/uri.html?one=two'
        expected = {
            'protocol': 'http',
            'domain': 'www.example.com',
            'uri': '/test/uri.html',
            'uri_segments': ['test', 'uri.html']
        }

        request = RequestStub().create(url)
        result = RequestParser().parse(request)
        assert_equal(result, expected)

class RequestStub:

    class Object(object):
        " See: http://stackoverflow.com/questions/2827623 "
        pass

    def create(self, url):
        stub = self.Object()
        stub.url = url
        stub.base_url = url.split('?')[0]
        return stub
