#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Sex 10 Ago 2012 14:22:33 CEST

from setuptools import setup, find_packages

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='xbob.db.casia_fasd',
    version='master',
    description='CASIA Face Anti-Spoofing Database Access API for Bob',
    url='http://github.com/bioidiap/bob.db.casia_fasd',
    license='GPLv3',
    author='Andre Anjos',
    author_email='andre.anjos@idiap.ch',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    namespace_packages = [
      'xbob',
      'xbob.db',
      ],

    install_requires=[
      'setuptools',
      'bob',  # base signal proc./machine learning library
    ],

    entry_points={

      # declare the database to bob
      'bob.db': [
        'casia_fasd = xbob.db.casia_fasd.driver:Interface',
        ],

      # declare tests to bob
      'bob.test': [
        'casia_fasd = xbob.db.casia_fasd.test:FASDDatabaseTest',
        ],
      },

)
