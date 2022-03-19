# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Tim Cocks for CircuitPython Organization
#
# SPDX-License-Identifier: MIT

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    # CircuitPython Org Bundle Information
    name="circuitpython-vectorio-helpers",
    use_scm_version={
        # This is needed for the PyPI version munging in the Github Actions release.yml
        "git_describe_command": "git describe --tags --long",
        "local_scheme": "no-local-version",
    },
    setup_requires=["setuptools_scm"],
    description="A collection of shape widgets and other helpers for CircuitPython vectorio module",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    # The project's main homepage.
    url="https://github.com/circuitpython/CircuitPython_Org_VectorIO_Helpers.git",
    # Author details
    author="Tim Cocks",
    author_email="",  # TODO: Add your email here
    install_requires=[
        "Adafruit-Blinka",
    ],
    # Choose your license
    license="MIT",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    # What does your project relate to?
    keywords="adafruit blinka circuitpython micropython vectorio_helpers vector vectorio "
    "displayio display shapes",
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=["vectorio_helpers"],
)
