#!/usr/bin/env python

import sys, os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requirements = []
try:
    import pyspatialite
except ImportError as e:
    install_requirements.append('pyspatialite')


classifiers = [
               'Development Status :: 4 - Beta',
               'Intended Audience :: Developers',
               'Intended Audience :: Science/Research',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Topic :: Scientific/Engineering :: GIS',
               ]


setup(name='libfeatureserver',
      version='0.1',
      description='',
      #long_description=read('doc/Readme.txt'),
      author='libfeatureserver (iocast)',
      author_email='',
      url='',
      
      packages=find_packages(exclude=["doc", "tests"]),
      include_package_data=True,
      
      install_requires=install_requirements,
      
      test_suite = 'tests.test_suite',
      
      zip_safe=False,
      license="MIT",
      classifiers=classifiers
)
