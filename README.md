COOL STORY BRO
==============

[Someone](http://twitter.com/garybernhardt) once said [Resisting the urge to write a test runner that raises CoolStoryBro if your test is over eight lines long.](http://twitter.com/#!/garybernhardt/status/125711084878442496).

You're welcome.

INSTALL, BRO
============

   $ pip install git+git://github.com/benjaminws/nose-coolstorybro.git

USAGE, BRO
==========

Your tests are too big, bro
---------------------------

    $ nosetests --with-coolstorybro test/examples
    E
    ======================================================================
    ERROR: test_ex_coolstorybro.TestCoolStoryBroExample.test_ex_coolstorybro
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/case.py", line 133, in run
        self.runTest(result)
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/case.py", line 151, in runTest
        test(result)
      File "/usr/lib/python2.7/unittest/case.py", line 385, in __call__
        return self.run(*args, **kwds)
      File "/usr/lib/python2.7/unittest/case.py", line 296, in run
        result.startTest(self)
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/proxy.py", line 172, in startTest
        self.plugins.startTest(self.test)
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/plugins/manager.py", line 94, in __call__
        return self.call(*arg, **kw)
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/plugins/manager.py", line 162, in simple
        result = meth(*arg, **kw)
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/plugins/manager.py", line 343, in startTest
        return self.plugin.startTest(test.test)
      File "build/bdist.linux-x86_64/egg/coolstorybro/coolstorybro.py", line 43, in startTest
        raise CoolStoryBro
    CoolStoryBro: U MAD?
    
    ----------------------------------------------------------------------
    Ran 0 tests in 0.002s
    
    FAILED (errors=1)

How many lines was that?
------------------------

    $ nosetests --with-coolstorybro --tl-dr test/examples
    E
    ======================================================================
    ERROR: test_ex_coolstorybro.TestCoolStoryBroExample.test_ex_coolstorybro
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/case.py", line 133, in run
        self.runTest(result)
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/case.py", line 151, in runTest
        test(result)
      File "/usr/lib/python2.7/unittest/case.py", line 385, in __call__
        return self.run(*args, **kwds)
      File "/usr/lib/python2.7/unittest/case.py", line 296, in run
        result.startTest(self)
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/proxy.py", line 172, in startTest
        self.plugins.startTest(self.test)
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/plugins/manager.py", line 94, in __call__
        return self.call(*arg, **kw)
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/plugins/manager.py", line 162, in simple
        result = meth(*arg, **kw)
      File "/home/bsmith/Dev/python/nose-coolstorybro/lib/python2.7/site-packages/nose/plugins/manager.py", line 343, in startTest
        return self.plugin.startTest(test.test)
      File "build/bdist.linux-x86_64/egg/coolstorybro/coolstorybro.py", line 42, in startTest
        raise CoolStoryBro("TL;DR: %d lines" % test_length)
    CoolStoryBro: TL;DR: 12 lines
    
    ----------------------------------------------------------------------
    Ran 0 tests in 0.002s
    
    FAILED (errors=1)
