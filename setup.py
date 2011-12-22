##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


tests_require = [
    'zope.testing',
    'zope.i18n',
    'zope.component',
    ]


setup(
    name='waitress',
    version='0.0',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    maintainer="Chris McDonough",
    maintainer_email="chrism@plope.com",
    description='Waitress WSGI server',
    long_description=(
        read('README.txt')
        + '\n\n' +
        read('CHANGES.txt')
        ),
    license='ZPL 2.1',
    keywords=('waitress wsgi server http'),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
    url='https://github.com/mcdonc/waitress',
    packages=find_packages(),
    tests_require=tests_require,
    install_requires=[
        'setuptools',
        'zope.interface',
        'zope.publisher',
        ],
    extras_require=dict(test=tests_require),
    include_package_data=True,
    test_suite='waitress',
    zip_safe=False,
    entry_points="""
    [paste.server_runner]
    main = waitress.server:run_paste
    """
    )
