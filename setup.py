# -*- coding: utf-8 -*-
"""
wigiki
------

Static html site generator that uses Github's Gists as pages.


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

    wigiki -t templates/default -o _site

"""

import os
import sys
from setuptools import setup
import wigiki

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

# default template files
tpl_path = "wigiki"
if os.name is 'posix':
    if sys.prefix.split(os.sep)[1] == 'usr':
        tpl_path = "/usr/share/wigiki"

tpl_files = [
    (os.path.join(tpl_path, "templates", "default"),
        ["templates/default/index.html",
        "templates/default/base.html",
        "templates/default/page.html"]
    ),
    (os.path.join(tpl_path, "templates", "default", "assets"),
        ["templates/default/assets/style.css"]
    )
]

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
    install_requires=requirements,
    entry_points = {
        "console_scripts": [
            "wigiki = wigiki.__main__:main",
        ],
    },
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet",
    ],
    data_files=tpl_files
)
