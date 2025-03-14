#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""This module is the install script for the `az capi` commmand-line extension."""

from codecs import open as codec_open
from setuptools import setup, find_packages
try:
    from azure_bdist_wheel import cmdclass  # pylint: disable=unused-import
except ImportError:
    from distutils import log as logger
    logger.warn("Wheel is not available, disabling bdist_wheel hook")

# Confirm this is the right version number you want and it matches your
# HISTORY.rst entry.
VERSION = '0.0.3'

# The full list of classifiers is available at
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: MIT License',
]

# Add any additional SDK dependencies here
DEPENDENCIES = [
    'azure-cli-core',
    "Jinja2",
    "MarkupSafe"
]

with codec_open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()
with codec_open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name='capi',
    version=VERSION,
    description='Microsoft Azure Command-Line Tools Cluster API Extension',
    author='Microsoft Corporation',
    author_email='Matt.Boersma@microsoft.com',
    url='https://github.com/Azure/azure-capi-cli-extension',
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    package_data={'azext_capi': ['azext_metadata.json', 'templates/*']},
    include_package_data=True,
)
