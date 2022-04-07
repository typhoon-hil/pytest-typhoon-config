#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-typhoon-config',
    version='1.0.0',
    author='Branko Milosavljevic',
    author_email='branko@typhoon-hil.com',
    maintainer='Branko Milosavljevic',
    maintainer_email='branko@typhoon-hil.com',
    license='MIT',
    url='https://github.com/typhoon-hil/pytest-typhoon-config',
    description='A Typhoon HIL plugin that facilitates test ' +
        'parameter configuration at runtime',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=['tytest.config'],
    python_requires='>=3.6',
    install_requires=[
        'pytest>=6.2.5',
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'tytest = tytest.config.plugin',
        ],
    },
)
