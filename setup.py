#!/usr/bin/env python

from distutils.core import setup

# Script inspired from https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/
setup(name='aias',
      version='0.0.1',
      description='Text based adventure game with a procedural generation scenario. And everything takes place in a giant seashell.',
      author='Pierre-Yves "Pirata" Martin',
      author_email='pym.aldebaran@gmail.comt',
      licence='GPLv3',
      url='https://github.com/pymaldebaran/aias',
      packages=['aias'],
      install_requires=['begins'],
      tests_requires=['pytest', 'pytest-bdd'],
      entry_point={
            'console_scripts': [
                  'aias = aias.__main__:main'
            ]
      }
     )