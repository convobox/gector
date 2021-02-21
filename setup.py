#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# Copy from the setup.py in ParlAI

from setuptools import setup, find_packages

VERSION = '1.0.0'

with open('README.md', encoding="utf8") as f:
    # strip the header and badges etc
    readme = f.read().split('--------------------')[-1]

if __name__ == '__main__':
    setup(
        name='gector',
        version=VERSION,
        description='facebook ai gector repo.',
        long_description=readme,
        url='https://github.com/convobox/gector',
#        python_requires='>=3.7',
        packages=find_packages(exclude=('data', 'docs', 'tests')),
        entry_points={
            "console_scripts": ["gector=gector.__main__:main"],
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Natural Language :: English",
        ],
    )

