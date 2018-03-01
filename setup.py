#!/usr/bin/env python

from distutils.core import setup

setup(name='aias',
      version='0.0.1',
      description='Text based adventure game with a procedural generation scenario. And everything takes place in a giant seashell.',
      author='Pierre-Yves "Pirata" Martin',
      author_email='pym.aldebaran@gmail.comt',
      licence='GPLv3',
      url='https://github.com/pymaldebaran/aias',
      packages=['aias'],
      install_requires=['begins'],
      tests_requires=['pytest', 'pytest-bdd']
     )