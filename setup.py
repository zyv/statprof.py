#!/usr/bin/env python

import os
from setuptools import find_packages, setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "statprof",
    version = "0.1.1",
    author = "Bryan O'Sullivan",
    author_email = "bos@serpentine.com",
    description = ("Statistical profiling for Python"),
    license = "LGPL",
    keywords = "profiling",
    url = "http://packages.python.org/statprof",
    py_modules = ['statprof'],
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    ],
)
