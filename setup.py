#!/usr/bin/env python
from setuptools import setup

setup(
    name="statprof",
    version="0.1.2",
    author="Bryan O'Sullivan",
    author_email="bos@serpentine.com",
    description="Statistical profiling for Python",
    license="LGPL",
    keywords="profiling",
    url="http://packages.python.org/statprof",
    py_modules=['statprof'],
    long_description=open('README.rst').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    ],
)
