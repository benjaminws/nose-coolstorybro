import sys
from setuptools import setup

setup(
    name='coolstorybro',
    version='0.1',
    author='Benjamin W. Smith',
    author_email = 'benjaminwarfield@just-another.net',
    description = 'TL;DR',
    license = 'BSD',
    packages = ['coolstorybro'],
    entry_points = {
        'nose.plugins': [
            'coolstorybro = coolstorybro:CoolStoryBroPlugin'
            ]
    },
    classifiers = [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2'
    ],
)
