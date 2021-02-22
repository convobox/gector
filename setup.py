#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# Copy from the setup.py in ParlAI
from setuptools import setup, find_packages

VERSION = '1.0.0'
if __name__ == '__main__':
    setup(
        name='gector',
        version=VERSION,
        packages=find_packages(), # only for .py files if __init__.py file is included
        include_package_data=True,
        package_data={'': ['data/*.txt', 'data/output_vocabulary/*.txt']}, # relative path of the dir utils
    )

