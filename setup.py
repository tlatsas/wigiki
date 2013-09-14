# -*- coding: utf-8 -*-
"""
wigiki
------

A simple static site generator that uses Github's Gists as pages.


Installation
------------

    pip install wigiki


Usage
-----

Run with:

    wigiki

For all available options use:

    wigiki --help

Example:

    wigiki -t ./templates/default -o ./_site -u /

"""

from setuptools import setup
import wigiki

setup(
    name="wigiki",
    version=wigiki.__version__,
    description=wigiki.__doc__.strip(),
    long_description=__doc__,
    url="https://github.com/tlatsas/wigiki",
    author="Tasos Latsas",
    author_email="tlatsas@gmx.com",
    license="MIT",
    packages=["wigiki"],
    entry_points = {
        "console_scripts": [
            "wigiki = wigiki.__main__:main",
        ],
    },
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet",
    ],
)
