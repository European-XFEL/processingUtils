#!/usr/bin/env python

from setuptools import find_packages, setup

setup(name='processing_utils',
      version='',
      description='Data processing utils',
      author='Andrea Parenti',
      author_email='andrea.parenti@xfel.eu',
      url='http://www.xfel.eu/',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      )
