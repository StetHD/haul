#!/usr/bin/env python

import os
import sys

from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import haul


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

license = open('LICENSE').read()

install_requires = [str(item.req) for item in parse_requirements('requirements.txt')]

packages = [
    'haul',
    'haul.finders',
    'haul.finders.pipeline',
    'haul.extenders',
    'haul.extenders.pipeline',
]

setup(
    name='haul',
    version=haul.__version__,
    description='An Extensible Image Crawler',
    long_description='An Extensible Image Crawler',
    keywords='haul web image content scraper parser crawler',
    author='Vinta Chen',
    author_email='vinta.chen@gmail.com',
    url='https://github.com/vinta/Haul',
    license=license,
    install_requires=install_requires,
    include_package_data=True,
    packages=packages,
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ),
)
