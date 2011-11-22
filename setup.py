#!/usr/bin/env python

"""
setup.py file for SWIG example
"""

from distutils.core import setup, Extension
import os
import os.path
import sys


def get_rootdir():
    return '/home/users/okazaki/local'
def get_includedir():
    return os.path.join(get_rootdir(), 'include')
def get_librarydir():
    return os.path.join(get_rootdir(), 'lib')

os.environ['CC'] = 'g++'
os.environ['CXX'] = 'g++'
os.environ['CPP'] = 'g++'
os.environ['LDSHARED'] = 'g++'


crfsuite_module = Extension(
        '_crfsuite',
        sources = [
                'swig/crfsuite.cpp',
                'swig/python/export_wrap.cpp',
            ],
        extra_link_args=['-shared'],
        libraries=['crfsuite'],
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

