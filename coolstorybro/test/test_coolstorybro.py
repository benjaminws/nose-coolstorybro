import os
import sys
import unittest
from nose.plugins import PluginTester

from coolstorybro import CoolStoryBroPlugin, CoolStoryBro


class CoolStoryBroTest(PluginTester, unittest.TestCase):

    activate = '--with-coolstorybro'
    plugins = [CoolStoryBroPlugin()]
    suitepath = os.path.join(os.path.dirname(__file__), 'examples')

    def test_emits_coolstorybro_exception(self):
        assert "U MAD?" in self.output

class CoolStoryBroTlDr(PluginTester, unittest.TestCase):

    activate = '--with-coolstorybro'
    args = ['--tl-dr']
    plugins = [CoolStoryBroPlugin()]
    suitepath = os.path.join(os.path.dirname(__file__), 'examples')

    def test_emits_tl_dr(self):
        assert "TL;DR" in self.output

if __name__ == '__main__':
    unittest.main()
