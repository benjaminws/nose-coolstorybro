import inspect
import os

from nose.case import MethodTestCase
from nose.plugins import Plugin
from unittest import TestResult, _TextTestResult


class CoolStoryBro(Exception):

    def __init__(self, tl_dr=None):
        self.tl_dr = tl_dr

    def __str__(self):
        if self.tl_dr:
            return self.tl_dr
        return "U MAD?"

class CoolStoryBroPlugin(Plugin):

    name = 'coolstorybro'
    enabled = True

    def options(self, parser, env=os.environ):
        parser.add_option('--tl-dr', action='store_true')
        super(CoolStoryBroPlugin, self).options(parser, env=env)

    def configure(self, options, config):
        super(CoolStoryBroPlugin, self).configure(options, config)
        self.config = config
        if not self.enabled:
            return

        self.tl_dr = options.tl_dr or None

    def startTest(self, test):
        if isinstance(test, MethodTestCase):
            source = inspect.getsourcelines(test.test)
            test_length = len(source[0])
            if test_length > 8:
                if self.tl_dr:
                    raise CoolStoryBro("TL;DR: %d lines" % test_length)
                raise CoolStoryBro
        pass

    def prepareTestRunner(self, runner):
        self.runner = runner

    def setOutputStream(self, stream):
        self.stream = stream
