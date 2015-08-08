__author__ = 'Zhichao HAN'

import os
from setuptools import setup, find_packages


version = '0.1.0'

README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read()


setup(name='mview',
      version=version,
      description=('Package to show graphic view of pandas.DataFrame.'),
      long_description=long_description,
      classifiers=[
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Visualization',
        ],
      keywords='matrix view data frame',
      author='Zhichao HAN',
      author_email='hanzhichao2000@foxmail.com',
      license='LGPL',
      packages=find_packages(),
      install_requires=['pandas']
      )