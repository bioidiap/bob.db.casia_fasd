#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Sex 10 Ago 2012 14:22:33 CEST

from setuptools import setup, find_packages

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='bob.db.casia_fasd',
    version='master',
    description='CASIA Face Anti-Spoofing Database Access API for Bob',
    url='http://github.com/bioidiap/bob.db.casia_fasd',
    license='LICENSE.txt',
    author_email='Andre Anjos <andre.anjos@idiap.ch>',
    #long_description=open('doc/howto.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),

    # Non-python data files to be shipped
    package_data = {
      'casia_fasd': [
        'db/cross_valid.txt',
        'db/cut_attack.txt',
        'db/cut_warped_attack.txt',
        'db/cut_warped_video_attack.txt',
        'db/real.txt',
        'db/video_attack.txt',
        'db/warped_attack.txt',
        ],
      },

    install_requires=[
        "bob == master",  # base signal proc./machine learning library
    ],

    entry_points={
      'console_scripts': [
        # for tests or db creation, enable the following line:
        #'replay_manager.py = bob.db.script.dbmanage:main',
        ],

      # declare the database to bob
      'bob.db': [
        'casia_fasd = casia_fasd.db',
        ],

      # declare tests to bob
      'bob.test': [
        'casia_fasd = casia_fasd.test',
        ],
      },

)
