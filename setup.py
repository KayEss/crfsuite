#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension
import os
import sys


def get_rootdir():
    return os.path.dirname(__file__)
def get_includedir():
    return os.path.join(get_rootdir(), 'include')
def get_librarydir():
    return os.path.join(get_rootdir(), 'lib')


crfsuite_module = Extension(
        '_crfsuite',
        sources = [
                'swig/crfsuite.cpp',
                'swig/python/export_wrap.cpp',
            ],
        swig_opts=['-c++', '-Iinclude'],
        include_dirs=['include'],
        extra_link_args=['-shared'],
        language='c++',
    )

setup(
        name = 'crfsuite',
        version = '0.12',
        author = 'Naoaki Okazaki',
        description = """CRFSuite Python module""",
        ext_modules = [crfsuite_module],
        py_modules = ["crfsuite"],
    )

